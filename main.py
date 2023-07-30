from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import Converter
from urllib import request

root = Tk()
root.title('Convertidor de Archivos')
root.resizable(0, 0)
root.iconbitmap('icon.ico')
root.geometry('300x85')

Label(root,text='Convierte archivos de Word a Pdf y de Pdf a Word',fg='red').grid(row=0,column=0,columnspan=2)

def Buscar_Archivo_Word():
    archivo = filedialog.askopenfilename(
        title='Selecciona Archivos Word', filetypes=[('Archivos Word', '*.docx')])
    convert(archivo)
    showinfo(title='Mensaje', message='El Archivo se Convirtio a Pdf Correctamente')


Label(root, text='Selecciona el Archivo Word : ').grid(row=1,column=0)
Button(root, text='Convertir de Word a Pdf',bg='blue',
       command=Buscar_Archivo_Word).grid(row=1,column=1)


def Buscar_Archivo_Pdf():
    archivo = filedialog.askopenfilename(
        title='Selecciona Archivos Pdf', filetypes=[('Archivos Pdf', '*.pdf')])
    cv = Converter(archivo)
    cv.convert(archivo+'.docx')
    cv.close()
    showinfo(title='Mensaje',
             message='El Archivo se Convirtio a Word Correctamente')


Label(root, text='Seleccionar Archivo Pdf : ').grid(row=2,column=0)
Button(root, text='Convertir de Pdf a Word',bg='red',
       command=Buscar_Archivo_Pdf).grid(row=2,column=1)

root.mainloop()
