import win32api
import win32con
import time
from PIL import ImageGrab

#Y=220 cactus alti 5 pix + 7 pix + 5 pix
#Y=231 cactus bassi 7 pixel

def premi(tasto,tempo):
    win32api.keybd_event(tasto,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(tasto,0,win32con.KEYEVENTF_KEYUP,0)
    
    
print('INIZIAMO YEEEE')

spacebar=0x20
up=0x26
down=0x28




    
oldScreen = [0]*600
#y=215 prende gli uccelli alti ma non quelli bassi
#y=231 fa il delirio per i cactus
#x tra 545 e 553 è buono



#for i in range(100): 
   #INIZIA IL GIOCO
time.sleep(3)
premi(spacebar,0.1)      
inizio = time.time()
vivo = True
altezzaOstacolo=0              

Xdino=450
Ybasso=225
Yalto=203

velocita=500
safeLine=400
ultimoSalto=0

clock=time.time()
while vivo:
    
    screen=ImageGrab.grab().load()
    bianco = screen[0,Ybasso]
    
    distanzaOstacolo=1000
    for y in range(Yalto, Ybasso):
        for x in range(Xdino+25, Xdino+400):
            #print('x='+str(x)+' y='+str(y))
            if bianco != screen[x,y] and bianco!=screen[x+1,y] and bianco!=screen[x+2,y]:
                if x-Xdino < distanzaOstacolo: 
                    distanzaOstacolo = x-Xdino 
                    altezzaOstacolo = Ybasso-y
                    #print('distanza minima=' + str(distanzaOstacolo)+'  altezza='+str(Ybasso-y))
    
    
    #con gli uccelli salta prima
    if altezzaOstacolo >20:
        distanzaOstacolo = distanzaOstacolo-40
            
            
            
    if distanzaOstacolo>40+velocita/50 and distanzaOstacolo<safeLine:
        #print('distanza minima=' + str(distanzaOstacolo)+'  altezza='+str(Ybasso-y))
        if time.time()-inizio<10:
            velocita = 430
        elif time.time()-inizio<40:
            velocita = 525
        elif time.time()-inizio<60:
            velocita = 625
        elif time.time()-inizio<80: 
            velocita = 770
        elif time.time()-inizio<100:
            velocita = 900
        elif time.time()-inizio<150:
            velocita = 1100
        elif time.time()-inizio<200:
            velocita = 1200
        else:
            velocita=1300
        print('aspetto '+str(time.time()-inizio)+' per ostacolo '+str(distanzaOstacolo))
        time.sleep(distanzaOstacolo/velocita)
        print('salto ' + str(time.time()-inizio))
        premi(up,0.12)
        ultimoSalto = time.time()-inizio
    elif distanzaOstacolo<safeLine:
        print('instant salto ' + str(time.time()-inizio))
        premi(up,0.12)
        
        
    
    if time.time()-clock>0.1:
        print('merda per ' + str(time.time()-clock)+'  dist '+str(distanzaOstacolo))
    clock=time.time()
    
    print('-')


    #GAME OVER
    vivo=False
    for x in range(430,460):
        for y in range(240,260):
            pointer = x-430 + 30*(y-240)
            if oldScreen[pointer] != screen[x,y]: 
                vivo=True
            oldScreen[pointer] = screen[x,y]
    if not vivo:
        print('dura per ' + str(time.time()-inizio) + ', ultimo a ' + str(time.time()-inizio-ultimoSalto))
    #print(str(i+1) + ' dura per ' + str(time.time()-inizio) + ', ultimo a ' + str(time.time()-inizio-ultimoSalto))