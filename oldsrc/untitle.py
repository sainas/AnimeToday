import psycopg2
import boto3
# from bs4 import BeautifulSoup
# date = '2019-01-31'
# id = '270683'
# s3 = boto3.resource('s3')
# object_e = s3.Object('animecrawling', date + '/' + id + '.txt')
# soup_e = BeautifulSoup(object_e.get()['Body'], "lxml")
#
# print( soup_e.find('img', itemprop='image').get('src'))

# from bostondate import bostondate
# print(bostondate())

# client = boto3.client("sns")
#
# # Send your sms message.
# client.publish(Message='anime', PhoneNumber='+18584058857')
# -*- coding:UTF-8 -*-
import psycopg2
import boto3
from bs4 import BeautifulSoup
from bostondate import bostondate

def update_anime(date):
    s3 = boto3.resource('s3')
    object = s3.Object('animecrawling', date + '/all_anime.txt')
    soup = BeautifulSoup(object.get()['Body'], "lxml")
    li = soup.find_all('li', itemtype='http://schema.org/TVSeries')

    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print("Opened database successfully")

    for each in li:
        a_bf = BeautifulSoup(str(each), "lxml")
        a = a_bf.find('a')
        # print(each.get('group_id'), a.get('title'))
        # print(each.get('group_id'), a.get('title'), self.server + a.get('href'))

        # finally:
        #     if cur:
        #         cur.close()

        # object_e = s3.Object('animecrawling', date + '/' + each.get('group_id') + '.txt')
        # soup_e = BeautifulSoup(object.get()['Body'], "lxml")
        # a1 = soup_e.find_all('a', "portrait-element block-link titlefix episode")
        # if a1.get('href') != str(row[2]):
        #     for string in a1.stripped_strings:
        #         info = str(string)
        #         break
        #     update_data = "UPDATE ANIMENAME\
        #                        SET lastupdated = %s, \
        #                              epinfo = %s,\
        #                               epurl = %s\
        #                        WHERE groupid = %s;"
        #
        #     data = (date, info, a1.get('href'), row[0])
        #     # try:
        #     cur = conn.cursor()
        #     cur.execute(update_data, data)
        #     # cur.execute("INSERT INTO ANIMENAME (GROUPID,NAME,URL) \
        #     #       VALUES ([" + each.get('group_id') + "],[" +  a.get('title') + "],[" + self.server + a.get('href') +"])");
        #
    conn.commit()
    conn.close()

    return li


# date = bostondate()
# for i in range(8):
#     list = ['05','06','07','08','09','10','11','12']
#     date = '2019-02-'+list[i]
#     print(date)
#     update_anime(date)

li = update_anime('2019-02-09')

conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
cur = conn.cursor()
cur.execute("""
            SELECT a_aid
            FROM anime
            ORDER BY a_atitle
        """)
        # rows = cur.fetchmany(6)
rows = cur.fetchall()
print('success')
cur.close()


list1 = []
list2=[]
i = 0
for each in li:
    list1.append(each.get('group_id'))
for each in rows:
    list2.append(str(each[0]))

print(len(li))
print(len(rows))
print(list1, list2)
retD = list(set(list2).difference(set(list1)))
print("retD is: ",retD)
list1.sort()
list2.sort()
print(list1, list2)

