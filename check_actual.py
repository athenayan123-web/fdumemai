# -*- coding: utf-8 -*-
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

print("=== 所有model字段 ===")
for m in re.findall(r"model:'[^']*'", c):
    print(m)

print("\n=== 所有Gemini ===")
for m in re.findall(r"Gemini[^'\"]*", c):
    print(m)

print("\n=== Claude相关 ===")
for m in re.findall(r"Claude[^'\"]*", c):
    print(m)

print("\n=== skills-locked ===")
print("found" if "skills-locked" in c else "NOT found")

print("\n=== updateSkillsVisibility ===")
print("found" if "updateSkillsVisibility" in c else "NOT found")
