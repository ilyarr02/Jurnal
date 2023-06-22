from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
import datetime


def home(request):
    return render(request, 'home.html')

def loginn(request):
    username = request.POST['log']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    allInfo = False
    table = 0
    allUs = Users.objects.all()

    if user is not None:
        login(request, user)
        us = Users.objects.get(user_info=user)
        print(us.FIO)
        print(user)
        if us.userStatus == 'Ученик':
            allJur = Jurnal.objects.filter(user=user)
            #return render(request, 'mainn.html', {'user': user, 'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, 'allJur': allJur})
            return redirect("/home/")
        else:
            #return render(request, 'mainn.html',
                          #{'user': user, 'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us})
            return redirect("/home/")
    else:
        print("gse")

        return redirect('/')

def mainn(request):
    allUs = Users.objects.all()
    allInfo = False
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 0
    if us.userStatus == 'Ученик':
        allJur = Jurnal.objects.filter(user=user)
        return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, 'allJur': allJur})
    elif us.userStatus == 'Учитель':
        teach = True
        return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, 'teach': teach})
    return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us})


def logoutt(request):
    logout(request)
    return redirect('/')

def teachers(request):
    allInfo = False
    allUs = Users.objects.all()
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 1
    if us.userStatus == 'Методист':
        table = 7
    return render(request, "mainn.html", {'allInfo': allInfo, 'allUs': allUs, 'table': table, 'us': us})

def pupils(request):
    allInfo = False
    allUs = Users.objects.all()
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 2
    return render(request, "mainn.html", {'allInfo': allInfo, 'allUs': allUs, 'table': table, 'us': us})

def metodists(request):
    allInfo = False
    allUs = Users.objects.all()
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 3
    return render(request, "mainn.html", {'allInfo': allInfo, 'allUs': allUs, 'table': table, 'us': us})

def addUs(request):
    sstatus = request.POST.get('status', None)
    return render(request, 'addUs.html', {'sstatus': sstatus})

def addUser(request):
    allInfo = False
    status = request.POST.get('status', None)
    fio = request.POST['FIO']


    password = request.POST['pas']
    username = request.POST['log']
    email = "email@email.email"
    user = User.objects.create_user(username,email, password)
    user.first_name = status
    user.last_name = status
    user.save()

    us = Users()
    us.pas = password
    us.FIO = fio


    if status == 'Учитель':
        predmet = request.POST['pred']
        us.predmet = predmet
        us.experience = request.POST['exp']
    elif status == 'Ученик':
        clas = request.POST['clas']
        gen = request.POST['gender']
        adr = request.POST['adress']
        us.clas = clas
        us.gender = gen
        us.adress = adr
    else:
        age = request.POST['age']
        us.age = age
    us.userStatus = status
    us.user_info = User.objects.get(username=username)
    us.save()
    allUs = Users.objects.all()
    return redirect('/home/')

def delUser(request):
    id = request.POST['id']
    us = Users.objects.get(pk=int(id))
    id1 = us.user_info.id
    uss = User.objects.filter(id=id1)
    us.delete()
    uss.delete()
    return redirect('/home/')

def allInfo(request):
    allUs = Users.objects.all()
    allInfo = True
    table = 0
    return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table})

def notAllInfo(request):
    allUs = Users.objects.all()
    allInfo = False
    table = 0
    return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table})

def rasp(request):
    allUs = Users.objects.all()
    allInfo = False
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 3
    if us.userStatus == "ADMIN":
        table = 0
    return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us})

def graph(request):
    allUs = Users.objects.all()
    allInfo = False
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 19
    allJur = Jurnal.objects.filter(user=user)
    return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, 'allJur':allJur})

