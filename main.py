from flask import Flask, request, Response
import flask
import werkzeug
import base64
import cv2
import requests
from PIL import Image
from io import BytesIO
import unist
# from ClassifiCard.testface import predictface
from detect import Xray
from detect1 import Skin
# from ClassifiCard.testcardfront import predictcardfront
# from ClassifiCard.testcard import predictcard
from ClassifiCard.checkFACE import detectFace
import json
import random
app = flask.Flask(__name__)
from flask import send_file
# from flask import jsonify
# import os

filename = ""
a = 0
CMDN = ""

@app.route('/FaceImage', methods = ['GET', 'POST'])
def handle_request():
    if flask.request.method == 'POST':
        imagefile = flask.request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(filename)
        data_uri = base64.b64encode(open(filename, 'rb').read()).decode('utf-8')
        im = Image.open(BytesIO(base64.b64decode(data_uri)))
        im.save('FACE.png', 'PNG')
        link = 'FACE.png'
        out = detectFace(link=link)
        print(out)

        if len(out) != 0:
            return "success"
        else:
            return 'fail' #fail
    return "fail"


@app.route('/CardFrontImage', methods = ['GET', 'POST'])
def handle_request1():
    if flask.request.method == 'POST':
        imagefile = flask.request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(filename)
        data_uri = base64.b64encode(open(filename, 'rb').read()).decode('utf-8')
        im = Image.open(BytesIO(base64.b64decode(data_uri)))
        im.save('CARDFRONT.png', 'PNG')
        link = 'CARDFRONT.png'
        # out1, out2 = predictcardfront(link=link)
        #
        # if out1 >= 1.8:#1.8
        #     return "success"
        # else:
        #     return 'fail'

        url = 'https://api.fpt.ai/vision/idr/vnm'

        files = {'image': open('CARDFRONT.png', 'rb').read()}
        headers = {
            'api-key': 'RQpZ1ZDQvVUIGqC9vvdEavSZmAnYU8W0'
        }

        # response = requests.post(url, files=files, headers=headers)
        #
        # print(response.text)

        # url = 'https://api.fpt.ai/vision/idr/vnm'
        #
        # files = {'image': open('CARDFRONT.png', 'rb').read()}
        # headers = {
        #     'api-key': 'RQpZ1ZDQvVUIGqC9vvdEavSZmAnYU8W0'
        # }
        response = requests.post(url, files=files, headers=headers)
        resultcardfront = response.json()
        print(resultcardfront)

        successLogin = unist.checktrung(resultcardfront["data"][0]["id"])
        CMDN = resultcardfront["data"][0]["id"]
        if successLogin=="error":
            return "error"

        try:
            dictionary = {
                "name" : resultcardfront["data"][0]["name"],
                "id": resultcardfront["data"][0]["id"],
                "gender": resultcardfront["data"][0]["sex"],
                "dateob": resultcardfront["data"][0]["dob"],
                "province": resultcardfront["data"][0]["address_entities"]['province'],
                "district": resultcardfront["data"][0]["address_entities"]['district'],
                "ward": resultcardfront["data"][0]["address_entities"]['ward'],
                "address": resultcardfront["data"][0]["address"],
            }

            json_object = json.dumps(dictionary, indent=8)
            return str(json_object)
        except:
            return 'error' # error


@app.route('/DoctorFrontImage', methods = ['GET', 'POST'])
def handle_request11():
    if flask.request.method == 'POST':
        imagefile = flask.request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(filename)
        data_uri = base64.b64encode(open(filename, 'rb').read()).decode('utf-8')
        im = Image.open(BytesIO(base64.b64decode(data_uri)))
        im.save('DOCTORFRONT.png', 'PNG')
        link = 'DOCTORFRONT.png'
        # out1, out2 = predictcardfront(link=link)

        # if out1 >= -10:#1.8
        return "success"
        # else:
        #     return 'error'# fail
    return "fail"

