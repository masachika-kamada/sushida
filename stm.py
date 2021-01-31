import serial

readSer = serial.Serial('/dev/tty.Bluetooth-Incoming-Port',9600, timeout=3)
c = readSer.read() # 1 byte
string = readSer.read(10) # 10 byte
line = readSer.readline() # 1 line (upto '\n')
print("Read Serial:")
print(c)
print(string)
print(line)
readSer.close()