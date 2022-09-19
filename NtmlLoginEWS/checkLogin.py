from impacket import ntlm
import requests
import base64
import re
import binascii
from requests_ntlm import HttpNtlmAuth


requests.packages.urllib3.disable_warnings()

ews_uri = "/EWS/Exchange.asmx"
post_body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:GetFolder>
      <m:FolderShape>
        <t:BaseShape>Default</t:BaseShape>
      </m:FolderShape>
      <m:FolderIds>
        <t:DistinguishedFolderId Id="inbox"/>
      </m:FolderIds>
    </m:GetFolder>
  </soap:Body>
</soap:Envelope>
'''

def login_check(url, domain, mode, username, password):
    # https://github.com/3gstudent/Homework-of-Python/blob/master/checkEWS.py
    server_url = "https://" + url + ews_uri

    session = requests.Session()

    session.get(server_url, verify=False)
    ntlm_nego = ntlm.getNTLMSSPType1(url, domain)
    negotiate = base64.b64encode(ntlm_nego.getData())
    # Headers
    headers = {
        "Authorization": 'NTLM %s' % negotiate.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    response = session.post(server_url, data=post_body, headers=headers, verify=False)

    www_authenticate = response.headers.get('WWW-Authenticate')

    if response.status_code != 401:
        print('Status code returned: %d. Authentication does not seem required for URL'%(response.status_code))
        return False
    try:
        if 'NTLM' not in www_authenticate:
            print('NTLM Auth not offered by URL, offered protocols: %s'%(www_authenticate))
            return False
    except (KeyError, TypeError):
        print('No authentication requested by the server for url %s'%(server_url))
        return False

    print('[*] Got 401, performing NTLM authentication')

    # ntlm认证
    session.auth=HttpNtlmAuth(domain + "\\" + username, password)
    response1 = session.post(server_url, post_body, verify=False)

    if response1.status_code == 401:
        print('[!] Server returned HTTP status 401 - authentication failed')
        return False

    else:
        print('[+] Valid:%s %s'%(username,password))       
        return True
