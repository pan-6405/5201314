import yaml
import json
from datetime import datetime

# 加载检测结果
with open("live_nodes.yaml", "r", encoding="utf-8") as f:
    live_nodes = yaml.safe_load(f)["proxies"]

with open("dead_nodes.yaml", "r", encoding="utf-8") as f:
    dead_nodes = yaml.safe_load(f)["proxies"]

# 加载记忆池
try:
    with open("memory_pool.json", "r", encoding="utf-8") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {}

today = datetime.now().strftime("%Y-%m-%d")

# 更新活跃节点
for node in live_nodes:
    name = node["name"]
    memory[name] = {
        "last_seen": today,
        "status": "alive",
        "fail_count": 0,
        "latency": None  # 可扩展为测速结果
    }

# 更新失效节点
for node in dead_nodes:
    name = node["name"]
    if name in memory:
        memory[name]["fail_count"] += 1
        memory[name]["status"] = "dead"
    else:
        memory[name] = {
            "last_seen": today,
            "status": "dead",
            "fail_count": 1,
            "latency": None
        }

# 自动淘汰连续失败超过 3 次的节点
cleaned_memory = {
    name: info for name, info in memory.items()
    if info["fail_count"] <= 3
}

# 保存更新后的记忆池
with open("memory_pool.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_memory, f, indent=2, ensure_ascii=False)
