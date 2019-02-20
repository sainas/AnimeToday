from bs4 import BeautifulSoup
import boto3
import time

s3 = boto3.resource('s3')
date = time.strftime("%Y-%m-%d", time.localtime())
# object = s3.Object('animecrawling', date + '/all_anime.txt')
object = s3.Object('animecrawling', '2019-01-31/all_anime.txt')
bf = BeautifulSoup(object.get()['Body'], "lxml")
li = bf.find_all('li', itemtype='http://schema.org/TVSeries')

print(len(li))
# for each in li[:15]:
#     a_bf = BeautifulSoup(str(each), "lxml")
#     a = a_bf.find('a')
#     print(each.get('group_id'), a.get('title'))

