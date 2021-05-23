#youleirongjiusuanchenggong
import json
from time import sleep
import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#实现无可视化界面
from selenium.webdriver import ChromeOptions#实现规避操作
class Museum_1:
    number=2

    def getTime(self):
        url='https://www.dpm.org.cn/Visit.html#block3'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
        response=requests.get(url=url,headers=headers,timeout=40)
        response.encoding='utf-8'
        text=response.text
        timeTree=etree.HTML(text)
        xp='//*[@id="block3"]/div[@class="title"]/p[1]//text()'
        xp2='//*[@id="block3"]/div[2]/div[1]/ul/li[1]/text()|//*[@id="block3"]/div[2]/div[1]/ul/li[1]/span/text()|//*[@id="block3"]/div[2]/div[1]/ul/li[3]/span/text()|//*[@id="block3"]/div[2]/div[1]/ul/li[3]/text()'
        time=timeTree.xpath(xp2)
        return time[1]+time[0]+'\n'+time[3]+time[2]
    def getExhibition(self):
        return '诚慎仁术——清宫医药文物展 展览地点：永和宫展厅\n吉祥如意——故宫博物院典藏如意展 展览地点：神武门展厅\n丝绸之路（乌兹别克斯坦段）考古成果展 展览地点：永寿宫'
    def getActivity(self):
        url = 'https://www.dpm.org.cn/Events.html#hd1-2'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='//*[@id="hd1-2"]/div/div[2]/div[2]/div[1]/div[1]/a/@href'
        html=requests.get(url=url,headers=headers).text
        tree=etree.HTML(html)
        href=tree.xpath(xp)
        url='https://www.dpm.org.cn'+href[0]
        html=requests.get(url=url,headers=headers)
        html.encoding='utf-8'
        tex=html.text
        xp='//*[@id="hl_content"]/div[2]/div[2]/div//text()'
        tree = etree.HTML(tex)
        text = tree.xpath(xp)
        str=''
        for t in text:
            str=str+t.strip()
        return str
    def getResearch(self):
        url = 'https://www.dpm.org.cn/learning/dynamic.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp = '//*[@id="lists"]/ul/li[1]/a/@href'
        html = requests.get(url=url, headers=headers).text
        tree = etree.HTML(html)
        href = tree.xpath(xp)
        url = 'https://www.dpm.org.cn' + href[0]
        html = requests.get(url=url, headers=headers)
        html.encoding = 'utf-8'
        tex = html.text
        xp2='//*[@id="hl_content"]/h1/text()'
        xp = '//*[@id="hl_content"]/div[2]/div[2]/div/p[1]/text()'
        tree = etree.HTML(tex)
        text = tree.xpath(xp2)[0]+'\n'+tree.xpath(xp)[0]
        return text.replace('None','')
    def getCollection(self):
        url = 'https://www.dpm.org.cn/searchs/ceramics.html?0.7563177341752938&category_id=90'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        params={
            '0.7563177341752938':'',
                'category_id': '90'
        }
        xp = '//*[@id="building2"]/div/div[2]/table/tbody/tr[2]/td/a/@href'
        html = requests.get(url=url, params=params,headers=headers).text
        url='https://www.dpm.org.cn' + etree.HTML(html).xpath(xp)[0]
        url=url.replace('None','')
        html = requests.get(url=url, headers=headers)
        html.encoding = 'utf-8'
        tex = html.text
        xp2 = '//*[@id="hl_content"]/div/div[2]/h3/span/text()'
        xp = '//*[@id="hl_content"]/div/div[2]/div[1]/div[1]/p/text()'
        tree = etree.HTML(tex)
        text = tree.xpath(xp2)[0]+'\n'
        for t in tree.xpath(xp) :
            text+=t.strip()
        return text
class Museum_2:
    driver=''
    def getTime(self):
        url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86/567902?fr=aladdin#9_1'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'http: // www.chnmuseum.cn / cg /'
        }
        res=requests.get(url=url,headers=headers).text
        tree=etree.HTML(res)
        xp='/html/body/div[3]/div[2]/div/div[1]/div[212]/text()'
        time=tree.xpath(xp)
        return time[0]
    def getExhibition(self):
        url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86/567902?fr=aladdin#9_1'
        url2='https://www.dpm.org.cn/Article/Index/shows_temporary5.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'http: // www.chnmuseum.cn / cg /'

        }
        response =requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        text = response.text
        xp='/html/body/div[3]/div[2]/div/div[1]/div[115]/text()|/html/body/div[3]/div[2]/div/div[1]/div[114]/h3/text()|/html/body/div[3]/div[2]/div/div[1]/div[116]/text()'
        textTree=etree.HTML(text)
        exh=textTree.xpath(xp)
        return exh[0]+'\n'+exh[1]+'\n'+exh[2]
    def getActivity(self):
        url = 'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86/567902?fr=aladdin#9_1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='/html/body/div[3]/div[2]/div/div[1]/div[189]/h3/text()|/html/body/div[3]/div[2]/div/div[1]/ul[4]/li/div/text()'
        html=requests.get(url=url,headers=headers).text
        tree=etree.HTML(html)
        href=tree.xpath(xp)
        return href[0]+'\n'+href[1]
    def getResearch(self):
        url = 'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86/567902?fr=aladdin#9_1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[177]/h3/text()|/html/body/div[3]/div[2]/div/div[1]/div[178]/text()|/html/body/div[3]/div[2]/div/div[1]/div[179]/text()|/html/body/div[3]/div[2]/div/div[1]/div[180]/text()|/html/body/div[3]/div[2]/div/div[1]/div[181]/text()'
        html = requests.get(url=url, headers=headers).text
        tree = etree.HTML(html)
        href = tree.xpath(xp)
        return href[0]+'\n'+href[1]+'\n'+href[2]+'\n'+href[3]+'\n'+href[4]
    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86/567902?fr=aladdin#9_1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        params={
            '0.7563177341752938':'',
                'category_id': '90'
        }
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[58]/h3/text()|/html/body/div[3]/div[2]/div/div[1]/table[2]//text()'
        tex=requests.get(url=url,headers=headers).text
        tree = etree.HTML(tex)
        text = tree.xpath(xp)
        str=text[0]+'\n'
        for t in text:
            str=str+t
        s=str.strip()
        s=s.replace('[17]','')
        return s
class Museum_3:
    def getTime(self):
        return '开放时间9:00-17:00 周二至周日 周一休馆(黄金周除外)'

    def getExhibition(self):
        url = 'http://www.sstm.org.cn/exarea!getList'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'type': '1'
        }
        res = requests.post(url=url, data=data, headers=headers).text
        re = json.loads(res)
        str = ''
        for b in re['body']:
            str = str + b['title'] + ':' + b['site'] + ','
        return str

    def getActivity(self):
        url = 'http://www.sstm.org.cn/active!getList'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'pageSize': '12',
            'pageNum': '1'
        }
        html = requests.post(url=url, data=data, headers=headers).text
        tex = json.loads(html)
        # print(tex)
        str = ''
        i = 0
        for t in tex['body']['rows']:
            s = t['title'] + ':' + '开始时间：' + t['startTime'] + ' 结束时间：' + t['endTime'] + '主题：' + t['theme'] + '位置：' + t[
                'site'] + '面向人群：' + t['targetItems'][0]['name'] + '\n'
            # print(s)
            str += s
            i += 1
            if i > 3: break
        return str

    def getResearch(self):
        url = 'http://www.sstm.org.cn/works!getWorksWF'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'mainTabId': '0',
            'pageSize': '10',
            'pageNum': '1'
        }
        html = requests.post(url=url, data=data, headers=headers).text
        tex = json.loads(html)
        str = ''
        for t in tex['body']['rows']:
            str += '作者：' + t['author'] + ' 文章名称：' + t['title'] + ' 分类：'
            for m in t['mainTabItems']:
                str += m['name']
                str += ' '
            str += '\n'
        return str

    def getCollection(self):
        url = 'http://www.sstm.org.cn/cinema!getCinSortListPage'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'cinemaID': '0',
            'pageSize': '100',
            'pageNum': '1'
        }
        res = requests.post(url=url, data=data, headers=headers).text
        tex = json.loads(res)
        st = ''
        for t in tex['body']['rows']:
            st += '电影名称：' + t['movicItem']['name'] + ' ' + t['palyTime'] + ' ' + str(t['price']) + '元 ' + '放映场所：' + \
                  t['cinemaItem']['name'] + '位于：' + t['site'] + '\n'
        return st##无可实话
class Museum_4:
    def getTime(self):
        url='https://cstm.cdstm.cn/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body/div[6]/div[1]/div[2]/div/p[1]/span[2]/em/text()|/html/body/div[6]/div[1]/div[2]/div/p[1]/span[1]/em/text()'
        time=tree.xpath(xp)
        str=''
        for t in time:
            str+=t
        return str
    def getExhibition(self):
        url='https://cstm.cdstm.cn/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data={
            'type': '1'
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body/div[1]/div/div[2]/ul/li[3]/div/a/@href'
        tex=tree.xpath(xp)
        str = ''
        for t in tex:
            sleep(3)
            t.replace('./','')
            res=requests.get(url=url+t,headers=headers)
            res.encoding='utf-8'
            text=res.text
            bs=BeautifulSoup(text,'lxml')
            re=bs.find('div',class_='TRS_Editor')
            if re!=None:
                str+=re.text+'\n'
        return str
    def getActivity(self):
        url = 'https://cstm.cdstm.cn/jyhd/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data={
            'pageSize': '12',
            'pageNum': '1'
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        html=res.text
        xp='/html/body/div[4]/div[3]/div/div/p//text()'
        tree=etree.HTML(html)
        act=tree.xpath(xp)
        str=''
        for s in act:
            str+=s
        return str
    def getResearch(self):
        url = 'https://cstm.cdstm.cn/jyhd/jyhdkxby/'
        xp='/html/body/div[4]/div[3]/div[2]/div[3]/div[1]/div/a[2]/text()'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        html = res.text
        tree = etree.HTML(html)
        act = tree.xpath(xp)
        str = '研究活动：'
        for s in act:
            str += s+' '
        return str
    def getCollection(self):
        url = 'https://cstm.cdstm.cn/txyy/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'type': '1'
        }
        res = requests.get(url=url, headers=headers)

        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[4]/div[3]/div/div/div/div/a/@href'
        tex = tree.xpath(xp)
        str = ''
        for t in tex:
            sleep(3)
            t.replace('./', '')
            res = requests.get(url=url + t, headers=headers)
            res.encoding = 'utf-8'
            text = res.text
            bs=BeautifulSoup(text,'lxml')
            re=bs.find_all('span',class_='qmdy-docc')
            ren=bs.find_all('a',class_='qmdy-name')
            ret=bs.select('body > div.main-wapper.Bgimg-fen-kk > div.main-cont > div > div.qmdy-list div.dy>span')
            for i in range(0,len(re)):
                str+=ren[i].text+'\n'+re[i].text+'\n'+ret[i].text+'\n'
        return str
class Museum_5:
    def getTime(self):
        return '浙江省博物馆自2004年起全年免费对外开放（特殊临展除外）周一闭馆，遇法定节假日正常开放，闭馆顺延至节后第一天。周二至周日9:00 - 17:00，16:30观众停止入场，16:50开始清场'
    def getExhibition(self):
        url='http://www.zjmuex.com/Exhibition/CExhibitionList/ZLJL?1=1&type=&areac=2ebfaf78-7f8c-47e9-8862-37b57baf05ea&city=&unit=2&keyword=&StartDate=&EndDate='
        data = {"entity": {"channelNo": "Slide", "portalId": "2341ijij234q_zb_portal"}, "param": {"pageNum": 0}}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; Mi Note 2 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1',

        }
        '''''
        global driver
        #无头浏览器
        chrome =Options()
        chrome.add_argument('--headless')
        chrome.add_argument('--disable-gpu')
        #规避
        option=ChromeOptions()
        option.add_experimental_option('excludeSwitches',['enable-automation'])
        driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome,options=option)
        driver.get(url)
        tree = etree.HTML(driver.page_source)
        '''''
        res=requests.get(url=url,headers=headers).text
        tree=etree.HTML(res)
        xp='/html/body/div[2]/div[3]/div[3]/ul/li[1]//text()|/html/body/div[2]/div[3]/div[3]/ul/li[2]//text()|/html/body/div[2]/div[3]/div[3]/ul/li[3]//text()'
        str = ''
        res=tree.xpath(xp)
        for r in res:
            str+=r.strip()+' '
        sleep(3)
        #driver.quit()
        return str
    def getActivity(self):
        url = 'https://baike.baidu.com/item/%E6%B5%99%E6%B1%9F%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1629454?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data={
            'pageSize': '12',
            'pageNum': '1'
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        html=res.text
        xp='/html/body/div[3]/div[2]/div/div[1]/div[95]//text()|/html/body/div[3]/div[2]/div/div[1]/div[96]/text()|/html/body/div[3]/div[2]/div/div[1]/div[97]//text()|/html/body/div[3]/div[2]/div/div[1]/div[98]/text()'
        tree=etree.HTML(html)
        act=tree.xpath(xp)
        str=''
        for s in act:
            str+=s+'\n'
        return str
    def getResearch(self):
        url = 'https://baike.baidu.com/item/%E6%B5%99%E6%B1%9F%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1629454?fr=aladdin'
        xp='/html/body/div[3]/div[2]/div/div[1]/div[105]/text()|/html/body/div[3]/div[2]/div/div[1]/div[107]/text()|/html/body/div[3]/div[2]/div/div[1]/div[112]/text()'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        html = res.text
        tree = etree.HTML(html)
        str=''
        act = tree.xpath(xp)
        for s in act:
            str += s+'\n'
        return str
    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E6%B5%99%E6%B1%9F%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1629454?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'type': '1'
        }
        res = requests.get(url=url, headers=headers)

        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        s = ''
        for i in range(0,4):
            xp = '/html/body/div[3]/div[2]/div/div[1]/table[1]/tr['+str(i+1)+']/td[2]//text()'
            text = tree.xpath(xp)
            for t in text:
                s+=t+'\n'
            s+='\n'
        ss=s.replace('[9]', '')
        sss=ss.replace('[10]','')
        return sss
class Museum_6:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url='http://www.njmuseum.com/api/home/info'
        data={

        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.post(url=url,headers=headers,data=data)
        html=res.text
        tex=json.loads(html)
        str=''
        for t in tex['data']['nbOpenTime']['list']:
            str+=t['label']+' '+t['value']
            str+='\n'
        return str
    def getExhibition(self):
        url='http://www.njmuseum.com/api/collection/halls'
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
        }
        res=requests.post(url=url,headers=headers)
        res.encoding='utf-8'
        text=res.text
        tex=json.loads(text)
        ss=''
        s='历史馆:'

        for t in tex['data']['lishi']['list']:
            #print(t)
            for h in t['halls']:
                s += '展览名：' + h['exhibitionName'] + ' 展厅：' + h['name']
                if h['show'] == False:
                    s += ' 静候展出'
                else:
                    s += ' 结束时间：' + h['finishTime']
                s += '\n'
        s+='艺术馆:'
        for t in tex['data']['yishu']['list']:
            for h in t['halls']:
                s += '展览名：' + h['exhibitionName'] + ' 展厅：' + h['name']
                if h['show'] == False:
                    s += ' 静候展出'
                else:
                    s += ' 结束时间：' + h['finishTime']
                s += '\n'
        return s
    def getActivity(self):
        url = 'https://activity.wisdommuseum.cn/reservation/activity/out/activityOutList.do?activityType=26'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'http: // www.njmuseum.com / zh / educationIndex'
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        text=res.text
        xp='/html/body//li[@class="acTitle"]/a/text()'
        tree=etree.HTML(text)
        re=tree.xpath(xp)
        str=''
        for r in re:
            str+=r+'\n'
        return str
    def getResearch(self):
        url = 'http://www.njmuseum.com/api/news/list'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'http: // www.njmuseum.com / zh / educationIndex'
        }
        data = {
            'pageNum': '1',
            'pageSize': '10',
            'typeValue': '1',
            'modular': 'sciproject'
        }
        res=requests.post(url=url,data=data,headers=headers)
        res.encoding='utf-8'
        js=json.loads(res.text)
        str=''
        for j in js['data']['list']:
            str+=j['title']+' '+j['time']+'\n'
        return str
    def getCollection(self):
        return '石器：'+'\n'+' 新石器时代钻孔有肩石斧 '+' 新石器时代钻孔石斧 \n'+'陶器：'+'\n'+' 江豚形陶壶 '+' 镂空红陶器 \n'
