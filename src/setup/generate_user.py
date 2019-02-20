# -*- coding:UTF-8 -*-
# https://gist.github.com/noxan/5845351

import random
import string
import psycopg2




def generate_word(length):
    VOWELS = "aeiou"
    CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word


def add_user_to_psql(namelist):
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print("Opened database successfully")
    for i in range(len(namelist)):
        insert_data = '''INSERT INTO userinfo (username) 
                                 VALUES (%s) 
                                 ON CONFLICT (username) DO NOTHING;  '''

        data = (str(namelist[i]),)
        # print(date, fulltitle)
        try:
            cur = conn.cursor()
            cur.execute(insert_data, data)
            conn.commit()
            print("Records created successfully")
        except Exception as e:
            print('insert record into table failed')
            print(e)
        finally:
            if cur:
                cur.close()

    conn.close()

    print('finish')


def user_interests_to_psql(namelist, animelist, animenum):
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print("Opened database successfully")
    for i in range(len(namelist)):
        for j in range(animenum):
            animeid = random.choice(animelist)
            insert_data = '''INSERT INTO following (username, a_id) 
                                     VALUES (%s, %s) 
                                     ON CONFLICT  DO NOTHING;  '''

            data = (str(namelist[i]), animeid)
            # print(date, fulltitle)
            try:
                cur = conn.cursor()
                cur.execute(insert_data, data)
                conn.commit()
                print("Records created successfully")
            except Exception as e:
                print('insert record into table failed')
                print(e)
            finally:
                if cur:
                    cur.close()
    conn.close()

    print('finish')


if __name__ == "__main__":
    count = 49
    length = 5
    namelist = []
    for i in range(count):
        namelist.append(generate_word(length))
    print(namelist)
    add_user_to_psql(namelist)

    # Recently released animes, more possible to have new episodes
    animelist_new = [246948,
                     257631,
                     260407,
                     260449,
                     260609,
                     269785,
                     270397,
                     270659,
                     270663,
                     271215,
                     271995,
                     275937,
                     275981,
                     276275,
                     277069,
                     277072,
                     277307,
                     277352,
                     277354,
                     277357,
                     277381,
                     277385,
                     277389,
                     277390,
                     277391,
                     277501,
                     277506,
                     277508,
                     277510,
                     277515, ]
    # Random old animes, less possible to have new episodes
    animelist_old = [169063,
                     246682,
                     271459,
                     273767,
                     245920,
                     265955,
                     244046,
                     81816,
                     192193,
                     260547,
                     271461,
                     271321,
                     42850,
                     258887,
                     271441,
                     189368,
                     240610,
                     258755,
                     269065,
                     273805,
                     62522,
                     81875,
                     269419,
                     261601,
                     272983,
                     257179,
                     272207,
                     258917,
                     234107,
                     257295,
                     241846,
                     271463,
                     273655,
                     270669,
                     277208,
                     42852,
                     271453,
                     260311,
                     241436]
    user_interests_to_psql(namelist, animelist_new, 5)
    user_interests_to_psql(namelist, animelist_old, 2)
