# -*- coding: utf-8 -*-
"""
v3.12.1 模型数据全面刷新 - 30+款模型
"""
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 定位API_DATA
start = c.find("const API_DATA = [")
end = c.find("];", start) + 2

new_data = r"""const API_DATA = [

  // ===== 🏆 旗舰系列 =====

  {provider:'OpenAI',model:'GPT-5.4',input:'$2.50/1M',output:'$15.00/1M',context:'1.05M',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'hot',tier:'T1',sub:'OpenAI旗舰',features:'原生电脑操作、工具搜索、多模态推理',bench:'OSWorld 75.0% | GDPval 83%'},
  {provider:'OpenAI',model:'GPT-5.4 Pro',input:'$30.00/1M',output:'$180.00/1M',context:'1.05M',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'new',tier:'T1',sub:'OpenAI旗舰',features:'企业级复杂任务，最高算力',bench:'推理深度更强'},
  {provider:'Anthropic',model:'Claude Opus 4.6',input:'$5~10/1M',output:'$25~37.5/1M',context:'1M(测试版)',region:'国际',url:'https://console.anthropic.com/',logo:'🟠',tag:'hot',tier:'T1',sub:'Anthropic旗舰',features:'Agent Teams并行处理、1M上下文',bench:'ARC AGI 2: 68.8% | SWE-bench: 80.8%'},
  {provider:'Google',model:'Gemini 3.2 Pro',input:'$5~10/1M',output:'$25~37.5/1M',context:'200K+',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'new',tier:'T1',sub:'Google旗舰',features:'构建智能体和编码的最智能模型',bench:'Google Cloud Vertex AI'},
  {provider:'阿里云',model:'Qwen3-Max',input:'¥2.5~7.0/1M',output:'¥10~28/1M',context:'262K',region:'国内',url:'https://dashscope.aliyun.com/',logo:'☁️',tag:'hot',tier:'T1',sub:'国产旗舰',features:'适合复杂任务，能力最强，支持思考模式',bench:'SWE-Bench 69.6 | AIME/HMMT双满分'},
  {provider:'阿里云',model:'Qwen3.5-Plus',input:'¥0.8~4.0/1M',output:'¥4.8~24/1M',context:'1M',region:'国内',url:'https://dashscope.aliyun.com/',logo:'☁️',tag:'new',tier:'T1',sub:'国产旗舰',features:'效果速度成本均衡，支持文本图像视频',bench:'纯文本媲美Qwen3-Max，速度更快'},
  {provider:'阿里云',model:'Qwen3.5-Flash',input:'¥0.2~1.2/1M',output:'¥2~12/1M',context:'1M',region:'国内',url:'https://dashscope.aliyun.com/',logo:'☁️',tag:'low',tier:'T1',sub:'国产旗舰',features:'适合简单任务，速度快、成本低',bench:''},
  {provider:'智谱AI',model:'GLM-5',input:'$1.00/1M',output:'$3.20/1M',context:'200K',region:'国内',url:'https://open.bigmodel.cn/',logo:'🟣',tag:'new',tier:'T1',sub:'国产旗舰',features:'744B总参数(40B激活)，MoE架构',bench:'SWE-bench 77.8%(开源SOTA)'},
  {provider:'月之暗面',model:'Kimi K2.5',input:'$0.60/1M',output:'$2.50/1M',context:'256K',region:'国内',url:'https://platform.moonshot.cn/',logo:'🌙',tag:'new',tier:'T1',sub:'国产旗舰',features:'1T总参数(32B激活)，原生多模态，Agent Swarm',bench:'全球首个万亿参数MoE'},
  {provider:'字节火山',model:'豆包2.0 Pro',input:'¥0.80/1M',output:'¥2.00/1M',context:'128K',region:'国内',url:'https://www.volcengine.com/product/doubao',logo:'🔥',tag:'hot',tier:'T1',sub:'国产旗舰',features:'复杂深度推理与Agent任务',bench:'HLE-Text 54.2(当前最高)'},
  {provider:'DeepSeek',model:'DeepSeek-V4',input:'~$0.28/1M',output:'~$1.10/1M',context:'1M',region:'国内',url:'https://platform.deepseek.com/',logo:'🐋',tag:'new',tier:'T1',sub:'国产旗舰',features:'~1T总参数，MoE架构，Engram记忆机制',bench:'新一代多模态旗舰'},
  {provider:'MiniMax',model:'MiniMax M2.5',input:'$0.30/1M',output:'$1.20/1M',context:'197K',region:'国内',url:'https://www.minimaxi.com/',logo:'✨',tag:'new',tier:'T1',sub:'国产旗舰',features:'230B总参数(10B激活)，Agent原生设计',bench:'专为Agent场景设计'},
  {provider:'阶跃星辰',model:'Step 3.5 Flash',input:'¥0.7/1M',output:'¥2.1/1M',context:'256K',region:'国内',url:'https://platform.stepfun.com/',logo:'🧠',tag:'new',tier:'T1',sub:'国产旗舰',features:'196B总参数(11B激活)，MoE架构',bench:'AIME 2025: 97.3'},
  {provider:'百度',model:'ERNIE 5.0',input:'¥6~10/1M',output:'¥24~40/1M',context:'128K+',region:'国内',url:'https://cloud.baidu.com/',logo:'🐻',tag:'new',tier:'T1',sub:'国产旗舰',features:'最新旗舰，支持思考模式',bench:'VBench 83.40 | MATH 73.89%'},
  {provider:'科大讯飞',model:'Spark X2',input:'¥2000~3000/1M',output:'¥2000~3000/1M',context:'1M',region:'国内',url:'https://xinghuo.xfyun.cn/',logo:'🎤',tag:'new',tier:'T1',sub:'国产旗舰',features:'深度推理旗舰，293B MoE架构',bench:'数学推理、智能体能力达国际顶尖'},

  // ===== 🥈 主力系列 =====

  {provider:'OpenAI',model:'GPT-4.1',input:'$2.00/1M',output:'$8.00/1M',context:'1M+',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'',tier:'T2',sub:'代码主力',features:'代码优化，指令遵循，百万上下文',bench:'SWE-bench 54.6%'},
  {provider:'Anthropic',model:'Claude Sonnet 4.6',input:'$3.00/1M',output:'$15.00/1M',context:'200K(1M beta)',region:'国际',url:'https://console.anthropic.com/',logo:'🟠',tag:'hot',tier:'T2',sub:'平衡主力',features:'史上最强Sonnet，智能体基础模型',bench:'Agent金融分析 63.3% | OSWorld 72.5'},
  {provider:'Google',model:'Gemini 2.5 Pro',input:'$1.25~2.50/1M',output:'$10~15/1M',context:'2M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'',tier:'T2',sub:'平衡主力',features:'复杂分析任务，自适应思考',bench:'WebDevArena领先21% | GPQA专家水平'},
  {provider:'百度',model:'ERNIE 4.5 Turbo',input:'¥0.8/1M',output:'¥3.2/1M',context:'128K',region:'国内',url:'https://cloud.baidu.com/',logo:'🐻',tag:'',tier:'T2',sub:'平衡主力',features:'主力模型，高性价比',bench:'SuperCLUE多模态66.47(国内第一)'},
  {provider:'科大讯飞',model:'Spark Ultra',input:'¥800/1M',output:'¥800/1M',context:'128K',region:'国内',url:'https://xinghuo.xfyun.cn/',logo:'🎤',tag:'',tier:'T2',sub:'平衡主力',features:'高性价比旗舰模型',bench:'指令跟随、文本生成能力突出'},
  {provider:'DeepSeek',model:'DeepSeek-V3.2',input:'$0.28/1M',output:'$0.42/1M',context:'128K',region:'国内',url:'https://platform.deepseek.com/',logo:'🐋',tag:'hot',tier:'T2',sub:'性价比主力',features:'MIT开源，文本+工具调用',bench:'国产性价比之王'},
  {provider:'科大讯飞',model:'Spark Pro',input:'¥5000/1M',output:'¥5000/1M',context:'128K',region:'国内',url:'https://xinghuo.xfyun.cn/',logo:'🎤',tag:'',tier:'T2',sub:'性价比主力',features:'性能高效模型',bench:'保证效果同时更快吐字速度'},

  // ===== 🥉 轻量系列 =====

  {provider:'Anthropic',model:'Claude Haiku 4.6',input:'$1.00/1M',output:'$5.00/1M',context:'200K',region:'国际',url:'https://console.anthropic.com/',logo:'🟠',tag:'low',tier:'T3',sub:'快速轻量',features:'速度最快，近前沿智能',bench:'SWE-bench 73.3%'},
  {provider:'Google',model:'Gemini 3.1 Flash-Lite',input:'$0.25/1M',output:'$1.50/1M',context:'1M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'new',tier:'T3',sub:'快速轻量',features:'替代2.5 Flash-Lite，支持思考等级调节',bench:'首字响应快2.5倍 | GPQA Diamond 86.9%'},
  {provider:'Google',model:'Gemini 2.5 Flash',input:'$0.30/1M',output:'$2.50/1M',context:'1M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'',tier:'T3',sub:'快速轻量',features:'兼顾推理与速度，低延迟',bench:'SWE-bench 54%'},
  {provider:'OpenAI',model:'GPT-5.3 Instant',input:'~$0.30/1M',output:'~$1.20/1M',context:'400K',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'new',tier:'T3',sub:'极致低价',features:'更具人味儿，大幅降低幻觉率',bench:'幻觉率降低26.8%'},
  {provider:'OpenAI',model:'GPT-4.1-nano',input:'$0.10/1M',output:'$0.40/1M',context:'1M+',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'low',tier:'T3',sub:'极致低价',features:'最低成本长上下文',bench:'最快最经济选项'},
  {provider:'OpenAI',model:'GPT-5 Nano',input:'$0.05/1M',output:'$0.40/1M',context:'400K',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'low',tier:'T3',sub:'极致低价',features:'GPT-5系列最轻量',bench:'支持文件搜索、图像生成'},
  {provider:'Google',model:'Gemini 2.5 Flash-Lite',input:'$0.10/1M',output:'$0.40/1M',context:'1M',region:'国际',url:'https://aistudio.google.com/',logo:'🔵',tag:'low',tier:'T3',sub:'极致低价',features:'Flash系列最经济选择',bench:'指令遵循能力显著提升'},
  {provider:'阿里云',model:'Qwen3.5-Flash',input:'¥0.2~1.2/1M',output:'¥2~12/1M',context:'1M',region:'国内',url:'https://dashscope.aliyun.com/',logo:'☁️',tag:'low',tier:'T3',sub:'极致低价',features:'千问系列速度最快、成本极低',bench:''},
  {provider:'科大讯飞',model:'Spark Lite',input:'免费',output:'免费',context:'32K',region:'国内',url:'https://xinghuo.xfyun.cn/',logo:'🎤',tag:'low',tier:'T3',sub:'极致低价',features:'免费轻量模型',bench:'响应速度高，适用于简单场景'},

  // ===== 🔬 特化系列 =====

  {provider:'OpenAI',model:'o4-mini',input:'$1.10/1M',output:'$4.40/1M',context:'200K',region:'国际',url:'https://openai.com/zh-Hans-CN/',logo:'🟢',tag:'hot',tier:'T4',sub:'推理特化',features:'紧凑型推理模型，数学编码强',bench:'LiveCodeBench 85.9% | AIME 94%'},
  {provider:'DeepSeek',model:'DeepSeek-R1',input:'¥4.00/1M',output:'¥16.00/1M',context:'128K',region:'国内',url:'https://platform.deepseek.com/',logo:'🐋',tag:'hot',tier:'T4',sub:'推理特化',features:'深度推理，数学逻辑，思维链',bench:'深度推理标杆'},

];"""

c = c[:start] + new_data + c[end:]

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
models = re.findall(r"model:'([^']*)'", v[v.find("const API_DATA"):v.find("];", v.find("const API_DATA"))])
tiers = {t: 0 for t in ['T1','T2','T3','T4']}
for t in re.findall(r"tier:'(T\d)'", v[v.find("const API_DATA"):v.find("];", v.find("const API_DATA"))]):
    tiers[t] = tiers.get(t, 0) + 1

print(f"模型总数: {len(models)}")
for i, m in enumerate(models, 1):
    print(f"  {i}. {m}")
print(f"\n梯队分布: T1旗舰={tiers['T1']} T2主力={tiers['T2']} T3轻量={tiers['T3']} T4特化={tiers['T4']}")
print(f"总计: {sum(tiers.values())}")
