pytesseract.pytesseract.tesseract_cmd = "C:/Users/Carlos André-DIGITAL/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
texto = pytesseract.image_to_string(imagem) 
print(texto)
