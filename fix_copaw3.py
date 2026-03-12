# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 直接替换完整条目
old = "name:'阿里云免费部署',icon:'☁️',desc:'零基础小白一键部署OpenClaw到阿里云ECS，全程图文教程，免费额度可用'"
new = "name:'阿里云CoPaw',icon:'☁️',desc:'阿里云官方AI编程助手CoPaw，一键部署，免费额度可用'"

if old in c:
    c = c.replace(old, new)
    print("PASS: 名称+描述已更新")
else:
    print("FAIL: 未找到旧条目，尝试逐字节搜索")
    # 尝试搜索
    if "阿里云免费部署" in c:
        c = c.replace("阿里云免费部署", "阿里云CoPaw")
        print("PASS: 名称已替换(备用)")
    if "零基础小白一键部署OpenClaw到阿里云ECS，全程图文教程，免费额度可用" in c:
        c = c.replace("零基础小白一键部署OpenClaw到阿里云ECS，全程图文教程，免费额度可用", "阿里云官方AI编程助手CoPaw，一键部署，免费额度可用")
        print("PASS: 描述已替换(备用)")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"验证 CoPaw: {'PASS' if '阿里云CoPaw' in v else 'FAIL'}")
print(f"验证 URL: {'PASS' if 'aliyun.com/solution/tech-solution/copaw' in v else 'FAIL'}")
