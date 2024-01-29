
import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()


def funct1(a,b,c,d,e,f,g):
  
    r="insert into patientinfo(pfname,plname,psex,paage,paddress, pemail, pphn) values (%s,%s,%s,%s,%s,%s,%s)"
    s=(a,b,c,d,e,f,g)
    mycur.execute(r,s)
    conn.commit()
