import scrapy
import os
import json

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'vendorcentral.amazon.com',
    'Referer': 'https://vendorcentral.amazon.com/hz/vendor/members/home/ba',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
cookie_str = 'session-id-time-vcna=2082758401l; ubid-vcna=131-4906712-3827323; x-wl-uid=1XGQHaDbtu2A0HJn6qe/ohgCfYB1lO/ggrOK1pe8pvwieePpQQjE685vmA/Lc2TSwo84Mtg0URXO/ntT8nVWSqw==; s_vnum=1964528128952%26vn%3D1; session-id-time=2082787201l; s_pers=%20s_fid%3D64FD79D0F9F88302-18C60115F27C28E3%7C1595687182740%3B%20s_dl%3D1%7C1532530582742%3B%20gpv_page%3DUS%253ALWA%253A%2520gsg-web%7C1532530582746%3B; session-id-vcna=143-1717540-2216821; ubid-main=131-4906712-3827323; session-id=143-1717540-2216821; sst-main=Sst1|PQFfsPDS7Y6bqj5AkPa_LxDNC7N18UEE4ga5SK6mbElxIxHvdBCE-w2UNJt5ZwXSa1ZQLxSaEhkHBgfFaisRomzHUkHGpn0N942QHETXk_Is440SZqXxD08u99S5aMbOOCFsq20Mt0WQuh2K-vVVcdD3LQAuT5yrLBdCF6xXA3zaYW2p3iXR_S80240Lj4VndKo75Zty7Ie22KUejB4Y_uBQgHtZyMzAE7QnbRAIi-wC822notSTaxgTMuIiuH4R2GLoilNZN76rOkWrBMysYCtgqWRfysJArQQiwePZNPfz22Y6QK2HYA5g7gRjiqzvi9ZDSW3ofIvc0_4EbO6b7VeU6A; lcvc-acbna=en_US; vg-vcna=2450910; lc-main=en_US; session-token=RI3H3QOOPgQV3CklO9LaXn1Wr/2bPDPx6Hye8mWNcqz2Ap3OfJuE1gk//dpHa4RPpKHtqi/VnmWcxwBCR+zmDg5yLMThE0u4mvMhuDdZndnjtpFfaG61muPCnS0k8EwvjlibNSMpL7VPrvK8greAxKzvWgf3kNhetidwsL5ZS1Y5b5WPXNGK0u0Z1pte+T2Z/0UKIhFeif6lFmCeuFtasA==; s_fid=4A129523E7CFB5FB-1852BF647864E151; s_cc=true; aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws_lang=en; aws-target-static-id=1533910596688-696717; aws-target-data=%7B%22support%22%3A%221%22%7D; s_campaign=PS%7Cacquisition_US%7Cgoogle%7CACQ-P%7CPS-GO%7CBrand%7CSU%7CManagement%20Tools%7CManagement%20Console%7CUS%7CEN%7CText%7Caws_mgmt_console_e%7Caws%20console%7C278498074531%7Cmanagement_console%7Ce%7CUS; aws-target-visitor-id=1533910596698-374797.28_98; aws-ubid-main=835-1051484-5758531; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A699571264729%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22gautham18113%22%2C%22keybase%22%3A%22TJZ6FvKoICal67pW4y0qro5LJISfKuV06J7N9FyS9AY%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%7D; regStatus=pre-register; c_m=undefinedwww.google.comSearch%20Engine; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1533910597550-77358; s_dslv=1534175376963; s_vn=1565446463564%26vn%3D5; s_nr=1534175376971-Repeat; x-main="j21IPkMPqe2@QS?2m8GHvwQOSI79MyJgAsq?@?ZlyVPzbLaI94k0c3TUg9uJjkyG"; at-main=Atza|IwEBIGuZ5QP6vn_WSEzvUTuQC_t63j2VMM6Ofbp1P7u4qNC0Df0vSDal3aAweqOuB8j7EmoFN8UugvcVueo6hDBP9an1NsdYl4urQZwF8JkSJ58rjmdSPrTwgZK2SgvToLXNlOAej_x2DBF8PRndIHPFtxFUG42B4yTomAUe0E62lj4MgFX73pFIpWJzvgEJlhw-G7y4JD1WbLuaOL4pdgMp0fxoeSYw63QgWUjuaWYNJkrJBF5iW5Y_D4uXNTS1kMMW6HncmE_60ON9X6lp4V5AenU5WLFFSeGZeaUABHmDbqruRMP5_EtP9pK4P6mgxjAWcN8Pcr6glDQzGwGHOsH-DdtZIzDsJc5JpfXIdQ31JrzlRU5Qlh35HP2eI6RVXgTUgNn-SKZmXzxTf0jf4SfxCDXX4kighqTj_hRChScYR8hczJrsO4j1aIaqWikIzQ-SUCOGjsOTHXFcNcNqqXngodBGBuInupAJ8_R9X4ert2z3Ew; sess-at-main="bAT6XUGOkoRbSPUP8Z/YyMLjpgRAbmQGN34TS9t7KUM="; session-token="6FvBtizzi1kTdBUTA/IMCvt6vdCRS78xxlPp7tv2i0BoGAapV+BGgmpqsdkGAVPUGpBj9raJpeqgYftsuX6GlYAZnpKtral+VLjTbEHRUvdYW99L4XYo2G7QqbGxlLp2dLX2oYiLN5Oa0PrOlafM0Jye0950pgDIsUI5JRaR2MBM1T+eqXUMSWerPYwZy5z85zrPBQBEuVGWdwBAz9I1tA=="; x-vcna=Hk4STgTFeKLbCXoVc0ZAkc3ePgAWbBlhVcWIBzzCMo9X8ELtNepFPCGOzqp48AC9; csm-hit=tb:3R7V3PR18X70PNDG9KB5+s-X3P9RYDSMW235PB13X6Z|1534192761472&adb:adblk_no'

