# -*- coding: utf-8 -*-
import re

path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. 在猎豹EasyClaw后面添加阿里云免费部署
old = "open:false},\n];\n\n// ===== \u6e32\u67d3\u51fd\u6570 ====="
# 找猎豹EasyClaw那行
idx = content.find("EasyClaw")
if idx == -1:
    print("ERROR: EasyClaw not found")
else:
    # 找到这行末尾的 }
    end_line = content.find("\n", idx)
    # 找到 ]; 的位置
    bracket = content.find("];", end_line)
    if bracket == -1:
        print("ERROR: ]; not found after EasyClaw")
    else:
        new_line = """\n  {name:'\\u963f\\u91cc\\u4e91\\u514d\\u8d39\\u90e8\\u7f72',icon:'\\u2601\\ufe0f',desc:'\\u96f6\\u57fa\\u7840\\u5c0f\\u767d\\u4e00\\u952e\\u90e8\\u7f72OpenClaw\\u5230\\u963f\\u91cc\\u4e91ECS\\uff0c\\u5168\\u7a0b\\u56fe\\u6587\\u6559\\u7a0b\\uff0c\\u514d\\u8d39\\u989d\\u5ea6\\u53ef\\u7528',url:'https://free.aliyun.com/',doc:'https://help.aliyun.com/zh/ecs/getting-started/',open:true,hot:true},"""
        content = content[:bracket] + new_line + "\n" + content[bracket:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS: Added aliyun entry")

# Verify
with open(path, "r", encoding="utf-8") as f:
    c2 = f.read()
if "free.aliyun.com" in c2:
    print("VERIFIED: aliyun entry exists")
else:
    print("FAILED: aliyun entry not found")
