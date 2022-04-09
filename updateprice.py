import pymysql

con=pymysql.connect(host='bt0kz5bt38jzlrerkqcm-mysql.services.clever-cloud.com',user='uuyfy9htzjgldeoz',password='H0TJKbZhz2xHdPC8nbBG',database='bt0kz5bt38jzlrerkqcm')
curs=con.cursor()


prodnm=int(input('Enter prod_id number : '))
curs.execute("select * from MOBILES where prod_id=%d " %prodnm)
data=curs.fetchone()

if data:
    prce=float(input('Enter price : '))
    curs.execute("update MOBILES set price='%f' where prod_id=%d" %(prce,prodnm))
    con.commit()
    print('price data updated')
else:
    print('mobile not found')
con.close()