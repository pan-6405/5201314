import json
import yaml

# 加载记忆池
with open("memory_pool.json", "r", encoding="utf-8") as f:
    memory = json.load(f)

# 选出活跃节点
active_nodes = [
    {"name": name}
    for name, info in memory.items()
    if info["status"] == "alive" and info["fail_count"] <= 2
]

# 构建策略组
group = {
    "name": "自动选择",
    "type": "select",
    "proxies": [node["name"] for node in active_nodes]
}

# 保存策略组
with open("strategy_group.yaml", "w", encoding="utf-8") as f:
    yaml.dump([group], f, allow_unicode=True)
