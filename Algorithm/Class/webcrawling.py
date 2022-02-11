from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

print("아침/점심/저녁 중 하나를 선택하여 주세요.\n")
menu = input()
m = datetime.today().month
y = datetime.today().day  

if (menu == "아침"):
    menu = "breakfast"
elif (menu == "점심"):
    menu = "lunch"
elif (menu == "저녁"):
    menu = "dinner"

html = urlopen('http://school.gyo6.net/gbsw/food/2021/'+  str(m) + '/' + str(y) + '/' + str(menu) +'')
bsObject = BeautifulSoup(html, "html.parser")

print (bsObject.body.div)
print (m)
print (y)