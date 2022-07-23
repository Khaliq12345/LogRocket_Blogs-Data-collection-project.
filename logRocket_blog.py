#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy

class logRocket_blog(scrapy.Spider):
    name = 'logRocket'
    allowed_domains = ['blog.logrocket.com']
    start_urls = ['https://blog.logrocket.com/']
    custom_settings = {"FEEDS":{"logRocket.csv":{"format":"csv"}}}
    
    def parse(self,response):
        for i in range(1,258): 
            cards = response.css('.card')
            for card in cards:
                name = card.css('h2.card-title a::text').extract_first()
                author = card.css('span.post-name a::text').extract_first()
                desc = card.css('span.card-text.d-block::text').extract_first()
                date = card.css('span.post-date::text').extract_first()
                read_time = card.css('span.readingtime::text').extract_first()
                link = card.css('h2.card-title a').attrib['href']

                scraped_info = {
                    'Author':author,
                    'Topic':name,
                    'Description':desc,
                    'Read Time':read_time,
                    'Date':date,
                    'Post link':link
                    }
                yield scraped_info

            next_p = f'https://blog.logrocket.com/page/{i}/'
            yield scrapy.Request(url = next_p,callback=self.parse)

