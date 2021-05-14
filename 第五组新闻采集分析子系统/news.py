import requests
from bs4 import BeautifulSoup
import datetime
import re
import pandas as pd
'''
@author: Sombra
NameExhibition: [博物馆名称]
main_texts: [新闻简介]
times: [(具体时间，新闻发布距现在的小时数)]
sources: [新闻来源]
sub_urls: [次级新闻网站]

get_spe_exhibition(name, time_limits, contents): 数据加工
'''
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
}

urls = "https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word="
tail = '&x_bfe_rqs=03E80&x_bfe_tjscore=0.100000&tngroupname=organic_news&newVideo=12&rsv_dl=news_b_pn&pn='


def get_soup(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    return soup
def get_main_texts(soup):
    texts = soup.find_all('span',class_ = 'c-font-normal c-color-text')
    main_texts = [x.text.replace('\u3000'*13,'\n\n') for x in texts]
    return main_texts

def get_new_sources(soup):
    timeAndsource = soup.find_all('div',class_ = 'news-source')
    pub_times = []
    pub_sources = []
    for i in timeAndsource:
        con = i.text.strip().split('\n')
        #print(con)
        if len(con) == 2:
            pub_sources.append(con[0])
            pub_times.append(con[1])
        else:
            pub_sources.append(con[0])
            pub_times.append('unknown')
        '''
        if '<span class=\"c-color-gray2 c-font-normal\">' in i.text:
            Time = i.split('<span class="c-color-gray2 c-font-normal">')[0].split('</span>')
            pub_times.append(Time)
        if '<span class="c-color-gray c-font-normal c-gap-right">' in i.text:
            source = i.split('<span class="c-color-gray c-font-normal c-gap-right">')[0].split('</span>')
            pub_sources.append(source)
        '''
    #print(len(pub_times))
    spe_pub_times = []
    for pub_time in pub_times:
        content = pub_time
        if len(re.findall('\d+天前', content)):
            spe_pub_times.append((re.findall('\d+天前', content)[0], int(re.findall('\d+', content)[0]) * 24))
        elif len(re.findall('\d+小时前', content)):
            spe_pub_times.append((re.findall('\d+小时前', content)[0], int(re.findall('\d+', content)[0])))
        elif len(re.findall('\d+月\d+日', content)):
            month_now = datetime.datetime.today().month
            spe_pub_times.append((re.findall('\d+月\d+日', content)[0], (month_now - (int(re.findall('\d+', content)[0][0]))) * 30 * 24))
        elif len(re.findall('前天\d+:\d+|昨天\d+:\d+', content)):
            spe_pub_times.append((re.findall('前天\d+:\d+|昨天\d+:\d+', content)[0], 24))
        elif len(re.findall('\d+年\d+月\d+日', content)):
            Date = re.findall('\d+', content)[0]
            year_now = datetime.datetime.today().year
            month_now = datetime.datetime.today().month
            gap = (year_now - int(Date[0]) - 1) * 12 * 30 * 24 + (int(Date[0]) + 12 - month_now) * 30 * 24
            spe_pub_times.append((re.findall('\d+年\d+月\d+日', content), gap))
        else:
            spe_pub_times.append(('unknown', 'unknown'))
    return spe_pub_times, pub_sources


def get_titles(soup):
    Titles = soup.find_all('h3',class_ = 'news-title_1YtI1')
    titles = [str(i.text) for i in Titles]
    return titles

def get_sub_urls(soup):
    sub_urls = soup.find_all('a', href=True, class_ = 'news-title-font_1xS-F')
    results = [str(i['href']) for i in sub_urls]
    return results

def WriteToExcel(contents):
    col = ['博物馆名称', '新闻来源', '新闻标题', '简介内容', '次级新闻网站', '新闻发布时间']
    csv = pd.DataFrame(columns = col, data = contents)
    csv.to_csv('baidu_news.csv')

def get_spe_exhibition(name, time_limits, contents):
    content = []
    for i in contents:
        if i[0] == name and int(i[5][1]) < time_limits * 24:
            content.append(i)
    return content

if __name__ == '__main__':
    contents = []
    Ex = open('exhibitions.txt')
    NameExhibition = []
    ex_lines = Ex.readlines()
    NameExhibition = [el.strip() for el in ex_lines]
    #print(NameExhibition)
    for name in NameExhibition[0:130]:
        for page in range(0, 101, 10):# 前十页
            url = urls + name + tail + str(page)
            soup = get_soup(url)


            main_texts = get_main_texts(soup)

            times, sources =  get_new_sources(soup)

            titles = get_titles(soup)

            sub_urls = get_sub_urls(soup)

            content = [[name, sources[i], titles[i], main_texts[i], sub_urls[i], times[i]] for i in range(len(main_texts))]
            contents = contents + content
    print("总博物馆数量：", len(NameExhibition))
    print("总事务数量：", len(contents))
    WriteToExcel(contents)

    '''
    for i in contents:
        print(i)
    '''