@app.route('/CardImage', methods = ['GET', 'POST'])
def handle_request2():
    if flask.request.method == 'POST':
        imagefile = flask.request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(filename)
        data_uri = base64.b64encode(open(filename, 'rb').read()).decode('utf-8')
        im = Image.open(BytesIO(base64.b64decode(data_uri)))
        im.save('CARD.png', 'PNG')
        link = 'CARD.png'
        # out1, out2 = predictcard(link=link)

        # if out1 >= 3.1: #3.2
        #     return "success"
        # else:
        #     return 'fail'
        url = 'https://api.fpt.ai/vision/idr/vnm'

        files = {'image': open('CARD.png', 'rb').read()}
        headers = {
            'api-key': 'RQpZ1ZDQvVUIGqC9vvdEavSZmAnYU8W0'
        }
        response = requests.post(url, files=files, headers=headers)
        resultcardback = response.json()
        try:
            check = resultcardback['data'][0]['features']
            return "success"
        except:
            return 'error'#error

        #data = {}
        #data['image'] = data_uri
        #data['number'] = '1'



        #return jsonify(data)
        #send_file(filename, mimetype='image/gif')


        #return "Image Uploaded Successfully"


@app.route("/register", methods = ['POST'])
def create_account():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        data1 = str(data)
        #data = json.loads(data)
        fullname = data['fullName']
        email = data['email']
        password = data['passWord']
        phone = data['phone']

        sucessregister = unist.insertregister(fullname, email, password, phone)
        if sucessregister == 1:
            return "Register Success"
        else:
            return "Register fail"

@app.route("/login", methods = ['POST'])
def login_account():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        password = data['passWord']
        successLogin = unist.login(email, password)
        return successLogin

@app.route('/updateprofile', methods = ['GET', 'POST'])
def updateprofile():
    if flask.request.method == 'POST':

        data = json.loads(request.data)
        bytearrayimage1 = ""
        fullname = data['fullName']
        email = data['email']
        bytearrayimage = data['bytearrayimage']
        newimg = data['imgnew']
        dateofbirth = data['dateofbirth']
        sex = data['sex']
        city = data['city']
        township = data['township']
        ward = data['ward']
        apartmentnumber = data['apartmentnumber']
        if(newimg!="0"):
            filename = "{}".format(random.uniform(1, 10))
            check = "user/" + email + filename
            decodeit = open('user/'+email+ filename+'.png', 'wb')
            decodeit.write(base64.b64decode((newimg)))
            decodeit.close()
            bytearrayimage1 = 'user/'+email+ filename
        else:
            bytearrayimage1 = bytearrayimage
        successupdate = unist.updateprofile(fullname, email, bytearrayimage1, dateofbirth, sex, city, township, ward, apartmentnumber)
        return successupdate

@app.route('/get', methods=['GET', 'POST'])
def get():
    if flask.request.method == 'GET':
        return unist.img()

@app.route('/updatemoney', methods=['GET', 'POST'])
def updatemoney():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        money = data['money']
        date = data['date']
        time = data['time']
        successupdate = unist.updatemoney(email, money, date, time)
        return successupdate
@app.route('/updatpoint', methods=['GET', 'POST'])
def updatpoint():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        money = data['points']
        date = data['date']
        time = data['time']
        successupdate = unist.updatepoint(email, money, date, time)
        return successupdate
    return "fail"

@app.route('/profilerelative', methods=['GET', 'POST'])
def profilerelative():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successget = unist.profilerelative(email)
        return successget
    return "fail"

@app.route('/profilerelativedetail', methods=['GET', 'POST'])
def profilerelativedetail():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        phone = data['phone']
        successget = unist.profilerelativedetail(phone)
        return successget
    return "fail"

@app.route('/profilerelativedetailupdate', methods=['GET', 'POST'])
def profilerelativedetailupdate():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        phonenew = data['phonenew']
        relative = data['relative']
        fullname = data['fullname']
        dataofbirth = data['dataofbirth']
        gender = data['gender']
        city = data['city']
        district = data['district']
        ward = data['ward']
        address = data['address']
        phoneold = data['phoneold']
        successget = unist.profilerelativedetailupdate(relative, fullname, phonenew, dataofbirth, gender, city, district, ward, address, phoneold)
        return successget
    return "fail"

