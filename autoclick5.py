from tkinter import *
import pyautogui
import sys
import threading
import time
import keyboard

def autoclick3():
    main.destroy()
    while True:
        if keyboard.is_pressed('ctrl'): #만약 ctrl를 누른다면
            easter()
            return
        pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999, interval=0.000000000000000000000000000000000000000000000000000000000000000000001)
def gui1():
    def gui21():
        def easter():
            def autoclick3():
                main.destroy()
                while True:
                    if keyboard.is_pressed('ctrl'):  # 만약 ctrl를 누른다면
                        egg()
                        return
                    pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999,
                                    interval=0.000000000000000000000000000000000000000000000000000000000000000000001)

            def gui1():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            egg()
                            return  # 이 함수는 종료 된다.
                        pyautogui.click()  # 클릭을 한다.
                        time.sleep(b)  # b초에 한번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            def gui2():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            egg()  # easter 실행하고
                            return  # 이 함수는 종료 된다.
                        pyautogui.click(clicks=2)  # 클릭을 한다.
                        time.sleep(b)  # b초에 두번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            main = Tk()  # 하나의 gui 창을 만든다.
            main.title('AUTO CLICK PROGRAM V 2.0')  # main이라는 gui 창의 타이틀을 정한다.
            main.geometry('520x600')  # main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

            mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")  # main이라는 창에 글씨를 쓴다
            mainlabel.place(x=10, y=20)  # mainlabel의 위치를 정한다.

            mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg="red",
                                 command=autoclick3)  # main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
            mainbutton1.place(x=15, y=200)  # mainbutton1의 위치를 정한다.

            mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="orange", command=gui1)
            mainbutton2.place(x=5, y=265)

            mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="green", command=gui2)
            mainbutton3.place(x=5, y=320)

            main.mainloop()  # 창을 유지한다.

        def egg():
            def autoclick3():
                main.destroy()
                while True:
                    if keyboard.is_pressed('ctrl'):  # 만약 ctrl를 누른다면
                        easter()
                        return
                    pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999, interval=0.000000000000000000000000000000000000000000000000000000000000000000001)

            def gui1():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            easter()
                            return  # 이 함수는 종료 된다.
                        pyautogui.click()  # 클릭을 한다.
                        time.sleep(b)  # b초에 한번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            def gui2():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            easter()  # easter 실행하고
                            return  # 이 함수는 종료 된다.
                        pyautogui.click(clicks=2)  # 클릭을 한다.
                        time.sleep(b)  # b초에 두번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            main = Tk()  # 하나의 gui 창을 만든다.
            main.title('AUTO CLICK PROGRAM V 2.0')  # main이라는 gui 창의 타이틀을 정한다.
            main.geometry('520x600')  # main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

            mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")  # main이라는 창에 글씨를 쓴다
            mainlabel.place(x=10, y=20)  # mainlabel의 위치를 정한다.

            mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg="red",
                                 command=autoclick3)  # main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
            mainbutton1.place(x=15, y=200)  # mainbutton1의 위치를 정한다.

            mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="orange", command=gui1)
            mainbutton2.place(x=5, y=265)

            mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="green", command=gui2)
            mainbutton3.place(x=5, y=320)

            main.mainloop()  # 창을 유지한다.
        a = get_var.get() #작성한 값을 얻는다.
        b = float(a)  #작성한 값의 형식을 바꾸어준다.
        main.destroy() #main 창을 끈다.
        main2.destroy() #main2 창을 끈다.
        time.sleep(2)   #2초 먼저 기다린다.
        while True: #무한 반복한다.
            if keyboard.is_pressed('ctrl'): #만약 CTRL을 누른다면
                easter()
                return #이 함수는 종료 된다.
            pyautogui.click()   #클릭을 한다.
            time.sleep(b) #b초에 한번 씩 클릭을 한다.


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

    mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
    mainlabel3.place(x = 5, y = 10)

