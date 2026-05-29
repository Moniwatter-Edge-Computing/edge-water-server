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
app/
├── auth/
│   └── __init__.py
│
├── logs/
│   ├── __init__.py
│   └── logs_dispatch.py
│
├── routes/
│   ├── __init__.py
│   └── payload.py
│
├── schemas/
│   ├── __init__.py
│   └── schemas.py
│
├── __init__.py
└── main.py
```

# Resposabilidades

A estrutura foi separada por responsbilidade, facilitando a organização do servidor, conforme o projeto for crescendo

A pasta `auth` tem como responsabilidade concentrar a lógica de autenticação, geração e validação de JWT.

A pasta `logs` tem como responsabilidade enviar todas as requisições `HTTP` para o front-end de logs,
contendo informações do cabeçalho das requisições recebidas no servidor, como: 

* `IP` do cliente;
* `Porta` acessada pelo cliente; 
* `Navegador` utilizado cliente ( caso a requisição tenha sido realizada por um navegador web );
* `Sistema` operacional do cliente dispositivo utilizado; 
* `Método` utilizado pelo cliente na requisição
* `Endpoint` acessado pelo cliente.

A pasta `routes` tem como responsabilidade gerenciar os endpoints que o servidor expõe na rede, como:

* `/conecta` — endpoint de handshake inicial;
* `/enviastatus` — endpoint de recebimento dos dados de sensores do Moniwater;
* `/enviarconsumos` — endpoint de recebimento do código `moni_id`;
* `/enviareventos` — endpoint de recebimento dos eventos ocorridos no Moniwater, como alertas;
* `/enviaconfig1` — endpoint de recebimento das configurações do Moniwater.

A pasta `schemas` tem como responsabilidade definir com a biblioteca Pydantic definir como a estrutura de dados deve ser e também validar se não faltou nenhum dado, além de também já realizar a convserão desses dados para os seus tipos corretos ( caso venham todos os dados definidos na estrutura ).

---

## Logs e controle de requisições

Também foi iniciado o controle das requisições recebidas pela API.

Através do objeto `Request` do FastAPI, é possível capturar informações como:

```bash
- método HTTP utilizado
- rota acessada
- payload enviado
```

Isso ajuda durante o desenvolvimento e debug da aplicação, principalmente para entender quais rotas estão sendo acessadas pela Edge Computing e quais dados estão chegando na API.

Futuramente, essa estrutura poderá ser expandida para registrar logs de sucesso, logs de erro, tentativas inválidas de acesso e falhas de validação.

--- 

