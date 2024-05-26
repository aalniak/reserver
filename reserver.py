import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter.font import Font
from datetime import datetime
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import ctypes  # An included library with Python install.   
import sys


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.chrome.options import Options


root2 = tk.Tk()
root2.title("Blank Form Template")
root2.geometry("1000x600")
res1 = "baraka 7 salı"
res2 = "baraka 6 perşembe"
res3 = "baraka 4 paazartesi"
res4 = "baraka 12 cumartesi"
res5 = "baraka 5 cuma"
options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
] 

clicked = StringVar() 
clicked.set( "Choose the day" ) 
def callback(selection):
    global current_day
    current_day = selection
drop = OptionMenu( root2 , clicked , *options, command=callback ) 
drop.place(relx=0.10,rely=0.80)


options = [ 
    "9.30-11.30", 
    "12.00-13.30", 
    "14.00-15.30", 
    "16.00-17.30", 
    "18.00-19.30", 
    "19.30-21.00"
    
] 
clicked = StringVar() 
clicked.set( "Choose the time" )

def callback(selection):
    global current_time
    current_time = selection

drop = OptionMenu( root2 , clicked , *options, command=callback ) 
drop.place(relx=0.25,rely=0.80)


options = [ 
    "tekno",
    "baraka"  
] 

clicked = StringVar() 
clicked.set( "Choose the place" )
 

def callback(selection):
    global current_place
    current_place = selection
drop = OptionMenu( root2 , clicked , *options, command=callback ) 
drop.place(relx=0.40,rely=0.80)

# Add your widgets here
click_number = 0
current_place=""
current_day = ""
current_time = ""
session0 = 2
session1 = 0
session2 = 0

def attainVars():
    global session0, session1, session2
    if current_place == "baraka":
        session0 = 0
    elif current_place == "tekno":
        session0 = 1
    
    if current_day == "Monday":
        session1 =1
    elif current_day == "Tuesday":
        session1 = 2
    elif current_day == "Wednesday":
        session1 = 3
    elif current_day == "Wednesday":
        session1 = 4
    elif current_day == "Friday":
        session1 = 5
    elif current_day == "Saturday":
        session1 = 6
    
    if current_time == "9.30-11.30":
        session2 = 1
    elif current_time == "12.00-13.30":
        session2 = 2
    elif current_time == "14.00-15.30":
        session2 = 3
    elif current_time == "16.00-17.30":
        session2 = 4
    elif current_time == "18.00-19.30":
        session2 = 5
    elif current_time == "19.30-21.00":
        session2 = 6
    
        
# ( salon 0 baraka 1 tekno , gün 1 pzt 6 cmt , saat 1 9.30 6 19.30)
session_list = [(7,7,7),(7,7,7),(7,7,7),(7,7,7),(7,7,7)]

'''
def editList1():
    global session0, session1, session2
    attainVars()
    session_list[0] = (session0,session1,session2)

def editList2():
    global session0, session1, session2
    attainVars()
    session_list[0] = (session0,session1,session2)

def editList3():
    global session0, session1, session2
    attainVars()
    session_list[0] = (session0,session1,session2)

def editList4():
    global session0, session1, session2
    attainVars()
    session_list[0] = (session0,session1,session2)

def editList5():
    global session0, session1, session2
    attainVars()
    session_list[0] = (session0,session1,session2)
'''



def addSession1():
    global session0, session1, session2
    attainVars()
    session_list[0] = (session0,session1,session2)
    current_selection = current_day + " " + current_time
    Status.config(text = "Seans 1:" +current_selection)
    print(session_list)

def addSession2():
    global session0, session1, session2
    attainVars()
    session_list[1] = (session0,session1,session2)
    current_selection = current_day + " " + current_time
    Status2.config(text = "Seans 2:" +current_selection)

def addSession3():
    global session0, session1, session2
    attainVars()
    session_list[2] = (session0,session1,session2)
    current_selection = current_day + " " + current_time
    Status3.config(text = "Seans 3:" + current_selection)

