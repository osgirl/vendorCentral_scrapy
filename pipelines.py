# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pyodbc
from datetime import datetime

class ProductsPipeline(object):
    cnxn = ''

    def __init__(self):
        cnxn_str = 'DRIVER={ODBC Driver 11 for SQL Server};SERVER=PEPWUL138150\MSSQLSERVER12;' \
                   'DATABASE=Test;Trusted_Connection=yes;'
        self.cnxn = pyodbc.connect(cnxn_str)

    def process_item(self, item, spider):
        """
        Sample data:
        {
        'BUDGET': '$5 000.00',
        'CAMPAIGN_NAME': 'VPC_NANBev_Bars_P9-11',
        'COUPON_ITEM_ASIN': 'B01BGQ1M1C',
        'COUPON_ITEM_NAME': 'Gatorade Prime Fuel Bar  Oatmeal Raisin  45g of carbs 5g of protein per bar (12 Count)',
        'COUPON_TITLE': 'Gatorade Prime Fuel Bar  Oatmeal Raisin  Pack of 12',
        'DISCOUNT': '20%',
        'END_DATE': 'November 4  2018',
        'START_DATE': 'September 9  2018',
        'URL': 'https://vendorcentral.amazon.com/hz/vendor/members/coupon-campaigns/view/A1247721YFG26K/coupons/ANPKM4SDDF9I0'
        }
        """
        try:
            item['BUDGET'] = float(str(item['BUDGET']).replace(' ', '').replace('$',''))
        except ValueError:
            item['BUDGET'] = None
        item['CAMPAIGN_NAME'] = str(item['CAMPAIGN_NAME']).lower()
        item['COUPON_TITLE'] = str(item['COUPON_TITLE']).lower()
        if str(item['COUPON_ITEM_NAME']) == 'NA':
            item['COUPON_ITEM_NAME'] = None
        else:
            item['COUPON_ITEM_NAME'] = str(item['COUPON_ITEM_NAME']).lower()
        if item['COUPON_ITEM_ASIN'] == 'NA':
            item['COUPON_ITEM_ASIN'] = None
        else:
            item['COUPON_ITEM_ASIN'] = str(item['COUPON_ITEM_ASIN']).lower()
        if '%' in str(item['DISCOUNT']):
            item['DISCOUNT_UNIT'] = "%"
            item['DISCOUNT'] = float(str(item['DISCOUNT']).replace('%', ''))
        elif '$' in str(item['DISCOUNT']):
            item['DISCOUNT_UNIT'] = "$"
            item['DISCOUNT'] = float(str(item['DISCOUNT']).replace('$', ''))
        dt_current_format = '%B %d %Y'
        dt_new_format = '%Y-%m-%d %X'
        try:
            item['START_DATE'] = datetime.strptime(' '.join(str(item['START_DATE']).split()), dt_current_format).strftime(
                dt_new_format)
            item['END_DATE'] = datetime.strptime(' '.join(str(item['END_DATE']).split()), dt_current_format).strftime(
                dt_new_format)
        except ValueError:
            item['START_DATE'] = str(item['START_DATE'])
            item['END_DATE'] = str(item['END_DATE'])
        item['CAMPAIGN_ID'] = str(item['URL']).split('/')[8]
        item['COUPON_ID'] = str(item['URL']).split('/')[-1]
        self._write(item)
        return item

    def _write(self, item):
        query = "insert into STG_vccCampaignData (campaign_id, couponId, couponUrl, campaignName, couponName," \
                "productName, productAsin, startDate, endDate, budget, discount, discountUnit, runtime) values " \
                "(?,?,?,?,?,?,?,?,?,?,?,?,?)"

        cursor = self.cnxn.cursor()
        cursor.execute(query, item['CAMPAIGN_ID'], item['COUPON_ID'], item['URL'], item['CAMPAIGN_NAME'],
                       item['COUPON_TITLE'], item['COUPON_ITEM_NAME'], item['COUPON_ITEM_ASIN'], item['START_DATE'],
                       item['END_DATE'],item['BUDGET'], item['DISCOUNT'], item['DISCOUNT_UNIT'],
                       datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cursor.commit()