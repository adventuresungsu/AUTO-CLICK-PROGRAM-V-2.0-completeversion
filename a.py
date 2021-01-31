from tkinter import *
from tkinter import messagebox
import pyautogui
import sys
import threading
import time
import keyboard
import webbrowser

def autoclick3():
    #try:
    ss1 = float(sseecond)
    #except:
        #pyautogui.alert(text='오토클릭 실행전 대기 시간을 설정하지 않은 것 같습니다. 설정에서 설정하여주십시오.')
        #return
    def a():
        pyautogui.click(clicks=999999999999, interval=0.000000000001)
    def ath():
        thread=threading.Thread(target=a)
        thread.daemon=True
        thread.start()
    main.destroy()
    try:
        def Tkaa2():
            aa2 = Tk()
            aa2.title('AUTO CLICK PROGRAM V 2.0')
            aa2.geometry('650x100')

            aa2label = Label(aa2, text="""{0}초 뒤부터 클릭이 시작됩니다. 이것을 조정하려면 설정에 가십시오
클릭 중 클릭을 종료하고 싶다면 esc키를 눌러주세요.""".format(ss1), font=("굴림", 12), fg="black")
            aa2label.place(x = 5, y = 30)

            aa2.mainloop()

            def aa2t():
                time.sleep(ss1)
                aa2.destroy()
            aa2t()
        def Tkaa2th():
            thread=threading.Thread(target=Tkaa2)
            thread.daemon=True
            thread.start()
        Tkaa2th()
        time.sleep(ss1)
        ath()
        while True:
            if keyboard.is_pressed('esc'):
                return
    except:
        ath()
        while True:
            if keyboard.is_pressed('esc'):
                return
def gui1():
    ss1 = float(sseecond)
    def gui21():
        try:
            a = get_var.get() #작성한 값을 얻는다.
            b = float(a)  #작성한 값의 형식을 바꾸어준다.
            main.destroy() #main 창을 끈다.
            main2.destroy() #main2 창을 끈다.
            time.sleep(ss1)   #2초 먼저 기다린다.
            def ab():
                while True:
                    pyautogui.click()
                    time.sleep(b)
            def abth():
                thread=threading.Thread(target=ab)
                thread.daemon=True
                thread.start()
            abth()
            while True: #무한 반복한다.
                if keyboard.is_pressed('esc'):
                    return #이 함수는 종료 된다.
        except ValueError:
            main2.destroy()
            messagebox.showerror("뭔가 잘못 됬는데요", """올바른 수를 입력하세요. 클릭 횟수는 정수만 사용가능하고,
초는 올바른 소수나 정수만 사용해주세요. 이 메세지 창을 닫을 때
꼭 확인을 눌러주세요. 아무것도 없는 창이 쓸때 없이 켜집니다.
클릭 중 클릭을 종료하려면 esc를 눌러주세요""")
    main2 = Tk()
    main2.title("AUTO CLICK PROGRAM V 2.0")
    main2.geometry('325x130')

    main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
    main2button.place(x = 7, y = 65)

    getsecond1 = StringVar() #입력을 할 수 있는 공간을 만든다.
    get_var = Entry(main2, width=39, textvariable = getsecond1)
    get_var.place(x = 5, y = 35) #getsecond1의 위치를 정한다.

    mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
    mainlabel2.place(x = 12, y = 100)

    mainlabel3 = Label(main2, text="확인을 누르고 난 후 {0}초 뒤부터 클릭이 시작됩니다.".format(ss1), font=('굴림', 8), fg="black")
    mainlabel3.place(x = 5, y = 10)

    main2.mainloop()

def gui2():
    ss1 = float(sseecond)
    def gui21():
        try:
            a = get_var.get() #작성한 값을 얻는다.
            b = float(a)  #작성한 값의 형식을 바꾸어준다.
            main.destroy() #main 창을 끈다.
            main2.destroy() #main2 창을 끈다.
            time.sleep(ss1)
            def ab():
                while True:
                    pyautogui.click(clicks=2)
                    time.sleep(b)
            def abth():
                thread=threading.Thread(target=ab)
                thread.daemon=True
                thread.start()
            abth()
            while True: #무한 반복한다.
                if keyboard.is_pressed('esc'):
                    return #이 함수는 종료 된다.
        except ValueError:
            main2.destroy()
            messagebox.showerror("뭔가 잘못 됬는데요", """올바른 수를 입력하세요. 클릭 횟수는 정수만 사용가능하고,
초는 올바른 소수나 정수만 사용해주세요. 이 메세지 창을 닫을 때
꼭 확인을 눌러주세요. 아무것도 없는 창이 쓸때 없이 켜집니다.
클릭 중 클릭을 종료하려면 esc를 눌러주세요""")


    main2 = Tk()
    main2.title("AUTO CLICK PROGRAM V 2.0")
    main2.geometry('325x130')

    main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
    main2button.place(x = 7, y = 65)

    getsecond1 = StringVar() #입력을 할 수 있는 공간을 만든다.
    get_var = Entry(main2, width=39, textvariable = getsecond1)
    get_var.place(x = 5, y = 35) #getsecond1의 위치를 정한다.

    mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
    mainlabel2.place(x = 12, y = 100)

    mainlabel3 = Label(main2, text="확인을 누르고 난 후 {0}초 뒤부터 클릭이 시작됩니다.".format(ss1), font=('굴림', 8), fg="black")
    mainlabel3.place(x = 5, y = 10)

    main2.mainloop()