class Museum_7:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url='http://www.sxhm.com/index.php?ac=article&at=list&tid=237'
        data={

        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.post(url=url,headers=headers)
        html=res.text
        tree=etree.HTML(html)
        re=tree.xpath('/html/body/div[3]/div[2]/div[2]/p[3]/span/span[1]//text()')
        str=''
        for t in re:
            str+=t
        return str.replace('一、','')
    def getExhibition(self):
        url='http://www.sxhm.com/index.php?ac=article&at=list&tid=196'
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        text=res.text
        xp='/html/body/div[3]/div[2]/div[2]/ul/li//a/@href'
        tree=etree.HTML(text)
        ur=tree.xpath(xp)
        str=''
        for h in ur:
            sleep(2)
            res=requests.get(url=h,headers=headers)
            text=res.text
            bs=BeautifulSoup(text,'lxml')
            bt=bs.find_all('div',class_='bt')
            str+=bt[0].text+'\n'
        return str
    def getActivity(self):
        xp='/html/body/div[3]/div[2]/div[2]/ul/li//a/text()'
        url = 'http://www.sxhm.com/index.php?ac=article&at=list&tid=216'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        text = res.text
        tree = etree.HTML(text)
        ur = tree.xpath(xp)
        str = ''
        for h in ur:
            str += h + '\n'
        return str
    def getResearch(self):
        url = 'http://www.sxhm.com/index.php?ac=article&at=list&tid=246'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='/html/body/div[3]/div[2]/div[2]/ul/li[1]/a/@href'
        tree=etree.HTML(requests.get(url=url,headers=headers).text)
        tree=etree.HTML(requests.get(url=tree.xpath(xp)[0],headers=headers).text)
        xp='/html/body/div[3]/div[2]/div[2]/div[3]//text()'
        str=''
        res=tree.xpath(xp)
        for r in res:

            str+=r.strip()+' '
        return str
    def getCollection(self):
        url='http://www.sxhm.com/index.php?page=2&ac=article&at=list&tid=218'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree=etree.HTML(requests.get(url=url,headers=headers).text)
        xp='/html/body/div[3]/div[2]/div[2]/ul/li/a//text()'
        str=''
        for x in tree.xpath(xp):
            str+=x+'\n'
        return str
class Museum_8:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url='https://www.shanghaimuseum.net/mu/frontend/pg/index#section1'
        data={

        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.post(url=url,headers=headers)
        html=res.text
        tree=etree.HTML(html)
        xp='//*[@id="banner-overlay2"]/div[1]//text()|//*[@id="banner-overlay2"]/div[2]/p[1]//text()'
        re=tree.xpath(xp)
        str=''
        for t in re:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url='https://www.shanghaimuseum.net/mu/frontend/pg/display/search-exhibit'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Content-Type': 'application/json',
        }
        params={'params': {'exhibitTypeCode': "OFFLINE_EXHIBITION", 'langCode': "CHINESE"}, 'page': 1, 'limit': 20}
        res=requests.post(url=url,data=json.dumps(params),headers=headers)
        js=json.loads(res.text)
        str=''
        for j in js['data']:
            str+=j['exhibitDateRange']+' '+j['exhibitPlace']+' '+j['issueTime']+' '+j['name']+'\n'
        return str
    def getActivity(self):
        url='https://www.shanghaimuseum.net/mu/frontend/pg/activity/search-activity'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data={'params': {}, 'page': 1, 'limit': 10}
        res=requests.post(url=url,data=data,headers=headers)
        js=json.loads(res.text)
        str=''
        for j in js['data']:
            str+=j['activityDate']+' '+j['activityName']+' '+j['activityStatusDescription']+' '+j['beginTime']+' '+j['speaker']+'\n'
        return str
    def getResearch(self):
        url = 'https://www.shanghaimuseum.net/mu/frontend/pg/article/id/R00004001'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data={'params': {'researchTypeCode': "ACHIEVEMENT", 'langCode': "CHINESE"}, 'page': 1, 'limit': 20}
        tree=etree.HTML(requests.get(url=url,headers=headers).text)
        xp='/html/body/div[5]/div/div/div/table[1]/tbody/tr//text()'
        str=''
        for s in tree.xpath(xp):
            str+=s.strip()+' '
        return str
    def getCollection(self):
        url='https://www.shanghaimuseum.net/mu/frontend/pg/collection/search-monthly-treasure'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Content-Type': 'application/json',
        }
        data={'params': {'langCode': "CHINESE"}, 'page': 1, 'limit': 20}

        js=json.loads(requests.post(url=url,data=json.dumps(data),headers=headers).text)
        str=''
        for j in js['data']:
            str+=j['title']+' '
        return str
class Museum_9:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url='http://www.chnmus.net/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        html=res.text
        tree=etree.HTML(html)
        xp='/html/body//p[@class="serve_time"]/text()|/html/body//p[@class="serve_timeTitle"]/text()'
        re=tree.xpath(xp)
        str=''
        for r in re:
            str+=r+' '
        return str
    def getExhibition(self):
        url='http://www.chnmus.net/sitesources/hnsbwy/page_pc/clzl/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree=etree.HTML(requests.get(url=url,headers=headers).text)
        xp='/html/body//ul[@class="pic"]/li//a/@title'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+' '
        return str
    def getActivity(self):
        url = 'http://www.chnmus.net/sitesources/hnsbwy/page_pc/ppjy/sjhd/list1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        xp = '//*[@id="articleListTable"]/ul/li//a/@title'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + ' '
        return str
    def getResearch(self):
        url = 'http://www.chnmus.net/sitesources/hnsbwy/page_pc/xsyj/xshd/list1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        xp = '//*[@id="articleListTable"]/ul/li//a/@title'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + ' '
        return str
    def getCollection(self):
        url = 'http://www.chnmus.net/sitesources/hnsbwy/page_pc/dzjp/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        #print(requests.get(url=url, headers=headers).text)Classic_tab_pal_bd_con_article
        xp = '/html/body//div[@class="Classic_tab_pal_bd"]//p[@class="Classic_tab_pal_bd_con_tit"]/text()|/html/body//div[@class="Classic_tab_pal_bd"]//p[@class="Classic_tab_pal_bd_con_article"]/text()'
        str=''
        tr = tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
class Museum_10:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '9:00-17:00 16:30停止入馆'
    def getExhibition(self):
        url='https://www.hongyan.info/list/39'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree=etree.HTML(requests.get(url=url,headers=headers).text)
        xp='/html/body/div[8]/div[2]/div[1]/div//h2/a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+' '
        return str
    def getActivity(self):
        url = 'https://www.hongyan.info/list/47/child/66'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        xp = '/html/body/div[8]/div[2]/div[3]/ul/li//text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getResearch(self):
        url = 'https://www.hongyan.info/list/43/child/63'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        xp = '/html/body/div[8]/div[2]/div[3]/ul/li//text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'https://www.hongyan.info/list/35'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        #print(requests.get(url=url, headers=headers).text)Classic_tab_pal_bd_con_article
        xp='/html/body/div[8]/div[2]/div//h2/a/text()'
        str=''
        tr = tree.xpath(xp)
        for t in tr:
            str+=t.strip()+'\n'
        return str
class Museum_11:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url='http://www.19371213.com.cn/guide/how/#%E5%BC%80%E6%94%BE%E6%97%B6%E9%97%B4'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='UTF-8'
        xp='//div[@class="views-row-odd views-row-first bottom-line"]//p/text()'
        tree = etree.HTML(res.text)
        tr = tree.xpath(xp)
        str=''
        for t in tr :
            str+=t+' '
        return str
    def getExhibition(self):
        url='http://www.19371213.com.cn/exhibition/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex);
        xp='//*[@id="block-system-main"]/div[1]/div/div//h2[@class="title-align-R margin-top-40"]/text()|//*[@id="block-system-main"]/div[1]/div/div//div[@class="view TRS_UEDITOR trs_paper_default trs_web"]//text()|//*[@id="block-system-main"]/div[1]/div/div//div[@class="view TRS_UEDITOR trs_paper_default trs_external"]//text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getActivity(self):
        url = 'http://www.19371213.com.cn/learn/community/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        xp = '//*[@id="views-bootstrap-grid-1"]/div/div[@class=" col-xs-12 col-sm-12 col-md-4 col-lg-4"]//h3[@class="card---title"]//text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):
        url = 'http://www.19371213.com.cn/research/publications/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        xp = '//*[@id="views-bootstrap-grid-1"]/div/div//h3/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'http://www.19371213.com.cn/collection/featured/index_16685_'
        uu='.html?_=162106768860'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'http: // www.19371213.com.cn / collection / featured /'
        }
        s=''
        for i in range(0,4):
            params={
                '_': '162106768860'+str(i)
            }
            url2=url+str(i)+uu+str(i)
            sleep(3)
            res=requests.get(url=url2,params=params,headers=headers)
            res.encoding='utf-8'
            bs=BeautifulSoup(res.text,'lxml')
            for b in bs.find_all('h3',class_='title'):
                #print(url2)
                s+=b.text.strip()+'\n'
        return s
class Museum_12:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '毛泽东同志故居开放时间为周一至周日每日8：00-17：00(16：30分停止身份验证)。分四个时间段预约：8：00-10：00、10:00-12:00、12：00-14：00、14：00-16:30。预约总限额12000人次/日，周末、节假日及有关纪念日预约总限额15000人次/日。\n生平展区开放时间为周二至周日每日9：00-16：00(周一闭馆维护，法定节假日顺延)。分四个时间段预约：9：00-11：00、11：00-13：00、13：00-15：00、15：00-16：00。预约总限额6000人次/日，周末、节假日及有关纪念日预约总限额9000人次/日。\n专题展区开放时间为周一至周日每日9：00-16：00。分四个时间段预约：9：00-11：00、11：00-13：00、13：00-15：00、15：00-16：00。预约总限额4000人次/日，周末、节假日及有关纪念日预约总限额6000人次/日。'
    def getExhibition(self):
        url='http://www.ssmzd.com/jngclzl/jngcl/Index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex);
        #print(tex)
        xp='/html/body/table[2]/tr/td/table/tr[2]/td[2]/table/tr[2]/td/table//a[@target="_blank"]/text()|/html/body/table[2]/tr/td/table/tr[2]/td[2]/table/tr[2]/td/table//table[2]//td/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getActivity(self):
        url = 'http://www.ssmzd.com/xuanchuanj/shehuihuodong/Index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        xp = '//*[@id="p_item"]//a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):
        url = 'http://www.19371213.com.cn/research/publications/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        xp = '//*[@id="views-bootstrap-grid-1"]/div/div//h3/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'http://www.ssmzd.com/jngwwjx/jngwwcl/Index.html'
        uu='.html?_=162106768860'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='//*[@id="p_item"]//a/text()'
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        tr=tree.xpath(xp)
        str=''
        for t in tr :
            str+=t.strip()+'\n'
        return str
class Museum_13:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.wuhouci.net.cn/pwxx.html'
        xp='/html/body/section[2]/section[2]/div[1]//text()'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        tree=etree.HTML(requests.get(url=url,headers=headers).text)
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.wuhouci.net.cn/exhibition/list.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        params={
            'time': '2',
            'category_id': '0',
            'page': '1',
            'pageSize': '8'
        }
        res = requests.get(url=url, params=params,headers=headers).text
        js=json.loads(res)
        str=''
        for j in js['data']['exhibition_list']:
            str+='展览名：'+j['exhibition_theme']+' '+'展览地址：'+j['exhibition_address']+' '+'展览信息：'+j['exhibition_info']+' '+'展览时间：'+j['exhibition_time']+'\n'
        return str
    def getActivity(self):
        url = 'http://www.wuhouci.net.cn/kmll.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        xp = '/html/body/section[2]/div[2]/div/div/div[2]/ul/li[1]//text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):
        url = 'http://www.wuhouci.net.cn/article/xshd.html?page=1&pageSize=8'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        str=''
        js=json.loads(tex)
        for j in js['data']['lists']:
            str+=j['title']+' '+j['description']+' '+j['time']+'\n'
        return str
    def getCollection(self):
        url = 'http://www.wuhouci.net.cn/essence/list.html?page=1&pageSize=8'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        str = ''
        js = json.loads(tex)
        for j in js['data']['list']:
            str += j['title'] + ' ' + j['abstract']  + '\n'
        return str
class Museum_14:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.bmy.com.cn/html/public/dl/0f082ba612ca4ebc8ffe58958470c487.html'
        xp='/html/body/div[4]/div[1]/div[3]/div/div[2]/div[2]//text()'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex);
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.bmy.com.cn/html/public/zl/70c3ad1f3b3444cf84b1a8b8301fe093.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='/html/body/div[4]/div/div[1]/ul//text()'
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        tr=tree.xpath(xp)
        str=''
        i=0
        for t in tr:
            str+=t.strip()+' '
            i+=1
            if i==2:
                i=0
                str+='\n'
        return str
    def getActivity(self):
        url = 'http://www.bmy.com.cn/bmy-websitems-1.0-SNAPSHOT/bmy/list.do?currentPage=1&showCount=15&code=005004002'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        js=json.loads(tex)
        str=''
        for j in js['list']:
            str+=j['name']+':'+j['title']+'\n'
        return str
    def getResearch(self):
        url = 'http://www.bmy.com.cn/bmy-websitems-1.0-SNAPSHOT/bmy/list.do?currentPage=1&showCount=15&code=005005001'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        js = json.loads(tex)
        str = ''
        for j in js['list']:
            str += j['name'] + ':' + j['title'] + '\n'
        return str
    def getCollection(self):
        url = 'http://www.bmy.com.cn/bmy-websitems-1.0-SNAPSHOT/bmy/list.do?currentPage=1&showCount=15&code=005003001'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        js = json.loads(tex)
        str = ''
        for j in js['list']:
            str += j['name'] + ':' + j['title'] + '\n'
        return str
class Museum_15:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '周二至周日9:00—17:00（16:00停止入场），每周一全天闭馆（国家法定假日除外）'
    def getExhibition(self):
        url = 'http://www.njmuseumadmin.com/Exhibit/index/id/14'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='//*[@id="form"]/div[3]/div[3]/div[1]/a/@href'
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        tr=tree.xpath(xp)
        str=''
        i=0
        uu='http://www.njmuseumadmin.com'
        for t in tr:
            sleep(3)
            url=uu+t
            res = requests.get(url=url, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            xp='//*[@id="form"]/div[3]/div[2]/div[2]//text()'
            tree=etree.HTML(tex)
            tr=tree.xpath(xp)
            for t in tr:
                str+=t.strip()+' '
            str+='\n'
        return str
    def getActivity(self):
        url = 'http://www.njmuseumadmin.com/Activity/indexTheme/pid/30'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree=etree.HTML(tex)
        str = ''
        #//*[@id="form"]//li/div[@class="addresstime"]//text()   div[@class="div_kuang"]//text()
        xp='/html/body//div[@class="contentInner"][1]/div[@class="tempWrap"]/ul/li//span/text()'
        tr=tree.xpath(xp)
        i=0
        for t in tr:
            str+=t.strip()+' '
            i+=1
            if i==3:
                i=0
                str+='\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.njmuseumadmin.com/Article/academic/pid/33'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        str = ''
        # //*[@id="form"]//li/div[@class="addresstime"]//text()   div[@class="div_kuang"]//text()
        xp = '/html/body//div[@class="Academic_cenleftcon1"]//li/span/text()'
        tr = tree.xpath(xp)
        i = 0
        for t in tr:
            str += t.strip() + ' '
            i += 1
            if i == 2:
                i = 0
                str += '\n'
        return str
    def getCollection(self):
        url = 'http://www.njmuseumadmin.com/Antique/lists'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="Object_listcon"]//span/text()'
        tr=tree.xpath(xp)
        str = ''
        for j in tr:
            str += j.strip()+'\n'
        return str
class Museum_16:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '开放时间：每周二至周日9:00—16:30，16:00停止领票（周一闭馆）'
    def getExhibition(self):
        url = 'https://www.tjbwg.com/cn/Exhibition.aspx'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        xp='/html/body//div[@class="item item1"]/div/a/h3/text()|/html/body//div[@class="item item2"]/div/a/h3/text()'
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        tr=tree.xpath(xp)
        str=''
        i=0
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getActivity(self):
        url = 'https://www.tjbwg.com/cn/News.aspx?TypeId=10972'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree=etree.HTML(tex)
        str = ''
        #//*[@id="form"]//li/div[@class="addresstime"]//text()   div[@class="div_kuang"]//text()
        xp='/html/body//div[@class="main"]//ul[@class="clearfix"]/li/a/div[2]/h3/text()'
        tr=tree.xpath(xp)
        i=0
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'https://www.tjbwg.com/cn/News.aspx?TypeId=10950'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        str = ''
        # //*[@id="form"]//li/div[@class="addresstime"]//text()   div[@class="div_kuang"]//text()
        xp = '/html/body//div[@class="main"]//ul[@class="clearfix"]/li/a/div[2]/h3/text()'
        tr = tree.xpath(xp)
        i = 0
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getCollection(self):
        url = 'https://www.tjbwg.com/cn/collection.aspx?TypeId=10929'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        str = ''
        # //*[@id="form"]//li/div[@class="addresstime"]//text()   div[@class="div_kuang"]//text()
        xp = '/html/body//div[@class="main"]//ul[@class="clearfix"]/li/div/a/h3/text()'
        tr = tree.xpath(xp)
        i = 0
        for t in tr:
            str += t.strip() + '\n'
        return str
class Museum_17:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '9:00-17:00（16:00后停止入馆，16:45清场，17:00闭馆）；星期一闭馆（国家法定节假日除外）。'
    def getExhibition(self):
        url = 'http://www.3gmuseum.cn/web/article/findArticleAndPage.do'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data={
            'pageNumber': '1',
            'pageSize': '8',
            'itemno': '24'
        }
        res=requests.post(url=url,data=data,headers=headers)
        tex=res.text
        js=json.loads(tex)
        str=''
        for j in js['list']:
            str+=j['subject']+'\n'
        return str
    def getActivity(self):
        url = 'http://www.3gmuseum.cn/web/activity/findActivityArticleAndPage.do'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'itemno': '34324333',
            'pageNumber': '1',
            'pageSize': '6',
            'type': '1'
        }
        res = requests.post(url=url, data=data, headers=headers)
        tex = res.text
        js = json.loads(tex)
        str = ''
        for j in js['list']:
            str += j['subject'] + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.3gmuseum.cn/web/article/findArticleAndPage.do'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'pageNumber': '1',
            'pageSize': '20',
            'itemno': '29'
        }
        res = requests.post(url=url, data=data, headers=headers)
        tex = res.text
        js = json.loads(tex)
        str = ''
        for j in js['list']:
            str += j['subject'] + '\n'
        return str
    def getCollection(self):
        url = 'http://www.3gmuseum.cn/web/article/findArticleAndPage.do'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        data = {
            'pageNumber': '1',
            'pageSize': '8',
            'itemno': '402880b25a3bb962015a3bc512601205'
        }
        res = requests.post(url=url, data=data, headers=headers)
        tex = res.text
        js = json.loads(tex)
        str = ''
        for j in js['list']:
            str += j['subject'] + '\n'
        return str
class Museum_18:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.pgm.org.cn/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[1]/b/text()'
        tr=tree.xpath(xp)
        return '开馆时间:'+tr[0]+' 停止检票时间:'+tr[1]+' 闭馆时间:'+tr[2]
    def getExhibition(self):
        url = 'http://www.pgm.org.cn/pgm/cszl/lm_list.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body/div[1]/div[3]/div[2]/ul/li/a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getActivity(self):
        url = 'http://www.pgm.org.cn/pgm/gjhd/list.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[1]/div[3]/div[2]/ul/li/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.pgm.org.cn/pgm/xsyjou/list.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[1]/div[3]/div[2]/ul/li/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getCollection(self):
        url = 'http://www.pgm.org.cn/pgm/gzjp/list.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[1]/div[3]/div[2]/ul/li/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
class Museum_19:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.shanximuseum.com/sx/index/index.html'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="padd"]/div[@class="item"]/div[@class="date"]//text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.shanximuseum.com/sx/exhibition/temporary_future?_=1621129470067'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        js=json.loads(tex)
        str=''
        for t in js['data']:
            str += t['title']+' '+t['description']+' '+t['start_time']+' '+t['end_time']+' '+t['address']+'\n'
        return str
        return str
    def getActivity(self):
        url = 'http://www.shanximuseum.com/sx/education/activity_list?offset=0&amount=9&year=&keyword=&_=1621130011168'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text

        js = json.loads(tex)
        str = ''
        for t in js['data']['list']:
            str += t['title'] + '\n'
        return str
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.shanximuseum.com/sx/research/paper_list?offset=0&amount=9&year=&keyword=&is_sx=0&_=1621130296549'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text

        js = json.loads(tex)
        str = ''
        for t in js['data']['list']:
            str += t['title'] + '\n'
        return str
        return str
    def getCollection(self):
        url = 'http://www.shanximuseum.com/sx/collection/collection_list?offset=0&count=9&dynasty=&material=&keyword=&categoryId=309&quality=&_=1621130449197'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text

        js = json.loads(tex)
        str = ''
        for t in js['data']['list']:
            str += t['title'] + '\n'
        return str
        return str
