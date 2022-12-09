# scraper_proxies
Scrape proxies from different sites, store in JSON format

### Install:
```
pip install -r requirements.txt
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
