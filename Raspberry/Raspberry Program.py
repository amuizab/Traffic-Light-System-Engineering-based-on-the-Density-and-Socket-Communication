import socket
import numpy
import pickle
import RPi.GPIO as GPIO
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.15', 12345))
GPIO.setmode(GPIO.BCM)

def defaultA():
    ah = 0
    am = 1
    bh = 0
    bm = 1
    ch = 0
    cm = 1
    d1h = 0
    d1m = 1
    return ah,am,bh,bm,ch,cm,d1h,d1m

def defaultB():
    d2h = 0
    d2m = 1
    eh = 0
    em = 1
    fh = 0
    fm = 1
    gh = 0
    gm = 1
    return d2h,d2m,eh,em,fh,fm,gh,gm


def nyalainLampuTL(): 
    GPIO.output(23,am)
    GPIO.output(24,ah)
    GPIO.output(25,bm)
    GPIO.output(8,bh)
    GPIO.output(7,cm)
    GPIO.output(1,ch)
    GPIO.output(20,d1m)
    GPIO.output(21,d1h)

    GPIO.output(26,gh)
    GPIO.output(19,gm)
    GPIO.output(6,fh)
    GPIO.output(5,fm)
    GPIO.output(27,eh)
    GPIO.output(17,em)
    GPIO.output(12,d2h)
    GPIO.output(4,d2m)

def recv():
    bytedatar = s.recv(1024)
    print(bytedatar)
    bytearraydatar = bytearray(bytedatar)
    datarecv = numpy.array(bytearraydatar)
    print(datarecv)
    return datarecv


def preSorting():

    if predictiona == 1 : aa = "a30"
    else : aa = "a10"
    
    if predictionb == 30 : bb = "b10"
    elif predictionb == 31 : bb = "b30"
    elif predictionb == 32 : bb = "b60"
    elif predictionb == 33 : bb = "b90"
    elif predictionb == 20 : bb = "b10"
    elif predictionb == 21 : bb = "b23"
    elif predictionb == 22 : bb = "b45"
    elif predictionb == 23 : bb = "b68"
    elif predictionb == 10 : bb = "b10"
    elif predictionb == 11 : bb = "b15"
    elif predictionb == 12 : bb = "b30"
    elif predictionb == 13 : bb = "b45"
    elif predictionb == 0 : bb = "b10"
    elif predictionb == 1 : bb = "b10"
    elif predictionb == 2 : bb = "b10"
    else : bb = "b10"
 
    if predictionc == 30 : cc = "c10"
    elif predictionc == 31 : cc = "c30"
    elif predictionc == 32 : cc = "c60"
    elif predictionc == 33 : cc = "c90"
    elif predictionc == 20 : cc = "c10"
    elif predictionc == 21 : cc = "c23"
    elif predictionc == 22 : cc = "c45"
    elif predictionc == 23 : cc = "c68"
    elif predictionc == 10 : cc = "c10"
    elif predictionc == 11 : cc = "c15"
    elif predictionc == 12 : cc = "c30"
    elif predictionc == 13 : cc = "c45"
    elif predictionc == 0 : cc = "c10"
    elif predictionc == 1 : cc = "c10"
    elif predictionc == 2 : cc = "c10"
    else : cc = "c10"
            
    if predictiond1 == 1 : dd1 = "d130"
    elif predictiond1 == 2 : dd1 = "d160"
    elif predictiond1 == 3 : dd1 = "d190"
    else : dd1 = "d110"

    if predictiond2 == 1 : dd2 = "d230"
    elif predictiond2 == 2 : dd2 = "d260"
    elif predictiond2 == 3 : dd2 = "d290"
    else : dd2 = "d210"
            
    if predictione == 30 : ee = "e10"
    elif predictione == 31 : ee = "e30"
    elif predictione == 32 : ee = "e60"
    elif predictione == 33 : ee = "e90"
    elif predictione == 20 : ee = "e10"
    elif predictione == 21 : ee = "e23"
    elif predictione == 22 : ee = "e45"
    elif predictione == 23 : ee = "e68"
    elif predictione == 10 : ee = "e10"
    elif predictione == 11 : ee = "e15"
    elif predictione == 12 : ee = "e30"
    elif predictione == 13 : ee = "e45"
    elif predictione == 0 : ee = "e10"
    elif predictione == 1 : ee = "e10"
    elif predictione == 2 : ee = "e10"
    else : ee = "e10"
            
    if predictionf == 30 : ff = "f10"
    elif predictionf == 31 : ff = "f30"
    elif predictionf == 32 : ff = "f60"
    elif predictionf == 33 : ff = "f90"
    elif predictionf == 20 : ff = "f10"
    elif predictionf == 21 : ff = "f23"
    elif predictionf == 22 : ff = "f45"
    elif predictionf == 23 : ff = "f68"
    elif predictionf == 10 : ff = "f10"
    elif predictionf == 11 : ff = "f15"
    elif predictionf == 12 : ff = "f30"
    elif predictionf == 13 : ff = "f45"
    elif predictionf == 0 : ff = "f10"
    elif predictionf == 1 : ff = "f10"
    elif predictionf == 2 : ff = "f10"
    else : ff = "f10"

    if predictiong == 1 : gg = "g30"
    else : gg = "g10"
    
    return aa,bb,cc,dd1,dd2,ee,ff,gg