class Museum_20:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.gansumuseum.com/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="header-right-box"]//text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.gansumuseum.com/zl/list-55.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="play_list"]//div[@class="title"]/label/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        url = 'http://www.gansumuseum.com/edu/list-87-1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="news_list_dynamic dyn_news_list"]//p/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.gansumuseum.com/xsyj/list-65.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="play_list"]//label/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'http://www.gansumuseum.com/dc/list-58-'
        uu='.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        s = ''
        for i in range(1,5):
            url2=url+str(i)+uu
            res = requests.get(url=url2, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp = '/html/body//div[@class="play_list"]//label/text()'
            tr = tree.xpath(xp)
            for t in tr:
                s += t + '\n'
        return s
class Museum_21:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.bjqtm.com/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="mar-l40 mar-r40 mar-t40 mar-b40 c-fff box"]//text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.bjqtm.com/clzl/jbcl/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//ul[@class="clearfix"]//h2/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        url = 'http://www.bjqtm.com/xcjy/sjhd/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="mar-t30 pad-t10 pad-b10 list"]//h3/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.bjqtm.com/wbyj/yjcg/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="mar-t30 pad-t10 pad-b10 list"]//h3/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'http://www.bjqtm.com/dzzp/qtq/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="clearfix"]//h2/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
class Museum_22:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='https://www.artmuseum.tsinghua.edu.cn/cgfw/cgxz/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="TRS_Editor"]//text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'https://www.artmuseum.tsinghua.edu.cn/cpsj/zlxx/zzzl/lszl/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="dhy_xs_zz dhy_xs_zzss"]//h4/a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        url = 'https://www.artmuseum.tsinghua.edu.cn/ggjy/ztjz_1236/jzyy/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="dhy_jy_lib dhy_jy_lib x_zyzlist"]//li/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'https://www.artmuseum.tsinghua.edu.cn/xsyj/ztyj/zlch/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="dhy_jy_lib dhy_jy_lib x_zyzlist"]//li//text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'http://www.artmuseum.tsinghua.edu.cn/was5/web/search?channelid=261334&page=1&searchword=chnlid=801'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '//div[@class="dhy_cg_q"]/h4/a/text()|//div[@class="dhy_cg_q"]/p/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
class Museum_23:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.nanhaimuseum.org/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="booking"]//text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.nanhaimuseum.org/411899/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@id="main"]/ul[@class="white clearfix"]/li/p/a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        url = 'http://www.nanhaimuseum.org/411906/419341/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="d2list cfx"]/ul/a/@href'
        tr = tree.xpath(xp)
        str=''
        for t in tr:
            sleep(3)
            res = requests.get(url=t, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp='/html/body//div[@class="text_content cfx"]/h1/text()|/html/body//div[@class="text_p cfx"]//text()'
            re=tree.xpath(xp)
            for r in re:
                str+=r.strip()+' '
            str+='\n'
        return str.replace('【1】 【2】 【3】','')
    def getResearch(self):#Academic_cenleftcon1
        return '无'
    def getCollection(self):
        url = 'http://www.nanhaimuseum.org/411890/417410/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="white clearfix"]/li/a/@href'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            sleep(3)
            res = requests.get(url=t, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp = '/html/body//div[@class="text_content cfx"]/h1/text()|/html/body//div[@class="text_p cfx"]//text()'
            re = tree.xpath(xp)
            for r in re:
                str += r.strip() + ' '
            str += '\n'
        return str
class Museum_24:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='http://www.sxgm.org/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers,timeout=100)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@style="float:left;padding-top:10px;"]/li/text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'http://www.sxgm.org/home/picnews/index/c_id/90/lanmu/58.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers,timeout=100)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="page_menu_view"]/ul/li[position()>2]/a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        return '无'
    def getResearch(self):#Academic_cenleftcon1
        return '无'
    def getCollection(self):
        url = 'http://www.sxgm.org/home/picnews/index/c_id/10'
        uu='/lanmu/61.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        s=''
        for i in range(4,9):
            url2=url+str(i)+uu
            res = requests.get(url=url2, headers=headers,timeout=100)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp = '//div[@class="pic_title"]/text()'
            tr = tree.xpath(xp)
            for t in tr :
                s+=t+' '
        return s
class Museum_25:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url ='https://www.cdmuseum.com/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers,timeout=100)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="list"]/p/text()'
        str=''
        tr=tree.xpath(xp)
        for t in tr:
            str+=t.strip()+' '
        return str
    def getExhibition(self):
        url = 'https://www.cdmuseum.com/linzhan/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//ul[@class="expo-cur clearfix"]//div[@class="title clearfix"]/p//text()|/html/body//ul[@class="expo-cur clearfix"]//div[@class="nums clearfix"]/p//text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        url = 'https://www.cdmuseum.com/huodongzhuanti/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="inlist4 inlist5 clearfix"]//p[@class="tt1 ellipsis"]/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'https://www.cdmuseum.com/chubanwu/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="inlist-cb clearfix"]/li//div[@class="con"]/p[position()<=5]/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'https://www.cdmuseum.com/jingpin.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '//ul[@class="theme"]/li/a/@href'
        tr = tree.xpath(xp)
        url='https://www.cdmuseum.com'
        str=''
        for t in tr:
            sleep(5)
            url2=url+t
            res = requests.get(url=url2, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp = '//ul[@class="collect-list swiper-wrapper clearfix"]//p[@class="title ellipsis"]/text()'
            re = tree.xpath(xp)
            for r in re:
                str+=r+' '
            str+='\n'
        return str
class Museum_26:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '周一至周日开放时间：9：00-21：30'
    def getExhibition(self):
        url = 'http://www.njiemuseum.com/index.php/Index/Index/col/c_id/41.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//ul[@class="exhi_list clearfix"]/li//h1/text()|/html/body//ul[@class="exhi_list clearfix"]/li//span/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t+'\n'
        return str
    def getActivity(self):
        url = 'http://www.njiemuseum.com/index.php/Index/Index/col/c_id/63.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="exhi_list clearfix"]/li//h1/text()|/html/body//ul[@class="exhi_list clearfix"]/li//span/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        return '无'
    def getCollection(self):
        url = 'http://www.njiemuseum.com/index.php/Index/Index/col/c_id/45/page/'
        uu='.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '//ul[@class="theme"]/li/a/@href'
        tr = tree.xpath(xp)
        s=''
        for t in range(1,5):
            sleep(5)
            url2=url+str(t)+uu
            res = requests.get(url=url2, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp = '//ul[@class="product_list"]//div[@class="prolist_title"]/a/text()'
            re = tree.xpath(xp)
            for r in re:
                s+=r+','
            s+='\n'
        return s
class Museum_27:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'http://www.portmuseum.cn/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '//*[@id="wrapper"]/div[5]/div/table/tr[2]/td[1]/strong/text()|//*[@id="wrapper"]/div[5]/div/table/tr[3]/td[1]/span/text()'
        str = ''
        tr = tree.xpath(xp)
        for t in tr:
            str += t.strip() + ' '
        return str
    def getExhibition(self):
        url = 'http://www.portmuseum.cn/doc/zl/lszl/index.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        uu='http://www.portmuseum.cn'
        xp='/html/body//ul[@class="lszl-list"]/li/a/@href'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            url=uu+t
            sleep(5)
            res = requests.get(url=url, headers=headers)
            res.encoding = 'utf-8'
            tex = res.text
            tree = etree.HTML(tex)
            xp = '/html/body//div[@class="bt-mian"]/div[position()<=3]//text()'
            re=tree.xpath(xp)
            for r in re:
                str+=r.strip()+' '
            str+='\n'
        return str
    def getActivity(self):
        url = 'http://www.portmuseum.cn/doc/jy/gbjt/index.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="gbzx-list"]//h3/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.portmuseum.cn/doc/xs/xsdt/index.shtml'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="xsdt-list"]//a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
    def getCollection(self):
        url = 'http://www.portmuseum.cn/cp_list.php?catg=1&types=1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//ul[@class="gcjp-pic"]//h3/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
class Museum_28:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'https://baike.baidu.com/item/%E5%9B%9B%E6%B8%A1%E8%B5%A4%E6%B0%B4%E7%BA%AA%E5%BF%B5%E9%A6%86/10949818?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]/text()'
        str = ''
        tr = tree.xpath(xp)
        for t in tr:
            str += t.strip() + ' '
        return str
    def getExhibition(self):
        return '战史陈列翔实地再现了红军1935年1月遵义会议后在毛泽东等的领导下，四次飞渡赤水河，至5月9日渡过金沙江，取得战略转移伟大胜利的光辉历史。分为土城战役、四渡序曲，一渡赤水、扎西整编，二渡赤水、再占遵义，三渡赤水、调虎离山，四渡赤水、出奇制胜等五个篇章，凸显了四渡赤水的“神”与“奇”。辅助陈列包括“四渡赤水精神，光耀革命老区”专题书画展，彭德怀、杨尚昆同志住室复原等'
    def getActivity(self):
        return '无'
    def getResearch(self):#Academic_cenleftcon1
        return '无'
    def getCollection(self):
        return '馆内收藏红军文物300余件。纪念馆旁还有红军植下的银杏树一对，每年秋季雌株都果实累累，有一股特别的清香味。'
class Museum_29:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'https://baike.baidu.com/item/%E5%90%90%E9%B2%81%E7%95%AA%E5%8D%9A%E7%89%A9%E9%A6%86/4800605?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]/text()'
        str = ''
        tr = tree.xpath(xp)
        for t in tr:
            str += t.strip() + ' '
        return str
    def getExhibition(self):
        url='https://baike.baidu.com/item/%E5%90%90%E9%B2%81%E7%95%AA%E5%8D%9A%E7%89%A9%E9%A6%86/4800605?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)#
        xp = '/html/body/div[3]/div[2]/div/div[1]/div['#33-38
        xp2=']//b/text()'
        s=''
        for i in range(33,39):
            xp3=xp+str(i)+xp2
            re=tree.xpath(xp3)
            for r in re:
                s+=r
            s+='\n'
        return s.replace('：',' ')
    def getActivity(self):
        return '吐鲁番博物馆举办“让文化遗产融入校园”宣教活动\n吐鲁番博物馆社教活动：让这个假期生活丰富多彩\n吐鲁番博物馆举办“折扇上的吐鲁番”亲子教育体验活动'
    def getResearch(self):#Academic_cenleftcon1
        return '无'
    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E5%90%90%E9%B2%81%E7%95%AA%E5%8D%9A%E7%89%A9%E9%A6%86/4800605?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)  #/html/body/div[3]/div[2]/div/div[1]/div[29]
        xp = '/html/body/div[3]/div[2]/div/div[1]/div['  # 18-29
        xp2 = ']//text()'
        s = ''
        for i in range(18, 30):
            xp3 = xp + str(i) + xp2
            re = tree.xpath(xp3)
            for r in re:
                s += r.strip()
            s += '\n'
        return s.replace('：', ' ')
class Museum_30:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'https://baike.baidu.com/item/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627548?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[2]/text()'
        str = ''
        tr = tree.xpath(xp)
        for t in tr:
            str += t.strip() + ' '
        return str
    def getExhibition(self):
        url = 'https://baike.baidu.com/item/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627548?fr=aladdin#2'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[3]/div[2]/div/div[1]/div['  # 21-34
        xp2 = ']/b/text()'
        s = ' '
        for i in range(21, 35):
            xp3 = xp + str(i) + xp2
            re = tree.xpath(xp3)
            for r in re:
                s += r.strip() + ' '
            s += '\n'
        return s
    def getActivity(self):
        s='新疆博物馆开办传统文化青少年研学课堂\n2018-01-24'
        return s
    def getResearch(self):#Academic_cenleftcon1
        url = 'https://baike.baidu.com/item/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627548?fr=aladdin#4'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[43]/text()|/html/body/div[3]/div[2]/div/div[1]/div[44]/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t +' '
        return str
    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627548?fr=aladdin#4'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//table[@log-set-param="table_view"]//b/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + ' '
        ss=str.replace('：','')
        return ss.replace('一','')
class Museum_31:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'http://www.nxgybwg.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '//*[@id="body_wrap"]/div/div[8]/div/div/div[1]/div/div[1]/p//text()'
        str = ''
        tr = tree.xpath(xp)
        for t in tr:
            str += t.strip() + ' '
        return str
    def getExhibition(self):
        url = 'http://www.nxgybwg.com/e/action/ListInfo/?classid=14'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        uu='http://www.portmuseum.cn'
        xp='/html/body//div[@class="section"]/dl/dt/a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getActivity(self):
        url = 'http://www.nxgybwg.com/e/action/ListInfo/?classid=42'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        uu = 'http://www.portmuseum.cn'
        xp = '/html/body//div[@class="section"]/dl/dt/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.nxgybwg.com/e/action/ListInfo/?classid=27'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        uu = 'http://www.portmuseum.cn'
        xp = '/html/body//div[@class="section"]/dl/dt/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getCollection(self):
        url = 'http://www.nxgybwg.com/e/action/ListInfo/?classid=47'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        uu = 'http://www.portmuseum.cn'
        xp = '/html/body//ul[@class="listmig"]/li/p/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
class Museum_32:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'https://baike.baidu.com/item/%E5%AE%81%E5%A4%8F%E5%9B%9E%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627604?fr=aladdin'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[4]/text()'
        str = ''
        tr = tree.xpath(xp)
        for t in tr:
            str += t.strip() + ' '
        return str
    def getExhibition(self):
        url = 'http://www.nxbwg.com/c/jqzl.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="article-list"]//a/text()'
        tr=tree.xpath(xp)
        str=''
        for t in tr:
            str+=t.strip()+'\n'
        return str
    def getActivity(self):
        url = 'http://www.nxbwg.com/c/xcjy.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//article[position()<=10]//a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        url = 'http://www.nxbwg.com/c/xscg.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//article[position()<=10]//a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getCollection(self):
        url = 'http://www.nxbwg.com/c/jpww.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="article-list grid"]//h3/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
class Museum_33:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        url = 'https://www.maigoo.com/citiao/61089.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '//*[@id="pos_articleinfo"]/ul[1]/li[2]/div/span/text()'
        str = ''
        tr = tree.xpath(xp)
        return tr[0]
    def getExhibition(self):
        url = 'http://www.tibetanculturemuseum.org/News_List.php?tag=Exhibition&theId=10'
        url2='http://www.tibetanculturemuseum.org/News_List.php?tag=Exhibition&theId=11'
        str = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        tex=res.text
        tree=etree.HTML(tex)
        xp='/html/body//div[@class="change"]//h3/a/text()'
        tr=tree.xpath(xp)
        str+='南馆：\n'
        for t in tr:
            str+=t.strip()+'\n'
        res = requests.get(url=url2, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="change"]//h3/a/text()'
        tr = tree.xpath(xp)
        str+='\n北馆：\n'
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getActivity(self):
        url = 'http://www.tibetanculturemuseum.org/News_List.php?tag=Activity&theId=35'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp='/html/body//div[@class="change"]//h2/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t.strip() + '\n'
        return str
    def getResearch(self):#Academic_cenleftcon1
        return '无'
    def getCollection(self):
        url = 'http://www.tibetanculturemuseum.org/News_List.php?tag=Collection'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        tree = etree.HTML(tex)
        xp = '/html/body//div[@class="change"]//h3/a/text()'
        tr = tree.xpath(xp)
        str = ''
        for t in tr:
            str += t + '\n'
        return str
class Museum_34:#时间，近期展览，社教活动，学术研究，经典藏品
    def getTime(self):
        return '已闭馆'
    def getExhibition(self):
        url = 'http://www.qhmuseum.cn/qhm-webapi/api/v1/permanent/permanentAll?pageNumber=1&pageSize=10'
        str = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        js=json.loads(tex)
        for j in js['data']['list']:
            str+=j['title']+'\n'
        return str
    def getActivity(self):
        url = 'http://www.qhmuseum.cn/qhm-webapi/api/v1/social/lectureAll?pageNumber=1&pageSize=10'
        str = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        js = json.loads(tex)
        for j in js['data']['list']:
            str += j['title'] +' '+j['address']+' '+j['jname']+' '+ '\n'
        return str
    def getResearch(self):  # Academic_cenleftcon1
        return '无'
    def getCollection(self):
        url = 'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=30&texture=104'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        tex = res.text
        js=json.loads(tex)
        str = ''
        for j in js['data']['list']:
            str+=j['collectionname']+':'+j['collectiondescribe']+' '+'\n'
        return str
class Museum_35:
    def __init__(self):
        self.url = "http://www.plsbwg.com/"
        self.strHtml = requests.get(self.url)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find_all('div', class_='openTime wrap2')
        m_span = texts[0].find_all('span')
        return m_span[1].text

    def getExhibition(self):
        url = self.url + '/index.php?m=content&c=index&a=lists&catid=20'
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_ = 'ab-main cl-main wrap3')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + '/index.php?m=content&c=index&a=lists&catid=31'
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='byj-content fl')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getResearch(self):

        return 'null'

    def getCollection(self):
        url = self.url + '/index.php?m=content&c=index&a=lists&catid=3'
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='wwTypeList')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

class Museum_36:
    def __init__(self):
        self.url = "http://www.tssbwg.com.cn/"
        self.strHtml = requests.get(self.url)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'html/2013/bzgg_1204/237.html'
        strHtml = requests.get(url)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='STYLE56')

        res = [0] * 100
        i = 0
        for s in texts[0]:
            res[i] = s
            i += 1

        msg = [0] * 100
        i = 0
        for s in res[2]:
            msg[i] = s
            i += 1
        return msg[2]

    def getExhibition(self):
        url = self.url + 'html/czxc/'
        strHtml = requests.get(url)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_ = 'bz2')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'html/fxwh/'
        strHtml = requests.get(url)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='list lh24 f14')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getResearch(self):
        url = self.url + 'index.php?m=content&c=index&a=show&catid=3&id=4875'
        strHtml = requests.get(url)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='STYLE56')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getCollection(self):
        url = self.url + 'html/guancang/'
        strHtml = requests.get(url)
        strHtml.encoding = 'gb2312'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', id='layout')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

