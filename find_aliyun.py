# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "rb") as f:
    raw = f.read()

# 搜索aliyun附近的内容
idx = raw.find(b"aliyun")
if idx > 0:
    snippet = raw[idx-200:idx+200]
    print("FOUND aliyun context:")
    print(snippet.decode("utf-8", errors="replace"))
else:
    print("aliyun NOT found in raw bytes")
