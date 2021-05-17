from LLBOT.studentmodel import LLBOTdb
import random

db = LLBOTdb.LLBOTdb()
conn = db.get_connection()
cursor = conn.cursor()


def check(keyword):
    sori=["S","I"]
    pick= random.choice(sori)
    

    sql = "SELECT FoS FROM fosbank where keyword=%s and s_i=%s"
    cursor.execute(sql,[keyword,pick])
    res = cursor.fetchall()
    res=[i[0] for i in res]
    
    if len(res)==0:
        return 0,0
    elif len(res)>0:
        return str(res[0]), pick
    
