#参见：https://docs.scrapy.org/en/latest/intro/tutorial.html
import scrapy
import json
 
from pokemon_icon.items import PokemonIconItem
 
class PokemonIconSpider(scrapy.Spider):
    name = "pokemon_icon"
    allowed_domains = ["pokewiki.de"]
    start_urls = [
        "https://www.pokewiki.de/Pok%C3%A9mon-Liste"
    ]
 
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        
        #sites = sel.xpath('/html/body/div[@class="content"]/div[@class="leftContent"]/ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"]/div[@class="info clear"]')
        trs = sel.xpath('//tbody/tr')

        items = []
        count = 0
        for tr in trs:
            count += 1
            #第一行为表头数据，无效，应当忽略
            if count == 1:
                continue
            # if count == 10:
            #     break
            item = PokemonIconItem()
            #使用特征定位
            #extract()的结果是字符串列表["xxxx","yyyy","zzzz"]，但是在生成csv或json文件时会自动转化为extract()[0]
            num = tr.xpath('td[1]/text()').extract()
            #某些宝可梦编号不规范，以空格开头，应当将其删去
            try:
                if num[0][0] == ' ':
                    num[0] = num[0][1:]
            #最后三个宝可梦既没有编号也没有头像
            except IndexError:
                item['num'] = [str(count)]
            else:
                item['num'] = num
            
            icon_src = tr.xpath('td[2]/span/img/@src').extract()
            
            #检查宝可梦是否有头像，若无则添加默认头像(为最后三个宝可梦添加精灵球作为头像)
            if icon_src == []:
                item['icon_src'] = [str('/images/2/2b/Miniportal_Icon_-_Pok%C3%A9ball.png')]
            else:
                item['icon_src'] = icon_src
            
            item['name'] = tr.xpath('td[4]/text()').extract()
            
            items.append(item)
        
        return items