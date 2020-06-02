from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def send_message(receiver,message):
    element_presence(By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]',30)
    receiver_element = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
    receiver_element.send_keys(receiver)
    receiver_element.send_keys("\n")
    element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
    msg_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(message)
    msg_box.send_keys('\n')
    
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com/")

message  = "Assalamualaikum <receiver>, Taqaballallah wa minna waminkum, minal aidzin wal faizin. Mohon maaf lahir batin."
with open('receiver.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        send_message(row[0], message.replace("<receiver>",row[1]))