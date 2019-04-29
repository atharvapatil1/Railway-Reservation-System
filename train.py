import os
import pickle
import random
import time
global name
def pass_details():
    name=str(input("Enter your name"))
    fstat=str(input("from:"))
    tstat=str(input("to:"))
    doj=str(input("date of journey"))
    gender=str(input("M?/F/O"))
    #generating random pnr number and file names
    a=("pnr"+name)

    f=open(a+".dat","w")
 #writing passenger details to different files
    print (">>>>>>>>>>>>>>TICKET RESERVED<<<<<<<<<<<<<<<<")
    c=random.randint(10000,99999)
    print ("your pnr number is ",c)
    f.write(name)
    f.write('\n')
    f.write(fstat)
    f.write('\n')
    f.write(tstat)
    f.write('\n')
    f.write(doj)
    f.write('\n')
    f.write(gender)
    f.write('\n')
    f.close()

def display_passdetails():
 z=str(input("ENTER YOUR NAME:"))
 x=int(input("ENTER PNR NUMBER:"))
 ra=random.randint(1,99)
 f2=open(r'pnr'+z+'.dat',"r")
 str1=f2.readline()
 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ONE FOR ALL RAILWAY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 print("                           ARRIVAL TIME:11:55      DEPARTURE TIME:14:23                       ")
 print("         Seat Number:",ra)
 print("          Class:2ac")
 print("Name:",str1)
 str2=f2.readline()
 print("Journey From Station:",str2)
 str3=f2.readline()
 print("To Station:",str3)
 str4=f2.readline()
 print("DATE OF JOURNEY:",str4)
 str5=f2.readline()
 print("GENDER:",str5)


 print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HAPPY JOURNEY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


 def intro():
  print("\n\n\tONE FOR ALL RAILWAY")
  print("\n\tRESERVATION SYSTEM")
 intro()
 time.sleep(0)
while True:

 print("_________________________________________________________________________________________")
 print("MAIN MENU\n1. Passengers booking\n2.Passengers reserved ticket details\n3.EXIT\n")
 ch=int(input("Enter Your Choice(1~3):"))
 if ch==1:
  pass_details()
 elif ch==2:
  display_passdetails()
 elif ch==3:
  break


 else:
  print("Input Correct Choice(1~3)")
  int(input("\n\n\n\n\n\nTHANK YOU\n\nPress Any Key To Exit...."))
print("end")