@app.route('/profilerelativeadd', methods=['GET', 'POST'])
def profilerelativeadd():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        relative = data['relative']
        fullname = data['fullname']
        dataofbirth = data['dataofbirth']
        gender = data['gender']
        city = data['city']
        district = data['district']
        ward = data['ward']
        address = data['address']
        phone = data['phone']
        successget = unist.profilerelativeadd(relative, fullname, phone, dataofbirth, gender, city, district,ward, address, email)
        return successget
    return "fail"

@app.route('/updatemoneydonation', methods=['GET', 'POST'])
def updatemoneydonation():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        money = data['money']
        date = data['date']
        time = data['time']
        k = data['k']
        successupdate = unist.updatemoneydonation(email, money, date, time, k)
        return successupdate
@app.route('/updatpointdonation', methods=['GET', 'POST'])
def updatpointdonation():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        point = data['point']
        successupdate = unist.updatepointdonation(email, point)
        return successupdate
    return "fail"

@app.route('/profileschedule', methods=['GET', 'POST'])
def profileschedule():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successget = unist.profileschedule(email)
        return successget
    return "fail"

@app.route('/profilescheduleadd', methods=['GET', 'POST'])
def profilescheduleadd():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        day = data['day']
        time = data['time']
        remind = data['remind']

        successget = unist.profilescheduleadd(email, day, time, remind)
        return successget
    return "fail"

@app.route('/profilescheduledelete', methods=['GET', 'POST'])
def profilescheduledelete():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        position = data['position']
        position = int(position);

        successget = unist.profilescheduledelete(email, position)
        return successget
    return "fail"

@app.route('/profilepasschange', methods=['GET', 'POST'])
def profilepasschange():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        passnew = data['passnew']
        successget = unist.profilepasschange(email, passnew)
        return successget
    return "fail"

@app.route('/activecarepay', methods=['GET', 'POST'])
def activecarepay():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']

        img = cv2.imread("CARDFRONT.png")
        cv2.imwrite('cmnd/' + email + "-front" + '.png', img)
        img = cv2.imread("CARD.png")
        cv2.imwrite('cmnd/' + email + "-back" + '.png', img)


        successget = unist.activecarepay(email, CMDN)
        return successget
    return "fail"

@app.route('/takeinftranfer', methods=['GET', 'POST'])
def takeinftranfer():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        phone = data['phone']
        successget = unist.takeinftranfer(phone)
        return successget
    return "fail"

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        phone = data['phone']
        am = data['am']
        date = data['date']
        time = data['time']
        am = float(am)
        successget = unist.transfer(email, phone, am, date, time)
        return successget
    return "fail"

@app.route('/transferbank', methods=['GET', 'POST'])
def transferbank():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        date = data['date']
        time = data['time']
        stk = data['stk']
        am = data['am']
        am = float(am)

        successget = unist.transferbank(email, stk, am, date, time)
        return successget
    return "fail"

@app.route('/postanew', methods = ['GET', 'POST'])
def postanew():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        content = data['content']
        image = data['image']
        date = data['date']
        time = data['time']

        if image != "0":
            decodeit = open('post/'+email+ content[0:3] +'.png', 'wb')
            decodeit.write(base64.b64decode((image)))
            decodeit.close()
            bytearrayimage1 = 'post/'+email + content[0:3]
        else:
            bytearrayimage1 = "0"


        successupdate = unist.post(email,content,  bytearrayimage1, date, time)
        return successupdate

