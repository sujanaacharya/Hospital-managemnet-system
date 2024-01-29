
import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()


def removepat(id,lname):
    remitem="DELETE FROM patientinfo where pid=%s and plname=%s"
    a=(id,lname)
    mycur.execute(remitem,a)
    conn.commit()

        
