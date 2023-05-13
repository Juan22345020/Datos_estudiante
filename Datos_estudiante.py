from tkinter import *
from tkinter import messagebox


# Funciones

#Abrir el boton IMC










#IMC
def abrir_boton_imc():
    global boton_imc
    global image_imc
    boton_imc = Toplevel()
    boton_imc.title("Calcular IMC")
    boton_imc.resizable(False,False)
    boton_imc.geometry("700x400")
    boton_imc.config(bg="white")
    
    image_imc = PhotoImage(file="imc.png")
    image_imc_1=Label(boton_imc, image=image_imc, bg="white")
    image_imc_1.place(x=0, y=0)  
    

    lb_a = Label(boton_imc, text = "Ingrese su altura en metros : ")
    lb_a.config(bg="orangered3", fg="black", font=("Helvetica", 20))
    lb_a.place(x=160, y=155)
    

    lb_p = Label(boton_imc, text = "Ingrese su peso en kg : ")
    lb_p.config(bg="orangered3", fg="black", font=("Helvetica", 20))
    lb_p.place(x=160, y=85)
    

    entry_p = Entry(boton_imc)
    entry_p.config(bg="white", fg= "black", font=("Helvetica",20))
    entry_p.focus_set()
    entry_p.place(x=465, y=86, width=100, height=35)
    

    entry_al = Entry(boton_imc)
    entry_al.config(bg="white", fg= "black", font=("Helvetica",20))
    entry_al.focus_set()
    entry_al.place(x=530, y=158, width=100, height=35)



    lb_e = Label(boton_imc, text = "Ingrese su edad: ")
    lb_e.config(bg="orangered3", fg="black", font=("Helvetica", 20))
    lb_e.place(x=160, y=25)
    

    entry_e = Entry(boton_imc)
    entry_e.config(bg="white", fg= "black", font=("Helvetica",20))
    entry_e.focus_set()
    entry_e.place(x=390, y=26, width=100, height=35)
    
    lb_f = Label(boton_imc, text = "Despues de registrar los datos los resultados se mostraran en la terminal \n principal si desea ingresar nuevos datos por favor hacer click \n  en el boton borrar")
    lb_f.config( fg="black", font=("Helvetica", 14))
    lb_f.place(x=40, y=300)





   

    def Calcular_imc():
        global IMC
        messagebox.showinfo("Confirmacion", "Sus datos seran mostrados en la terminal principal")
        peso = float(entry_p.get())
        altura = float(entry_al.get())
        IMC = peso / altura ** 2
        


       
        boton_imc.destroy()

      

       
   

    bt_medic_aceptar = Button(boton_imc, text="Calcular \n IMC", width=20, height=3, bg="gray80", command=Calcular_imc )
    bt_medic_aceptar.place(x=260, y=220)

    
    
 









def test_psicologico():
   global test
   global image_test
   test = Toplevel()
   test.title("Test Psicologico")
   test.resizable(False,False)
   test.geometry("600x400") 
   
   image_test=PhotoImage(file="tes.png")
   image_test_1=Label(test, image=image_test, bg="white" )
   image_test_1.place(x=0, y=0)

   
   
    


   def aceptar_test():
      global puntaje
      global respuestas
      messagebox.showinfo("Confirmacion", "Sus resultados seran mostrados en la terminal principal")
      test.destroy()



   lb_pre_1 = Label(test, text = "¿Te has sentido estresad@ ultimamente? ")
   lb_pre_1.config(bg="white", fg="black", font=("Helvetica", 15))
   lb_pre_1.place(x=20, y=20)
    
   lb_pre_2 = Label(test, text = "¿Has dormido mal ultimamente? ")
   lb_pre_2.config(bg="white", fg="black", font=("Helvetica", 15))
   lb_pre_2.place(x=20, y=70)

   lb_pre_3 = Label(test, text = "¿Has experimentado cambios en tu estado \n de ánimo ")
   lb_pre_3.config(bg="white", fg="black", font=("Helvetica", 15))
   lb_pre_3.place(x=20, y=120)

   lb_pre_4 = Label(test, text = "¿Has sentido una disminución en tu interés \n por actividades que antes disfrutabas?")
   lb_pre_4.config(bg="white", fg="black", font=("Helvetica", 15))
   lb_pre_4.place(x=20, y=200)

    
   lb_pre_5 = Label(test, text = "Te has sentido aislado socialmente \n recientemente? ")
   lb_pre_5.config(bg="white", fg="black", font=("Helvetica", 15))
   lb_pre_5.place(x=20, y=270)

   bt_aceptar_test=Button(test, text="Aceptar", width=15, height=2, bg="grey80", command=aceptar_test)
   bt_aceptar_test.place(x=230,  y=340)
   




   opciones = ["Si", "No"]
   opcion_var1 =StringVar(value="")
   opcion_var2 =StringVar(value="")
   opcion_var3 =StringVar(value="")
   opcion_var4 =StringVar(value="")
   opcion_var5 =StringVar(value="")


   pregunta1 = OptionMenu(test, opcion_var1, *opciones)
   pregunta1.place(x=420, y=20)
   pregunta2 = OptionMenu(test, opcion_var2, *opciones)
   pregunta2.place(x=420, y=70)
   pregunta3 = OptionMenu(test, opcion_var3, *opciones)
   pregunta3.place(x=420, y=120)
   pregunta4 = OptionMenu(test, opcion_var4, *opciones)
   pregunta4.place(x=420, y=200)
   pregunta5 = OptionMenu(test, opcion_var5, *opciones)
   pregunta5.place(x=420, y=270)
     
   


