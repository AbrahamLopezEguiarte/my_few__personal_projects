# Se importan los módulos para extraer texto y convertir de texto a mp3 (gtts) y para abrir y leer PDF (PyPDF2) 
import gtts
from PyPDF2 import PdfFileReader
# file sirve para indicar el archivo PDF que deseamos convertir a mp3
file = input("Enter the file's name you want to read: ")
# temp nos ayuda a abrir de forma binaria y en modo lectura nuestro archivo, agregando la terminación .PDF a file
temp = open(file+'.PDF', 'rb')
# PDF_read nos ayuda a utilizar la función PdfFileReader para leer el archivo por medio de la variable temp
PDF_read = PdfFileReader(temp)
# Utilizamos index para almacenar la cantidad de páginas de nuestro archivo
index = PDF_read.getNumPages()
# Creamos una lista vacía en donde almacenaremos el contenido de cada página
text_list = []
# Iniciamos un for loop para recorrer cada página
for page in range(index):
  # Almacenaremos cada página en la variable page
  page = PDF_read.getPage(page)
  # Extraeremos el texto de page y lo añadiremos a nuestra lista
  text_list.append(page.extractText())
# Haremos un join al contenido de nuestra lista para separar las cadenas con un espacio
text_string = " ".join(text_list)
# Imprimimos nuestra cadena de modo que visualicemos el contenido que será convertido
print(text_string)
# Indicamos el idioma que deseamos para nuestro archivo mp3 en la variable language
language = 'es'
# tts nos servirá para indicar el texto que deseamos convertir, el idioma y, en caso de desearlo, marcar como True la propiedad slow para hacer que el audio se ralentice
tts = gtts.gTTS(text=text_string, lang=language, slow=True)
# Finalmente usamos tts para guardar el texto transformado a audio en un archivo mp3
tts.save("Part1.mp3")