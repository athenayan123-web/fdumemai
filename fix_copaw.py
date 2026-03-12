# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 替换阿里云免费部署 -> 阿里云CoPaw
old_name = "name:'\u963f\u91cc\u4e91\u514d\u8d39\u90e8\u7f72'"
new_name = "name:'\u963f\u91cc\u4e91CoPaw'"

old_desc = "desc:'\u96f6\u57fa\u7840\u5c0f\u767d\u4e00\u952e\u90e8\u7f72OpenClaw\u5230\u963f\u91cc\u4e91ECS\uff0c\u5168\u7a0b\u56fe\u6587\u6559\u7a0b\uff0c\u514d\u8d39\u989d\u5ea6\u53ef\u7528'"
new_desc = "desc:'\u963f\u91cc\u4e91\u5b98\u65b9AI\u7f16\u7a0b\u52a9\u624b\uff0c\u4e00\u952e\u90e8\u7f72\uff0c\u514d\u8d39\u989d\u5ea6\u53ef\u7528'"

old_url = "url:'https://free.aliyun.com/'"
new_url = "url:'https://www.aliyun.com/solution/tech-solution/copaw'"

old_doc = "doc:'https://help.aliyun.com/zh/ecs/getting-started/'"
new_doc = "doc:'https://www.aliyun.com/solution/tech-solution/copaw'"

for old, new, label in [
    (old_name, new_name, "名称"),
    (old_desc, new_desc, "描述"),
    (old_url, new_url, "URL"),
    (old_doc, new_doc, "文档链接"),
]:
    if old in c:
        c = c.replace(old, new)
        print(f"PASS {label}: {old[:30]}... -> {new[:30]}...")
    else:
        print(f"SKIP {label}: 未找到")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证: CoPaw={'PASS' if 'CoPaw' in v else 'FAIL'}")
print(f"验证: aliyun.com/solution={'PASS' if 'aliyun.com/solution/tech-solution/copaw' in v else 'FAIL'}")
print(f"验证: hot=true {'PASS' if 'hot:true' in v else 'FAIL'}")