@app.route('/postacomment', methods=['GET', 'POST'])
def postacomment():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        content = data['content']
        image = data['image']
        date = data['date']
        time = data['time']

        idpeople = data['idpeople']
        idpost = data['idpost']
        idpost = int(idpost)
        if image != "0":
            decodeit = open('comment/'+idpeople+ "-" + str(idpost) + content +'.png', 'wb')
            decodeit.write(base64.b64decode((image)))
            decodeit.close()
            bytearrayimage1 = 'comment/'+idpeople + "-" + str(idpost) + content
        else:
            bytearrayimage1 = "0"

        successupdate = unist.postcomment(content,bytearrayimage1, date,  time, idpeople, idpost)
        return successupdate
@app.route('/allcomment', methods=['GET', 'POST'])
def allcomment():
    if flask.request.method == 'POST':
        data = json.loads(request.data)

        idpeople = data['idpeople']
        idpost = data['idpost']
        idpost = int(idpost)
        idpeople = int(idpeople)
        successupdate = unist.ALLcomment(idpeople, idpost)
        return successupdate

@app.route('/news', methods=['GET', 'POST'])
def news():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successget = unist.news(email)
        return successget
    return "fail"

@app.route('/hospital', methods=['GET', 'POST'])
def hospital():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        successget = unist.hospitals()
        return successget
    return "fail"

@app.route('/dataonehospital', methods=['GET', 'POST'])
def dataonehospital():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        successget = unist.dataonehospital()
        return successget
    return "fail"


@app.route('/dataonerelative', methods=['GET', 'POST'])
def dataonerelative():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successget = unist.dataonerelative(email)
        return successget
    return "fail"


@app.route('/dataonespec', methods=['GET', 'POST'])
def dataonespec():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        hospital = data['hospital']
        successget = unist.dataonespec(hospital)
        return successget
    return "fail"

@app.route('/profilesremind', methods=['GET', 'POST'])
def profilesremind():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successget = unist.profilesremind(email)
        return successget
    return "fail"

@app.route('/postremind', methods=['GET', 'POST'])
def postremind():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        tt = data['tt']
        email = data['email']
        remind = data['remind']
        date = data['date']
        time = data['time']

        successget = unist.postremind(email, remind, date, time, tt)
        return successget
    return "fail"
@app.route('/postpharmacy', methods=['GET', 'POST'])
def postpharmacy():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        img = data['toa']
        date = data['date']
        time = data['time']


        filename = "{}".format(random.uniform(20, 30))
        check = "toa/" + email + filename
        decodeit = open('toa/' + email + filename + '.png', 'wb')
        decodeit.write(base64.b64decode((img)))
        decodeit.close()

        successget = unist.postpharmacy(email, check, date, time)
        return successget
    return "fail"
import mysql.connector
@app.route('/user/<string:email><string:filename>', methods=['GET', 'POST'])
def getupdate(email, filename):
    if flask.request.method == 'GET':
        return send_file("user/" +email + filename +'.png', mimetype='image/gif')


@app.route('/comment/<string:email>-<string:idpost><string:content>', methods=['GET', 'POST'])
def getupcomment(email, idpost, content):
    if flask.request.method == 'GET':
        return send_file('comment/'+email + "-" + str(idpost) + content +'.png', mimetype='image/gif')

@app.route('/post/<string:email><string:content>', methods=['GET', 'POST'])
def getuppost(email, content):
    if flask.request.method == 'GET':
        return send_file('post/'+email  + content +'.png', mimetype='image/gif')

@app.route('/profileshistory', methods=['GET', 'POST'])
def profileshistory():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successget = unist.profileshistory(email)
        return successget
    return "fail"

@app.route('/qa', methods=['GET', 'POST'])
def qa():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        hoi = data['hoi']
        successget = unist.qa(email, hoi)
        return successget
    return "fail"


@app.route('/xray', methods = ['GET', 'POST'])
def xray():
    if flask.request.method == 'POST':

        data = json.loads(request.data)
        email = data['email']
        iamge = data['image']
        filename = random.uniform(1,10)


        decodeit = open('userXray/'+email+ str(filename)+'.png', 'wb')
        decodeit.write(base64.b64decode((iamge)))
        decodeit = open("dt" + '.jpg', 'wb')
        decodeit.write(base64.b64decode((iamge)))
        decodeit.close()

        nametake = Xray()

        nametake = str(nametake)
        a = str(nametake)
        nametake = nametake.split("exp")[1]
        successget = unist.xray(email, nametake, a)


    return nametake


