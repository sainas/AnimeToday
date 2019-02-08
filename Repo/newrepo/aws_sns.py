import boto3
import psycopg2
import time


def send_message( message="Test", topic_name="animetoday"):
    # Create an SNS client
    client = boto3.client('sns')
    print('connected')
    # message = {"foo": "bar"}
    # client = boto3.client('sns')
    # response = client.publish(
    #     TargetArn=arn,
    #     Message=json.dumps({'default': json.dumps(message)}),
    #     MessageStructure='json'
    # )
    # Publish a message
    client.publish(Message=message, TopicArn='arn:aws:sns:us-east-1:153770056708:animetoday')

conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print("Opened database successfully")
cur = conn.cursor()
insert_data = "SELECT episode.pub_date,  episode.full_title, episode.ep_title2, episode.ep_url\
 FROM following, episode \
where episode.a_id = following.a_id and episode.pub_date in ('2019-02-02', '2019-02-01', '2019-02-03') and following.username = 'bikoc' ;"
insert_data = "SELECT episode.pub_date,  episode.full_title, episode.ep_title2, episode.ep_url\
 FROM  episode \
where episode.pub_date in ('2019-02-02', '2019-02-01', '2019-02-03')  ;"

try:
    cur = conn.cursor()
    print('1')
    cur.execute("SELECT  episode.pub_date,  episode.full_title, episode.ep_title2, episode.ep_url\
  FROM following, episode \
where episode.a_id = following.a_id and  episode.pub_date in ('2019-02-02', '2019-02-01', '2019-02-03') \
 and  following.username = 'bikoc' ;")
    print('2')
    # time.sleep(20)
    print('2')
    rows = cur.fetchall()
    print("Records created successfully")
except Exception as e:
    print('insert record into table failed')
    print(e)
        # rows = cur.fetchmany(6)

print('success')
cur.close()
conn.close()

message = rows
for each in rows:
    print(each)
# send_message(message)
# def main(args):
#     sms_list = args.number
#     message = " ".join(args.message)
#     send_message(sms_list=sms_list, message=message)
#
#
# if "__main__" == __name__:
#     parser = argparse.ArgumentParser()
#     parser.add_argument('message', type=str, nargs='+', default="测试消息", help="短信内容")
#     parser.add_argument('--number', '-n', type=str, nargs='+', help="接收号码")
#     args = parser.parse_args()
#
#     main(args)
#
#     import boto3
#
#     message = {"foo": "bar"}
#     client = boto3.client('sns')
#     response = client.publish(
#         TargetArn=arn,
#         Message=json.dumps({'default': json.dumps(message)}),
#         MessageStructure='json'
#     )