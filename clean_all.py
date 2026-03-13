# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 查找所有包含Aclouder或微信的内容并移除
lines = c.split('\n')
new_lines = []
for line in lines:
    if 'Aclouder' in line or '微信' in line or '💬' in line:
        print(f"REMOVE: {line[:80]}...")
        continue
    new_lines.append(line)

c = '\n'.join(new_lines)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print(f"\n验证 Aclouder: {'PASS' if 'Aclouder' not in v else 'FAIL'}")
print(f"验证 微信: {'PASS' if '微信' not in v else 'FAIL'}")
print(f"验证 💬: {'PASS' if '💬' not in v else 'FAIL'}")
