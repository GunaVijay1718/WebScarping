from bs4 import BeautifulSoup
import requests 
import csv

myWeb = requests.get('https://www.tutorialspoint.com/java/index.htm').text
soup = BeautifulSoup(myWeb, 'lxml') 
header=['S.No','Heading','Topic.No','Topic','Link']
file_name="javaguna_ws_project.csv"
with open (file_name,"w") as f:
    write=csv.writer(f)
    write.writerow(header)
    chapter=soup.find_all('ul',class_="toc chapters")
    count=0
    for i in chapter:
        li=i.find_all('li')
        for index, title in enumerate(li):
            if index==0:
                main_heading=title.text
                continue
