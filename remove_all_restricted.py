# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 移除所有restricted-overlay
lines = c.split('\n')
new_lines = []
for line in lines:
    if 'restricted-overlay' in line and 'trend-content' in line:
        # 只移除trend-content的restricted
        line = line.replace('class="restricted-overlay"', '')
    new_lines.append(line)

c = '\n'.join(new_lines)

# 确保趋势内容可见
if 'id="trend-content"' in c:
    c = c.replace('id="trend-content"', 'id="trend-content" style="display:block"')

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"restricted-overlay in trend: {'PASS' if 'trend-content' in v and 'restricted-overlay' not in v else 'FAIL'}")
print(f"AI实战案例: {'PASS' if 'AI实战案例' in v else 'FAIL'}")
