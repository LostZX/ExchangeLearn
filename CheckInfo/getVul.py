from getVersion import get_version
from colorama import Fore

exchange_servers = [
{"server":"Exchange Server 2019 CU12 May22SU","date":"05/10/2022","version":"15.2.1118.9","short":"15.2.1118"},
{"server":"Exchange Server 2019 CU12 (2022H1)","date":"04/20/2022","version":"15.2.1118.7","short":"15.2.1118"},
{"server":"Exchange Server 2019 CU11 May22SU","date":"05/10/2022","version":"15.2.986.26","short":"15.2.986"},
{"server":"Exchange Server 2019 CU11 Mar22SU","date":"03/08/2022","version":"15.2.986.22","short":"15.2.986"},
{"server":"Exchange Server 2019 CU11 Jan22SU","date":"01/11/2022","version":"15.2.986.15","short":"15.2.986"},
{"server":"Exchange Server 2019 CU11 Nov21SU","date":"11/09/2021","version":"15.2.986.14","short":"15.2.986"},
{"server":"Exchange Server 2019 CU11 Oct21SU","date":"10/12/2021","version":"15.2.986.9","short":"15.2.986"},
{"server":"Exchange Server 2019 CU11","date":"09/28/2021","version":"15.2.986.5","short":"15.2.986"},
{"server":"Exchange Server 2019 CU10 Mar22SU","date":"03/08/2022","version":"15.2.922.27","short":"15.2.922"},
{"server":"Exchange Server 2019 CU10 Jan22SU","date":"01/11/2022","version":"15.2.922.20","short":"15.2.922"},
{"server":"Exchange Server 2019 CU10 Nov21SU","date":"11/09/2021","version":"15.2.922.19","short":"15.2.922"},
{"server":"Exchange Server 2019 CU10 Oct21SU","date":"10/12/2021","version":"15.2.922.14","short":"15.2.922"},
{"server":"Exchange Server 2019 CU10 Jul21SU","date":"07/13/2021","version":"15.2.922.13","short":"15.2.922"},
{"server":"Exchange Server 2019 CU10","date":"07/29/2021","version":"15.2.922.7","short":"15.2.922"},
{"server":"Exchange Server 2019 CU9 Jul21SU","date":"07/13/2021","version":"15.2.858.15","short":"15.2.858"},
{"server":"Exchange Server 2019 CU9 May21SU","date":"05/11/2021","version":"15.2.858.12","short":"15.2.858"},
{"server":"Exchange Server 2019 CU9 Apr21SU","date":"04/13/2021","version":"15.2.858.10","short":"15.2.858"},
{"server":"Exchange Server 2019 CU9","date":"03/16/2021","version":"15.2.858.5","short":"15.2.858"},
{"server":"Exchange Server 2019 CU8 May21SU","date":"05/11/2021","version":"15.2.792.15","short":"15.2.792"},
{"server":"Exchange Server 2019 CU8 Apr21SU","date":"04/13/2021","version":"15.2.792.13","short":"15.2.792"},
{"server":"Exchange Server 2019 CU8 Mar21SU","date":"03/02/2021","version":"15.2.792.10","short":"15.2.792"},
{"server":"Exchange Server 2019 CU8","date":"12/15/2020","version":"15.2.792.3","short":"15.2.792"},
{"server":"Exchange Server 2019 CU7 Mar21SU","date":"03/02/2021","version":"15.2.721.13","short":"15.2.721"},
{"server":"Exchange Server 2019 CU7","date":"09/15/2020","version":"15.2.721.2","short":"15.2.721"},
{"server":"Exchange Server 2019 CU6 Mar21SU","date":"03/02/2021","version":"15.2.659.12","short":"15.2.659"},
{"server":"Exchange Server 2019 CU6","date":"06/16/2020","version":"15.2.659.4","short":"15.2.659"},
{"server":"Exchange Server 2019 CU5 Mar21SU","date":"03/02/2021","version":"15.2.595.8","short":"15.2.595"},
{"server":"Exchange Server 2019 CU5","date":"03/17/2020","version":"15.2.595.3","short":"15.2.595"},
{"server":"Exchange Server 2019 CU4 Mar21SU","date":"03/02/2021","version":"15.2.529.13","short":"15.2.529"},
{"server":"Exchange Server 2019 CU4","date":"12/17/2019","version":"15.2.529.5","short":"15.2.529"},
{"server":"Exchange Server 2019 CU3 Mar21SU","date":"03/02/2021","version":"15.2.464.15","short":"15.2.464"},
{"server":"Exchange Server 2019 CU3","date":"09/17/2019","version":"15.2.464.5","short":"15.2.464"},
{"server":"Exchange Server 2019 CU2 Mar21SU","date":"03/02/2021","version":"15.2.397.11","short":"15.2.397"},
{"server":"Exchange Server 2019 CU2","date":"06/18/2019","version":"15.2.397.3","short":"15.2.397"},
{"server":"Exchange Server 2019 CU1 Mar21SU","date":"03/02/2021","version":"15.2.330.11","short":"15.2.330"},
{"server":"Exchange Server 2019 CU1","date":"02/12/2019","version":"15.2.330.5","short":"15.2.330"},
{"server":"Exchange Server 2019 RTM Mar21SU","date":"03/02/2021","version":"15.2.221.18","short":"15.2.221"},
{"server":"Exchange Server 2019 RTM","date":"10/22/2018","version":"15.2.221.12","short":"15.2.221"},
{"server":"Exchange Server 2019 Preview","date":"07/24/2018","version":"15.2.196.0","short":"15.2.196"},
{"server":"Exchange Server 2016 CU23 May22SU","date":"05/10/2022","version":"15.1.2507.9","short":"15.1.2507"},
{"server":"Exchange Server 2016 CU23 (2022H1)","date":"04/20/2022","version":"15.1.2507.6","short":"15.1.2507"},
{"server":"Exchange Server 2016 CU22 May22SU","date":"05/10/2022","version":"15.1.2375.28","short":"15.1.2375"},
{"server":"Exchange Server 2016 CU22 Mar22SU","date":"03/08/2022","version":"15.1.2375.24","short":"15.1.2375"},
{"server":"Exchange Server 2016 CU22 Jan22SU","date":"01/11/2022","version":"15.1.2375.18","short":"15.1.2375"},
{"server":"Exchange Server 2016 CU22 Nov21SU","date":"11/09/2021","version":"15.1.2375.17","short":"15.1.2375"},
{"server":"Exchange Server 2016 CU22 Oct21SU","date":"10/12/2021","version":"15.1.2375.12","short":"15.1.2375"},
{"server":"Exchange Server 2016 CU22","date":"09/28/2021","version":"15.1.2375.7","short":"15.1.2375"},
{"server":"Exchange Server 2016 CU21 Mar22SU","date":"03/08/2022","version":"15.1.2308.27","short":"15.1.2308"},
{"server":"Exchange Server 2016 CU21 Jan22SU","date":"01/11/2022","version":"15.1.2308.21","short":"15.1.2308"},
{"server":"Exchange Server 2016 CU21 Nov21SU","date":"11/09/2021","version":"15.1.2308.20","short":"15.1.2308"},
{"server":"Exchange Server 2016 CU21 Oct21SU","date":"10/12/2021","version":"15.1.2308.15","short":"15.1.2308"},
{"server":"Exchange Server 2016 CU21 Jul21SU","date":"07/13/2021","version":"15.1.2308.14","short":"15.1.2308"},
{"server":"Exchange Server 2016 CU21","date":"07/29/2021","version":"15.1.2308.8","short":"15.1.2308"},
{"server":"Exchange Server 2016 CU20 Jul21SU","date":"07/13/2021","version":"15.1.2242.12","short":"15.1.2242"},
{"server":"Exchange Server 2016 CU20 May21SU","date":"05/11/2021","version":"15.1.2242.10","short":"15.1.2242"},
{"server":"Exchange Server 2016 CU20 Apr21SU","date":"04/13/2021","version":"15.1.2242.8","short":"15.1.2242"},
{"server":"Exchange Server 2016 CU20","date":"03/16/2021","version":"15.1.2242.4","short":"15.1.2242"},
{"server":"Exchange Server 2016 CU19 May21SU","date":"05/11/2021","version":"15.1.2176.14","short":"15.1.2176"},
{"server":"Exchange Server 2016 CU19 Apr21SU","date":"04/13/2021","version":"15.1.2176.12","short":"15.1.2176"},
{"server":"Exchange Server 2016 CU19 Mar21SU","date":"03/02/2021","version":"15.1.2176.9","short":"15.1.2176"},
{"server":"Exchange Server 2016 CU19","date":"12/15/2020","version":"15.1.2176.2","short":"15.1.2176"},
{"server":"Exchange Server 2016 CU18 Mar21SU","date":"03/02/2021","version":"15.1.2106.13","short":"15.1.2106"},
{"server":"Exchange Server 2016 CU18","date":"09/15/2020","version":"15.1.2106.2","short":"15.1.2106"},
{"server":"Exchange Server 2016 CU17 Mar21SU","date":"03/02/2021","version":"15.1.2044.13","short":"15.1.2044"},
{"server":"Exchange Server 2016 CU17","date":"06/16/2020","version":"15.1.2044.4","short":"15.1.2044"},
{"server":"Exchange Server 2016 CU16 Mar21SU","date":"03/02/2021","version":"15.1.1979.8","short":"15.1.1979"},
{"server":"Exchange Server 2016 CU16","date":"03/17/2020","version":"15.1.1979.3","short":"15.1.1979"},
{"server":"Exchange Server 2016 CU15 Mar21SU","date":"03/02/2021","version":"15.1.1913.12","short":"15.1.1913"},
{"server":"Exchange Server 2016 CU15","date":"12/17/2019","version":"15.1.1913.5","short":"15.1.1913"},
{"server":"Exchange Server 2016 CU14 Mar21SU","date":"03/02/2021","version":"15.1.1847.12","short":"15.1.1847"},
{"server":"Exchange Server 2016 CU14","date":"09/17/2019","version":"15.1.1847.3","short":"15.1.1847"},
{"server":"Exchange Server 2016 CU13 Mar21SU","date":"03/02/2021","version":"15.1.1779.8","short":"15.1.1779"},
{"server":"Exchange Server 2016 CU13","date":"06/18/2019","version":"15.1.1779.2","short":"15.1.1779"},
{"server":"Exchange Server 2016 CU12 Mar21SU","date":"03/02/2021","version":"15.1.1713.10","short":"15.1.1713"},
{"server":"Exchange Server 2016 CU12","date":"02/12/2019","version":"15.1.1713.5","short":"15.1.1713"},
{"server":"Exchange Server 2016 CU11 Mar21SU","date":"03/02/2021","version":"15.1.1591.18","short":"15.1.1591"},
{"server":"Exchange Server 2016 CU11","date":"10/16/2018","version":"15.1.1591.10","short":"15.1.1591"},
{"server":"Exchange Server 2016 CU10 Mar21SU","date":"03/02/2021","version":"15.1.1531.12","short":"15.1.1531"},
{"server":"Exchange Server 2016 CU10","date":"06/19/2018","version":"15.1.1531.3","short":"15.1.1531"},
{"server":"Exchange Server 2016 CU9 Mar21SU","date":"03/02/2021","version":"15.1.1466.16","short":"15.1.1466"},
{"server":"Exchange Server 2016 CU9","date":"03/20/2018","version":"15.1.1466.3","short":"15.1.1466"},
{"server":"Exchange Server 2016 CU8 Mar21SU","date":"03/02/2021","version":"15.1.1415.10","short":"15.1.1415"},
{"server":"Exchange Server 2016 CU8","date":"12/19/2017","version":"15.1.1415.2","short":"15.1.1415"},
{"server":"Exchange Server 2016 CU7","date":"09/19/2017","version":"15.1.1261.35","short":"15.1.1261"},
{"server":"Exchange Server 2016 CU6","date":"06/27/2017","version":"15.1.1034.26","short":"15.1.1034"},
{"server":"Exchange Server 2016 CU5","date":"03/21/2017","version":"15.1.845.34","short":"15.1.845"},
{"server":"Exchange Server 2016 CU4","date":"12/13/2016","version":"15.1.669.32","short":"15.1.669"},
{"server":"Exchange Server 2016 CU3","date":"09/20/2016","version":"15.1.544.27","short":"15.1.544"},
{"server":"Exchange Server 2016 CU2","date":"06/21/2016","version":"15.1.466.34","short":"15.1.466"},
{"server":"Exchange Server 2016 CU1","date":"03/15/2016","version":"15.1.396.30","short":"15.1.396"},
{"server":"Exchange Server 2016 RTM","date":"10/01/2015","version":"15.1.225.42","short":"15.1.225"},
{"server":"Exchange Server 2016 Preview","date":"07/22/2015","version":"15.1.225.16","short":"15.1.225"},
{"server":"Exchange Server 2013 CU23 May22SU","date":"05/10/2022","version":"15.0.1497.36","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Mar22SU","date":"03/08/2022","version":"15.0.1497.33","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Jan22SU","date":"01/11/2022","version":"15.0.1497.28","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Nov21SU","date":"11/09/2021","version":"15.0.1497.26","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Oct21SU","date":"10/12/2021","version":"15.0.1497.24","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Jul21SU","date":"07/13/2021","version":"15.0.1497.23","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 May21SU","date":"05/11/2021","version":"15.0.1497.18","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Apr21SU","date":"04/13/2021","version":"15.0.1497.15","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23 Mar21SU","date":"03/02/2021","version":"15.0.1497.12","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU23","date":"06/18/2019","version":"15.0.1497.2","short":"15.0.1497"},
{"server":"Exchange Server 2013 CU22 Mar21SU","date":"03/02/2021","version":"15.0.1473.6","short":"15.0.1473"},
{"server":"Exchange Server 2013 CU22","date":"02/12/2019","version":"15.0.1473.3","short":"15.0.1473"},
{"server":"Exchange Server 2013 CU21 Mar21SU","date":"03/02/2021","version":"15.0.1395.12","short":"15.0.1395"},
{"server":"Exchange Server 2013 CU21","date":"06/19/2018","version":"15.0.1395.4","short":"15.0.1395"},
{"server":"Exchange Server 2013 CU20","date":"03/20/2018","version":"15.0.1367.3","short":"15.0.1367"},
{"server":"Exchange Server 2013 CU19","date":"12/19/2017","version":"15.0.1365.1","short":"15.0.1365"},
{"server":"Exchange Server 2013 CU18","date":"09/19/2017","version":"15.0.1347.2","short":"15.0.1347"},
{"server":"Exchange Server 2013 CU17","date":"06/27/2017","version":"15.0.1320.4","short":"15.0.1320"},
{"server":"Exchange Server 2013 CU16","date":"03/21/2017","version":"15.0.1293.2","short":"15.0.1293"},
{"server":"Exchange Server 2013 CU15","date":"12/13/2016","version":"15.0.1263.5","short":"15.0.1263"},
{"server":"Exchange Server 2013 CU14","date":"09/20/2016","version":"15.0.1236.3","short":"15.0.1236"},
{"server":"Exchange Server 2013 CU13","date":"06/21/2016","version":"15.0.1210.3","short":"15.0.1210"},
{"server":"Exchange Server 2013 CU12","date":"03/15/2016","version":"15.0.1178.4","short":"15.0.1178"},
{"server":"Exchange Server 2013 CU11","date":"12/15/2015","version":"15.0.1156.6","short":"15.0.1156"},
{"server":"Exchange Server 2013 CU10","date":"09/15/2015","version":"15.0.1130.7","short":"15.0.1130"},
{"server":"Exchange Server 2013 CU9","date":"06/17/2015","version":"15.0.1104.5","short":"15.0.1104"},
{"server":"Exchange Server 2013 CU8","date":"03/17/2015","version":"15.0.1076.9","short":"15.0.1076"},
{"server":"Exchange Server 2013 CU7","date":"12/09/2014","version":"15.0.1044.25","short":"15.0.1044"},
{"server":"Exchange Server 2013 CU6","date":"08/26/2014","version":"15.0.995.29","short":"15.0.995"},
{"server":"Exchange Server 2013 CU5","date":"05/27/2014","version":"15.0.913.22","short":"15.0.913"},
{"server":"Exchange Server 2013 SP1 Mar21SU","date":"03/02/2021","version":"15.0.847.64","short":"15.0.847"},
{"server":"Exchange Server 2013 SP1","date":"02/25/2014","version":"15.0.847.32","short":"15.0.847"},
{"server":"Exchange Server 2013 CU3","date":"11/25/2013","version":"15.0.775.38","short":"15.0.775"},
{"server":"Exchange Server 2013 CU2","date":"07/09/2013","version":"15.0.712.24","short":"15.0.712"},
{"server":"Exchange Server 2013 CU1","date":"04/02/2013","version":"15.0.620.29","short":"15.0.620"},
{"server":"Exchange Server 2013 RTM","date":"12/03/2012","version":"15.0.516.32","short":"15.0.516"},
]

