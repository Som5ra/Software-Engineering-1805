from fileinput import filename
from time import sleep
import xlrd
from xlutils.copy import copy
import requests
import os
import re
from lxml import etree
import json
import museumClass
from bs4 import BeautifulSoup
import museumClass
import selenium
from selenium import webdriver
def transform(t):
    if type(t).__name__=='list':
        str=''
        for l in t:
            if l!=None:
                str+=l
        return str
    else :
        return t

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}

params={
    'action': 'getpage',
    'dataid': '2519808',
    'page': '1',
    'templateid': '5548',
    'ismobile': '0',
    'startid': '100',
    'num': '100',
    'append': '1',
    'numshow': '204',
    'blockac': 'zhishi',
    'blockitid': '167245'
}

url="https://www.maigoo.com/goomai/167245.html"
museumHtml=requests.get(url=url,headers=headers,timeout=30).text
museumTree=etree.HTML(museumHtml)
museumDict='{'
museumMessageUrlDict='{'
museumLocationDict='{'
#前一百个名字，网址
for i in range(2,102):
    xp='//*[@id="modellist-678504"]/div/div[1]/div/table/tr['+str(i)+']/td[2]/a/text()'
    xp2='//*[@id="modellist-678504"]/div/div[1]/div/table/tr['+str(i)+']/td[2]/a/@href'
    xp3='//*[@id="modellist-678504"]/div/div[1]/div/table/tr['+str(i)+']/td[4]/text()'
    museumName=museumTree.xpath(xp)
    museumMessageUrl=museumTree.xpath(xp2)
    museumLocation=museumTree.xpath(xp3)
    museumDict = museumDict + '"'+str(museumName[0])+ '"'+':' + '"' + str(i) + '",'
    museumMessageUrlDict=museumMessageUrlDict+'"' + str(i) + '"'+ ':' + '"'+str(museumMessageUrl[0])+'" ,'
    museumLocationDict=museumLocationDict+'"' + str(i) + '"'+ ':' + '"'+str(museumMessageUrl[0])+'" ,'


url="https://www.maigoo.com/public/mod/php/getpage.php?action=getpage&dataid=2519808&page=1&templateid=5548&ismobile=0&startid=100&num=100&append=1&numshow=204&blockac=zhishi&blockitid=167245"
museumHtml=requests.get(url=url,params=params,headers=headers,timeout=30).text
museumTree=etree.HTML(museumHtml)
#后三十个名字，网址
for i in range(1,32):
    xp='/html/body/tr[@class="li font14"]['+str(i)+']/td[@class="sch_name"]/a/text()'
    xp2='/html/body/tr[@class="li font14"]['+str(i)+']/td[@class="sch_name"]/a/@href'
    xp3='/html/body/tr[@class="li font14"]['+str(i)+']/td[4]/text()'
    museumName=museumTree.xpath(xp)
    museumMessageUrl=museumTree.xpath(xp2)
    museumLocation=museumTree.xpath(xp3)
    museumDict = museumDict + '"' + str(museumName[0]) + '"' + ':' + '"' + str(101+i) + '"'
    museumMessageUrlDict = museumMessageUrlDict + '"' + str(101+i) + '"' + ':' + '"' + str(museumMessageUrl[0]) + '" '
    museumLocationDict = museumLocationDict + '"' + str(101 + i) + '"' + ':' + '"' + str(museumLocation[0]) + '" '
    if i!=31:
        museumDict+=','
        museumMessageUrlDict+=','
        museumLocationDict+=','


museumDict+='}'
museumMessageUrlDict+='}'
museumDict=json.loads(museumDict)
museumMessageUrlDict=json.loads(museumMessageUrlDict)
#博物馆图片，打开excel文件
filename='museum.xls'
rb=xlrd.open_workbook(filename=filename,formatting_info=True)
wb=copy(rb)
ws=wb.get_sheet(0)
file='./museumPhoto/'
for i in range(2,132):
    sleep(2)
    museumMessageHtml = requests.get(url=museumMessageUrlDict[str(i)], headers=headers, timeout=100).text
    tree=etree.HTML(museumMessageHtml)
    photoXp='/html/body//span[@class="showauthor"]//img/@src'
    res=tree.xpath(photoXp)
    if res:
        name=''
        for k,v in museumDict.items():
            if v==str(i):
                name=k
                break