def calcular_def():
    global IMC
    global puntaje
    messagebox.showinfo("Confirmacion", "Los resultados serán vistos pronto...")
    t_resultados_medic.insert(INSERT, f"Su índice de masa corporal es de:" + str(IMC) + "\n")
    if (IMC < 16):
        t_resultados_medic.insert(INSERT, f"Tienes Criterio de ingreso en el hospital ")
    elif (16 < IMC < 17):
        t_resultados_medic.insert(INSERT, f"Tienes INFRAPESO ")
    elif (17 < IMC < 18):
        t_resultados_medic.insert(INSERT, f"Tienes BAJO PESO")
    elif (18 < IMC < 25):
        t_resultados_medic.insert(INSERT, f"Estás SALUDABLE")
    elif (25 < IMC < 30):
        t_resultados_medic.insert(INSERT, f"Tienes Obesidad grado I")
    elif (30 < IMC < 35):
        t_resultados_medic.insert(INSERT, f"Tienes Obesidad grado II\n")
    elif (35 < IMC < 40):
        t_resultados_medic.insert(INSERT, f"Tienes Obesidad grado III \n")
    elif (IMC > 40):
        t_resultados_medic.insert(INSERT, f"Tienes Obesidad grado IV \n")
    
    
    
    
def evaluar_estado_mental(respuestas):
      puntaje = 0

      if respuestas[0] == "No":
        puntaje += 1

      if respuestas[1] == "Si":
        puntaje += 1

      if respuestas[2] == "Si":
        puntaje += 1

      if respuestas[3] == "Si":
        puntaje += 1

      if respuestas[4] == "Si":
        puntaje += 1

      if puntaje >= 3 and puntaje <= 5:
        t_resultados_medic.insert(INSERT, f"Estás bien, trabaja por mejorar tu salud mental :D\n")
      elif puntaje == 5:
        t_resultados_medic.insert(INSERT, f"¡Qué bien, tienes un estado mental muy bueno!\n")
      elif puntaje < 3 and puntaje > 0:
        t_resultados_medic.insert(INSERT, f"Puedes buscar ayuda si lo necesitas\n")

def borrar_medi():
   messagebox.showinfo("Borrar", "Los datos seran borrados")

   t_resultados_medic.delete("1.0", "end")

 


