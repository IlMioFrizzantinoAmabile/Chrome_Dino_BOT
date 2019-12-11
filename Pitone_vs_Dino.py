# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:12:28 2019

@author: Miani
"""

import win32api
import win32con
import time
import numpy as np
import random as rd
from PIL import ImageGrab
#import d3dshot


#schermo=d3dshot.create()
#screen = schermo.screenshot().load()

#print(screen)


#Y=220 cactus alti 5 pix + 7 pix + 5 pix
#Y=231 cactus bassi 7 pixel

spacebar=0x20
up=0x26
down=0x28

oldScreen = [0]*600
oldDistOstacolo = 0


def premi(tasto):
    win32api.keybd_event(tasto,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(tasto,0,win32con.KEYEVENTF_KEYUP,0)
      
    
    
    
    
#popolazione = []
#dim_popolazione = 32

class Cervello:
    def __init__(self,dimensione,RN):
        self.dimensione=dimensione    
        self.RN=RN
        self.fitness=0
    def computa(self,data):
        return np.inner(RN,data)>2
def sorta(yo):
    return yo.fitness
    
dimensione_cervello_x = 15
#RN = [0]*dimensione_cervello_x*dim_popolazione
#data = [0]*dimensione_cervello_x
##RN=[0]*14+[1]*2+[0]*14
##cervello = Cervello(dimensione_cervello_x , RN)
#RNs=[]
#for i in range(0,dim_popolazione):
#    RNs.append([0]*dimensione_cervello_x)
#    RN=RNs[i]
#    for x in range(0,dimensione_cervello_x):
#        RN[x] = 2*rd.random()-1 
#    popolazione.append(Cervello(dimensione_cervello_x , RN))
#results=[]
#
#for cervello in popolazione:
#    print(cervello.RN[1])

report=[]
repp=[]

for culone in range(0,10000):
    print('GENERAZIONE '+str(culone+1))
    print() 
    esemplare=0
    #for cervello in popolazione[:round(dim_popolazione/2)]:
    for cervello in popolazione+popolazione+popolazione:
        for i in range(0,1):
              #print('INIZIAMO YEEEE')
              print('--Esemplare '+str(esemplare%dim_popolazione + 1)+' start--')
              time.sleep(1.5)
        ###### INIZIA IL GIOCO #######
        premi(spacebar)      
        
        tempocicli=0
        numcicli=0
        inizio = time.time()
        vivo = True
        while vivo:
            
            screen=ImageGrab.grab().load()
            bianco = screen[20,225]
            
            
            #trova altezza terreno
            lineaterra=270 #casuale 
            for y in range(230, 270):
                islineaterra=1
                for x in range(140 , 190):
                    if screen[x,y]==bianco:
                        islineaterra=0;
                if islineaterra==1:
                    lineaterra=y
            lineavisuale=lineaterra-37
            
            
            
            #INDIVIDUA GLI OSTACOLI
            #le x degli ostacoli vanno da 180 a 570
            #sarebbe bello vedere ad almeno 300 di distanza
            y_ostacoli_alti=211
            y_ostacoli_bassi=227
        #    linea='';
        #    for x in range(180, 370, 5):
        #        if screen[x,y_ostacoli_alti]!=bianco: 
        #            linea+='O'
        #        else:
        #            linea+='_'
        #    print(linea)
            linea='';
            for aus_x in range(0,dimensione_cervello_x):
                x = 180 + aus_x*10
                is_there_ostacolo=0
                for i in range(0,10):
                    if screen[x+i,y_ostacoli_bassi]!=bianco:
                        is_there_ostacolo=1            
                    if screen[x+i,y_ostacoli_alti]!=bianco:
                        is_there_ostacolo=1
                if is_there_ostacolo==1:
                    linea+='O'
                    data[aus_x]=1
                else:
                    linea+='_'
                    data[aus_x]=0
            
            
            
            #salta
            if ( cervello.computa(data) ):
                premi(up)
    #            print('SALTO')
    #            print()
                  
            
            fitness = time.time()-inizio 
            
            
            
            
            #stampa lo stampabile
    #        print()
    #        print()
    #        print('-----------------------')
    #        print('NUOVO SCREENSHOT') 
    #        print('altezza terra='+str(y))
    ##        for y in range(lineavisuale,lineaterra,2):
    ##            linea='';
    ##            linea+=str(y)+' '
    ##            #for x in range(115 , 690, 5):
    ##            for x in range(130, 570, 5):
    ##                if screen[x,y]!=bianco: 
    ##                    linea+='O'
    ##                else:
    ##                    linea+='_'
    ##            print(linea)
    #        
    #        print('#'*dimensione_cervello_x)
    #        print(linea)
    #        print('#'*dimensione_cervello_x)
    #        print('finess =  '+str(fitness))
    #        print()
            #print(data) 
            
                  
                  
        #          
        #    lineadino=200
        #    ostacoli=[]
        #    distanzaOstacolo=-1000
        #    for x in range(lineadino, 470):
        #        for y in range(lineavisuale, lineaterra-10):
        #            if bianco!=screen[x,y] and bianco!=screen[x+1,y] and bianco!=screen[x+2,y]:
        #                #x è un ostacolo
        #                if x-lineadino > distanzaOstacolo + 42:  #più vicini di 41 sono lo stesso ostacolo
        #                    distanzaOstacolo = x-lineadino
        #                    ostacoli.append(distanzaOstacolo)
        #
        #    #print('ostacoli '+str(ostacoli))
            
            
            
            
            numcicli+=1
            clock = time.time()
            
        
            #CHECK GAME OVER
            vivo=False
            for x in range(430,460):
                for y in range(240,260):
                    pointer = x-430 + 30*(y-240)
                    if oldScreen[pointer] != screen[x,y]: 
                        vivo=True
                    oldScreen[pointer] = screen[x,y]
        tempomedio=(time.time()-inizio)/numcicli
        print('GAME OVER - fit='+str(fitness))
        if esemplare<dim_popolazione:
            cervello.fitness = fitness
        elif esemplare<2*dim_popolazione:
            cervello.fitness = (cervello.fitness+fitness)/2
            print('fit intermedio = '+str(cervello.fitness))
        else:
            cervello.fitness = (2*cervello.fitness+fitness)/3
            print('fit medio = '+str(cervello.fitness))
        esemplare+=1
    #    print()
    #    print()
        #print('media per ciclo = '+str(tempomedio))
        
    
    results=[]
    for cervello in popolazione:
        results.append(cervello.fitness)
    print()
    print()
    print('Risultati')
    print(results)
    print('Migliore: '+str(max(results)))
    print()
    
    popolazione.sort(key=sorta)
    
    report.append('GENERAZIONE '+str(culone)+' il migliore ha fit='+str(popolazione[-1].fitness)+' e RN='+str(popolazione[-1].RN)+'_____________')
    repp.append(popolazione[-1].fitness )
    
    #MUTAZIONE#
    fattore_di_crescita=0.3
    
    for indice in range(0,round(dim_popolazione/2)):
        cervellocacca = popolazione[indice]
        cervellobuono = popolazione[-1-indice]
        for x in range(0,dimensione_cervello_x):
            cervellocacca.RN[x] = cervellobuono.RN[x] + (2*rd.random()-1)*fattore_di_crescita
    cervellobuono = popolazione[-1]
    cervellobuono2 = popolazione[-2]
    cervellocacca = popolazione[round(dim_popolazione/2)-1]
    for x in range(0,dimensione_cervello_x):
        cervellocacca.RN[x] = cervellobuono.RN[x] + (2*rd.random()-1)*fattore_di_crescita
    cervellocacca = popolazione[round(dim_popolazione/2)-2]
    for x in range(0,dimensione_cervello_x):
        cervellocacca.RN[x] = cervellobuono.RN[x] + (2*rd.random()-1)
    cervellocacca = popolazione[round(dim_popolazione/2)-3]
    for x in range(0,dimensione_cervello_x):
        cervellocacca.RN[x] = cervellobuono.RN[x] + (2*rd.random()-1)
    cervellocacca = popolazione[round(dim_popolazione/2)-4]
    for x in range(0,dimensione_cervello_x):
        cervellocacca.RN[x] = cervellobuono2.RN[x] + (2*rd.random()-1)
    cervellocacca = popolazione[round(dim_popolazione/2)-5]
    for x in range(0,dimensione_cervello_x):
        cervellocacca.RN[x] = (cervellobuono.RN[x]+cervellobuono2.RN[x])/2 + (2*rd.random()-1)*fattore_di_crescita

    
#for cervello in popolazione:
#    print()
#    print(cervello.RN)