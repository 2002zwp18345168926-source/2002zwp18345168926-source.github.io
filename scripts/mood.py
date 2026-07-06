#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path


DATA_FILE = Path("static/data/moods.json")

MOODS = {
    "1": ("great", "超开心", "#e85d75"),
    "2": ("good", "开心", "#f28c8c"),
    "3": ("calm", "平静", "#f6c1c1"),
    "4": ("tired", "疲惫", "#a8b8d8"),
    "5": ("sad", "难过", "#7d88a8"),
}


def load_records() -> dict[str, dict[str, str]]:
    if not DATA_FILE.exists():
        return {}

    try:
        content = DATA_FILE.read_text(encoding="utf-8").strip()

        if not content:
            return {}

        loaded = json.loads(content)

        if not isinstance(loaded, dict):
            raise ValueError("心情数据必须是 JSON 对象")

        return loaded

    except (json.JSONDecodeError, ValueError) as error:
        raise SystemExit(f"无法读取 {DATA_FILE}：{error}") from error


def ask_for_date() -> str:
    today = date.today().isoformat()

    while True:
        value = input(f"记录日期 [{today}]：").strip() or today

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("日期格式不正确，请使用 YYYY-MM-DD。")


def show_choices() -> None:
    print()
    print("请选择今天的心情：")
    print("1. ■ 超开心")
    print("2. ■ 开心")
    print("3. ■ 平静")
    print("4. ■ 疲惫")
    print("5. ■ 难过")
    print("0. 删除这一天的记录")
    print()


def main() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    records = load_records()
    selected_date = ask_for_date()

    show_choices()

    while True:
        choice = input("输入 0–5：").strip()

        if choice == "0":
            if selected_date in records:
                del records[selected_date]
                action = f"已删除 {selected_date} 的记录"
            else:
                action = f"{selected_date} 原本没有记录"
            break

        if choice in MOODS:
            mood_key, mood_label, _ = MOODS[choice]
            note = input("写一句当天的记录（可直接回车跳过）：").strip()

            records[selected_date] = {
                "mood": mood_key,
                "label": mood_label,
                "note": note,
            }

            action = (
                f"已记录 {selected_date}："
                f"{mood_label}"
                + (f"｜{note}" if note else "")
            )
            break

        print("请选择 0、1、2、3、4 或 5。")

    ordered_records = dict(sorted(records.items()))

    DATA_FILE.write_text(
        json.dumps(
            ordered_records,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print()
    print(action)
    print(f"数据已保存到：{DATA_FILE}")
    print()


if __name__ == "__main__":
    main()
