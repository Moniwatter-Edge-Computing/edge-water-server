# Hydric Monitoring System - Edge Server

## Sobre o Servidor

O servidor é o coração da camada de Edge Computing, responsável por receber, validar, tratar e armazenar os dados enviados pelo Moniwater MCD20.

Ele recebe os dados enviados pelo Moniwater, valida e trata essas informações, realizando o processamento necessário para facilitar a leitura, organização e análise dos dados.

Além disso, o servidor também permite a consulta dos dados armazenados e possibilita a criação de alertas personalizados, auxiliando no monitoramento hídrico em tempo real e no acompanhamento do histórico das informações coletadas.

---

## Tecnologias Utilizadas

```bash
- Python
- FastAPI
- Pydantic
- Uvicorn
- MySQL
- Banco NoSQL
- JWT
- HTTP/JSON
```

O servidor local está sendo desenvolvido utilizando Python, por sua flexibilidade e facilidade na criação de serviços voltados para recebimento, tratamento e processamento de dados.

Com o FastAPI, o servidor consegue disponibilizar rotas HTTP para receber os dados enviados pelo Moniwater MCD20, como conexão, status, eventos, consumos e configurações.

A biblioteca Pydantic é utilizada para validar os dados recebidos, garantindo que os payloads enviados pelo equipamento sigam uma estrutura esperada antes de serem tratados e armazenados.

O Uvicorn é utilizado como servidor ASGI, sendo responsável por executar a aplicação FastAPI e deixá-la disponível na rede local para receber requisições do Moniwater.

Para o armazenamento dos dados históricos, está prevista a utilização de um banco MySQL, responsável por guardar leituras, eventos, consumos e registros enviados pelo equipamento.

Também está prevista a utilização de um banco NoSQL para armazenar informações dos dispositivos cadastrados, como IMEI, moni_id, versão do dispositivo e dados de configuração.

A camada de comunicação principal entre o Moniwater e o servidor local será feita através de HTTP/JSON, permitindo que os dados sejam recebidos, tratados e posteriormente disponibilizados para visualização ou consumo por outras camadas do sistema.

A camada de segurança será baseada em JWT, permitindo que o servidor valide dispositivos autorizados e proteja rotas sensíveis da aplicação.


## Estrutura do projeto

Atualmente o projeto está organizado da seguinte forma:

```bash
edge-water-server/
├── app/
│   ├── auth/
│   │   └── __init__.py
│   │
│   ├── logs/
│   │   ├── __init__.py
│   │   └── logs_dispatch.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── payload.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── api_send.py
│   │   └── data_processorFor_api.py
│   │
│   ├── .env
│   ├── __init__.py
│   └── main.py
│
├── test/
│   ├── logs.py
│   ├── requirements.txt
│   └── test.py
│
└── .dockerignore
```

Essa estrutura foi separada por responsabilidade, facilitando a organização do servidor conforme o projeto for crescendo.

A ideia é evitar que todas as regras fiquem dentro das rotas. As rotas recebem as requisições, os schemas validam os dados, os services realizam o envio e o processamento dos dados, e a camada de logs registra as requisições recebidas pelo servidor.

---

# Resposabilidades

A pasta `auth` tem como responsabilidade concentrar a lógica de autenticação, geração e validação de JWT.

A pasta `logs` tem como responsabilidade enviar todas as requisições `HTTP` para o front-end de logs.

O arquivo `logs_dispatch.py` concentra a lógica responsável por capturar informações do cabeçalho requisição, como:

* `IP` do cliente;
* `Porta` acessada pelo cliente; 
* `Navegador` utilizado cliente ( caso a requisição tenha sido realizada por um navegador web );
* `Sistema` operacional do cliente dispositivo utilizado; 
* `Método` utilizado pelo cliente na requisição
* `Endpoint` acessado pelo cliente.
* `Data e hora atual` no momento em que foi enviado a requisição

Essa camada ajuda no debug e no monitoramento das requisições recebidas pelo servidor, principalmente para acompanhar quais rotas estão sendo acessadas e se as respostas estão retornando com sucesso ou erro.


A pasta `routes` tem como responsabilidade gerenciar os endpoints que o servidor expõe na rede, como:

O arquivo `payload.py` concentra as rotas principais de comunicação com o Moniwater, como:

* `/conecta` — endpoint de handshake inicial;
* `/enviastatus` — endpoint de recebimento dos dados de sensores do Moniwater;
* `/enviarconsumos` — endpoint de recebimento do código `moni_id`;
* `/enviareventos` — endpoint de recebimento dos eventos ocorridos no Moniwater, como alertas;
* `/enviaconfig1` — endpoint de recebimento das configurações do Moniwater.


A pasta `schemas` tem como responsabilidade definir, com a biblioteca Pydantic, como a estrutura dos dados deve ser.

O arquivo `schemas.py` concentra os modelos de validação dos payloads recebidos pelo servidor.

Essa camada valida se não faltou nenhum dado obrigatório e também pode realizar a conversão dos dados para os tipos corretos, caso os valores recebidos sejam compatíveis com os tipos definidos.

Como muitos dados enviados pelo Moniwater chegam em formato de `string`, os schemas ajudam a converter informações para tipos como:

```bash
- int
- float
- str
- list[int]
```

Exemplo:

```bash
fk_sistema -> int
hidrometro1 -> float
nivelPrcTanqueInferior -> int
entradasDigitais -> list[int]
```

O arquivo `main.py` é o ponto principal da aplicação.

Ele é responsável por criar a aplicação FastAPI, configurar a documentação conforme o ambiente, registrar o middleware de logs, criar a rota de health check e incluir as rotas do arquivo `payload.py`.

O arquivo `.env` concentra as variáveis de ambiente utilizadas pelo servidor, como ambiente de execução, URL do serviço de logs e URL da API de destino.

Esse arquivo é importante para separar configurações sensíveis ou variáveis do código-fonte.

A pasta `test` tem como responsabilidade concentrar arquivos utilizados para testes locais do servidor.

O arquivo `test.py` é utilizado para testar automaticamente as rotas principais do servidor, simulando requisições para endpoints como `/conecta`, `/enviastatus`, `/enviareventos` e `/enviarconsumos`.

O arquivo `logs.py` pode ser utilizado para simular ou testar o recebimento dos logs enviados pelo servidor.

O arquivo `requirements.txt` dentro da pasta `test` concentra as dependências necessárias para executar os testes dessa camada, caso ela seja executada de forma separada.

O arquivo `.dockerignore` tem como responsabilidade definir quais arquivos ou pastas não devem ser enviados para o contexto de build do Docker.

Ele ajuda a evitar que arquivos desnecessários, como ambiente virtual, cache do Python e arquivos locais, sejam incluídos na imagem Docker.