cookies = {}

for x in cookie_str.split(';'):
    y = x.split('=')
    cookies[y[0]] = y[1]

campaign_data_file_path = os.getcwd() + "/campaigns.json"
coupon_data_file_path = os.getcwd() + "/coupons.json"

"""
Scraper is divided into 4 parts/spiders:
1.  CampaignSpider: Crawls high level coupon campaign pages to extract links to underlying coupons. Stores results into 
    campaigns.json.
2.  CouponSpider: Crawls coupon from links in campaign.json and extracts links to individual coupon products within each
    coupon parent category, and stores urls under coupons.json.
3.  CouponDetailSpider: Reads all data in coupons.json and iterates through hyperlinks in the file. Yields url, campaign 
    name, start date, end date, budget, discount, coupon product name etc. 
4.  CampaignMetrics Spider:  Crawls all links from campaigns.json and downloads excel from 'view metric' hyperlink.    
"""


class CampaignSpider(scrapy.Spider):
    name = 'campaign_crawl'
    allowed_domains = ['vendorcentral.amazon.com']

    def start_requests(self):
        start_urls = ['https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns?ref_=vc_ven-ven-home_subNav']
        for _i in range(0, 760, 10):
            if _i == 0:
                yield scrapy.Request(url=start_urls[0], headers=headers, cookies=cookies,
                                     callback=self.scrape_campaign_id)
            else:
                yield self.next_page(_i)

    def scrape_campaign_id(self, response):
        _campaign_details_container_xpath = "//div[@class='a-box-group a-spacing-base vft-richrows-container']"
        _campaign_href_xpath = "div[@class='a-box a-color-offset-background vft-richrows-header']/div//ul/li/span/" \
                               "div/a/@href"
        _no_of_coupons_xpath = "div[@class='a-box a-color-offset-background vft-richrows-header']/div/ul/li[2]/span/" \
                               "div/text()"
        for _div in response.xpath(_campaign_details_container_xpath):
            if _div.xpath(_campaign_href_xpath).extract_first() is not None:
                campaign_id = _div.xpath(_campaign_href_xpath).extract_first().split('/')[-1]
                no_of_coupons = _div.xpath(_no_of_coupons_xpath).extract_first().split()[0]
                yield {'campaignID': campaign_id, '#coupons': no_of_coupons}
    """
    Next Page is called as a XHR request with index as (n-1)*10 where n is the page number
    """
    def next_page(self, index):
        _next_page_params = {
            'startIndex': str(index),
            'sortOrder': 'DESCENDING',
            'sortBy': 'start_date'
        }
        _next_page_header = headers.copy()
        _next_page_header['X-Requested-With'] = 'XMLHttpRequest'
        _next_page_header['Referer'] = 'https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns?ref_' \
                                       '=vc_ven-ven-home_subNav'
        request = scrapy.FormRequest(
            url='https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/ajax/campaigns-next-page',
            method='GET',
            headers=_next_page_header,
            cookies=cookies,
            formdata=_next_page_params,
            callback=self.scrape_campaign_id)
        return request