def gui2():
    def gui21():
        def easter():
            def autoclick3():
                main.destroy()
                while True:
                    if keyboard.is_pressed('ctrl'):  # 만약 ctrl를 누른다면
                        egg()
                        return
                    pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999,
                                    interval=0.000000000000000000000000000000000000000000000000000000000000000000001)

            def gui1():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            egg()
                            return  # 이 함수는 종료 된다.
                        pyautogui.click()  # 클릭을 한다.
                        time.sleep(b)  # b초에 한번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            def gui2():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            egg()  # easter 실행하고
                            return  # 이 함수는 종료 된다.
                        pyautogui.click(clicks=2)  # 클릭을 한다.
                        time.sleep(b)  # b초에 두번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            main = Tk()  # 하나의 gui 창을 만든다.
            main.title('AUTO CLICK PROGRAM V 2.0')  # main이라는 gui 창의 타이틀을 정한다.
            main.geometry('520x600')  # main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

            mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")  # main이라는 창에 글씨를 쓴다
            mainlabel.place(x=10, y=20)  # mainlabel의 위치를 정한다.

            mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg="red",
                                 command=autoclick3)  # main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
            mainbutton1.place(x=15, y=200)  # mainbutton1의 위치를 정한다.

            mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="orange", command=gui1)
            mainbutton2.place(x=5, y=265)

            mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="green", command=gui2)
            mainbutton3.place(x=5, y=320)

            main.mainloop()  # 창을 유지한다.

        def egg():
            def autoclick3():
                main.destroy()
                while True:
                    if keyboard.is_pressed('ctrl'):  # 만약 ctrl를 누른다면
                        easter()
                        return
                    pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999, interval=0.000000000000000000000000000000000000000000000000000000000000000000001)

            def gui1():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            easter()
                            return  # 이 함수는 종료 된다.
                        pyautogui.click()  # 클릭을 한다.
                        time.sleep(b)  # b초에 한번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            def gui2():
                def gui21():
                    a = get_var.get()  # 작성한 값을 얻는다.
                    b = float(a)  # 작성한 값의 형식을 바꾸어준다.
                    main.destroy()  # main 창을 끈다.
                    main2.destroy()  # main2 창을 끈다.
                    time.sleep(2)  # 2초 먼저 기다린다.
                    while True:  # 무한 반복한다.
                        if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                            easter()  # easter 실행하고
                            return  # 이 함수는 종료 된다.
                        pyautogui.click(clicks=2)  # 클릭을 한다.
                        time.sleep(b)  # b초에 두번 씩 클릭을 한다.

                main2 = Tk()
                main2.title("AUTO CLICK PROGRAM V 2.0")
                main2.geometry('325x130')

                main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
                main2button.place(x=7, y=65)

                getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
                get_var = Entry(main2, width=39, textvariable=getsecond1)
                get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

                mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
                mainlabel2.place(x=12, y=100)

                mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
                mainlabel3.place(x=5, y=10)

            main = Tk()  # 하나의 gui 창을 만든다.
            main.title('AUTO CLICK PROGRAM V 2.0')  # main이라는 gui 창의 타이틀을 정한다.
            main.geometry('520x600')  # main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

            mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")  # main이라는 창에 글씨를 쓴다
            mainlabel.place(x=10, y=20)  # mainlabel의 위치를 정한다.

            mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg="red",
                                 command=autoclick3)  # main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
            mainbutton1.place(x=15, y=200)  # mainbutton1의 위치를 정한다.

            mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="orange", command=gui1)
            mainbutton2.place(x=5, y=265)

            mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="green", command=gui2)
            mainbutton3.place(x=5, y=320)

            main.mainloop()  # 창을 유지한다.
        a = get_var.get() #작성한 값을 얻는다.
        b = float(a)  #작성한 값의 형식을 바꾸어준다.
        main.destroy() #main 창을 끈다.
        main2.destroy() #main2 창을 끈다.
        time.sleep(2)   #2초 먼저 기다린다.
        while True: #무한 반복한다.
            if keyboard.is_pressed('ctrl'): #만약 CTRL을 누른다면
                easter() #easter 실행하고
                return #이 함수는 종료 된다.
            pyautogui.click(clicks=2)   #클릭을 한다.
            time.sleep(b) #b초에 두번 씩 클릭을 한다.


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

    mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
    mainlabel3.place(x = 5, y = 10)



