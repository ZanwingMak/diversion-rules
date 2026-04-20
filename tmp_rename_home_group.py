from pathlib import Path


ROOT = Path(__file__).resolve().parent

FILES = [
    ROOT / "config" / "personal" / "marvin.ini",
    ROOT / "config" / "personal" / "marvin-no-zhuanxian.ini",
    ROOT / "subconverter" / "snippets" / "groups.toml",
    ROOT / "subconverter" / "snippets" / "groups-no-zhuanxian.toml",
]


for path in FILES:
    text = path.read_text(encoding="utf-8")
    updated = text.replace("[]家宽", "[]家宽节点")
    updated = updated.replace("custom_proxy_group=家宽`", "custom_proxy_group=家宽节点`")
    updated = updated.replace('name = "家宽"', 'name = "家宽节点"')
    if updated != text:
        path.write_text(updated, encoding="utf-8", newline="\n")
        print(f"updated: {path}")