class Museum_37:
    def __init__(self):
        self.url = "http://public.dha.ac.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return "旺季： 08:00 - 18:00 \n淡季： 09:00 - 17:30"

    def getExhibition(self):
        url = 'http://tour.dha.ac.cn/list.aspx?id=142223442522'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('tr')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + '/list.aspx?id=896339635046'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('tr')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getResearch(self):
        url = self.url + '/list.aspx?id=896339635046'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('tr')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getCollection(self):
        url = 'http://tour.dha.ac.cn/list.aspx?id=715037769780'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('tr')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

class Museum_38:
    def __init__(self):
        self.url = "http://www.dtxsmuseum.com/index.aspx"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return "全年开放（每周一及除夕闭馆，法定节假日正常开放）\n夏季：9：00-17：30（16：30停止票务办理）\n冬季：9：00-17：00（16:：0停止票务办理）"

    def getExhibition(self):
        url = 'http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=24'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span',class_ = 'title')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = 'http://www.dtxsmuseum.com/news_title_list.aspx?category_id=31'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('a',class_ = 'title')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = 'http://www.dtxsmuseum.com/news_title_list.aspx?category_id=41'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('a', class_='title')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = 'http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=29'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span',class_ = 'title')
        msg = ""
        for act in texts:
            msg += act.text +'\n'
        return msg

class Museum_39:
    def __init__(self):
        self.url = "http://www.yagmjng.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return " 每天开放时间为8：30—16：00时，星期六、星期日、法定节假日正常开放"

    def getExhibition(self):
        url = self.url + '/rsf/site/jinianguan/jibenchenlie/index.html'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('a',target = '_blank')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + '/rsf/site/jinianguan/quntuangongzuo/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('a',target = '_blank')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + '/rsf/site/jinianguan/yanjiuchengguo/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('a',target = '_blank')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'rsf/site/jinianguan/wenwujianshang/index.html'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('a',target = '_blank')
        msg = ""
        for act in texts:
            msg += act.text +'\n'
        return msg

class Museum_40:
    def __init__(self):
        self.url = "https://www.banpomuseum.com.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'index.php?m=content&c=index&a=lists&catid=8&kid=28'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='daodu01-l')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getExhibition(self):
        url = self.url + 'index.php?m=content&c=index&a=lists&catid=3&kid=17'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_ = 'txt1')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + 'index.php?m=content&c=index&a=lists&catid=37'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_ = 'shehui01-tp-txt')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getResearch(self):
        url = self.url + 'index.php?m=content&c=index&a=lists&catid=6'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul',id = 'newshe')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        msg = ""
        for id in range(19,20):
            url = self.url + 'index.php?m=content&c=index&a=lists&catid=' + str(id)
            strHtml = requests.get(url,headers = self.headers)
            strHtml.encoding = strHtml.apparent_encoding
            html = strHtml.text
            bf = BeautifulSoup(html, "html.parser")
            texts = bf.find_all('div',class_ = 'txt1')
            for act in texts:
                msg += act.text
        return msg

class Museum_41:
    def __init__(self):
        self.url = "https://www.xabwy.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return '旺季（3月15日至10月31日）9:00-18:00，17:00停止入园。\n淡季（11月1日至3月14日）9:00-17:30，16:30停止入园。\n每周二（国家法定节假日除外）及除夕闭馆，其余时间正常开放。'

    def getExhibition(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E5%AE%89%E5%8D%9A%E7%89%A9%E9%99%A2/4374388?fromtitle=%E8%A5%BF%E5%AE%89%E5%8D%9A%E7%89%A9%E9%A6%86&fromid=1627893&fr=aladdin#6'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        for i in range(53,71):
            s = selecter.xpath("""/html/body/div[3]/div[2]/div/div[1]/div[""" + str(i) + """]/text()""")
            msg += s[0]
        return msg

    def getActivity(self):
        url = 'https://www.sohu.com/na/466069917_121106869'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('article', class_ = 'article')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E5%AE%89%E5%8D%9A%E7%89%A9%E9%99%A2/4374388?fromtitle=%E8%A5%BF%E5%AE%89%E5%8D%9A%E7%89%A9%E9%A6%86&fromid=1627893&fr=aladdin#6'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = selecter.xpath("""/html/body/div[3]/div[2]/div/div[1]/div[93]/text()""")
        return msg[0]

    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E5%AE%89%E5%8D%9A%E7%89%A9%E9%99%A2/4374388?fromtitle=%E8%A5%BF%E5%AE%89%E5%8D%9A%E7%89%A9%E9%A6%86&fromid=1627893&fr=aladdin#6'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        for i in range(74, 91):
            s = selecter.xpath("""/html/body/div[3]/div[2]/div/div[1]/div[""" + str(i) + """]/text()""")
            msg += s[0]
        return msg

class Museum_42:
    def __init__(self):
        self.url = "http://www.hylae.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        selecter = etree.HTML(self.html)
        s = selecter.xpath(""" // *[ @ id = "index-one"] / div[2] / div[2] / div / div[1] / div[2] / text()[1]""")
        return s[0]

    def getExhibition(self):
        url = self.url + 'index.php?ac=article&at=list&tid=33'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='xinxi')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'index.php?ac=article&at=list&tid=53'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_ = 'wenzi')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'index.php?ac=article&at=list&tid=46'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('span',class_ = 'wenzi')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'index.php?ac=article&at=list&tid=37'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        msg = ""
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('span',class_ = 'xx')
        for act in texts:
            msg += act.text + '\n'
        return msg

class Museum_43:
    def __init__(self):
        self.url = "http://www.beilin-museum.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find_all('div', class_='visitR3')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getExhibition(self):
        url = self.url + 'index.php?m=home&c=Lists&a=index&tid=108'
        strHtml = requests.get(url,headers = self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='piclist')
        msg = ""
        for act in texts:
            s = act.find_all('p')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'index.php?m=home&c=Lists&a=index&tid=128'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_ = 'newslist')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'index.php?m=home&c=Lists&a=index&tid=120'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('ul',class_ = 'xsdtlist')
        msg = ""
        for act in texts:
            s = act.find_all('h2')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'index.php?m=home&c=Lists&a=index&tid=72'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='piclist')
        msg = ""
        for act in texts:
            s = act.find_all('p')
            for i in s:
                msg += i.text + '\n'
        return msg

class Museum_44:
    def __init__(self):
        self.url = "http://www.tibetmuseum.com.cn/zh-CN/index?navIndex=0"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E8%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/1627112?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        for i in range(62,66):
            s = selecter.xpath("/ html / body / div[3] / div[2] / div / div[1] / div[" + str(i) + "] /text()")
            msg += s[0] + '\n'
        return msg

    def getExhibition(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E8%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/1627112?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        for k in range(22,26):
            s = selecter.xpath(" / html / body / div[3] / div[2] / div / div[1] / div[" + str(k) + "] / text()")
            for i in s:
                msg += i
        return msg

    def getActivity(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E8%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/1627112?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        s = selecter.xpath(
            " / html / body / div[3] / div[2] / div / div[1] / div[48] /text()|/ html / body / div[3] / div[2] / div / div[1] / div[49]/text()")
        for i in s:
            msg += i
        return msg

    def getResearch(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E8%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/1627112?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        for k in range(52, 55):
            s = selecter.xpath(" / html / body / div[3] / div[2] / div / div[1] / div[" + str(k) + "] / text()")
            for i in s:
                msg += i
        return msg

    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E8%A5%BF%E8%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/1627112?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        for k in range(28, 46):
            s = selecter.xpath(" / html / body / div[3] / div[2] / div / div[1] / div[" + str(k) + "] / text()")
            for i in s:
                msg += i
        return msg

class Museum_45:
    def __init__(self):
        self.url = "http://www.ynnmuseum.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'canguan.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        selecter = etree.HTML(html)
        msg = ""
        s = selecter.xpath("""//*[@id="FrontComContent_detail01-1345106357285_cont_1"]/p[2]/text()""")
        for i in s:
            msg += i
        return msg

    def getExhibition(self):
        url = self.url + '/products_list/pmcId=36.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("li",class_ = 'code')
        msg = ""
        for act in texts:
            s = act.find_all('a')
            for i in s:
                msg += i.text
        return msg

    def getActivity(self):
        url = self.url + 'kj/c=7&i=7&comContentId=7.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='FrontComContent_detail01-1345105408838_htmlbreak')
        msg = ""
        for act in texts:
            s = act.find_all('p')
            for i in s:
                msg += i.text
        return msg

    def getResearch(self):
        url = self.url + 'kj/c=12&i=18&comContentId=18.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='FrontComContent_detail01-1345105408838_htmlbreak')
        msg = ""
        for act in texts:
            s = act.find_all('p')
            for i in s:
                msg += i.text
        return msg

    def getCollection(self):
        url = self.url + 'products_list1.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("ul", class_='basic')
        msg = ""
        for act in texts:
            s = act.find_all('a')
            for i in s:
                msg += i.text
        return msg

class Museum_46:
    def __init__(self):
        self.url = "http://www.ynmuseum.org/index.html"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find("div", class_='con')
        msg = ""
        msg += texts.text
        return msg

    def getExhibition(self):
        url = 'http://www.ynmuseum.org/exhibition/display.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div",class_ = 'con')
        msg = ""
        for act in texts:
            s = act.find_all("div" , class_ = 'h3')
            for i in s:
                msg += i.text
        return msg

    def getActivity(self):
        url = 'http://www.ynmuseum.org/education/events.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='con')
        msg = ""
        for act in texts:
            s = act.find_all("div", class_='h3')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getResearch(self):
        url = 'http://www.ynmuseum.org/learning/forum.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='con')
        msg = ""
        for act in texts:
            s = act.find_all("div", class_='h3')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getCollection(self):
        url = 'http://www.ynmuseum.org/appreciate/gem/bronze.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("ul", class_='prod_list cf')
        msg = ""
        for act in texts:
            s = act.find_all("div", class_='ellipsis')
            for i in s:
                msg += i.text + '\n'
        return msg

class Museum_47:
    def __init__(self):
        self.url = "http://www.gzsmzmuseum.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'news-30.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='detail_text')
        msg = ""
        for act in texts:
            s = act.find_all("p")
        msg += s[3].text+ s[4].text+s[5].text
        return msg

    def getExhibition(self):
        url = self.url + 'list-27.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("ul",class_ = 'newsli')
        msg = ""
        for act in texts:
            s = act.find_all('h3')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'list-19.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("ul", class_='newsli')
        msg = ""
        for act in texts:
            s = act.find_all('h3')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'list-15.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("ul", class_='newsli')
        msg = ""
        for act in texts:
            s = act.find_all('h3')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'collection.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('li')
        msg = ""
        for act in texts:
            s = act.find_all('h3')
            for i in s:
                msg += i.text + '\n'
        return msg

class Museum_48:
    def __init__(self):
        self.url = "http://www.gzmuseum.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + '/dl/cgzn/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find("div", class_='ls_miaosu f_l mgL25')
        msg = ""
        s = texts.find("p")
        msg += s.text
        return msg

    def getExhibition(self):
        url = self.url + 'zl/zzzc/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div",class_ = 'zzzc_ms f_l')
        msg = ""
        for act in texts:
            s = act.find_all('a')
            for i in s:
                msg += i.get('title') + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'hd/hdjz/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='ls_miaosu f_l')
        msg = ""
        for act in texts:
            s = act.find_all('a')
            for i in s:
                msg += i.get('title') + '\n'
        return msg

    def getResearch(self):
        url = self.url + '/xs/gbjt/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='ls_miaosu f_l')
        msg = ""
        for act in texts:
            s = act.find_all('a')
            for i in s:
                msg += i.get('title') + '\n'
        return msg

    def getCollection(self):
        url = self.url + '/dl/gzjx/gsw/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_='list_show')
        msg = ""
        for act in texts:
            s = act.find_all('p')
            for i in s:
                msg += i.text + '\n'
        return msg

class Museum_49:
    def __init__(self):
        self.url = "http://www.zunyihy.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + '#page2/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find("div", class_='time')
        msg = texts.text
        return msg

    def getExhibition(self):
        url = self.url + 'five_story.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div",class_ = 'txt')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + '/training.html#tr3'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='con')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getResearch(self):
        url = self.url + 'publication.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='t4 ellipsis')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        return "不可转载"

class Museum_50:
    def __init__(self):
        self.url = "https://baike.baidu.com/item/5%C2%B712%E6%B1%B6%E5%B7%9D%E7%89%B9%E5%A4%A7%E5%9C%B0%E9%9C%87%E7%BA%AA%E5%BF%B5%E9%A6%86/15421377?fr=aladdin#4"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find_all("div", class_='para')
        msg = ""
        for i in range(15,19):
            msg += texts[i].text + '\n'
        return msg

    def getExhibition(self):
        texts = self.bf.find_all("div", class_='para')
        msg = ""
        for i in range(25, 41):
            msg += texts[i].text + '\n'
        return msg

    def getActivity(self):
        texts = self.bf.find_all("div", class_='para')
        msg = ""
        for i in range(11, 14):
            msg += texts[i].text + '\n'
        return msg

    def getResearch(self):
        texts = self.bf.find_all("div", class_='para')
        msg = ""
        for i in range(97, 99):
            msg += texts[i].text + '\n'
        return msg

    def getCollection(self):
        texts = self.bf.find_all("div", class_='para')
        msg = ""
        for i in range(10, 11):
            msg += texts[i].text + '\n'
        return msg

class Museum_51:
    def __init__(self):
        self.url = "https://www.jc-museum.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'ticket/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("span", style='font-size:14px;')
        return texts[26].text

    def getExhibition(self):
        url = self.url + '/display/list-7/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div",class_ = 'list_box1 wf100')
        msg = ""
        for act in texts:
            s = act.find_all('p')
            for i in s:
                msg += i.text + '\n'
        return msg

    def getActivity(self):
        return 'null'

    def getResearch(self):
        url = 'https://baike.baidu.com/item/%E5%BB%BA%E5%B7%9D%E5%8D%9A%E7%89%A9%E9%A6%86/862201?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='para')
        msg = ""
        for i in range(136,148):
            msg += texts[i].text + '\n'
        return msg

    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E5%BB%BA%E5%B7%9D%E5%8D%9A%E7%89%A9%E9%A6%86/862201?fr=aladdin#7'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='para')
        msg = ""
        for i in range(21, 36):
            msg += texts[i].text + '\n'
        return msg

class Museum_52:
    def __init__(self):
        self.url = "http://www.zhudeguli.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find("div", class_='con1-Right')
        msg = texts.find('li',class_ = 'li1')
        return msg.text

    def getExhibition(self):
        url = self.url + 'article/tour_area'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("span",class_ = 'contents_list_span_left')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'article/info_news'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("span", class_='contents_list_span_left')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + '/article/zhude_culture'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("span", class_='contents_list_span_left')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getCollection(self):
        url = self.url + 'article/tour_collection'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("span", class_='contents_list_span_left')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

class Museum_53:
    def __init__(self):
        self.url = "http://www.zgshm.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return 'null'

    def getExhibition(self):
        url = self.url + '/imglist.jsp?id=78abd44f3517405da73197aa6e9b0ccb'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div",class_ = 'txt')
        msg = ""
        for act in texts:
            s = act.find('label')
            msg += s.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + '/pagelist.jsp?id=47be2172f5ef4be08038dd20d1e6773f'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find("div", class_='pagelist_con')
        s = texts.find_all('a')
        msg = ""
        for act in s:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + '/pagelist.jsp?id=5d7c6d5506e44fa28f5659754a347905'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find("div", class_='pagelist_con')
        s = texts.find_all('a')
        msg = ""
        for act in s:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + '/content.jsp?id=297e0fc26386368801638c40788f011f&classid=2e4d84b1fd574326ae0f1915eb1c28da'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", class_='news_conent_two_text')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

class Museum_54:
    def __init__(self):
        self.url = "http://www.sxd.cn/index.asp/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = 'http://www.sxd.cn/showinfo.asp?id=18&bigclass=31'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("p", class_='MsoNormal')
        msg = ""
        for i in range(5,7):
            msg += texts[i].text
        return msg

    def getExhibition(self):
        url = 'http://www.sxd.cn/showinfo.asp?id=9&bigclass=23'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("strong")
        msg = ""
        for act in range(3,9):
            msg += texts[act].text + '\n'
        return msg

    def getActivity(self):
        url = 'http://www.sxd.cn/list_1.asp?bigclass=25&smallclass=81'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'gb2312'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('table',class_='BORDER1')
        msg = ""
        for act in texts:
            for i in act.find_all('a'):
                msg += i.text + '\n'
        return msg

    def getResearch(self):
        url = 'http://www.sxd.cn/list_1.asp?bigclass=33'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'gb2312'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('table', class_='BORDER1')
        msg = ""
        for act in texts:
            for i in act.find_all('a'):
                msg += i.text + '\n'
        return msg

    def getCollection(self):
        url = 'http://www.sxd.cn/list_2.asp?bigclass=29'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("div", align='center')
        msg = ""
        for act in texts:
            msg += act.find('font').text
        return msg

class Museum_55:
    def __init__(self):
        self.url = "http://cpc.people.com.cn/GB/69112/69113/69687/index.html/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return '开放时间：淡季8:30～17:30　旺季8:30～18:00'

    def getExhibition(self):
        url = 'http://www.sxd.cn/showinfo.asp?id=9&bigclass=23'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all("strong")
        msg = ""
        for act in range(3,9):
            msg += texts[act].text + '\n'
        return msg

    def getActivity(self):
        url = 'https://baike.baidu.com/item/%E9%82%93%E5%B0%8F%E5%B9%B3%E6%95%85%E5%B1%85%E9%99%88%E5%88%97%E9%A6%86/9803788?fr=aladdin#3'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_='para')
        msg = ""
        for act in range(18,20):
            msg += texts[act].text + '\n'
        return msg

    def getResearch(self):
        url = 'http://cpc.people.com.cn/GB/69112/69113/69117/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'GB2312'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='list_14')
        msg = ""
        for act in texts:
            for i in act.find_all('a'):
                msg += i.text + '\n'
        return msg

    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E9%82%93%E5%B0%8F%E5%B9%B3%E6%95%85%E5%B1%85%E9%99%88%E5%88%97%E9%A6%86/9803788?fr=aladdin#3'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='para')
        msg = ""
        for act in range(15, 18):
            msg += texts[act].text + '\n'
        return msg

class Museum_56:
    def __init__(self):
        self.url = "http://www.zdm.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find('ul',class_='list1Box')
        return texts.text

    def getExhibition(self):
        url = self.url + 'display.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_="col-lg-6")
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + 'wikipedia_secrets.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div',class_='float-left title')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'results.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('p', class_='title')
        msg = ""
        for act in texts:
           msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + '/treasure.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('p', class_='jewelleryInfo wow fadeInUp')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

class Museum_57:
    def __init__(self):
        self.url = "http://www.cddfct.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'info/show/id/17/Tpls/w5'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('p', class_="MsoNormal")
        msg = ""
        for act in texts:
            msg += act.text
        return texts[4].text

    def getExhibition(self):
        url = self.url + 'index.php'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul',class_="carousel-list")
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + 'index.php'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('dd')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = 'https://baike.baidu.com/item/%E6%88%90%E9%83%BD%E6%9D%9C%E7%94%AB%E8%8D%89%E5%A0%82%E5%8D%9A%E7%89%A9%E9%A6%86/4824775?fr=aladdin#2'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='para')
        msg = ""
        for act in range(82, 86):
            msg += texts[act].text
        return msg

    def getCollection(self):
        url = 'https://baike.baidu.com/item/%E6%88%90%E9%83%BD%E6%9D%9C%E7%94%AB%E8%8D%89%E5%A0%82%E5%8D%9A%E7%89%A9%E9%A6%86/4824775?fr=aladdin#2'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='para')
        msg = ""
        for act in range(37,40):
            msg += texts[act].text
        return msg

class Museum_58:
    def __init__(self):
        self.url = "http://www.jinshasitemuseum.com/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + '/Visit/VisitOpenTime'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_="openTime-details")
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getExhibition(self):
        url = self.url + 'Exhibition/ExhibitionBasicDisplay'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('dd',style = 'color:#51280D;')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + '/CulturalActivity/CultureInternational'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = strHtml.apparent_encoding
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('div',class_ = 'international-item clearfix').find_all('dd')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = 'http://academic.jinshasitemuseum.com:8014/'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='xsjl')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getCollection(self):
        url = self.url + 'Treasure'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'UTF-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('div', class_='treasures-list container').find_all('p')
        msg = ""
        for act in texts:
            msg += act.get('title') + '\n'
        return msg

class Museum_59:
    def __init__(self):
        self.url = "https://baike.baidu.com/item/%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1628327?fr=aladdin"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return '周二至周日9：00-17:00'

    def getExhibition(self):
        texts = self.bf.find_all('h3',class_ = 'title-text')
        msg = ""
        for act in range(10):
            msg += texts[act].text + '\n'
        return msg

    def getActivity(self):
        return 'null'

    def getResearch(self):
        return 'null'

    def getCollection(self):
        texts = self.bf.find_all('div', class_='para')
        msg = ""
        for act in texts:
            s = act.find_all('b')
            for i in s:
                msg += i.text + '\n'
        return msg

class Museum_60:
    def __init__(self):
        self.url = "https://baike.baidu.com/item/%E5%A4%A7%E8%B6%B3%E7%9F%B3%E5%88%BB%E5%8D%9A%E7%89%A9%E9%A6%86/1010507?fr=aladdin"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return 'null'

    def getExhibition(self):
        texts = self.bf.find_all('div',class_ = 'para')
        msg = ""
        return texts[7].text

    def getActivity(self):
        return 'null'

    def getResearch(self):
        texts = self.bf.find_all('div', class_='para')
        msg = ""
        return texts[9].text

    def getCollection(self):
        texts = self.bf.find_all('div', class_='para')
        msg = ""
        return texts[6].text

class Museum_61:
    def __init__(self):
        self.url = "http://www.cqsxymjng.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'contents/19/729.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('p',style = 'margin:0px;text-indent:0em;')
        return texts.text

    def getExhibition(self):
        url = self.url + 'channels/236.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='ct')
        msg = ""
        for act in texts:
            msg += act.find('a').text + '\n'
        return msg

    def getActivity(self):
        url = self.url + '/channels/15.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='ct')
        msg = ""
        for act in texts:
            msg += act.find('a').text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'channels/240.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('li', class_='clearfix')
        msg = ""
        for act in texts:
            msg += act.find('a').text + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'channels/26.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='ct')
        msg = ""
        for act in texts:
            msg += act.find('a').text + '\n'
        return msg

class Museum_62:
    def __init__(self):
        self.url = "https://www.cmnh.org.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        texts = self.bf.find('p',class_ = 'pf')
        return texts.text

    def getExhibition(self):
        url = self.url + 'list/?11.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('p', class_='pm')
        msg = ""
        for act in texts:
            msg += act.find('a').get('title') + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'list/?71_1.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='xwListCon')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + '/list/?27_1.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='w382 fr')
        msg = ""
        for act in texts:
            msg += act.find('a').get('title') + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'list/?26_1.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='w382 fr')
        msg = ""
        for act in texts:
            msg += act.find('a').get('title') + '\n'
        return msg

class Museum_63:
    def __init__(self):
        self.url = "http://www.hainanmuseum.org/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + 'hnbwgcms/info/3055'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('p', style ='margin-bottom:0cm;line-height:2em')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getExhibition(self):
        url = self.url + 'hnbwgcms/node/250'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='f-left f-size-18 newsTitle f-family-impact')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + '/hnbwgcms/node/471'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='f-left f-size-18 newsTitle f-family-impact')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'hnbwgcms/node/264'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('div', class_='cbw box-bg').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + '/hnbwgcms/node/163'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('ul', class_='cultural2-tabs').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

class Museum_64:
    def __init__(self):
        self.url = "http://www.guilinmuseum.org.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        url = self.url + '/Home/Index'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_ ='cont')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getExhibition(self):
        url = self.url + 'Exhibition/Permanent/cszl'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('h3', class_='ellipsis')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

    def getActivity(self):
        url = self.url + '/News/List/sjhd'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='info')
        msg = ""
        for act in texts:
            msg += act.find('h3').text
        return msg

    def getResearch(self):
        url = self.url + '/News/List/kykt'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='info')
        msg = ""
        for act in texts:
            msg += act.find('h3').text
        return msg

    def getCollection(self):
        url = self.url + 'Collection/List/sh'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('ul', class_='collectlist').find_all('p')
        msg = ""
        for act in texts:
            msg += act.text
        return msg

class Museum_65:
    def __init__(self):
        self.url = "http://www.amgx.org/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }

    def getTime(self):
        return 'null'

    def getExhibition(self):
        url = self.url + 'exhibimore-32.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='mbright02t')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getActivity(self):
        url = self.url + 'more-94.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('div', class_='pdlistc02 listli').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'more-310.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('div', class_='pdlistc02 listli').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + 'boutique.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('div',class_='mbinnerr dright').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

class Museum_66:
    def __init__(self):
        self.url = "http://www.gxmuseum.cn/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', }
        self.strHtml = requests.get(self.url, headers=self.headers)
        self.strHtml.encoding = 'utf-8'
        self.html = self.strHtml.text
        self.bf = BeautifulSoup(self.html, "html.parser")

    def getTime(self):
        return '每周二至周日9：00-17：00(16:00停止发票，16：50清场)。每周一全天闭馆（国家法定假日除外）整修'

    def getExhibition(self):
        url = self.url + 'a/exhibition/11/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='show_sub')
        msg = ""
        for act in texts:
            msg += act.find('a').get('title') + '\n'
        return msg

    def getActivity(self):
        url = self.url + '/a/education/54/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('ul', class_='d1 mt2').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getResearch(self):
        url = self.url + 'a/science/93/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('ul', class_='d1 mt2').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg

    def getCollection(self):
        url = self.url + '/a/antique/index.html'
        strHtml = requests.get(url, headers=self.headers)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find('ul',class_='d5').find_all('a')
        msg = ""
        for act in texts:
            msg += act.text + '\n'
        return msg
# This is a sample Python script.
import requests
import csv
from bs4 import BeautifulSoup

class Museum_67(object):
    def __init__(self):
        url="http://www.ypzz.cn/f/index"
    def getTime(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='cgdl fr')
        m_span = texts[0].find_all('p')
        return (m_span[0].text)
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='picList')
        return (texts[0].text)
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.zgkjbwg.com/zwgk/hd/gnzx/t20210305_781.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='zhengwen')
        m_span = texts[0].find_all('p')
        s=""
        for i in range(4,12):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='title')
        s=texts[0].text
        texts = bf.find_all('div', class_='zhengwen')
        m_span = texts[0].find_all('p')
        for i in range(0, 2):
            s+=(m_span[i].text)+'\n'
        return s
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='same-height')
        m_span = texts[0].find_all('p')
        s=""
        for i in range(0,5):
            s+=(m_span[i].text)+'\n'
        return s

class Museum_68(object):
    def __init__(self):
        url="http://www.ypzz.cn/f/index"
    def getTime(self):
        url = "http://www.ypzz.cn/f/index"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='p2_r_inner')
        m_span = texts[0].find_all('p')
        return (m_span[1].text)
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.ypzz.cn/f/basicShow/detail?pid=3e807d55b08b46c297ca3c9256e9aa42&categoryId=19053eeacdc84f7e9c7c6cdb0be18949&cid=faa6b0cddc5f4db99515da890afece83"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='hd clear')
        m_span = texts[0].find_all('p')
        return (m_span[0].text)
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.ypzz.cn/f/hddetail?aid=8e313bfb059a4addb89ae7141d5e1cb1&pid=5e052004591d43259cd48a46af746e78&categoryId=5e052004591d43259cd48a46af746e78"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='bd clear')
        m_span = texts[0].find_all('p')
        s=""
        for i in range(1,9):
            s+=m_span[i].text+'\n'
        return s
    def getResearch(self):
        url="http://www.ypzz.cn/f/basicShow/newsxs?Name=%E3%80%8A%E6%98%8E%E6%B8%85%E6%B5%B7%E9%98%B2%E7%A0%94%E7%A9%B6%E3%80%8B%E7%AC%AC%E4%B8%80%E8%BE%91&Id=202a61ddeb5045bf88ee25cc7cd8ccbf&pid=8ec18e35918845798b31412fc6ca90bc&categoryId=c0927d419d9844c5b32924b4856f9887"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='top')
        m_span = texts[0].find_all('h3')
        return m_span[0].text
    def getCollection(self):
        url = "http://www.ypzz.cn/SANWEIWENTI/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        #texts = bf.find_all('div', class_='containers')
        m_span =" 19世纪英国皇家海军9磅炮弹搬运筒"
        return m_span

class Museum_69(object):
    def __init__(self):
        url="https://www.msrmuseum.com/"
    def getTime(self):
        url = "https://www.msrmuseum.com/"
        strHtml = requests.get(url,verify=False)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='yf-opentime text-center')
        return (texts[0].text)
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "https://www.msrmuseum.com/News/Index/28"
        strHtml = requests.get(url,verify=False)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='wrap')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0,7):
            s+=(m_span[i].text)+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url = "https://www.msrmuseum.com/News/Index/24"
        strHtml = requests.get(url, verify=False)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='wrap')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0, 2):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="https://www.msrmuseum.com/News/Detailed/22"
        strHtml = requests.get(url,verify=False)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('h1', class_='yf-submenu yf-pdt20')
        s=(texts[0].text)
        texts=bf.find_all('div',class_='yf-detail pull-left')
        s+=(texts[0].text)
        return s

    def getCollection(self):
        url = "https://www.msrmuseum.com/News/Special/4"
        strHtml = requests.get(url,verify=False)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='list-unstyled yf-article-list')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0,5):
            s+=(m_span[i].text)+'\n'
        return s

class Museum_70(object):
    def __init__(self):
        url="https://www.gzam.com.cn/"
    def getTime(self):
        url = "https://www.gzam.com.cn/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='Hkfsj')
        return (texts[0].text)
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "https://www.gzam.com.cn/zzzc/list_18.aspx?State=0"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='Content')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0, 3):
            s+=(m_span[i].text)+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="https://www.gzam.com.cn/jyhd/list_26.aspx"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='Content')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0,7):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="https://www.gzam.com.cn/yjlw/list_30.aspx"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='Content')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0, 7):
            s+=(m_span[i].text)+'\n'
        return s
    def getCollection(self):
        url = "https://www.gzam.com.cn/cp/info_24.aspx?itemid=36774&lcid=3"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='yc_infoCon')
        m_span = texts[0].find_all('span')
        s=""
        for i in range(1,3):
            s+=(m_span[i].text)+'\n'
        return s

class Museum_71(object):
    def __init__(self):
        url="https://www.gzchenjiaci.com/MYwebsite/rc/my_index.htm"
    def getTime(self):
        url = "https://www.gzchenjiaci.com/MYwebsite/rc/my_index.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='right')
        m_span = texts[0].find_all('p')
        s=(m_span[1].text)+'\n'+(m_span[2].text)
        return s
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        s=("岭南民间艺术展\n")+("岭南民间百艺")
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.zgkjbwg.com/zwgk/hd/gnzx/t20210305_781.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return("回顾 | 缤纷灰塑 俏丽女神 ——灰塑探索营妇女节专场活动")
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "《万紫千红：潮汕平原孕育的民间工艺大观》"
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "民国粉彩山水图长方盆\n"+"民国粉彩柳蝉纹梅瓶"

class Museum_72(object):
    def __init__(self):
        url="http://www.ypzz.cn/f/index"
    def getTime(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='cgdl fr')
        m_span = texts[0].find_all('p')
        return "09:00-17:30"
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='picList')
        return "镇海楼展区\n"+"美术馆展区\n"+"三·二九起义指挥部旧址纪念馆"
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.zgkjbwg.com/zwgk/hd/gnzx/t20210305_781.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "无"
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='title')
        return "无"
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "镇海楼"

class Museum_73(object):
    def __init__(self):
        url="http://www.sunyat-sen.org/"
    def getTime(self):
        url = "http://www.sunyat-sen.org/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='H2_01')
        m_span = texts[0].find_all('p')
        return (m_span[0].text)
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=53"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='dis_none')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0,7):
            s+=(m_span[i].text)+'\n'
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=76"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='ng_picbox')
        return (texts[0].text)
    def getResearch(self):
        url="http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=83"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='conli con_liwjx')
        m_span = texts[0].find_all('a')
        s=""
        for i in range(0, 6):
            s+=(m_span[i].text)+'\n'
        return s
    def getCollection(self):
        url = "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=173"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='ng_picbox')
        return (texts[0].text)

class Museum_74(object):  #网页没法右键查看源代码
    def __init__(self):
        url="https://www.shenzhenmuseum.com/?idnews=341"
    def getTime(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "开放时间10:00-18:00（17:30停止入场，周一闭馆，重要节假日期间开放，重要节假日后的第一天闭馆）"

    def getExhibition(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='picList')
        return "问陶之旅——深圳博物馆陶瓷展\n"+"吉金春秋——深圳博物馆铜器展\n"+"近代深圳"
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.zgkjbwg.com/zwgk/hd/gnzx/t20210305_781.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "我的博物馆之旅——深圳博物馆纪念手账体验官（第一期）招募公告\n"+"中国古代餐桌礼仪"
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='title')
        return "深圳民间文艺创新发展论坛在深圳博物馆召开"
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "原始青瓷提梁三足盉\n"+"1984年邓小平视察深圳时所乘的丰田中巴车\n"+"三彩白马"

class Museum_75(object):    #网站什么都有，但是爬不出来
    def __init__(self):
        url="https://www.gznywmuseum.org/"
    def getTime(self):
        url = "https://www.gznywmuseum.org/cgfw/index.jhtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "开放时间：9: 00 - - 17:30\n"+"全年开放（仅一天闭馆检测电力设备，时间不定）"
    def getExhibition(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='picList')
        return "滇王与南越王\n"+"曾国宝藏\n"+"寻找夜郎"
    def getActivity(self):
        url="http://www.zgkjbwg.com/zwgk/hd/gnzx/t20210305_781.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "探越学堂\n"+"南越工坊"
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "第十五期：古希腊罗马艺术鉴赏技巧——以庞贝展为例\n"+"第十六期：庞贝历史漫谈"
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "“右夫人玺”金印\n"+"赵昧玉印\n"+"“文帝行玺”金印"

class Museum_76(object):
    def __init__(self):
        url="https://www.gznywmuseum.org/"
    def getTime(self):
        url = "http://www.gdmuseum.com/gdmuseum/_300882/_300886/547925/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='detail_cont')
        m_span = texts[0].find_all('p')
        s=""
        for i in range(1,5):
            s+=(m_span[i].text)+'\n'
        return s

    def getExhibition(self):        #有很多空行怎么解决
        url = "http://www.gdmuseum.com/gdmuseum/_300730/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='product')
        s=""
        for i in range(0,3):
            s+=(texts[i].text)+'\n'
        return s
    def getActivity(self):
        url="http://www.gdmuseum.com/gdmuseum/_301014/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='name')
        s=""
        for i in range(0,3):
            s+=(texts[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.gdmuseum.com/gdmuseum/_300990/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='list_ul')
        m_span = texts[3].find_all('p')
        s=""
        for i in range(0, 2):
            s+=(m_span[i].text)+'\n'
        return s
    def getCollection(self):
        url = "http://www.gdmuseum.com/gdmuseum/_300746/_300758/tc45/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('a', class_='pro_title')
        s=""
        for i in range(0,4):
            s+=(texts[i].text)+'\n'
        return s

class Museum_77(object):
    def __init__(self):
        url="https://www.gznywmuseum.org/"
    def getTime(self):
        return "开放时间：全年开放\n"+"08:00-17:30"
    def getExhibition(self):
        url = "http://www.gdmuseum.com/gdmuseum/_300730/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "胡耀邦故居对外开放。现开放有故居、陈列馆、耀邦广场、胡氏宗祠、胡氏祖墓、胡家古井等多处景点。\n"
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.gdmuseum.com/gdmuseum/_301014/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "故居结合爱国主义教育基地自身特点，精心组织开展了多次主题鲜明、生动直观的宣传教育活动，使基地成为广大参观者缅怀先烈、树立理想和探索人生意义的活动基地及第二课堂。\n"
    def getResearch(self):
        url="http://www.gdmuseum.com/gdmuseum/_300990/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return ""
    def getCollection(self):
        url = "http://www.gdmuseum.com/gdmuseum/_300746/_300758/tc45/index.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "采用声、光、电等现代展示手段，共计展出图片330多幅，文物170多件，并用文物、雕刻、蜡像等复原展示了反映胡耀邦生平的9处场景。"

class Museum_78(object):
    def __init__(self):
        url="http://www.csm.hn.cn/#/Visit/appointment"
    def getTime(self):
        url = "http://www.csm.hn.cn/#/Visit/appointment"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "开放时间\n"+"每周二至周日9:00—17:00（16:30停止入馆），每周一（国家法定节假日除外）及农历除夕、正月初一、正月初二闭馆。"
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        s="湘江北去——长沙古代历史文化陈列\n"+"展览类型：常年陈列，免费开放\n"+"所在展厅：一楼一展厅、二展厅\n"+"展览内容：展示长沙自有人类活动以来，历经商周南征、楚人经略、唐宋繁华至清朝定为湖南中枢的发展过程"
        return s
    def getActivity(self):
        url="http://www.zgkjbwg.com/zwgk/hd/gnzx/t20210305_781.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        s="博乐园精品绘本流浪活动|狮身人面像是怎么来博物馆的\n"+"博乐园精品绘本流浪活动|陨石是怎么来博物馆的\n"
        return s
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        s="如果穿越到古代，这些字你认识吗？——衣着篇\n"+"一觉醒来，睡在古色古香的庭院中，来往皆是髻发长衫的人，说不出来的诡秘。望着镜中邋遢的自己，一脸茫然。既来之，则安之，衣食住行总是要继续，然而，这些物件你知道叫什么？怎么用吗？"
        return s
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='same-height')
        m_span = texts[0].find_all('p')
        s="商 象纹大铜铙\n"+"商 兽面纹觚\n"+"商 兽面夔龙纹提梁卣首页典藏详情页\n"
        return s

