from pathlib import Path
import base64
import html
import mimetypes

photo_dir = Path.home() / "Pictures" / "private-blog-album"
output_file = Path(".private-build/index.html")

supported = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

if not photo_dir.exists():
    raise SystemExit(f"找不到照片目录：{photo_dir}")

photos = sorted(
    p for p in photo_dir.iterdir()
    if p.is_file() and p.suffix.lower() in supported
)

if not photos:
    raise SystemExit(
        f"{photo_dir} 中没有找到 jpg、jpeg、png、webp 或 gif 图片"
    )

cards = []

for photo in photos:
    mime_type = mimetypes.guess_type(photo.name)[0]

    if not mime_type or not mime_type.startswith("image/"):
        continue

    encoded = base64.b64encode(photo.read_bytes()).decode("ascii")
    caption = html.escape(
        photo.stem.replace("_", " ").replace("-", " ")
    )

    cards.append(
        f"""
        <figure class="photo-card">
          <img
            src="data:{mime_type};base64,{encoded}"
            alt="{caption}"
            loading="lazy"
          >
          <figcaption>{caption}</figcaption>
        </figure>
        """
    )

page = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1"
  >
  <title>我们的私密相册</title>

  <style>
    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      background: #161616;
      color: #f7f7f7;
      font-family:
        -apple-system, BlinkMacSystemFont,
        "PingFang SC", "Microsoft YaHei", sans-serif;
    }}

    .page {{
      width: min(1120px, calc(100% - 32px));
      margin: 0 auto;
      padding: 42px 0 70px;
    }}

    h1 {{
      margin-bottom: 8px;
      font-size: clamp(28px, 5vw, 48px);
    }}

    .description {{
      color: #c8c8c8;
      margin-bottom: 32px;
    }}

    .back-link {{
      display: inline-block;
      margin-bottom: 26px;
      color: #fa8b84;
      text-decoration: none;
    }}

    .gallery {{
      display: grid;
      grid-template-columns:
        repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }}

    .photo-card {{
      margin: 0;
      overflow: hidden;
      background: #222;
      border-radius: 14px;
    }}

    .photo-card img {{
      display: block;
      width: 100%;
      height: 320px;
      object-fit: cover;
    }}

    .photo-card figcaption {{
      padding: 12px 14px;
      color: #d7d7d7;
      font-size: 14px;
    }}

    @media (max-width: 600px) {{
      .photo-card img {{
        height: 300px;
      }}
    }}
  </style>
</head>

<body>
  <main class="page">
    <a class="back-link" href="/">← 返回博客首页</a>

    <h1>我们的私密相册</h1>
    <p class="description">
      一些只想和重要的人分享的照片。
    </p>

    <section class="gallery">
      {''.join(cards)}
    </section>
  </main>
</body>
</html>
"""

output_file.parent.mkdir(parents=True, exist_ok=True)
output_file.write_text(page, encoding="utf-8")

size_mb = output_file.stat().st_size / 1024 / 1024

print(f"已生成：{output_file}")
print(f"照片数量：{len(cards)}")
print(f"未加密文件大小：{size_mb:.1f} MB")
