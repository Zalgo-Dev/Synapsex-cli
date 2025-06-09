import requests

def resolve(code):
    try:
        url = f"https://cfx.re/join/{code}"
        response = requests.get(url, allow_redirects=False)

        real_ip = response.headers.get("X-Citizenfx-Url")
        token = response.headers.get("X-Citizenfx-Join-Token")

        if real_ip:
            return {
                "ip": real_ip,
                "token": token
            }
        else:
            return {"error": "IP not found in headers."}
    except Exception as e:
        return {"error": str(e)}
