import scrapy
from ..items import ClutchItem
from scrapy.loader import ItemLoader

class CompaniesSpider(scrapy.Spider):
    name = 'companies'
    url = "https://clutch.co/agencies/content-marketing"
    def start_requests(self):

    
        yield scrapy.Request(url=self.url,callback=self.parse)
    
    page_no = 0
    def parse(self, response):
        if(response.status == 200):
            companies = response.xpath("//li[@class='provider-row']")
            
            for company in companies:
                informations = company.xpath(".//div[contains(@class,'list-item')]/text()").getall()
                if(len(informations)):
                    loader = ItemLoader(item=ClutchItem(),response=response,selector=company)
                    loader.add_xpath('Company_Name',".//h3[@class='company-name']/a/text()")
                    loader.add_xpath('Website',".//li[@class='website-link website-link-a']/a/@href")
                    loader.add_xpath('Service_Focus',".//div[@class='chart-label hidden-xs']/i/text()")
                    loader.add_value('Min_Project_Size',informations[0])
                    loader.add_value('Avg_Hourly_Rate',str(informations[1]))
                    loader.add_value('Employees',str(informations[2]))
                    loader.add_xpath('Locality',".//span[@class='locality']/text()")
                    loader.add_xpath('Region',".//span[@class='region']/text()")
                    yield loader.load_item()

            last_page = response.xpath("//li[@class='pager-last']").get()
  

            if(last_page):
                self.page_no = self.page_no + 1
                next_page_url = self.url + f'?page={self.page_no}'
                yield scrapy.Request(url=next_page_url,callback=self.parse)
            else:
                pass