@app.route('/skin', methods = ['GET', 'POST'])
def skin():
    if flask.request.method == 'POST':

        data = json.loads(request.data)
        email = data['email']
        iamge = data['image']
        filename = random.uniform(1,10)


        decodeit = open('userSkin/'+email+ str(filename)+'.png', 'wb')
        decodeit.write(base64.b64decode((iamge)))
        decodeit = open("dt1" + '.jpg', 'wb')
        decodeit.write(base64.b64decode((iamge)))
        decodeit.close()

        nametake = Skin()

        nametake = str(nametake)
        a = str(nametake)
        nametake = nametake.split("exp")[1]
        #successget = unist.skin(email, nametake, a)


    return nametake


@app.route('/runs/detect/exp<string:path1>', methods=['GET', 'POST'])
def getXray(path1):
    if flask.request.method == 'GET':
        return send_file("runs/detect/exp" +path1 +"/"+ "dt" +'.jpg', mimetype='image/gif')

@app.route('/runs/detect/exp<string:path1>/dt1', methods=['GET', 'POST'])
def getSkin(path1):
    if flask.request.method == 'GET':
        return send_file("runs/detect/exp" +path1 +"/"+ "dt1" +'.jpg', mimetype='image/gif')




@app.route('/qadoctor', methods=['GET', 'POST'])
def qadoctor():
    if flask.request.method == 'POST':
        data = json.loads(request.data)

        successget = unist.qadoctor()
        return successget
    return "fail"

@app.route('/postanewqa', methods = ['GET', 'POST'])
def postanewqa():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        content = data['content']
        date = data['date']
        time = data['time']

        successupdate = unist.postanewqa(email, content, date, time)
        return successupdate

@app.route('/allservice', methods=['GET', 'POST'])
def allservice():
    if flask.request.method == 'POST':
        data = json.loads(request.data)

        successget = unist.allservice()
        return successget
    return "fail"

@app.route('/buyservice', methods=['GET', 'POST'])
def buyservice():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        money = data['money']
        date = data['date']
        time = data['time']
        content = data['content']
        nameH = data['nameH']
        successupdate = unist.buyservice(email, money, date, time, content, nameH)
        return successupdate


@app.route('/activedoctor', methods=['GET', 'POST'])
def activedoctor():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        hosppital = data['hospital']
        spec = data['spec']
        filename = "{}".format(random.uniform(10, 20))
        img = cv2.imread("DOCTORFRONT.png")
        cv2.imwrite("doctor/chungchi/" + email + filename + ".png", img)
        cc = "doctor/chungchi/" + email + filename
        successget = unist.activedoctor(email, hosppital, spec, cc)
        return successget
    return "fail"

@app.route('/doctor/chungchi/<string:email><string:filename>', methods=['GET', 'POST'])
def getcc(email, filename):
    if flask.request.method == 'GET':
        return send_file("doctor/chungchi/" +email + filename +'.png', mimetype='image/gif')

@app.route('/toa/<string:email><string:filename>', methods=['GET', 'POST'])
def gettoa(email, filename):
    if flask.request.method == 'GET':
        return send_file("toa/" +email + filename +'.png', mimetype='image/gif')

@app.route('/allthuoc', methods = ['GET', 'POST'])
def allthuoc():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']

        successupdate = unist.allthuoc()
        return successupdate
@app.route('/postacommentdt', methods = ['GET', 'POST'])
def postacommentdt():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        content = data['content']
        date = data['date']
        time = data['time']
        idpeople = data['idpeople']
        idpost = data['idpost']
        successupdate = unist.postcommentdt(content, date,  time, idpeople, idpost)
        return successupdate

