texto="un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
texto2=texto.split("#")
for i in texto2:
    
    if i == 0:
        texto2[i]=texto2[i]+"..."  

    print(i.capitalize())


