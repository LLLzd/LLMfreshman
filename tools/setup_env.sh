#!/bin/bash
# LLMfreshman 环境配置脚本
# 适用于 Apple Silicon Mac (M1/M2/M3)

set -e

echo "🚀 开始配置LLMfreshman开发环境..."

# 检查操作系统
if [[ $(uname -m) != "arm64" ]]; then
    echo "⚠️  警告: 此脚本为Apple Silicon Mac优化"
fi

# 检查Python版本
echo "📦 检查Python环境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到Python3，请先安装Python 3.11"
    echo "建议: brew install python@3.11"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python版本: $PYTHON_VERSION"

# 创建虚拟环境
echo "🌍 创建虚拟环境..."
if [ ! -d "../venv" ]; then
    python3 -m venv ../venv
    echo "✅ 虚拟环境创建完成"
else
    echo "✅ 虚拟环境已存在"
fi

# 激活虚拟环境
source ../venv/bin/activate

# 升级pip
echo "⬆️  升级pip..."
pip install --upgrade pip

# 安装PyTorch (CPU版本，M1优化)
echo "🔥 安装PyTorch (Apple Silicon优化)..."
pip install torch torchvision torchaudio

# 安装Transformers和相关库
echo "🤗 安装Hugging Face库..."
pip install transformers datasets accelerate
pip install peft bitsandbytes

# 安装tokenizers
echo "🔤 安装tokenizers..."
pip install tokenizers sentencepiece

# 安装实验跟踪工具
echo "📊 安装实验跟踪工具..."
pip install wandb tensorboard

# 安装其他常用工具
echo "🛠️  安装其他工具..."
pip install numpy pandas matplotlib seaborn
pip install jupyter ipython
pip install tqdm rich

# 安装MLX (Apple Silicon专用)
echo "🍎 安装MLX (Apple Silicon优化框架)..."
pip install mlx

# 安装代码质量工具
echo "📝 安装代码质量工具..."
pip install black isort flake8

echo ""
echo "✅ 环境配置完成！"
echo ""
echo "📋 已安装的包:"
echo "  - PyTorch (Apple Silicon优化)"
echo "  - Transformers, Datasets, Accelerate"
echo "  - PEFT, BitsAndBytes"
echo "  - Weights & Biases, TensorBoard"
echo "  - MLX (Apple Silicon专用)"
echo "  - Jupyter, NumPy, Pandas, Matplotlib"
echo ""
echo "🎯 下一步:"
echo "  1. 激活环境: source venv/bin/activate"
echo "  2. 运行测试: python -c 'import torch; print(torch.__version__)'"
echo "  3. 开始第一个项目: cd projects/01-transformer-from-scratch"
echo ""
echo "💡 提示:"
echo "  - 使用 'wandb login' 登录Weights & Biases"
echo "  - 使用 'huggingface-cli login' 登录Hugging Face"
echo ""
