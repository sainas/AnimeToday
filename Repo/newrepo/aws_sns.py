import boto3


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
    #
    # Publish a message
    client.publish(Message=message, TopicArn='arn:aws:sns:us-east-1:153770056708:animetoday')

send_message()
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