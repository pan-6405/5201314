import requests
import yaml

def check_node(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        r = requests.get("https://www.google.com", proxies=proxies, timeout=5)
        return r.status_code == 200
    except:
        return False

with open("raw_nodes.yaml", "r", encoding="utf-8") as f:
    raw = yaml.safe_load(f)

live_nodes = []
dead_nodes = []

for node in raw["proxies"]:
    proxy = f'{node["server"]}:{node["port"]}'
    if check_node(proxy):
        live_nodes.append(node)
    else:
        dead_nodes.append(node)

with open("live_nodes.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"proxies": live_nodes}, f, allow_unicode=True)

with open("dead_nodes.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"proxies": dead_nodes}, f, allow_unicode=True)
