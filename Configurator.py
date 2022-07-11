# Importing Libraries
import serial
import time
import subprocess


#OPen the Serial Port
ser = serial.Serial(port='COM12', baudrate=38400, timeout=.1)

def printParams(axis_no):
    #Motor Accel
    print("Motor Acceleration:\r")
    ser.write(axis_no.encode())
    ser.write(b"A\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Baud Rate
    print("Baud Rate:\r")
    ser.write(axis_no.encode())
    ser.write(b"B\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Direction Flag
    ser.write(axis_no.encode())
    print("Direction Flag:\r")
    ser.write(b"C\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Encoder Counts
    print("Encoder Counts:\r")
    ser.write(axis_no.encode())
    ser.write(b"E\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Hold Current
    print("Hold Current:\r")
    ser.write(axis_no.encode())
    ser.write(b"H\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Init Load
    print("Initialization Load:\r")
    ser.write(axis_no.encode())
    ser.write(b"I\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Output 1 CFG
    print("Out 1 CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"J\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Output 2 CFG
    print("Out 2 CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"K\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Load - Running
    print("Run Load:\r")
    ser.write(axis_no.encode())
    ser.write(b"L\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Motor Resolution
    print("Motor Resolution:\r")
    ser.write(axis_no.encode())
    ser.write(b"M\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Current Scale
    print("Current Scale:\r")
    ser.write(axis_no.encode())
    ser.write(b"O\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Product Code
    print("Full Step Morphing:\r")
    ser.write(axis_no.encode())
    ser.write(b"P\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Run Current
    print("Run Current:\r")
    ser.write(axis_no.encode())
    ser.write(b"R\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Motor Velocity/Max Speed
    print("Motor MAX Speed:\r")
    ser.write(axis_no.encode())
    ser.write(b"S\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Input 1 CFG
    print("Input 1 CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"T\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Input 2 CFG
    print("Input 2 CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"U\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Input 3 CFG
    print("Input 3 CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"V\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Input 4 CFG
    print("Input 4 CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"W\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Index CFG
    print("Index CFG:\r")
    ser.write(axis_no.encode())
    ser.write(b"Z\r")
    #time.sleep(.1)
    value = ser.readline()
    print(value.decode('Ascii'))
    #Print FW REV
    ser.write(axis_no.encode())
    ser.write(b"z\r")
    value = ser.readline()
    print(value.decode('Ascii'))


def loadDefaults(axis_no):
    #Motor Accel
    ser.write(axis_no.encode())
    ser.write(b"A5000\r")
    time.sleep(.1)    
    #Baud Rate
    ser.write(axis_no.encode())
    ser.write(b"B2\r")
    time.sleep(.1)
    #Direction Flag
    ser.write(axis_no.encode())
    ser.write(b"C0\r")
    time.sleep(.1)     
    #Encoder Counts
    ser.write(axis_no.encode())
    ser.write(b"E800\r")
    time.sleep(.1)     
    #Hold Current
    ser.write(axis_no.encode())
    ser.write(b"H2\r")
    time.sleep(.1)       
    #Init Load
    ser.write(axis_no.encode())
    ser.write(b"I32\r")
    time.sleep(.1)      
    #Output 1 CFG
    ser.write(axis_no.encode())
    ser.write(b"J1\r")
    time.sleep(.1)      
    #Output 2 CFG
    ser.write(axis_no.encode())
    ser.write(b"K2\r")
    time.sleep(.1)      
    #Load - Running
    ser.write(axis_no.encode())
    ser.write(b"L12800\r")
    time.sleep(.1)     
    #Motor Resolution
    ser.write(axis_no.encode())
    ser.write(b"M256\r")
    time.sleep(.1)       
    #Current Scale
    ser.write(axis_no.encode())
    ser.write(b"O1\r")
    time.sleep(.1)      
    #Product Code
    ser.write(axis_no.encode())
    ser.write(b"P6\r")
    time.sleep(.1)    
    #Run Current
    ser.write(axis_no.encode())
    ser.write(b"R16\r")
    time.sleep(.1)    
    #Motor Velocity/Max Speed
    ser.write(axis_no.encode())
    ser.write(b"S10000\r")
    time.sleep(.1)    
    #Input 1 CFG
    ser.write(axis_no.encode())
    ser.write(b"T3\r")
    time.sleep(.1)    
    #Input 2 CFG
    ser.write(axis_no.encode())
    ser.write(b"U3\r")
    time.sleep(.1)    
    #Input 3 CFG
    ser.write(axis_no.encode())
    ser.write(b"V3\r")
    time.sleep(.1)    
    #Input 4 CFG
    ser.write(axis_no.encode())
    ser.write(b"W3\r")
    time.sleep(.1)    
    #Index CFG
    ser.write(axis_no.encode())
    ser.write(b"Z1\r")
    time.sleep(.1)    

#Save the defaults
def saveDefaults(axis_no):
        ser.write(axis_no.encode())
        ser.write(b"Q\r")
        #time.sleep(.1)
        value = ser.readline()
        print(value.decode('Ascii'))
        tmp_value = value.decode('Ascii')
        if(tmp_value[2] == '>'):
            print("Success! NVM Saved...\r")
        elif(tmp_value[2] == '!'):
            print("Something went wrong...No NVM update saved.")

#Change the address
def changeAddr(axis_no):
        ser.write(axis_no.encode())
        #Send the unlock code
        ser.write(b"k\r")
        time.sleep(.1)
        value = ser.readline()
        tmp_value = value.decode('Ascii')
        print(tmp_value)
        print("\r")
        print(list(tmp_value))
        print("\r")
        if((tmp_value[3] == ">") and (tmp_value[4] == ">")):
            print("Address unlocked...\r")
            invalue = input("Enter new address: ")
            serVal = axis_no + "D" + invalue + "\r"
            print(list(serVal))
            ser.write(serVal.encode())            

#Load New Firmware
def loadCode(axis_no):
        print("New Firmware Load...\r")
        print("btl_host.py must be in this same directory.\r")
        print("New firmware should be named C2B.bin and be in this same directory.\r")
        serVal = ":0X" + axis_no + "\r"
        print(list(serVal))
        ser.write(serVal.encode())
        ser.close()
        result = subprocess.run(['python', 'btl_host.py', '-v','-r38400', '-iCOM12', '-fC2B.bin', '-dPIC32CM', '-a0x800'], capture_output=True, encoding='UTF-8')
        print(result.stdout)
        print(result.stderr)        
        #exit()        
    
while True:    
    print("Use the following Commands to read/write NVM Parameters:\r")
    print("Type read to Read flash contents:\r")
    print("Type done to exit:\r")
    print("Type defaults to load defaults:\r")
    print("Type save to Save defaults:\r")
    print("Type add to change address of axis:\r")
    print("Type fw to upload new firmware:\r")
    #Get the axis number first
    usrInput = input("Type AXIS number to begin:\r")
    #print(list(usrInput))
    axis_no = ":" + usrInput
    print(list(axis_no))
    print("Type Command: \r")
    usrInput = input()
    if(usrInput == "read"):
        printParams(axis_no)
    elif(usrInput == "defaults"):
        loadDefaults(axis_no)
    elif(usrInput == "save"):
        saveDefaults(axis_no)
    elif(usrInput == "add"):
        changeAddr(axis_no)
    elif(usrInput == "fw"):
        axis_no = input("Type in Axis Number to Load FW: \r")        
        loadCode(axis_no)
    elif(usrInput == "done"):
        #Close the Serial port
        ser.close()
        exit()
        
