import pymysql

try:
    no=int(input('Enter productid  : '))
    modelnm=input('Enter model name : ')
    cmpnm=input('Enter company name : ')
    conty=input('Enter connectivity : ')
    ram=input('Enter ram : ')
    rom=input('Enter rom : ')
    clr=input('Enter colour : ')
    scrn=input('Enter screen : ')
    btry=int(input('Enter battary(mAh) : '))
    prosnm=input('Enter processor name : ')
    price=float(input('Enter price  : '))
    rating=float(input('Enter rating out of 5 : '))
    

    con=pymysql.connect(host='bt0kz5bt38jzlrerkqcm-mysql.services.clever-cloud.com',user='uuyfy9htzjgldeoz',password='H0TJKbZhz2xHdPC8nbBG',database='bt0kz5bt38jzlrerkqcm')
    curs=con.cursor()

    
    curs.execute("insert into MOBILES values(%d,'%s','%s','%s','%s','%s','%s','%s','%d','%s','%.2f','%.2f')" %(no,modelnm,cmpnm,conty,ram,rom,clr,scrn,btry,prosnm,price,rating))
    con.commit()
    print('mobile data stored in the cloud')
    con.close()
except Exception as e:
        print('this data cant be inserted - ',e)

    

