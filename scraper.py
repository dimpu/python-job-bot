# import scrapy

# class JobScraper(scrapy.Spider):
#   name = "IndeedSpider"
#   start_urls = ['http://www.indeed.com/']
#   def __init__(self, name, start_urls):
#     # self.start_urls = start_urls
#     pass

#   def scrape(self,skillset, region):
#     self.skillset = skillset
#     self.region = region

#   def parse(self, response):
#     pass
  
#   def perform_search(self, q, l):





# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     start_urls = ['https://blog.scrapinghub.com']

#     def parse(self, response):
#         for title in response.css('h2.entry-title'):
#             yield {'title': title.css('a ::text').extract_first()}

#         for next_page in response.css('div.prev-post > a'):
#             yield response.follow(next_page, self.parse)



import scrapy

class JobSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.indeed.com/jobs?q=Angular&l=New+York']
    
    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'q': 'react', 'l': 'New York,Ny'},
            callback=self.after_login
        )

    def after_login(self, response):
       pass

