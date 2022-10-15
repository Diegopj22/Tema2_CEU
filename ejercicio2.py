texto="un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
texto2=texto.split("#")
for contador,frase in enumerate(texto2):
    texto2[contador]=frase.capitalize()
    if contador == 0:
        texto2[contador]=texto2[contador]+"..."
    else:
        texto2[contador]="-"+texto2[contador]+"."
for i in texto2:
    print(i)


 
    
        
    


