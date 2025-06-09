# synapsex/core/terminal.py

import importlib
import pkgutil

COMMANDS = {}

def display_banner():
    print("\n=== SynapseX Terminal ===")
    print("Type `help` to show all available commands.\n")

def load_commands():
    from synapsex import commands
    package_path = commands.__path__
    for loader, module_name, is_pkg in pkgutil.iter_modules(package_path):
        module = importlib.import_module(f"synapsex.commands.{module_name}")
        if hasattr(module, "Command"):
            cmd_instance = module.Command()
            COMMANDS[cmd_instance.name] = cmd_instance

def run_terminal():
    display_banner()
    load_commands()

    while True:
        try:
            cmd = input("SynapseX> ").strip()
            if cmd in ("exit", "quit"):
                print("Exiting ...")
                break
            elif cmd == "help":
                print("Available commands:")
                for command in COMMANDS.values():
                    print(f" - {command.name}: {command.desc}")
                continue

            if not cmd:
                continue

            cmd_name, *args = cmd.split()
            if cmd_name in COMMANDS:
                COMMANDS[cmd_name].run(args)
            else:
                print(f"Unknown command: {cmd_name}")

        except KeyboardInterrupt:
            print("\n[!] Exiting...")
            break
        except Exception as e:
            print(f"[Erreur] {e}")
