from tkinter import *



def submit():
    sum=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get())
    subtotal.set(sum)

    
    gst=int(net.get())*18/100
    gstbill.set(gst)


    grandtotal=sum+gst
    finalbill.set(grandtotal)    


    billing=billno1.get()
    billno2.set(billing)

    name=name1.get()
    name2.set(name)

    age=age1.get()
    age2.set(age)

    phone=phone1.get()
    phone2.set(phone)

    place=place1.get()
    place2.set(place)

    doctor=doctor1.get()
    doctor2.set(doctor)

    date=date1.get()
    date2.set(date)


bill=Tk()
subtotal=StringVar()
gstbill=StringVar()
finalbill=StringVar()


bill.title('Billing Form')
bill.config(bg='#ECF5F2')
bill.geometry('1580x900')

menu=StringVar()

billno1=StringVar()
billno2=StringVar()
name1=StringVar()
name2=StringVar()
age1=StringVar()
age2=StringVar()
phone1=StringVar()
phone2=StringVar()
place1=StringVar()
place2=StringVar()
doctor1=StringVar()
doctor2=StringVar()
date1=StringVar()
date2=StringVar()


Label(bill,text="BABU'S MEDICAL STORE",font='times 20 bold',bg='#ECF5F2',fg="black",relief=GROOVE,bd=8).grid(row=0,column=3)
Label(bill,text='Near post office, Chandappadi,\nPonnani-679577 Phone: 9876543210',font='times 17',bg='#ECF5F2').grid(row=1,column=3)
Label(bill,text='---------------------------------------',font='times 17',bg='#ECF5F2').grid(row=2,column=3)

Label(bill,text='   ',font='times 12',bg='#ECF5F2').grid(row=3,column=0)
Label(bill,text='   ',font='times 12',bg='#ECF5F2').grid(row=4,column=0)
Label(bill,text='   ',font='times 12',bg='#ECF5F2').grid(row=5,column=0)
Label(bill,text='   ',font='times 12',bg='#ECF5F2').grid(row=6,column=0)


Label(bill,text='BILL NO: ',font='times 10',bg='#ECF5F2').grid(row=3,column=1)
Entry(bill,textvariable=billno1).grid(row=3,column=2)
Label(bill,text='NAME: ',font='times 10',bg='#ECF5F2').grid(row=4,column=1)
Entry(bill,textvariable=name1).grid(row=4,column=2)
Label(bill,text='AGE: ',font='times 10',bg='#ECF5F2').grid(row=5,column=1)
Entry(bill,textvariable=age1).grid(row=5,column=2)
Label(bill,text='PHONE: ',font='times 10',bg='#ECF5F2').grid(row=6,column=1)
Entry(bill,textvariable=phone1).grid(row=6,column=2)
Label(bill,text='PLACE: ',font='times 10',bg='#ECF5F2').grid(row=3,column=4)
Entry(bill,textvariable=place1).grid(row=3,column=5)
Label(bill,text='   ',font='times 12',bg='#ECF5F2').grid(row=4,column=5)
Label(bill,text='Consulting Doctor: ',font='times 12',bg='#ECF5F2').grid(row=5,column=4)
Entry(bill,textvariable=doctor1).grid(row=5,column=5)
Label(bill,text='Date: ',font='times 11',bg='#ECF5F2').grid(row=6,column=4)
Entry(bill,textvariable=date1).grid(row=6,column=5)

Label(bill,text='   ',font='times 12',bg='#ECF5F2').grid(row=7)

Label(bill,text='Sl.No',font='times 11',bg='#ECF5F2').grid(row=8,column=1)
Label(bill,text='----',font='times 11',bg='#ECF5F2').grid(row=9,column=1)
Label(bill,text='Medicines',font='times 11',bg='#ECF5F2').grid(row=8,column=2)
Label(bill,text='--------',font='times 11',bg='#ECF5F2').grid(row=9,column=2)
Label(bill,text='Quantity',font='times 11',bg='#ECF5F2').grid(row=8,column=3)
Label(bill,text='--------',font='times 11',bg='#ECF5F2').grid(row=9,column=3)
Label(bill,text='Unit Price',font='times 11',bg='#ECF5F2').grid(row=8,column=4)
Label(bill,text='----',font='times 11',bg='#ECF5F2').grid(row=9,column=4)
Label(bill,text='Net Amount',font='times 11',bg='#ECF5F2').grid(row=8,column=5)
Label(bill,text='----------',font='times 11',bg='#ECF5F2').grid(row=9,column=5)

Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=10,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=10,column=1)


menu.set('Select the medicine')
drop=OptionMenu(bill,menu,'Aciclovir (Zovirax)','Acrivastine','Adalimumab','Alendronic acid','Allopurinol','Alogliptin','Amitriptyline','Amitriptyline','Amlodipine','Amoxicillin','Anastrozole','Apixaban','Aspirin','Aspirin','Atenolol','Atorvastatin','Azathioprine','Azithromycin').grid(row=10,column=2)



Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=11,column=0)

Entry(bill).grid(row=12,column=1)
Entry(bill).grid(row=12,column=2)
Entry(bill).grid(row=12,column=3)
Entry(bill).grid(row=12,column=4)
e1=Entry(bill)
e1.grid(row=12,column=5)

