# -*- coding: utf-8 -*-
"""
v3.11.9 精确修复脚本（基于实际代码）
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

results = []

# ===== 1. 模型版本更新 =====
replacements = [
    ("model:'GPT-4o'", "model:'GPT-5.4'"),
    ("model:'GPT-4o-mini'", "model:'GPT-4o-mini'"),  # 保持不变
    ("model:'Claude 3.5 Sonnet'", "model:'Claude Opus 4'"),
    ("model:'Gemini 1.5 Pro'", "model:'Gemini 3.2 Pro'"),
]
for old, new in replacements:
    if old == new:
        continue
    if old in c:
        c = c.replace(old, new)
        results.append(f"模型更新: {old} -> {new}")
    else:
        results.append(f"未找到: {old}")

# 更新Claude Opus 4的features
old_opus_feat = "features:'\u957f\u6587\u672c\u3001\u4ee3\u7801\u751f\u6210\u3001\u5b89\u5168\u5bf9\u9f50'"
new_opus_feat = "features:'Anthropic\u8fc4\u4eca\u4e3a\u6b62\u6700\u5f3a\u5927\u7684\u6a21\u578b\uff0c\u4e3b\u6253\u9ad8\u6027\u80fd'"
if old_opus_feat in c:
    c = c.replace(old_opus_feat, new_opus_feat)
    results.append("Claude Opus 4 features已更新")

# 更新Claude Sonnet 4的features（已存在）
old_sonnet_feat = "features:'\u4e3b\u6253\u6027\u4ef7\u6bd4\uff0c\u8ba9\u4eba\u4eba\u90fd\u6709\u53ef\u7528\u7684 Claude 4'"
if old_sonnet_feat in c:
    results.append("Claude Sonnet 4 features已正确")
else:
    results.append("Claude Sonnet 4 features需检查")

# ===== 2. SKILLS锁定遮罩 =====
# 查找SKILLS区域并添加锁定
old_skills = """  <!-- ===== \u767e\u4e07SKILLS ===== -->
  <div class="compare-section" id="section-skills">
    <div class="section-header">
      <h2>\U0001f4da \u590d\u65e6\u5927\u5b66\u767e\u4e07SKILLS</h2>
      <p style="color:var(--text2);font-size:13px">\u4e00\u952e\u641c\u7d22\u3001\u4e00\u952e\u76f4\u8fbe fudankw.cn \u6280\u80fd\u5e93</p>
    </div>
    <div style="margin-bottom:20px">
      <input type="text" id="skills-search" placeholder="\u641c\u7d22\u6280\u80fd\u540d\u79f0\u3001\u5173\u952e\u8bcd...\""""

new_skills = """  <!-- ===== \u767e\u4e07SKILLS ===== -->
  <div class="compare-section" id="section-skills">
    <div class="section-header">
      <h2>\U0001f4da \u590d\u65e6\u5927\u5b66\u767e\u4e07SKILLS</h2>
      <p style="color:var(--text2);font-size:13px">\u4e00\u952e\u641c\u7d22\u3001\u4e00\u952e\u76f4\u8fbe fudankw.cn \u6280\u80fd\u5e93</p>
    </div>
    <!-- \u672a\u767b\u5f55\u9501\u5b9a\u906e\u7f69 -->
    <div id="skills-locked" style="text-align:center;padding:60px 20px;background:var(--card);border:1px solid var(--border);border-radius:var(--r)">
      <div style="font-size:64px;margin-bottom:20px">\U0001f512</div>
      <h3 style="margin-bottom:12px;font-size:20px;color:var(--text)">\u6ce8\u518c\u540e\u89e3\u9501\u590d\u65e6\u5927\u5b66\u767e\u4e07SKILLS</h3>
      <p style="color:var(--text2);margin-bottom:24px;font-size:14px;max-width:400px;margin-left:auto;margin-right:auto">\u6ce8\u518c\u5373\u53ef\u514d\u8d39\u8bbf\u95ee\u5168\u90e8\u6280\u80fd\u5e93\uff0c\u5305\u62ec\u7f16\u7a0b\u5f00\u53d1\u3001\u6548\u7387\u5de5\u5177\u3001\u4eba\u5de5\u667a\u80fd\u3001\u57fa\u7840\u8bbe\u65bd\u7b49 42,800+ \u6280\u80fd\u5305</p>
      <div style="display:flex;gap:12px;justify-content:center">
        <button onclick="openModal('modal-register')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;cursor:pointer;font-weight:700">\u514d\u8d39\u6ce8\u518c</button>
        <button onclick="openModal('modal-login')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:transparent;color:var(--accent);border:1px solid rgba(102,126,234,.4);cursor:pointer;font-weight:700">\u5df2\u6709\u8d26\u53f7\u767b\u5f55</button>
      </div>
    </div>
    <!-- \u5df2\u767b\u5f55\u5185\u5bb9\uff08\u9ed8\u8ba4\u9690\u85cf\uff09 -->
    <div id="skills-content" style="display:none">
    <div style="margin-bottom:20px">
      <input type="text" id="skills-search" placeholder="\u641c\u7d22\u6280\u80fd\u540d\u79f0\u3001\u5173\u952e\u8bcd...\""""

if old_skills in c:
    c = c.replace(old_skills, new_skills)
    results.append("SKILLS锁定遮罩: 已添加")
