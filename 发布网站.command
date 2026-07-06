#!/bin/zsh
cd "$(dirname "$0")"

echo "正在构建网站……"
rm -rf docs

if ! hugo --gc --minify --destination docs; then
  echo "网站构建失败，请检查上面的错误。"
  read "?按回车关闭窗口……"
  exit 1
fi

touch docs/.nojekyll

git add -A

if git diff --cached --quiet; then
  echo "没有发现需要发布的新内容。"
  read "?按回车关闭窗口……"
  exit 0
fi

commit_message="Update website $(date '+%Y-%m-%d %H:%M')"

git commit -m "$commit_message"

if git push origin main; then
  echo
  echo "网站发布成功。"
else
  echo
  echo "推送失败，请检查网络后重新双击本文件。"
fi

read "?按回车关闭窗口……"
