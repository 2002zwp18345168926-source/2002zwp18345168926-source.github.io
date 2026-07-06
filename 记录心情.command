#!/bin/zsh
cd "$(dirname "$0")"
python3 scripts/mood.py
echo
read "?操作结束，按回车关闭窗口……"