class Museum_79(object):
    def __init__(self):
        url="http://www.ypzz.cn/f/index"
    def getTime(self):
        url = "http://www.chinajiandu.cn/News/Details/fw#kfsj"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='cont')
        m_span = texts[0].find_all('p')
        return (m_span[2].text)
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        url = "http://www.chinajiandu.cn/Exhibition/TList/lszl"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('h3', class_='ellipsis')
        s=""
        for i in range(0,3):
            s+=(texts[i].text)+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.chinajiandu.cn/News/List/whjt"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('h3', class_='ellipsis')
        s=""
        for i in range(0,4):
            s+=(texts[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.chinajiandu.cn/News/List/xsyj"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('h3', class_='ellipsis')
        s = ""
        for i in range(0, 4):
            s += (texts[i].text) + '\n'
        return s
    def getCollection(self):
        url = "http://www.chinajiandu.cn/Collection/List/wj"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('h3', class_='ellipsis')
        s = ""
        for i in range(0, 4):
            s += (texts[i].text) + '\n'
        return s

class Museum_80(object):
    def __init__(self):
        url="http://www.csm.hn.cn/#/Visit/appointment"
    def getTime(self):

        return "参观时间： 9:00 - 17:00（16:30停止入园），周一生平陈列馆、工运专题馆、文保中心闭馆，其余景点正常开放。"
        #print(len(texts))
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getExhibition(self):
        s="《共和国主席刘少奇》展览简介及虚拟展厅\n"+"2018年刘少奇同志诞辰120周年之际，刘少奇同志纪念馆对刘少奇生平业绩陈列展览进行重新布展。新陈列的主题是“共和国主席刘少奇”，展线497米，展出图片400余张，展示文物实物94件，文物复制件182件，汉白玉主题雕塑2尊，油画8幅，艺术雕塑14尊，多媒体场景9个。"
        return s
    def getActivity(self):
        s="刘少奇同志故居\n"+"刘少奇同志纪念馆\n"+"炭子冲学校旧址"
        return s
    def getResearch(self):
        url="http://www.zgkjbwg.com/xsyj/yjcg/t20160918_111.htm"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        s="刘少奇同志纪念馆召开2020年度学术报告会\n"+"“他山之石 可以攻玉” ——刘少奇同志纪念馆举办考察学习成果交流会"
        return s
    def getCollection(self):
        url = "http://www.zgkjbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='same-height')
        m_span = texts[0].find_all('p')
        s="一块普通的门匾\n"+"使用过的1954年《中华人民共和国宪法》\n"+"一条褪了色的毛巾被"
        return s

class Museum_81(object):
    def __init__(self):
        url="http://www.hnmuseum.com/"
    def getTime(self):
        url = "http://www.hnmuseum.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='otherinfo_block')
        m_span=texts[0].find_all('p')
        return "开放时间\n"+m_span[0].text

    def getExhibition(self):
        url = "http://www.hnmuseum.com/zh-hans/content/%E5%BD%93%E5%89%8D%E5%B1%95%E8%A7%88%EF%BC%8D%E5%9F%BA%E6%9C%AC%E9%99%88%E5%88%97"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='view-content')
        return texts[0].text
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.hnmuseum.com/zh-hans/huodong_zhuanti"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('span', class_='field-content')
        s=""
        for i in range(0,4):
            s+=(texts[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.hnmuseum.com/zh-hans/jiangzuoyuyue"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('span', class_='field-content')
        s = ""
        for i in range(0, 3):
            s += (texts[i].text) + '\n'
        return s
    def getCollection(self):
        url = "http://www.hnmuseum.com/zh-hans/guangcang_gauobao"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('span', class_='field-content')
        s = ""
        for i in range(0, 4):
            s += (texts[i].text) + '\n'
        return s

class Museum_82(object):
    def __init__(self):
        url="http://www.hnmuseum.com/"
    def getTime(self):
        url = "http://www.changjiangcp.com/list/12.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='open')
        m_span=texts[0].find_all('p')
        return "开放时间\n"+m_span[0].text

    def getExhibition(self):
        url = "http://www.changjiangcp.com/list/19.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='scroll')
        return texts[0].text
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.changjiangcp.com/list/22.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='hotNews owl-carousel')
        m_span=texts[0].find_all('p')
        s=""
        for i in range(0,4):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.changjiangcp.com/list/26.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='hotNews owl-carousel')
        m_span = texts[0].find_all('p')
        s = ""
        for i in range(0, 4):
            s += (m_span[i].text) + '\n'
        return s
    def getCollection(self):
        url = "http://www.changjiangcp.com/list/150.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('h2', )
        s = ""
        for i in range(1, 5):
            s += (texts[i].text) + '\n'
        return s

class Museum_83(object):
    def __init__(self):
        url="http://www.hnmuseum.com/"
    def getTime(self):
        url = "http://www.zhongshanwarship.org.cn/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='am-u-sm-12 am-u-md-12 am-u-lg-3')
        m_span=texts[0].find_all('p')
        return "开放时间\n"+m_span[0].text

    def getExhibition(self):
        url = "http://www.zhongshanwarship.org.cn/zhanlan.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "中山舰史迹陈列\n"+"出水文物精品陈列\n"
    def getActivity(self):
        url="http://www.changjiangcp.com/list/22.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "对外交流|我馆与德国汉堡国际海事博物馆达成战略合作意向\n"+"武汉市中山舰博物馆志愿者招募公告\n"+"馆校合作 | “红色文化展览进校园”活动正式启幕"
    def getResearch(self):
        url="http://www.changjiangcp.com/list/26.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='hotNews owl-carousel')
        m_span = texts[0].find_all('p')
        return "关于2018年中国博物馆协会航海博物馆专业委员会 武汉年会学术论文集征稿的通知"

    def getCollection(self):
        url = "http://www.changjiangcp.com/list/150.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "二官厅餐桌\n"+"中山舰八号瓷碗\n"+"缆绳发射器"

class Museum_84(object):
    def __init__(self):
        url="http://wlt.hubei.gov.cn/1911museum/"
    def getTime(self):
        url = "http://wlt.hubei.gov.cn/1911museum/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "开放时间:\n"+"周二至周日，每天9:00——17:00 （16:00停止入馆）。\n"+"周一全天闭馆，国家法定节假日例外。"

    def getExhibition(self):
        url = "http://wlt.hubei.gov.cn/1911museum/clzl/jbcl/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text

        return "《为天下先——辛亥革命武昌起义史迹陈列》\n"+"《鄂军都督府旧址复原陈列》\n"+"《辛亥革命武昌起义纪念馆导览》"
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.changjiangcp.com/list/22.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "青少年课堂\n"+"首义寻踪\n"+"我心中的红楼"
    def getResearch(self):
        url="http://www.changjiangcp.com/list/26.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "《辛亥革命动态》征稿启事"
    def getCollection(self):
        url = "http://www.changjiangcp.com/list/150.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "粉彩双旗纹帽筒\n"+"王汉画像"

class Museum_85(object):
    def __init__(self):
        url="http://www.whgmbwg.com/"
    def getTime(self):
        url = "http://www.whgmbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='p1')
        return texts[6].text

    def getExhibition(self):
        url = "http://www.whgmbwg.com/clzl/jbcl2/index.shtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='gmg_ntwlb')
        return texts[0].text
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.whgmbwg.com/shjy/hdyg/index.shtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='gmg_nullb')
        m_span=texts[0].find_all('a')
        s=""
        for i in range(0,4):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.whgmbwg.com/kycg/xscg/index.shtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='gmg_nullb')
        m_span = texts[0].find_all('a')
        s = ""
        for i in range(0, 4):
            s += (m_span[i].text) + '\n'
        return s
    def getCollection(self):
        url = "http://www.whgmbwg.com/gzjx/index.shtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div',class_='gmg_pbl')
        m_span = texts[0].find_all('a')
        s = ""
        for i in range(0, 6):
            s += (m_span[i].text) + '\n'
        return s

class Museum_86(object):
    def __init__(self):
        url="https://www.szbwg.net/"
    def getTime(self):
        url = "https://www.szbwg.net/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='content-box')
        m_span=texts[1].find_all('p')
        return m_span[0].text+m_span[1].text

    def getExhibition(self):
        url = "https://www.szbwg.net/list-15-1.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='content-list')
        m_span=texts[0].find_all('h2')
        s=""
        for i in range(0,6,2):
            s+=m_span[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="https://www.szbwg.net/list-23-1.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='content')
        m_span=texts[0].find_all('p')
        s="编钟演奏：\n"
        for i in range(0,4):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="https://www.szbwg.net/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='news')
        m_span = texts[1].find_all('b')
        s = ""
        for i in range(0, 3):
            s += (m_span[i].text) + '\n'
        return s
    def getCollection(self):
        url = "https://www.szbwg.net/list-10-1.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div',class_='content-list')
        m_span = texts[0].find_all('h2')
        s = ""
        for i in range(0, 3):
            s += (m_span[i].text) + '\n'
        return s

class Museum_87(object):
    def __init__(self):
        url="http://www.ycbwg.com/"
    def getTime(self):
        url = "http://www.ycbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='time-item')
        return "开放时间：9：00-17：00，16：30停止入馆"

    def getExhibition(self):
        url = "http://www.ycbwg.com/web/exhibition/basicDisplay/list.shtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='clearfix')
        m_span=texts[0].find_all('h5')
        s=""
        for i in range(0,4):
            s+=m_span[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.ycbwg.com/web/education/socialEducation/list.shtml"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='listitem-box')
        m_span=texts[0].find_all('h1')
        s=""
        for i in range(0,4):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="https://www.szbwg.net/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        return "暂无\n"
    def getCollection(self):
        url = "http://www.ycbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div',class_='collect-item clearfix')
        m_span = texts[0].find_all('h5')
        s = ""
        for i in range(0, 4):
            s += (m_span[i].text) + '\n'
        return s

class Museum_88(object):
    def __init__(self):
        url="http://www.jzmsm.org/yk/"
    def getTime(self):
        url = "http://www.jzmsm.org/yk/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "免费开放时间（节假日不闭馆） 周二至周日上午 9:00 开馆 16:00 停止发票 17:00 闭馆 周一闭馆\n"

    def getExhibition(self):
        url = "http://www.jzmsm.org/yk/zhanlan/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='xwdt')
        m_span=texts[0].find_all('a')
        s=""
        for i in range(0,4):
            s+=m_span[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.jzmsm.org/yk/huodong1/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='xwdt')
        m_span=texts[0].find_all('a')
        s=""
        for i in range(0,5):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.jzmsm.org/yk/zhishi/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='xwdt')
        m_span = texts[0].find_all('a')
        s = ""
        for i in range(0, 5):
            s += (m_span[i].text) + '\n'
        return s
    def getCollection(self):
        url = "http://www.jzmsm.org/yk/cangpin/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='xwdt')
        m_span = texts[0].find_all('a')
        s = ""
        for i in range(0, 5):
            s += (m_span[i].text) + '\n'
        return s

class Museum_89(object):
    def __init__(self):
        url="https://www.whmuseum.com.cn/"
    def getTime(self):
        url = "https://www.whmuseum.com.cn/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "9:00 ~ 17:00 周二至周日（16:00停止入馆），周一闭馆（法定节假日除外）。\n"

    def getExhibition(self):
        url = "http://www.jzmsm.org/yk/zhanlan/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='xwdt')
        m_span=texts[0].find_all('a')
        s="历代文物陈列\n"+"古代陶瓷艺术陈列\n"+"武汉古代历史陈列"
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.jzmsm.org/yk/huodong1/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        s="武博“行走的课堂”微课：诗话忆清明 折菊寄哀思\n"+"武博送展——与您相约欢乐谷\n"+"馆校云牵手 新春嘉年华"
        return s
    def getResearch(self):
        url="http://www.jzmsm.org/yk/zhishi/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='xwdt')
        m_span = texts[0].find_all('a')
        s="清黄均《招鹤亭图》卷赏析\n"+"釉中奇葩——武汉博物馆馆藏明清蓝釉瓷珍萃"
        return s
    def getCollection(self):
        url = "http://www.jzmsm.org/yk/cangpin/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        s="马家窑文化蛙纹彩陶罐\n"+"屈家岭文化石耜\n"+"凤纹方罍"
        return s

class Museum_90(object):
    def __init__(self):
        url="http://www.hbww.org/home/Index.aspx"
    def getTime(self):
        url = "http://www.hbww.org/home/Index.aspx"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='opentime')
        return texts[0].text

    def getExhibition(self):
        url = "http://www.jzmsm.org/yk/zhanlan/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        s="曾侯乙\n"+"楚文化\n"
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.jzmsm.org/yk/huodong1/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        s="学雷锋日带你领略湖北省博物馆志愿者风采\n"+"湖北省博物馆“礼乐学堂”荣获“2015—2019”年度最佳研学课程及优秀研学线路"
        return s
    def getResearch(self):
        url="http://www.jzmsm.org/yk/zhishi/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        s = "关于“2020年度高等学校科学研究成果奖（科学技术）自然科学奖”提名的公示信息"
        return s
    def getCollection(self):
        url = "http://www.jzmsm.org/yk/cangpin/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        s = "曾侯乙编钟\n"+"越王勾践剑\n"+"云梦睡虎地秦简"
        return s

class Museum_91(object):
    def __init__(self):
        url="http://www.jzmsm.org/yk/"
    def getTime(self):
        url = "http://www.jzmsm.org/yk/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "开放时间：\n"+"参观时间：周二至周日上午9:00——下午5:00\n"+"下午4:00停止入场，周一闭馆"

    def getExhibition(self):
        url = "http://www.pdsm.org.cn/front/exhibit/exhibitdisplay.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='pic_list jbcl_list clearfix')
        m_span=texts[0].find_all('a')
        s=""
        for i in range(1,8,2):
            s+=m_span[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.pdsm.org.cn/front/information/index/cat_id/14/pid/8.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='art_list')
        m_span=texts[0].find_all('p')
        s=""
        for i in range(0,5,2):
            s+=(m_span[i].text)+'\n'
        return s
    def getResearch(self):
        url="http://www.pdsm.org.cn/front/information/index/cat_id/13/pid/7.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='art_list')
        m_span = texts[0].find_all('p')
        s = ""
        for i in range(0, 4, 2):
            s += (m_span[i].text) + '\n'
        return s
    def getCollection(self):
        url = "http://www.pdsm.org.cn/front/collection/browsecollection.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='pic_list jbcl_list clearfix')
        m_span = texts[0].find_all('p')
        s = ""
        for i in range(0, 5):
            s += (m_span[i].text) + '\n'
        return s

class Museum_92(object):
    def __init__(self):
        url="http://www.jzmsm.org/yk/"
    def getTime(self):
        url = "http://www.jzmsm.org/yk/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        return "开放时间：\n"+"参观时间：周二至周日上午9:00——下午5:00\n"+"下午4:30停止入场，周一闭馆"

    def getExhibition(self):
        url = "http://www.wzbwg.com/news/22"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='t1 truncate')
        s=""
        for i in range(0,4):
            s+=texts[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.wzbwg.com/Sjzc/jgxt"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='col s9 cont')
        return texts[0].text
    def getResearch(self):
        url="http://www.wzbwg.com/Xsyj"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('big', class_='truncate')
        return texts[0].text+'\n'+texts[1].text
    def getCollection(self):
        url = "http://www.pdsm.org.cn/front/collection/browsecollection.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='pic_list jbcl_list clearfix')
        m_span = texts[0].find_all('p')
        s = "善夫吉父鬲（lì）\n"+"伯梁其盨（xǔ）\n"+"父辛爵（jué）"
        return s

class Museum_93(object):
    def __init__(self):
        url="http://www.aybwg.org/"
    def getTime(self):
        url = "http://www.aybwg.org/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='in_zhinan_con clearfix')
        return texts[0].text

    def getExhibition(self):
        url = "http://www.aybwg.org/anbozhanlan/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='exbname')
        s=""
        for i in range(0,4):
            s+=texts[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.aybwg.org/anbojiaoyu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='newlist-container')
        s=""
        m_span=texts[0].find_all('p')
        for i in range(0,4):
            s+=m_span[i].text+'\n'
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = ""
        m_span = texts[0].find_all('p')
        for i in range(0, 4):
            s += m_span[i].text + '\n'
        return s
    def getCollection(self):
        url = "http://www.aybwg.org/photo/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='newlist-container')
        s = ""
        m_span = texts[0].find_all('span')
        for i in range(0, 4):
            s += m_span[i].text + '\n'
        return s

class Museum_94(object):
    def __init__(self):
        url="http://www.aybwg.org/"
    def getTime(self):
        url = "http://www.kfsbwg.com/html/2016/cgzn_0815/95.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='time')
        m_span=texts[0].find_all('p')
        return "开封市博物馆开放时间：每周二至周日，周一全天闭馆（国家法定节假日外）\n"

    def getExhibition(self):
        url = "http://www.kfsbwg.com/html/zhanlan/jbcl/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='tw')
        m_span=texts[0].find_all('p')
        s="开封记忆——近现代社会生活展\n"+"千年印记——馆藏石刻精品展\n"+"开封朱仙镇木版年画展"
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.aybwg.org/anbojiaoyu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='newlist-container')
        s="研学课程如火如荼 开博本周继续上新\n"+"画·色（二）｜“云”上非遗 96岁年画传承人直播古法炼色——遗产日特别活动"
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = "金犀·中国（开封）国际动漫节举办连环画讲座\n"+"开封市博物馆社教部工作人员参加河南博物院历史教室品牌合作单位2019年第一期"
        return s
    def getCollection(self):
        url = "http://www.aybwg.org/photo/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='newlist-container')
        s = "中姞鬲\n"+"清乾隆官窑霁红瓷瓶\n"+"明宣德青花瓷盘"
        return s

