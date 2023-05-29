import tkinter as tk
from tkinter import ttk
import mysql.connector

root=tk.Tk()
root.title("Dane studentow")
def fetch_data():
    mydb=mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
      )
    cursor=mydb.cursor()
    cursor.execute("SELECT*FROM student")
    wynik=cursor.fetchall()

    cursor.close()
    mydb.close()
    return wynik

def zapisz():
    noweImie = imie.get()
    noweNazwiko = nazwisko.get()
    nowyMail = mail.get()
    nowePnk = punkty.get()
    nowyIndex = index.get()

    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    cursor = mydb.cursor()
    sql = "INSERT INTO student (imie,nazwisko,mail,punkty,index) VALUES(%s,%s,%s,%s,%s)"
    elementy = (noweImie, noweNazwiko, nowyMail, nowePnk, nowyIndex)
    cursor.execute(sql, elementy)
    mydb.commit()
    cursor.close()
    mydb.close()
def usun():
    imieDoU=imie.get()
    nazwiskodoU=nazwisko.get()
    mailDU=mail.get()
    punktyDU=punkty.get()
    indexDU=index.get()
    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    cursor = mydb.cursor()
    sql="DELETE FROM student WHERE imie=%s,nazwisko=%s,mail=%s,punkty=%s,index=%s"
    elementy=(imieDoU,nazwiskodoU,mailDU,punktyDU,indexDU)
    cursor.execute(sql,elementy)
    mydb.commit()
    cursor.close()
    mydb.close()

def edytuj():
    imieZ=imie.get()
    nZ = imie.get()
    mZ = imie.get()
    pZ = imie.get()
    iZ = imie.get()

    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    cursor = mydb.cursor()
    sql = "UPDATE student SET imie=%s,nazwisko=%s,mail=%s,punkty=%s WHERE index=%s"
    elementy = (imieZ,nZ,mZ,pZ,iZ)
    cursor.execute(sql, elementy)
    mydb.commit()
    cursor.close()
    mydb.close()

