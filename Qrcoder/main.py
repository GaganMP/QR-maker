import qrcode
from tkinter import *
root=Tk()

xi=''
def genQR():
    xi=li.get()
    Qrs=qrcode.QRCode(version='1',box_size='10',border="12")
    Qrs.add_data(xi)
    Qrs.make(fit=True)
    imgs=Qrs.make_image(fill_color="black",back_color="white")
    imgs.save("Qs.png")
    print(xi)
    ld=Label(root,image='./QR.png')
    ld.pack()
   

root.geometry("700x350")
l1=Label(root,text="Create QR code",background="white",padx='20',pady='5',width='20',height='5',font='15',foreground="blue").pack()
l2=Label(root,text="Enter the link you need to enter",pady=30).pack()
li=Entry(root)
li.pack()



l3=Label(root,text=xi,pady=30).pack()

b1=Button(root,text="Get QR" ,command=genQR)
b1.pack()


root.mainloop()