#输出爬取的图片名称
        print(name+'.jpg')
        ws.write(i - 2 + 1, 7, res[0])
#写入excel
#博物馆名字
ws.write(0,0,'name')
ws.write(0,1,'introduction')
ws.write(0,2,'opentime')
ws.write(0,3,'exhibition')
ws.write(0,4,'activity')
ws.write(0,5,'reseatch')
ws.write(0,6,'collection')
ws.write(0,7,'photosrc')
for i in range(0,130):
    museum=''
    for key,val in museumDict.items():
        if val==str(i+2):
            museum=key
            break
 # 输出博物馆名称进度
    print('name'+str(i+1))
    ws.write(i+1,0,museum)



#博物馆的简介
for i in range(2,132):#132
    sleep(2)
    museumMessageHtml=requests.get(url=museumMessageUrlDict[str(i)],headers=headers,timeout=100).text
    museumMessageXp=etree.HTML(museumMessageHtml)
    introduceXp='/html/body//div[@class="cont c666 font16"]/text()'
    introduce=museumMessageXp.xpath(introduceXp)
    for key, val in museumDict.items():
        if val == str(i):
            ws.write(i-2+1, 1, introduce[0])
# 输出博物馆介绍进度
            print('introduction' + str(i - 1))
            break

#定义博物馆
m = [0] * 150
m[1] = museumClass.Museum_1()
m[2] = museumClass.Museum_2()
m[3] = museumClass.Museum_3()
m[4] = museumClass.Museum_4()
m[5] = museumClass.Museum_5()
m[6] = museumClass.Museum_6()
m[7] = museumClass.Museum_7()
m[8] = museumClass.Museum_8()
m[9] = museumClass.Museum_9()
m[10] = museumClass.Museum_10()
m[11] = museumClass.Museum_11()
m[12] = museumClass.Museum_12()
m[13] = museumClass.Museum_13()
m[14] = museumClass.Museum_14()
m[15] = museumClass.Museum_15()
m[16] = museumClass.Museum_16()
m[17] = museumClass.Museum_17()
m[18] = museumClass.Museum_18()
m[19] = museumClass.Museum_19()
m[20] = museumClass.Museum_20()
m[21] = museumClass.Museum_21()
m[22] = museumClass.Museum_22()
m[23] = museumClass.Museum_23()
m[24] = museumClass.Museum_24()
m[25] = museumClass.Museum_25()
m[26] = museumClass.Museum_26()
m[27] = museumClass.Museum_27()
m[28] = museumClass.Museum_28()
m[29] = museumClass.Museum_29()
m[30] = museumClass.Museum_30()
m[31] = museumClass.Museum_31()
m[32] = museumClass.Museum_32()
m[33] = museumClass.Museum_33()
m[34] = museumClass.Museum_34()
m[35] = museumClass.Museum_35()
m[36] = museumClass.Museum_36()
m[37] = museumClass.Museum_37()
m[38] = museumClass.Museum_38()
m[39] = museumClass.Museum_39()
m[40] = museumClass.Museum_40()
m[41] = museumClass.Museum_41()
m[42] = museumClass.Museum_42()
m[43] = museumClass.Museum_43()
m[44] = museumClass.Museum_44()
m[45] = museumClass.Museum_45()
m[46] = museumClass.Museum_46()
m[47] = museumClass.Museum_47()
m[48] = museumClass.Museum_48()
m[49] = museumClass.Museum_49()
m[50] = museumClass.Museum_50()
m[51] = museumClass.Museum_51()
m[52] = museumClass.Museum_52()
m[53] = museumClass.Museum_53()
m[54] = museumClass.Museum_54()
m[55] = museumClass.Museum_55()
m[56] = museumClass.Museum_56()
m[57] = museumClass.Museum_57()
m[58] = museumClass.Museum_58()
m[59] = museumClass.Museum_59()
m[60] = museumClass.Museum_60()
m[61] = museumClass.Museum_61()
sleep(2)
m[62] = museumClass.Museum_62()
m[63] = museumClass.Museum_63()
m[64] = museumClass.Museum_64()
m[65] = museumClass.Museum_65()
m[66] = museumClass.Museum_66()
m[67] = museumClass.Museum_67()
m[68] = museumClass.Museum_68()
m[69] = museumClass.Museum_69()
m[70] = museumClass.Museum_70()
m[71] = museumClass.Museum_71()

