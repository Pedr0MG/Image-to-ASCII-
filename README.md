# 🇧🇷 Conversor de Imagem para ASCII Art 

Um script em Python desenvolvido do zero que transforma qualquer imagem comum (`.jpg`, `.jpeg`, `.png`) em uma arte visual feita puramente de caracteres ASCII. O projeto analisa a densidade de brilho de cada pixel para mapear o caractere correspondente, gerando resultados impressionantes em alta resolução diretamente em arquivos de texto.

------------------------------------------------------------------------------------------------------------------------------------------

## Como Funciona? 

O algoritmo foi construído seguindo conceitos fundamentais de processamento digital de imagens e computação gráfica:

1. **Escala de Cinza:** A imagem colorida (RGB) é convertida para o modo de luminância, onde cada pixel se torna um valor numérico entre `0` (preto absoluto) e `255` (branco absoluto).
2. **Redimensionamento Proporcional:** A imagem é reduzida para a largura desejada. Como os caracteres do terminal são retangulares (mais altos do que largos), o script aplica um fator de correção geométrico para que a arte final não fique esticada ou distorcida.
3. **Mapeamento de Brilho:** Usando uma rampa com quase 70 níveis de caracteres ordenados por densidade de "tinta" (ex: `@` para áreas escuras e `.` para áreas claras), o script faz uma divisão inteira para converter o valor do pixel no índice correspondente da string.
4. **Estruturação:** A fila linear de caracteres convertidos é fatiada na largura exata da imagem, adicionando quebras de linha (`\n`) e exportando o resultado.

------------------------------------------------------------------------------------------------------------------------------------------

## Tecnologias Utilizadas

* **Python 3.14** (ou superior)
* **Pillow (PIL):** Para carregamento, conversão de cor e redimensionamento da imagem.
* **Sys:** Para captura de argumentos dinâmicos via linha de comando.

------------------------------------------------------------------------------------------------------------------------------------------
# 🇺🇸 ImgToAscii - Image to ASCII Art Converter

A Python script built from scratch that transforms any common image (`.jpg`, `.jpeg`, `.png`) into visual art made purely of ASCII characters. The project analyzes the brightness density of each pixel to map it to its corresponding character, generating impressive high-resolution results directly into text files.

------------------------------------------------------------------------------------------------------------------------------------------

## How It Works? 

The algorithm was built following fundamental concepts of digital image processing and computer graphics:

1. **Grayscale Conversion:** The colored image (RGB) is converted into luminance mode, where each pixel becomes a numerical value between `0` (absolute black) and `255` (absolute white).
2. **Proportional Resizing:** The image is downscaled to the desired width. Since terminal characters are rectangular (taller than they are wide), the script applies a **geometric correction factor** so the final art doesn't look stretched or distorted.
3. **Brightness Mapping:** Using a professional ramp of nearly 70 characters ordered by "ink" density (e.g., `@` for dark areas and `.` for light areas), the script performs an integer division to map the pixel value to the corresponding string index.
4. **Structuring:** The linear sequence of converted characters is sliced at the exact width of the image, adding line breaks (`\n`) and exporting the final output.

------------------------------------------------------------------------------------------------------------------------------------------

## Technologies Used

* **Python 3.14** (or higher)
* **Pillow (PIL):** For image loading, color conversion, and resizing.
* **Sys:** For capturing dynamic arguments via the command line (CLI).