main = Tk() #하나의 gui 창을 만든다.
main.title('AUTO CLICK PROGRAM V 2.0') #main이라는 gui 창의 타이틀을 정한다.
main.geometry('520x600') #main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black") #main이라는 창에 글씨를 쓴다
mainlabel.place(x=10, y=20) #mainlabel의 위치를 정한다.

mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg = "red", command=autoclick3) #main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
mainbutton1.place(x = 15, y =200) #mainbutton1의 위치를 정한다.

mainbutton2 = Button(main,  text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg = "orange", command=gui1)
mainbutton2.place(x = 5, y = 265)

mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg = "green", command=gui2)
mainbutton3.place(x = 5, y = 320)

main.mainloop() #창을 유지한다.

def easter():
    def autoclick3():
        main.destroy()
        while True:
            if keyboard.is_pressed('ctrl'):  # 만약 ctrl를 누른다면
                egg()
                return
            pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999, interval=0.000000000000000000000000000000000000000000000000000000000000000000001)

    def gui1():
        def gui21():
            a = get_var.get()  # 작성한 값을 얻는다.
            b = float(a)  # 작성한 값의 형식을 바꾸어준다.
            main.destroy()  # main 창을 끈다.
            main2.destroy()  # main2 창을 끈다.
            time.sleep(2)  # 2초 먼저 기다린다.
            while True:  # 무한 반복한다.
                if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                    egg()
                    return  # 이 함수는 종료 된다.
                pyautogui.click()  # 클릭을 한다.
                time.sleep(b)  # b초에 한번 씩 클릭을 한다.

        main2 = Tk()
        main2.title("AUTO CLICK PROGRAM V 2.0")
        main2.geometry('325x130')

        main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
        main2button.place(x=7, y=65)

        getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
        get_var = Entry(main2, width=39, textvariable=getsecond1)
        get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

        mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
        mainlabel2.place(x=12, y=100)

        mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
        mainlabel3.place(x=5, y=10)

    def gui2():
        def gui21():
            a = get_var.get()  # 작성한 값을 얻는다.
            b = float(a)  # 작성한 값의 형식을 바꾸어준다.
            main.destroy()  # main 창을 끈다.
            main2.destroy()  # main2 창을 끈다.
            time.sleep(2)  # 2초 먼저 기다린다.
            while True:  # 무한 반복한다.
                if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                    egg()  # easter 실행하고
                    return  # 이 함수는 종료 된다.
                pyautogui.click(clicks=2)  # 클릭을 한다.
                time.sleep(b)  # b초에 두번 씩 클릭을 한다.

        main2 = Tk()
        main2.title("AUTO CLICK PROGRAM V 2.0")
        main2.geometry('325x130')

        main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
        main2button.place(x=7, y=65)

        getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
        get_var = Entry(main2, width=39, textvariable=getsecond1)
        get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

        mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
        mainlabel2.place(x=12, y=100)

        mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
        mainlabel3.place(x=5, y=10)

    main = Tk()  # 하나의 gui 창을 만든다.
    main.title('AUTO CLICK PROGRAM V 2.0')  # main이라는 gui 창의 타이틀을 정한다.
    main.geometry('520x600')  # main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

    mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")  # main이라는 창에 글씨를 쓴다
    mainlabel.place(x=10, y=20)  # mainlabel의 위치를 정한다.

    mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg="red", command=autoclick3)  # main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
    mainbutton1.place(x=15, y=200)  # mainbutton1의 위치를 정한다.

    mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="orange", command=gui1)
    mainbutton2.place(x=5, y=265)

    mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="green", command=gui2)
    mainbutton3.place(x=5, y=320)

    main.mainloop()  # 창을 유지한다.