def gui3():
    ss1 = float(sseecond)
    def gui31():
        try:
            a1 = get_var1.get()
            a2 = get_var2.get()
            b1 = int(a1)
            b2 = float(a2)
            main.destroy()
            main3.destroy()
            time.sleep(ss1)
            def ab():
                while True:
                    pyautogui.click(clicks=b1)
                    time.sleep(b2)
            def abth():
                thread=threading.Thread(target=ab)
                thread.daemon=True
                thread.start()
            abth()
            while True:
                if keyboard.is_pressed('esc'):
                    return
        except ValueError:
            main3.destroy()
            messagebox.showerror("뭔가 잘못 됬는데요", """올바른 수를 입력하세요. 클릭 횟수는 정수만 사용가능하고,
초는 올바른 소수나 정수만 사용해주세요. 이 메세지 창을 닫을 때
꼭 확인을 눌러주세요. 아무것도 없는 창이 쓸때 없이 켜집니다.
클릭 중 클릭을 종료하려면 esc를 눌러주세요""")

    main3 = Tk()
    main3.title("AUTO CLICK PROGRAM V 2.0")
    main3.geometry('400x175')

    mainbutton = Button(main3, text="                                   확인                                   ", font=("굴림", 9), fg="black", command=gui31)
    mainlabel1 = Label(main3, text="몇초에 몇번 씩 클릭 하도록 설정 하시겠습니까?", font=("굴림", 10), fg="black")
    mainlabel2 = Label(main3, text="확인을 누르고 난 후 {0}초 뒤부터 클릭이 시작됩니다.".format(ss1), font=("굴림", 8), fg="black")
    mainlabel3 = Label(main3, text="여기에 클릭 횟 수를 입력하세요.", font=("굴림", 7), fg="black")
    mainlabel4 = Label(main3, text="여기에 초를 입력하세요.", font=("굴림", 7), fg="black")

    mainlabel1.place(x = 5, y = 10)
    mainlabel2.place(x = 5, y = 35)
    mainlabel3.place(x = 5, y = 59)
    mainlabel4.place(x = 5, y = 103)
    mainbutton.place(x = 5, y = 145)

    getsecond1 = StringVar()
    getclicks1 = StringVar()
    get_var1 = Entry(main3, width=48, textvariable = getsecond1)
    get_var2 = Entry(main3, width=48, textvariable = getclicks1)
    get_var1.place(x = 5, y = 75)
    get_var2.place(x = 5, y = 120)

    main3.mainloop()

def gui4():

    def gui41():
        webbrowser.open('https://drive.google.com/file/d/1sLZjDHuGbxNZ-f5B-XVXTswwjuqsoyK2/view?usp=sharing')
    main1234 = Tk()
    main1234.title("AUTO CLICK PROGRAM V 2.0/정보")
    main1234.geometry("825x275")

    nmbutton = Button(main1234, text="이 프로그램의 파이썬 소스코드 보기.", font=("굴림", 28), fg = "black", command=gui41)
    nmbutton.place(x = 0, y = 5)

    nmlabel = Label(main1234, text="""이 프로그램은 qhd 환경에서 만들어졌습니다. 그 외의 해상도에서는 버튼 배치나
창 크기가 매우 이상할 수 있습니다. 이 프로그램은 2021 1월 21일 저녁에 만들어 졌고 
한두달 있으면 중학생이 되는 컴퓨터에 관심이 많은 초*딩이 만들었습니다. 잘 사용하세여.
python3로 만들었습니다. 혹시나 이 프로그램의 코드가 필요 하실 수도 있는 파이썬 
초보분들을 위해서 파이썬 코드를 올려 놓았습니다. 필요하면 이용해 주세요.
그리고 버튼 배치가 영 퀄리티 떨어지고 신경 쓰이 신다면 디스플레이 설정에 들어가서
텍스트, 앱 및 기타 항목의 크기 변경에서 125퍼센트를 선택해주세요. 제가 개발할 때
비율이기 때문에 배치가 잘 나올 겁니다!!!!!""", font=("굴림", 12), fg = "black")
    nmlabel.place(x = 5, y = 100)

def gui5():
    흔한변수 = pyautogui.confirm(text="정말로 오토클릭 프로그램을 종료하시겠습니까?", title="AUTO CLICK PROGRAM V 2.0/종료", buttons=['Yes', 'No'])
    if 흔한변수 == 'Yes':
        sys.exit()
    if 흔한변수 == 'No':
        return

