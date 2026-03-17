# -*- coding: utf-8 -*-
"""
修改：
1. AI实战案例模块加锁（同SKILLS一起锁住）
2. 锁定提示改为"注册后解锁复旦大学百万SKILLS和实战案例集"
3. 页脚显示"Claw AI 智能助手平台"
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

results = []

# ===== 1. SKILLS锁定提示更新 =====
old_skills_lock = "注册后解锁复旦大学百万SKILLS"
new_skills_lock = "注册后解锁复旦大学百万SKILLS和实战案例集"
c = c.replace(old_skills_lock, new_skills_lock)
results.append("[1] SKILLS锁定提示已更新")

# ===== 2. AI实战案例加锁 =====
# 找到section-trends的内容区域，添加锁定遮罩
old_trends_header = """      <p style="color:var(--text2);font-size:13px;margin-top:4px">Claw AI 团队真实项目落地经验分享</p>
    </div>
    <div id="trend-content\""""

new_trends_header = """      <p style="color:var(--text2);font-size:13px;margin-top:4px">Claw AI 团队真实项目落地经验分享</p>
    </div>
    <!-- 未登录锁定遮罩 -->
    <div id="trends-locked" style="text-align:center;padding:60px 20px;background:var(--card);border:1px solid var(--border);border-radius:var(--r)">
      <div style="font-size:64px;margin-bottom:20px">🔒</div>
      <h3 style="margin-bottom:12px;font-size:20px;color:var(--text)">注册后解锁复旦大学百万SKILLS和实战案例集</h3>
      <p style="color:var(--text2);margin-bottom:24px;font-size:14px;max-width:400px;margin-left:auto;margin-right:auto">注册即可免费访问AI实战案例集和全部技能库</p>
      <div style="display:flex;gap:12px;justify-content:center">
        <button onclick="openModal('modal-register')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;cursor:pointer;font-weight:700">免费注册</button>
        <button onclick="openModal('modal-login')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:transparent;color:var(--accent);border:1px solid rgba(102,126,234,.4);cursor:pointer;font-weight:700">已有账号登录</button>
      </div>
    </div>
    <!-- 已登录内容（默认隐藏） -->
    <div id="trends-content" style="display:none">
    <div id="trend-content\""""

if old_trends_header in c:
    c = c.replace(old_trends_header, new_trends_header)
    results.append("[2] AI实战案例锁定遮罩已添加")
else:
    results.append("[2] WARNING: 未找到trends header")

# 找到trends section的结束div，添加闭合
# 在section-trends的最后一个</div>之前添加闭合</div>
old_trends_end = "  </div>\n\n</div>\n\n<!-- ===== 底栏 ===== -->"
new_trends_end = "  </div>\n  </div>\n\n</div>\n\n<!-- ===== 底栏 ===== -->"
if old_trends_end in c:
    c = c.replace(old_trends_end, new_trends_end)
    results.append("[2] trends-content闭合div已添加")

# ===== 3. 更新updateSkillsVisibility函数 =====
old_func = """function updateSkillsVisibility() {
  var locked = document.getElementById('skills-locked');
  var content = document.getElementById('skills-content');
  if (!locked || !content) return;
  if (user) { locked.style.display='none'; content.style.display='block'; }
  else { locked.style.display='block'; content.style.display='none'; }
}"""

new_func = """function updateSkillsVisibility() {
  var locked = document.getElementById('skills-locked');
  var content = document.getElementById('skills-content');
  if (locked && content) {
    if (user) { locked.style.display='none'; content.style.display='block'; }
    else { locked.style.display='block'; content.style.display='none'; }
  }
  var trendsLocked = document.getElementById('trends-locked');
  var trendsContent = document.getElementById('trends-content');
  if (trendsLocked && trendsContent) {
    if (user) { trendsLocked.style.display='none'; trendsContent.style.display='block'; }
    else { trendsLocked.style.display='block'; trendsContent.style.display='none'; }
  }
}"""

if old_func in c:
    c = c.replace(old_func, new_func)
    results.append("[3] updateSkillsVisibility已更新（含trends锁定）")
else:
    results.append("[3] WARNING: 未找到updateSkillsVisibility函数")

# ===== 4. 页脚更新 =====
old_footer = "© 2026 Claw AI 智能助手平台"
if old_footer in c:
    results.append("[4] 页脚已正确显示'Claw AI 智能助手平台'")
else:
    # 查找并替换
    old_f2 = "© 2025 复旦大学未来信息创新学院工程管理校友会"
    new_f2 = "© 2026 Claw AI 智能助手平台"
    if old_f2 in c:
        c = c.replace(old_f2, new_f2)
        results.append("[4] 页脚已更新为'Claw AI 智能助手平台'")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 验证 =====
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print("=" * 60)
for r in results:
    print(f"  {r}")
print("=" * 60)
print(f"验证 SKILLS+实战案例锁定提示: {'PASS' if '百万SKILLS和实战案例集' in v else 'FAIL'}")
print(f"验证 trends-locked: {'PASS' if 'trends-locked' in v else 'FAIL'}")
print(f"验证 trends-content: {'PASS' if 'trends-content' in v else 'FAIL'}")
print(f"验证 updateSkillsVisibility含trends: {'PASS' if 'trendsLocked' in v else 'FAIL'}")
print(f"验证 页脚Claw AI: {'PASS' if 'Claw AI 智能助手平台' in v else 'FAIL'}")
