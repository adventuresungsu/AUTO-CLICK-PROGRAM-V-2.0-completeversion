from tkinter import *
import pyautogui
import keyboard
import sys
import threading
import time

def autoclick2():
	pyautogui.click(clicks=9999999999999, interval=0.00000000000000000000000001)
def autoclick3():
	thread=threading.Thread(target=autoclick2)
	thread.daemon=True
	thread.start()
def autoclick():
	autoclick3()
	while True:
		if keyboard.is_pressed('ctrl'):
			sys.exit()

def gui2():
	def autoclick2():
		a = get_var.get()
		b = int(a)
		main2.destroy()
		time.sleep(2)
		while True:
			pyautogui.click()
			time.sleep(b)
	main2 = Tk()
	main2.title("AUTO CLICK PROGRAM V 2.0")
	main2.geometry('325x130')
	main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg = "black", command=autoclick2)
	main2button.place(x = 7, y = 65)
	getsecond1 = StringVar()
	get_var = Entry(main2, width = 39, textvariable = getsecond1)
	get_var.place(x = 5, y = 35)
	mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
	mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
	mainlabel3.place(x = 12, y = 100)
	mainlabel2.place(x = 5, y = 10)

def gui3():
	pass

main = Tk()
main.title('AUTO CLICK PROGRAM V 2.0')
main.geometry('520x600')

mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")
mainbutton = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg = "red", command=autoclick)
mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg = "orange", command=gui2)
mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg = "green", command=gui3)

mainbutton.place(x = 15, y = 200)
mainbutton2.place(x = 5, y = 265)
mainbutton3.place(x = 5, y = 320)
mainlabel.place(x=10, y=20)
main.mainloop()