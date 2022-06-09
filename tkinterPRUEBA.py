# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:37:36 2022

@author: Usuario
"""

import  tkinter  as  tk
import tkinter.font as tkFont

def DDADMS():
    DMS2lat()
    DMS2lon()

def DMS2lat ():
        #decDMS2= float(input("Ingrese el valor de los numeros decimales para la longitud: "))
#         minuto=cajatexto.get()
#         minente=int(minuto)
#         mindeci=(minuto-minente)*60
#         segun=int(mindeci)
#         segun2=(mindeci-segun)*60
#         grado=int(cajatexto.get())
         
         
         ideg = abs(int(float(cajatexto.get())))
       #  print(ideg)
         dMin = (abs(float((cajatexto.get()))) - ideg) * 60
        # print(dMin)
         imin = int(dMin)
         #print(imin)
         dseg = (dMin - imin) * 60
         #print(dseg)
         if float(cajatexto.get())< 0:
             varlat.set("S")
         else:
             varlat.set("N")
         cajatexto3.delete(0, tk.END)
         cajatexto3.insert(0, ideg)
         cajatexto4.delete(0, tk.END)
         cajatexto4.insert(0, imin)
         cajatexto5.delete(0, tk.END)
         cajatexto5.insert(0, dseg)       
         
def DMS2lon ():
#         minuto2=cajatexto2.get()
#         minente2=int(minuto2)
#         mindeci2=(minuto2-minente2)
#         segun2=mindeci2*60
#         grado2=int(cajatexto3.get())
#         cajatexto6.insert(grado2)
#         cajatexto7.insert(minente2)
#         cajatexto8.insert(segun2)
         
         ideg = abs(int(float(cajatexto2.get())))
         #print(ideg)
         dMin = (abs(float((cajatexto2.get()))) - ideg) * 60
        # print(dMin)
         imin = int(dMin)
         #print(imin)
         dseg = (dMin - imin) * 60
         #print(dseg)
         if float(cajatexto2.get())< 0:
             varlat2.set("W")
         else:
             varlat2.set("E")
         cajatexto6.delete(0, tk.END)
         cajatexto6.insert(0, ideg)
         cajatexto7.delete(0, tk.END)
         cajatexto7.insert(0, imin)
         cajatexto8.delete(0, tk.END)
         cajatexto8.insert(0, dseg)
        
       
def opcion2():
    DD()
    DDlat()
   
   
def DD ():
    resultad=(((float(cajatexto8.get())/60)/60)+(int(cajatexto7.get())/60)+int(cajatexto6.get()))
    cajatexto2.delete(0, tk.END)
    #print(resultad)
    letra=varlat2.get()
    #print(letra)
    if letra=='W':
        resultad=resultad * -1
    cajatexto2.insert(0, resultad)
    return resultad    
    

def DDlat ():
    resulta=(((float(cajatexto5.get())/60)/60)+(int(cajatexto4.get())/60)+int(cajatexto3.get()))
    cajatexto.delete(0, tk.END)
    
    letras=varlat.get()
    
    if letras=='S':
            resulta=resulta * -1
    cajatexto.insert(0, resulta)
    return resulta 

##Crear una instancia de Tkinter
ventana  =  tk.Tk()
ventana.geometry("700x400")

ventana.config(bg="gray")

##Añadir color al fondo
ventana.title("Conversor de Coordenadas")

varlat=tk.StringVar(ventana)
varlat.set("N")
lathem=tk.OptionMenu(ventana, varlat, "S", "N")
lathem.grid(row=6, column=4)

varlat2=tk.StringVar(ventana)
varlat2.set("W")
lonhem=tk.OptionMenu(ventana, varlat2, "E", "W")
lonhem.grid(row=7, column=4)

fontStyle1 = tkFont.Font(family="Times new roman", size=30)
fontStyle2 = tkFont.Font(family="Times new roman", size=10)
etiqueta = tk.Label(ventana, text='CONVERSOR DE COORDENADAS', bg='black', fg='white', font=fontStyle1)
etiqueta2 = tk.Label(ventana, text='Grados Decimales', font=fontStyle2)
etiqueta.grid(row = 0, column = 0, columnspan=5, pady=5)
etiqueta2.grid(row = 1, column = 0, columnspan=2, pady=5)

latDD= tk.Label(ventana, text='LATITUD', font=fontStyle2)
lonDD= tk.Label(ventana, text='LONGITUD', font=fontStyle2)
latDD.grid(row = 2, column = 0, pady=5)
lonDD.grid(row = 3, column = 0)

latDMS= tk.Label(ventana, text='LATITUD', font=fontStyle2)
lonDMS= tk.Label(ventana, text='LONGITUD', font=fontStyle2)
latDMS.grid(row = 6, column = 0)
lonDMS.grid(row = 7, column = 0)

cajatexto= tk.Entry(ventana)
cajatexto.grid(row=2, column=1)
cajatexto2= tk.Entry(ventana)
cajatexto2.grid(row=3, column=1)

boton1=tk.Button(ventana, text="Convertir DD a DMS", command=DDADMS)
boton1.grid(row=4, column=1, pady=5)

etiqueta3 = tk.Label(ventana, text='Grados, Minutos, Segundos', font=fontStyle2)
etiqueta3.grid(row=5, column=1, pady=5)

cajatexto3= tk.Entry(ventana)
cajatexto3.grid(row=6, column=1)
cajatexto4= tk.Entry(ventana)
cajatexto4.grid(row=6, column=2)
cajatexto5= tk.Entry(ventana)
cajatexto5.grid(row=6, column=3)
cajatexto6= tk.Entry(ventana)
cajatexto6.grid(row=7, column=1)
cajatexto7= tk.Entry(ventana)
cajatexto7.grid(row=7, column=2)
cajatexto8= tk.Entry(ventana)
cajatexto8.grid(row=7, column=3)

boton2=tk.Button(ventana, text="Convertir DMS a DD", command = opcion2)
boton2.grid(row=8, column=1, pady=5)

ventana.mainloop()