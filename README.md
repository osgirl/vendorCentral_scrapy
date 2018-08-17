# Vendor Central Coupon Campaign Data
Run Instructions:  
Create a scrapy project from CLI: scrapy startproject [your project name]  
Place the vc_Spider1.py into './spiders/'  
Replace settings.py withthe one provided here  
  
Following commands have to be run in order:  
  scrapy crawl campaign_crawl -o campaigns.json  
  scrapy crawl coupon_crawl -o coupons.json  
  scrapy crawl coupon_detail_crawl -o coupon_detail.json  
  scrapy crawl campaign_metrics_crawl  
  
Pending tasks:  
  Automate extraction of total number of pages at the Campaign level and pass store it into variable _campaign_pg_nos  
  Automate run of above commands with CrawlerProcess  

Takeaways and caveats:  
To use rotating proxies, use HttpProxyMiddleware. Provide proxies as a list in settings.py  
To enable Autothrottle, comment out the 'CONCURRENT REQUESTS PER DOMAIN' and uncomment the 'AUTO THROTTLE' option in settings .py  
