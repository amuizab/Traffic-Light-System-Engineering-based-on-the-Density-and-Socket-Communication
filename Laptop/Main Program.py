import os
import sys
import optparse
import pickle
import time

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


from sumolib import checkBinary  
import traci


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

def sensor(sensor):
    if traci.inductionloop.getLastStepOccupancy(sensor) <= 20 : x = 0
    elif traci.inductionloop.getLastStepOccupancy(sensor) <= 40 : x = 1
    elif traci.inductionloop.getLastStepOccupancy(sensor) <= 60 : x = 2
    elif traci.inductionloop.getLastStepOccupancy(sensor) <= 80 : x = 3
    else : x = 4

    if sensor == "A11" :
        A11 = x
        return A11
    elif sensor == "B11" :
        B11 = x
        return B11
    elif sensor == "B12" :
        B12 = x
        return B12
    elif sensor == "B13" :
        B13 = x
        return B13
    elif sensor == "B14" :
        B14 = x
        return B14
    elif sensor == "B15" :
        B15 = x
        return B15
    elif sensor == "B16" :
        B16 = x
        return B16
    elif sensor == "C11" :
        C11 = x
        return C11
    elif sensor == "C12" :
        C12 = x
        return C12
    elif sensor == "C13" :
        C13 = x
        return C13
    elif sensor == "D11" :
        D11 = x
        return D11
    elif sensor == "D12" :
        D12 = x
        return D12
    elif sensor == "D13" :
        D13 = x
        return D13
    elif sensor == "D14" :
        D14 = x
        return D14
    elif sensor == "D15" :
        D15 = x
        return D15
    elif sensor == "D16" :
        D16 = x
        return D16
    elif sensor == "D21" :
        D21 = x
        return D21
    elif sensor == "D22" :
        D22 = x
        return D22
    elif sensor == "D23" :
        D23 = x
        return D23
    elif sensor == "D24" :
        D24 = x
        return D24
    elif sensor == "D25" :
        D25 = x
        return D25
    elif sensor == "D26" :
        D26 = x
        return D26
    elif sensor == "E11" :
        E11 = x
        return E11
    elif sensor == "E12" :
        E12 = x
        return E12
    elif sensor == "E13" :
        E13 = x
        return E13
    elif sensor == "E14" :
        E14 = x
        return E14
    elif sensor == "E15" :
        E15 = x
        return E15
    elif sensor == "E16" :
        E16 = x
        return E16
    elif sensor == "F11" :
        F11 = x
        return F11
    elif sensor == "F12" :
        F12 = x
        return F12
    elif sensor == "F13" :
        F13 = x
        return F13
    elif sensor == "F14" :
        F14 = x
        return F14
    elif sensor == "F15" :
        F15 = x
        return F15
    elif sensor == "F16" :
        F16 = x
        return F16

def lampuTL(jalan, kode):
    if jalan == "gneJ2" :
        ah = 0
        am = 1
        bh = 0
        bm = 1
        ch = 0
        cm = 1
        d1h = 0
        d1m = 1

        if kode[:1] == "a" :
            ah = 1
            am = 0
        elif kode[:1] == "b" :
            bh = 1
            bm = 0
        elif kode[:1] == "c" :
            ch = 1
            cm = 0
        elif kode[:1] == "d" :
            d1h = 1
            d1m = 0
        else :
            ah = 0
            am = 1
            bh = 0
            bm = 1
            ch = 0
            cm = 1
            d1h = 0
            d1m = 1
        
        traci.trafficlight.setProgram("gneJ2", kode)
        print("berhasil mengganti lampu persimpangan 1")
        return ah,am,bh,bm,ch,cm,d1h,d1m
        
    if jalan == "gneJ1" :
        d2h = 0
        d2m = 1
        eh = 0
        em = 1
        fh = 0
        fm = 1
        gh = 0
        gm = 1

        if kode[:1] == "s" :
            d2h = 1
            d2m = 0
        elif kode[:1] == "e" :
            eh = 1
            em = 0
        elif kode[:1] == "f" :
            fh = 1
            fm = 0
        elif kode[:1] == "g" :
            gh = 1
            gm = 0
        else :
            d2h = 0
            d2m = 1
            eh = 0
            em = 1
            fh = 0
            fm = 1
            gh = 0
            gm = 1
        
        traci.trafficlight.setProgram("gneJ1", kode)
        print("berhasil mengganti lampu persimpangan 2")
        return d2h,d2m,eh,em,fh,fm,gh,gm

def send():
    data = [ah,am,bh,bm,ch,cm,d1h,d1m,d2h,d2m,eh,em,fh,fm,gh,gm,A11,B11,B12,B13,B14,B15,B16,C11,C12,C13,D11,D12,D13,D14,D15,D16,D21,D22,D23,D24,D25,D26,E11,E12,E13,F11,F12,F13,F14,F15,F16,G11]
    bytedata = bytes(data)
    conn.send(bytedata)

'''def sendSensor():
    dataSensor = [A11,B11,B12,B13,B14,B15,B16,C11,C12,C13,D11,D12,D13,D14,D15,D16,D21,D22,D23,D24,D25,D26,E11,E12,E13,F11,F12,F13,F14,F15,F16,G11]
    bytedataSensor = bytes(dataSensor)
    conn.send()'''

def recv():
    bytedatar = conn.recv(1024)
    datar = bytedatar.decode('utf-8')
    return datar

