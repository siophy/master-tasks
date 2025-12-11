# restart_space.py
import os
import sys
from huggingface_hub import HfApi

# 从命令行参数获取 repo_id（支持多 Space 循环调用）
if len(sys.argv) > 1:
    repo_id = sys.argv[1].strip()
else:
    repo_id = ""

token = os.getenv("HF_TOKEN", "").strip()

if not repo_id:
    print("错误：缺少 Space ID")
    sys.exit(1)

if not token:
    print("错误：缺少 HF_TOKEN")
    sys.exit(1)

print(f"正在唤醒 Space: {repo_id}")

try:
    HfApi().restart_space(repo_id=repo_id, token=token)
    print(f"{repo_id} 重启请求已成功发送")
except Exception as e:
    print(f"{repo_id} 重启失败: {e}")
    sys.exit(1)