m[72] = museumClass.Museum_72()
m[73] = museumClass.Museum_73()
m[74] = museumClass.Museum_74()
m[75] = museumClass.Museum_75()
m[76] = museumClass.Museum_76()
m[77] = museumClass.Museum_77()
m[78] = museumClass.Museum_78()
m[79] = museumClass.Museum_79()
m[80] = museumClass.Museum_80()
m[81] = museumClass.Museum_81()
m[82] = museumClass.Museum_82()
m[83] = museumClass.Museum_83()
m[84] = museumClass.Museum_84()
m[85] = museumClass.Museum_85()
m[86] = museumClass.Museum_86()
m[87] = museumClass.Museum_87()
m[88] = museumClass.Museum_88()
m[89] = museumClass.Museum_89()
m[90] = museumClass.Museum_90()
m[91] = museumClass.Museum_91()
m[92] = museumClass.Museum_92()
m[93] = museumClass.Museum_93()
m[94] = museumClass.Museum_94()
m[95] = museumClass.Museum_95()
m[96] = museumClass.Museum_96()
m[97] = museumClass.Museum_97()
m[98] = museumClass.Museum_98()
m[99] = museumClass.Museum_99()
m[100] = museumClass.Museum_100()
m[101] = museumClass.Museum_101()
m[102] = museumClass.Museum_102()
m[103] = museumClass.Museum_103()
sleep(3)
m[104] = museumClass.Museum_104()
m[105] = museumClass.Museum_105()
m[106] = museumClass.Museum_106()
m[107] = museumClass.Museum_107()
m[108] = museumClass.Museum_108()
m[109] = museumClass.Museum_109()
m[110] = museumClass.Museum_110()
m[111] = museumClass.Museum_111()
m[112] = museumClass.Museum_112()
m[113] = museumClass.Museum_113()
m[114] = museumClass.Museum_114()
m[115] = museumClass.Museum_115()
m[116] = museumClass.Museum_116()
m[117] = museumClass.Museum_117()
m[118] = museumClass.Museum_118()
m[119] = museumClass.Museum_119()
m[120] = museumClass.Museum_120()
m[121] = museumClass.Museum_121()
m[122] = museumClass.Museum_122()
m[123] = museumClass.Museum_123()
m[124] = museumClass.Museum_124()
m[125] = museumClass.Museum_125()
m[126] = museumClass.Museum_126()
m[127] = museumClass.Museum_127()
m[128] = museumClass.Museum_128()
m[129] = museumClass.Museum_129()
m[130] = museumClass.Museum_130()

for i in range(1,131):
    time=m[i].getTime()
    exhibition=m[i].getExhibition()
    activity=m[i].getActivity()
    research=m[i].getResearch()
    collection=m[i].getCollection()
    t=transform(time)
    e=transform(exhibition)
    a=transform(activity)
    r=transform(research)
    c=transform(collection)
    ws.write(i , 2, t)
    ws.write(i , 3, e)
    ws.write(i , 4, a)
    ws.write(i , 5, r)
    ws.write(i , 6, c)
#输出爬取的其他信息的进度
    print('other'+str(i))
wb.save(filename)