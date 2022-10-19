'''A Simple URl/Text Shortener With Python Tkinter(GUI)
It Can Automatically Detects The Type URL/Text And Gives A Short URL And a QR Code'''


#Importhing Required Packages
from tkinter import *
import pyshorteners
import clipboard
import requests
from random import *
import webbrowser
import qrcode
from PIL import ImageTk,Image

#Creating Main Window
root=Tk()
S=pyshorteners.Shortener()
root.title("Url Shortner")
root.geometry('800x540')
root.config(bg='Light Blue')
icon=PhotoImage(file='D:/QRCodes/Url_icon.png')
root.iconphoto(False,icon)
root.resizable(False,False)

#String Variables Declaration
Url_input=StringVar(root)
Prefix=StringVar(root)
Prefix.set('1')
Out_Url=StringVar(root)
MessageOut=StringVar(root)
allchar="abcdefghijklmnopqrstuvwxyzASDFGHJKLZXCVBNMQWERTYUIOP0123456789"

#QR Code Gerator
def GenerateQr():
	QrName="".join(choice(allchar) for x in range(8))
	qr=qrcode.make(Out_Url.get())
	qr.save('QrDump/'+QrName+'.png')
	Img=Image.open('QrDump/'+QrName+'.png')
	ResizedImg=Img.resize((190,190))
	QrImage=ImageTk.PhotoImage(ResizedImg)
	QrHolder.config(image=QrImage)
	
#Opens Link in Browser
def Open_Link():
	webbrowser.open_new(Out_Url.get())

#Text Shortner Using Cl1p.net
def Cl1p():
		headers = {'Content-Type': 'text/html; charset=UTF-8',}
		data=Url_input.get()
		clip_sufix = "".join(choice(allchar) for x in range(8))
		Cl1p_api='https://api.cl1p.net/{}'.format(clip_sufix)
		Cl1p_Url='https://cl1p.net/{}'.format(clip_sufix)
		res = requests.post(Cl1p_api, headers=headers, data=data)
		MessageOut.set('Note: Cl1p Links are for 1 Time use only')
		Out_Url.set(Cl1p_Url)

#Copy Generated Short URL to Clipboard. To Paste Press "Ctrl + V"
def Copy_Url():
	if(Out_Url.get()!=''):
	    try:
	        clipboard.copy(Out_Url.get())
	        MessageOut.set("URL copied successfully!")
	    except:
	        MessageOut.set("Something went wrong, Please try again!")
	else:
		MessageOut.set('Generate a Short Url First')

#Generates Short Url Using TinyUrl.com
def TinyUrl():

	try:
		Url=Url_input.get().strip()
		ShortUrl= S.tinyurl.short(Url)
		Out_Url.set(ShortUrl)
		MessageOut.set("Tinly Url Is Generated!")
	except:
		Url_input.delete(0, 'END')
		MessageOut.set("Enter URL Please!")

#Generates Short Url Using Is.gd
def is_gd():

	try:
		Url=Url_input.get().strip()
		ShortUrl= S.isgd.short(Url)
		Out_Url.set(ShortUrl)
		MessageOut.set("Is.gd Url Is Generated!")
	except:
		Url_input.delete(0, END)
		MessageOut.set("Enter URL Please!")

#Generates Short Url Using Chilp.it
def Chilp():

	try:
		Url=Url_input.get().strip()
		ShortUrl= S.chilpit.short(Url)
		Out_Url.set(ShortUrl)
		MessageOut.set("Chilp Url Is Generated!")
	except:
		Url_input.delete(0,END)
		MessageOut.set("Enter URL Please!")

#Generates Short Url Using Da.gd
def da_gd():

	try:
		Url=Url_input.get().strip()
		ShortUrl= S.dagd.short(Url)
		Out_Url.set(ShortUrl)
		MessageOut.set("Is.gd Url Is Generated!")
	except:
		Url_input.delete(0, END)
		MessageOut.set("Enter URL Please!")

