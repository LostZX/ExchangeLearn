# Exchange学习

整理和自己写了一些exchange的脚本

## 版本识别和漏洞检测

### 版本识别

1. 通过owa接口，获取短版本信息

2. 通过/ecp/Current/exporttool/microsoft.exchange.ediscovery.exporttool.application接口获取完整版本信息

3. 通过/owa/service, /owa接口响应头 X-OWA-Version获取完整版本

4. 爆破 /ecp/{version}/exporttool/ 最后一位，获取完整版本

### 漏洞检测
参考[这篇文章](https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-Exchange%E7%89%88%E6%9C%AC%E6%8E%A2%E6%B5%8B%E5%92%8C%E6%BC%8F%E6%B4%9E%E6%A3%80%E6%B5%8B)，根据https://learn.microsoft.com/en-us/Exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019匹配版本和日期识别漏洞
## NtmlLoginEWS

checkLogin 支持明文密码和ntlm登录，参考[这篇文章](https://github.com/3gstudent/Homework-of-Python/blob/master/checkEWS.py)修改的脚本，更简洁明了


