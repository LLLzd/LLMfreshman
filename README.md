# LLMfreshman 🤖

> 大语言模型（LLM）新手入门学习仓库 - 从零开始掌握LLM核心技术

适合**16GB内存 + Apple M1芯片**的MacBook Pro用户，专注于理论学习+轻量级实践项目。

---

## 📚 学习路线图

### Phase 1: 基础理论（第1-2周）
- **目标**: 理解Transformer架构和注意力机制
- **论文**: Attention Is All You Need, BERT, GPT系列
- **实践**: 实现简化版Transformer

### Phase 2: 预训练与微调（第3-4周）
- **目标**: 掌握预训练原理和高效微调方法
- **论文**: LLaMA, LoRA, QLoRA
- **实践**: 使用LoRA微调小模型

### Phase 3: 对齐与强化学习（第5-6周）
- **目标**: 理解RLHF和偏好优化
- **论文**: InstructGPT, DPO, PPO
- **实践**: 实现DPO训练流程

### Phase 4: 多模态与推理（第7-8周）
- **目标**: 了解多模态LLM和推理优化
- **论文**: CLIP, LLaVA, vLLM
- **实践**: 构建简单多模态应用

---

## 📁 项目结构

```
LLMfreshman/
├── README.md                 # 本文件
├── papers/                   # 经典论文学习
│   ├── fundamentals/         # 基础架构
│   ├── pretraining/          # 预训练
│   ├── alignment/            # 对齐技术
│   ├── multimodal/           # 多模态
│   └── efficiency/           # 效率优化
├── projects/                 # 实践项目
│   ├── 01-transformer-from-scratch/      # 从零实现Transformer
│   ├── 02-lora-finetune/                 # LoRA微调
│   ├── 03-rlhf-simulation/               # RLHF模拟
│   ├── 04-multimodal-rag/                # 多模态RAG
│   └── 05-mini-gpt/                      # 迷你GPT训练
├── notes/                    # 学习笔记
├── resources/                # 学习资源
└── tools/                    # 实用工具脚本
```

---

## 📖 核心论文清单

