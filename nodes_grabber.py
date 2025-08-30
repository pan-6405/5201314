import requests
import base64
import yaml

def fetch_nodes(urls):
    all_nodes = []
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            content = base64.b64decode(res.text).decode()
            data = yaml.safe_load(content)
            if "proxies" in data:
                all_nodes.extend(data["proxies"])
        except Exception as e:
            print(f"❌ Failed to fetch from {url}: {e}")
    return all_nodes

if __name__ == "__main__":
    with open("sources.yaml", "r", encoding="utf-8") as f:
        urls = yaml.safe_load(f)["sources"]
    nodes = fetch_nodes(urls)
    with open("raw_nodes.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"proxies": nodes}, f, allow_unicode=True)