@app.route('/allcommentdt', methods=['GET', 'POST'])
def allcommentdt():
    if flask.request.method == 'POST':
        data = json.loads(request.data)

        idpeople = data['idpeople']
        idpost = data['idpost']
        idpost = int(idpost)
        idpeople = int(idpeople)
        successupdate = unist.ALLcommentdt(idpeople, idpost)
        return successupdate
@app.route('/xraydt', methods=['GET', 'POST'])
def xraydt():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.xraydt(email)
        return successupdate
@app.route('/skindt', methods=['GET', 'POST'])
def skindt():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.skindt(email)
        return successupdate
@app.route('/alllichdt', methods=['GET', 'POST'])
def alllichdt():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.alllichdt(email)
        return successupdate

@app.route('/takeserviceofspec', methods=['GET', 'POST'])
def takeserviceofspec():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.takeserviceofspec(email)
        return successupdate

@app.route('/createex', methods=['GET', 'POST'])
def createex():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        ex = data['ex']
        idl = data['idl']
        successupdate = unist.createex(email, ex, idl)
        return successupdate
@app.route('/alllichdtthuoc', methods=['GET', 'POST'])
def alllichdtthuoc():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        hospital = data['hospital']
        successupdate = unist.alllichdtthuoc(email, hospital)
        return successupdate

@app.route('/takeallthuoc', methods=['GET', 'POST'])
def takeallthuoc():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        hospital = data['hospital']
        successupdate = unist.takeallthuoc(hospital)
        return successupdate


@app.route('/ktkethuoc', methods=['GET', 'POST'])
def ktkethuoc():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        drug = data['drug']
        kq = data['kq']
        idl = data['idl']
        successupdate = unist.ktkethuoc(email, drug, kq, idl)
        return successupdate

@app.route('/allrecodmedical', methods=['GET', 'POST'])
def allrecodmedical():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.allrecodmedical(email)
        return successupdate


@app.route('/turnoncall', methods=['GET', 'POST'])
def turnoncall():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.turnoncall(email)
        return successupdate
@app.route('/turnoffcall', methods=['GET', 'POST'])
def turnoffcall():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.turnoffcall(email)
        return successupdate

@app.route('/allspeccall', methods=['GET', 'POST'])
def allspeccall():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        #email = data['email']
        successupdate = unist.allspeccall()
        return successupdate

@app.route('/doctorspecall', methods=['GET', 'POST'])
def doctorspecall():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        spec = data['spec']
        successupdate = unist.doctorspecall(spec)
        return successupdate


@app.route('/addhospital', methods=['GET', 'POST'])
def addhospital():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        address = data['address']
        image = data['image']

        filename = "{}".format(random.uniform(30, 40))
        check = "hospital/" + filename
        decodeit = open('hospital/' + filename + '.png', 'wb')
        decodeit.write(base64.b64decode((image)))
        decodeit.close()
        linkimage = 'hospital/'  + filename

        successupdate = unist.addhospital(name, address, linkimage)
        return successupdate

@app.route('/hospital/<string:filename>', methods=['GET', 'POST'])
def gethospital(filename):
    if flask.request.method == 'GET':
        return send_file("hospital/" + filename +'.png', mimetype='image/gif')

@app.route('/service/<string:filename>', methods=['GET', 'POST'])
def getservice(filename):
    if flask.request.method == 'GET':
        return send_file("service/" + filename +'.png', mimetype='image/gif')

@app.route('/deletehospital', methods=['GET', 'POST'])
def deletehospital():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        successupdate = unist.deletehospital(name)
        return successupdate
@app.route('/allclient', methods=['GET', 'POST'])
def allclient():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.allclient()
        return successupdate

@app.route('/alldoctor', methods=['GET', 'POST'])
def alldoctor():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.alldoctor()
        return successupdate

@app.route('/alllichathome', methods=['GET', 'POST'])
def alllichathome():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.alllichathome()
        return successupdate

