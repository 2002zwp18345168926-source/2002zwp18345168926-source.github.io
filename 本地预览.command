#!/bin/zsh
cd "$(dirname "$0")"
open http://localhost:1313/
hugo server -D