def addSession4():
    global session0, session1, session2
    attainVars()
    session_list[3] = (session0,session1,session2)
    current_selection = current_day + " " + current_time
    Status4.config(text = "Seans 4:" + current_selection)

def addSession5():
    global session0, session1, session2
    attainVars()
    session_list[4] = (session0,session1,session2)
    current_selection = current_day + " " + current_time
    Status5.config(text = "Seans 4:" + current_selection)

def clearSession1():
    session_list[0] = (7,7,7)
    Status.config(text = "Seans 1:")

def clearSession2():
    session_list[1] = (7,7,7)
    Status2.config(text = "Seans 2:")

def clearSession3():
    session_list[2] = (7,7,7)
    Status3.config(text = "Seans 3:")

def clearSession4():
    session_list[3] = (7,7,7)
    Status4.config(text = "Seans 4:")

def clearSession5():
    session_list[4] = (7,7,7)
    Status5.config(text = "Seans 5:")





Status = tk.Label(root2,text="Seans 1:" +res1)
Status.place(relx=0.75,rely=0.7)
Status2 = tk.Label(root2,text="Seans 2: "+res2)
Status2.place(relx=0.75,rely=0.75)
Status3 = tk.Label(root2,text="Seans 3: "+res3)
Status3.place(relx=0.75,rely=0.8)
Status4 = tk.Label(root2,text="Seans 4: "+res4)
Status4.place(relx=0.75,rely=0.85)
Status5 = tk.Label(root2,text="Seans 5: "+res5)
Status5.place(relx=0.75,rely=0.90)



Button1 = tk.Button(root2, text= "+", command=addSession1)
Button1.place(relx=0.71,rely=0.7)
Button2 = tk.Button(root2, text= "+", command=addSession2)
Button2.place(relx=0.71,rely=0.75)
Button3 = tk.Button(root2, text= "+", command=addSession3)
Button3.place(relx=0.71,rely=0.8)
Button4 = tk.Button(root2, text= "+", command=addSession4)
Button4.place(relx=0.71,rely=0.85)
Button5 = tk.Button(root2, text= "+", command=addSession5)
Button5.place(relx=0.71,rely=0.9)

cButton1 = tk.Button(root2, text= "-", command=clearSession1)
cButton1.place(relx=0.68,rely=0.7)
cButton2 = tk.Button(root2, text= "-", command=clearSession2)
cButton2.place(relx=0.68,rely=0.75)
cButton3 = tk.Button(root2, text= "-", command=clearSession3)
cButton3.place(relx=0.68,rely=0.8)
cButton4 = tk.Button(root2, text= "-", command=clearSession4)
cButton4.place(relx=0.68,rely=0.85)
cButton5 = tk.Button(root2, text= "-", command=clearSession5)
cButton5.place(relx=0.68,rely=0.9)
no_of_ops = 0


