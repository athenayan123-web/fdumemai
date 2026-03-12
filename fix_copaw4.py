# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "rb") as f:
    raw = f.read()

c = raw.decode("utf-8")

# 搜索CLAW_DATA中包含aliyun的那一行
import re
# 找到包含copaw的整行
lines = c.split("\n")
for i, line in enumerate(lines):
    if "copaw" in line.lower() or ("aliyun" in line and "name:" in line):
        print(f"Line {i}: {line[:120]}...")
        # 替换这一行
        new_line = line
        # 替换name
        new_line = re.sub(r"name:'[^']*'", "name:'阿里云CoPaw'", new_line, count=1)
        # 替换desc
        new_line = re.sub(r"desc:'[^']*'", "desc:'阿里云官方AI编程助手CoPaw，一键部署，免费额度可用'", new_line, count=1)
        lines[i] = new_line
        print(f"  -> {new_line[:120]}...")

c = "\n".join(lines)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 CoPaw: {'PASS' if 'CoPaw' in v else 'FAIL'}")
print(f"验证 URL: {'PASS' if 'aliyun.com/solution/tech-solution/copaw' in v else 'FAIL'}")
print(f"验证 hot: {'PASS' if 'hot:true' in v else 'FAIL'}")
