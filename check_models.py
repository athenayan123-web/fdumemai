# -*- coding: utf-8 -*-
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 查找所有model字段
for m in re.findall(r"model:'[^']*'", c):
    print("MODEL:", m)

# 查找图灵链接
for m in re.findall(r"turingcm[^'\"]*", c):
    print("TURING:", m)

# 查找GPU url字段
for m in re.findall(r"url:'[^']*turing[^']*'", c):
    print("GPU_URL:", m)