def startBot():
    options = Options()
    options.add_argument("--window-size=600x400")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    actual_list = []
    items_list = []
    drivers_list = []
    solver_list = []
    data_list = []
    global no_of_ops
    for k in session_list:
        if k != (7,7,7):
            no_of_ops += 1
            actual_list.append(k)
    if no_of_ops == 0:
        tkMessageBox.showinfo(title="Wait", message="You don't have any active session added????")
    else:
        
        driver1 = webdriver.Chrome('C:/chromedriver', options=options)
        drivers_list.append(driver1)
        solver1 = RecaptchaSolver(driver=driver1)
        solver_list.append(solver1)
        items_list.append([driver1,solver1])
        data1 = actual_list[-1]
        data_list.append(data1)
        actual_list.pop(-1)
        no_of_ops -=1
        
        if no_of_ops != 0:
            driver2 = webdriver.Chrome('C:/chromedriver', options=options)
            drivers_list.append(driver2)
            solver2 = RecaptchaSolver(driver=driver2)
            solver_list.append(solver2)
            items_list.append([driver2,solver2])
            data2 = actual_list[-1]
            data_list.append(data2)
            actual_list.pop(-1)
            no_of_ops -=1
        else:
            pass
        if no_of_ops != 0:
            driver3 = webdriver.Chrome('C:/chromedriver', options=options)
            drivers_list.append(driver3)
            solver3 = RecaptchaSolver(driver=driver3)
            solver_list.append(solver3)
            items_list.append([driver3,solver3])
            data3 = actual_list[-1]
            data_list.append(data3)
            actual_list.pop(-1)
            no_of_ops -=1
        else:
            pass
        if no_of_ops != 0:
            driver4 = webdriver.Chrome('C:/chromedriver', options=options)
            drivers_list.append(driver4)
            solver4 = RecaptchaSolver(driver=driver4)
            solver_list.append(solver4)
            items_list.append([driver4,solver4])
            data4 = actual_list[-1]
            data_list.append(data4)
            actual_list.pop(-1)
            no_of_ops -=1
        else:
            pass
        if no_of_ops != 0:
            driver5 = webdriver.Chrome('C:/chromedriver', options=options)
            drivers_list.append(driver5)
            solver5 = RecaptchaSolver(driver=driver5)
            solver_list.append(solver5)
            items_list.append([driver5,solver5])
            data5 = actual_list[-1]
            data_list.append(data5)
            actual_list.pop(-1)
            no_of_ops -=1
        else:
            pass
        
        for k in drivers_list:
            login(k)
        for i in range(0,5):
            reserveSession(data_list[i][0],data_list[i][1],data_list[i][2],drivers_list[i],solver_list[i])
                    
        
        
        
        
        
        
       # login(driver)
       # reserveSession(data[0],data[1],data[2],driver,solver)
        
        
        

def login(driver):
    driver.get("https://rez.metu.edu.tr")
    time.sleep(1)
    username = driver.find_element(By.NAME,"j_idt23:user")
    password = driver.find_element(By.NAME,"j_idt23:password")
    username.send_keys('e244239')
    password.send_keys('Pi**3141')
    driver.find_element(By.NAME,'j_idt23:j_idt46').click()
    time.sleep(1)
#Day 1 Monday -> Day 7 Sunday
#Time 1 9.30 -> Time 6 -> 19.30
def reserveSession(sports_centre,day,daytime,driver,solver):
    if sports_centre == 0:
        centre_index = 10
    elif (sports_centre == 1):
        centre_index = 22
    
    modified_xpath = '/html/body/section/div[2]/div/div[2]/div[2]/form/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td['+str(day+1)+']/div/div[2]/a['+str(daytime)+']'
    
    select = Select(driver.find_element(By.XPATH,'/html/body/section/div[2]/div/div[2]/div[2]/form/select'))
    select.select_by_index(centre_index)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/section/div[2]/div/div[2]/div[2]/form/div[2]/div/div[1]/div[2]/div/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,modified_xpath).click()
    time.sleep(6)
    recaptcha_iframe = driver.find_element(By.XPATH,'/html/body/section/div[2]/div/form[2]/fieldset/div/div[5]/div/div/div/div/iframe')
    #try:
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)  
    #except:
    driver.find_element(By.XPATH,'/html/body/section/div[2]/div/form[2]/fieldset/div/div[7]/div/div/div[2]').click()
    driver.find_element(By.XPATH,'/html/body/section/div[2]/div/form[2]/fieldset/div/div[8]/div/div/div[2]').click()
    time.sleep(1)
    print("qwe")
        #driver.find_element(By.XPATH,'/html/body/section/div[2]/div/form[2]/div/button').click()
            

startButton = tk.Button(root2, text="Start", command=startBot)
startButton.place(relx=10,y=10)






image = PhotoImage(file="hg.png")
hourglass1 = tk.Label(root2, image=image)
hourglass1.place(relx=0.73,rely=0.7)


hourglass2 = tk.Label(root2, image=image)
hourglass2.place(relx=0.73,rely=0.75)


hourglass3 = tk.Label(root2, image=image)
hourglass3.place(relx=0.73,rely=0.8)


hourglass4 = tk.Label(root2, image=image)
hourglass4.place(relx=0.73,rely=0.85)


hourglass5 = tk.Label(root2, image=image)
hourglass5.place(relx=0.73,rely=0.9)





root2.mainloop()