### **一、基础架构与Transformer**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **Transformer** | Attention Is All You Need | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | ⭐⭐⭐ 必读 |
| **BERT** | Pre-training of Deep Bidirectional Transformers | [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) | ⭐⭐⭐ 必读 |
| **GPT-1** | Improving Language Understanding by Generative Pre-Training | [PDF](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | ⭐⭐⭐ 必读 |
| **GPT-2** | Language Models are Unsupervised Multitask Learners | [PDF](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | ⭐⭐⭐ 必读 |
| **GPT-3** | Language Models are Few-Shot Learners | [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) | ⭐⭐⭐ 必读 |

### **二、预训练与开源模型**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **LLaMA** | LLaMA: Open and Efficient Foundation Language Models | [arXiv:2302.13971](https://arxiv.org/abs/2302.13971) | ⭐⭐⭐ 必读 |
| **LLaMA-2** | Llama 2: Open Foundation and Fine-Tuned Chat Models | [arXiv:2307.09288](https://arxiv.org/abs/2307.09288) | ⭐⭐⭐ 必读 |
| **Chinchilla** | Training Compute-Optimal Large Language Models | [arXiv:2203.15556](https://arxiv.org/abs/2203.15556) | ⭐⭐ 重要 |
| **Scaling Laws** | Scaling Laws for Neural Language Models | [arXiv:2001.08361](https://arxiv.org/abs/2001.08361) | ⭐⭐ 重要 |

### **三、高效微调与参数高效方法**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **LoRA** | LoRA: Low-Rank Adaptation of Large Language Models | [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) | ⭐⭐⭐ 必读 |
| **QLoRA** | QLoRA: Efficient Finetuning of Quantized LLMs | [arXiv:2305.14314](https://arxiv.org/abs/2305.14314) | ⭐⭐⭐ 必读 |
| **Prefix Tuning** | Prefix-Tuning: Optimizing Continuous Prompts for Generation | [arXiv:2101.00190](https://arxiv.org/abs/2101.00190) | ⭐⭐ 重要 |
| **Prompt Tuning** | The Power of Scale for Parameter-Efficient Prompt Tuning | [arXiv:2104.08691](https://arxiv.org/abs/2104.08691) | ⭐⭐ 重要 |

### **四、对齐与强化学习**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **RLHF** | Training Language Models to Follow Instructions with Human Feedback | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) | ⭐⭐⭐ 必读 |
| **DPO** | Direct Preference Optimization | [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) | ⭐⭐⭐ 必读 |
| **PPO** | Proximal Policy Optimization Algorithms | [arXiv:1707.06347](https://arxiv.org/abs/1707.06347) | ⭐⭐ 重要 |
| **SFT** | LIMA: Less Is More for Alignment | [arXiv:2305.11206](https://arxiv.org/abs/2305.11206) | ⭐⭐ 重要 |
| **Constitutional AI** | Constitutional AI: Harmlessness from AI Feedback | [arXiv:2212.08073](https://arxiv.org/abs/2212.08073) | ⭐⭐ 重要 |

### **五、多模态基础模型**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **CLIP** | Learning Transferable Visual Models From Natural Language Supervision | [arXiv:2103.00020](https://arxiv.org/abs/2103.00020) | ⭐⭐⭐ 必读 |
| **BLIP** | Bootstrapping Language-Image Pre-training | [arXiv:2201.12086](https://arxiv.org/abs/2201.12086) | ⭐⭐ 重要 |
| **BLIP-2** | Generic and Efficient Foundation Models for Vision-Language Tasks | [arXiv:2301.12597](https://arxiv.org/abs/2301.12597) | ⭐⭐ 重要 |
| **LLaVA** | Visual Instruction Tuning with Large Language Models | [arXiv:2304.08485](https://arxiv.org/abs/2304.08485) | ⭐⭐⭐ 必读 |
| **Qwen-VL** | Qwen-VL: A Versatile Vision-Language Model | [arXiv:2308.12966](https://arxiv.org/abs/2308.12966) | ⭐⭐ 重要 |

### **六、推理优化与效率**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **FlashAttention** | FlashAttention: Fast and Memory-Efficient Exact Attention | [arXiv:2205.14135](https://arxiv.org/abs/2205.14135) | ⭐⭐⭐ 必读 |
| **FlashAttention-2** | FlashAttention-2: Faster Attention with Better Parallelism | [arXiv:2307.08691](https://arxiv.org/abs/2307.08691) | ⭐⭐ 重要 |
| **vLLM** | vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180) | ⭐⭐⭐ 必读 |
| **KV Cache** | Efficient Memory Management for Large Language Model Serving | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180) | ⭐⭐ 重要 |
| **Quantization** | LLM.int8(): 8-bit Matrix Multiplication for Transformers | [arXiv:2208.07339](https://arxiv.org/abs/2208.07339) | ⭐⭐ 重要 |

### **七、视觉表征学习**
| 技术 | 论文标题 | arXiv链接 | 重要性 |
|------|----------|-----------|--------|
| **DINO** | Emerging Properties in Self-Supervised Vision Transformers | [arXiv:2104.14294](https://arxiv.org/abs/2104.14294) | ⭐⭐ 重要 |
| **DINOv2** | DINOv2: Learning Robust Visual Features without Supervision | [arXiv:2304.07193](https://arxiv.org/abs/2304.07193) | ⭐⭐ 重要 |
| **SAM** | Segment Anything | [arXiv:2304.02643](https://arxiv.org/abs/2304.02643) | ⭐⭐ 重要 |
| **VAE** | Auto-Encoding Variational Bayes | [arXiv:1312.6114](https://arxiv.org/abs/1312.6114) | ⭐⭐ 重要 |

---

## 🔧 实践项目

### 适合M1 Mac的小型项目

#### 项目1: 从零实现Transformer
- **难度**: ⭐⭐
- **时间**: 3-5天
- **资源需求**: CPU即可
- **学习目标**: 深入理解Attention机制和Transformer架构
- **代码量**: ~500行

#### 项目2: LoRA微调小模型
- **难度**: ⭐⭐
- **时间**: 2-3天
- **资源需求**: 8GB内存
- **学习目标**: 掌握参数高效微调方法
- **模型**: TinyLlama-1.1B或Phi-2 (2.7B)

#### 项目3: RLHF流程模拟
- **难度**: ⭐⭐⭐
- **时间**: 5-7天
- **资源需求**: 16GB内存
- **学习目标**: 理解奖励模型训练和PPO优化
- **简化**: 使用小模型和合成数据

#### 项目4: 多模态RAG应用
- **难度**: ⭐⭐
- **时间**: 3-4天
- **资源需求**: 8GB内存
- **学习目标**: 构建图文检索增强生成系统
- **工具**: CLIP + 轻量级LLM

#### 项目5: 迷你GPT训练
- **难度**: ⭐⭐⭐
- **时间**: 7-10天
- **资源需求**: 16GB内存
- **学习目标**: 完整预训练流程体验
- **规模**: 10M-100M参数

---

## 🛠️ 开发环境配置

### M1 Mac推荐配置

```bash
# 1. 安装Homebrew (如果还没有)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 安装Python 3.11
brew install python@3.11

# 3. 创建虚拟环境
python3.11 -m venv llm_env
source llm_env/bin/activate

# 4. 安装核心库
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers accelerate peft bitsandbytes
pip install datasets tokenizers sentencepiece
pip install wandb tensorboard

# 5. 安装M1优化版本
pip install mlx  # Apple Silicon优化的机器学习框架
```

### 推荐工具

| 工具 | 用途 | 安装命令 |
|------|------|----------|
| **Ollama** | 本地运行LLM | `brew install ollama` |
| **LM Studio** | 模型管理和推理 | [下载](https://lmstudio.ai/) |
| **Hugging Face Hub** | 模型下载 | `pip install huggingface_hub` |
| **Weights & Biases** | 实验跟踪 | `pip install wandb` |

---

## 📚 学习资源

### 在线课程
- [Stanford CS224N: NLP with Deep Learning](http://web.stanford.edu/class/cs224n/)
- [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/)
- [Fast.ai: Practical Deep Learning for Coders](https://www.fast.ai/)

### 博客与教程
- [Hugging Face Blog](https://huggingface.co/blog)
- [Lilian Weng's Blog](https://lilianweng.github.io/)
- [Jay Alammar's Visualizations](https://jalammar.github.io/)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

### 开源项目
- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)
- [unsloth](https://github.com/unslothai/unsloth) - M1优化训练

---

## 🎯 学习建议

### 阅读论文的方法
1. **第一遍**: 读摘要、引言、结论，了解主要贡献
2. **第二遍**: 看图和表，理解实验设置
3. **第三遍**: 深入方法部分，理解技术细节
4. **实践**: 复现核心算法或运行开源代码

### 代码实践原则
1. **从小开始**: 先用小模型验证想法
2. **逐步扩展**: 确认可行后再扩大规模
3. **记录实验**: 使用W&B或TensorBoard跟踪
4. **分享成果**: 写博客或GitHub记录学习过程

### M1 Mac优化技巧
1. 使用`torch.compile`加速PyTorch代码
2. 利用`mlx`框架进行Apple Silicon优化
3. 使用量化模型减少内存占用
4. 开启内存交换以支持更大模型

---

## 📈 进阶路线

完成本仓库学习后，可以探索：

1. **Agent开发**: LangChain, AutoGPT, BabyAGI
2. **模型压缩**: 知识蒸馏、剪枝、量化
3. **长上下文**: 位置编码改进、Ring Attention
4. **多模态**: GPT-4V, Gemini, Claude 3
5. **前沿研究**: MoE, Mixture of Depths, Mamba

---

## 🤝 贡献指南

欢迎提交：
- 论文阅读笔记
- 代码实现
- 学习心得
- 问题讨论

---

## 📄 License

MIT License - 自由学习和使用

---

> **开始你的LLM学习之旅吧！** 🚀
