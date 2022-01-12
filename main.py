from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep  


import find_results

username = ""

options = webdriver.ChromeOptions() 

if os.name == 'nt':
	driver = webdriver.Chrome(executable_path=(os.path.abspath(os.getcwd()) + "chromedriver.exe"), options=options)
	
else:
	try:
		driver = webdriver.Chrome(options=options) 
	except Exception as e:
		try:
			import chromedriver_binary  # Adds chromedriver binary to path
			driver = webdriver.Chrome(options=options) 
		except Exception as e:
			print(e)
			exit(1)
			
driver.get('https://www.instagram.com')
driver.implicitly_wait(5)  

sleep(5)
driver.execute_script('''document.getElementsByClassName("aOOlW  bIiDR  ")[0].click()''')

# sleep(5)

# driver.execute_script('''document.getElementsByClassName("-nal3 ")[1].click();''')

sleep(5)

print("Type your username and password. Once you type them, DO NOT press enter on the broswer.")
print("Type here anything and press enter")

random = input()

driver.execute_script('''document.getElementsByClassName("sqdOP  L3NKy   y3zKF")[0].click();''')
sleep(5)
driver.execute_script('''document.getElementsByClassName("sqdOP")[1].click();''')
sleep(6)


driver.get('https://www.instagram.com/' + username)
driver.implicitly_wait(5)  
sleep(3)

#of followers
followers_number = int(driver.execute_script('''return document.getElementsByClassName("g47SY ")[1].innerText;'''))
#of followings
following_number = int(driver.execute_script('''return document.getElementsByClassName("g47SY ")[2].innerText;'''))

print(f"To verify, you have {followers_number} followers and you follow {following_number} people") 

# click followers
driver.execute_script('''document.getElementsByClassName("-nal3 ")[1].click();''')

sleep(5)

number = followers_number
curr = int(driver.execute_script('''return document.getElementsByClassName("wo9IH").length;'''))
try:
    while True:
        current = int(driver.execute_script('''return document.getElementsByClassName("wo9IH").length;'''))
        if current >= number:
            break
        driver.execute_script('''document.getElementsByClassName("isgrP")[0].scrollTo(0,50000)''')
        print(current, number)
        sleep(1)
        if curr == current:
            current = int(driver.execute_script('''return document.getElementsByClassName("wo9IH").length;'''))
            if current >= number:
                break
            driver.execute_script('''document.getElementsByClassName("isgrP")[0].scrollTo(0,50000)''')
            sleep(1)
            if curr == current:
                break
except Exception as e:
    print(e)

sleep(5)

print("Went to the bottom of the page") 

sleep(1)
followers_obj = driver.execute_script('''return document.getElementsByClassName("wo9IH");''') 
followers = [f.text.split('\n')[0] for f in followers_obj]    
sleep(1)

driver.execute_script('''document.getElementsByClassName("-nal3 ")[2].click();''')

sleep(5)

number = following_number
curr = int(driver.execute_script('''return document.getElementsByClassName("wo9IH").length;''')) 
try:
    while True:
        current = int(driver.execute_script('''return document.getElementsByClassName("wo9IH").length;'''))
        if current >= number:
            break
        driver.execute_script('''document.getElementsByClassName("isgrP")[0].scrollTo(0,50000)''')
        print(current, number)
        sleep(1)
        if curr == current:
            current = int(driver.execute_script('''return document.getElementsByClassName("wo9IH").length;'''))
            if current >= number:
                break
            driver.execute_script('''document.getElementsByClassName("isgrP")[0].scrollTo(0,50000)''')
            sleep(1)
            if curr == current:
                break
except Exception as e:
    print(e)

sleep(5)

print("Went to the bottom of following's page")

following_obj = driver.execute_script('''return document.getElementsByClassName("wo9IH");''') 
following = [f.text.split('\n')[0] for f in following_obj]    
sleep(1)

print("Followers", followers)
print("Following", following)

print("Writing on files")

file = open("following.txt", "w+")

for f in following:
	file.write(f)	
	file.write("\n")

file.close()

file = open("followers.txt", "w+")
for f in followers:
    file.write(f + '\n')

file.close()

print("Finding differences")
find_results.find_differences()
