# 预训练与开源模型论文

本目录包含预训练技术、开源模型（LLaMA等）相关的经典论文。

## 论文列表

### 必读论文

1. **LLaMA: Open and Efficient Foundation Language Models** (2023)
   - 作者: Touvron et al. (Meta)
   - 贡献: 开源高效基础语言模型，推动开源社区发展
   - 链接: [arXiv:2302.13971](https://arxiv.org/abs/2302.13971)
   - 状态: ⏳ 待阅读

2. **Llama 2: Open Foundation and Fine-Tuned Chat Models** (2023)
   - 作者: Touvron et al. (Meta)
   - 贡献: LLaMA改进版，包含对话优化版本
   - 链接: [arXiv:2307.09288](https://arxiv.org/abs/2307.09288)
   - 状态: ⏳ 待阅读

3. **Chinchilla: Training Compute-Optimal Large Language Models** (2022)
   - 作者: Hoffmann et al. (DeepMind)
   - 贡献: 提出计算最优的训练策略，数据量与模型大小关系
   - 链接: [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
   - 状态: ⏳ 待阅读

4. **Scaling Laws for Neural Language Models** (2020)
   - 作者: Kaplan et al. (OpenAI)
   - 贡献: 系统研究语言模型的缩放规律
   - 链接: [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)
   - 状态: ⏳ 待阅读

## 阅读建议

**阅读顺序**: Scaling Laws → Chinchilla → LLaMA → LLaMA-2

**重点理解**:
- 模型规模与数据量的关系
- 训练计算最优配置
- 开源模型的训练细节
- 预训练数据处理方法

## 实践建议

1. 使用Hugging Face加载LLaMA模型进行推理
2. 尝试使用LLaMA-2进行微调
3. 理解不同规模模型的性能差异

## 笔记

- 使用 `../paper_template.md` 模板记录阅读笔记
- 每读完一篇论文，更新上面的状态为 ✅ 已完成
