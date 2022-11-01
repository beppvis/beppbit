import string


import random
from turtle import rt
from time import sleep
import os

face_def_file = open('face_def.txt',"r")
f_def = face_def_file.read()
face_m_open_file = open('face_m_open.txt','r')
f_m_open = face_m_open_file.read()

def randomise(face:string):
    rt_str = ""
    for i in face:
        if i == "#":
            n = random.choice(['o','a','2','4','#','#'])
            rt_str = rt_str + n
        else:
            rt_str = rt_str+i
    print(rt_str)
def voice():
    pass

while True:
    randomise(f_def)
    sleep(0.2)
    os.system("cls")
    randomise(f_m_open)
    sleep(0.2)
    os.system("cls")
