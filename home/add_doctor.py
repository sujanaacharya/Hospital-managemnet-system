import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()

def funct2(a,b,c,d,e,f,g,h,i,j):
    print('aa')
    r="insert into docinfo(did,dfname,dlname,dsex,dexp,depname,daddress,dqual, dphn,demail) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    s=(a,b,c,d,e,f,g,h,i,j)
    mycur.execute(r,s)
    conn.commit()
    print('aasasdfg')
  

   