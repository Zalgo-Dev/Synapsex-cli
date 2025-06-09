# synapsex/commands/resolve.py
from synapsex.utils.server import Server

class Command:
    name = "resolve"
    desc = "Resolve a CFX.re URL to IP:Port"
    usage = "resolve <cfx_code>"

    def run(self, args):
        if not args:
            print(f"Usage: {self.usage}")
            return
        try:
            server = Server(args[0])
            print(f"[+] Resolved IP: {server.ip}")
        except Exception as e:
            print(f"[!] Error: {e}")
