# test_dataset.py
import datasets
import os
import json

dataset_path = "/home/fuzhizhang.fzz/data/OpenR1-Math-220k"

print(f"=== 检查目录结构 ===")
print(f"Path exists: {os.path.exists(dataset_path)}")
print(f"Is directory: {os.path.isdir(dataset_path)}")

print(f"\n=== 目录内容 ===")
try:
    contents = os.listdir(dataset_path)
    for item in contents:
        item_path = os.path.join(dataset_path, item)
        if os.path.isdir(item_path):
            print(f"DIR:  {item}")
        else:
            print(f"FILE: {item}")
except Exception as e:
    print(f"Error listing directory: {e}")

print(f"\n=== 检查关键文件 ===")
key_files = ['dataset_info.json', 'state.json', 'data']
for file in key_files:
    file_path = os.path.join(dataset_path, file)
    exists = os.path.exists(file_path)
    print(f"{file}: {'存在' if exists else '不存在'}")
    
    if exists and file.endswith('.json'):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                print(f"  -> JSON 内容概览: {list(data.keys())}")
        except Exception as e:
            print(f"  -> JSON 读取失败: {e}")

print(f"\n=== 尝试加载数据集 ===")
try:
    dataset = datasets.load_from_disk(dataset_path)
    print("✅ 数据集加载成功!")
    print(f"数据集信息: {dataset}")
except Exception as e:
    print(f"❌ 数据集加载失败: {e}")
    print(f"错误类型: {type(e)}")