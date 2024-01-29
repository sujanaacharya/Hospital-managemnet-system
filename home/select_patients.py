
import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()


def selectpatients():
    mycur.execute ("select * from patientinfo")
    a=mycur.fetchall()
    return a
    

def getinfo(m):
    commd1="Select * from patientinfo where pid = '{}'  ".format(m)
    mycur.execute(commd1)
    val=mycur.fetchall()
    return val