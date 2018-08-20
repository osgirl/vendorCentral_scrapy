# Vendor Central Coupon Campaign Data
<h1>Run Instructions:  </h1>
Create a scrapy project from CLI: scrapy startproject [your project name]  
Place the vc_Spider1.py into './spiders/'  
Replace pipelines.py and settings.py with the respective files provided here    
  
<b>Following commands have to be run in order:</b>
<ul>
<li>scrapy crawl campaign_crawl -o campaigns.json </li> 
<li>scrapy crawl coupon_crawl -o coupons.json </li> 
<li>scrapy crawl coupon_detail_crawl -o coupon_detail.json  </li>
<li>scrapy crawl campaign_metrics_crawl </li> 
</ul>
<b>Pending tasks:</b>  
<ul>
<li>Automate login and retrieval of cookie data.</li>
<li>Automate extraction of total number of pages at the Campaign level and pass store it into variable _campaign_pg_nos  </li>
<li>Automate run of above commands with CrawlerProcess  </li>
<li>Schedule runs on daily/weekly basis</li>  
</ul>
<b>Takeaways and caveats:</b>  
<ul>
<li>To use rotating proxies, use HttpProxyMiddleware. Provide proxies as a list in settings.py  </li>
<li>To enable Autothrottle, comment out the 'CONCURRENT REQUESTS PER DOMAIN' and uncomment the 'AUTO THROTTLE' option in settings .py  </li>
<ul>