Entry(bill).grid(row=13,column=1)
Entry(bill).grid(row=13,column=2)
Entry(bill).grid(row=13,column=3)
Entry(bill).grid(row=13,column=4)
e2=Entry(bill)
e2.grid(row=13,column=5)

Entry(bill).grid(row=14,column=1)
Entry(bill).grid(row=14,column=2)
Entry(bill).grid(row=14,column=3)
Entry(bill).grid(row=14,column=4)
e3=Entry(bill)
e3.grid(row=14,column=5)

Entry(bill).grid(row=15,column=1)
Entry(bill).grid(row=15,column=2)
Entry(bill).grid(row=15,column=3)
Entry(bill).grid(row=15,column=4)
e4=Entry(bill)
e4.grid(row=15,column=5)

Entry(bill).grid(row=16,column=1)
Entry(bill).grid(row=16,column=2)
Entry(bill).grid(row=16,column=3)
Entry(bill).grid(row=16,column=4)
e5=Entry(bill)
e5.grid(row=16,column=5)


Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=17,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=18,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=18,column=1)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=18,column=2)
Label(bill,text='Total: ',font='times 13',bg='#ECF5F2').grid(row=18,column=4)
net=Entry(bill,textvariable=subtotal)
net.grid(row=18,column=5)

Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=19,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=19,column=1)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=19,column=2)
Label(bill,text='GST (%): ',font='times 10',bg='#ECF5F2').grid(row=19,column=4)
gstax=Entry(bill,text='',textvariable=gstbill)
gstax.grid(row=19,column=5)

Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=20,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=20,column=1)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=20,column=2)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=20,column=4)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=20,column=5)

Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=21,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=21,column=1)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=21,column=2)
Label(bill,text='GRAND TOTAL : ',font='times 13',bg='#ECF5F2').grid(row=21,column=4)
Label(bill,text='',textvariable=finalbill,font='times 18',bg='#ECF5F2').grid(row=21,column=5)

Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=22,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=23,column=0)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=23,column=1)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=23,column=2)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=23,column=3)
Label(bill,text='',font='times 12',bg='#ECF5F2').grid(row=23,column=4)
btn=Button(bill,text='Print bill',font='times 10',command=submit).grid(row=23,column=5)


f=Frame(bill,width='600',height='850',bg='#87CEFA').place(x=950,y=20)
Label(f,text="BABU'S MEDICAL STORE",font='times 20 bold',bg='#87CEFA',fg="black",relief=GROOVE,bd=8).place(x=1080,y=30)
Label(f,text='Near post office, Chandappadi,\nPonnani-679577 Phone: 9876543210',font='times 15',bg='#87CEFA').place(x=1105,y=80)
Label(f,text='--------------------------------',font='times 17',bg='#87CEFA').place(x=1125,y=125)
Label(f,text='BILL NO: ',font='times 12',bg='#87CEFA').place(x=980,y=160)
Label(f,text='NAME: ',font='times 12',bg='#87CEFA').place(x=980,y=185)
Label(f,text='AGE: ',font='times 12',bg='#87CEFA').place(x=980,y=210)
Label(f,text='PHONE: ',font='times 12',bg='#87CEFA').place(x=980,y=235)
Label(f,text='PLACE: ',font='times 11',bg='#87CEFA').place(x=1300,y=165)
Label(f,text='Consulting Doctor: ',font='times 12',bg='#87CEFA').place(x=1300,y=190)
Label(f,text='Date: ',font='times 13',bg='#87CEFA').place(x=1300,y=215)
Label(f,text='---------------------------------------------------------------------------------------------------',font='times 13',bg='#87CEFA').place(x=950,y=260)
Label(f,text='Sl No.',font='times 11',bg='#87CEFA').place(x=990,y=310)
Label(f,text='-----',font='times 11',bg='#87CEFA').place(x=995,y=330)
Label(f,text='Medicine',font='times 11',bg='#87CEFA').place(x=1070,y=310)
Label(f,text='-------',font='times 11',bg='#87CEFA').place(x=1080,y=330)
Label(f,text='Quantity',font='times 11',bg='#87CEFA').place(x=1180,y=310)
Label(f,text='-------',font='times 11',bg='#87CEFA').place(x=1190,y=330)
Label(f,text='Unit Price',font='times 11',bg='#87CEFA').place(x=1290,y=310)
Label(f,text='---------',font='times 11',bg='#87CEFA').place(x=1295,y=330)
Label(f,text='Net Amount',font='times 11',bg='#87CEFA').place(x=1400,y=310)
Label(f,text='------------',font='times 11',bg='#87CEFA').place(x=1405,y=330)

Entry(f,textvariable=billno2).place(x=1060,y=163)
Entry(f,textvariable=name2).place(x=1060,y=188)
Entry(f,textvariable=age2).place(x=1060,y=213)
Entry(f,textvariable=phone2).place(x=1060,y=238)
Entry(f,textvariable=place2).place(x=1420,y=168)
Entry(f,textvariable=doctor2).place(x=1420,y=193)
Entry(f,textvariable=date2).place(x=1420,y=218)



bill.mainloop()
