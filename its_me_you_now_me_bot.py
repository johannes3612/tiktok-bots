from selenium import webdriver
from os import system, name

from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title MADE BY its_me_you_now_me')
print("[+] Jan Bukun. [its_me_you_now_me]")
print("[+] Jan Bukun.")
print(pyfiglet.figlet_format("Jan Bukun", font="slant"))
print("1. Viewbot.\n2. Heartbot.\n3. Followerbot.")

auto = int(input("Mode: "))

if auto == 1 or auto == 2 or auto == 3 or auto == 4:
    print("[+] video voor likes of naam voor volgers")
    vidUrl = input("TikTok video URL OR name: ")

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1(): # Update the title IF option 1 was picked.
    global Views
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title MADE BY its_me_you_now_me ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

def title2(): # Update the title IF option 2 was picked.
    global Hearts
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title MADE BY its_me_you_now_me ^| Hearts Sent: {beautify(Hearts)} ^| Elapsed Time: {time_elapsed}')

def title3(): # Update the title IF option 3 was picked.
    global Followers
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title MADE BY its_me_you_now_me ^| Followers Sent: {beautify(Followers)} ^| Elapsed Time: {time_elapsed}')


    
def loop1():
    global Views
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop1()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div[1]/h5/button[2]").click()
        
        driver.refresh()
        Views += 1
        print("[+] Views sended!")
        
        sleep(60)
        loop1()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop1()

def loop2():
    global Hearts
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop2()
        
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="searchinput"]').send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath('//*[@id="form1"]/div/div/button').click()
        
        sleep(5)
        driver.find_element_by_xpath('//*[@id="msg"]/div/div/div[1]/h5/button[1]').click()
        
        sleep(6)
        hearts = driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/div').text.split()
        
        
        Hearts += 1
        print("[+] Hearts sended!")
        
        sleep(5)
        driver.refresh()
        
        sleep(60)
        loop2()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop2()

def loop3():
    global Followers
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop3()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/button").click()
        sleep(25)
        folls = driver.find_element_by_xpath('//*[@id="bootstrap-show-modal-1"]/div/div/div[2]/text()').text.split()
        
        Followers += 1
        print("[+] Followers sended!")
        driver.refresh()
        
        sleep(60)
        loop3()
        
    except:
        print("[-] An error occured. Retrying..")
        driver.refresh()
        loop3()

clear()

print(pyfiglet.figlet_format("Jan Bukun", font="slant"))
print("Log:")

if auto == 1:
    driver.get("https://homedecoratione.com/")
    
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    
    a.start()
    b.start()
    
elif auto == 2:
    driver.get("https://homedecoratione.com/")
    
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    
    a.start()
    b.start()
    
elif auto == 3:
    driver.get("https://homedecoratione.com/")
    
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    
    a.start()
    b.start()
    
elif auto == 4:
    driver.get("https://homedecoratione.com/")
    
    a = threading.Thread(target=title4)
    b = threading.Thread(target=loop4)
    
    a.start()
    b.start()
    
elif auto == 5:
    print("[+] MADE BY its_me_you_now_me. [jan Bukun]")
    print("[+] MADE BY its_me_you_now_me.")
    
else:
    print(f"{auto} is not a valid option. Please pick 1, 2, 3,")
