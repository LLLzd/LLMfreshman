# 项目2: LoRA微调小模型

> 难度: ⭐⭐ | 时间: 2-3天 | 资源: 8GB内存

## 项目目标

掌握参数高效微调(PEFT)方法，通过LoRA技术微调小模型：
- 理解LoRA原理和优势
- 使用PEFT库进行微调
- 在特定任务上微调模型
- 对比全参数微调与LoRA的效果

## 项目结构

```
02-lora-finetune/
├── README.md              # 本文件
├── lora_config.py         # LoRA配置
├── finetune.py           # 微调脚本
├── inference.py          # 推理脚本
├── evaluate.py           # 评估脚本
├── data/                 # 数据集
└── outputs/              # 模型输出
```

## 环境准备

```bash
# 安装依赖
pip install transformers datasets peft accelerate
pip install bitsandbytes  # 用于量化
```

## 推荐模型

适合M1 Mac的轻量级模型：

1. **TinyLlama-1.1B** (推荐)
   - 参数量: 1.1B
   - 内存需求: ~4GB (INT8量化)
   - HuggingFace: `TinyLlama/TinyLlama-1.1B-Chat-v1.0`

2. **Phi-2 (2.7B)**
   - 参数量: 2.7B
   - 内存需求: ~6GB (INT8量化)
   - HuggingFace: `microsoft/phi-2`

3. **Qwen2-0.5B/1.5B**
   - 参数量: 0.5B/1.5B
   - 内存需求: ~2-4GB
   - HuggingFace: `Qwen/Qwen2-0.5B-Instruct`

## 实现步骤

### Step 1: 环境搭建与模型加载 (Day 1)
- [ ] 安装PEFT和相关库
- [ ] 加载预训练模型
- [ ] 配置LoRA参数
- [ ] 测试基础推理能力

### Step 2: 数据准备 (Day 1)
- [ ] 选择微调任务（如：问答、摘要、指令遵循）
- [ ] 准备/下载数据集
- [ ] 实现数据预处理
- [ ] 创建DataLoader

### Step 3: 微调训练 (Day 2)
- [ ] 配置LoRA (rank, alpha, dropout)
- [ ] 实现训练循环
- [ ] 添加评估指标
- [ ] 保存检查点

### Step 4: 评估与对比 (Day 3)
- [ ] 评估微调后模型
- [ ] 对比微调前后效果
- [ ] 尝试不同的LoRA配置
- [ ] 总结实验结果

## LoRA配置示例

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16,                    # LoRA rank
    lora_alpha=32,          # LoRA alpha
    target_modules=["q_proj", "v_proj"],  # 目标模块
    lora_dropout=0.05,      # dropout
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
```

## 数据集建议

1. **Alpaca数据集** (指令遵循)
   - 52K条指令-输出对
   - 适合快速实验

2. **Chinese-LLaMA-Alpaca** (中文指令)
   - 中文指令数据
   - 适合中文场景

3. **自定义数据**
   - 特定领域问答
   - 文本摘要任务

## 代码示例

```python
# 预期代码结构
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType

# 加载模型
model = AutoModelForCausalLM.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    load_in_8bit=True,  # M1 Mac使用8bit量化
    device_map="auto"
)

# 配置LoRA
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

# 应用LoRA
model = get_peft_model(model, lora_config)

# 训练
# ... 训练代码
```

## 实验对比

建议对比以下配置：

| 配置 | Rank | Alpha | 可训练参数 | 效果 |
|------|------|-------|-----------|------|
| 小Rank | 8 | 16 | ~1M | ? |
| 中Rank | 16 | 32 | ~4M | ? |
| 大Rank | 32 | 64 | ~16M | ? |

## 评估指标

- **困惑度(Perplexity)**: 语言建模能力
- **BLEU/ROUGE**: 生成质量
- **人工评估**: 回答质量

## 参考资源

- [PEFT官方文档](https://huggingface.co/docs/peft/index)
- [LoRA论文](https://arxiv.org/abs/2106.09685)
- [QLoRA论文](https://arxiv.org/abs/2305.14314)
- [Hugging Face微调教程](https://huggingface.co/docs/transformers/training)

## 学习笔记

### LoRA理解
- 为什么LoRA有效？
- Rank的选择依据？
- 哪些层应该添加LoRA？

### 实验结果
- 不同Rank的效果对比
- 量化对性能的影响
- 训练时间与显存占用

### 遇到的问题
- 

### 下一步
- 尝试QLoRA
- 多任务微调
- 模型合并技术