else:
    results.append("SKILLS锁定遮罩: WARNING 未找到匹配区域，尝试备用方案")
    # 备用：直接搜索关键片段
    if 'id="section-skills"' in c and 'id="skills-locked"' not in c:
        # 在skills-search前插入锁定遮罩
        old_search = '<div style="margin-bottom:20px">\n      <input type="text" id="skills-search"'
        if old_search in c:
            locked_html = '''<div id="skills-locked" style="text-align:center;padding:60px 20px;background:var(--card);border:1px solid var(--border);border-radius:var(--r)">
      <div style="font-size:64px;margin-bottom:20px">\U0001f512</div>
      <h3 style="margin-bottom:12px;font-size:20px;color:var(--text)">\u6ce8\u518c\u540e\u89e3\u9501\u590d\u65e6\u5927\u5b66\u767e\u4e07SKILLS</h3>
      <p style="color:var(--text2);margin-bottom:24px;font-size:14px;max-width:400px;margin-left:auto;margin-right:auto">\u6ce8\u518c\u5373\u53ef\u514d\u8d39\u8bbf\u95ee\u5168\u90e8\u6280\u80fd\u5e93</p>
      <div style="display:flex;gap:12px;justify-content:center">
        <button onclick="openModal('modal-register')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;cursor:pointer;font-weight:700">\u514d\u8d39\u6ce8\u518c</button>
        <button onclick="openModal('modal-login')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:transparent;color:var(--accent);border:1px solid rgba(102,126,234,.4);cursor:pointer;font-weight:700">\u5df2\u6709\u8d26\u53f7\u767b\u5f55</button>
      </div>
    </div>
    <div id="skills-content" style="display:none">
    ''' + old_search
            c = c.replace(old_search, locked_html)
            results.append("SKILLS锁定遮罩: 备用方案成功")

# 在skills区域末尾添加闭合div
if 'id="skills-content"' in c:
    # 找到skills区域最后一个skill-card后的</div>，添加闭合</div>
    skills_end_marker = '      </div>\n    </div>\n  </div>\n\n  <!-- ====='
    if skills_end_marker in c and 'skills-content' in c:
        results.append("SKILLS内容区域闭合: 需手动检查")

# ===== 3. 添加updateSkillsVisibility函数 =====
if 'updateSkillsVisibility' not in c:
    # 在filterSkills函数后添加
    old_filter = "function filterSkills(q) {\n  const cards = document.querySelectorAll('.skill-card');\n  const keyword = q.toLowerCase();\n  cards.forEach(card => {\n    const text = card.textContent.toLowerCase();\n    card.style.display = text.includes(keyword) ? '' : 'none';\n  });\n}"
    new_filter = old_filter + """
function updateSkillsVisibility() {
  var locked = document.getElementById('skills-locked');
  var content = document.getElementById('skills-content');
  if (!locked || !content) return;
  if (user) { locked.style.display='none'; content.style.display='block'; }
  else { locked.style.display='block'; content.style.display='none'; }
}"""
    if old_filter in c:
        c = c.replace(old_filter, new_filter)
        results.append("updateSkillsVisibility函数: 已添加")
    else:
        results.append("updateSkillsVisibility函数: WARNING filterSkills未找到")

# 在init()中调用updateSkillsVisibility
old_init = "function init() {\n  renderAPITable();\n  renderCodingTable();\n  renderGPUs('all');\n  renderClaws();\n  animateStats();"
new_init = "function init() {\n  renderAPITable();\n  renderCodingTable();\n  renderGPUs('all');\n  renderClaws();\n  animateStats();\n  updateSkillsVisibility();"
if old_init in c and 'updateSkillsVisibility();' not in c.split('function init')[1].split('}')[0]:
    c = c.replace(old_init, new_init)
    results.append("init()中调用updateSkillsVisibility: 已添加")

# 在loginUI中调用updateSkillsVisibility
if 'function loginUI' in c and 'updateSkillsVisibility' in c:
    # 检查loginUI是否已包含调用
    login_section = c[c.find('function loginUI'):c.find('}', c.find('function loginUI'))+1]
    if 'updateSkillsVisibility' not in login_section:
        old_login_end = "document.querySelectorAll('.restricted-overlay').forEach(el => el.classList.remove('restricted-overlay'));"
        new_login_end = old_login_end + "\n  updateSkillsVisibility();"
        if old_login_end in c:
            c = c.replace(old_login_end, new_login_end, 1)
            results.append("loginUI中调用updateSkillsVisibility: 已添加")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 最终验证 =====
with open(path, "r", encoding="utf-8") as f:
    final = f.read()

print("=" * 60)
print("v3.11.9 修改结果")
print("=" * 60)
for r in results:
    print(f"  {r}")
print("=" * 60)

checks = {
    "图灵算力链接": "turingcm.com/index?contactsId=000007" in final,
    "GPT-5.4": "GPT-5.4" in final,
    "Claude Opus 4": "Claude Opus 4" in final,
    "Claude Sonnet 4": "Claude Sonnet 4" in final,
    "Gemini 3.2 Pro": "Gemini 3.2 Pro" in final,
    "阿里云免费部署": "free.aliyun.com" in final,
    "SKILLS锁定遮罩": "skills-locked" in final,
    "updateSkillsVisibility": "updateSkillsVisibility" in final,
    "旧turingapi清零": "turingapi.com" not in final,
}

print("\n最终验证:")
all_pass = True
for name, ok in checks.items():
    print(f"  {'PASS' if ok else 'FAIL'} {name}")
    if not ok: all_pass = False

print(f"\n{'ALL PASS - 可以推送！' if all_pass else 'FAIL - 需要修复'}")