class Museum_95(object):
    def __init__(self):
        url="http://www.eywsqsfbwg.com/"
    def getTime(self):
        url = "http://www.eywsqsfbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='ind_ykxz')
        m_span=texts[0].find_all('p')
        return texts[0].text

    def getExhibition(self):
        url = "http://www.kfsbwg.com/html/zhanlan/jbcl/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='tw')
        m_span=texts[0].find_all('p')
        s="基本陈列：红色大别山\n"
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.aybwg.org/anbojiaoyu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='newlist-container')
        s="县博物馆、县教育局联合举办“诵读红色家书 传承红色基因”主题演讲比赛\n"
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = "【红色故事小讲堂】第六讲：智取“太湖野猪队”\n"
        return s
    def getCollection(self):
        url = "http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=lists&catid=15"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='of')
        m_span=texts[0].find_all('p')
        s = ""
        for i in range(0,4):
            s+=m_span[i].text+'\n'
        return s

class Museum_95(object):
    def __init__(self):
        url="http://www.eywsqsfbwg.com/"
    def getTime(self):
        url = "http://www.eywsqsfbwg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='ind_ykxz')
        m_span=texts[0].find_all('p')
        return texts[0].text

    def getExhibition(self):
        url = "http://www.kfsbwg.com/html/zhanlan/jbcl/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('ul', class_='tw')
        m_span=texts[0].find_all('p')
        s="基本陈列：红色大别山\n"
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.aybwg.org/anbojiaoyu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='newlist-container')
        s="县博物馆、县教育局联合举办“诵读红色家书 传承红色基因”主题演讲比赛\n"
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = "【红色故事小讲堂】第六讲：智取“太湖野猪队”\n"
        return s
    def getCollection(self):
        url = "http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=lists&catid=15"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('ul', class_='of')
        m_span=texts[0].find_all('p')
        s = ""
        for i in range(0,4):
            s+=m_span[i].text+'\n'
        return s

class Museum_96(object):
    def __init__(self):
        url="http://www.aybwg.org/"
    def getTime(self):
        url = "http://www.kfsbwg.com/html/2016/cgzn_0815/95.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='time')
        m_span=texts[0].find_all('p')
        return "开放时间：9:00-17:00,16:00停止入场 \n"

    def getExhibition(self):
        url = "http://www.hnzzmuseum.com/display9_list.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='special_box')
        s=""
        m_span=texts[0].find_all('a')
        for i in range(0,2):
            s+=m_span[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://www.hnzzmuseum.com/article4_list.html"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='n_box')
        s = ""
        m_span = texts[0].find_all('p')
        for i in range(0, 6,3):
            s += m_span[i].text + '\n'
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = "2016年郑州博物馆学术成果清单\n"+"2015年郑州博物馆学术成果清单"
        return s
    def getCollection(self):
        url = "http://www.hnzzmuseum.com/index"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('span', class_='bd_con_t')
        s = ""
        for i in range(0,4):
            s+=texts[i].text+'\n'
        return s

class Museum_97(object):
    def __init__(self):
        url="http://nyhhg.com/"
    def getTime(self):
        url = "http://nyhhg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='fcon_m')
        return texts[0].text

    def getExhibition(self):
        url = "http://nyhhg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='ygfc_ctv')
        s=""
        m_span=texts[0].find_all('p')
        for i in range(0,3):
            s+=m_span[i].text+'\n'
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://nyhhg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='gsjj')
        s = ""
        m_span = texts[0].find_all('li')
        for i in range(0, 4):
            s += m_span[i].text + '\n'
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = "2020年学术成果清单\n"+"2020年学术交流活动"
        return s
    def getCollection(self):
        url = "http://www.hnzzmuseum.com/index"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('span', class_='bd_con_t')
        s = "阳乌\n"+"雷公车\n"+"二桃杀三士"
        return s

class Museum_98(object):
    def __init__(self):
        url="http://nyhhg.com/"
    def getTime(self):
        url = "http://nyhhg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='fcon_m')
        return "09:00-17:00每周二至周日开馆接待游客\n"

    def getExhibition(self):
        url = "http://nyhhg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='ygfc_ctv')
        s="唐三彩馆\n"+"珍宝馆\n"+"宫廷文物馆\n"+"书画馆"
        return s
        #print(texts[0].text.replace('\u3000' * 13, '\n\n'))
    def getActivity(self):
        url="http://nyhhg.com/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('div', class_='gsjj')
        s = "“国学传承，健康生活”专题讲座圆满结束\n"+"提升业务素养 增强业务能力——洛阳博物馆业务培训圆满成功"
        return s
    def getResearch(self):
        url="http://www.aybwg.org/xueshuyanjiu/"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.find_all('div', class_='newlist-container')
        s = "徐昭峰：东周王城的文化内涵及现代启示"
        return s
    def getCollection(self):
        url = "http://www.hnzzmuseum.com/index"
        strHtml = requests.get(url)
        strHtml.encoding = 'utf-8'
        html = strHtml.text
        bf = BeautifulSoup(html, "html.parser")

        texts = bf.find_all('span', class_='bd_con_t')
        s = "“子申父己”铜鼎\n"+"乳钉纹铜爵\n"+"兽面纹铜方鼎"
        return s








#滕州市汉画像石馆
class Museum_99(object):

     def __init__(self):
          self.url = 'http://www.tzhhxsg.com/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag1 = soup.find_all('p', 'big')
          tag2 = soup.find_all('p', 'small')
          res = tag2[0].string + ' ' + tag1[0].string
          return res

     def getExhibition(self):
          url1 = self.url + 'index.php?c=content&a=list&catid=34'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          tag.pop()
          tag.pop(0)
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getActivity(self):
          url1 = self.url + 'index.php?c=content&a=list&catid=84'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p', 'bt')
          num = len(tag)
          i = 0
          res = list()
          while i < num:
               res.append(tag[i].text)
               i += 1
          return res


     def getResearch(self):
          url1 = self.url + 'index.php?c=content&a=list&catid=80'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p', 'bt')
          num = len(tag)
          i = 0
          res = list()
          while i < num:
               res.append(tag[i].text)
               i += 1
          return res


     def getCollection(self):
          url = self.url + 'index.php?c=content&a=list&catid='
          loc = 50
          res = list()
          while loc < 58:
               url1 = url + str(loc)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('p', attrs={})
               num = len(tag)
               i = 0
               while i < num:
                    if tag[i].text != '类别' and tag[i].text != '\n\n':
                         res.append(tag[i].text)
                    i += 1
               loc += 1
          return res



#淄博市陶瓷博物馆
class Museum_100(object):

     def __init__(self):
          self.url = 'http://www.zbstcbwg.cn/'

     def getTime(self):
          url1 = self.url + 'guide.html#gui1'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag1 = soup.find('div', 'time')
          tag2 = soup.find('div', 'ul')
          return tag1.text + tag2.text

     def getExhibition(self):
          url1 = self.url + 'basicDisplay.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'exhibition_list flex flex-wrap')
          return tag.text

     def getActivity(self):
          str = 'null'
          return str


     def getResearch(self):
          url1 = self.url + 'academic.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'list')
          return tag.text


     def getCollection(self):
          url1 = self.url + 'collections.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'name h18')
          res = ['龙山文化黑陶双耳杯', '龙山文化陶鬶', '黄地粉彩盘', '青釉莲花尊', '近代广彩开光人物盘', '金黑釉花口线条瓶']
          return res



#青岛山炮台遗址展览馆
class Museum_101(object):

     def __init__(self):
          self.url = 'http://www.qdyzyzmuseum.com/'

     def getTime(self):
          url1 = self.url + 'Home/About/content/pageid/50'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          return tag[1].text

     def getExhibition(self):
          url1 = self.url + 'Home/Zhanlan/index/cateid/48'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p', 'clips')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url = self.url + 'Home/Huodong/index/cateid/'
          loc = 40
          res = list()
          while loc < 44:
               url1 = url + str(loc)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('p', 'clips')
               for i in tag:
                    res.append(i.text)
               loc += 1
          return res


     def getResearch(self):
          url1 = self.url + 'Home/Yanjiu/index/cateid/31'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p', 'clips')
          num = len(tag)
          i = 0
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getCollection(self):
          url = self.url + 'Home/Huodong/index/cateid/'
          loc = 44
          res = list()
          while loc < 47:
               url1 = url + str(loc)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('p', 'clips')
               for i in tag:
                    res.append(i.text)
               loc += 1
          return res



#山东大学博物馆
class Museum_102(object):

     def __init__(self):
          self.url = 'http://museum.sdu.edu.cn/'

     def getTime(self):
          res = '周一至周五 上午9:30-11:30；下午14:00-17:00 节假日除外'
          return res

     def getExhibition(self):
          url = self.url + 'clzl/'
          res = list()
          mid = ['cszl.htm', 'ztzl.htm', 'zlyg.htm']
          for i in mid:
               url1 = url + str(i)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('div', 'pictitle')
               for j in tag:
                    res.append(j.text)
          return res

     def getActivity(self):
          url1 = self.url + 'bgxx/zhxx.htm'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', id='c')
          res = list()
          for i in tag:
               res.append(i.text)
          res.pop(0)
          return res


     def getResearch(self):
          url1 = self.url + 'xszz.htm'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'pica')
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getCollection(self):
          url = self.url + 'gchclist.jsp?totalpage=84&PAGENUM='
          loc = 1
          res = list()
          while loc < 85:
               url1 = url + str(loc)
               url1 += '&urltype=tree.TreeTempUrl&wbtreeid=1052'
               loc += 1
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('div', 'pictitle')
               for i in tag:
                   if i.text not in res:
                        res.append(i.text)
          return res



#济南市章丘区博物馆
class Museum_103(object):

     def __init__(self):
          self.url = 'http://www.bytravel.cn/landscape/107/zhangqiubowuguan.html'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          return tag[4].text

     def getExhibition(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          return tag[0].text

     def getActivity(self):
          res = 'null'
          return res


     def getResearch(self):
          res = 'null'
          return res


     def getCollection(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          return tag[0].text



#滕州市博物馆
class Museum_104(object):

     def __init__(self):
          self.url = 'http://www.tengzhoumuseum.com/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getExhibition(self):
          url1 = self.url + 'productlist/list-8-1.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('td')
          res = list()
          res.append(tag[21].string)
          res.append(tag[23].string)
          return res

     def getActivity(self):
          url1 = self.url + 'newslist/list-4-1.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('td', 'line2')
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getResearch(self):
          url1 = 'https://bwg.cnki.net/XSYJ_tzbwg.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'zhuan2')
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getCollection(self):
          url = self.url + 'productlist/list-1'
          loc = 13
          res = list()
          while loc < 21:
               url1 = url + str(loc) + '-1.html'
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('td', height="36", align="center", valign="top")
               for i in tag:
                    if i.text not in res:
                         res.append(i.text)
               loc += 1
          return res



#曲阜市孔子博物院
class Museum_105(object):

     def __init__(self):
          self.url = 'http://www.kzbwg.cn/'

     def getTime(self):
          r = requests.get(self.url,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('p')
          return tag.text

     def getExhibition(self):
          url1 = self.url + 'zhanlan/now/'
          r = requests.get(url1,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'jbclinfo')
          res = list()
          for i in tag:
               if i.text not in res:
                    res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'news/my/'
          r = requests.get(url1,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'dspt')
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getResearch(self):
          url1 = self.url + 'xueshu/xshd/'
          r = requests.get(url1,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'dspt')
          res = list()
          for i in tag:
               res.append(i.text)

          return res


     def getCollection(self):
          url = self.url + 'diancang/zhenpin/'
          loc = ['kfda', 'gjwx', 'tcq', 'tongqi', 'szp', 'sh', 'zmyd', 'ysq', 'jsq', 'jj']
          res = list()
          for i in loc:
               url1 = url + str(i) + '/'
               r = requests.get(url1,timeout=100)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('a', target="_blank")
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          res.pop(0)
          res.pop(0)
          return res



#济宁市博物馆
class Museum_106(object):

     def __init__(self):
          self.url = 'http://www.jiningmuseum.com/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('dl', 'guide-time clearfix')
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getExhibition(self):
          res = '济宁市博物馆推出自己的微信公众平台啦,期待您的关注！微信号：jnsbwg2015'
          return res

     def getActivity(self):
          url1 = self.url + 'list/article_list.do?channelId=204'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'news-list fl')
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getResearch(self):
          url1 = self.url + 'list/article_list.do?channelId=212'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'news-list fl')
          res = list()
          for i in tag:
               res.append(i.text)
          return res


     def getCollection(self):
          loc = ['陶器', '铜器', '玉石器、宝石', '瓷器', '金银器', '铁器、其他金属器', '漆器', '雕塑、造像', '石器、石刻、砖瓦', '书法、绘画', '文具', '甲骨', '玺印符牌', '钱币', '牙骨角器', '竹木雕', '家具', '珐琅器', '织绣', '古籍图书', '碑帖拓本', '武器', '邮品', '文件、宣传品', '档案文书', '名人遗物', '玻璃器', '乐器、法器', '皮革', '音像制品', '票据', '交通、运输工具', '度量衡器', '标本、化石', '其他']
          res = list()
          for i in loc:
               url1 = self.url + 'collection_list.do?leibie' + '=' + str(i)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('td', style="text-align:left")
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res



#烟台市博物馆
class Museum_107(object):

     def __init__(self):
          self.url = 'http://www.ytmuseum.com/'

     def getTime(self):
          url1 = self.url + 'service/kfsj'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', style="padding:0px;margin:0px;")
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getExhibition(self):
          url1 = self.url + 'showroom/notice'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_blank")
          res = list()
          for i in tag:
               if i.text not in res:
                    res.append(i.text)
          res.pop(0)
          return res

     def getActivity(self):
          url1 = self.url + 'informations/dt'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'listrow')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'academic/jd'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'listrow')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getCollection(self):
          loc = ['zg', 'cq', 'qtq', 'yq', 'zh', 'ww', 'gmww', 'qt']
          res = list()
          for i in loc:
               url1 = self.url + 'collection/' + str(i)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('div', 'dclist1')
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res



#齐国故城遗址博物馆
class Museum_108(object):

     def __init__(self):
          self.url = 'https://baike.baidu.com/item/%E9%BD%90%E6%96%87%E5%8C%96%E5%8D%9A%E7%89%A9%E9%A6%86/20621288?fromtitle=%E9%BD%90%E5%9B%BD%E6%95%85%E5%9F%8E%E9%81%97%E5%9D%80%E5%8D%9A%E7%89%A9%E9%A6%86&fromid=8715495&fr=aladdin'

     def getTime(self):
          res = '2016年9月12日，齐文化博物馆开馆, 2019年5月18日，齐文化博物馆实行门票免费对公众开放'
          return res

     def getExhibition(self):
          res = ['基本陈列展厅', '特色陈列展厅', '专题陈列展厅', '临时展厅']
          return res

     def getActivity(self):
          res = 'null'
          return res


     def getResearch(self):
          res = 'null'
          return res


     def getCollection(self):
          res = ['牺尊']
          return res



#青岛啤酒博物馆
class Museum_109(object):

     def __init__(self):
          self.url = 'https://baike.baidu.com/item/%E9%9D%92%E5%B2%9B%E5%95%A4%E9%85%92%E5%8D%9A%E7%89%A9%E9%A6%86/560506?fr=aladdin'

     def getTime(self):
          res = '08:30~16:30 '
          return res

     def getExhibition(self):
          res = ['核心区域', '生产工艺流程区域', '多功能区域']
          return res

     def getActivity(self):
          res = 'null'
          return res


     def getResearch(self):
          res = 'null'
          return res


     def getCollection(self):
          res = ['与世界干杯雕像', '西门子发电机', '全息投影', '醉酒小屋', 'TSINGTAO1903旗舰餐厅酒吧']
          return res



#济南市博物馆
class Museum_110(object):

     def __init__(self):
          self.url = 'http://www.jnmuseum.com/#/'

     def getTime(self):
          res = '开放时间：周二至周日9：00—17：00（16:30停止入馆），周一闭馆（法定节假日除外）'
          return res

     def getExhibition(self):
          res = ['《济南历史文化名城展》', '《古城辉煌——济南历史暨馆藏文物展览》', '古城辉煌——济南历史暨馆藏文物展览<二> ', '古城辉煌——济南历史暨馆藏文物展览', '古城辉煌——济南历史暨馆藏文物展览<一>']
          return res

     def getActivity(self):
          res = ['5.18国际博物馆日，簪娘工作坊活动报名', '济南市博物馆古建筑研学报名开始啦']
          return res


     def getResearch(self):
          res = ['曹操的“分香卖履”', '三神香', '寿阳公主梅花妆（香）']
          return res


     def getCollection(self):
          res = ['清冲耳龙纹三足鼎式铜炉', '清桥耳鬲式鎏金铜炉', '唐三彩三足炉', '中华民国镶珍珠戒指']
          return res



#潍坊市博物馆
class Museum_111(object):

     def __init__(self):
          self.url = 'http://www.wfsbwg.com/'

     def getTime(self):
          url1 = self.url + 'index.asp'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'gonggao_info')
          res = list()
          for i in tag:
               res.append(i.string)
          res.pop(0)
          res.pop()
          res.pop()
          return res

     def getExhibition(self):
          url1 = self.url + 'list/?53_1.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('li', style="position:relative;")
          res = list()
          for i in tag:
               if i.text not in res:
                    res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'list/?52_1.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('li', style="position:relative;")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'list/?23_1.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('li', 'list top')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getCollection(self):
          loc = ['6', '7', '56', '55', '54', '76', '20', '72', '73', '71']
          res = list()
          for i in loc:
               url1 = self.url + 'list/?' + str(i) + '_1.html'
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('li', style="position:relative;")
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res



#临沂市博物馆
class Museum_112(object):

     def __init__(self):
          self.url = 'http://museum.linyi.cn/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'w_timeR')
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getExhibition(self):
          res = ['“石上史诗”——汉画像石专题展', '馆藏造像和其他石刻艺术品陈列展', '临沂历史文化展', '书画、印章展', '“土与火的艺术”——陶器专题展', '铜镜、货币展', '沂蒙红色文化展', '家道馆']
          return res

     def getActivity(self):
          url1 = self.url + 'gzdt/lbkx.htm'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_blank")
          res = list()
          for i in tag:
               res.append(i.text)
          res.pop(0)
          res.pop(0)
          return res

     def getResearch(self):
          url1 = self.url + 'xsyj/yjhd.htm'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_blank")
          res = list()
          for i in tag:
               res.append(i.text)

          res.pop(0)
          return res

     def getCollection(self):
          res = ["新石器时代龙山文化夹砂...", "新石器时代大汶口文化夹...", "隋八系莲花瓣瓷罐", "新石器时代龙山文化泥质...", "新石器时代龙山文化泥质...", "新石器时代大汶口文化泥...", "新石器时代龙山文化泥质...", "新石器时代龙山文化泥质...", "汉彩绘陶俑1", "汉彩绘陶俑"]
          return res


