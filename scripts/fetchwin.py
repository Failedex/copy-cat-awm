#! /usr/bin/env python3
from i3ipc import Connection
from iconfetch import fetch
import json
import time

memo = {}
def get_icon(name):
    name = name.lower()
    if name in memo:
        return memo[name]
    
    memo[name] = fetch(name) or fetch("unknown")
    return memo[name]

state = {}

def equivalent(a, b):
    return (
        a.name == b.name and 
        a.rect.x == b.rect.x and
        a.rect.y == b.rect.y and
        a.rect.width == b.rect.width and
        a.rect.height == b.rect.height
    )

def fetch_win():
    root = i3.get_tree()
    focused = root.find_focused()
    if not focused:
        return
    fws = focused.workspace()
    data = []

    changes = False
    unseen = set(state.keys())

    for l in fws.descendants():
        if not l.pid or not l.app_id:
            continue

        data.append(dict(
            pid = l.pid,
            icon = get_icon(l.app_id),
            name = l.name,
            focused = l.focused,
            x = l.rect.x-90,
            y = l.rect.y,
            width = l.rect.width,
            height = l.rect.height,
        ))

        if l.pid not in state or not equivalent(state[l.pid], l):
            changes = True

        state[l.pid] = l
        if l.pid in unseen:
            unseen.remove(l.pid)

    for u in unseen:
        changes = True
        del state[u]

    if changes or len(data) == 0:
        print(json.dumps(data), flush=True)

def main():
    while True:
        fetch_win()
        time.sleep(1/60)

if __name__ == "__main__":
    try:
        i3 = Connection(auto_reconnect = True)
        # i3.command("gaps inner all set 90")

        main()
    except KeyboardInterrupt:
        pass
    
    finally:
        # i3.command("gaps inner all set 15")
        pass
