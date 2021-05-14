from snownlp import SnowNLP
from snownlp import sentiment
import pandas as pd

'''
sentiments < .5 被认为是negetive
否则被认为是postive
'''

def WriteToExcel(contents):
    col = ['新闻好坏']
    csv = pd.DataFrame(columns = col, data = contents)
    csv.to_csv('baidu_news_classification.csv')

if __name__ == '__main__':
    data = pd.read_csv('baidu_news.csv')
    texts = list(data['简介内容'])
    CLASS = []
    for text in texts:
        s = SnowNLP(text)
        if s.sentiments < 0.5:
            CLASS.append('Negetive')
        else:
            CLASS.append('Postive')
    WriteToExcel(CLASS)