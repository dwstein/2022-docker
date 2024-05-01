# app/models/channel.py

import json
from dataclasses import dataclass, field

@dataclass
class Channel:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ""

def load_channels(filepath: str) -> dict[str, Channel]:
    with open(filepath, encoding="utf8") as file:
        channels_raw = json.load(file)
        channels = {item['id']: Channel(**item) for item in channels_raw}
    return channels

channels = load_channels("channels.json")