class CouponSpider(scrapy.Spider):
    name = 'coupon_crawl'

    def start_requests(self):
        _dict = self._load_campaign_data(campaign_data_file_path)
        for _d in _dict:
            _id = _d['campaignID']
            _no = int(_d['#coupons'])
            url = "https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/view/%s" % _id

            _pages = self._pages(_no)

            for _i in _pages:
                if _i == 0:
                    yield scrapy.Request(url=url, cookies=cookies, headers=headers, callback=self.parse)
                else:
                    yield self._next_page(index=_i, _id=_id)

    def parse(self, response):
        _campaign_details_container_xpath = "//div[@class='a-box-group a-spacing-base vft-richrows-container']"
        _href_xpath = "div/div/ul/li/span/div/a/@href"

        for _div in response.xpath(_campaign_details_container_xpath):
            yield {'url': "https://vendorcentral.amazon.com" + _div.xpath(_href_xpath).extract_first()}

    """
        Next Page is called as a XHR request with index equal to the number of coupons in campaign
    """
    def _next_page(self, index, _id):
        _next_page_params = {
            'startIndex': str(index),
            'sortOrder': 'ASCENDING',
            'sortBy': 'product_name'
        }
        _next_page_header = headers.copy()
        _next_page_header['X-Requested-With'] = 'XMLHttpRequest'
        _next_page_header[
            'Referer'] = 'https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/view/%s' % _id
        request = scrapy.FormRequest(
            url='https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/'
                'ajax/%s/campaign-coupons' % _id,
            method='GET',
            headers=_next_page_header,
            cookies=cookies,
            formdata=_next_page_params,
            callback=self.parse,
            dont_filter=True
        )
        return request

    def _load_campaign_data(self, file_path):
        try:
            _campaign_id = {}
            with open(file_path, 'r') as f:

                _campaign_id = json.load(f)
        except FileNotFoundError:
            print("JSON File Not Found")
        return _campaign_id

    """XHR page index changes every 20 pages"""
    def _pages(self, _no):
        if _no > 5 and _no <= 20:
            _pages = [0, _no]
        elif _no > 20 and _no % 20 != 0:
            _pages = [_n for _n in range(0, _no, 20)]
            _pages.append(_no)
        elif _no > 20 and _no % 20 == 0:
            _pages = [_n for _n in range(0, _no, 20)]
        else:
            _pages = [0]
        return _pages


