import json
import urllib.request
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# import pokemon_icon.pokemon_icon.spiders.pokemon_icon_spider as spider


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('Usr-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def save_icon(icon_info):
    img_addr = 'https://www.pokewiki.de' + icon_info['icon_src'][0]
    filename = icon_info['num'][0] + '_' + icon_info['name'][0] + '.png'
    with open(filename, 'wb') as f:
        img = url_open(img_addr)
        f.write(img)    

def download_icon(folder, filename):
    os.mkdir(folder)
    os.chdir(folder)
    with open(filename) as json_file:
        data = json.load(json_file)
        for each in data:
            try:
                save_icon(each)
            except IndexError:
                continue
        
def crawler():
    os.chdir('pokemon_icon')
    exit_status = os.system('scrapy crawl pokemon_icon -o items.json -t json')
    print(exit_status)
    os.chdir(r'..\\icons')


if __name__ == '__main__':
    crawler()
    download_icon('down_icons','C:\developmentTools\Lecture\Python\myPython\HTW\DataScience\crawler\pokemon\pokemon_icon\items.json')
