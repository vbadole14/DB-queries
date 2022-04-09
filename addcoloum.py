import pymysql

con=pymysql.connect(host='bt0kz5bt38jzlrerkqcm-mysql.services.clever-cloud.com',user='uuyfy9htzjgldeoz',password='H0TJKbZhz2xHdPC8nbBG',database='bt0kz5bt38jzlrerkqcm')
curs=con.cursor()
curs.execute("ALTER TABLE MOBILES ADD purpose varchar(50) AFTER price ")
data=curs.fetchall()

print("coloum added")

con.close()