if __name__ == "__main__":
    options = get_options()

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "1502.main.cfg.txt" ])
    step = 0
    step2 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    step3 = 100
    step4 = 100
    step5 = 100
    step6 = 100
    def numb(elem):
        return elem[-2:]

    
    
    while step < 100:
        traci.simulationStep()
                
#pembacaan sensor
        print("step now:", step2)
        print("-----target step:", step4)
        print("-----target step 2:", step6)
        #if step2==step5:

        if traci.inductionloop.getLastStepOccupancy("A11") >= 50 : A11 = 1
        else : A11 = 0
        #A11 = sensor("A11")
        B11 = sensor("B11")
        B12 = sensor("B12")
        B13 = sensor("B13")
        B14 = sensor("B14")
        B15 = sensor("B15")
        B16 = sensor("B16")

        C11 = sensor("C11")
        C12 = sensor("C12")
        C13 = sensor("C13")

        D11 = sensor("D11")
        D12 = sensor("D12")
        D13 = sensor("D13")
        D14 = sensor("D14")
        D15 = sensor("D15")
        D16 = sensor("D16")

        D21 = sensor("D21")
        D22 = sensor("D22")
        D23 = sensor("D23")
        D24 = sensor("D24")
        D25 = sensor("D25")
        D26 = sensor("D26")

        E11 = sensor("E11")
        E12 = sensor("E12")
        E13 = sensor("E13")

        F11 = sensor("F11")
        F12 = sensor("F12")
        F13 = sensor("F13")
        F14 = sensor("F14")
        F15 = sensor("F15")
        F16 = sensor("F16")

        if traci.inductionloop.getLastStepOccupancy("G11") >= 50 : G11 = 1
        else : G11 = 0


        if step2==0 :
            start = time.time()
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2","b30")
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1","s30")
            #print('ini waktunya disini')
            send()
            print("data lampu TL telah terkirim")
            end=time.time()
            print(end-start)

        if step2==30 :
            start = time.time()
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2","c30")
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1","e30")
            #print('ini waktunya disini')
            send()
            print("data lampu TL telah terkirim")
            end=time.time()
            print(end-start)

        if step2==60 :
            start = time.time()
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2","d30")
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1","f30")
            #print('ini waktunya disini')
            send()
            print("data lampu TL telah terkirim")
            end=time.time()
            print(end-start)
            
        if step2==90 :
            start = time.time()
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2","a10")
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1","g10")
            #print('ini waktunya disini')
            send()
            print("data lampu TL telah terkirim")
            end=time.time()
            print(end-start)

        
        if step2==step3 :
            recv()
            start = time.time()
            send()
            print("----------------------------------")
            print("data sensor terbaru telah terkirim - persimpangan 1")
            datar = recv()
            print("data prediksi telah diterima - persimpangan 1")


            pertama = datar[0:3]
            kedua = datar[3:6]
            ketiga = datar[6:9]
            keempat = datar[9:12]

            print([pertama, kedua, ketiga, keempat])
            
            picknum1 = pertama[-2:]
            num1 = int(picknum1)
            picknum2 = kedua[-2:]
            num2 = int(picknum2)
            picknum3 = ketiga[-2:]
            num3 = int(picknum3)
            picknum4 = keempat[-2:]
            num4 = int(picknum4)
        
            print("match1")
            step4 = step3+num1
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2", pertama)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)

        if step2==step3+num1 :
            start = time.time()
            print("match2")
            step4 = step3+num1+num2
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2", kedua)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)
        if step2==step3+num1+num2 :
            start = time.time()
            print("match3")
            step4 = step3+num1+num2+num3
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2", ketiga)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)
        if step2==step3+num1+num2+num3 :
            start = time.time()
            print("match4")
            ah,am,bh,bm,ch,cm,d1h,d1m = lampuTL("gneJ2", keempat)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)
            totalnum = num1+num2+num3+num4
            step4 = step3+totalnum
            step3 = step4


        if step2==step5 :
            recv()
            start = time.time()
            send()
            print("----------------------------------")
            print("data sensor terbaru telah terkirim - persimpangan 2")
            datar = recv()
            print("data prediksi telah diterima - persimpangan 2")


            kelima = datar[12:15]
            keenam = datar[15:18]
            ketujuh = datar[18:21]
            kedelapan = datar[21:24]

            print([kelima, keenam, ketujuh, kedelapan])
            
            picknum5 = kelima[-2:]
            num5 = int(picknum5)
            picknum6 = keenam[-2:]
            num6 = int(picknum6)
            picknum7 = ketujuh[-2:]
            num7 = int(picknum7)
            picknum8 = kedelapan[-2:]
            num8 = int(picknum8)
            
        
            print("match5")
            step6 = step5+num5
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1", kelima)
            #print('ini waktunya disini')
            send()
            print("data lampu TL telah terkirim")
            end=time.time()
            print(end-start)
        if step2==step5+num5 :
            start = time.time()
            print("match6")
            step6 = step5+num5+num6
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1", keenam)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)
        if step2==step5+num5+num6 :
            start = time.time()
            print("match7")
            step6 = step5+num5+num6+num7
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1", ketujuh)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)
        if step2==step5+num5+num6+num7 :
            start = time.time()
            print("match8")
            d2h,d2m,eh,em,fh,fm,gh,gm = lampuTL("gneJ1", kedelapan)
            send()
            print("data lampu TL telah terkirim")
            end = time.time()
            print(end-start)
            totalnum2 = num5+num6+num7+num8
            step6 = step5+totalnum2
            step5 = step6       
              
        step2 +=1
