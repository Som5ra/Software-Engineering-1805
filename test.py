import json
from time import sleep
import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#实现无可视化界面
from selenium.webdriver import ChromeOptions#实现规避操作
import xlrd
from xlutils.copy import copy
def transform(t):
    if type(t).__name__=='list':
        str=''
        for l in t:
            if l!=None:
                str+=l
        return str
    else :
        return t
def insert():
    filename = 'museum.xls'
    rb = xlrd.open_workbook(filename=filename, formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)