def calcular_promedio():
   Quimica= float(entry_a_1.get())
   Algebra_lineal=float(entry_a_2.get())
   calculo_1 = float(entry_a_3.get())
   Programacion = float(entry_a_4.get())
   notas=Quimica + Algebra_lineal + calculo_1 + Programacion
   promedio=notas/4   

   dias_fal = float(entry_a_5.get())   

   if promedio >= 4.0 and dias_fal <= 4:
    t_resultados_estud.insert(INSERT, f"Llevas muy buen promedio y has asistido a clases de buena manera, felicidades, eres un crack :D ")
   elif promedio >= 3.0 and promedio < 4.0 and dias_fal < 4:
      t_resultados_estud.insert(INSERT, f"Llevas un promedio medianamente bueno y has asistido a clase de buena manera, vas bien")
   elif promedio  < 3.0 and dias_fal < 4:
      t_resultados_estud.insert(INSERT, f"Llevas mal promedio y has asistido a clase debidamente ¡tienes que mejorar tus notas!")
   elif promedio >= 4.0 and dias_fal >= 4 and dias_fal <=8:
      t_resultados_estud.insert(INSERT,f"Tu promedio es bueno pero no debes faltar mucho a clases") 
   elif promedio >= 3.0 and promedio < 4 and dias_fal >= 4 and dias_fal <=8:
      t_resultados_estud.insert(INSERT,f"Tu promedio es regular y faltas a clase medianamente, debes mejorar")
   elif promedio < 3.0 and dias_fal >= 4 and dias_fal <=8:
      t_resultados_estud.insert(INSERT,f"Tu promedio es muy bajo y faltas a clases, ¡cuidado!")
   elif promedio >= 4.0 and dias_fal > 8:
      t_resultados_estud.insert(INSERT,f"Tu promedio es alto, ¿y faltas mucho a clase? sospechoso")
   elif  promedio >= 3.0 and promedio < 4 and dias_fal >8:
      t_resultados_estud.insert(INSERT,f"Tu promedio es regular y tu asistencia muy baja ¡es importante mejorar!")
   elif promedio < 3.0 and dias_fal >8:
      t_resultados_estud.insert(INSERT, f"Tu promedio es malo y tu asistencia es poca, tienes mucho que mejorar")     



def borrar_estud():
   messagebox.showinfo("Borrar", "Los datos seran borrados")
   global text_content
   t_resultados_estud.delete("1.0", "end")
   





#ventana principal

ventana_principal =Tk()
ventana_principal.title(" Datos del Estudiante")
ventana_principal.geometry("1100x650")
ventana_principal.resizable(0,0)
ventana_principal.config(bg ="white")





# Variables de control 

global puntaje
global respuestas


frame_imagen=Frame(ventana_principal)
frame_imagen.config(bg="white", width=1100, height=650)
frame_imagen.place(x=0, y=0)


imagen_4= PhotoImage(file="univers.png")
lb_Imagen_4 =Label(frame_imagen, image=imagen_4)
lb_Imagen_4.place(x=0, y=0)



lb_titulo=Label(frame_imagen, text= ("Datos del estudiante, Juan David Gutierrez Blanco"))
lb_titulo.config(bg=("LightSkyBlue3"), fg=("DeepSkyBlue4"), font=("Courier", 20, "italic"))
lb_titulo.place(x=290, y=15)



frame_medic= Frame(ventana_principal)
frame_medic.config(bg="white",width=500, height=500)
frame_medic.place(x=30, y=100)

imagen_6= PhotoImage(file="fondo.png")
lb_Imagen_6 =Label(frame_medic, image=imagen_6)
lb_Imagen_6.place(x=0, y=0)





frame_sub_11 = Frame(frame_medic)
frame_sub_11.config(bg="white", width=460, height=360)
frame_sub_11.place(x=20, y=125)


imagen_s= PhotoImage(file="fondo_sub.png")
lb_Imagen_s =Label(frame_sub_11, image=imagen_s)
lb_Imagen_s.place(x=0, y=0)



lb_imc=Label(frame_sub_11, text= ("¡Veamos tu indice de masa corporal!"))
lb_imc.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
lb_imc.place(x=80, y=4)


lb_imc_1=Label(frame_sub_11, text= ("Vamos a ver que tal tu salud mental"))
lb_imc_1.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
lb_imc_1.place(x=100, y=100)


lb_imc_2=Label(frame_sub_11, text= ("!Veamos como te fue!"))
lb_imc_2.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
lb_imc_2.place(x=140, y=200)


bt_medic_mm = Button(frame_medic, text="Calcular imc", width=15, height=2, bg="gray80",
command=calcular_def)
bt_medic_mm.place(x=20, y=30)

bt_medic_mmmm = Button(frame_medic, text="Calcular test", width=15, height=2, bg="gray80",
command=evaluar_estado_mental)
bt_medic_mmmm.place(x=20, y=70)
 
bt_medic_mmm = Button(frame_medic, text="Borrar", width=15, height=2, bg="gray80"  )
bt_medic_mmm.place(x=360, y=30)

