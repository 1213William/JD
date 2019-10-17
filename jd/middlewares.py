# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class JdSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JdDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        cookie = 'unpl=V2_ZzNtbRFRS0BxX0VcchteBGJTFA4RBRQXfAkWAC4cX1E3UBcKclRCFX0URlVnGVoUZwIZXEpcQRxFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsaXwVjABBaSlNzJXI4dmR4GVgMYAAiXHJWc1chVE9TeBlaBSoDEV5CU0AXcgBCZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_b79d5f2983304a7bbcf380aed42eab4f|1571278178726; o2State={%22webp%22:true}; __jdu=1221523695; areaId=2; ipLoc-djd=2-2823-51974-0; PCSYCityID=CN_310000_310100_310110; user-key=cab021c9-ab34-485c-bbae-d5b8db6267d6; cn=0; shshshfpa=1c9c5586-9e83-9e91-e9ad-f7b5e13faa35-1571278182; shshshfpb=wqYoYnbmob5B9lWDQ9YU1Nw%3D%3D; TrackID=13kJRDRriEj1IXSJY7ZfD_1fcY7CCVHK7lSBz-sNBLBp91oGoDK4UMgjN3_OuabDCUxejOnvmJgpj589hCL-TNXVKaCn-c32JRCoT93UZGilM899InBYRaH5V1AOKhii8; thor=4F2B22337AC358D9BA177D87F2BAA1DA0EAA5BC9A583CD359BD0B31B458FE7087E501B0FFE20F75612DAE41450442AA72EA2F0D81F400D531211C3E9F96392CFDBB54B504040D87F37A8237DC3AEE54BD973EADA81F0775FB505615192B9D932D3B37D975F8CAEC38E3609ABE037BD21A9020124BCF67B3EC51E7A17CDD642045C51CB2C45DB6EE3DC1DC43A98274F9E50B432F230CEE523980256EFAFD1D01F; pinId=qpOs5A89HwW56_TTf5PkZLV9-x-f3wj7; pin=jd_5c7815518eadc; unick=jd_5c7815518eadc; ceshi3.com=000; _tp=5xzD%2FpI8q%2B0YVr5ZShqhqfxAxqOLVDSGeGyQV4GebfU%3D; _pst=jd_5c7815518eadc; __jda=76161171.1221523695.1571278178.1571278178.1571278179.1; __jdb=76161171.16.1221523695|1.1571278179; __jdc=76161171; shshshfp=9ee453971e60ac11c2e8f3ea1d01caee; shshshsID=c5ad9812d0b32e78c51c2637cb4d063a_11_1571279991855'
        itemDict = {}
        items = cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        request.cookies = itemDict
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
