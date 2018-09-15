import urllib.request

try:

    url = 'http://www.python.org'
    webagent = {}
    webagent['User-Agent'] = 'Firefox/24.0'
    req = urllib.request.Request(url, headers=webagent, data=None)
    resp = urllib.request.urlopen(req)
    PageData = resp.read()

#   print(PageData)

    with open('ResponseData.txt', 'w') as f:
    	f.write(str(PageData))

except Exception as ee:
    print(str(ee))


