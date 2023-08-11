# Scrapy settings for workua project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = "workua"

SPIDER_MODULES = ["workua.spiders"]
NEWSPIDER_MODULE = "workua.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "workua (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(0.2, 1)
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "workua.middlewares.WorkuaSpiderMiddleware": 543,
# }

ROTATING_PROXY_LIST = [
    # "209.79.65.132:8080",
    # "203.85.120.69:8080",
    # "8.209.114.72:3129",
    # "20.33.5.27:8888",
    # "45.152.188.241:3128",
    # "209.79.65.132:8080",
    # "191.252.92.34:8889",
    # "136.243.92.30:26541",
    # "35.194.228.247:3128",
    # "188.166.209.131:3128",
    # "114.7.27.98:8080",
    # "37.148.211.30:3128",
    # "202.154.36.60:8080",
    # "167.86.99.172:8080",
    # "186.121.235.222:8080",
    # "51.81.32.81:8888",
    # "51.81.32.81:8888",
    # "164.92.105.75:2083",
    # "164.92.105.75:2083",
    # "136.243.92.30:26541",
    # "186.121.235.66:8080",
    # "59.17.70.80:8080",
    # "200.105.215.22:33630",
    # "36.138.120.73:3128",
    # "123.126.158.50:80",
    # "191.252.92.34:8889",
    # "113.223.212.29:8089",
    # "211.106.84.247:1022",
    # "117.71.132.160:8089",
    # "123.182.58.174:8089",
    # "170.187.229.216:3128",
    # "201.91.82.155:3128",
    # "209.79.65.132:8080",
    # "113.125.82.11:3128",
    # "35.194.228.247:3128",
    # "34.81.113.225:3128",
    # "136.243.92.30:26541",
    # "103.39.133.213:3128",
    # "47.242.3.214:8081",
    # "194.233.81.116:14344",
    # "209.94.61.32:3128",
    # "212.129.15.88:8080",
    # "190.90.39.76:999",
    # "103.143.63.35:3125",
    # "152.32.67.107:65535",
    # "64.225.4.29:10000",
    # "116.111.68.94:4005",
    # "116.130.233.22:3129",
    # "167.86.99.172:8080",
    # "45.81.145.128:8080",
    # "61.7.146.7:80",
    # "113.160.241.196:19132",
    # "173.249.37.45:5005",
    # "185.15.172.212:3128",
    # "36.88.170.170:8080",
    # "102.132.19.90:3128",
    # "123.126.158.50:80",
    # "103.111.29.134:8080",
    # "37.210.207.179:8080",
    # "187.1.57.206:20183",
    # "45.250.169.132:8080",
    # "102.68.128.217:8080",
    # "115.127.79.234:8080",
    # "20.44.206.138:80",
    # "60.248.185.247:80",
    # "64.225.4.85:10000",
    # "13.57.64.79:8080",
    # "59.17.70.80:8080",
    # "43.255.38.101:8080",
    # "165.227.80.229:3128",
    # "188.132.222.45:8080",
    # "103.39.133.213:3128",
    # "196.23.154.117:10832",
    # "222.81.218.66:443",
    # "203.150.128.76:8080",
    # "103.6.177.174:8002",
    # "201.91.82.155:3128",
    # "196.23.154.117:10846",
    # "186.121.235.66:8080",
    # "45.220.1.13:8080",
    # "103.155.54.38:83",
    # "168.90.92.169:999",
    # "196.23.154.117:11240",
    # "194.233.81.116:14344",
    # "196.23.154.117:11111",
    # "196.23.154.117:9480",
    # "103.165.253.10:3125",
    # "190.97.240.10:1994",
    # "196.23.154.117:11136",
    # "95.56.254.139:3128",
    # "82.222.11.215:8080",
    # "190.113.40.42:999",
    # "168.90.92.65:999",
    # "191.102.254.26:8085",
    # "103.204.208.90:3127",
    # "111.225.153.94:8089",
    # "45.5.119.61:999",
    # "167.86.99.172:8080",
    # "170.83.242.250:999",
    # "138.121.161.82:8290",
    # "103.1.93.184:55443",
    # "181.191.94.126:8999",
    # "200.105.215.22:33630",
    # "36.89.213.98:3137",
    # "122.3.41.154:8090",
    # "38.156.233.75:999",
    # "58.136.169.93:8080",
    # "193.138.178.6:8282",
    # "181.113.135.254:52058",
    # "84.254.0.86:32650",
    # "209.141.47.74:1080",
    # "190.239.221.192:999",
    # "123.182.58.174:8089",
    # "190.113.40.41:999",
    # "194.233.81.116:14344",
    # "154.70.107.81:3128",
    # "171.226.235.192:4002",
    # "189.202.205.236:9005",
    # "103.145.200.13:6969",
    # "38.156.238.94:999",
    # "179.61.229.178:999",
    # "45.152.188.241:3128",
    # "190.53.46.11:38525",
    # "187.141.184.235:8080",
    # "209.126.124.140:3128",
    # "46.53.187.235:3128",
    # "185.189.199.75:23500",
    # "222.165.205.154:8089",
    # "180.178.99.138:8080",
    # "102.68.128.214:8080",
    # "187.63.157.51:999",
    # "186.121.235.66:8080",
    # "41.60.26.210:32650",
    # "182.253.63.10:8080",
    # "206.42.55.98:3128",
    # "209.79.65.132:8080",
    # "47.242.3.214:8081",
    # "197.248.86.237:32650",
    # "85.196.179.34:8080",
    # "200.106.184.12:999",
    # "5.2.76.163:17000",
    # "180.232.171.210:8080",
    # "36.138.56.214:3128",
    # "154.72.77.10:8080",
    # "109.195.23.223:34031",
    # "45.116.156.251:8080",
    # "136.243.88.20:26541",
    # "43.129.223.147:38080",
    # "181.143.106.162:52151",
    # "212.108.144.67:8080",
    # "170.79.12.75:9090",
    # "200.116.198.222:9812",
    # "103.165.155.226:1111",
    # "181.225.101.50:999",
    # "164.92.105.75:2083",
    # "41.242.116.150:50003",
    # "103.245.204.214:8080",
    # "168.90.92.169:999",
    # "92.242.212.50:8080",
    # "45.127.245.42:8080",
    # "95.56.254.139:3128",
    # "180.184.91.187:443",
    # "200.30.138.54:3128",
    # "85.234.126.107:55555",
    # "5.165.6.188:1513",
    # "201.182.251.140:999",
    # "190.211.173.201:999",
    # "103.133.24.211:8080",
    # "188.132.222.163:8080",
    # "105.112.135.166:8080",
    # "136.243.92.30:26541",
    # "37.148.211.30:3128",
    # "103.92.226.19:8080",
    # "115.127.96.14:8674",
    # "209.94.61.32:3128",
    # "38.156.238.180:999",
    # "212.154.82.52:9090",
    # "111.178.11.20:8088",
    # "41.33.219.132:8080",
    # "170.83.242.250:999",
    # "202.5.51.161:8080",
    # "183.88.224.123:8080",
    # "167.86.99.172:8080",
    # "177.87.144.122:8086",
    # "103.121.120.69:8080",
    # "201.220.112.98:999",
    # "122.3.41.154:8090",
    # "123.25.15.209:9812",
    # "20.31.205.142:3128",
    # "118.173.242.189:8080",
    # "186.251.224.82:8080",
    # "187.95.11.107:8080",
    # "188.132.221.162:8080",
    # "47.90.126.78:8118",
    # "34.101.245.121:80",
    # "177.93.45.156:999",
    # "186.125.152.20:8080",
    # "185.88.158.34:3128",
    # "31.43.52.176:41890",
    # "103.60.161.18:8080",
    # "41.65.160.171:1981",
    # "91.107.247.115:4000",
    # "217.11.184.30:3128",
    # "103.168.44.114:8080",
    # "154.223.182.139:3128",
    # "41.77.13.186:53281",
    # "136.243.55.199:3128",
    # "43.159.46.237:3128",
    # "183.56.253.129:8118",
    # "197.232.47.122:8080",
    # "110.78.164.224:8888",
    # "51.81.32.81:8888",
    # "163.172.31.44:80",
    # "204.199.120.30:999",
    # "116.130.233.22:3129",
    # "179.48.15.160:80",
    # "14.225.3.187:8666",
    # "80.194.38.106:3333",
    # "200.106.184.97:999",
    # "91.238.211.110:8080",
    # "34.81.113.225:3128",
    # "117.102.103.146:9890",
    # "203.85.120.69:8080",
    # "177.87.250.23:999",
    # "203.128.75.195:8080",
    # "45.169.92.149:999",
]

# ROTATING_PROXY_LIST_PATH = "../proxies.txt"
ROTATING_PROXY_LOGSTATS_INTERVAL = 16

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "workua.pipelines.WorkuaPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
