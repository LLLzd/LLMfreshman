# M1 Mac LLM开发优化指南

> 针对16GB内存Apple Silicon Mac的优化技巧

---

## 🍎 硬件特性

### M1芯片优势
- **统一内存架构**: CPU和GPU共享内存，减少数据拷贝
- **Neural Engine**: 16核神经网络引擎，加速ML推理
- **高效能耗比**: 相同性能下功耗更低

### 16GB内存限制
- 无法加载大模型（>7B参数）
- 需要量化和内存优化
- 适合小模型实验和原型开发

---

## ⚡ 性能优化技巧

### 1. PyTorch优化

```python
import torch

# 使用MPS后端（Apple GPU）
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# 启用tf32（如果支持）
torch.backends.cuda.matmul.allow_tf32 = True

# 使用torch.compile加速（PyTorch 2.0+）
model = torch.compile(model)
```

### 2. 模型量化

```python
from transformers import AutoModelForCausalLM

# 8bit量化
model = AutoModelForCausalLM.from_pretrained(
    "model_name",
    load_in_8bit=True,
    device_map="auto"
)

# 4bit量化（更激进）
model = AutoModelForCausalLM.from_pretrained(
    "model_name",
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    device_map="auto"
)
```

### 3. MLX框架使用

```python
import mlx.core as mx

# MLX是Apple Silicon优化的ML框架
# 比PyTorch MPS后端更高效

# 创建数组
a = mx.array([1, 2, 3, 4])

# 矩阵运算
b = mx.random.normal((1000, 1000))
c = mx.matmul(b, b.T)
```

### 4. 内存管理

```python
import gc
import torch

# 及时清理缓存
del model
del optimizer
gc.collect()
torch.mps.empty_cache()  # 清空MPS缓存

# 使用梯度检查点
from torch.utils.checkpoint import checkpoint

# 混合精度训练
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
```

---

## 🛠️ 推荐工具链

### 模型推理
| 工具 | 用途 | 优势 |
|------|------|------|
| **Ollama** | 本地运行LLM | 自动M1优化，简单易用 |
| **LM Studio** | GUI模型管理 | 可视化，支持多种格式 |
| **llama.cpp** | 高效推理 | C++实现，Metal加速 |
| **mlx-lm** | MLX推理 | Apple Silicon原生优化 |

### 训练框架
| 框架 | 适用场景 | 特点 |
|------|----------|------|
| **PyTorch** | 通用训练 | 社区大，文档全 |
| **MLX** | Apple Silicon | 性能最优 |
| **unsloth** | 微调 | 2-5倍加速，省内存 |

---

## 📊 模型内存需求参考

### 推理内存（约估值）

| 模型大小 | FP16 | INT8 | INT4 |
|----------|------|------|------|
| 1B | 2GB | 1GB | 0.5GB |
| 3B | 6GB | 3GB | 1.5GB |
| 7B | 14GB | 7GB | 3.5GB |
| 13B | 26GB | 13GB | 6.5GB |

**16GB Mac建议**: 最大7B INT8或13B INT4

### 训练内存（LoRA微调）

| 基础模型 | LoRA Rank | 预估内存 |
|----------|-----------|----------|
| 1B | 16 | 4-6GB |
| 3B | 16 | 8-12GB |
| 7B | 8 | 14-16GB |

---

## 🔧 环境配置最佳实践

### 1. Conda环境（推荐）

```bash
# 创建环境
conda create -n llm python=3.11
conda activate llm

# 安装PyTorch
conda install pytorch torchvision torchaudio -c pytorch

# 安装其他包
pip install transformers datasets accelerate peft
```

### 2. 虚拟环境

```bash
# 创建虚拟环境
python3.11 -m venv llm_env
source llm_env/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3. 系统优化

```bash
# 增加交换空间（如果需要）
sudo dd if=/dev/zero of=/private/var/vm/swapfile bs=1g count=16

# 关闭内存压缩（可选）
sudo nvram boot-args="vm_compressor=1"
```

---

## 🚀 加速技巧

### 1. 使用Metal Performance Shaders

```python
# 确保使用MPS后端
import torch
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("Using MPS backend")
else:
    device = torch.device("cpu")
    print("MPS not available, using CPU")
```

### 2. 批处理优化

```python
# 使用合适的batch size
# M1建议: 推理时batch size 1-4，训练时根据内存调整

# 动态批处理
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="model_name",
    device_map="auto",
    batch_size=2  # 根据内存调整
)
```

### 3. 模型分片

```python
# 使用device_map自动分片
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "large_model",
    device_map="auto",  # 自动分配到CPU和GPU
    max_memory={0: "14GB", "cpu": "30GB"}  # 限制内存使用
)
```

---

## 📈 性能监控

### 内存监控

```bash
# 命令行监控
vm_stat 1

# 或使用活动监视器
open -a "Activity Monitor"
```

### Python中监控

```python
import psutil
import torch

def print_memory_stats():
    # CPU内存
    cpu_mem = psutil.virtual_memory()
    print(f"CPU Memory: {cpu_mem.percent}% used")
    
    # MPS内存
    if torch.backends.mps.is_available():
        print(f"MPS allocated: {torch.mps.current_allocated_memory() / 1e9:.2f} GB")
```

---

## 🐛 常见问题

### 问题1: MPS后端OOM
**解决**: 减少batch size，使用更小模型，或切换到CPU

### 问题2: 模型加载慢
**解决**: 使用SSD，开启内存交换，或预加载模型

### 问题3: 精度问题
**解决**: MPS某些操作可能有精度问题，尝试使用CPU执行特定操作

```python
# 强制使用CPU执行某些操作
with torch.no_grad():
    # 敏感操作在CPU上执行
    output_cpu = model.cpu()(input.cpu())
    output = output_cpu.to(device)
```

---

## 📚 参考资源

- [PyTorch MPS文档](https://pytorch.org/docs/stable/notes/mps.html)
- [MLX官方文档](https://ml-explore.github.io/mlx/)
- [Apple ML Performance](https://developer.apple.com/metal/performance/)
- [Hugging Face M1优化](https://huggingface.co/docs/transformers/perf_infer_gpu_one)

---

> 💡 **提示**: M1 Mac虽然有限制，但通过优化完全可以进行高效的LLM学习和开发！