def raspDay(request):
    date = request.POST.get('day', None)
    print(date)
    allUs = Users.objects.all()
    allInfo = False
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 1
    if us.userStatus == 'Методист':
        table = 6
    if us.userStatus == "Ученик":
        try:
            raspp = timetable.objects.get(clas= us.clas,date=date)
        except:
            global lastdate
            lastdate = date
            raspp = {}
            topic = {}
    else:
        clas = request.POST['clas']
        try:
            raspp = timetable.objects.get(clas=clas, date=date)
        except:
            raspp = {}
    try:
        predm = {"p1": raspp.predmet1, 'p2': raspp.predmet2, 'p3': raspp.predmet3, 'p4': raspp.predmet4, 'p5': raspp.predmet5, 'p6': raspp.predmet6, 'p7': raspp.predmet7}
        dz = {"d1": raspp.dz1, 'd2': raspp.dz2, 'd3': raspp.dz3, 'd4': raspp.dz4,
             'd5': raspp.dz5, 'd6': raspp.dz6, 'd7': raspp.dz7}
        topic = {"t1": raspp.topic1, 't2': raspp.topic2, 't3': raspp.topic3, 't4': raspp.topic4, 't5': raspp.topic5, 't6': raspp.topic6, 't7': raspp.topic7}
    except:
        predm = {}
        dz = {}
        topic = {}
    return render(request, 'mainn.html', {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, "raspp": raspp, 'predm': predm, 'dz': dz, 'd': date, 'topic': topic})


def raspAdd(request):
    table = 5
    user = request.user
    us = Users.objects.get(user_info=user)
    return render(request, 'mainn.html',
                  {'table': table, 'us': us})

