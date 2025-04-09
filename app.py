import streamlit as st

# Dicionários Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..',
    '0': '-----', '1': '.----','2': '..---','3': '...--',
    '4': '....-', '5': '.....','6': '-....','7': '--...',
    '8': '---..', '9': '----.'
}
morse_dict_reverso = {v: k for k, v in morse_dict.items()}


def cifra_cesar(texto, deslocamento, modo='criptografar'):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if modo == 'criptografar':
                resultado += chr((ord(char) - base + deslocamento) % 26 + base)
            else:
                resultado += chr((ord(char) - base - deslocamento) % 26 + base)
        elif char.isdigit():
            if modo == 'criptografar':
                resultado += chr((ord(char) - ord('0') + deslocamento) % 10 + ord('0'))
            else:
                resultado += chr((ord(char) - ord('0') - deslocamento) % 10 + ord('0'))
        else:
            resultado += char
    return resultado

def para_morse(texto):
    morse = ''
    for char in texto.upper():
        if char in morse_dict:
            morse += morse_dict[char] + ' '
        else:
            morse += char + ' '
    return morse.strip()

def de_morse(morse_string):
    letras = morse_string.strip().split()
    texto = ''
    for m in letras:
        if m in morse_dict_reverso:
            texto += morse_dict_reverso[m]
        else:
            texto += '?'
    return texto

def criptografar_personalizado(texto, deslocamento=9):
    palavras = texto.split()
    resultado_final = []

    for palavra in palavras:
        palavra_cesar = cifra_cesar(palavra, deslocamento)
        palavra_morse = para_morse(palavra_cesar)

        if len(palavra) % 2 == 0:
            palavra_morse += '.'
        else:
            palavra_morse = '.' + palavra_morse

        palavra_repetida = ' '.join([palavra_morse] * len(palavra))
        resultado_final.append(palavra_repetida)

    return ' | '.join(resultado_final)

def descriptografar_personalizado(texto, deslocamento=9):
    palavras_codificadas = texto.split(" | ")
    resultado = []

    for bloco in palavras_codificadas:
        morse_lista = bloco.strip().split()
        total = len(morse_lista)
        if total == 0:
            continue

        for i in range(1, total + 1):
            if total % i == 0:
                trecho = morse_lista[:i]
                if trecho * (total // i) == morse_lista:
                    unidade_morse = ' '.join(trecho)
                    break
        else:
            unidade_morse = ' '.join(morse_lista)

        if unidade_morse.startswith('.'):
            unidade_morse = unidade_morse[1:]
        elif unidade_morse.endswith('.'):
            unidade_morse = unidade_morse[:-1]

        texto_morse = de_morse(unidade_morse)
        texto_final = cifra_cesar(texto_morse.lower(), deslocamento, modo='descriptografar')
        resultado.append(texto_final)

    return ' '.join(resultado)

# Interface Streamlit
st.set_page_config(page_title="Cripto", layout="centered")

st.title("🔐 Cripto")


modo = st.radio("Escolha a operação:", ["Criptografar", "Descriptografar"])
texto = st.text_area("Digite o texto aqui:")

if st.button("Executar"):
    if modo == "Criptografar":
        resultado = criptografar_personalizado(texto)
        st.success("Texto Criptografado:")
        st.code(resultado, language="text")
    else:
        resultado = descriptografar_personalizado(texto)
        st.success("Texto Descriptografado:")
        st.code(resultado, language="text")
