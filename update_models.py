# -*- coding: utf-8 -*-
"""
替换API_DATA为16款模型（3梯队）
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 定位API_DATA
start = c.find("const API_DATA = [")
end = c.find("];", start) + 2

old_block = c[start:end]

new_block = """const API_DATA = [

  // === 🏆 第一梯队（顶级旗舰） ===

  {provider:'OpenAI',model:'GPT-5.4',input:'$2.00/1M',output:'$8.00/1M',context:'1M',region:'国际',url:'https://platform.openai.com/docs/api-reference',logo:'🟢',tag:'hot',tier:'T1',features:'最新旗舰，百万上下文，多模态推理增强'},
  {provider:'Anthropic',model:'Claude Opus 4',input:'$15.00/1M',output:'$75.00/1M',context:'200K',region:'国际',url:'https://console.anthropic.com/',logo:'🟠',tag:'hot',tier:'T1',features:'Anthropic迄今为止最强大的模型，主打高性能'},
  {provider:'Google',model:'Gemini 3.2 Pro',input:'$1.25/1M',output:'$10.00/1M',context:'2M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'new',tier:'T1',features:'200万上下文窗口，多模态，搜索集成'},

  // === 🥈 第二梯队（高性价比主力） ===

  {provider:'OpenAI',model:'GPT-4.1',input:'$2.00/1M',output:'$8.00/1M',context:'1M',region:'国际',url:'https://platform.openai.com/docs/api-reference',logo:'🟢',tag:'',tier:'T2',features:'代码优化，指令遵循，百万上下文'},
  {provider:'OpenAI',model:'GPT-4o-mini',input:'$0.15/1M',output:'$0.60/1M',context:'128K',region:'国际',url:'https://platform.openai.com/docs/api-reference',logo:'🟢',tag:'low',tier:'T2',features:'极致低成本，适合批量调用'},
  {provider:'Anthropic',model:'Claude Sonnet 4',input:'$3.00/1M',output:'$15.00/1M',context:'200K',region:'国际',url:'https://console.anthropic.com/',logo:'🟠',tag:'hot',tier:'T2',features:'主打性价比，让人人都有可用的Claude 4'},
  {provider:'Anthropic',model:'Claude Haiku 3.5',input:'$0.80/1M',output:'$4.00/1M',context:'200K',region:'国际',url:'https://console.anthropic.com/',logo:'🟠',tag:'low',tier:'T2',features:'快速响应，低成本，轻量级'},
  {provider:'Google',model:'Gemini 2.5 Flash',input:'$0.15/1M',output:'$0.60/1M',context:'1M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'low',tier:'T2',features:'极速响应，百万上下文，低成本'},
  {provider:'DeepSeek',model:'DeepSeek-V3',input:'¥1.00/1M',output:'¥2.00/1M',context:'128K',region:'国内',url:'https://platform.deepseek.com/',logo:'🐋',tag:'hot',tier:'T2',features:'国产之光，高性能低成本，中文优化'},
  {provider:'DeepSeek',model:'DeepSeek-R1',input:'¥4.00/1M',output:'¥16.00/1M',context:'128K',region:'国内',url:'https://platform.deepseek.com/',logo:'🐋',tag:'new',tier:'T2',features:'深度推理，数学逻辑，思维链'},
  {provider:'阿里云',model:'Qwen3-Max',input:'¥2.00/1M',output:'¥8.00/1M',context:'128K',region:'国内',url:'https://dashscope.aliyun.com/',logo:'☁️',tag:'new',tier:'T2',features:'通义千问旗舰，多模态，中英双语'},

  // === 🥉 第三梯队（轻量/特化） ===

  {provider:'OpenAI',model:'GPT-4.1-nano',input:'$0.10/1M',output:'$0.40/1M',context:'1M',region:'国际',url:'https://platform.openai.com/docs/api-reference',logo:'🟢',tag:'low',tier:'T3',features:'最低成本，百万上下文，适合嵌入式'},
  {provider:'Google',model:'Gemini 2.0 Flash',input:'$0.10/1M',output:'$0.40/1M',context:'1M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'low',tier:'T3',features:'实时流式，多模态，极致低成本'},
  {provider:'字节火山',model:'Doubao-1.5-Pro',input:'¥0.80/1M',output:'¥2.00/1M',context:'128K',region:'国内',url:'https://www.volcengine.com/product/doubao',logo:'🔥',tag:'low',tier:'T3',features:'豆包最新版，多模态，极致低成本'},
  {provider:'智谱AI',model:'GLM-4-Plus',input:'¥5.00/1M',output:'¥5.00/1M',context:'128K',region:'国内',url:'https://open.bigmodel.cn/',logo:'🟣',tag:'',tier:'T3',features:'多模态，代码生成，中文理解'},
  {provider:'Moonshot',model:'Kimi-128K',input:'¥12.00/1M',output:'¥12.00/1M',context:'128K',region:'国内',url:'https://platform.moonshot.cn/',logo:'🌙',tag:'',tier:'T3',features:'超长上下文，文档理解，联网搜索'},
];"""

c = c[:start] + new_block + c[end:]

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

import re
models = re.findall(r"model:'([^']*)'", v[v.find("const API_DATA"):v.find("];", v.find("const API_DATA"))])
print(f"模型总数: {len(models)}")
for i, m in enumerate(models, 1):
    print(f"  {i}. {m}")

t1 = sum(1 for x in re.findall(r"tier:'T1'", v))
t2 = sum(1 for x in re.findall(r"tier:'T2'", v))
t3 = sum(1 for x in re.findall(r"tier:'T3'", v))
print(f"\n梯队: T1={t1} T2={t2} T3={t3} 总计={t1+t2+t3}")
print(f"验证: {'PASS' if len(models)==16 and t1==3 and t2==8 and t3==5 else 'FAIL'}")
