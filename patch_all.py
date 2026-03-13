# -*- coding: utf-8 -*-
"""
v3.12.1 最终修改包
1. 页脚: 内容建议 / 技术支持 / 加入校友会(微信：Aclouder)
2. SKILLS: 增加复旦大学科研武器库备注
3. H3C MegaCube: 添加到CLAW集合
4. 品牌: OpenClaw AI -> Claw AI 智能助手平台
"""
import re

path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

results = []

# ===== 1. 修改页脚 =====
old_footer = """  <div>© 2025 复旦大学未来信息创新学院工程管理校友会</div>
  <div style="margin-top:4px;font-size:10px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>"""

new_footer = """  <div>© 2025 复旦大学未来信息创新学院工程管理校友会</div>
  <div style="margin-top:8px;font-size:12px;color:var(--text2)">内容建议 / 技术支持 / 加入校友会（微信：Aclouder）</div>
  <div style="margin-top:4px;font-size:10px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>"""

if old_footer in c:
    c = c.replace(old_footer, new_footer)
    results.append("[1] 页脚: 已添加'加入校友会（微信：Aclouder）'")
else:
    results.append("[1] 页脚: WARNING 未匹配")

# ===== 2. SKILLS增加备注 =====
old_skills_header = """    <div class="section-header">
      <h2>📚 复旦大学百万SKILLS</h2>
      <p style="color:var(--text2);font-size:13px">一键搜索、一键直达 fudankw.cn 技能库</p>
    </div>"""

new_skills_header = """    <div class="section-header">
      <h2>📚 复旦大学百万SKILLS</h2>
      <p style="color:var(--text2);font-size:13px">复旦大学科研武器库 · 肖仰华团队DataHub平台 · 百万计SKILLS资源库</p>
      <p style="color:var(--accent);font-size:12px;margin-top:4px">一键搜索、一键直达 fudankw.cn 技能库</p>
    </div>"""

if old_skills_header in c:
    c = c.replace(old_skills_header, new_skills_header)
    results.append("[2] SKILLS: 已添加科研武器库备注")
else:
    results.append("[2] SKILLS: WARNING 未匹配")

# ===== 3. 添加H3C MegaCube =====
# 在阿里云CoPaw之后插入
h3c_entry = "  {name:'H3C盒装大龙虾',icon:'🖥️',desc:'新华三LinSeer MegaCube桌面级AI工作站，GB10芯片，支持200B推理/70B微调',url:'https://www.h3c.com/cn/Products_And_Solution/IntelligentTerminalProducts/Star_Products/LinSeer_Magic_Cube/',doc:'https://www.h3c.com/cn/Products_And_Solution/IntelligentTerminalProducts/Star_Products/LinSeer_Magic_Cube/',open:false,hot:true},"

if "H3C" not in c and "阿里云CoPaw" in c:
    # 找到阿里云CoPaw行，在其后插入
    idx = c.find("阿里云CoPaw")
    if idx > 0:
        end_line = c.find("\n", idx)
        c = c[:end_line+1] + h3c_entry + "\n" + c[end_line+1:]
        results.append("[3] H3C: 已添加盒装大龙虾")
    else:
        results.append("[3] H3C: WARNING 未找到插入位置")
elif "H3C" in c:
    results.append("[3] H3C: 已存在")

# ===== 4. 品牌替换 =====
c = c.replace("OpenClaw AI 全网比价智能平台", "Claw AI 智能助手平台")
c = c.replace("© 2025 复旦大学", "© 2026 Claw AI 智能助手平台 · 复旦大学")
results.append("[4] 品牌: 已更新为'Claw AI 智能助手平台'")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 验证 =====
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print("=" * 60)
print("修改结果:")
for r in results:
    print(f"  {r}")
print("=" * 60)
print(f"验证 加入校友会: {'PASS' if '加入校友会' in v else 'FAIL'}")
print(f"验证 微信Aclouder: {'PASS' if '微信：Aclouder' in v else 'FAIL'}")
print(f"验证 科研武器库: {'PASS' if '科研武器库' in v else 'FAIL'}")
print(f"验证 肖仰华团队: {'PASS' if '肖仰华' in v else 'FAIL'}")
print(f"验证 H3C: {'PASS' if 'H3C' in v else 'FAIL'}")
print(f"验证 Claw AI: {'PASS' if 'Claw AI 智能助手平台' in v else 'FAIL'}")
print(f"验证 2026: {'PASS' if '2026' in v else 'FAIL'}")
