﻿# SynapseX CLI ⚡

Advanced FiveM Pentest Tool - CLI

---

- 🔍 Resolve `cfx.re` links to real server IP
- 🧪 Scan and retrieve server info (status, players, tags, etc.)
- 🧩 Modular command structure
- 🛠️ Easily extendable with your own commands

---

## 🚀 Features

- Resolve CFX join codes to IP:Port
- Retrieve live server data from `/info.json` and `/players.json`
- Modular command handler system
- CLI-based, no GUI, pure terminal experience

---

## 📦 Installation

```bash
git clone https://github.com/Zalgo-Dev/Synapsex-cli.git
cd Synapsex-cli
pip install -r requirements.txt
```

---

## 💻 Usage

```bash
python run.py
```

You will enter an simple interactive CLI interface:

```bash
=== SynapseX Terminal ===
Type `help` to show all available commands.

SynapseX>
```

---

## 🧩 Available Commands

| Command | Description |
|---|---|
| `resolve <cfx_token>` | Resolve a cfx.re token or link to IP:Port |
| `scan <cfx_link / cfx_token>` | Show server informations |
| `help` | Show all available commands |
| `exit / ctrl + c` | Exit the CLI |

---

## 🗂 Project Structure

```
└── 📁SynapseX - CLI
    └── 📁synapsex
        └── __init__.py
        └── 📁commands
            └── resolve.py
            └── scan.py
            └── your_command.py
        └── 📁core
            └── __init__.py
            └── terminal.py
        └── 📁utils
            └── __init__.py
            └── server.py
    └── README.md
    └── run.py
```

---

## ➕ Creating a Custom Command

1. Create a file in synapsex/commands/your_command.py
2. Use this template:

```python
class Command:
    name = "yourcommand"
    desc = "Your command description"
    usage = "yourcommand <args>"

    def run(self, args):
        print("Hello from yourcommand!")
```

**New commands are automatically loaded by the command manager.**

---

## 🙋‍♂️ Contributing
Pull requests are welcome! Feel free to open an issue or suggest a feature.

---

## ⭐ Credits
Created by **ZalgoDev** — follow me for more open-source security tools.
