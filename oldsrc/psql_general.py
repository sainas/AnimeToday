def get_pic_null():
    conn = None
    try:
        conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
        cur = conn.cursor()
        cur.execute("""
            SELECT a_aid, a_aurl
            FROM anime
            WHERE a_aimg IS NULL;
        """)
        # rows = cur.fetchmany(6)
        rows = cur.fetchall()
        print('success')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows



