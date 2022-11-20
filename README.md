# sd_replicate-api
Integração da API do replicate com código em python.

<H2>Utilização</H2>
Para usá-lo, primeiramente, é necessário instalar um ambiente virtual python e ativar o mesmo, através do comando no terminal:
    python3 -m venv env
    python3 ./env/bin/activate

Logo, deve-se instalar a biblioteca do replicate (com o ambiente devidamente ativado):
    pip install replicate

Depois de ativado é necessário exportar a chave da API
    export REPLICATE_API_TOKEN=[token]

    
<h2>Como Funciona?</h2>
Ao iniciar é o arquivo <b>main.py</b> será pedido o prompt para geração da imagem (como entrada). Logo a predição será sava dentro do diretório <b>media</b>, para isso será necessário criar a pasta previamente antes de iniciar a aplicação.

A imagem gerada será salva com o nome da predição (será substituido os espaços pos underline) e timestamp concatenados.
