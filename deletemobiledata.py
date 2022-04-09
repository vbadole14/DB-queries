
import pymysql

con=pymysql.connect(host='bt0kz5bt38jzlrerkqcm-mysql.services.clever-cloud.com',user='uuyfy9htzjgldeoz',password='H0TJKbZhz2xHdPC8nbBG',database='bt0kz5bt38jzlrerkqcm')
curs=con.cursor()


prodnm=int(input('Enter prod_id number : '))
curs.execute("select * from MOBILES where prod_id=%d " %prodnm)
data=curs.fetchone()
print(data)

if data  :
   
    curs.execute("delete from MOBILES where prod_id=%d " %prodnm)
    con.commit()
    print(' deleted successfully')
else:
    print('mobile does not exist')

con.close()