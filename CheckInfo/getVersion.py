from requests_html import HTMLSession
from colorama import Fore
import requests

requests.packages.urllib3.disable_warnings()


session = HTMLSession()

def get_complete_version(url):
    complete_version, short_version = get_version(url)
    return complete_version

def get_version(url):
    short_version = method1(url)
    print(Fore.WHITE, "[+] short version " + short_version)
    complete_version = method2(url)
    if complete_version:
        print(Fore.WHITE, "[+] complete version " + complete_version)
        return complete_version, short_version
    complete_version = method3(url)
    if complete_version:
        print(Fore.WHITE, "[+] complete version " + complete_version)
        return complete_version, short_version
    complete_version = method4(url, short_version)
    if complete_version:
        print(Fore.WHITE, "[+] complete version " + complete_version)
        return complete_version, short_version
    print(Fore.WHITE, "[-] not found complete version")
    return False
    
# 不完整路径

def method1(url):
    method1_path = "/owa"
    internal_version_short_url = "https://" + url + method1_path
    method1_response = session.get(internal_version_short_url, verify=False)
    version_str = method1_response.html.find("link", first=True).attrs.get("href")
    version = version_str.split("/")[3]
    return version

# xml解析完整路径

def method2(url):
    method2_path = "/ecp/Current/exporttool/microsoft.exchange.ediscovery.exporttool.application"
    complete_version_url = "https://" + url + method2_path
    method2_response = session.get(complete_version_url, verify=False)
    if method2_response.status_code == 200:
        method2_response.encoding = "utf8"
        try:
            version = method2_response.html.find("assemblyIdentity", first=True).attrs.get("version")
            
            return version
        except Exception:
            print("[-] ecp not found complete version")
    else:
        print("[-] ecp not found complete version status code " + str(method2_response.status_code))
    

# 响应头X-OWA-Version

def method3(url):
    method3_path = "/owa/service"
    complete_version_url = "https://" + url + method3_path
    method3_response = session.get(complete_version_url, verify=False, allow_redirects=False)
    if method3_response.status_code == 404:
        method3_response = session.get("https://" + url + "/owa", verify=False, allow_redirects=False)
    version = method3_response.headers.get("X-OWA-Version")
    if not version:
        print("[-] owa not found complete version")
    else:
        return version

# 爆破路径

def method4(url, short_version):
   
    method4_path_template = "/ecp/{version}/exporttool/"
    for i in range(1, 100):
        version = short_version + "." + str(i)
        method4_path = method4_path_template.format(version=version)
        complete_version_url = "https://" + url + method4_path
        method4_response = session.get(complete_version_url, verify=False)
        if method4_response.status_code == 200:
            return version
    print("[-] brute ecp not found complete version")

if __name__ == "__main__":
    get_version("mail.delacruzny.com")