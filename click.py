import pyautogui
import time
import pynput
import webbrowser

def stop(key):
    global flag
    try:
        if key.char == 'p':
            print("paused")
            flag=1
        if key.char == 's':
            print('stopped')
            flag=2
        if key.char == 'r':
            print('resumed')
            flag=3
        else:
            pass
    except:
        pass

def main():
    global flag
    move=False
    while not move:
        move= not input('Press Enter to open cookieclicker')
    webbrowser.open('https://orteil.dashnet.org/cookieclicker/')    
    start=time.time()
    
    flag=1
    keyli = pynput.keyboard.Listener(on_press = stop)
    keyli.start()
    while True:
        end=time.time()
        if end-start>15000 or flag==1:
            print('Press R to continue, S to exit\n')
            if end-start>15000:
                quit()
            while flag == 1:
                if flag==2:
                    keyli.join()
                    quit()
                if flag==3:
                    break
        if flag==2:
            keyli.join()
            quit()
        pyautogui.click(200, 500)
     


if __name__=="__main__":
    flag=0
    main()

