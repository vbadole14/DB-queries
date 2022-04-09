import pymysql

con=pymysql.connect(host='bt0kz5bt38jzlrerkqcm-mysql.services.clever-cloud.com',user='uuyfy9htzjgldeoz',password='H0TJKbZhz2xHdPC8nbBG',database='bt0kz5bt38jzlrerkqcm')
curs=con.cursor()


curs.execute("select * from MOBILES  where company like samsung order by price")
data=curs.fetchall()


try:
    print(data)
except:
    print('mobile does not exist')

con.close()
