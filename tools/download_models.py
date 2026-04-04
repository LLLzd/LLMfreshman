#!/usr/bin/env python3
"""
模型下载工具
用于下载适合M1 Mac的小型模型
"""

import os
import sys
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse

# 适合M1 Mac的模型列表
M1_COMPATIBLE_MODELS = {
    "tinyllama": {
        "name": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "description": "1.1B参数，适合快速实验",
        "memory": "~4GB (INT8)",
        "size": "2.2GB"
    },
    "phi2": {
        "name": "microsoft/phi-2",
        "description": "2.7B参数，性能优秀",
        "memory": "~6GB (INT8)",
        "size": "5.2GB"
    },
    "qwen2-0.5b": {
        "name": "Qwen/Qwen2-0.5B-Instruct",
        "description": "0.5B参数，中文友好",
        "memory": "~2GB (INT8)",
        "size": "1GB"
    },
    "qwen2-1.5b": {
        "name": "Qwen/Qwen2-1.5B-Instruct",
        "description": "1.5B参数，中文友好",
        "memory": "~3GB (INT8)",
        "size": "3GB"
    },
    "gemma-2b": {
        "name": "google/gemma-2b-it",
        "description": "2B参数，Google开源",
        "memory": "~4GB (INT8)",
        "size": "4.8GB"
    },
    "stablelm-2": {
        "name": "stabilityai/stablelm-2-1_6b",
        "description": "1.6B参数，Stability AI",
        "memory": "~3GB (INT8)",
        "size": "3.2GB"
    }
}


def list_models():
    """列出所有可用的模型"""
    print("\n📋 适合M1 Mac的模型列表:\n")
    print(f"{'名称':<15} {'描述':<30} {'内存需求':<15} {'大小':<10}")
    print("-" * 70)
    for key, info in M1_COMPATIBLE_MODELS.items():
        print(f"{key:<15} {info['description']:<30} {info['memory']:<15} {info['size']:<10}")
    print()


def download_model(model_key: str, cache_dir: str = None):
    """下载指定模型"""
    if model_key not in M1_COMPATIBLE_MODELS:
        print(f"❌ 未知模型: {model_key}")
        print("可用模型:", ", ".join(M1_COMPATIBLE_MODELS.keys()))
        return False
    
    model_info = M1_COMPATIBLE_MODELS[model_key]
    model_name = model_info["name"]
    
    print(f"\n📥 正在下载模型: {model_name}")
    print(f"💾 预计大小: {model_info['size']}")
    print(f"📝 {model_info['description']}")
    print()
    
    try:
        # 下载tokenizer
        print("🔤 下载Tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            cache_dir=cache_dir,
            trust_remote_code=True
        )
        
        # 下载模型
        print("🤖 下载模型...")
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            cache_dir=cache_dir,
            trust_remote_code=True,
            torch_dtype="auto"
        )
        
        print(f"\n✅ 模型下载完成: {model_name}")
        
        # 测试模型
        print("\n🧪 测试模型...")
        test_input = "Hello, I am a language model"
        inputs = tokenizer(test_input, return_tensors="pt")
        
        print(f"   输入: {test_input}")
        print(f"   输入IDs: {inputs['input_ids'].shape}")
        print("   模型可以正常加载和运行！")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 下载失败: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="下载适合M1 Mac的LLM模型",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python download_models.py --list              # 列出所有模型
  python download_models.py tinyllama           # 下载TinyLlama
  python download_models.py qwen2-1.5b --cache ./models  # 指定缓存目录
        """
    )
    
    parser.add_argument(
        "model",
        nargs="?",
        help="要下载的模型名称"
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="列出所有可用模型"
    )
    
    parser.add_argument(
        "--cache", "-c",
        default=None,
        help="模型缓存目录 (默认: ~/.cache/huggingface)"
    )
    
    args = parser.parse_args()
    
    if args.list or not args.model:
        list_models()
        if not args.model:
            print("💡 使用: python download_models.py <model_name>")
        return
    
    # 下载模型
    success = download_model(args.model, args.cache)
    
    if success:
        print("\n🎉 完成！")
        print(f"💡 模型已保存到: {args.cache or '~/.cache/huggingface'}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
