# -*- coding: utf-8 -*-
"""
v3.11.9 逐条修改与验证脚本
目标文件: E:\智能整理\openclaw\app\index.html
"""
import re

path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

results = []

# ===== 修改1: 图灵算力链接 =====
old_turing = "https://www.turingapi.com/"
new_turing = "https://www.turingcm.com/index?contactsId=000007"
c1 = content.count(old_turing)
c1b = content.count(new_turing)
if c1 > 0:
    content = content.replace(old_turing, new_turing)
    results.append(f"[修改1] 图灵链接: 替换 {c1} 处 turingapi -> turingcm")
elif c1b > 0:
    results.append(f"[修改1] 图灵链接: 已正确({c1b}处)")
else:
    results.append("[修改1] 图灵链接: WARNING 未找到任何图灵链接")

# 验证1
v1 = content.count(new_turing)
v1_old = content.count(old_turing)
results.append(f"  验证1: 正确链接={v1}处, 旧链接={v1_old}处 {'PASS' if v1>0 and v1_old==0 else 'FAIL'}")

# ===== 修改2: 模型版本更新 =====
model_updates = [
    ("model:'GPT-5.2'", "model:'GPT-5.4'"),
    ("model:'GPT-5.1'", "model:'GPT-5.3'"),
    ("model:'Claude 4 Sonnet'", "model:'Claude Opus 4'"),
]
for old_m, new_m in model_updates:
    if old_m in content:
        content = content.replace(old_m, new_m)
        results.append(f"[修改2] 模型更新: {old_m} -> {new_m}")
    elif new_m in content:
        results.append(f"[修改2] 模型已正确: {new_m}")
    else:
        results.append(f"[修改2] 未找到: {old_m}")

# 添加Claude Sonnet 4（如果不存在）
if "Claude Sonnet 4" not in content and "Claude 3.5 Haiku" in content:
    content = content.replace(
        "  {provider:'Anthropic',model:'Claude 3.5 Haiku'",
        "  {provider:'Anthropic',model:'Claude Sonnet 4',input:'$3.00/1M',output:'$15.00/1M',context:'200K',region:'\u56fd\u9645',url:'https://console.anthropic.com/',logo:'\U0001f7e0',tag:'hot',features:'\u4e3b\u6253\u6027\u4ef7\u6bd4\uff0c\u8ba9\u4eba\u4eba\u90fd\u6709\u53ef\u7528\u7684 Claude 4'},\n  {provider:'Anthropic',model:'Claude 3.5 Haiku'"
    )
    results.append("[修改2] 新增Claude Sonnet 4（性价比款）")

# 更新Claude Opus 4描述
if "Claude Opus 4" in content:
    # 更新features
    old_feat = "features:'\u957f\u6587\u672c\u3001\u4ee3\u7801\u751f\u6210\u3001\u5b89\u5168\u5bf9\u9f50'"
    new_feat = "features:'Anthropic \u8fc4\u4eca\u4e3a\u6b62\u6700\u5f3a\u5927\u7684\u6a21\u578b\uff0c\u4e3b\u6253\u9ad8\u6027\u80fd'"
    if old_feat in content:
        content = content.replace(old_feat, new_feat)
        results.append("[修改2] Claude Opus 4 features已更新")

# Gemini更新
gemini_updates = [
    ("model:'Gemini 2.5 Pro'", "model:'Gemini 3.2 Pro'"),
    ("model:'Gemini 2.5 Flash'", "model:'Gemini 3.2 Flash'"),
    ("model:'Gemini 2.0 Flash'", "model:'Gemini 3.0 Flash'"),
]
for old_g, new_g in gemini_updates:
    if old_g in content:
        content = content.replace(old_g, new_g)
        results.append(f"[修改2] Gemini更新: {old_g} -> {new_g}")
    elif new_g in content:
        results.append(f"[修改2] Gemini已正确: {new_g}")

# 验证2
for check in ["GPT-5.4", "GPT-5.3", "Claude Opus 4", "Claude Sonnet 4", "Gemini 3.2 Pro"]:
    found = check in content
    results.append(f"  验证2: {check} {'PASS' if found else 'FAIL'}")

# ===== 修改3: Claw集合增加阿里云免费部署 =====
if "free.aliyun.com" not in content:
    # 在猎豹EasyClaw后添加
    old_claw = "{name:'\u7360\u8c79EasyClaw'"
    if old_claw in content:
        idx = content.find(old_claw)
        # 找到这行的结尾
        end = content.find("\n", idx)
        insert = "\n  {name:'\u963f\u91cc\u4e91\u514d\u8d39\u90e8\u7f72',icon:'\u2601\ufe0f',desc:'\u96f6\u57fa\u7840\u5c0f\u767d\u4e00\u952e\u90e8\u7f72OpenClaw\u5230\u963f\u91cc\u4e91ECS\uff0c\u5168\u7a0b\u56fe\u6587\u6559\u7a0b\uff0c\u514d\u8d39\u989d\u5ea6\u53ef\u7528',url:'https://free.aliyun.com/',doc:'https://help.aliyun.com/zh/ecs/getting-started/',open:true,hot:true},"
        content = content[:end] + insert + content[end:]
        results.append("[修改3] Claw集合: 新增阿里云免费部署")
    else:
        results.append("[修改3] WARNING: 未找到猎豹EasyClaw")
else:
    results.append("[修改3] Claw集合: 阿里云已存在")

# 验证3
v3 = "free.aliyun.com" in content
results.append(f"  验证3: 阿里云免费部署 {'PASS' if v3 else 'FAIL'}")

# ===== 修改4: SKILLS注册锁定 =====
if "skills-locked" in content:
    results.append("[修改4] SKILLS锁定遮罩: 已存在")
else:
    results.append("[修改4] WARNING: SKILLS锁定遮罩未找到")

if "updateSkillsVisibility" in content:
    results.append("[修改4] updateSkillsVisibility函数: 已存在")
else:
    results.append("[修改4] WARNING: updateSkillsVisibility函数未找到")

# 验证4
v4a = "skills-locked" in content
v4b = "updateSkillsVisibility" in content
results.append(f"  验证4: 锁定遮罩={'PASS' if v4a else 'FAIL'}, 函数={'PASS' if v4b else 'FAIL'}")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# ===== 输出结果 =====
print("=" * 60)
print("v3.11.9 逐条修改与验证结果")
print("=" * 60)
for r in results:
    print(r)
print("=" * 60)

# 最终全量验证
with open(path, "r", encoding="utf-8") as f:
    final = f.read()

checks = {
    "图灵算力链接": "turingcm.com/index?contactsId=000007" in final,
    "GPT-5.4": "GPT-5.4" in final,
    "GPT-5.3": "GPT-5.3" in final,
    "Claude Opus 4": "Claude Opus 4" in final,
    "Claude Sonnet 4": "Claude Sonnet 4" in final,
    "Gemini 3.2 Pro": "Gemini 3.2 Pro" in final,
    "阿里云免费部署": "free.aliyun.com" in final,
    "SKILLS锁定": "skills-locked" in final,
    "updateSkillsVisibility": "updateSkillsVisibility" in final,
    "旧图灵链接清零": "turingapi.com" not in final,
}

print("\n最终验证:")
all_pass = True
for name, ok in checks.items():
    s = "PASS" if ok else "FAIL"
    print(f"  {'✅' if ok else '❌'} {name}: {s}")
    if not ok:
        all_pass = False

print(f"\n{'🎉 全部通过！可以推送。' if all_pass else '⚠️ 部分失败，请检查。'}")
