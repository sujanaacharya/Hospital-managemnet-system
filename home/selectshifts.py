
import mysql.connector 
conn=mysql.connector.connect ( user='root',password='admin',database='hospital')
mycur=conn.cursor()


def viewshiftt():
    mycur.execute ("select * from shift")
    shifts=mycur.fetchall()
    return shifts