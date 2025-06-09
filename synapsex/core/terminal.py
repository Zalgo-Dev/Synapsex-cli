import sys

def display_banner():
    print("\n=== SynapseX Terminal ===")
    print("Type `help` for show all available commands.\n")

def run():
    display_banner()
    while True:
        try:
            cmd = input("SynapseX> ").strip()
            if cmd in ("exit", "quit"):
                print("Exiting ...")
                break
            elif cmd == "help":
                print("Commands :\n - resolve <cfx_token>\n - exit")
            elif cmd.startswith("resolve "):
                from synapsex.utils.resolve_cfx import resolve
                cfx_url = cmd.split(" ", 1)[1]
                print(resolve(cfx_url))
            else:
                print("Unknow command.")
        except KeyboardInterrupt:
            print("\n[!] Exiting...")
            break
            
        except Exception as e:
            print(f"[Erreur] {e}")
