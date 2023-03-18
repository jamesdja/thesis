import serial
import time
import matplotlib.pyplot as plt

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 115200, timeout=1)
time.sleep(2)
data1 =[]
data2 = []

while True:
    data = ser.readline()
    data = data.decode("utf").rstrip("\r\n")
    data = data.split(",")
    time_stamp = time.time()
    vut_lat =       float(data[0])
    vut_long =      float(data[1])
    vut_acc_north=  float(data[2])
    vut_acc_east =  float(data[3])
    vut_acc_down =  float(data[4])
    vut_heading =   float(data[5])
    vut_cal_sys =   float(data[6])
    vut_cal_gyro =  float(data[7])
    vut_cal_acc =   float(data[8])
    vut_cal_mag =   float(data[9])
    print(time_stamp, vut_lat, vut_long, vut_heading,vut_acc_north, vut_acc_east)