# -*- coding: utf-8 -*-
"""
替换CODING_DATA：扩展火山引擎Lite/Pro、智谱Lite/Pro/Max、百度Comate Pro、月之暗面
"""
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

start = c.find("const CODING_DATA = [")
end = c.find("];", start) + 2
old_block = c[start:end]

new_block = """const CODING_DATA = [

  // === 国际 ===

  {product:'GitHub Copilot',plan:'Individual',monthly:'$10',yearly:'$8.33',features:'代码补全、Chat、CLI、多模型切换',region:'国际',url:'https://github.com/features/copilot',logo:'🐙'},
  {product:'GitHub Copilot',plan:'Business',monthly:'$19',yearly:'$19',features:'团队管理、策略控制、IP保护',region:'国际',url:'https://github.com/features/copilot',logo:'🐙'},
  {product:'Cursor',plan:'Pro',monthly:'$20',yearly:'$16.67',features:'无限补全、500次快速请求、多模型',region:'国际',url:'https://cursor.com/',logo:'⚡'},
  {product:'Cursor',plan:'Business',monthly:'$40',yearly:'$33.33',features:'团队协作、集中计费、管理后台',region:'国际',url:'https://cursor.com/',logo:'⚡'},
  {product:'Windsurf',plan:'Pro',monthly:'$15',yearly:'$12.50',features:'AI Flow、多模型切换、代码重构',region:'国际',url:'https://codeium.com/windsurf',logo:'🏄'},
  {product:'Augment Code',plan:'Pro',monthly:'$30',yearly:'$25',features:'全仓库上下文、多文件编辑',region:'国际',url:'https://www.augmentcode.com/',logo:'🧩'},

  // === 国内免费 ===

  {product:'通义灵码',plan:'个人版',monthly:'免费',yearly:'免费',features:'代码补全、单元测试生成、Qwen驱动',region:'国内',url:'https://tongyi.aliyun.com/lingma',logo:'🌐'},
  {product:'Trae',plan:'个人版',monthly:'免费',yearly:'免费',features:'字节出品、AI原生IDE、免费GPT-4o',region:'国内',url:'https://www.trae.ai/',logo:'🔥'},
  {product:'MarsCode',plan:'个人版',monthly:'免费',yearly:'免费',features:'豆包驱动、AI补全、Chat、多语言',region:'国内',url:'https://www.marscode.com/',logo:'🚀'},
  {product:'Baidu Comate',plan:'个人版',monthly:'免费',yearly:'免费',features:'文心驱动、代码生成、智能补全',region:'国内',url:'https://comate.baidu.com/',logo:'🐻'},
  {product:'Tencent Cloud AI Code',plan:'基础版',monthly:'免费',yearly:'免费',features:'混元驱动、代码补全、代码解释',region:'国内',url:'https://cloud.tencent.com/product/acc',logo:'🐧'},

  // === 国内付费 ===

  {product:'火山引擎',plan:'Lite Plan',monthly:'¥49',yearly:'¥39',features:'豆包/GLM/MiniMax/Kimi基础调用',region:'国内',url:'https://www.volcengine.com/product/doubao',logo:'🔥'},
  {product:'火山引擎',plan:'Pro Plan',monthly:'¥199',yearly:'¥169',features:'豆包/GLM/MiniMax/Kimi高级调用+团队管理',region:'国内',url:'https://www.volcengine.com/product/doubao',logo:'🔥'},
  {product:'智谱AI',plan:'Lite',monthly:'¥29',yearly:'¥24',features:'GLM-4-Flash、基础代码补全',region:'国内',url:'https://open.bigmodel.cn/',logo:'🟣'},
  {product:'智谱AI',plan:'Pro',monthly:'¥99',yearly:'¥79',features:'GLM-4-Plus、高级代码生成+Chat',region:'国内',url:'https://open.bigmodel.cn/',logo:'🟣'},
  {product:'智谱AI',plan:'Max',monthly:'¥299',yearly:'¥249',features:'GLM-4全系列、团队协作、API无限调用',region:'国内',url:'https://open.bigmodel.cn/',logo:'🟣'},
  {product:'Baidu Comate',plan:'企业版',monthly:'¥99',yearly:'¥79',features:'ERNIE 4.0驱动、团队管理、私有部署',region:'国内',url:'https://comate.baidu.com/',logo:'🐻'},
  {product:'月之暗面',plan:'Kimi开发者',monthly:'¥59',yearly:'¥49',features:'Kimi-128K驱动、超长上下文编程',region:'国内',url:'https://platform.moonshot.cn/',logo:'🌙'},

];"""

c = c[:start] + new_block + c[end:]

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

products = re.findall(r"product:'([^']*)'", v[v.find("const CODING_DATA"):v.find("];", v.find("const CODING_DATA"))])
plans = re.findall(r"plan:'([^']*)'", v[v.find("const CODING_DATA"):v.find("];", v.find("const CODING_DATA"))])

print(f"产品总数: {len(products)}")
for i, (p, pl) in enumerate(zip(products, plans), 1):
    print(f"  {i}. {p} - {pl}")

free_count = v[v.find("const CODING_DATA"):v.find("];", v.find("const CODING_DATA"))].count("monthly:'免费'")
print(f"\n免费产品: {free_count}")
print(f"火山引擎: {'PASS' if '火山引擎' in v else 'FAIL'}")
print(f"智谱Lite/Pro/Max: {'PASS' if 'Lite' in v and 'Pro' in v and 'Max' in v else 'FAIL'}")
print(f"月之暗面: {'PASS' if '月之暗面' in v else 'FAIL'}")
print(f"Trae: {'PASS' if 'Trae' in v else 'FAIL'}")
print(f"总计: {'PASS' if len(products)==18 else 'FAIL'} ({len(products)}款)")
