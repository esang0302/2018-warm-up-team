#아두이노와 라즈베리파이의 시리얼 통신을 하고
#아두이노에서 전송한 정보를 라즈베리파이에서 수신하여
#서버로 전달하고 서버에서 보내는 값을 받는다.


//서버와의 코드

import serial 
import urllib.request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
port = "/dev/ttyACM0" 

ser = serial.Serial(port, 9600) 
ser.flushInput() 
status='safe';
count=0;

try:
    GPIO.setmode(GPIO.BCM)
    input =0
    while True:
        sign = ser.readline()
        data = sign.decode('utf-8').split('\\')[0]
        print(data)
        if data == '1':
                                          status='warning'
                                          data_b = {'question_text':status}
                                          data_par = urllib.parse.urlencode(data_b).encode("utf-8")

                                          req=urllib.request.Request(url='http://222.117.181.227:8080/polls/save', data= data_par,method='PUT')
                                          
                                          response = urllib.request.urlopen(req)
                                          page = response.read()
                                          print(page)

        

        else:
                                          status='safe'
                                          data_b = {'question_text':status}
                                          data_par = urllib.parse.urlencode(data_b).encode("utf-8")

                                          req=urllib.request.Request(url='http://222.117.181.227:8080/polls/save', data= data_par,method='PUT')
                                          
##                                          url='http://220.67.124.128:8000/yun/test'
                                          response = urllib.request.urlopen(req)
                                          page = response.read()
                                          print(page)
                                                
except KeyboardInterrupt:
    GPIO.cleanup()
