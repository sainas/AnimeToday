import psycopg2
import jinja2
import boto3
from botocore.exceptions import ClientError

from bostondate import bostondate


def get_array(date):
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print('connect to PostgreSQL success')
    cur = conn.cursor()
    cur.execute('''
        create temporary view etoday as select * from episode where e_epdate = '{}' ;
        create temporary view etoday2 as select e_aid, e_epid, e_epfulltitle, e_epurl,f_username from etoday inner join following on e_aid = f_aid;
        create temporary view etoday3 as select * from etoday2 left join anime on a_aid = e_aid;
        create temporary view etoday5 as select f_username , array_agg(array[a_atitle,a_aimg, e_epfulltitle,e_epurl]) from etoday3 group by f_username ;
        select u_username, u_useremail, array_agg  from etoday5 left join userinfo on u_username = f_username order by f_username;
              ;'''.format(date))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def make_it_html(line):
    templateLoader = jinja2.FileSystemLoader(searchpath="/home/ubuntu/AnimeToday/src/templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "email_template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    body_html = template.render(username=line[0], record=line[2])
    return body_html


def make_it_text(line):
    content = ['Hi {}! You have new episode(s):\r\n'.format(line[0])]
    for each in line[2]:
        content.append(each[2] + '\r\n' + 'https://www.crunchyroll.com' + each[3])
    body_text = '\r\n'.join(content)

    return body_text


def sent_one_email(client, body_text, body_html ,emailaddress):

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "AnimeToday <animetodayservice@gmail.com>"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = emailaddress

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # The subject line for the email.
    SUBJECT = "Your New Episodes Today!"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = body_text

    BODY_HTML = body_html

    # The character encoding for the email.
    CHARSET = "UTF-8"

    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def sent_one_sms(client,content, number):
    try:
        response = client.publish(Message=content, PhoneNumber=number)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


if __name__ == '__main__':
    # date = '2019-02-01'
    date = bostondate()
    rows = get_array(date)
    if rows:
        client_ses = boto3.client("ses")
        print('Connect to AWS SNS: success!')
        client_sns = boto3.client("sns")
        print('Connect to AWS SNS: success!')
        num = min(len(rows), 1)
        for line in rows[:num]:
            body_html = make_it_html(line)
            body_text = make_it_text(line)
            sent_one_email(client_ses, body_text, body_html, "animetodayuser@gmail.com")
            sent_one_sms(client_sns, body_text, "+18584058857")