class CouponDetailSpider(scrapy.Spider):
    name = 'coupon_detail_crawl'

    def start_requests(self):
        start_urls = [_u['url'] for _u in self._load_coupon_data(coupon_data_file_path)]
        for url in start_urls:
            yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        _campaign_name_xpath = "//div[@class='a-fixed-right-grid-col a-col-left']/div/div/a/text()"
        _coupon_title_xpath = "//h1[@class='vss-coupon-item-title']/text()"
        _coupon_start_dt_xpath = "//*[@id='vss-coupon-details-start-date']/span/div/text()"
        _coupon_end_dt_xpath = "//*[@id='vss-coupon-details-end-date']/span/div/text()"
        _coupon_budget_xpath = "//div[@aria-labelledby='vft-details-list-header-property-label-2']/text()"
        _coupon_discount_xpath = "//*[@id='vss-coupon-details-discount']/span/div/text()"
        _coupon_products_xpath = "//div[@class='a-section vft-richrows-item-details-container']"
        _coupon_item_name_xpath = "h4/text()"
        _coupon_item_asin_xpath = "div/ul/li/span/span[3]/text()"


        CAMPAIGN_NAME = response.xpath(_campaign_name_xpath).extract_first().strip().replace(',', ' ')
        COUPON_TITLE = response.xpath(_coupon_title_xpath).extract_first().strip().replace(',', ' ')
        START_DATE = response.xpath(_coupon_start_dt_xpath).extract_first().strip().replace(',', ' ')
        END_DATE = response.xpath(_coupon_end_dt_xpath).extract_first().strip().replace(',', ' ')
        BUDGET = response.xpath(_coupon_budget_xpath).extract_first().strip().strip().replace(',', ' ')
        DISCOUNT = response.xpath(_coupon_discount_xpath).extract_first().strip().strip().replace(',', ' ')

        for _div in response.xpath(_coupon_products_xpath):
            if response.xpath(_coupon_products_xpath).extract_first() is None:
                yield {'URL': response.url,
                       'CAMPAIGN': CAMPAIGN_NAME,
                       'COUPON': COUPON_TITLE,
                       'START': START_DATE,
                       'END': END_DATE,
                       'BUDGET': BUDGET,
                       'DISCOUNT': DISCOUNT,
                       'COUPON ITEM NAME': 'NA',
                       'COUPON ITEM ASIN': 'NA'}
            else:
                if _div.xpath(_coupon_item_name_xpath).extract_first() is not None:
                    COUPON_ITEM_NAME = _div.xpath(_coupon_item_name_xpath).extract_first().strip().replace(',', ' ')
                else:
                    COUPON_ITEM_NAME='NA'

                if _div.xpath(_coupon_item_asin_xpath).extract_first() is not None:
                    COUPON_ITEM_ASIN = _div.xpath(_coupon_item_asin_xpath).extract_first().strip().replace(',', ' ')
                else:
                    COUPON_ITEM_ASIN = 'NA'

                yield {'URL': response.url,
                       'CAMPAIGN': CAMPAIGN_NAME,
                       'COUPON': COUPON_TITLE,
                       'START': START_DATE,
                       'END': END_DATE,
                       'BUDGET': BUDGET,
                       'DISCOUNT': DISCOUNT,
                       'COUPON ITEM NAME': COUPON_ITEM_NAME,
                       'COUPON ITEM ASIN': COUPON_ITEM_ASIN}


    def _load_coupon_data(self, file_path):
        try:
            _start_urls = {}
            with open(file_path, 'r') as f:

                _start_urls = json.load(f)
        except FileNotFoundError:
            print("JSON File Not Found")
        return _start_urls

"""
    Crawler class to download all campaign metric files
"""
class CampaignMetricsSpider(scrapy.Spider):
    name = 'campaign_metrics_crawl'

    def start_requests(self):
        _dict = self._load_campaign_data(campaign_data_file_path)
        # print(_dict)
        for _d in _dict:
            _id = _d['campaignID']
            url = "https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/view/%s" % _id
            metrics_page = 'https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/' \
                           'download/%s/download-metrics' % _id
            yield scrapy.Request(metrics_page, cookies=cookies, headers=headers, callback=self.save_metrics,
                                 meta={'campaignId':_id})

    def save_metrics(self, response):
        fileName = response.meta['campaignId']
        path = os.getcwd() + "\\metrics\\" + fileName + ".xlsx"
        with open(path, "wb") as f:
            f.write(response.body)

    def _load_campaign_data(self, file_path):
        try:
            _campaign_id = {}
            with open(file_path, 'r') as f:

                _campaign_id = json.load(f)
        except FileNotFoundError:
            print("JSON File Not Found")
        return _campaign_id