#Shortner Domain Selector - Text or Url Detector
def Url_Shortner():

	Button(root,text='Generate QR',width=14,bg='#2c87c5',font=('Helventica','11','bold'),command=GenerateQr).grid(row=9,column=1,padx=2,pady=15,ipady=5,rowspan=2)
	Button(root,text='Copy',width=8,bg='#2c87c5',font=('Helventica','11','bold'),command=Copy_Url).grid(row=7,column=0,padx=2,pady=15,ipady=5)
	Button(root,text='Open in Browser',width=13,bg='#2c87c5',font=('Helventica','11','bold'),command=Open_Link).grid(row=7,column=4,padx=2,pady=15,ipady=5)

	Str=Url_input.get().strip()
	Strl=Str.split('.',1)
	st=Strl[0].lower()
	if('http://' in Strl[0] or 'www' == Strl[0] or 'https://www' == Strl[0] or 'https://' in Strl[0] or 'http://www' == Strl[0]):
		Op=Prefix.get()

		if(Op=='1'):
			TinyUrl()
		elif (Op=='2'):
			is_gd()
		elif (Op=='3'):
			Chilp()
		elif (Op=='4'):
			da_gd()
		else:
			Cl1p()
	else:
		Cl1p()

#SVCET Logo Placing
SVL=Image.open('SVCET_Logo.png')
SVLogo=SVL.resize((308,70))
SVCETLogo=ImageTk.PhotoImage(SVLogo)
SVCET=Label(root,bg='Light Blue',image=SVCETLogo)
SVCET.grid(row=0,column=0,columnspan=5)

Label(root,text='Url Shortner GUI',font=('times new roman','18','bold'),bg='Light Blue').grid(row=1,column=0,columnspan=5)
Label(root,text='Enter Url',font=('times new roman','17','bold'),bg='Light Blue').grid(row=2,column=0,pady=15)
Entry(root,textvariable=Url_input,width=90,borderwidth=3,bd='2').grid(row=2,column=1,padx=2,pady=15,ipady=5,columnspan=3)
Button(root,text="Shorten it",bg='#2c87c5',width=13,font=('times new roman','12','bold'),command=Url_Shortner).grid(row=2,column=4,sticky='w')

#Radio Buttons For Domain Selection
Label(root,text='Select a Domain: ',font=('Arial',11,'bold'),bg='Light Blue').grid(row=4,column=0,columnspan=5)
Radiobutton(root,text='TinyUrl*',font=('Arial',8,'bold'),width=10,bg='Light Blue',variable=Prefix,value=1).grid(row=5,column=0)
Radiobutton(root,text='Is.gd',font=('Arial',8,'bold'),width=10,bg='Light Blue',variable=Prefix,value=2).grid(row=5,column=1)
Radiobutton(root,text='Chilp',font=('Arial',8,'bold'),width=8,bg='Light Blue',variable=Prefix,value=3).grid(row=5,column=2)
Radiobutton(root,text='Da.gd',font=('Arial',8,'bold'),width=8,bg='Light Blue',variable=Prefix,value=4).grid(row=5,column=3)
Radiobutton(root,text='Cl1p.net',font=('Arial',8,'bold'),width=8,bg='Light Blue',variable=Prefix,value=5).grid(row=5,column=4)

#Url Output
Label(root,textvariable=MessageOut,bg='#ebccd1',fg='Red',anchor=CENTER,font=('bold')).grid(row=6,column=0,ipadx=5,columnspan=5)
Entry(root,textvariable=Out_Url,width=60,bd=4,bg='Light Blue',font=('Helventica','12','bold')).grid(row=7,column=1,padx=2,pady=15,ipady=5,columnspan=3)

#Exit Button
Button(root,text='Exit',width=8,bg='red',font=('Helventica','10','bold'),command=root.quit).grid(row=10,column=4,sticky='SE')
Qrframe=Frame(root,borderwidth=5,highlightbackground='black',highlightthickness=5).grid(row=9,column=2,rowspan=2,columnspan=2)
QrHolder=Label(Qrframe,bg='Light Blue')
QrHolder.grid(row=9,column=2,rowspan=2,columnspan=2)
root.mainloop()