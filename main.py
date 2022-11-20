import replicate
#import webbrowser
import os
from modulos_auxiliares import *

prompt_input = input("Digite o prompt para gerar imagem: ")
model = replicate.models.get("stability-ai/stable-diffusion")
output_url = model.predict(prompt=prompt_input)[0]
#print(output_url)

nome_arquivo = novo_nome_arquivo(prompt_input)
gerador_de_hash(prompt_input)

ave_path='media/'
os.system("wget -cO - {} > media/{}.png".format(output_url,nome_arquivo))

# reune os dados p

#abre o navegador com a imagem gerada
#webbrowser.open(output_url)