from tkinter import *

tabla = Tk()
tabla.title("Tabla de proveedores")
tabla.geometry("1220x720")
tabla.config(bg="#5f9ea0")
encabezado = Label(tabla, text="Tabla de proveedores", bd=5, relief=SUNKEN,
font=("Arial black", 20), bg="#006690",fg="lime").pack(fill=X)

informacion = LabelFrame(tabla, text="Area de informacion",font=("Arial black", 12), bg="#006690",
    fg="lime", bd=8)
informacion.place(x=0, y=90, relwidth=1) 

canal = Label(informacion, text="Canal:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=0, column=0,padx=8)
canal_entry = Entry(informacion,borderwidth=4,width=5).grid(row=0,column=1,padx=8)

registro = Label(informacion, text="Registro:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=0, column=2,padx=8)
registro_entry = Entry(informacion,borderwidth=4,width=21).grid(row=0,column=3,padx=8)

factura = Label(informacion, text="Fecha factura:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=0, column=4,padx=8)
factura_entry = Entry(informacion,borderwidth=4,width=21).grid(row=0,column=5,padx=8)

año = Label(informacion, text="Año:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=0, column=6,padx=8)
año_entry = Entry(informacion,borderwidth=4,width=15).grid(row=0,column=7,padx=8)

deposito = Label(informacion, text="Deposito:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=0, column=8,padx=8)
deposito_entry = Entry(informacion,borderwidth=4,width=15).grid(row=0,column=9,padx=8)

proveedor = LabelFrame(tabla, text="Informacion del proveedor",font=("Arial black", 12),
    bg="#006690",fg="lime",bd=8)
proveedor.place(x=5, y=170, height=180,width=670)  

codigo = Label(proveedor, text="Codigo del proveedor:",font=("Arial black", 12),
bg="#006690",fg="lime").grid(row=0,column=0,padx=8)
codigo_entry = Entry(proveedor,borderwidth=4,width=21).grid(row=0,column=1,padx=8)

n_factura = Label(proveedor, text="Numero factura:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=1, column=0,padx=8)
n_factura_entry = Entry(proveedor,borderwidth=4,width=21).grid(row=1,column=1,padx=8)

serie = Label(proveedor, text="Serie:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=1, column=2,padx=8) 
serie_entry = Entry(proveedor,borderwidth=4,width=21).grid(row=1,column=3,padx=8)

fecha1 = Label(proveedor, text="Desde fecha:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=2, column=0,padx=8)
fecha1_entry = Entry(proveedor,borderwidth=4,width=21).grid(row=2,column=1,padx=8)

fecha2 = Label(proveedor, text="Hasta fecha:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=2, column=2,padx=8)
fecha2_entry = Entry(proveedor,borderwidth=4,width=21).grid(row=2,column=3,padx=8)

frame1 = Frame(tabla, bd=10,bg="#006690")
frame1.place(x=660, y=375,width=550,height=250)

comentarios = Label(frame1, text="Area de comentarios",font=("Arial black", 12),
bg="#006690",fg="lime").pack(fill=X)

texarea = Text(frame1)
texarea.pack(fill=BOTH, expand=1)

frame2 = Frame(tabla,bd=10,bg="#006690")
frame2.place(x=5, y=375,width=585,height=250)

datos1 = Label(frame2, text="Base IVA 1:",font=("Arial black", 12),
bg="#006690",fg="lime").grid(row=0,column=0,padx=8)
datos1_entry = Entry(frame2,borderwidth=4,width=21).grid(row=0,column=1,padx=8)

datos2 = Label(frame2, text="Base IVA 2:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=1, column=0,padx=8)
datos2_entry = Entry(frame2,borderwidth=4,width=21).grid(row=1,column=1,padx=8)

datos3 = Label(frame2, text="Base IVA 3:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=2, column=0,padx=8)
datos3_entry = Entry(frame2,borderwidth=4,width=21).grid(row=2,column=1,padx=8)


datos4 = Label(frame2, text="%REC 1:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=3, column=0,padx=8)
datos4_entry = Entry(frame2,borderwidth=4,width=21).grid(row=3,column=1,padx=8)

datos5 = Label(frame2, text="%REC 1:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=4, column=0,padx=8)
datos5_entry = Entry(frame2,borderwidth=4,width=21).grid(row=4,column=1,padx=8)

datos6 = Label(frame2, text="%REC 1:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=5, column=0,padx=8)
datos6_entry = Entry(frame2,borderwidth=4,width=21).grid(row=5,column=1,padx=8)

datos7 = Label(frame2, text="Importe IVA 1:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=0, column=2,padx=8)
datos7_entry = Entry(frame2,borderwidth=4,width=21).grid(row=0,column=3,padx=8)

datos8 = Label(frame2, text="Importe IVA 2:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=1, column=2,padx=8)
datos8_entry = Entry(frame2,borderwidth=4,width=21).grid(row=1,column=3,padx=8)

datos9 = Label(frame2, text="Importe IVA 3:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=2, column=2,padx=8)
datos9_entry = Entry(frame2,borderwidth=4,width=21).grid(row=2,column=3,padx=8)

datos10 = Label(frame2, text="Importe Bruto:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=3, column=2,padx=8)
datos10_entry = Entry(frame2,borderwidth=4,width=21).grid(row=3,column=3,padx=8)

datos11 = Label(frame2, text="Importe Neto:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=4, column=2,padx=8)
datos11_entry = Entry(frame2,borderwidth=4,width=21).grid(row=4,column=3,padx=8)

datos12 = Label(frame2, text="Impuestos:",font=("Arial black", 12),bg="#006690",
fg="lime").grid(row=5, column=2,padx=8)
datos12_entry = Entry(frame2,borderwidth=4,width=21).grid(row=5,column=3,padx=8)

botones = LabelFrame(tabla, text="Botones",font=("Arial black", 12),bg="#006690",
    bd=5,fg="lime")
botones.place(x=0, y=610, relwidth=1, height=100) 

boton_insertar = Button(botones, text="Insertar", width=15,font=("Arial black", 12),
pady=10,bg="#006690",fg="lime").grid(row=0,column=1,padx=20,pady=6)

button_limpiar = Button(botones, text="Limpiar",  font=("Arial Black", 12), 
pady=10, bg="#006690",fg="lime", width=15).grid(row=0, column=2, padx=300, pady=6)

button_salir = Button(botones, text="Salir", font=("Arial Black", 12), 
pady=10, bg="#006690",fg="lime", width=15).grid(row=0, column=3, padx=20, pady=6)

tabla.mainloop()