
import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()


def selectdoctors():
    mycur.execute ("select * from docinfo")
    doct=mycur.fetchall()
    return doct