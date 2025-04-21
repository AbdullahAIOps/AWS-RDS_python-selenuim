from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pymysql
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

input_user = driver.find_element(By.ID,'username')
input_user.send_keys("student")

input_pass = driver.find_element(By.ID,'password')
input_pass.send_keys("Password123")

button = driver.find_element(By.ID,"submit")
button.click()

conn = pymysql.connect(
    host="database-1.cm9w6oi4ek28.us-east-1.rds.amazonaws.com",
    user="admin",
    password="mianarshan123",
    database="test_db_1"
)
time.sleep(5)
courser = conn.cursor()

creating_table=("""CREATE TABLE IF NOT EXISTS submision_form(
               id INT AUTO_INCREMENT PRIMARY KEY,
               username VARCHAR(255),
               password VARCHAR(255)
               )
               """)

courser.execute(creating_table)

sql = """ INSERT INTO submision_form(username,password) VALUES (%s,%s)"""
values = ("student","Password123")

courser.execute(sql,values)

conn.commit()
