# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

old = "https://www.turingapi.com/"
new = "https://www.turingcm.com/index?contactsId=000007"

count = c.count(old)
print(f"Found {count} occurrences of '{old}'")

c = c.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# Verify
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"After: {v.count(new)} occurrences of correct URL")
print(f"After: {v.count(old)} occurrences of old URL")
