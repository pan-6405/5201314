import os
import json

def check_file(path):
    return os.path.exists(path) and os.path.getsize(path) > 0

status = {
    "memory_pool": check_file("memory_pool.yaml"),
    "config_template": check_file("config_template.yaml"),
    "node_sources": check_file("nodes.txt"),
    "strategy_groups": check_file("strategy_groups.yaml")
}

with open("check_result.json", "w") as f:
    json.dump(status, f)

if not all(status.values()):
    print("❌ 检查失败：部分关键文件无效")
    exit(1)
else:
    print("✅ 所有关键文件有效，继续执行")
