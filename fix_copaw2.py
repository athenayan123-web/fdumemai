# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 查找实际的阿里云条目
import re
matches = re.findall(r"name:'[^']*阿里[^']*'", c)
print("找到阿里相关:", matches)

# 替换名称
for m in matches:
    c = c.replace(m, "name:'阿里云CoPaw'")
    print(f"替换: {m} -> name:'阿里云CoPaw'")

# 替换描述
descs = re.findall(r"(name:'阿里云CoPaw'[^}]*desc:')([^']*)'", c)
for full, desc in descs:
    old = full + desc + "'"
    new = full + "阿里云官方AI编程助手，一键部署，免费额度可用" + "'"
    c = c.replace(old, new)
    print(f"描述更新: {desc[:30]}... -> 阿里云官方AI编程助手...")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证: CoPaw={'PASS' if 'CoPaw' in v else 'FAIL'}")
print(f"验证: aliyun.com/solution={'PASS' if 'aliyun.com/solution' in v else 'FAIL'}")