#中国甲午战争博物院
class Museum_113(object):

     def __init__(self):
          self.url = 'http://jiawuzhanzheng.cn/'

     def getTime(self):
          url = self.url + '?page_id=9#entrancetime'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          res = list()
          res.append(tag[4].string)
          res.append(tag[5].string)
          return res

     def getExhibition(self):
          url = self.url + 'menu/visiting#visit-guide'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('ul')
          res = list()
          res.append(tag[2].text)
          return res

     def getActivity(self):
          url1 = self.url + 'news-cat/museum-news'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('h4')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'menu/papers'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('h4')
          res = list()
          for i in tag:
               res.append(i.text)

          res.pop(0)
          return res

     def getCollection(self):
          res = ['旅游码头', '北洋海军提督署', '龙王庙(请双击地图放大后查看)', '丁汝昌寓所(请双击地图放大后查看)', '北洋海军将士纪念馆(请双击地图放大后查看)', '水师学堂(请双击地图放大后查看)', '旗顶山炮台(请双击地图放大后查看)', '东泓炮台(请双击地图放大后查看)']
          return res



#青州市博物馆
class Museum_114(object):

     def __init__(self):
          self.url = 'http://www.qingzhoumuseum.cn/'

     def getTime(self):
          url = self.url + 'fw/cgzn/'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('span', style="font-family: 宋体; mso-ascii-font-family: Calibri; mso-ascii-theme-font: minor-latin; mso-fareast-font-family: 宋体; mso-fareast-theme-font: minor-fareast; mso-hansi-font-family: Calibri; mso-hansi-theme-font: minor-latin")
          res = list()
          res.append(tag[9].text)
          return res

     def getExhibition(self):
          url = self.url + 'zl/jbcl/'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('span', 'title2', style="color:#81191e;")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'zx/wbzx/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('span', style="color:#81191e;")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'xs/cbw/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('span', style="font-family: 微软雅黑;font-size: 18px;color: #91300f;")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getCollection(self):
          loc = ['tq', 'cq', 'sh', 'yq', 'qtq', 'sk', 'lxs', 'qt']
          res = list()
          for i in loc:
               url1 = self.url + 'cp/' + str(i) + '/'
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('span', style="font-family: 微软雅黑;font-size: 18px;color: #91300f;")
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res




#青岛市博物馆
class Museum_115(object):

     def __init__(self):
          self.url = 'http://www.qingdaomuseum.com/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'str1 str_wrap')
          return tag.text

     def getExhibition(self):
          url = self.url + 'exhibition/category/16'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'zl_text')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'education'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'sj_text')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'study/index/29'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'col-xs-12 col-md-10')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getCollection(self):
          url = self.url + 'collection/category/36'
          res = list()
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'form-group')
          for j in tag:
               if j.text not in res:
                    res.append(j.text)
          return res



#山东博物馆
class Museum_116(object):

     def __init__(self):
          self.url = 'http://www.sdmuseum.com/'

     def getTime(self):
          res = ['周二至周日9:00—17:00开馆，16:00停止入馆', '周一（除国家法定节假日）闭馆']
          return res

     def getExhibition(self):
          url = self.url + 'channels/ch00069/'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'zl2-con-t2')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'channels/ch00011/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('td', 'lblist')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'channels/ch00117/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'liebiao-r')
          res = list()
          for i in tag:
               res.append(i.text)
          res.pop(0)
          return res

     def getCollection(self):
          loc = ['ch00079/', 'ch00081/', 'ch00083/', 'ch00099/', 'ch00101/', 'ch00826/', 'ch00827/']
          res = list()
          for i in loc:
               url1 = self.url + 'channels/' + str(i)
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('div', 'cp-name')
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res



#赣州市博物馆
class Museum_117(object):

     def __init__(self):
          self.url = 'http://www.gzsbwg.cn/'

     def getTime(self):
          res = '开放时间：每周二至周日, 逢周一闭馆（法定节假日和特殊情况除外）'
          return res

     def getExhibition(self):
          url = self.url + 'html/m_infolist-16.html'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', style="padding-top:5px;line-height:20px;")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'html/m_infolist-12.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', style="padding-top:5px;line-height:20px;")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'html/m_infolist-27.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          res = list()
          for i in tag:
               res.append(i.text)
          res.pop(0)
          return res

     def getCollection(self):
          loc = ['32', '33', '35', '36']
          res = list()
          for i in loc:
               url1 = self.url + 'html/m_infolist-' + str(i) + '.html'
               r = requests.get(url1)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('div', style="padding-top:5px;line-height:20px;")
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res



#萍乡博物馆
class Museum_118(object):

     def __init__(self):
          self.url = 'http://www.pxmuseum.com/'

     def getTime(self):
          res = ['全年免费对外开放周一闭馆（法定节假日除外）,周二到周日　夏季9:00-17:00（16:30停止入馆）,冬季9:00-16:30（16:00停止入馆）']
          return res

     def getExhibition(self):
          res = ['展览预告 | 到世界找敦煌——敦煌流散海外文物复制展', '展览预告 | 鉴证千秋——历代铜镜精品展', '展览预告 | 李祖葳山水画作品展', '展览预告】奔走在生命线上的凡人——萍乡民间公益救援队事迹图片展', '【展讯预告 】甘远龙水彩画展即将在萍乡博物馆开展']
          return res

     def getActivity(self):
          res = ['喜讯！萍乡博物馆荣升为国家一级博物馆！', '展览预告 | 到世界找敦煌——敦煌流散海外文物复制展', '“非遗＋文保”——萍乡博物馆开展社会教育系列活动', '萍乡博物馆在萍乡孔庙举行“游文庙，闹元宵，猜灯谜”活动']
          return res

     def getResearch(self):
          res = ['谈萍乡博物馆建筑防火设计及灭火设施', '浅谈博物馆的财务管理工作', '关于博物馆社会教育的思考']
          return res

     def getCollection(self):
          res = ['东汉斜方格纹陶罈', '东汉铁斧', '西汉斜方格纹圈足陶缽', '东汉双唇陶盖罐', '东汉带顶陶鸡舍', '唐陶男人俑']
          return res



#江西省庐山博物馆
class Museum_119(object):

     def __init__(self):
          self.url = 'http://www.lushanmuseum.com/'

     def getTime(self):
          res = ['08:00-17:30 (1月1日-12月31日 周一-周日)']
          return res

     def getExhibition(self):
          url = self.url + 'show_info.asp?id=89'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('span', 'left_list')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'news.asp?id=62'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_blank")
          res = list()
          for i in tag:
               res.append(i.text)
          res.pop(0)
          return res

     def getResearch(self):
          res = ['论陈銮《传砚图》的文史价值']
          return res

     def getCollection(self):
          res = ['五百罗汉图']
          return res



#九江市博物馆
class Museum_120(object):

     def __init__(self):
          self.url = 'http://www.jjmuseum.cn/lib/Index.html'

     def getTime(self):
          r = requests.get(self.url,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'hea-new')
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getExhibition(self):
          res = ['浔阳文脉——九江非物质文化遗产集萃', '九派云横——九江历史文化陈列']
          return res

     def getActivity(self):
          res = ['九江市博物馆清明假期开放公告', '2020年《政府工作报告》量化指标任务完成了！', '转载|总理报告：人民是真正的英雄']
          return res


     def getResearch(self):
          res = ['九江市博物馆海昏侯学术讲座']
          return res


     def getCollection(self):
          res = 'null'
          return res




#景德镇中国陶瓷博物馆
class Museum_121(object):

     def __init__(self):
          self.url = 'http://www.zgtcbwg.com/index.php'

     def getTime(self):
          url = self.url + '?s=/Home/Article/page/id/60.html'
          r = requests.get(url,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('span', style="font-size:16px;color:#64451D;")
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getExhibition(self):
          url = self.url + '?s=/Home/Article/lists/category/newzl.html'
          r = requests.get(url,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'row newslist')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + '?s=/Home/Article/lists/category/eduactvie.html'
          r = requests.get(url1,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'row newslist')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + '?s=/Home/Article/lists/category/Researchfindings.html'
          r = requests.get(url1,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'row newslist')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getCollection(self):
          res = list()
          loc = ['ancientceramics.html', 'mceramics.html', 'modernceramics.html']
          for i in loc:
               url = self.url + '?s=/Home/Article/lists/category/' + str(i)
               r = requests.get(url,timeout=100)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('div', 'col-xs-3 text-center')
               for j in tag:
                    if j.text not in res:
                       res.append(j.text)
          return res



#八大山人纪念馆
class Museum_122(object):

     def __init__(self):
          self.url = 'http://www.bdsrjng.cn/'

     def getTime(self):
          r = requests.get(self.url,timeout=100)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('p')
          res = list()
          res.append(tag[12].string)
          res.append(tag[14].string)
          return res

     def getExhibition(self):
          res = 'null'
          return res

     def getActivity(self):
          res = 'null'
          return res

     def getResearch(self):
          res = ['八大仙人研究']
          return res

     def getCollection(self):
          res = ['仿董北苑山水轴', '行书程子四箴', '杂画册']
          return res




#安源路矿工人运动纪念馆
class Museum_123(object):

     def __init__(self):
          self.url = 'http://www.aymuseum.com/'

     def getTime(self):
          res = ['开放日期：星期二至星期日   星期一闭馆检修,参观时间：夏季9:00——17:30（17:00停止入内）,冬季9:00——17:00（16:30停止入内）']
          return res

     def getExhibition(self):
          res = 'null'
          return res

     def getActivity(self):
          res = '铭记初心学党史——安源纪念馆党史学习专题教育'
          return res

     def getResearch(self):
          res = 'null'
          return res

     def getCollection(self):
          res = ['照亮工人革命道路的一扇窗——《安源旬刊》', '劳工之歌--《劳工记》', '红色股票', '大罢工的胜利成果《十三条协议》', '播撒工人信仰的种子——《小学国语教科书》']
          return res



#瑞金中央革命根据地纪念馆
class Museum_124(object):

     def __init__(self):
          self.url = 'http://www.rjjng.com.cn/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'box')
          res = list()
          res.append(tag[0].text)
          res.append(tag[1].text)
          return res

     def getExhibition(self):
          url = self.url + 'jiuzhi.thtml?id=10955'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'c')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'list.thtml?id=10944'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'txt txt2')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getResearch(self):
          url1 = self.url + 'xueshu.thtml?id=10965'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_blank")
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getCollection(self):
          loc = 10950
          res = list()
          while loc < 10955:
               url = self.url + 'cangpin.thtml?id=' + str(loc)
               r = requests.get(url)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('a', target="_blank")
               for j in tag:
                    if j.text not in res:
                        res.append(j.text)
               loc += 1
          return res




#井冈山革命博物馆
class Museum_125(object):

    def __init__(self):
        self.url = 'http://www.jgsgmbwg.com/'

    def getTime(self):
        res = '开放时间：每星期二至星期日8：00—17：00，每周一闭馆（国家法定节假日除外）。'
        return res

    def getExhibition(self):
        return '序厅 朱毛会师 红军洞 黄洋界保卫战 挑粮上山 党的一大旧址 八角楼的灯光 三湾改编 长征出发 五百里井冈 九八抗洪 “胜利的起点”'
    def getActivity(self):
        return '井冈山革命博物馆举办“迎端午 学传统”主题社会教育活动 2018-06-19\n星火燎原——井冈山斗争革命故事讲述 2019-2-9'

    def getResearch(self):
        s='井冈山革命博物馆在丰富的馆藏文物、资料的基础上，充分发挥文物保管、史料整理、专题研究、编纂出版等专业人员的作用，现在已形成一支具有相当水平的老中青结合的科研编辑队伍，先后整理出井冈山斗争史的专题课目196个；在深入开展陈列研究、学术交流的同时，在省级以上各出版社或报刊杂志出版、发表的专著、论文有：由馆里编纂出版的专著15部；馆里参与出版的专著25部；专业人员个人编著出版的专著30余部；专业人员撰写的各种专题论文、考证文章500余篇达1000余万字；获得省级以上各种奖励25部（篇）；定期编辑出版学术期刊《井冈山精神研究》和馆刊《摇篮》，创办井冈山革命博物馆网站，在全国文博界广泛地开展学术交流活动。'
        return s

    def getCollection(self):
        return '朱德题名手稿 钟步全的党徽 王佐的青龙剑 横街合作社印 党会的记录本'




#景德镇中国陶瓷博物馆
class Museum_126(object):

     def __init__(self):
          self.url = 'http://www.81-china.com/'

     def getTime(self):
          url = self.url + '?s=/Home/Article/page/id/60.html'
          r = requests.get(url)
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('div', 'canguanxinxi')
          res = list()
          for i in tag:
               res.append(i.string)
          return res[5]+res[7]

     def getExhibition(self):
          url = self.url + 'zhanlan/57.html'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_self")
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(8):
               res.pop(0)
          return res

     def getActivity(self):
          url1 = self.url + 'news/52.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_self")
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(8):
               res.pop(0)
          return res

     def getResearch(self):
          url1 = self.url + 'research/63.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_self")
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(5):
               res.pop(0)
          return res

     def getCollection(self):
          res = list()
          loc = ['60', '61', '62', '117']
          for i in loc:
               url = self.url + 'collect/' + str(i) + '.html'
               r = requests.get(url)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('a', target="_self")
               for j in tag:
                    if j.text not in res:
                       res.append(j.text)
          for i in range(7):
               res.pop(0)
          return res



#江西省博物馆
class Museum_127(object):

     def __init__(self):
          self.url = 'http://www.jxmuseum.cn/'

     def getTime(self):
          res = ['9:00开馆-16:00停止入馆-17:00闭馆, 周二至周日免费开放（周一闭馆，节假日除外）']
          return res

     def getExhibition(self):
          res = ['物华天宝 人杰地灵——江西古代历史文化展', '红色摇篮 ——江西革命史陈列', '万年窑火 千年瓷都——江西古代陶瓷文化展', '物华新诗——赣鄱非遗展']
          return res

     def getActivity(self):
          res = ['江西省博物馆开展2021年第一季度公共机构节能环保宣传活动', '资讯 | 江西省博物馆理事会成立大会暨第一次会议召开']
          return res

     def getResearch(self):
          res = ['《饰代风华—江西省博物馆藏明代王妃首饰精品展》', '《江西宋代纪年墓与纪年青白瓷》']
          return res

     def getCollection(self):
          res = ['商虎耳虎形扁足青铜鼎', '七里镇窑褐釉乳丁柳条纹罐', '商神人兽面纹玉牌', '明鎏金四瓣花形扣', '蓝涛工笔人物花卉翎毛山水图册（共8幅）']
          return res




#中央苏区（闽西）历史博物馆
class Museum_128(object):

     def __init__(self):
          self.url = 'http://www.crt.com.cn/mx/'

     def getTime(self):
          res = ['开放时间：星期二到星期日上午8：15到11：45，下午2：15到5：15，夏季：上午不变，下午3：00到5：45，实行免费开放, 闭馆时间：每星期一']
          return res

     def getExhibition(self):
          res = ['展讯《从闽西大山走出的开国功臣——七位闽西籍革命老前辈诞辰百年纪念展》', '展讯：《苏区精神 永放光芒》', '《陈培光中国画作品展》及《青春奉献 老有所为——詹灿富捐赠文物展》']
          return res

     def getActivity(self):
          res = ['《红色遗珍 见证辉煌——闽西革命文物背后的故事精品展》荣登“福建陈列展最佳创意项目”', '闽粤赣边老同志陈少明亲属来我馆参观']
          return res

     def getResearch(self):
          res = ['中央苏区（闽西）历史博物馆2019年第一场“红色文化”讲堂开讲', '调查红军标语 保护文化遗产（一）——我馆赴武平县中堡镇林坊村调查红军标语侧记']
          return res

     def getCollection(self):
          res = ['20世纪50年代外国使团赠邓子恢的钵子', '20世纪50年代袁子钦的抗美援朝二级国旗勋章', '1934—1936年黄乎在长征中缴获的医用镊子']
          return res



#古田会议纪念馆
class Museum_129(object):

     def __init__(self):
          self.url = 'http://www.gthyjng.com/'

     def getTime(self):
          r = requests.get(self.url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'con1_top')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getExhibition(self):
          res = 'null'
          return res

     def getActivity(self):
          url1 = self.url + 'xwzx/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('h1')
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(8):
               res.pop()
          return res

     def getResearch(self):
          url1 = self.url + 'kxyj/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('a', target="_blank")
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(3):
               res.pop()
          res.pop(0)
          return res

     def getCollection(self):
          res = list()
          loc = ['tdgmsq/', 'krzzsq/', 'jfzzsq/', 'gjdww/']
          for i in loc:
               url = self.url + 'gcww/wwjs/' + str(i)
               r = requests.get(url)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('p')
               for j in tag:
                    if j.text not in res:
                         res.append(j.text)
          return res



#泉州海外交通史博物馆
class Museum_130(object):

     def __init__(self):
          self.url = 'http://www.qzhjg.cn/html/'

     def getTime(self):
          url = self.url + 'index.html'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find('dl', 'col_info', style="border: 1px solid #fff;border-width: 0 0 0 1px;margin-top: 20px;padding: 0 25px;")
          res = list()
          for i in tag:
               res.append(i.string)
          return res

     def getExhibition(self):
          url = self.url + 'gdzl/'
          r = requests.get(url)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('div', 'info')
          res = list()
          for i in tag:
               res.append(i.text)
          return res

     def getActivity(self):
          url1 = self.url + 'zhdt/index.html'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('ul')
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(3):
               res.pop(0)
          return res

     def getResearch(self):
          url1 = self.url + 'xsdt/'
          r = requests.get(url1)
          
          r.encoding = r.apparent_encoding
          demo = r.text
          soup = BeautifulSoup(demo, "html.parser")
          tag = soup.find_all('ul')
          res = list()
          for i in tag:
               res.append(i.text)
          for i in range(3):
               res.pop(0)
          return res

     def getCollection(self):
          res = list()
          loc = ['jddc/', 'qzwxc/', 'wyj/']
          for i in loc:
               url = self.url + str(i)
               r = requests.get(url)
               
               r.encoding = r.apparent_encoding
               demo = r.text
               soup = BeautifulSoup(demo, "html.parser")
               tag = soup.find_all('ul', 'clearfix')
               for j in tag:
                    if j.text not in res:
                       res.append(j.text)
          res.pop(0)
          return res