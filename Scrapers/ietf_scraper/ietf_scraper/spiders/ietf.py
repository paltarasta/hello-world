import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        description = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()
        creator = response.xpath('//meta[@name="DC.Creator"]/@content').get()
        date = response.xpath('//meta[@name="DC.Date.Issued"]/@content').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        subHeading = response.xpath('//span[@class="subheading"]/text()').getall()
        text = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())

        outputs = []
        outputs.append({"description":description})
        outputs.append({"creator":creator})
        outputs.append({"date":date})
        outputs.append({"title":title})
        outputs.append({"subHeading":subHeading})
        outputs.append({"text":text})

        return outputs