def numb(elem):
        return elem[-2:]

load1 = pickle.load(open("modelruas6x6withtagclean.sav","rb"))
load2 = pickle.load(open("modelruas3x6.sav","rb"))
load3 = pickle.load(open("ruasfix.sav","rb"))

GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
    
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
step = 0
print('aman')
'''if len(dataread) == 16 : dataread = datar
else : dataread = datar2'''
while step < 100:
    datar = recv()
    '''if len(datarecv) == 16 :
        datar = datarecv
    else :
        datar = datarecv'''
  
    ah = int(datar[0])
    am = int(datar[1])
    bh = int(datar[2])
    bm = int(datar[3])
    ch = int(datar[4])
    cm = int(datar[5])
    d1h = int(datar[6])
    d1m = int(datar[7])

    d2h = int(datar[8])
    d2m = int(datar[9])
    eh = int(datar[10])
    em = int(datar[11])
    fh = int(datar[12])
    fm = int(datar[13])
    gh = int(datar[14])
    gm = int(datar[15])
    
    nyalainLampuTL()
    


    a = int(datar[16])
    b = numpy.array(datar[17:23]
    c = numpy.array(datar[23:26]
    d1 = numpy.array(datar[26:32]
    d2 = numpy.array(datar[32:38]
    e = numpy.array(datar[38:41]
    f = numpy.array(datar[41:47]
    g = int(datar[47])

    ruasb = numpy.concatenate((b,d2), axis=0)
    ruasc = numpy.concatenate((c,d2), axis=0)
    ruasd1 = d1
    ruasd2 = d2
    ruase = numpy.concatenate((e,d1)), axis=0)
    ruasf = numpy.concatenate((f,d1)), axis=0)

    predictiona = a
    predictionb = load1.predict([ruasb])
    predictionc = load2.predict([ruasc])
    predictiond1 = load3.predict([ruasd1])
    predictiond2 = load3.predict([ruasd2])
    predictione = load2.predict([ruase])
    predictionf = load1.predict([ruasf])
    predictiong = g

    print("##############New Cycle###############")
    print("####Prediction")
    print("ruas a:", predictiona)
    print("ruas b:", predictionb)
    print("ruas c:", predictionc)
    print("ruas d1:", predictiond1)
    print("##############New Cycle 2###############")
    print("ruas d2:", predictiond2)
    print("ruas e:", predictione)
    print("ruas f:", predictionf)
    print("ruas g:", predictiong)

    aa,bb,cc,dd1,dd2,ee,ff,gg = preSorting()

    sorting = [aa, bb, cc, dd1]
    sorting.sort(key=numb, reverse=True)
    print('Sorted list:', sorting)

    sorting2 = [dd2, ee, ff, gg]
    sorting2.sort(key=numb, reverse=True)
    print('Sorted list:', sorting2)

    data = sorting[0]+sorting[1]+sorting[2]+sorting[3]+sorting2[0]+sorting2[1]+sorting2[2]+sorting2[3]
    databyte = str.encode(c)
    conn.send(bytedata)
