import scrapy
from scrapy.exceptions import CloseSpider
import json


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    nPage = 0
    INCREMENTED_BY = 1
    allowed_domains = ['www.gartner.com']
    start_urls = ['https://www.gartner.com/ngw/syspath-bin/gartner/dynamiccontent?requestType=curated-select-by-tags&designType=list&languageCode=en&showLocalizedContent=true&showGcomDomainContent=&filterCodes=153332823&tagType=emt:page/content-type&resourceType=emt/components/content/globalsite/curateddynamiccontent&currentPagePath=https://www.gartner.com/smarterwithgartner/archive&lastSelectedFilter=&tags=emt%3Apage%2Fcontent-type%2Farticles&excludeFilterTags=emt%3Apage%2Fregion%2Fasia-pacific%2Fjapan%2Cemt%3Apage%2Fregion%2Fasia-pacific%2Fchina%2Cemt%3Apage%2Fregion%2Fasia-pacific&pageSizesList=8']

    def parse(self, response):
        if response.status == 500:
            raise CloseSpider('Last Page')
        r = json.loads(response.body)
        url_base = 'www.gartner.com'
        info = r.get('data')['announcements'][:8]
        for titles in info:
            yield {
                'Title': titles['title'],
                'Date': titles['date'],
                'Link': url_base+titles['url']
            }

            self.nPage += self.INCREMENTED_BY

            yield scrapy.Request(
                url= f'https://www.gartner.com/ngw/syspath-bin/gartner/dynamiccontent?requestType=curated-select-by-tags&designType=list&languageCode=en&showLocalizedContent=true&showGcomDomainContent=&filterCodes=153332823&tagType=emt:page/content-type&resourceType=emt/components/content/globalsite/curateddynamiccontent&currentPagePath=https://www.gartner.com/smarterwithgartner/archive&lastSelectedFilter=&tags=emt%3Apage%2Fcontent-type%2Farticles&excludeFilterTags=emt%3Apage%2Fregion%2Fasia-pacific%2Fjapan%2Cemt%3Apage%2Fregion%2Fasia-pacific%2Fchina%2Cemt%3Apage%2Fregion%2Fasia-pacific&pageSizesList=8&nPage={self.nPage}',
                callback= self.parse
            )
            
