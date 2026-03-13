# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 恢复腾讯QClaw
if "腾讯推出的OpenCla" not in c and "腾讯QClaw" in c:
    c = c.replace(
        "{name:'腾讯QClaw',icon:'🐧',desc:'", 
        "{name:'腾讯QClaw',icon:'🐧',desc:'腾讯推出的OpenClaw一键启动包，本地部署，可接入QQ',url:'https://claw.guanjia.qq.com/',doc:'https://cloud.tencent.com/developer/article/2636112',open:false,beta:true,betaUrl:'https://claw.guanjia.qq.com/'},\n  {name:"
    )
    print("RESTORE: 腾讯QClaw")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if '腾讯QClaw' in line:
        print(f"Line {i}: {line.strip()}")
