# synapsex/utils/server.py
import requests

class Server:
    def __init__(self, address, timeout=30):
        self.timeout = timeout
        self.ip = None
        self.errmsg = "Error Occurred"

        if ":" in address:
            self.ip = address
            print("Connected to server:", self.ip)
        else:
            self._resolve_cfx(address)

    def _resolve_cfx(self, code):
        try:
            url = code
            if not url.startswith("https://"):
                if not url.startswith("cfx.re/join/"):
                    url = "https://cfx.re/join/" + code
                else:
                    url = "https://" + url
            response = requests.get(url, timeout=self.timeout, allow_redirects=False)
            redirect = response.headers.get("x-citizenfx-url")
            if redirect:
                self.ip = redirect.replace("http://", "").rstrip("/")
                print("Connected to server:", self.ip)
        except Exception as e:
            print("Error resolving CFX.re URL:", e)

    def _get_json(self, endpoint):
        if not self.ip:
            raise Exception("Server IP not initialized")
        try:
            url = f"http://{self.ip}/{endpoint}"
            response = requests.get(url, timeout=self.timeout)
            return response.json()
        except Exception as e:
            print(f"Error fetching {endpoint}:", e)
            return None

    def get_players(self):
        data = self._get_json("players.json")
        return len(data) if data else self.errmsg

    def get_players_all(self):
        return self._get_json("players.json") or self.errmsg

    def get_server_status(self):
        try:
            self._get_json("info.json")
            return {"online": True}
        except:
            return {"online": False}

    def get_info_field(self, field):
        data = self._get_json("info.json")
        if not data:
            return self.errmsg
        for key in field.split("."):
            data = data.get(key, None)
            if data is None:
                return self.errmsg
        return data

    # Fonctions spécialisées :
    def get_resources(self): return self.get_info_field("resources")
    def get_onesync(self): return self.get_info_field("vars.onesync_enabled")
    def get_max_players(self): return self.get_info_field("vars.sv_maxClients")
    def get_locale(self): return self.get_info_field("vars.locale")
    def get_gamename(self): return self.get_info_field("vars.gamename")
    def get_steam_ticket(self): return self.get_info_field("requestSteamTicket")
    def get_game_build(self): return self.get_info_field("vars.sv_enforceGameBuild")
    def get_enhanced_host_support(self): return self.get_info_field("vars.sv_enhancedHostSupport")
    def get_license_key_token(self): return self.get_info_field("vars.sv_licenseKeyToken")
    def get_script_hook_allowed(self): return self.get_info_field("vars.sv_scriptHookAllowed")
    def get_tags(self): return self.get_info_field("vars.tags")
    def get_server_name(self):
        name = self.get_info_field("vars.sv_projectName")
        return name.lstrip("^0123456789") if name else self.errmsg
    def get_server_desc(self): return self.get_info_field("vars.sv_projectDesc")
