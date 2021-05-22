import requests
from bs4 import BeautifulSoup
import datetime
import re
import pandas as pd
import  datetime
'''
NameExhibition: [博物馆名称]
main_texts: [新闻简介]
times: [(具体时间，新闻发布距现在的小时数)]
sources: [新闻来源]
sub_urls: [次级新闻网站]
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}

urls = "https://so.toutiao.com/search?keyword="
tail = '&pd=information&source=search_subtab_switch&dvpf=pc&aid=4916&page_num='
NameExhibition = ['中国国家博物馆', '北京军事博物馆', '故宫博物院', '北京鲁迅博物馆', '中国美术馆', '毛主席纪念堂', '民族文化宫博物馆', '中国地质博物馆',
                  '中国古动物馆', '中华航天博物馆', '中国人民抗日战争纪念馆', '中国科学技术馆', '宋庆龄故居', '中国人民革命军事博物馆', '中国航空博物馆',
                  '北京天文馆', '首都博物馆', '大钟寺古钟博物馆', '北京艺术博物馆', '北京古代建筑博物馆', '北京石刻艺术博物馆', '徐悲鸿纪念馆',
                  '炎黄艺术馆', '明十三陵博物馆', '北京古观象台', '郭沫若纪念馆', '梅兰芳纪念馆', '中国佛教图书文物馆', '中国长城博物馆', '雍和宫藏传佛教艺术博物馆',
                  '北京古代钱币博物馆', '北京西周燕都遗址博物馆', '北京辽金城垣博物馆', '北京大葆台西汉墓博物馆', '北京大学赛克勒考古与艺术博物馆', '北京市白塔寺管理处',
                  '李大钊烈士陵园', '中国园林博物馆', '焦庄户地道战遗址纪念馆', '中央民族大学民族博物馆', '北京航空馆', '北京房山云居寺石经陈列馆', '北京市昌平区博物馆',
                  '北京红楼文化艺术博物馆']

def get_soup(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_main_texts(soup):
    texts = soup.find_all('span',class_ = 'text-underline-hover')
    main_texts = [x.text.replace('\u3000'*13,'\n\n') for x in texts]
    return main_texts

def get_new_sources(soup):
    sourcess = soup.find_all('span',class_ = 'd-flex align-items-center text-ellipsis margin-right-4')
    timess = soup.find_all('span',class_ = 'text-ellipsis margin-right-4')
    timeAndsource = soup.find_all('div',class_ = 'cs-view cs-view-flex align-items-center flex-row cs-source-content')
    pub_sources = []
    pub_times = []
    for i in sourcess:
        con = i.text.strip().split('\n')
        pub_sources.append(con)

    for i,j,k in zip(sourcess,timess,timeAndsource):
        a = i.text.strip().split('\n')
        b = j.text.strip().split('\n')
        c = k.text.strip().split('\n')
        
        aa ="".join(a[0])
        bb ="".join(b[0])
        cc ="".join(c[0])
        
    
        d=cc.replace(aa,"")
        d=d.replace(bb,"")
        
        time_now = datetime.datetime.now()
        

        xx = 0
        yy = 0
        if d.find("小时",0) != -1:
            xx = 1
        else:
            if len(d)<9:
                if d.find("天",0) != -1:
                    xx = 3
                    if d.find("昨天",0) != -1:
                        yy=1
                    else:
                        if d.find("前天",0) != -1:
                            yy=2
                        else:
                            yy = (int)(d[0])
                else:
                    xx = 2

        if xx == 1:
            time_now = time_now.strftime("%Y-%m-%d")
            d = time_now
            d = time_now.replace("-","年",1)
            d = d.replace("-","月",1)
            d = d+"日"
        elif xx == 2:
            d = "2021年" + d
        elif xx == 0:
            d = d
        elif xx == 3:
            
            time_now = (time_now + datetime.timedelta(days=-yy)).strftime("%Y-%m-%d")
            d = time_now.replace("-","年",1)
            d = d.replace("-","月",1)
            d = d+"日"
       

        pub_times.append(d)
    print(pub_times)
    spe_pub_times = []
    return pub_times, pub_sources
   
    


def get_titles(soup):
    Titles = soup.find_all('div',class_ = 'flex-1 text-darker text-xl text-medium d-flex align-items-center overflow-hidden')
    titles = [str(i.text) for i in Titles]
    return titles


def get_sub_urls(soup):
    sub_urls = soup.find_all('a', href=True, class_ = 'text-ellipsis text-underline-hover')
    results = [str('https://so.toutiao.com')+str(i['href']) for i in sub_urls]
    return results

def WriteToExcel(contents):
    col = ['博物馆名称', '新闻来源', '新闻标题', '简介内容', '次级新闻网站', '新闻发布时间']
    csv = pd.DataFrame(columns = col, data = contents)
    csv.to_csv('souhu_news.csv')

if __name__ == '__main__':
    contents = []
    for name in NameExhibition:
        for page in range(0, 11):# 前十页
            url = urls + name + tail + str(page)
            print(url)

            soup = get_soup(url)
            
            main_texts = get_main_texts(soup)
            times, sources =  get_new_sources(soup)

            titles = get_titles(soup)

            sub_urls = get_sub_urls(soup)
            print(len(sub_urls))
            content = [[name, sources[i], titles[i], main_texts[i], sub_urls[i], times[i]] for i in range(len(main_texts))]
            contents = contents + content
            
    
    print("总博物馆数量：", len(NameExhibition))
    print("总事务数量：", len(contents))
    WriteToExcel(contents)
    '''
    for i in contents:
        print(i)
    '''