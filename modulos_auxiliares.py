import hashlib
from datetime import date,datetime
import os

# Aqui é o core desse programa, a seguir vamos fazer uma versão melhorada do mesmo
# string = input("Digite o texto a ser gerado a hash: ")
# resultado = hashlib.md5(string.encode('utf-8'))
#
# print("O hash da string é:",resultado.hexdigest())



class Dados:
     def __init__(self,dados) -> None:
        prompt = dados['prompt']
        seed = dados['seed']
        path = dados['path']
        hash = dados['hash']



# Altera os espaços por underline("_")
def separa_palavras(prompt):
    separator = '_'
    prompt = prompt.split()
    prompt = [separator.join(prompt)]  
    return prompt[0]

# adiciona o timestamp para inserir como nome o arquivo
def novo_nome_arquivo(string):
    string = separa_palavras(string)
    data_hora=datetime.now().timestamp()
    print(111,data_hora)
    nova_string = string+"_"+str(data_hora)
    return nova_string


def gerador_de_hash(string):
    string=string+"-"+str(datetime.now())
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("O hash SHA1 da string:",string,'é:',resultado.hexdigest())
    print("Hash SHA1 criado para o arquivo")
    return resultado.hexdigest()


if __name__ == '__main__':     
    data = datetime.now()
    print(data)
    data = data.timestamp()
    print(data)
