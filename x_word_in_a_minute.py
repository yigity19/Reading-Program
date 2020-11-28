import time
import random_text
import os


def main():
    speed = random_text.desired_num()
    words = random_text.open_random_file(speed)
    speed = 60 / speed 
    t0 = time.time()
    tfinal = t0+60
    i = 0
    window = random_text.gui(words[0])
    print("BAŞLATILIYOR...")
    time.sleep(10)
    while (time.time()<tfinal):
        
        os.system("cls")
        print(words[i])
        i+=1
        #window.read()
        #window['-OUTPUT-'].update("{}".format(str(words[i]))) 
        time.sleep(speed)
        #window.close()

main()