def setting():
    setting = Tk()
    setting.geometry('400x125')
    setting.title('AUTO CLICK PROGRAM V 2.0/설정')

    def settingsecond():
        a = get_var1.get()
        ㅠㅠ = open("clickstart--time.txt", 'w')
        ㅠㅠ.write(a)
        if a == '':
            pyautogui.alert("옳은 값이 아닙니다. 다시 해주십시오. 대기 시간을 원하지 않으시면 공백을 넣지 마시고 0을 입력하여주십시오")
            return
        pyautogui.alert('적용이 완료되었습니다. 프로그램을 재시작 하십시오')
        main.destroy()
        setting.destroy()

    mainlabels1 = Label(setting, text="""클릭을 시작하기 전 대기 시간을 설정합니다.
원하는 대기 시간을 입력후, 확인을 눌러주세요""")
    mainlabels1.place(x = 0, y = 5)
    mainlabels = Button(setting, text="                    확인                    ", font=("굴림", 15), command=settingsecond)
    mainlabels.place(x = 5, y = 80)

    getsecond111 = StringVar
    get_var1 = Entry(setting, width=48, textvariable = getsecond111)
    get_var1.place(x = 5, y = 50)

try:
    f = open("clickstart--time.txt", 'r')
    sseecond = f.readline()
    f.close()
except:
    f1 = open("clickstart--time.txt", 'w')
    f1.write('2')
    f1.close()

try:
    fdsa = open("다시는.txt", 'r')
    fdsa.close()
except:
    def asko():
        gkt = pyautogui.confirm("""설정-시스템-디스플레이-배율 및 레이아웃-텍스트, 
앱 및 기타항목의 크기변경에서 125퍼센트로 설정해놓는
것을 추천 드립니다. 안 그러면 버튼 배치가 이상해집니다.""", "헤이 이봐요", buttons=['확인', '이 메시지를 다시는 표시하지 않음'])
        if gkt == '확인':
            pyautogui.alert()
            return
        if gkt == '이 메시지를 다시는 표시하지 않음':
            pyautogui.alert('이 메시지를 다시 표시하도록 하려면 이 파일이 있는 폴더에 있는 다시는.txt를 삭제하여 주시기 바랍니다.')
            gksrmf = open("다시는.txt", 'w')
            gksrmf.close()
    asko()

main = Tk() #하나의 gui 창을 만든다.
main.title('AUTO CLICK PROGRAM V 2.0') #main이라는 gui 창의 타이틀을 정한다.
main.geometry('520x600') #main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 18), fg="black") #main이라는 창에 글씨를 쓴다
mainlabel.place(x=5, y=5) #mainlabel의 위치를 정한다.

mainlabel2 = Label(main, text="오토클릭 중에 클릭을 종료하고 싶으시면 esc 버튼을", font=("굴림", 12), fg='red')
mainlabel2.place(x=10, y=60)

mainlabel3 = Label(main, text="누르시면 됩니다! 그냥 한번 만들어 봤어요!", font=("굴림", 12), fg='black')
mainlabel3.place(x=10, y=85)

mainlabel4 = Label(main, text="https://www.youtube.com/channel/UCSusOpb6pjWWjIudkqgqGTg", font=("굴림", 10), fg='black')
mainlabel4.place(x=10, y=110)

mainlabel5 = Label(main, text="하고 있는 유튜브 링크입니다 ㅇㅅㅇ 컴린이에요", font=("굴림", 12), fg="black")
mainlabel5.place(x=10, y=135)

mainlabel6 = Label(main, text="바이러스 없구요 만들지도 못해연.", font=("굴림", 12), fg="black")
mainlabel6.place(x=10, y=165)

mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg = "red", command=autoclick3) #main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
mainbutton1.place(x = 15, y =200) #mainbutton1의 위치를 정한다.

mainbutton2 = Button(main,  text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg = "orange", command=gui1)
mainbutton2.place(x = 5, y = 265)

mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg = "green", command=gui2)
mainbutton3.place(x = 5, y = 320)

mainbutton4 = Button(main, text="""직접 초 간격, 클릭 횟수를
직접 설정하겠습니다.""", font=("굴림", 19), fg = "blue", command=gui3)
mainbutton4.place(x = 55, y = 370)

mainbutton5 = Button(main, text="정보", font=("굴림", 18), fg = "purple", command=gui4)
mainbutton5.place(x = 200, y = 475)

mainbutton6 = Button(main, text="프로그램 종료", font=("굴림", 15), fg = "Indigo", command=gui5)
mainbutton6.place(x = 155, y = 550)

mainbutton7 = Button(main, text="설정", font=("굴림", 18), fg = "black", command=setting)
mainbutton7.place(x = 429, y = 545)

main.mainloop() #창을 유지한다.