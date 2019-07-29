Esta aplicação foi desenvolvida em Python 3 e cria um servidor HTTP que, para cada requisição GET, retorna um JSON cuja chave `extenso` é a versão por extenso do número inteiro enviado no path. Os números devem estar no intervalo [-99999, 99999].

Exemplo:  
```
λ curl http://localhost:3000/94587  
{"extenso": "noventa e quatro mil e quinhentos e oitenta e sete"}
```

## Requisitos
<ul>
  <li>Python 3.5 </li>
  <li>Request 2.7</li>
</ul>

## Iniciando o servidor

Para iniciar o servidor execute o arquivo `start_server.py`, como segue:  
`$ python3 start_server.py`

O arquivo `start_server.py` instancia um servidor HTTP na porta 3000. O comportamento do servidor HTTP é descrito pelo arquivo `appserver/server.py`. 

Um Docker do servidor foi criado e está disponível em <a href=https://hub.docker.com/r/laisborin/desafio>https://hub.docker.com/r/laisborin/desafio</a>. Se possuir o Docker instalado em sua máquina, basta digitar os seguintes comando para baixar e executar o docker:  
`$ docker pull laisborin/desafio`  
`$ docker run --rm -ti -p 3000:3000 laisborin/desafio`  
Ao executar o comando acima, o servidor será imediatamente instanciado na porta 3000 do docker. Ainda, o docker passa a escutar  também na porta 3000 da máquina local.

Qualquer problema ao executar o docker, favor entrar em contato pelo e-mail: borin.lais@gmail.com

## Descrição geral do diretório

Diretório `appserver`:  
<ul>
  <li>server.py: descreve o servidor HTTP</li>
  <li>validate.py: valida a entrada de um número no intervalo [-99999, 99999]</li>
  <li>translate.py: traduz um número inteiro para sua versão em extenso</li>
</ul>

Diretório `tests`:  
<ul>
  <li>test_server.py: testa o método da classe Server (é necessário iniciar o servidor antes de rodar o teste)</li>
  <li>test_validate.py: testa os métodos da classe Validate</li>
  <li>test_translate.py: testa os métodos da classe Translate</li>
</ul>  
start_server: inicia o servidor descrito no arquivo server.py na porta 3000.
