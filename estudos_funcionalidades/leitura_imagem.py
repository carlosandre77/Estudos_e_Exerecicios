import pytesseract
import cv2
import re

#importar imagem e transformar em texto
imagem = cv2.imread("momo.jpeg")

#"C:\Users\Carlos André-DIGITAL\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = "C:/Users/Carlos André-DIGITAL/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
texto = pytesseract.image_to_string(imagem) 

#texto2 = texto.replace('”','xxxxx')
print(str(texto))


#extrair caracteres numericos

#texto = " - Coordenadas geográficasPonto 1: Latitude 30°05'103\"S e Longitude 52°51'22.1\"W Ponto 2: Latitude 30°05'38.7\"S e Longitude 52°51'26.5\"W Ponto 3: Latitude 30°05'46.2\"S e Longitude 52°50'43.7\"WPonto 4: Latitude 30°05'19.7\"S e Longitude 52°50'39.5\"W As coordenadas são 56°55'7\" sul e 5°2'79\" leste depoi  5°7'8\" norte 70°60\'"
padrao = r'\d+°\d+\’\d+”'


texto_final = texto

lst =[]
i=0
cond = True


while cond:    
    resultado = re.search(padrao, texto_final)
    if resultado:
        numero = resultado.group(0)
        lst.append(numero)
        print(numero)
        texto_final.replace(numero, ' ')
        texto_final = texto_final.replace(numero, ' ')
        
    else:
        cond=False
        print("Não foi encontrado nenhum número")
        
print(lst)