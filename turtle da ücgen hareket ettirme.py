                                #turtle da  hareket ettirme

import turtle

panel=turtle.Screen()  #panel oluşturma
panel.screensize(800,800)  # panele boyut verme işlemi 
panel.bgcolor("gray")  # panele renk verme
panel.title("hareket")  #panelin adı

hareketci=turtle.Turtle()  #  hareket olacak olan turle  nesnesi oluşturma
hareketci.color("green")  # turtle  nesnesine renk verme
hareketci.shape("turtle")  # turtle  şeklini belirlem işlemi
hareketci.shapesize(3)   #turtle boyutunu belirleme
hareketci.up()     #cizme işlemini durdurma 

def soladön():
    hareketci.left(90)  # sola dönme fonksiyonu

def sağadön():
    hareketci.right(90)     # sağa dönme fonksiyonu


panel.listen()
panel.onkey(soladön,'Left')   # key tuşları kullanma metotları
panel.onkey(sağadön,'Right')

# while döngüsü ile turtle hareket ettirma işlemi
while True:
    hareketci.forward(3)
    if hareketci.xcor()>450:   # eğer paneli  kenarına gelirse turtle 180 derece dönecek
        hareketci.right(180)
    elif hareketci.xcor()<-450:
        hareketci.left(180)  
    if hareketci.ycor()>400:
        hareketci.right(180)
    elif hareketci.ycor()<-400:
        hareketci.left(180)  







turtle.done()






