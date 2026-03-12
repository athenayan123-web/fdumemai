# -*- coding: utf-8 -*-
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 提取API_DATA完整内容
start = c.find("const API_DATA = [")
end = c.find("];", start) + 2
api_block = c[start:end]
print("=== 当前API_DATA ===")
print(api_block)
print(f"\n行数: {api_block.count(chr(10))}")

# 提取所有model
for m in re.findall(r"model:'([^']*)'", api_block):
    print(f"  MODEL: {m}")