def jurnal(reqeust):
    allUs = Users.objects.all()
    user = reqeust.user
    us = Users.objects.get(user_info=user)
    if us.predmet == 'Математика':
        predm = 'mat'
    elif us.predmet == 'Русский':
        predm = 'rus'
    elif us.predmet == 'Биология':
        predm = 'bio'
    elif us.predmet == 'Химия':
        predm = 'him'
    elif us.predmet == 'Физра':
        predm = 'fizra'
    elif us.predmet == "ОБЖ":
        predm = 'obj'
    else:
        predm = 'fizra'
    print(predm)
    clas = reqeust.POST['clas']
    goodUsers = Users.objects.filter(clas=clas)
    arr = []
    arrJur = []
    maxx = 0
    for elem in goodUsers:
        a = elem.user_info
        jurr = Jurnal.objects.filter(user=a, predmet=us.predmet)
        arr.append(jurr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arrJur.append(arr[i][j])
    table = 2
    return render(reqeust, 'mainn.html', {'allUs': allUs, 'table': table, 'us': us, "clas": clas, 'predmm': predm, 'goodUsers': goodUsers, 'arrJur': arrJur})

def jur(request):
    table = 4
    user = request.user
    us = Users.objects.get(user_info=user)
    return render(request, 'mainn.html', {'table': table, 'us': us})


def addJurnal(request):
    user = request.user
    us = Users.objects.get(user_info=user)
    fio = request.POST['addJurFio']
    date = request.POST['addJurDate']
    clas = request.POST['addJurClas']
    num = request.POST['addJurNum']
    try:
        userss = Users.objects.get(FIO=fio, clas=clas)
    except:
        userss = None
    table = 4
    if userss is not None:
        jur = Jurnal()
        jur.predmet = us.predmet
        jur.date = date
        jur.num = int(num)
        jur.user = userss.user_info
        jur.save()
        return render(request, 'mainn.html', {'table': table, 'us': us})
    else:
        addJur = True
        return render(request, 'mainn.html', {'addJur': addJur, 'us': us, 'table': table})

def jurnalAdd(request):
    addJur = True
    user = request.user
    us = Users.objects.get(user_info=user)
    table = 4
    allUs = Users.objects.all()
    return render(request, 'mainn.html', {'addJur': addJur, 'us': us, 'table': table, 'allUs': allUs})

def changeJurnal(request):
    counter = request.POST['counter']
    user = request.user
    us = Users.objects.get(user_info=user)
    arrUsers = []
    if us.predmet == 'Математика':
        arrMat = []
        for i in range(int(counter)+1):
            arrMat.append([])
            counterChild = request.POST[f'counterChildMat{i}']
            for j in range(int(counterChild)+1):
                try:
                    arrMat[i].append(request.POST[f'mat{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'usermat{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrMat[i][j])
                jur[j].save()

    elif us.predmet == 'Русский':
        arrRus = []
        for i in range(int(counter) + 1):
            arrRus.append([])
            counterChild = request.POST[f'counterChildRus{i}']
            for j in range(int(counterChild) + 1):
                try:
                    arrRus[i].append(request.POST[f'rus{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'userrus{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrRus[i][j])
                jur[j].save()
    elif us.predmet == 'Биология':
        arrBio = []
        for i in range(int(counter) + 1):
            arrBio.append([])
            counterChild = request.POST[f'counterChildBio{i}']
            for j in range(int(counterChild) + 1):
                try:
                    arrBio[i].append(request.POST[f'bio{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'userbio{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrBio[i][j])
                jur[j].save()
    elif us.predmet == 'Химия':
        arrHim = []
        for i in range(int(counter) + 1):
            arrHim.append([])
            counterChild = request.POST[f'counterChildHim{i}']
            for j in range(int(counterChild) + 1):
                try:
                    arrHim[i].append(request.POST[f'him{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'userhim{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrHim[i][j])
                jur[j].save()
    elif us.predmet == 'Физра':
        arrFizra = []
        for i in range(int(counter) + 1):
            arrFizra.append([])
            counterChild = request.POST[f'counterChildFizra{i}']
            for j in range(int(counterChild) + 1):
                try:
                    arrFizra[i].append(request.POST[f'fizra{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'userfizra{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrFizra[i][j])
                jur[j].save()
    elif us.predmet == "ОБЖ":
        arrObj = []
        for i in range(int(counter) + 1):
            arrObj.append([])
            counterChild = request.POST[f'counterChildObj{i}']
            for j in range(int(counterChild) + 1):
                try:
                    arrObj[i].append(request.POST[f'obj{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'userobj{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrObj[i][j])
                jur[j].save()
    else:
        arrFizika = []
        for i in range(int(counter) + 1):
            arrFizika.append([])
            counterChild = request.POST[f'counterChildFizika{i}']
            for j in range(int(counterChild) + 1):
                try:
                    arrFizika[i].append(request.POST[f'fizika{i}{j}'])
                except:
                    pass
            arrUsers.append(request.POST[f'userfizika{i}'])
        for i in range(len(arrUsers)):
            pupilUs = User.objects.get(username=arrUsers[i])
            jur = Jurnal.objects.filter(user=pupilUs, predmet=us.predmet)
            for j in range(len(jur)):
                jur[j].num = int(arrFizika[i][j])
                jur[j].save()
    table = 4
    return render(request, 'mainn.html', {'table': table, 'us': us})

def changeRasp(request):
    allUs = Users.objects.all()
    user = request.user
    us = Users.objects.get(user_info=user)
    arrPredm = []
    arrDz = []
    arrTopic = []
    day = request.POST['dayraspp']
    clas = request.POST['clas']
    for i in range(7):
        if us.userStatus == 'Методист':
            try:
                arrPredm.append(request.POST[f'pr{i+1}'])
            except:
                arrPredm.append('0')
        else:
            try:
                arrDz.append(request.POST[f'dz{i + 1}'])
                arrTopic.append((request.POST[f'topic{i+1}']))
            except:
                arrDz.append('0')
                arrTopic.append('0')
    try:
        rasp = timetable.objects.get(date=day, clas=clas)
    except:
        rasp = timetable()
    if us.userStatus == 'Методист':
        if arrPredm[0] != '0':
            rasp.predmet1 = arrPredm[0]
        if arrPredm[1] != '0':
            rasp.predmet2 = arrPredm[1]
        if arrPredm[2] != '0':
            rasp.predmet3 = arrPredm[2]
        if arrPredm[3] != '0':
            rasp.predmet4 = arrPredm[3]
        if arrPredm[4] != '0':
            rasp.predmet5 = arrPredm[4]
        if arrPredm[5] != '0':
            rasp.predmet6 = arrPredm[5]
        if arrPredm[6] != '0':
            rasp.predmet7 = arrPredm[6]
    else:
        if arrDz[0] != '0':
            rasp.dz1 = arrDz[0]
        if arrDz[1] != '0':
            rasp.dz2 = arrDz[1]
        if arrDz[2] != '0':
            rasp.dz3 = arrDz[2]
        if arrDz[3] != '0':
            rasp.dz4 = arrDz[3]
        if arrDz[4] != '0':
            rasp.dz5 = arrDz[4]
        if arrDz[5] != '0':
            rasp.dz6 = arrDz[5]
        if arrDz[6] != '0':
            rasp.dz7 = arrDz[6]

        if arrTopic[0] != '0':
            rasp.topic1 = arrTopic[0]
        if arrTopic[1] != '0':
            rasp.topic2 = arrTopic[1]
        if arrTopic[2] != '0':
            rasp.topic3 = arrTopic[2]
        if arrTopic[3] != '0':
            rasp.topic4 = arrTopic[3]
        if arrTopic[4] != '0':
            rasp.topic5 = arrTopic[4]
        if arrTopic[5] != '0':
            rasp.topic6 = arrTopic[5]
        if arrTopic[6] != '0':
            rasp.topic7 = arrTopic[6]
    rasp.date = day
    rasp.clas = clas
    rasp.save()
    print(rasp.date)
    table = 3
    user = request.user
    us = Users.objects.get(user_info=user)
    return render(request, 'mainn.html', {'table': table, 'us': us})

lastclas = ''
lastdate = ''

def raspNextDay(request):

    d = request.POST['date']
    user = request.user
    us = Users.objects.get(user_info=user)
    allUs = Users.objects.all()
    allInfo = False
    table = 1
    global lastdate
    if d != '':
        lastdate = d
    if us.userStatus == 'Ученик':
        try:
            try:
                dd = datetime.datetime.strptime(d, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(d, "%Y-%m-%d")
            dd += datetime.timedelta(days=1)
            date = dd.strftime("%Y-%m-%d")
        except:
            try:
                dd = datetime.datetime.strptime(lastdate, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            dd += datetime.timedelta(days=1)
            date = dd.strftime("%Y-%m-%d")
            lastdate = date
            lastdate = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            lastdate = lastdate.strftime("%B %d, %Y")

        try:
            raspp = timetable.objects.get(clas=us.clas, date=date)
        except:
            raspp = {}
    else:
        if us.userStatus == 'Методист':
            table = 6
        global lastclas
        clas = request.POST['clas']
        if clas != '':
            lastclas = clas
        if clas == '':
            clas = lastclas
        print(f'lclas {lastclas}')
        print(f'clas {clas}')
        try:
            try:
                dd = datetime.datetime.strptime(d, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(d, "%Y-%m-%d")
            dd += datetime.timedelta(days=1)
            date = dd.strftime("%Y-%m-%d")
        except:
            try:
                dd = datetime.datetime.strptime(lastdate, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            dd += datetime.timedelta(days=1)
            date = dd.strftime("%Y-%m-%d")
            lastdate = date
            lastdate = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            lastdate = lastdate.strftime("%B %d, %Y")

        print(date)
        try:
            raspp = timetable.objects.get(clas=clas, date=date)
        except:
            raspp = {}
    try:
        predm = {"p1": raspp.predmet1, 'p2': raspp.predmet2, 'p3': raspp.predmet3, 'p4': raspp.predmet4, 'p5': raspp.predmet5, 'p6': raspp.predmet6, 'p7': raspp.predmet7}
        dz = {"d1": raspp.dz1, 'd2': raspp.dz2, 'd3': raspp.dz3, 'd4': raspp.dz4,
             'd5': raspp.dz5, 'd6': raspp.dz6, 'd7': raspp.dz7}
    except:
        predm = {}
        dz = {}
    return render(request, 'mainn.html',
                  {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, "raspp": raspp, 'predm': predm,
                   'dz': dz, 'd': date})

def raspPrevDay(request):
    d = request.POST['date']
    user = request.user
    us = Users.objects.get(user_info=user)
    allUs = Users.objects.all()
    allInfo = False
    table = 1
    global lastdate
    if d != '':
        lastdate = d
    if us.userStatus == 'Ученик':
        try:
            try:
                dd = datetime.datetime.strptime(d, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(d, "%Y-%m-%d")
            dd += datetime.timedelta(days=-1)
            date = dd.strftime("%Y-%m-%d")
        except:
            try:
                dd = datetime.datetime.strptime(lastdate, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            dd += datetime.timedelta(days=-1)
            date = dd.strftime("%Y-%m-%d")
            lastdate = date
            lastdate = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            lastdate = lastdate.strftime("%B %d, %Y")

        try:
            raspp = timetable.objects.get(clas=us.clas, date=date)
            date = lastdate
        except:
            raspp = {}
    else:
        if us.userStatus == 'Методист':
            table = 6
        global lastclas
        clas = request.POST['clas']
        if clas != '':
            lastclas = clas
        if clas == '':
            clas = lastclas
        print(f'lclas {lastclas}')
        print(f'clas {clas}')
        try:
            try:
                dd = datetime.datetime.strptime(d, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(d, "%Y-%m-%d")
            dd += datetime.timedelta(days=-1)
            date = dd.strftime("%Y-%m-%d")
        except:
            try:
                dd = datetime.datetime.strptime(lastdate, "%B %d, %Y")
            except:
                dd = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            dd += datetime.timedelta(days=-1)
            date = dd.strftime("%Y-%m-%d")
            lastdate = date
            lastdate = datetime.datetime.strptime(lastdate, "%Y-%m-%d")
            lastdate = lastdate.strftime("%B %d, %Y")

        print(date)
        try:
            raspp = timetable.objects.get(clas=clas, date=date)
        except:
            raspp = {}
    try:
        predm = {"p1": raspp.predmet1, 'p2': raspp.predmet2, 'p3': raspp.predmet3, 'p4': raspp.predmet4,
                 'p5': raspp.predmet5, 'p6': raspp.predmet6, 'p7': raspp.predmet7}
        dz = {"d1": raspp.dz1, 'd2': raspp.dz2, 'd3': raspp.dz3, 'd4': raspp.dz4,
              'd5': raspp.dz5, 'd6': raspp.dz6, 'd7': raspp.dz7}
    except:
        predm = {}
        dz = {}
    return render(request, 'mainn.html',
                  {'allUs': allUs, 'allInfo': allInfo, 'table': table, 'us': us, "raspp": raspp, 'predm': predm,
                   'dz': dz, 'd': date})

def progress(request):
    table = 33
    user = request.user
    us = Users.objects.get(user_info=user)
    allUs = Users.objects.all()
    return render(request, 'mainn.html', {'table': table, 'us': us, 'allUs': allUs})

def progressStudent(request):
    fio = request.POST['fio']
    print(f'fio = {fio}')
    us = Users.objects.get(FIO=fio)
    print(f'us = {us}')
    allUs = Users.objects.all()
    allJur = Jurnal.objects.filter(user=us.user_info)
    print(f'jur = {allJur}')
    return render(request, 'progress.html', {'us': us, 'allUs': allUs, 'allJur':allJur})