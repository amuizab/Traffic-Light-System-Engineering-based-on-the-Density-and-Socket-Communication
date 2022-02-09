import os
import sys
import optparse

import pandas

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


def run():
    step = 0
    step2 = 0
    w = 0
    df = pandas.DataFrame([""]*100)
    while step < 100:
        traci.simulationStep()
                
        
        A11 = traci.inductionloop.getLastStepOccupancy("A11")

        B11 = traci.inductionloop.getLastStepOccupancy("B11")
        B12 = traci.inductionloop.getLastStepOccupancy("B12")
        B13 = traci.inductionloop.getLastStepOccupancy("B13")
        B14 = traci.inductionloop.getLastStepOccupancy("B14")
        B15 = traci.inductionloop.getLastStepOccupancy("B15")
        B16 = traci.inductionloop.getLastStepOccupancy("B16")
        
        C11 = traci.inductionloop.getLastStepOccupancy("C11")
        C12 = traci.inductionloop.getLastStepOccupancy("C12")
        C13 = traci.inductionloop.getLastStepOccupancy("C13")
            
        D11 = traci.inductionloop.getLastStepOccupancy("D11")
        D12 = traci.inductionloop.getLastStepOccupancy("D12")
        D13 = traci.inductionloop.getLastStepOccupancy("D13")
        D14 = traci.inductionloop.getLastStepOccupancy("D14")
        D15 = traci.inductionloop.getLastStepOccupancy("D15")
        D16 = traci.inductionloop.getLastStepOccupancy("D16")

        D21 = traci.inductionloop.getLastStepOccupancy("D21")
        D22 = traci.inductionloop.getLastStepOccupancy("D22")
        D23 = traci.inductionloop.getLastStepOccupancy("D23")
        D24 = traci.inductionloop.getLastStepOccupancy("D24")
        D25 = traci.inductionloop.getLastStepOccupancy("D25")
        D26 = traci.inductionloop.getLastStepOccupancy("D26")

        E11 = traci.inductionloop.getLastStepOccupancy("E11")
        E12 = traci.inductionloop.getLastStepOccupancy("E12")
        E13 = traci.inductionloop.getLastStepOccupancy("E13")
        
        F11 = traci.inductionloop.getLastStepOccupancy("F11")
        F12 = traci.inductionloop.getLastStepOccupancy("F12")
        F13 = traci.inductionloop.getLastStepOccupancy("F13")
        F14 = traci.inductionloop.getLastStepOccupancy("F14")
        F15 = traci.inductionloop.getLastStepOccupancy("F15")
        F16 = traci.inductionloop.getLastStepOccupancy("F16")

        G11 = traci.inductionloop.getLastStepOccupancy("G11")
        
        
        #ruasa1 = A11
        #ruasb1 = B11,B12,B13,B14,B15,B16
        #ruasc1 = C11,C12,C13
        #ruasd1 = D11,D12,D13,D14,D15,D16
        #ruasd2 = D21,D22,D23,D24,D25,D26
        #ruase1 = E11,E12,E13
        #ruasf1 = F11,F12,F13,F14,F15,F16
        ruasg1 = G11

        #df.loc[w] = [ruasa1]
        #df.loc[w] = [ruasb1]
        #df.loc[w] = [ruasc1]
        #df.loc[w] = [ruasd1]
        #df.loc[w] = [ruasd2]
        #df.loc[w] = [ruase1]
        #df.loc[w] = [ruasf1]
        df.loc[w] = [ruasg1]

        df.to_csv('ruasg1.csv')
        step2 +=1
        w +=1
        #if step2 == 10 and a1 == 100 and a2 == 100 and a3 == 100 : a = 7
        #elif step2 == 10 and a1 == 100 and a2 == 100 and a3 == 0 : a = 3
        #elif step2 == 10 and a1 == 100 and a2 == 0 and a3 == 0 : a = 1
        #elif step2 == 10 and a1 == 0 and a2 == 0 and a3 == 0 : a = 0

        #if step2 == 10 and b1 == 100 and b2 == 100 and b3 == 100 : b = 7
        #elif step2 == 10 and b1 == 100 and b2 == 100 and b3 == 0 : b = 3
        #elif step2 == 10 and b1 == 100 and b2 == 0 and b3 == 0 : b = 1
        #elif step2 == 10 and b1 == 0 and b2 == 0 and b3 == 0 : b = 0

        #if step2 == 10 and c1 == 100 and c2 == 100 and c3 == 100 : c = 7
        #elif step2 == 10 and c1 == 100 and c2 == 100 and c3 == 0 : c = 3
        #elif step2 == 10 and c1 == 100 and c2 == 0 and c3 == 0 : c = 1
        #elif step2 == 10 and c1 == 0 and c2 == 0 and c3 == 0 : c = 0

        print("###########################")
        print(step2)
        print("Ruas 1 - 0 :"), print(E11)
        print("Ruas 2 - 0 :"), print(E12)
        print("Ruas 3 - 0 :"), print(E13)
        #print("Ruas 4 - 1 :"), print(B14)
        #print("Ruas 5 - 1 :"), print(B15)
        #print("Ruas 6 - 1 :"), print(B16)
    



if __name__ == "__main__":
    options = get_options()

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "1502.main.cfg.txt" ])
    run()
