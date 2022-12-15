# scraper_proxies
Scrape proxies from different sites, store in JSON format

### Install:
```
pip install -r requirements.txt
```
### Your IP:
py/python3 myip.py
```
123.x.x.x
123.x.x.x
{"ip":"123.x.x.x","country":"Pakistan","cc":"PK"}
123.x.x.x
```
```json
{
  "query": "198.49.68.80",
  "status": "success",
  "country": "United States",
  "countryCode": "US",
  "region": "FL",
  "regionName": "Florida",
  "city": "Orlando",
  "zip": "32826",
  "lat": 28.5752,
  "lon": -81.2003,
  "timezone": "America/New_York",
  "isp": "HostDime.com, Inc.",
  "org": "HostDime.com, Inc.",
  "as": "AS33182 HostDime.com, Inc."
}
```

### Scrape:
#### Linux:
```
python3 scrape_proxies.py
```
#### Windows:
```
python/py scrape_proxies.py
```

### Output:
```
>> py scrape_proxies.py     

[ proxies_(ssl).json : 52 KB ]
[ proxies_(all).json : 52 KB ]
[ proxies_(anonymous).json : 58 KB ]
[ proxies_(socks).json : 54 KB ]
[ proxies_(uk).json : 51 KB ]
[ proxies_(usa).json : 52 KB ]
[ proxies_(all_2).json : 54 KB ]
[ proxies_(socks_2).json : 56 KB ]
```
### Files:

![image](https://user-images.githubusercontent.com/45902447/206640032-9f488456-bcb0-4e88-b12c-6c2af0525cc5.png)

### JSON:

```json
[
  {
    "id": 0,
    "IP Address": "80.48.119.28",
    "Port": "8080",
    "Code": "PL",
    "Country": "Poland",
    "Anonymity": "elite proxy",
    "Google": "yes",
    "Https": "no",
    "Last Checked": "13 secs ago"
  },
  {
    "id": 1,
    "IP Address": "49.0.2.242",
    "Port": "8090",
    "Code": "ID",
    "Country": "Indonesia",
    "Anonymity": "elite proxy",
    "Google": "no",
    "Https": "yes",
    "Last Checked": "13 secs ago"
  },
  {
    "id": 2,
    "IP Address": "198.49.68.80",
    "Port": "80",
    "Code": "US",
    "Country": "United States",
    "Anonymity": "elite proxy",
    "Google": "yes",
    "Https": "no",
    "Last Checked": "13 secs ago"
  },
  {
    "id": 3,
    "IP Address": "169.57.1.85",
    "Port": "8123",
    "Code": "MX",
    "Country": "Mexico",
    "Anonymity": "elite proxy",
    "Google": "no",
    "Https": "no",
    "Last Checked": "13 secs ago"
  }
]
```
