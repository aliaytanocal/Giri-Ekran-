import tkinter as tk
from tkinter import *


def submitact():
     
    user = Username.get()
    passw = password.get()
  
    print(f"Girilen isim {user} {passw}")
  
    logintodb(user, passw)



root = tk.Tk()
root.geometry("300x300")
root.title("Giriş Ekranı")
root.configure(bg="Green")


lblfrstrow = tk.Label(root, text ="Kullanıcı Adı -", )
lblfrstrow.place(x = 50, y = 20)
 
kullanıcıadı = tk.Entry(root, width = 35)
kullanıcıadı.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Parola-")
lblsecrow.place(x = 50, y = 50)
 
parola = tk.Entry(root, width = 35)
parola.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Giriş",
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()
