import mysql.connector
import json
# import base64
def insertregister(fullname, email, password, phone):
    #same email and pass
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    k = 1
    sql = ("insert into users(fullname, email, password, phone, image, dateofbirth, sex, city, township, ward, apartmentnumber, money, accumulatedpoints, rolekey, setlock, addcard) "
           + "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    image = None
    dateofbirth = None
    sex = None
    city = None
    township = None
    ward = None
    apartmentnumber = None
    money = 0.00
    accumulatedpoints = 0
    rolekey = 2
    setlock = "0"
    addcard = "0"
    val = (fullname, email, password, phone, image, dateofbirth, sex, city, township, ward, apartmentnumber, money, accumulatedpoints , rolekey, setlock, addcard)
    try:
        cur.execute(sql, val)
        myconn.commit()
        myconn.close()
    except:
        k = 0
        myconn.rollback()
        myconn.close()
    return k

def adminregister(fullname, email, password, phone):
    #same email and pass
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    k = 1
    sql = ("insert into users(fullname, email, password, phone, image, dateofbirth, sex, city, township, ward, apartmentnumber, money, accumulatedpoints, rolekey, setlock, addcard) "
           + "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    image = None
    dateofbirth = None
    sex = None
    city = None
    township = None
    ward = None
    apartmentnumber = None
    money = 0.00
    accumulatedpoints = 0
    rolekey = 3
    setlock = "0"
    addcard = "0"
    val = (fullname, email, password, phone, image, dateofbirth, sex, city, township, ward, apartmentnumber, money, accumulatedpoints , rolekey, setlock, addcard)
    try:
        cur.execute(sql, val)
        myconn.commit()
        myconn.close()
    except:
        k = 0
        myconn.rollback()
        myconn.close()
    return k

def login(email, password):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT * FROM users WHERE email = '{email}'")
    #fullname, email, password, phone, image, dateofbirth, sex, city, township, ward, apartmentnumber, money, accumulatedpoints
    id = 0
    for i in cur:
        id = i[0]
        if i[15]==2:


            dictionary = {
                "fullname": i[1],
                "email": i[2],
                "password": i[3],
                "phone": i[4],
                "image": i[5],
                "dateofbirth": i[6],
                "sex": i[7],
                "city": i[8],
                "township": i[9],
                "ward": i[10],
                "apartmentnumber": i[11],
                "money": i[12],
                "accumulatedpoints": i[13],
                "carepayactive": i[14],
                "role": str(i[15]),
                "setlock": str(i[16]),
                "addcard": str(i[17])
            }
            print(dictionary)



            # Serializing json
            json_object = json.dumps(dictionary, indent=15)
            if email == i[2] and password == i[3]:
                return json_object
            else:
                return "0"

        elif i[15]==1:
            #cur = myconn.cursor()
            cur.execute(f"SELECT * FROM infordoctor WHERE infordoctorKey  = '{id}'")

            for i1 in cur:
                infordoctorchungchi = i1[1]
                infordoctoristrk = i1[2]
                infordoctorist = i1[3]
                infordoctorhospital = i1[4]
                infordoctorspec = i1[5]
                infordoctoriscall = i1[7]
                dictionary = {
                    "fullname": i[1],
                    "email": i[2],
                    "password": i[3],
                    "phone": i[4],
                    "image": i[5],
                    "dateofbirth": i[6],
                    "sex": i[7],
                    "city": i[8],
                    "township": i[9],
                    "ward": i[10],
                    "apartmentnumber": i[11],
                    "money": i[12],
                    "accumulatedpoints": i[13],
                    "carepayactive": i[14],
                    "role": str(i[15]),
                    "setlock": str(i[16]),
                    "addcard": str(i[17]),
                    "infordoctorchungchi": infordoctorchungchi,
                    "infordoctoristrk": str(infordoctoristrk),
                    "infordoctorist": str(infordoctorist),
                    "infordoctorhospital": infordoctorhospital,
                    "infordoctorspec": infordoctorspec,
                    "infordoctoriscall": infordoctoriscall
                }

                # Serializing json
                json_object = json.dumps(dictionary, indent=21)
                if email == i[2] and password == i[3]:
                    return json_object
                else:
                    return "0"

    return "0"



def adminlogin(email, password):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT * FROM users WHERE email = '{email}' and rolekey = '3'")
    #fullname, email, password, phone, image, dateofbirth, sex, city, township, ward, apartmentnumber, money, accumulatedpoints
    id = 0
    for i in cur:
        id = i[0]

        dictionary = {
                "fullname": i[1],
                "email": i[2],
                "password": i[3],
                "phone": i[4],
                "image": i[5],
                "dateofbirth": i[6],
                "sex": i[7],
                "city": i[8],
                "township": i[9],
                "ward": i[10],
                "apartmentnumber": i[11],
                "money": i[12],
                "accumulatedpoints": i[13],
                "carepayactive": i[14],
                "role": str(i[15]),
                "setlock": str(i[16]),
                "addcard": str(i[17])
        }



        # Serializing json
        json_object = json.dumps(dictionary, indent=15)
        if email == i[2] and password == i[3]:
            return json_object
        else:
            return "0"
    return "0"


def updateprofile(fullname, email, image, dateofbirth, sex, city, township, ward, apartmentnumber):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    k = image
    try:
        sql = """
            UPDATE users
            SET fullname=%s, image=%s, dateofbirth=%s, sex=%s, city=%s, township=%s, ward=%s, apartmentnumber=%s
            WHERE email=%s
        """
        val =(fullname, image, dateofbirth, sex, city, township, ward, apartmentnumber, email)

        cur.execute(sql, val)

        myconn.commit()
        myconn.close()


    except:
        myconn.rollback()
        myconn.close()
        k = "0"
    return k

def updatemoney(email, money, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    k = "1"
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0]
        moneynew = moneyold + money
        idu = i[1]
        cur.execute(f"SELECT cardKey FROM usercard WHERE userKey = '{idu}'")
        myresult = cur.fetchall()
        for i in myresult:
            cardid = i[0]
            cmoney = ""
            cur.execute(f"SELECT cardMoney FROM card WHERE cardID = '{cardid}'")
            myresult = cur.fetchall()
            for i in myresult:
                cmoney = i[0]

            cmoneynew = float(cmoney) - money
            if cmoneynew < 0:
                return "error"

            try:
                sql = """
                UPDATE card
                SET cardMoney=%s
                WHERE cardID=%s
                """
                val = (cmoneynew, cardid)
                cur.execute(sql, val)
                myconn.commit()
            except:
                myconn.rollback()
                myconn.close()
                return "error"


        try:
            sql = """
            UPDATE users
            SET money=%s
            WHERE email=%s
            """
            val =(moneynew, email)

            cur.execute(sql, val)
            myconn.commit()
            toHistory(email, money, date, time)
        except:
            myconn.rollback()
            myconn.close()
            return "error"


    return str(moneynew)


def toHistory(email, money, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0] - money
        id = i[1]
        moneynew = moneyold + money
        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("0" , "Deposit money from bank account", time, date, str(i[0]) , str(money), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"

def updatepoint(email, money, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money,accumulatedpoints FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0]
        pointold = i[1]
        moneynew = moneyold - money
        point = money * 100
        pointnew = pointold + point
        if moneynew<0:
            return "fail"


        try:
            sql = """
            UPDATE users
            SET accumulatedpoints=%s, money=%s
            WHERE email=%s
            """
            val =(pointnew,moneynew , email)

            cur.execute(sql, val)

            myconn.commit()
            toHistoryP(email, money, date, time)


        except:
            myconn.rollback()
            myconn.close()

            return "error"

    dictionary = {
        "money": moneynew,
        "accumulatedpoints": pointnew
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=2)
    return json_object

def toHistoryP(email, money, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[1]
        remind = "Redeem "+ str(money*10) +" bonus points"

        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("1" , remind, time, date, str(i[0]) , str(money), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"


def profilerelative(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    List = ""
    for i in cur:
        id = i[0]
        cur.execute(f"SELECT relative, fullname, relativedateofbirth, relativephone, relativecity, relativedistrict, relativeward, 	relativeaddress  FROM relativeprofile WHERE idkey = '{id}'")
        for i in cur:
            relative = i[0]
            fullname = i[1]
            relativedateofbirth = i[2]
            relativephone = i[3]
            relativecity = i[4]
            relativedistrict = i[5]
            relativeward = i[6]
            relativeaddress = i[7]



            dictionary = {
            "relative" : relative,
            "fullname" : fullname,
            "relativedateofbirth" : relativedateofbirth,
            "relativephone" : relativephone,
            "relativecity" : relativecity,
            "relativedistrict" : relativedistrict,
            "relativeward" : relativeward,
            "relativeaddress" : relativeaddress
            }
            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]


def profilerelativedetail(phone):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT * FROM relativeprofile WHERE relativephone = '{phone}'")
    List = ""
    for i in cur:

        relative = i[1]
        fullname = i[2]
        relativedateofbirth = i[3]
        relativedateofgender = i[4]
        relativephone = i[5]
        relativecity = i[6]
        relativedistrict = i[7]
        relativeward = i[8]
        relativeaddress = i[9]



        dictionary = {
            "relative" : relative,
            "fullname" : fullname,
            "relativedateofbirth" : relativedateofbirth,
            "relativedateofgender": relativedateofgender,
            "relativephone" : relativephone,
            "relativecity" : relativecity,
            "relativedistrict" : relativedistrict,
            "relativeward" : relativeward,
            "relativeaddress" : relativeaddress
            }
        json_object = json.dumps(dictionary, indent=8)
        return json_object




def profilerelativedetailupdate(relative, fullname, phonenew, dataofbirth, gender, city, district,ward, address, phoneold):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    try:
        sql = """
        UPDATE relativeprofile
        SET relative=%s, fullname=%s, relativedateofbirth=%s, relativesex=%s, 
        relativephone=%s, relativecity=%s, relativedistrict=%s, relativeward=%s, relativeaddress=%s
        WHERE relativephone=%s
        """
        val = (relative, fullname, dataofbirth, gender, phonenew, city, district, ward, address, phoneold)
        cur.execute(sql, val)
        myconn.commit()
        myconn.close()


    except:
        myconn.rollback()
        myconn.close()

        return "error"
    return "success"


def profilerelativeadd(relative, fullname, phone, dataofbirth, gender, city, district,ward, address, email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]
        mycursor = myconn.cursor()

        sql = "INSERT INTO relativeprofile (relative, fullname, relativedateofbirth, relativesex, relativephone, relativecity, relativedistrict, relativeward, relativeaddress, idkey) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (relative, fullname, dataofbirth, gender, phone, city, district, ward, address, id)
        try:
            mycursor.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
        return 'success'


def updatemoneydonation(email, money, date, time, f):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    k = "1"
    cur.execute(f"SELECT money,id FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0]
        moneynew = moneyold - money
        idu = i[1]
        if f=="0":
            cur.execute(f"SELECT cardKey FROM usercard WHERE userKey = '{idu}'")
            myresult = cur.fetchall()
            for i in myresult:
                cardid = i[0]
                cmoney = ""
                cur.execute(f"SELECT cardMoney FROM card WHERE cardID = '{cardid}'")
                myresult = cur.fetchall()
                for i in myresult:
                    cmoney = i[0]

                cmoneynew = float(cmoney) + money
                try:
                    sql = """
                            UPDATE card
                            SET cardMoney=%s
                            WHERE cardID=%s
                            """
                    val = (cmoneynew, cardid)
                    cur.execute(sql, val)
                    myconn.commit()
                except:
                    myconn.rollback()
                    myconn.close()
                    return "error"

        if moneynew < 0:
            return "error"

        try:
            sql = """
            UPDATE users
            SET money=%s
            WHERE email=%s
            """
            val =(moneynew, email)
            cur.execute(sql, val)

            myconn.commit()
            if(f=="0"):
                toHistoryW(email, money, date, time)
            else:
                toHistoryDN(email, money, date, time)

            myconn.close()


        except:
            myconn.rollback()
            myconn.close()
            return "error"
    return str(moneynew)

def toHistoryW(email, money, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[1]
        remind = "Withdraw money to wallet"

        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("2" , remind, time, date, str(i[0]) , str(money), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"
def toHistoryDN(email, money, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[1]
        remind = "Supporting children with serious illnesses"

        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("2" , remind, time, date, str(i[0]) , str(money), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"

def updatepointdonation(email, point):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT accumulatedpoints FROM users WHERE email = '{email}'")
    for i in cur:
        pointold = i[0]
        pointnew = pointold - point
        if pointnew < 0:
            return "error"

        try:
            sql = """
            UPDATE users
            SET money=%s
            WHERE email=%s
            """
            val =(pointnew, email)

            cur.execute(sql, val)

            myconn.commit()
            myconn.close()


        except:
            myconn.rollback()
            myconn.close()
            return "error"
    return str(pointnew)

def profileschedule(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    List = ""
    for i in cur:
        id = i[0]
        cur.execute(f"SELECT scheduleremind	, scheduletime, scheduledate FROM schedule WHERE schedulekey = '{id}'")
        for i in cur:
            remind = i[0]
            time = i[1]
            date = i[2]

            gio = time.split(':')[0]
            phut = time.split(':')[1]
            if phut[0] == "0":
                phut = phut[1]
            dictionary = {
            "remind" : remind,
            "time" : time,
            "date" : date,
            "gio": gio,
            "phut": phut,

            }
            json_object = json.dumps(dictionary, indent=3)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]


def profilescheduleadd(email, day, time, remind):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]
        mycursor = myconn.cursor()

        sql = "INSERT INTO schedule (scheduleremind, scheduletime, scheduledate, schedulekey) VALUES (%s, %s, %s, %s)"
        val = (remind, time, day, id)
        try:
            mycursor.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
        return 'success'

def profilescheduledelete(email, position):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    list = []
    for i in cur:
        id = i[0]
    cur = myconn.cursor()
    cur.execute(f"SELECT scheduleID FROM schedule WHERE schedulekey = '{id}'")
    for i in cur:
        list.append(i[0])
    try:
        cur = myconn.cursor()
        cur.execute(f"DELETE FROM schedule WHERE scheduleID = '{list[position]}'")
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'

def profilepasschange(email, passnew):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    try:
        sql = """
        UPDATE users
        SET password=%s
        WHERE email=%s
        """
        val =(passnew, email)

        cur.execute(sql, val)

        myconn.commit()
        myconn.close()


    except:
        myconn.rollback()
        myconn.close()
        return "fail"
    return 'success'

def activecarepay(email, CMDN):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    idu = ""
    # resultcardfront = json.loads(resultcardfront)
    # resultcardback = json.loads(resultcardback)
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]
    sql = "INSERT INTO cmnd (cmndimgfront ,cmndimgback ,userKey, number) VALUES (%s, %s, %s, %s)"
    linkfront = 'cmnd/' + email + "-front" + '.png'
    linkback = 'cmnd/' + email + "-back" + '.png'
    val = (linkfront, linkback, int(idu), CMDN)

    cur.execute(sql, val)
    myconn.commit()


    try:
        sql = """
        UPDATE users
        SET carepayactive=%s
        WHERE email=%s
        """
        val =(1, email)
        cur.execute(sql, val)
        myconn.commit()
        myconn.close()


    except:
        myconn.rollback()
        myconn.close()
        return "fail"
    return 'success'

def takeinftranfer(phone):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    try:
        k = 0
        cur.execute(f"SELECT * FROM users WHERE phone = '{phone}'")

    except:
        return "fail"
    for i in cur:
        k = 1

        dictionary = {
            "fullname": i[1],
            "image": i[5],
        }
        # Serializing json
        json_object = json.dumps(dictionary, indent=2)

        return json_object
    if k == 0:
        return "fail"

def transfer(email, phone, am, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0]
        moneynew = moneyold - am
        if moneynew < 0:
            return "error"

        try:
            sql = """
            UPDATE users
            SET money=%s
            WHERE email=%s
            """
            val =(moneynew, email)

            cur.execute(sql, val)

            myconn.commit()



        except:
            myconn.rollback()
            myconn.close()
            return "fail"

    cur = myconn.cursor()
    cur.execute(f"SELECT money FROM users WHERE phone = '{phone}'")
    for i in cur:
        moneyold = i[0]
        moneynew = moneyold + am


        try:
            sql = """
                    UPDATE users
                    SET money=%s
                    WHERE phone=%s
                    """
            val = (moneynew, phone)

            cur.execute(sql, val)

            myconn.commit()
            toHistoryCare(email, phone, am, date, time)
            myconn.close()


        except:
            myconn.rollback()
            myconn.close()
            return "fail"




    return "success"


def toHistoryCare(email, phone, am, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    nameto = ""

    cur.execute(f"SELECT fullname FROM users WHERE phone = '{phone}'")
    myresult = cur.fetchall()
    for i in myresult:
        nameto = i[0]

    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[1]
        remind = "Transfer money to CarePay (" + phone + ") - " + nameto

        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("2" , remind, time, date, str(i[0]) , str(int(am)), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"
    namedt = ""
    phonedt = ""
    cur.execute(f"SELECT fullname, phone FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        namedt = i[0]
        phonedt = i[1]

    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE phone = '{phone}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[1]
        remind = "Receive money from (" + phonedt + ") - " + namedt

        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("0", remind, time, date, str(i[0]), str(int(am)), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"



def transferbank(email, stk, am, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0]
        moneynew = moneyold - am
        if moneynew < 0:
            return "error"

        try:
            sql = """
            UPDATE users
            SET money=%s
            WHERE email=%s
            """
            val =(moneynew, email)
            cur.execute(sql, val)
            myconn.commit()
            toHistorybank(email, stk, am, date, time)
            myconn.close()
        except:
            myconn.rollback()
            myconn.close()
            return "fail"
    return "success"

def toHistorybank(email, stk, am, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[1]
        remind = "transfer money to account (" + str(stk) +")"

        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("2" , remind, time, date, str(i[0]) , str(int(am)), id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"

def post(email, content, image, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]
        mycursor = myconn.cursor()

        sql = "INSERT INTO news (newText, newNumberLike	,date, time, newImage, id) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (content, 0, date, time, image,   id)
        try:
            mycursor.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
        return 'success'

def news(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    idu = ""
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]

    cur.execute("SELECT newID FROM news")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)


    for ids in ID:
        cur.execute(f"SELECT newText, newNumberLike, date, time, newImage, id FROM news WHERE newID = '{ids}'")
        myresult = cur.fetchall()
        for i in myresult:
            like = "0"
            cur.execute(f"SELECT usernewLike id FROM usernew WHERE newKey = '{ids}' and userKey = '{idu}'")
            myresult = cur.fetchall()
            for i1 in myresult:
                like = i1[0]
            content = i[0]
            numberlike = i[1]
            date = i[2]
            time = i[3]
            image = i[4]
            id = i[5]


            cur.execute(f"SELECT id, fullname, image FROM users WHERE id = '{id}'")

            fullname = ""
            imageface = ""
            for i in cur:
                imageface = i[2]
                fullname = i[1]
                idpeople = i[0]


            idpost = ids
            dictionary = {
                    "content" : content,
                    "numberlike" : numberlike,
                    "date" : date,
                    "time" : time,
                    "image" : image,
                    "imageface" : imageface,
                     "fullname": fullname,
                     "idpeople": idpeople,
                     "idpost": idpost,
                    "like" : like

                    }
            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]

def postcomment(content,image, date,  time, idpeople, idpost):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{idpeople}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
    sql = "INSERT INTO commentapost (commentText,commentImage, commentDate, commentTime, peopleID , postID) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (content,image, date, time, id, idpost)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'







def ALLcomment(idpeople, idpost):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    cur.execute(f"SELECT commentID  FROM commentapost WHERE  postID = '{idpost}' ")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])
    ID.sort(reverse=True)
    for ids in ID:
        cur.execute(f"SELECT commentText, commentImage, commentDate, commentTime, peopleID FROM commentapost WHERE commentID = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:


            content = i[0]
            image = i[1]
            date = i[2]
            time = i[3]
            idpeoplecomment = i[4]

            cur.execute(f"SELECT  fullname, image FROM users WHERE id = '{idpeoplecomment}'")


            fullname = ""
            imageface = ""
            for i in cur:
                imageface = i[1]
                fullname = i[0]






            dictionary = {
                    "content" : content,
                    "date" : date,
                    "time" : time,
                    "image" : image,
                    "imageface" : imageface,
                     "fullname": fullname,


                    }
            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]


def hospitals():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    cur.execute("SELECT hospitalID FROM hospital")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)


    for ids in ID:
        cur.execute(f"SELECT hospitalName, hospitalAddress FROM hospital WHERE hospitalID = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:


            name = i[0]
            address = i[1]




            dictionary = {
                    "name" : name,
                    "address" : address,

                    }

            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]



def dataonehospital():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    cur.execute("SELECT hospitalID FROM hospital")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)


    for ids in ID:
        cur.execute(f"SELECT hospitalName, hospitalAddress, hospitalImage FROM hospital WHERE hospitalID = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:


            name = i[0]
            address = i[1]
            image = i[2]




            dictionary = {
                    "name" : name,
                    "address" : address,
                    "image" : image,

                    }

            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]





def dataonerelative(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    List = ""
    cur.execute(f"SELECT * FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:

        name = i[1]
        gender = i[7]
        age = i[6]
        age = age.split("/")[-1]
        relative = "Me"
        phone = i[4]
        address = i[11] + ", " + i[10] + ", " + i[9] + ", " + i[8] + "."


        dictionary = {
            "name": name,
            "gender": gender,
            "age": age,
            "relative": relative,
            "phone": phone,
            "address": address,

        }

        json_object = json.dumps(dictionary, indent=8)

        List = List + str(json_object) + ",-,"
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()

    for i in myresult:
        id = i[0]
        cur.execute(
            f"SELECT relative, fullname, relativedateofbirth, relativephone, relativecity, relativedistrict, relativeward, 	relativeaddress  FROM relativeprofile WHERE idkey = '{id}'")
        for i in cur:
            relative = i[0]
            name = i[1]
            age = i[2]
            age = age.split("/")[-1]
            phone = i[3]

            address = i[7] + ", " + i[6] + ", " + i[5] + ", " + i[4] + "."
            dictionary = {
                "name": name,
                "gender": gender,
                "age": age,
                "relative": relative,
                "phone": phone,
                "address": address,

            }

            json_object = json.dumps(dictionary, indent=8)

            List = List + str(json_object) + ",-,"
    return List[0:-3]


def dataonespec(hospital):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute(f"SELECT * FROM hospital WHERE hospitalName = '{hospital}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
        cur.execute(f"SELECT * FROM specialist WHERE hospitalkey = '{id}'")
        myresult = cur.fetchall()
        for a, i in enumerate(myresult):

            if a % 2 == 0:
                name1 = i[1]

            else:
                name2 = i[1]

                dictionary = {
                    "name1": name1,
                    "name2": name2,

                }

                json_object = json.dumps(dictionary, indent=8)

                List = List + str(json_object) + ",-,"
    return List[0:-3]



def profilesremind(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    List = ""
    for i in cur:
        id = i[0]
        cur.execute(f"SELECT remind	, remindDate, remindTime FROM remind WHERE remindKey = '{id}'")
        for i in cur:
            remind = i[0]
            time = i[1]
            date = i[2]
            dictionary = {
            "remind" : remind,
            "time" : time,
            "date" : date,
            }
            json_object = json.dumps(dictionary, indent=3)
            List =  str(json_object) +  ",-," + List 
    return List[0:-3]

def postremind(email, remind, date, time, tt):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    st = remind.split(" have ")[1]
    hospital = ""
    spec = ""
    if(tt=="nottesthome"):
        hospital = st.split(" at ")[1].strip()
        spec = st.split(" at ")[0].strip()

    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
    sql = "INSERT INTO remind (remind, remindDate, remindTime, remindKey) VALUES (%s, %s, %s, %s)"
    val = (remind, date, time,  id)
    try:
        cur.execute(sql, val)
        if (tt == "nottesthome"):
            tolichdt(hospital, spec, email, date, time)
        else:
            tolichadmin(email, date, time)
        myconn.commit()

    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'

def tolichdt(hospital, spec, email, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idclient = ""
    iddoctor = ""

    hospital = str(hospital)
    spec = str(spec)
    myresult = cur.fetchall()
    for i in myresult:
        idclient = i[0]
    cur.execute(f"SELECT infordoctorKey FROM infordoctor WHERE infordoctorspec = '{spec}' and infordoctorhospital = '{hospital}'")
    myresult = cur.fetchall()
    for i in myresult:
        iddoctor = i[0]


    sql = "INSERT INTO lichdt (lichdtTime, lichdtDate, userKey , doctorKey, active) VALUES (%s, %s, %s, %s, %s)"
    val = (time, date, idclient, iddoctor, "not yet")

    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'

def tolichadmin(email, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idclient = ""
    myresult = cur.fetchall()
    for i in myresult:
        idclient = i[0]

    sql = "INSERT INTO lichadminathome (lichadminathomeDate, lichadminathomeTime, 	lichadminathomeActive , clientKey) VALUES (%s, %s, %s, %s)"
    val = (date, time, "not yet", idclient)

    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'


def postpharmacy(email, img, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
    sql = "INSERT INTO pharmacyonline (pharmacyonlineImage ,pharmacyonlineDate, pharmacyonlineTime, pharmacyonlineKey) VALUES (%s, %s, %s, %s)"
    val = (img ,date, time, id)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'

def profileshistory(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")




    List = ""
    for i in cur:
        id = i[0]
        ID = []
        cur.execute(f"SELECT historyID  FROM history WHERE  historyKey = '{id}' ")
        myresult = cur.fetchall()
        for i in myresult:
            ID.append(i[0])
        ID.sort(reverse=True)
        for ids in ID:


            cur.execute(f"SELECT historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd FROM history WHERE historyID = '{ids}'")
            for i in cur:
                type = i[0]
                remind = i[1]
                time = i[2]
                date = i[3]
                money = i[4]
                moneyadd = i[5]
                dictionary = {
                "type": type,
                "remind" : remind,
                "time" : time,
                "date" : date,
                "money": money,
                "moneyadd": moneyadd,
                }
                json_object = json.dumps(dictionary, indent=6)
                List = List + str(json_object)+ ",-,"
    return List[0:-3]


def qa(email, hoi):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT money, id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[1]


        sql = "INSERT INTO qa (QAText, QAKey) VALUES (%s ,%s)"
        val = (hoi, id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
    return 'success'


def xray(email, nametake, a):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]


        sql = "INSERT INTO xray (xrayImage, xrayKey) VALUES (%s ,%s)"
        val = (a, id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"
    return nametake

def skin(email, nametake, a):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]


        sql = "INSERT INTO xray (xrayImage, xrayKey) VALUES (%s ,%s)"
        val = (a, id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"
    return nametake






def qadoctor():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    cur.execute("SELECT qadoctorID FROM qadoctor")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)


    for ids in ID:
        cur.execute(f"SELECT qadoctorText, qadoctorDate, qadoctorTime, qadoctorKey FROM qadoctor WHERE qadoctorID = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:


            content = i[0]
            date = i[1]
            time = i[2]
            id = i[3]



            cur.execute(f"SELECT id, fullname, image FROM users WHERE id = '{id}'")


            fullname = ""
            imageface = ""
            for i in cur:
                imageface = i[2]
                fullname = i[1]
                idpeople = i[0]


            idpost = ids
            dictionary = {
                    "content" : content,
                    "date" : date,
                    "time" : time,
                    "imageface" : imageface,
                     "fullname": fullname,
                     "idpeople": idpeople,
                     "idpost": idpost

                    }
            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]

def postanewqa(email, content, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]
        mycursor = myconn.cursor()

        sql = "INSERT INTO qadoctor (qadoctorText, qadoctorDate, qadoctorTime, qadoctorKey) VALUES (%s, %s, %s, %s)"
        val = (content, date, time,  id)
        try:
            mycursor.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
        return 'success'

def allservice():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    List = ""
    cur = myconn.cursor()
    cur.execute(f"SELECT * FROM service ")
    myresult = cur.fetchall()


    for i in myresult:
        id = i[0]
        content = i[1]
        money = i[2]
        image = i[3]
        idh = i[4]

        cur.execute(f"SELECT hospitalName FROM hospital WHERE hospitalID = '{idh}' ")
        myresult = cur.fetchall()
        for i in myresult:
            hName = i[0]

            dictionary = {
                    "content" : content,
                    "money" : money,
                    "image": image,
                    "hName": hName
                    }

            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]


def buyservice(email, money, date, time, content, nameH):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    k = "1"
    cur.execute(f"SELECT accumulatedpoints FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0]
        moneynew = moneyold - int(money)
        if moneynew < 0:
            return "error"

        try:
            sql = """
            UPDATE users
            SET accumulatedpoints=%s
            WHERE email=%s
            """
            val =(moneynew, email)
            cur.execute(sql, val)

            myconn.commit()

            toHistoryService(email, money, date, time, content, nameH)


            myconn.close()


        except:
            myconn.rollback()
            myconn.close()
            return "error"
    return "success"

def toHistoryService(email, money, date, time, content, nameH):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT accumulatedpoints, id FROM users WHERE email = '{email}'")
    for i in cur:
        moneyold = i[0] - int(money)
        id = i[1]
        moneynew = moneyold + int(money)
        a = "Sign up for services " + content + " from " + nameH + " (-" + money +" Points" +")"
        sql = "INSERT INTO history (historyType, historyRemind, historyTime, historyDate, historyMoney, historyMoneyadd, historyKey) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = ("0" , a, time, date, str(i[0]) , "0", id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"


def activedoctor(email, hosppital, spec, cc):
    #same email and pass
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    id = ""
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()

    for i in myresult:
        id = i[0]


    cur = myconn.cursor()
    sql = ("insert into infordoctor(infordoctorchungchi, infordoctoristrk, infordoctorist, infordoctorhospital, infordoctorspec ,infordoctorKey) "
           + "values (%s, %s, %s, %s, %s, %s)")

    val = (cc, "0", "0", hosppital, spec, id)
    try:
        cur.execute(sql, val)
        myconn.commit()
        myconn.close()
        doctorat(email)
    except:

        myconn.rollback()
        myconn.close()
        return "fail"

    return "success"


def doctorat(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    try:
        sql = """
        UPDATE users
        SET rolekey=%s
        WHERE email=%s
        """
        val =(1, email)

        cur.execute(sql, val)

        myconn.commit()
        myconn.close()


    except:
        myconn.rollback()
        myconn.close()
        return "fail"
    return 'success'


def allthuoc():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute("SELECT * FROM pharmacyonline")
    myresult = cur.fetchall()
    for i in myresult:
        image = i[1]
        idu = i[4]
        ID = i[0]
        cur.execute(f"SELECT * FROM users WHERE id = '{idu}'")
        myresult = cur.fetchall()
        for a in myresult:
            address = a[11] + ", " + a[10] + ", " + a[9] + ", " + a[8] + "."
            phone = a[4]
            name = a[1]
            dictionary = {
                "image": image,
                "phone": phone,
                "address": address,
                "name": name,
                "ID" : ID
            }

            json_object = json.dumps(dictionary, indent=4)
            List = List + str(json_object) + ",-,"
    return List[0:-3]



def postcommentdt(content, date,  time, idpeople, idpost):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{idpeople}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
        sql = "INSERT INTO commentapostdt (commentdtText, commentdtDate, commentdtTime, peopleID , postID) VALUES (%s, %s, %s, %s, %s)"
        val = (content, date, time, id, idpost)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'



def ALLcommentdt(idpeople, idpost):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    # cur.execute(f"SELECT commentID  FROM commentapostdt WHERE  commentapostdtID = '{idpost}' ")
    cur.execute(f"SELECT commentapostdtID  FROM commentapostdt WHERE  postID = '{idpost}' ")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)
    for ids in ID:
        cur.execute(f"SELECT commentdtText, commentdtDate, commentdtTime, peopleID FROM commentapostdt WHERE commentapostdtID = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:


            content = i[0]
            image = "0"
            date = i[1]
            time = i[2]
            idpeoplecomment = i[3]

            cur.execute(f"SELECT  fullname, image FROM users WHERE id = '{idpeoplecomment}'")
            fullname = ""
            imageface = ""
            for i in cur:
                imageface = i[1]
                fullname = i[0]






            dictionary = {
                    "content" : content,
                    "date" : date,
                    "time" : time,
                    "image" : image,
                    "imageface" : imageface,
                     "fullname": fullname,
                    }
            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]



def xraydt(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]
        mycursor = myconn.cursor()

        sql = "INSERT INTO registeriamge (registeriamgeType,  registeriamgeKey) VALUES (%s, %s)"
        val = ("Xray", id)
        try:
            mycursor.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
        return 'success'

def skindt(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    for i in cur:
        id = i[0]
        mycursor = myconn.cursor()

        sql = "INSERT INTO registeriamge (registeriamgeType,  registeriamgeKey) VALUES (%s, %s)"
        val = ("Skill", id)
        try:
            mycursor.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return 'fail'
        return 'success'





def alllichdt(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    iddt = ""
    idl = ""
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        iddt = i[0]
    cur.execute(f"SELECT * FROM lichdt WHERE doctorKey = '{iddt}'")
    myresult = cur.fetchall()
    for i in myresult:
        idl = i[0]
        time = i[1]
        date = i[2]
        active = i[5]
        cur.execute(f"SELECT * FROM users WHERE id = '{i[3]}'")
        myresult = cur.fetchall()
        for i in myresult:
            name = i[1]
            image = i[5]
            gender = i[7]
            age = i[6]
            age = age.split("/")[-1]
            phone = i[4]
            address = i[11] + ", " + i[10] + ", " + i[9] + ", " + i[8] + "."

            dictionary = {
                "idl" : str(idl),
                "name": name,
                "gender": gender,
                "age": age,
                "phone": phone,
                "address": address,
                "time": time,
                "date": date,
                "image": image,
                "active": active,
            }

            json_object = json.dumps(dictionary, indent=8)
            if(active == "not yet" or active == "home"):########################################################################
                List = List + str(json_object) + ",-,"
    return List[0:-3]


def takeserviceofspec(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    namehH= ""
    List = ""
    nameS = ""
    idu = ""
    idH = ""
    idfind = ""
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]
    cur.execute(f"SELECT infordoctorhospital, infordoctorspec FROM infordoctor WHERE infordoctorKey = '{idu}'")
    myresult = cur.fetchall()
    for i in myresult:
        nameS = i[1]
        namehH = i[0]

    cur.execute(f"SELECT hospitalID FROM hospital WHERE hospitalName = '{namehH}'")
    myresult = cur.fetchall()
    for i in myresult:
        idH = i[0]
    cur.execute(f"SELECT specialistID FROM specialist WHERE specialistName = '{nameS}' and hospitalkey = '{idH}'")
    myresult = cur.fetchall()
    for i in myresult:
        idfind = i[0]

    cur.execute(f"SELECT servicespecName FROM servicespec WHERE specKey = '{idfind}'")
    myresult = cur.fetchall()
    for i in myresult:
        name = i[0]
        dictionary = {
            "name": name,
        }

        json_object = json.dumps(dictionary, indent=1)
        List = List + str(json_object) + ",-,"
    return List[0:-3]

def createex(email, ex, idl):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    sql = """
                UPDATE lichdt
                SET active=%s
                WHERE lichdtID=%s
            """
    val = ("being", idl)
    cur.execute(sql, val)
    myconn.commit()
    sql = "INSERT INTO recodmedicin (recodmedicinEx, lichdtKey) VALUES (%s ,%s)"
    val = (ex, int(idl))
    cur.execute(sql, val)
    myconn.commit()
    return "success"

def alllichdtthuoc(email, hospital):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    iddt = "being"
    idl = ""
    idh = ""
    idu = ""
    ex = ""
    listidh = []
    cur.execute(f"SELECT * FROM infordoctor WHERE 	infordoctorhospital = '{hospital}'")
    myresult = cur.fetchall()
    for i in myresult:
        idh = i[6]
        listidh.append(idh)
    cur.execute(f"SELECT * FROM lichdt WHERE active = '{iddt}'")
    myresult = cur.fetchall()
    for i in myresult:
        if i[4] in listidh:
            idl = i[0]
            time = i[1]
            date = i[2]
            idu = i[3]
            active = i[5]
            cur.execute(f"SELECT * FROM recodmedicin WHERE lichdtKey = '{idl}'")
            myresult = cur.fetchall()
            for i in myresult:
                ex = i[1]
            cur.execute(f"SELECT * FROM users WHERE id = '{idu}'")
            myresult = cur.fetchall()
            for i in myresult:
                name = i[1]
                image = i[5]
                gender = i[7]
                age = i[6]
                age = age.split("/")[-1]
                phone = i[4]
                address = i[11] + ", " + i[10] + ", " + i[9] + ", " + i[8] + "."

                dictionary = {
                    "idl" : str(idl),
                    "name": name,
                    "gender": gender,
                    "age": age,
                    "phone": phone,
                    "address": address,
                    "time": time,
                    "date": date,
                    "image": image,
                    "active": active,
                    "ex" : ex,

                }

                json_object = json.dumps(dictionary, indent=8)
                List = List + str(json_object) + ",-,"
    return List[0:-3]

def takeallthuoc(hospital):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    idh = ""
    List = ""
    cur.execute(f"SELECT hospitalID FROM hospital WHERE hospitalName = '{hospital}'")
    myresult = cur.fetchall()
    for i in myresult:
        idh = i[0]
    cur.execute(f"SELECT * FROM nhathuoc WHERE hospitalKey = '{idh}'")
    myresult = cur.fetchall()
    for i in myresult:
        drug = i[1]
        dictionary = {
            "drug": drug,
        }
        json_object = json.dumps(dictionary, indent=1)
        List = List + str(json_object) + ",-,"
    return List[0:-3]

def ktkethuoc(email, drug, kq, idl):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    sql = """
                UPDATE lichdt
                SET active=%s
                WHERE lichdtID=%s
            """
    val = ("end", idl)
    cur.execute(sql, val)
    myconn.commit()

    sql = """
                    UPDATE recodmedicin
                    SET recodmedicinKQ=%s, recodmedicinDrug=%s
                    WHERE lichdtKey=%s
                """
    val = (kq, drug, idl)
    cur.execute(sql, val)
    myconn.commit()
    return "success"

def allrecodmedical(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idu= ""
    dtid = ""
    namedt = ""
    phonedt = ""
    List =""
    hospital = ""
    spec = ""
    time = ""
    lichid = []
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]
    cur.execute(f"SELECT * FROM lichdt WHERE userKey = '{idu}' and active = 'end'")
    myresult = cur.fetchall()
    for i in myresult:
        lichid.append(i[0])

    for idl in lichid:
        cur.execute(f"SELECT * FROM recodmedicin WHERE lichdtKey = '{idl}'")
        myresult = cur.fetchall()
        for i in myresult:
            if i[4]!="":
                print(i)
                test = i[1][1:]
                test = test.replace("-", " and ")
                kq = i[3][0:-1]
                kq = kq.replace("-", " and ")
                drug = i[2][1:]
                drug = drug.replace("-", " and ")
                cur.execute(f"SELECT doctorKey, lichdtDate, lichdtTime FROM lichdt WHERE lichdtID = '{idl}'")
                myresult = cur.fetchall()
                for i in myresult:
                    dtid = i[0]
                    time = i[1]+ "-" + i[2]
                cur.execute(f"SELECT fullname, phone  FROM users WHERE id = '{dtid}'")
                myresult = cur.fetchall()
                for i in myresult:
                    namedt = i[0]
                    phonedt = i[1]

                cur.execute(f"SELECT infordoctorhospital, infordoctorspec  FROM infordoctor WHERE infordoctorKey = '{dtid}'")
                myresult = cur.fetchall()
                for i in myresult:
                    hospital = i[0]
                    spec = i[1]
                # print(test)
                # print(kq)
                # print(drug)
                # print(namedt)
                # print(phonedt)
                # print(hospital)
                # print(spec)
                # print("////////////////")
                dictionary = {
                    "test": test,
                    "kq": kq,
                    "drug": drug,
                    "namedt": namedt,
                    "phonedt": phonedt,
                    "hospital": hospital,
                    "spec": spec,
                    "time": time
                }
                print(dictionary)

                json_object = json.dumps(dictionary, indent=7)
                List = List + str(json_object) + ",-,"
    return List[0:-3]

def turnoncall(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idu= ""
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]

    sql = """
                       UPDATE infordoctor
                       SET infordoctoriscall=%s
                       WHERE infordoctorKey=%s
                   """
    val = ("1", idu)
    cur.execute(sql, val)
    myconn.commit()
    return "success"


def turnoffcall(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idu= ""
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]

    sql = """
                       UPDATE infordoctor
                       SET infordoctoriscall=%s
                       WHERE infordoctorKey=%s
                   """
    val = ("0", idu)
    cur.execute(sql, val)
    myconn.commit()
    return "success"


def allspeccall():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute(f"SELECT * FROM specialist WHERE hospitalkey = '{1}'")
    myresult = cur.fetchall()
    for a, i in enumerate(myresult):

        if a % 2 == 0:
            name1 = i[1]

        else:
            name2 = i[1]

            dictionary = {
                    "name1": name1,
                    "name2": name2,

            }

            json_object = json.dumps(dictionary, indent=8)

            List = List + str(json_object) + ",-,"
    return List[0:-3]

def doctorspecall(spec):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute(f"SELECT * FROM infordoctor WHERE infordoctorspec = '{spec}'")
    myresult = cur.fetchall()
    for i in myresult:
        if i[7] == "1":
            iddt = i[6]
            chungchi = i[1]
            hospital = i[4]
            cur.execute(f"SELECT * FROM users WHERE id = '{iddt}'")
            myresult = cur.fetchall()
            for i1 in myresult:
                name = i1[1]
                phone = i1[4]
                face = i1[5]
                address = i1[11] + ", " + i1[10] + ", " + i1[9] + ", " + i1[8] + "."
                dictionary = {
                    "chungchi": chungchi,
                    "hospital": hospital,
                    "name": name,
                    "phone": phone,
                    "face": face,
                    "address": address,
                }

                json_object = json.dumps(dictionary, indent=8)

                List = List + str(json_object) + ",-,"
    return List[0:-3]


def addhospital(name, address, image):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    sql = "INSERT INTO hospital (hospitalName, hospitalAddress, hospitalImage) VALUES (%s ,%s, %s)"
    val = (name, address, image)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return "error"
    return "success"

def deletehospital(name):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT * FROM infordoctor WHERE infordoctorhospital = '{name}'")
    myresult = cur.fetchall()
    for i in myresult:
        if len(i)>0:
            return "fail"

    try:
        cur = myconn.cursor()
        cur.execute(f"DELETE FROM hospital WHERE hospitalName = '{name}'")
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'


def allclient():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute(f"SELECT * FROM users WHERE rolekey = '{2}'")
    myresult = cur.fetchall()
    for i in myresult:
        address = str(i[11]) + ", " + str(i[10]) + ", " + str(i[9]) + ", " + str(i[8]) + "."
        dictionary = {
            "name": i[1],
            "email": i[2],
            "password": i[3],
            "phone": i[4],
            "image": i[5],
            "dateofbirth": i[6],
            "gender": i[7],
            "address": address,
            "money": i[12],
            "point": i[13],
            "carepayactive": str(i[14]),
        }
        json_object = json.dumps(dictionary, indent=11)
        List = List + str(json_object) + ",-,"
    return List[0:-3]

def alldoctor():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    hospital = ""
    spec = ""
    cc = ""
    cur.execute(f"SELECT * FROM users WHERE rolekey = '{1}'")
    myresult = cur.fetchall()
    for i in myresult:
        address = str(i[11]) + ", " + str(i[10]) + ", " + str(i[9]) + ", " + str(i[8]) + "."
        cur.execute(f"SELECT * FROM infordoctor WHERE infordoctorKey  = '{i[0]}'")
        myresult = cur.fetchall()
        for i1 in myresult:
            cc = i1[1]
            hospital = i1[4]
            spec = i1[5]

        dictionary = {
            "iddoctor": i[0],
            "name": i[1],
            "email": i[2],
            "password": i[3],
            "phone": i[4],
            "image": i[5],
            "dateofbirth": i[6],
            "gender": i[7],
            "address": address,
            "money": i[12],
            "point": i[13],
            "carepayactive": str(i[14]),
            "cc" : cc,
            "hospital": hospital,
            "spec": spec,

        }
        json_object = json.dumps(dictionary, indent=14)
        List = List + str(json_object) + ",-,"
    return List[0:-3]


def alllichathome():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute(f"SELECT * FROM lichadminathome WHERE lichadminathomeActive = 'not yet'")
    myresult = cur.fetchall()
    for i in myresult:
        idl = i[0]
        date = i[2]
        time = i[3]
        active = i[1]
        cur.execute(f"SELECT * FROM users WHERE id = '{i[4]}'")
        myresult = cur.fetchall()
        for i in myresult:
            idclient = i[0]
            name = i[1]
            image = i[5]
            gender = i[7]
            age = i[6]
            age = age.split("/")[-1]
            phone = i[4]
            address = i[11] + ", " + i[10] + ", " + i[9] + ", " + i[8] + "."

            dictionary = {
                "idl" : str(idl),
                "name": name,
                "gender": gender,
                "age": age,
                "phone": phone,
                "address": address,
                "time": time,
                "date": date,
                "image": image,
                "active": active,
                "idclient": idclient
            }


            json_object = json.dumps(dictionary, indent=12)
            if(active == "not yet"):
                List = List + str(json_object) + ",-,"
    print(List)
    return List[0:-3]

def alldoctorfree(date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    ListDT = []
    hospital = ""
    spec = ""
    cc = ""
    cur.execute(f"SELECT * FROM infordoctor")
    myresult = cur.fetchall()
    for i in myresult:
        ListDT.append(i[6])
    cur.execute(f"SELECT * FROM lichdt WHERE lichdtDate = '{date}'and lichdtTime = '{time}'")
    myresult = cur.fetchall()
    for i in myresult:
        ListDT.remove(i[4])
            #lst.remove('Orchids')
    for idd in ListDT:
        cur.execute(f"SELECT * FROM users WHERE id = '{idd}'")
        myresult = cur.fetchall()
        for i in myresult:
            address = str(i[11]) + ", " + str(i[10]) + ", " + str(i[9]) + ", " + str(i[8]) + "."
            cur.execute(f"SELECT * FROM infordoctor WHERE infordoctorKey  = '{i[0]}'")
            myresult = cur.fetchall()
            for i1 in myresult:
                cc = i1[1]
                hospital = i1[4]
                spec = i1[5]

            dictionary = {
                "iddoctor": i[0],
                "name": i[1],
                "email": i[2],
                "password": i[3],
                "phone": i[4],
                "image": i[5],
                "dateofbirth": i[6],
                "gender": i[7],
                "address": address,
                "money": i[12],
                "point": i[13],
                "carepayactive": str(i[14]),
                "cc" : cc,
                "hospital": hospital,
                "spec": spec,

            }
            json_object = json.dumps(dictionary, indent=14)
            List = List + str(json_object) + ",-,"
    return List[0:-3]



def testhomefinish(id, idclient, iddoctor, date, time):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    sql = """
                UPDATE lichadminathome
                SET lichadminathomeActive=%s
                WHERE 	lichadminathomeID =%s
            """
    val = ("being", id)
    cur.execute(sql, val)
    myconn.commit()
    sql = "INSERT INTO lichdt (lichdtTime, lichdtDate, userKey, doctorKey, active) VALUES (%s ,%s, %s ,%s, %s )"
    val = (time, date, idclient, iddoctor, "home")
    cur.execute(sql, val)
    myconn.commit()
    return "success"


def endow(code, email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ide = ""
    moneye = ""
    idu = ""
    moneyu = ""
    k = "0"
    cur.execute(f"SELECT endowID, endowmoney FROM endow WHERE endowcode = '{code}'")
    myresult = cur.fetchall()
    for i in myresult:
        k = "1"
        ide = i[0]
        moneye = i[1]
    if k == "0":
        return k
    cur.execute(f"SELECT id, money FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]
        moneyu = i[1]

    cur.execute(f"SELECT * FROM userendow WHERE userkey = '{idu}' and endowkey  = '{ide}'")
    myresult = cur.fetchall()
    for i in myresult:
        k = "0"
    if k == "0":
        return k
    sql = "INSERT INTO userendow (userkey, endowkey) VALUES (%s ,%s)"
    val = (int(idu), int(ide))
    cur.execute(sql, val)
    myconn.commit()

    try:
        sql = """
                    UPDATE users
                    SET money=%s
                    WHERE id=%s
                """
        moneynew = float(moneyu) + float(moneye)
        val = (moneynew, idu)
        cur.execute(sql, val)
        myconn.commit()
        myconn.close()
    except:
        myconn.rollback()
        myconn.close()
        k = "0"
    if k == "0":
        return k
    return str(moneye)

def healcv(email, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
        sq = s1 + "-" + s2 + "-" + s3 + "-" + s4 + "-" + s5 + "-" + s6 + "-" + s7 + "-" + s8 + "-" + s9 + "-" + s10 + "-" + s11 + "-" + s12 + "-" + s13;
        sql = "INSERT INTO healcv (healcvresult, healcvkey) VALUES (%s ,%s)"
        val = (sq , id)
        try:
            cur.execute(sql, val)
            myconn.commit()
        except:
            myconn.rollback()
            myconn.close()
            return "error"
    return "success"

def turnonlock(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    sql = """
                       UPDATE users
                       SET setlock=%s
                       WHERE email=%s
                   """
    val = ("1", email)
    cur.execute(sql, val)
    myconn.commit()
    return "success"

def turnofflock(email):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    sql = """
                       UPDATE users
                       SET setlock=%s
                       WHERE email=%s
                   """
    val = ("0", email)
    cur.execute(sql, val)
    myconn.commit()
    return "success"


def addcard(email, number):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT cardID FROM card WHERE cardNumber = '{number}'")
    k = "0"
    a = ""
    cardID = ""
    myresult = cur.fetchall()
    for i in myresult:
        k = "1"
        cardID = i[0]
    if k == "0":
        return "fail"
    cur.execute(f"SELECT cardKey FROM usercard WHERE cardKey = '{cardID}'")
    myresult = cur.fetchall()
    for i in myresult:
        k = "0"
    if k == "0":
        return "fail"

    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idu = ""
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]
    cur.execute(f"SELECT userKey FROM usercard WHERE userKey = '{idu}'")
    myresult = cur.fetchall()
    for i in myresult:
        a = "0"
    if a=="0":
        sql = """
            UPDATE usercard
            SET cardKey=%s, userKey=%s
            WHERE userKey=%s
            """
        val =(cardID, idu, idu)
        cur.execute(sql, val)
        myconn.commit()
    else:
        sql = "INSERT INTO usercard(cardKey, userKey) VALUES (%s ,%s)"
        val = (cardID, idu)
        cur.execute(sql, val)
        myconn.commit()

        sql = """
                    UPDATE users
                    SET addcard=%s
                    WHERE id=%s
                    """
        val = ("1", idu)
        cur.execute(sql, val)
        myconn.commit()
    return "success"



def like(email, idpost, likec):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
    idu = ""
    idun = ""
    myresult = cur.fetchall()
    for i in myresult:
        idu = i[0]
    k = "0"
    cur.execute(f"SELECT usernewID  FROM usernew WHERE userKey = '{idu}' and newKey = '{idpost}'")

    myresult = cur.fetchall()
    for i1 in myresult:
        k = "1"
        idun = i1[0]
    if likec == "0":
        if k == "1":
            sql = """
                                        UPDATE usernew
                                        SET usernewLike=%s
                                        WHERE usernewID=%s
                                        """
            val = ("1", idun)
            cur.execute(sql, val)
            myconn.commit()

        if k == "0":
            sql = "INSERT INTO usernew (usernewLike, userKey, newKey) VALUES (%s ,%s, %s)"
            val = ("1", int(idu), int(idpost))
            cur.execute(sql, val)
            myconn.commit()

        cur.execute(f"SELECT newNumberLike  FROM news WHERE newID = '{idpost}'")
        myresult = cur.fetchall()
        for i in myresult:
            number = int(i[0])


            sql = """
                                                    UPDATE news
                                                    SET newNumberLike=%s
                                                    WHERE newID=%s
                                                    """
            val = (number + 1, idpost)
            cur.execute(sql, val)
            myconn.commit()
            return str(number + 1)
    else:
        sql = """
                                                UPDATE usernew
                                                SET usernewLike=%s
                                                WHERE usernewID=%s
                                                """
        val = ("0", idun)
        cur.execute(sql, val)
        myconn.commit()

        cur.execute(f"SELECT newNumberLike  FROM news WHERE newID = '{idpost}'")
        myresult = cur.fetchall()
        for i in myresult:
            number = int(i[0])

            sql = """
                                                            UPDATE news
                                                            SET newNumberLike=%s
                                                            WHERE newID=%s
                                                            """
            val = (number - 1, idpost)
            cur.execute(sql, val)
            myconn.commit()
            return str(number - 1)


def checklich(hospital, spec, date):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    kq = ""
    idd = ""
    cur.execute(f"SELECT infordoctorKey  FROM infordoctor WHERE infordoctorhospital = '{hospital}' and infordoctorspec = '{spec}' and infordoctoristrk = '1'")
    myresult = cur.fetchall()
    for i in myresult:
        idd = i[0]

    cur.execute(f"SELECT lichdtTime  FROM lichdt WHERE doctorKey = '{int(idd)}' and lichdtDate = '{date}'")
    myresult = cur.fetchall()
    for i in myresult:
        kq = kq + i[0] + "-"
    return kq


def allgift():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    cur.execute("SELECT endowID  FROM endow WHERE endowmoney  != '0'")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)


    for ids in ID:
        cur.execute(f"SELECT endowcode, endowmoney FROM endow WHERE endowID  = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:
            name = i[0]
            money = i[1]


            dictionary = {
                    "name" : name,
                    "money" : money,
                    }

            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"
    return List[0:-3]


def deletegift(name):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    sql = """
                UPDATE endow
                SET endowmoney=%s
                WHERE endowcode =%s
            """
    val = ("0", name)
    cur.execute(sql, val)
    myconn.commit()
    return "success"

def addgift(name ,money):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    cur.execute(f"SELECT endowcode FROM endow WHERE endowcode  = '{name}'")
    myresult = cur.fetchall()
    for i in myresult:
        return "error"
    sql = "INSERT INTO endow (endowcode, endowmoney) VALUES (%s ,%s)"
    val = (name, money)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return "error"
    return "success"

def allserviceadmin():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    ID = []
    List = ""
    cur.execute("SELECT serviceID  FROM service")
    myresult = cur.fetchall()
    for i in myresult:
        ID.append(i[0])

    ID.sort(reverse=True)


    for ids in ID:
        cur.execute(f"SELECT serviceContent, serviceMoney, pserviceImage FROM service WHERE serviceID  = '{ids}'")
        myresult = cur.fetchall()

        for i in myresult:
            name = i[0]
            money = i[1]
            image = i[2]


            dictionary = {
                    "name" : name,
                    "money" : money,
                    "image": image,
                    }

            json_object = json.dumps(dictionary, indent=8)
            List = List + str(json_object)+ ",-,"

    return List[0:-3]

def deleteservice(name):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    try:
        cur = myconn.cursor()
        cur.execute(f"DELETE FROM service WHERE serviceContent = '{name}'")
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return 'fail'
    return 'success'

def addservice(name, money, image):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()

    sql = "INSERT INTO service (serviceContent, serviceMoney, pserviceImage) VALUES (%s ,%s, %s)"
    val = (name, money, image)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        myconn.rollback()
        myconn.close()
        return "error"
    return "success"

def allcontribute():
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    List = ""
    cur.execute(f"SELECT QAKey, QAText FROM qa")
    myresult = cur.fetchall()
    for i in myresult:
        id = i[0]
        content = i[1]
        cur.execute(f"SELECT fullname, image QAText FROM users WHERE id = '{id}'")
        myresult = cur.fetchall()
        for i1 in myresult:
            name = i1[0]
            avatar = i1[1]
            dictionary = {
                "name": name,
                "content": content,
                "avatar": avatar,
            }

        json_object = json.dumps(dictionary, indent=8)
        List = List + str(json_object) + ",-,"

    return List[0:-3]

def checktrung(CMND):
    myconn = mysql.connector.connect(host="localhost", user="root", database="doctor1")
    cur = myconn.cursor()
    cur.execute(f"SELECT number FROM cmnd WHERE number = '{CMND}'")
    myresult = cur.fetchall()
    for i in myresult:
        return "error"