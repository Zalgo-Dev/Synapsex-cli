# synapsex/commands/scan.py
from synapsex.utils.server import Server

class Command:
    name = "scan"
    desc = "Scan server info from CFX or IP"
    usage = "scan <cfx_code|ip:port>"

    def run(self, args):
        if not args:
            print(f"Usage: {self.usage}")
            return
        try:
            server = Server(args[0])
            print(f"[+] IP: {server.ip}")
            print(f"[+] Status: {server.get_server_status()}")
            print(f"[+] Name: {server.get_server_name()}")
            print(f"[+] Desc: {server.get_server_desc()}")
            print(f"[+] Players: {server.get_players()}")
            print(f"[+] Max Players: {server.get_max_players()}")
            print(f"[+] Tags: {server.get_tags()}")
        except Exception as e:
            print(f"[!] Error during scan: {e}")
