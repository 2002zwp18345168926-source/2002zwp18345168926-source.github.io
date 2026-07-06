#!/bin/zsh

cd "$(dirname "$0")" || exit 1

echo "================================"
echo "正在发布博客……"
echo "================================"

echo
echo "1. 同步 GitHub 最新内容"
if ! git pull --rebase --autostash origin main; then
  echo
  echo "同步失败，请检查网络或 Git 冲突。"
  read "?按回车关闭窗口……"
  exit 1
fi

echo
echo "2. 重新生成网站"
rm -rf docs

if ! hugo --gc --minify --destination docs; then
  echo
  echo "网站生成失败，请检查上方错误。"
  read "?按回车关闭窗口……"
  exit 1
fi

touch docs/.nojekyll

echo
echo "3. 检查修改"
git add -A

if git diff --cached --quiet; then
  echo
  echo "没有发现新的修改，不需要发布。"
  read "?按回车关闭窗口……"
  exit 0
fi

echo
echo "4. 保存修改"
git commit -m "Update website $(date '+%Y-%m-%d %H:%M')"

echo
echo "5. 上传到 GitHub"
if git push origin main; then
  echo
  echo "================================"
  echo "网站发布成功！"
  echo "================================"

  open "https://2002zwp18345168926-source.github.io/"
else
  echo
  echo "上传失败。通常是网络问题。"
  echo "修改已经保存在本地，网络恢复后重新双击本文件即可。"
fi

echo
read "?按回车关闭窗口……"