bt_medic_m = Button(frame_sub_11, text="¡Test Psicologico!", width=15, height=2, bg="gray80", command=test_psicologico)
bt_medic_m.place(x=174, y=140)


bt_medic = Button(frame_sub_11, text="IMC", width=10, height=2, bg="gray80", command=abrir_boton_imc)
bt_medic.place(x=190, y=40)

Imagen_1= PhotoImage(file="medi.png")
lb_Imagen_1 =Label(frame_medic, image=Imagen_1, bg="white")
lb_Imagen_1.place(x=180, y=15)


frame_estudio= Frame(ventana_principal)
frame_estudio.config(bg="blue",width=500, height=500)
frame_estudio.place(x=565, y=100)


imagen_5= PhotoImage(file="fondd.png")
lb_Imagen_5 =Label(frame_estudio, image=imagen_5)
lb_Imagen_5.place(x=0, y=0)

bt_estudio_mm = Button(frame_estudio, text="Calcular", width=15, height=2, bg="gray80",
command=calcular_promedio)
bt_estudio_mm.place(x=20, y=30)

bt_estudi_mmm = Button(frame_estudio, text="Borrar", width=15, height=2, bg="gray80",
command=borrar_estud  )
bt_estudi_mmm.place(x=360, y=30)

frame_sub_22 = Frame(frame_estudio)
frame_sub_22.config(bg="white", width=460, height=360)
frame_sub_22.place(x=20, y=125)

imagen_es= PhotoImage(file="es.png")
lb_Imagen_es =Label(frame_sub_22, image=imagen_es)
lb_Imagen_es.place(x=0, y=0)



lb_est=Label(frame_sub_22, text= ("¡Vamos a calcular tus notas parciales!"))
lb_est.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
lb_est.place(x=30, y=10)

bt_estud = Label(frame_sub_22, text="Quimica")
bt_estud.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
bt_estud.place(x=15, y=45)

entry_a_1 = Entry(frame_sub_22)
entry_a_1.config(bg="white", fg= "blue", font=("Helvetica",20))
entry_a_1.focus_set()
entry_a_1.place(x=15, y=80, width=70, height=25)



bt_estud_2 = Label(frame_sub_22, text="Algebra Lineal I")
bt_estud_2.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
bt_estud_2.place(x=95, y=45)

entry_a_2 = Entry(frame_sub_22)
entry_a_2.config(bg="white", fg= "blue", font=("Helvetica",20))
entry_a_2.focus_set()
entry_a_2.place(x=95, y=80, width=140, height=25)


bt_estud_3 = Label(frame_sub_22, text="Calculo I")
bt_estud_3.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
bt_estud_3.place(x=255, y=45)

entry_a_3 = Entry(frame_sub_22)
entry_a_3.config(bg="white", fg= "blue", font=("Helvetica",20))
entry_a_3.focus_set()
entry_a_3.place(x=255, y=80, width=85, height=25)



bt_estud_4 = Label(frame_sub_22, text="Fundamentos")
bt_estud_4.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
bt_estud_4.place(x=345, y=45)

entry_a_4 = Entry(frame_sub_22)
entry_a_4.config(bg="white", fg= "blue", font=("Helvetica",20))
entry_a_4.focus_set()
entry_a_4.place(x=345, y=80, width=100, height=25)



lb_est_1=Label(frame_sub_22, text= ("¿Cuantas clases faltas al semestre?"))
lb_est_1.config(bg=("DeepSkyBlue4"), fg=("white"), font=("Courier", 11, "italic"))
lb_est_1.place(x=70, y=110)

Imagen_2= PhotoImage(file="estudi.png")
lb_Imagen_2 =Label(frame_estudio, image=Imagen_2, bg="SkyBlue1")
lb_Imagen_2.place(x=200, y=15)

entry_a_5 = Entry(frame_sub_22)
entry_a_5.config(bg="white", fg= "green", font=("Helvetica",20))
entry_a_5.focus_set()
entry_a_5.place(x=180, y=145, width=100, height=30)




t_resultados_medic = Text(frame_sub_11)
t_resultados_medic.config(bg="black", fg="green", font=("courier",18))
t_resultados_medic.place(x=10, y=240, width=440, height= 105)


t_resultados_estud = Text(frame_sub_22)
t_resultados_estud.config(bg="black", fg="green", font=("courier",18))
t_resultados_estud.place(x=10, y=200, width=440, height= 145)





















ventana_principal.mainloop()