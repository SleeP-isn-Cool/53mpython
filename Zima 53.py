#python 2. ucebnica ulohy 5.1-4, 5.4-24, 5.4-32

import tkinter

canvas = tkinter.Canvas(width = 400, height = 200, bg="white")

canvas.pack()


#def
def start():
#def
        #citanie suboru
        subor = open("zastavba_na_ulici.txt", "r")
        #citanie suboru

###############
#pocty = [0]*16
###############
        #premenne
        vyska = 0
        y=200
        x=200
        #premenne

        #citanie riadku
        riadok = subor.readline().strip()
        #citanie riadku


        #########################
        #for riadok in range(16):
        #        canvas.create_rectangle(50+i*30, 450, 50+i*30+20, 450-pocty[i], fill='#4cb050')
        ########################################################################################


        #toto malo citat velkosti (aj to cita) ale nerobi to viacej obldznikov to som skusal s kodom vyssie ale nic to nerobi aspon to robi jeden
        for riadok in subor:
                cislo = riadok.split()
                
                dlzka = int(cislo[0])
                vyska = int(cislo[1])
        #citanie velkosti

        #vykreslenie oblznika
        if vyska >= 1:
                canvas.create_rectangle(x,y, x + dlzka, y - vyska, fill="gray")
        #vykreslenie obdlznika

               
        subor.close()

#nacitanie vstupov a buttonu
entry1 = tkinter.Entry()
entry1.insert(0,"0")
entry1.pack()

button1 = tkinter.Button(text="start", command=start)
button1.pack()
#nacitanie vstupov a buttonu
