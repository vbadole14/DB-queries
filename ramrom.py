import pymysql

con=pymysql.connect(host='bt0kz5bt38jzlrerkqcm-mysql.services.clever-cloud.com',user='uuyfy9htzjgldeoz',password='H0TJKbZhz2xHdPC8nbBG',database='bt0kz5bt38jzlrerkqcm')
curs=con.cursor()

ram=input('Enter ram number : ')
rom=input('Enter rom number : ')
curs.execute("select * from MOBILES where ram=%s and rom=%s" %(ram,rom))
data=curs.fetchall()
print(data)

con.close()