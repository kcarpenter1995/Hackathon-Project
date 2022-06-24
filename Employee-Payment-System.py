root = Tk()
root.title("Employee Payment System")
root.geometry('1370x720+0+0')
root.maxsize(width=1370, height=720)
root.minsize(width=1370, height=720)
root.configure(background="dark gray")

Tops = Frame(root, width=1350, height=50, bd=8, bg="dark blue")
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=600, bd=8, bg="dark gray")
f1.pack(side=LEFT)
f2 = Frame(root, width=300, height=700, bd=8, bg="dark blue")
f2.pack(side=RIGHT)

fla = Frame(f1, width=600, height=200, bd=8, bg="dark blue")
fla.pack(side=TOP)
flb = Frame(f1, width=300, height=600, bd=8, bg="dark blue")
flb.pack(side=TOP)

lbl_information = Label(Tops, font=('arial', 45, 'bold'), text="Employee Payment Management System ", relief=GROOVE, bd=10, bg="Dark Gray", fg="Black")
lbl_information.grid(row=0, column=0)