@app.route('/alldoctorfree', methods=['GET', 'POST'])
def alldoctorfree():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        date = data['date']
        time = data['time']
        successupdate = unist.alldoctorfree(date, time)
        return successupdate

@app.route('/testhomefinish', methods=['GET', 'POST'])
def testhomefinish():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        id = data['id']
        idclient = data['idclient']
        iddoctor = data['iddoctor']
        date = data['date']
        time = data['time']
        successupdate = unist.testhomefinish(id, idclient, iddoctor, date, time)
        return successupdate

@app.route('/endow', methods=['GET', 'POST'])
def endow():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        code = data['code']
        successupdate = unist.endow(code, email)
        return successupdate

@app.route('/healcv', methods=['GET', 'POST'])
def healcv():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        s1 = data['s1']
        s2 = data['s2']
        s3 = data['s3']
        s4 = data['s4']
        s5 = data['s5']
        s6 = data['s6']
        s7 = data['s7']
        s8 = data['s8']
        s9 = data['s9']
        s10 = data['s10']
        s11 = data['s11']
        s12 = data['s12']
        s13 = data['s13']
        successupdate = unist.healcv(email, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13)
        return successupdate

@app.route('/turnonlock', methods=['GET', 'POST'])
def turnonlock():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.turnonlock(email)
        return successupdate
@app.route('/turnofflock', methods=['GET', 'POST'])
def turnofflock():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successupdate = unist.turnofflock(email)
        return successupdate

@app.route('/addcard', methods=['GET', 'POST'])
def addcard():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        number = data['number']
        successupdate = unist.addcard(email, number)
        return successupdate

@app.route('/like', methods=['GET', 'POST'])
def like():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        likec = data['likec']
        idpost = data['idpost']
        successupdate = unist.like(email, idpost, likec)
        return successupdate

@app.route('/checklich', methods=['GET', 'POST'])
def checklich():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        hospital = data['hospital']
        spec = data['spec']
        date = data['date']
        successupdate = unist.checklich(hospital, spec, date)
        return successupdate

@app.route("/adminregister", methods = ['POST'])
def adminregister():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        data1 = str(data)
        #data = json.loads(data)
        fullname = data['fullName']
        email = data['email']
        password = data['passWord']
        phone = data['phone']

        sucessregister = unist.adminregister(fullname, email, password, phone)
        if sucessregister == 1:
            return "Register Success"
        else:
            return "Register fail"

@app.route("/adminlogin", methods = ['POST'])
def adminlogin():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        password = data['passWord']
        successLogin = unist.adminlogin(email, password)

        return successLogin

@app.route("/allgift", methods = ['POST'])
def allgift():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successLogin = unist.allgift()

        return successLogin

@app.route("/deletegift", methods = ['POST'])
def deletegift():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        name = name.split("Code : ")[1]
        successLogin = unist.deletegift(name)

        return successLogin

@app.route("/addgift", methods = ['POST'])
def addgift():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        money = data['money']
        successLogin = unist.addgift(name ,money)

        return successLogin

@app.route("/allserviceadmin", methods = ['POST'])
def allserviceadmin():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successLogin = unist.allserviceadmin()

        return successLogin

@app.route("/deleteservice", methods = ['POST'])
def deleteservice():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        successLogin = unist.deleteservice(name)

        return successLogin

@app.route('/addservice', methods=['GET', 'POST'])
def addservice():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        money = data['money']
        image = data['image']

        filename = "{}".format(random.uniform(30, 40))
        check = "service/" + filename
        decodeit = open('service/' + filename + '.png', 'wb')
        decodeit.write(base64.b64decode((image)))
        decodeit.close()
        linkimage = 'service/'  + filename

        successupdate = unist.addservice(name, money, linkimage)
        return successupdate

@app.route("/allcontribute", methods = ['POST'])
def allcontribute():
    if flask.request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        successLogin = unist.allcontribute()

        return successLogin

app.run(host="0.0.0.0", port=5000, debug=True)