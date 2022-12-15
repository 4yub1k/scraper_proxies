from requests import get, exceptions
from concurrent.futures import ThreadPoolExecutor

# urls = ['http://ipecho.net/plain', 'https://api.ipify.org', 'https://api.myip.com', 'https://ip.seeip.org']
# proxy = 'http://104.148.36.10:80'

urls = ['http://ipecho.net/plain']
proxies = [
    "104.148.36.10:80",
    "45.79.110.81:80",
    "198.59.191.234:8080",
    "47.251.15.176:1080",
    "54.225.134.57:8000",
    "162.240.75.37:80"
]

def check_proxy(url, proxy, MAX_TIMEOUT=3):
    try:
        # resp = get(url, proxies={"http": proxy, "https": proxy}, timeout=MAX_TIMEOUT)
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
        }
        resp = get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=MAX_TIMEOUT)
        return resp.text
    except exceptions.ProxyError as err:
        # print(err)
        print(f"Proxy Error : {url} : [ Proxy {proxy} ]")
    except exceptions.ConnectTimeout as err:
        print(f"Connection Timeout : {url} : [ Proxy {proxy} ]")
    except exceptions.ConnectTimeout as err:
        print(f"Connection Timeout : {url} : [ Proxy {proxy} ]")
    except Exception as err:
        print(err)

def main(urls=None, proxies=None):

    MAX_TIMEOUT = 5     # seconds
    with ThreadPoolExecutor() as exe:
        output = {exe.submit(check_proxy, url,proxy, MAX_TIMEOUT): url for url in urls for proxy in proxies}
    
    for res in output:
        # working proxies
        if res.result():
            print(f'\t{output[res]:^5s}: Proxy >> {res.result()} [ OK ]')


if __name__ == "__main__":
    main(urls, proxies)
