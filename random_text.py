import random
import os
import PySimpleGUI as sg

def gui(word):
    layout = [  [sg.Text(word, size =(20, 2), justification ='center',key ='-OUTPUT-')], ]
    window = sg.Window("OKUMA HIZI PROGRAMI", layout)
    # Create an event loop
    return window

def gui_exit(window):
    window.close()

def available_files():
    txts= []
    for files in os.listdir("./"):
        if "txt" in files:
            txts.append(files)
    return txts

def open_random_file(x):
    print("DOSYALARI ARAŞTIRIYORUM...")
    length = len(find_suitable_texts(x))
    print("ARAŞTIRMA TAMAMLANDI...")
    random_num = random.randint(0,length - 1)
    return words_in_file(find_suitable_texts(x)[random_num])

def words_in_file(desired_file):
    words = list()
    with open(desired_file,encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words


def desired_num():
    print("60 SANİYEDE KAÇ KELİME OKUMAK İSTEDİĞİNİZİ GİRİN :",end="")
    x = int(input())
    return x


def find_suitable_texts(x):
    wanted_num = x
    num_files = len(available_files())
    suitable_texts = list()
    for i in range(num_files):
        if (wanted_num<= len(words_in_file(available_files()[i]))):
            print(available_files()[i], "in kelime sayısı", len(words_in_file(available_files()[i])) )
            suitable_texts.append(available_files()[i])
    if (len(suitable_texts) == 0):
        print("UYGUN METİN BULAMADIM. LÜTFEN DAHA UZUN BİR METİN EKLEYİN...")
        exit()
    return suitable_texts











      
