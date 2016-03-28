#!/usr/local/bin/python2.7
# encoding: utf-8
import Tkinter
import time

from calendar import Mycalendar

events = Mycalendar.main()


#creation de la mainframe Tkinter
mainFrame = Tkinter.Tk()

# Creation de la canvas
w = Tkinter.Canvas (mainFrame,bg="black",height=1080,width=1900)
position = 50,50
#Generation du temps au moment t
string = time.localtime(time.time())
 
w.create_text(position,\
              #Selection de la police et de sa taille
              font=("Liberation Serif",70),\
              #Selection de la position du text par rapport aux coordonées de depart, ici nord ouest
              anchor="nw",\
              #Text couleur blanche
              fill="white",\
              #afficahge de l'heure courant
              text="{0}:{1}".format(string.tm_hour,string.tm_min))
w.create_text(300,40,\
              #Selection de la police et de sa taille
              font=("Liberation Serif",30),\
              #Selection de la position du text par rapport aux coordonées de depart, ici nord ouest
              anchor="nw",\
              #Text couleur blanche
              fill="white",\
              #afficahge de l'heure courant
              text="Vos evenements:" )
i=100
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    w.create_text(300,40+i,\
              #Selection de la police et de sa taille
              font=("Liberation Serif",30),\
              #Selection de la position du text par rapport aux coordonées de depart, ici nord ouest
              anchor="nw",\
              #Text couleur blanche
              fill="white",\
              #afficahge de l'heure courant
              text="{0}    {1}".format(event['summary'], start) )
    i+=100
#ajout du canvas à la page
w.pack()
#la main loop
mainFrame.mainloop()