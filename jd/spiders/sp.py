# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

"""
1、第一步就是要找打当前的所有的页面的链接
2、，然后才是根据这个链接来进行分析
3、得到链接里面的所有公司的名称
页面的跳转只是在第一页的基础上加上了double的变量，在后面加上一个page参数  比如说第二页就是4  第五十页就是一百以此类推

在执行翻页操作的时候需要先获取到所有的页数，然后在来对页面进行操作

"""


class SpSpider(scrapy.Spider):
    name = 'sp'
    allowed_domains = ['www.jd.com']
    start_urls = [
        'https://search.jd.com/Search?keyword=男装&enc=utf-8&wq=男装'
        # https://search.jd.com/Search?keyword=男装&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=男装&cid2=1342&page=3&s=52&click=0
    ]

    def parse(self, response):
        sel = Selector(response)
        all_page = sel.xpath('//span[@class="fp-text"]/i/text()').extract_first()
        if all_page:
            for page in range(int(all_page) + 1):
                # print(page)
                url = response.url + '&page=%s' % (page*2)
                yield scrapy.Request(url, callback=self.parse_url_content, dont_filter=True)
        else:
            print('error')

    def parse_url_content(self, response):
        sel = Selector(response)
        # print(response.url)
        for data in sel.xpath('//ul[@class="gl-warp clearfix"]/li'):
            # print(data)
            cmp_url = data.xpath('div/div[1]/a/@href').extract_first()
            # print(cmp_url)
            if not cmp_url.startswith('https'):
                cmp_url = 'https:' + cmp_url
            # print(cmp_url)
            yield scrapy.Request(cmp_url, callback=self.parse_shop, dont_filter=True)

    def parse_shop(self, response):
        sel = Selector(response)
        shop_title = sel.xpath('//div[@class="J-hove-wrap EDropdown fr"]/div/div/a/text()').extract_first()
        shop_url = 'https:' + sel.xpath('//div[@class="J-hove-wrap EDropdown fr"]/div/div/a/@href').extract_first()

        print(shop_title,  shop_url)


        # print(all_page.extract())

    # def start_requests(self):
    #     for i in range(100 + 1):
    #         cmp_url = self.start_urls[0] + '&page=%s' % (i * 2)
    #         yield scrapy.Request(cmp_url, callback=self.parse)

    # def parse(self, response):
    #     # 这里得到的是某一个页面里面的URL
    #     sel = Selector(response)
    #     # print(response.url)
    #     # class="gl-warp clearfix"
    #     for data in sel.xpath('//ul[@class="gl-warp clearfix"]/li'):
    #         # 在这里我需要得到所有的单个商品的URL
    #         cmp_url = data.xpath('div/div[1]/a/@href').extract_first()
    #         # print(cmp_url)
    #         if not cmp_url.startswith('https'):
    #             cmp_url = 'https:' + cmp_url
    #
    #         print(cmp_url)

# //*[@id="J_bottomPage"]/span[2]
# def parse(self, response):
#     sel = Selector(response)
#     for data in sel.xpath('//ul[@class="gl-warp clearfix"]/li'):
#         print(data.extract())
