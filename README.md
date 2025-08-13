# LLMfreshman
Study some papers and knowledge about MMLLM and AIGC.

以下为您整理的**大模型核心技术论文arXiv地址清单**，包含每个技术的核心论文及关键衍生工作，按技术领域分类：

---

### **一、多模态基础模型**
| 技术       | 论文标题                                                                 | arXiv链接                                                                 |
|------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **CLIP**   | Learning Transferable Visual Models From Natural Language Supervision    | [arXiv:2103.00020](https://arxiv.org/abs/2103.00020)                      |
| **BLIP**   | Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding | [arXiv:2201.12086](https://arxiv.org/abs/2201.12086)                |
| **BLIP-2** | Generic and Efficient Foundation Models for Vision-Language Tasks        | [arXiv:2301.12597](https://arxiv.org/abs/2301.12597)                      |

---

### **二、对齐与强化学习技术**
| 技术        | 论文标题                                                                 | arXiv链接                                                                 |
|-------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **RLHF**    | Training Language Models to Follow Instructions with Human Feedback     | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) (InstructGPT)       |
| **SFT**     | LIMA: Less Is More for Alignment                                         | [arXiv:2305.11206](https://arxiv.org/abs/2305.11206)                      |
| **PPO**     | Proximal Policy Optimization Algorithms                                 | [arXiv:1707.06347](https://arxiv.org/abs/1707.06347)                      |
| **DPO**     | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)                |
| **RPO**     | Rejection Sampling Improves Reasoning in LLMs                            | [arXiv:2310.00635](https://arxiv.org/abs/2310.00635)                      |
| **GRPO**    | Gradient Regularization Improves DPO                                     | [arXiv:2404.07837](https://arxiv.org/abs/2404.07837) (2024腾讯)          |

---

### **三、大模型架构与训练**
| 技术         | 论文标题                                                                 | arXiv链接                                                                 |
|--------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **LLaMA**    | LLaMA: Open and Efficient Foundation Language Models                     | [arXiv:2302.13971](https://arxiv.org/abs/2302.13971)                      |
| **LLaVA**    | Visual Instruction Tuning with Large Language Models                     | [arXiv:2304.08485](https://arxiv.org/abs/2304.08485)                      |
| **Qwen-VL**  | Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization... | [arXiv:2308.12966](https://arxiv.org/abs/2308.12966)                |
| **Swift**    | Swift: Optimized Training of Large Language Models on GPU Clusters       | [arXiv:2402.00819](https://arxiv.org/abs/2402.00819) (华为)               |

---

### **四、视觉表征学习**
| 技术         | 论文标题                                                                 | arXiv链接                                                                 |
|--------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **DINO**     | Emerging Properties in Self-Supervised Vision Transformers              | [arXiv:2104.14294](https://arxiv.org/abs/2104.14294)                      |
| **DINOv2**   | DINOv2: Learning Robust Visual Features without Supervision             | [arXiv:2304.07193](https://arxiv.org/abs/2304.07193)                      |
| **Metric3D** | Metric3D: Towards Zero-shot Metric 3D Prediction from A Single Image    | [arXiv:2307.10984](https://arxiv.org/abs/2307.10984)                      |
| **SAM**      | Segment Anything                                                         | [arXiv:2304.02643](https://arxiv.org/abs/2304.02643)                      |
| **VAE**      | Auto-Encoding Variational Bayes                                          | [arXiv:1312.6114](https://arxiv.org/abs/1312.6114)                        |

---

### **五、高效微调与推理**
| 技术           | 论文标题                                                                 | arXiv链接                                                                 |
|----------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **LoRA**       | LoRA: Low-Rank Adaptation of Large Language Models                       | [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)                      |
| **QLoRA**      | QLoRA: Efficient Finetuning of Quantized LLMs                            | [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)                      |
| **vLLM**       | vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention              | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)                      |
| **FlashAttention-2** | FlashAttention-2: Faster Attention with Better Parallelism            | [arXiv:2307.08691](https://arxiv.org/abs/2307.08691)                      |

---

### **关键说明**
1. **版本注意**：
   - **Qwen-VL**：最新版论文参考 [Qwen技术报告](https://qwenlm.github.io/zh/tech_memo/)（arXiv更新滞后）
   - **Swift**：华为优化框架论文含工程细节
2. **衍生工作推荐**：
   - **LLaVA-1.5**：[arXiv:2310.03744](https://arxiv.org/abs/2310.03744)（性能提升版）
   - **DPO变种**：
     - IPO ([arXiv:2310.12036](https://arxiv.org/abs/2310.12036))
     - KTO ([arXiv:2402.01306](https://arxiv.org/abs/2402.01306))
3. **实用资源**：
   - FlashAttention代码库：[github.com/Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
   - vLLM生产部署指南：[vLLM官方文档](https://vllm.readthedocs.io/)

> 建议按技术演进顺序阅读：  
> **CLIP → LLaMA → LoRA → RLHF/DPO → LLaVA → vLLM**  
> 配合代码实践（Hugging Face/官方GitHub）效果更佳。