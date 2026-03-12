# -*- coding: utf-8 -*-
import json

path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 替换模型版本
replacements = [
    ("GPT-5.2", "GPT-5.4"),
    ("GPT-5.1", "GPT-5.3"),
    ("Claude 4 Sonnet", "Claude Sonnet 4.6"),
    ("Gemini 2.5 Pro", "Gemini 3.2 Pro"),
    ("Gemini 2.5 Flash", "Gemini 3.2 Flash"),
    ("Gemini 2.0 Flash", "Gemini 3.0 Flash"),
]

for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"REPLACED: '{old}' -> '{new}' ({count} occurrences)")
    else:
        print(f"NOT FOUND: '{old}'")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# Verify
with open(path, "r", encoding="utf-8") as f:
    c2 = f.read()
for _, new in replacements:
    if new in c2:
        print(f"VERIFIED: '{new}' exists")
    else:
        print(f"MISSING: '{new}'")
