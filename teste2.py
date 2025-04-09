import streamlit as st

def cifra_cesar(texto, deslocamento=9, modo="Criptografar"):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if modo == "Criptografar":
                resultado += chr((ord(char) - base + deslocamento) % 26 + base)
            elif modo == "Descriptografar":
                resultado += chr((ord(char) - base - deslocamento) % 26 + base)
        else:
            resultado += char 
    return resultado

st.title("App de criptografar e descriptografar")

texto = st.text_input("Digite o texto:")
modo = st.radio("Escolha o modo:", ("Criptografar", "Descriptografar"))

deslocamento = 9  

if st.button("Executar"):
    resultado = cifra_cesar(texto, deslocamento, modo)
    st.text_area("Resultado:", resultado, height=100)