def egg():
    def autoclick3():
        main.destroy()
        while True:
            if keyboard.is_pressed('ctrl'):  # 만약 ctrl를 누른다면
                easter()
                return
            pyautogui.click(clicks=99999999999999999999999999999999999999999999999999999,
                            interval=0.000000000000000000000000000000000000000000000000000000000000000000001)

    def gui1():
        def gui21():
            a = get_var.get()  # 작성한 값을 얻는다.
            b = float(a)  # 작성한 값의 형식을 바꾸어준다.
            main.destroy()  # main 창을 끈다.
            main2.destroy()  # main2 창을 끈다.
            time.sleep(2)  # 2초 먼저 기다린다.
            while True:  # 무한 반복한다.
                if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                    easter()
                    return  # 이 함수는 종료 된다.
                pyautogui.click()  # 클릭을 한다.
                time.sleep(b)  # b초에 한번 씩 클릭을 한다.

        main2 = Tk()
        main2.title("AUTO CLICK PROGRAM V 2.0")
        main2.geometry('325x130')

        main2button = Button(main2, text="                          확인                           ", font=("굴림", 10),
                             fg="black", command=gui21)
        main2button.place(x=7, y=65)

        getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
        get_var = Entry(main2, width=39, textvariable=getsecond1)
        get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

        mainlabel2 = Label(main2, text="몇초에 한 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
        mainlabel2.place(x=12, y=100)

        mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
        mainlabel3.place(x=5, y=10)

    def gui2():
        def gui21():
            a = get_var.get()  # 작성한 값을 얻는다.
            b = float(a)  # 작성한 값의 형식을 바꾸어준다.
            main.destroy()  # main 창을 끈다.
            main2.destroy()  # main2 창을 끈다.
            time.sleep(2)  # 2초 먼저 기다린다.
            while True:  # 무한 반복한다.
                if keyboard.is_pressed('ctrl'):  # 만약 CTRL을 누른다면
                    easter()  # easter 실행하고
                    return  # 이 함수는 종료 된다.
                pyautogui.click(clicks=2)  # 클릭을 한다.
                time.sleep(b)  # b초에 두번 씩 클릭을 한다.

        main2 = Tk()
        main2.title("AUTO CLICK PROGRAM V 2.0")
        main2.geometry('325x130')

        main2button = Button(main2, text="                          확인                           ", font=("굴림", 10), fg="black", command=gui21)
        main2button.place(x=7, y=65)

        getsecond1 = StringVar()  # 입력을 할 수 있는 공간을 만든다.
        get_var = Entry(main2, width=39, textvariable=getsecond1)
        get_var.place(x=5, y=35)  # getsecond1의 위치를 정한다.

        mainlabel2 = Label(main2, text="몇초에 두 번 클릭 하도록 설정 하시겠습니까?", font=("굴림", 9), fg="black")
        mainlabel2.place(x=12, y=100)

        mainlabel3 = Label(main2, text="확인을 누르고 난 후 2초 뒤부터 클릭이 시작됩니다.", font=('굴림', 8), fg="black")
        mainlabel3.place(x=5, y=10)

    main = Tk()  # 하나의 gui 창을 만든다.
    main.title('AUTO CLICK PROGRAM V 2.0')  # main이라는 gui 창의 타이틀을 정한다.
    main.geometry('520x600')  # main이라는 창의 크기를 설정한다. 여기서는 520x600으로 설정 하였다.

    mainlabel = Label(main, text="안녕하세요 오토클릭 프로그램입니다.", font=("굴림", 15), fg="black")  # main이라는 창에 글씨를 쓴다
    mainlabel.place(x=10, y=20)  # mainlabel의 위치를 정한다.

    mainbutton1 = Button(main, text="최대한 빠르게 클릭하겠습니다.", font=("굴림", 20), fg="red",
                         command=autoclick3)  # main이란 창에 버튼을 생성한다. 만약 이 버튼을 누르면 autoclick3라는 함수가 실행된다.
    mainbutton1.place(x=15, y=200)  # mainbutton1의 위치를 정한다.

    mainbutton2 = Button(main, text="몇초에 한 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="orange", command=gui1)
    mainbutton2.place(x=5, y=265)

    mainbutton3 = Button(main, text="몇초에 두 번 클릭 할지 설정하겠습니다.", font=("굴림", 16), fg="green", command=gui2)
    mainbutton3.place(x=5, y=320)

    main.mainloop()  # 창을 유지한다.