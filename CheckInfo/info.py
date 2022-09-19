import re
import requests

headers = {     
    "Content-type": "text/xml; charset=utf-8",
    "Accept": "text/xml",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

def getInfo(url):
    ews_url = "https://" + url + "/ews"
    req = requests.get(ews_url, headers=headers, verify=False)
    if "X-OWA-Version" in req.headers:
        version = req.headers["X-OWA-Version"]
        print(version)
    else:
        print("not found ")


def getLocalIp(url):
    apis = [
        "/OWA",
        "/Autodiscover",
        "/Exchange",
        "/ecp",
        "/aspnet_client"
    ]
    for api in apis:
        try:
            url1 = "https://" + url + api
            print("[*] Try to access " + url1)
            requests.get(url, headers=headers, verify=False)
            print("[+] check url " + url1)
        except Exception as e:
            pattern_name = re.compile(r"host='(.*?)',")
            name = pattern_name.findall(str(e))
            if len(name[0])!=0:
                print("[+] Internal IP: " + name[0])
                return True
    return False