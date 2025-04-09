deslocamento = 9
def cifra_cesar(texto, deslocamento, modo):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if modo == "criptografar":
                resultado += chr((ord(char) - base + deslocamento) % 26 + base)
            elif modo == "descriptografar":
                resultado += chr((ord(char) - base - deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado


modo = input("Você deseja:\n1 - Criptografar\n2 - Descriptografar\n")

if modo == '1':
    texto = input("Insira o texto para criptografar: \n")
    
    print("Texto Criptografado:", cifra_cesar(texto, deslocamento, "criptografar"))

elif modo == '2':
    texto = input("Insira o texto para descriptografar: \n")
    
    print("Texto Descriptografado:", cifra_cesar(texto, deslocamento, "descriptografar"))

else:
    print("Opção inválida!")
