# import boto3
# from bs4 import BeautifulSoup
# date = '2019-01-31'
# id = '270683'
# s3 = boto3.resource('s3')
# object_e = s3.Object('animecrawling', date + '/' + id + '.txt')
# soup_e = BeautifulSoup(object_e.get()['Body'], "lxml")
#
# print( soup_e.find('img', itemprop='image').get('src'))

from bostondate import bostondate
print(bostondate())
