# -*- coding: utf-8 -*-
"""
v3.12.1 快速修改：
1. Claw集增加H3C盒装大龙虾
2. 底部增加"内容建议/技术支持/加入我们(微信：Aclouder)"
"""
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

results = []

# ===== 1. Claw集增加H3C盒装大龙虾 =====
# 在飞书龙虾之前插入
lines = c.split("\n")
inserted = False
for i, line in enumerate(lines):
    if "飞书龙虾" in line and "name:" in line:
        h3c_line = "  {name:'H3C盒装大龙虾',icon:'📦',desc:'新华三MegaCube一体机，开箱即用的AI算力盒子，适合中小企业私有化部署',url:'https://www.h3c.com/cn/Products_And_Solution/IntelligentTerminalProducts/Star_Products/LinSeer_Magic_Cube/',doc:'https://www.h3c.com/cn/Products_And_Solution/IntelligentTerminalProducts/Star_Products/LinSeer_Magic_Cube/',open:false,hot:true},"
        lines.insert(i, h3c_line)
        inserted = True
        results.append("[1] H3C盒装大龙虾: 已添加(飞书龙虾之前)")
        break

if not inserted:
    # 备用：在CLAW_DATA的];之前插入
    for i, line in enumerate(lines):
        if "const CLAW_DATA" in line:
            # 找到这个数组的];
            for j in range(i, min(i+30, len(lines))):
                if lines[j].strip() == "];":
                    h3c_line = "  {name:'H3C盒装大龙虾',icon:'📦',desc:'新华三MegaCube一体机，开箱即用的AI算力盒子，适合中小企业私有化部署',url:'https://www.h3c.com/cn/Products_And_Solution/IntelligentTerminalProducts/Star_Products/LinSeer_Magic_Cube/',doc:'https://www.h3c.com/cn/Products_And_Solution/IntelligentTerminalProducts/Star_Products/LinSeer_Magic_Cube/',open:false,hot:true},"
                    lines.insert(j, h3c_line)
                    inserted = True
                    results.append("[1] H3C盒装大龙虾: 已添加(CLAW_DATA末尾)")
                    break
            break

if not inserted:
    results.append("[1] H3C盒装大龙虾: FAIL 未找到插入位置")

c = "\n".join(lines)

# ===== 2. 底部增加文字 =====
old_footer = "OpenClaw AI 全网比价智能平台 · 数据来源于各厂商公开信息，仅供参考"
new_footer = "OpenClaw AI 全网比价智能平台 · 数据来源于各厂商公开信息，仅供参考</div>\n  <div style=\"margin-top:8px;font-size:12px;color:var(--text2)\">内容建议 / 技术支持 / 加入我们（微信：Aclouder）"

if old_footer in c:
    c = c.replace(old_footer, new_footer)
    results.append("[2] 底部文字: 已添加(内容建议/技术支持/加入我们)")
else:
    results.append("[2] 底部文字: FAIL 未找到页脚")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 验证 =====
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print("=" * 50)
print("修改结果:")
for r in results:
    print(f"  {r}")
print("=" * 50)
print(f"验证 H3C: {'PASS' if 'H3C' in v and 'MegaCube' in v else 'FAIL'}")
print(f"验证 Aclouder: {'PASS' if 'Aclouder' in v else 'FAIL'}")
print(f"验证 内容建议: {'PASS' if '内容建议' in v else 'FAIL'}")
