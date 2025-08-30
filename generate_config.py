import yaml

# 加载活跃节点
with open("live_nodes.yaml", "r", encoding="utf-8") as f:
    nodes = yaml.safe_load(f)["proxies"]

# 加载策略组
with open("strategy_group.yaml", "r", encoding="utf-8") as f:
    groups = yaml.safe_load(f)

# 构建 Clash 配置
config = {
    "port": 7890,
    "socks-port": 7891,
    "allow-lan": True,
    "mode": "rule",
    "log-level": "info",
    "proxies": nodes,
    "proxy-groups": groups,
    "rules": [
        "MATCH,自动选择"
    ]
}

# 保存最终配置
with open("final_config.yaml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, allow_unicode=True, sort_keys=False)
