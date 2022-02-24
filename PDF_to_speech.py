import gtts
from PyPDF2 import PdfFileReader
file = input("Enter the file's name you want to read: ")
temp = open(file+'.PDF', 'rb')
PDF_read = PdfFileReader(temp)
index = PDF_read.getNumPages()
text_list = []
for i in range(index):
  page = PDF_read.getPage(i)
  text_list.append(page.extractText())
text_string = " ".join(text_list)
print(text_string)
language = 'es'
tts = gtts.gTTS(text=text_string, lang=language, slow=True)
tts.save("Part1.mp3")
#while(index < PDF_read.getNumPages()):
  #first_page = PDF_read.getPage(index)
  #print(first_page.extractText())
  #index+=1