vularray = [
{"cve":"CVE-2020-0688", "date":"02/11/2020"},
{"cve":"CVE-2021-26855+CVE-2021-27065","date":"03/02/2021"},
{"cve":"CVE-2021-28482", "date":"04/13/2021"},
{"cve":"CVE-2021-34473+CVE-2021-34523+CVE-2021-31207", "date":"04/13/2021"},
{"cve":"CVE-2021-31195+CVE-2021-31196", "date":"05/11/2020"},
{"cve":"CVE-2021-31206", "date":"07/13/2021"},
{"cve":"CVE-2021-42321", "date":"11/09/2021"},
{"cve":"CVE-2022-23277", "date":"03/08/2022"}
]


def getVul(url):
    complete_version, short_version = get_version(url)
    # complete_version = 
    for exchange_server in exchange_servers:
        server = exchange_server.get("server")
        date = exchange_server.get("date")
        version = exchange_server.get("version")
        short = exchange_server.get("short")
        if short_version == short:
            print(Fore.BLUE, "[+] server version: " + version)
            print(Fore.GREEN, "[*] Product: " + server)
            print(Fore.GREEN, "[*] Date: " + date)
            vulscan(date)
    

def vulscan(date):
    for value in vularray:
        if (date.split('/')[2] < value.get("date").split('/')[2]):
            print(Fore.RED, "[*] " + value.get("cve") + ", " + value.get("date"))
        else:
            if (date.split('/')[2] == value.get("date").split('/')[2]) & (date.split('/')[0] < value.get("date").split('/')[0]):
                print(Fore.RED, "[*] " + value.get("cve") + ", " + value.get("date"))
            else:
                if (date.split('/')[2] == value.get("date").split('/')[2]) & (date.split('/')[0] == value.get("date").split('/')[0]) & (date.split('/')[1] < value.get("date").split('/')[1]):
                    print(Fore.RED, "[*] " + value.get("cve") + ", " + value.get("date"))



if __name__ == "__main__":
    getVul("192.168.52.149")