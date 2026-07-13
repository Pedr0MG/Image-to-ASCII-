from PIL import Image
import sys

ascii_char = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

imagem = Image.open(sys.argv[1]).convert("L")

largura_original, altura_original = imagem.size

proporcao = altura_original / largura_original

nova_altura = int(300 * proporcao * 0.45)

imagem_redimensionada = imagem.resize((300, nova_altura))

pixels = imagem_redimensionada.get_flattened_data()

caracteres_ascii = []
for pixel in pixels: 
    posicao = (pixel * len(ascii_char))//256 
    caractere = ascii_char[posicao]
    caracteres_ascii.append(caractere)

texto_completo = "".join(caracteres_ascii) 

arte_final = "" 

for i in range (0, len(texto_completo), 300):
    linha = texto_completo[i : i + 300]
    arte_final += linha + "\n"

with open("resultado.txt", "w") as arquivo:
    arquivo.write(arte_final)