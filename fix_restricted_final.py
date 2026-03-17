# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 找到trend-content行
lines = content.split("\n")
for i, line in enumerate(lines):
    if "trend-content" in line:
        print(f"Line {i+1}: {line[:200]}")
        # 替换这一行
        if "restricted-overlay" in line:
            lines[i] = line.replace('class="restricted-overlay"', '').replace('restricted-overlay', '')
            print("  -> Fixed")

# 写回
with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# 验证
with open(path, "r", encoding="utf-8") as f:
    content2 = f.read()
    
if "trend-content" in content2 and "restricted-overlay" not in content2:
    print("\nFinal check: PASS - restricted-overlay removed from trend-content")
else:
    print("\nFinal check: FAIL - restricted-overlay still exists")
    
print(f"AI实战案例: {'PASS' if 'AI实战案例' in content2 else 'FAIL'}")
