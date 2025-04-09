# Dicionários de Código Morse
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


# Cifra de César (pode criptografar letras e números)
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


# Texto → Código Morse
def para_morse(texto):
    morse = ''
    for char in texto.upper():
        if char in morse_dict:
            morse += morse_dict[char] + ' '
        else:
            morse += char + ' '
    return morse.strip()


# Código Morse → Texto
def de_morse(morse_string):
    letras = morse_string.strip().split()
    texto = ''
    for m in letras:
        if m in morse_dict_reverso:
            texto += morse_dict_reverso[m]
        else:
            texto += '?'  # caractere desconhecido
    return texto


# Criptografar personalizado
def criptografar_personalizado(texto, deslocamento=9):
    palavras = texto.split()
    resultado_final = []

    for palavra in palavras:
        palavra_cesar = cifra_cesar(palavra, deslocamento)
        palavra_morse = para_morse(palavra_cesar)

        if len(palavra) % 2 == 0:
            palavra_morse += '.'  # ponto extra no fim
        else:
            palavra_morse = '.' + palavra_morse  # ponto extra no início

        palavra_repetida = ' '.join([palavra_morse] * len(palavra))
        resultado_final.append(palavra_repetida)

    return ' | '.join(resultado_final)  # separador de palavras


# Descriptografar personalizado
def descriptografar_personalizado(texto, deslocamento=9):
    palavras_codificadas = texto.split(" | ")
    resultado = []

    for bloco in palavras_codificadas:
        morse_lista = bloco.strip().split()
        total = len(morse_lista)
        if total == 0:
            continue

        # Detecta tamanho real da palavra (quantas vezes foi repetida)
        for i in range(1, total + 1):
            if total % i == 0:
                # tenta com esse tamanho
                trecho = morse_lista[:i]
                if trecho * (total // i) == morse_lista:
                    unidade_morse = ' '.join(trecho)
                    break
        else:
            unidade_morse = ' '.join(morse_lista)

        # Remove ponto extra
        if unidade_morse.startswith('.'):
            unidade_morse = unidade_morse[1:]
        elif unidade_morse.endswith('.'):
            unidade_morse = unidade_morse[:-1]

        # Morse para texto (em maiúsculo)
        texto_morse = de_morse(unidade_morse)

        # Reverter cifra de césar
        texto_final = cifra_cesar(texto_morse.lower(), deslocamento, modo='descriptografar')
        resultado.append(texto_final)

    return ' '.join(resultado)


# Menu principal
def main():
    modo = input("Você deseja:\n1 - Criptografar\n2 - Descriptografar\n")

    if modo == '1':
        texto_original = input("Digite o texto para criptografar:\n")
        criptografado = criptografar_personalizado(texto_original)
        print("\nTexto Criptografado:\n", criptografado)

    elif modo == '2':
        texto_criptografado = input("Digite o texto criptografado:\n")
        descriptografado = descriptografar_personalizado(texto_criptografado)
        print("\nTexto Descriptografado:\n", descriptografado)

    else:
        print("Opção inválida!")

# Executa o programa
main()
