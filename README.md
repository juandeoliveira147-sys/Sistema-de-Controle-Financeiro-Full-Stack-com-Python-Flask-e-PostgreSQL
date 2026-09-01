# Controle Financeiro com Python, Flask e PostgreSQL

Aplicação web de controle financeiro desenvolvida com Python, Flask, PostgreSQL, HTML e CSS.

O sistema permite cadastrar receitas e despesas, visualizar o extrato financeiro, consultar o saldo total, editar movimentações e excluir registros por meio de uma interface web.

Este projeto é uma evolução de uma versão anterior do Controle Financeiro desenvolvida para o terminal. Nesta versão, a aplicação passou a utilizar uma interface acessível pelo navegador e um banco de dados PostgreSQL para armazenar as informações.

## Demonstrações

### Tela inicial


> <img width="1037" height="482" alt="Captura de tela 2026-09-01 124049" src="https://github.com/user-attachments/assets/0665955a-2fe8-4c9e-83de-a962e34550b2" />

### Extrato financeiro


> <img width="1016" height="465" alt="Captura de tela 2026-09-01 124118" src="https://github.com/user-attachments/assets/cbc6db7b-acc9-48d1-ac6e-0dfad59a62d3" />

## Funcionalidades

* Cadastro de receitas;
* Cadastro de despesas;
* Inclusão de descrição nas movimentações;
* Visualização do extrato financeiro;
* Cálculo automático do saldo total;
* Edição de movimentações;
* Alteração de descrição, valor e tipo;
* Exclusão de movimentações;
* Verificação de movimentações por ID;
* Registro automático de data e horário;
* Formatação de valores em Real Brasileiro;
* Armazenamento dos dados em PostgreSQL.

## Tecnologias utilizadas

* **Python** — desenvolvimento da lógica da aplicação;
* **Flask** — criação das rotas e integração entre backend e páginas HTML;
* **PostgreSQL** — armazenamento das movimentações financeiras;
* **HTML** — estrutura das páginas e formulários;
* **CSS** — estilização da interface.

> Este projeto não utiliza JavaScript. A comunicação entre a interface e o backend é realizada por meio de formulários HTML e requisições HTTP processadas pelo Flask.

## Como a aplicação funciona

A comunicação entre as partes do sistema ocorre da seguinte forma:

```text
Usuário
   ↓
HTML + CSS
   ↓
Flask
   ↓
Python
   ↓
PostgreSQL
```

Ao cadastrar uma receita ou despesa:

```text
Usuário preenche o formulário
        ↓
O formulário envia os dados
        ↓
O Flask recebe a requisição
        ↓
O Python processa as informações
        ↓
O PostgreSQL armazena a movimentação
        ↓
O usuário recebe uma resposta da aplicação
```

## Receitas e despesas

Para cadastrar uma movimentação, o usuário informa:

* Valor;
* Descrição;
* Tipo da movimentação.

O Flask recebe os dados por meio de uma requisição `POST`. Em seguida, o Python processa as informações e registra a movimentação no PostgreSQL junto com a data e o horário do cadastro.

As receitas são adicionadas ao saldo, enquanto as despesas são subtraídas.

```text
Receita
+ Valor

Despesa
- Valor

Resultado
= Saldo total
```

## Extrato financeiro

A página de extrato consulta as movimentações armazenadas no PostgreSQL e exibe os registros organizados por ID.

Além da listagem das movimentações, o sistema calcula automaticamente o saldo total com base nas receitas e despesas cadastradas.

## Edição de movimentações

O usuário pode editar uma movimentação informando o ID correspondente.

Antes da alteração, o sistema verifica se o registro existe no banco de dados. Caso seja encontrado, é possível alterar:

* Descrição;
* Valor;
* Tipo da movimentação.

Após a edição, os dados atualizados são salvos no PostgreSQL.

## Exclusão de movimentações

Também é possível excluir uma movimentação utilizando o ID.

O sistema verifica se o registro existe antes de realizar a exclusão. Caso o ID seja encontrado, a movimentação é removida do banco de dados.

## Estrutura do projeto

```text
Controle-Financeiro/
│
├── controle_financeiro_flask.py
├── banco_de_dados.py
│
├── templates/
│   ├── index.html
│   ├── receita.html
│   ├── despesa.html
│   ├── extrato.html
│   ├── alteracoes.html
│   ├── excluir_movimentacao.html
│   ├── sucesso.html
│   ├── excluido.html
│   └── id_nao_encontrado.html
│
└── static/
    └── estilo.css
```

### Principais arquivos

* `controle_financeiro_flask.py` — arquivo principal da aplicação e responsável pelas rotas do Flask;
* `banco_de_dados.py` — responsável pela conexão e operações com o PostgreSQL;
* `templates/` — contém as páginas HTML;
* `static/` — contém os arquivos CSS da aplicação.

## Banco de dados

O PostgreSQL é utilizado para armazenar permanentemente as movimentações financeiras.

Cada registro contém informações como:

```text
ID
Tipo
Valor
Data e horário
Descrição
```

Para criar a tabela utilizada pela aplicação, acesse o PostgreSQL, selecione o banco de dados do projeto e execute o seguinte comando SQL:

```sql
CREATE TABLE controlefinanceiro (
    id serial PRIMARY KEY,
    tipo varchar(20) NOT NULL,
    valor float NOT NULL,
    horario TIMESTAMP,
    descricao text
);
```

Exemplo de registro:

```text
ID: 1
Tipo: receita
Valor: 3000
Descrição: Pagamento mensal
Horário: 01/09/2026 12:00:00
```

## Instalação

### Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

* Python;
* PostgreSQL;
* Git.

### Clone o repositório

```bash
git clone https://github.com/juandeoliveira147-sys/Sistema-de-Controle-Financeiro-Full-Stack-com-Python-Flask-e-PostgreSQL
```

### Acesse a pasta do projeto

```bash
cd Sistema-de-Controle-Financeiro-Full-Stack-com-Python-Flask-e-PostgreSQL
```

### Instale as dependências

Instale o Flask:

```bash
pip install flask
```

Instale o driver do PostgreSQL:

```bash
pip install psycopg2
```

Configure o banco de dados

Crie um banco de dados chamado controlefinanceiro no PostgreSQL. Em seguida, conecte-se a esse banco e execute o comando SQL de criação da tabela apresentado na seção Banco de dados.

Depois, abra o arquivo banco_de_dados.py e configure os dados de acesso:

Usuário;
Senha;
Host;
Porta;
Nome do banco de dados.

Exemplo:

conect = pg.connect(
    user="postgres",
    password="sua_senha_aqui",
    host="127.0.0.1",
    port="5432",
    database="controlefinanceiro"
)

Substitua sua_senha_aqui pela senha definida no seu ambiente PostgreSQL.

### Execute a aplicação

```bash
python controle_financeiro_flask.py
```

Após iniciar o servidor, acesse no navegador o endereço informado pelo Flask.

## Objetivo do projeto

O objetivo deste projeto foi praticar o desenvolvimento de uma aplicação web utilizando:

* Python;
* Flask;
* PostgreSQL;
* HTML;
* CSS;
* Formulários HTML;
* Requisições HTTP;
* Rotas;
* Operações CRUD;
* Integração entre frontend, backend e banco de dados.

## Evolução do projeto

Este projeto representa a evolução de uma versão anterior do Controle Financeiro desenvolvida para o terminal.

A aplicação passou de um sistema executado no terminal para uma aplicação web com interface gráfica, rotas Flask e persistência de dados em PostgreSQL.

```text
Controle Financeiro — Terminal
              ↓
Python + arquivos
              ↓
Controle Financeiro — Aplicação Web
              ↓
Python + Flask
              ↓
HTML + CSS
              ↓
PostgreSQL
```

## Próximas melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* Categorias financeiras;
* Filtros de movimentações;
* Pesquisa avançada;
* Gráficos financeiros;
* Dashboard;
* Exportação de relatórios;
* API REST;
* Autenticação de usuários;
* Interface com JavaScript;
* Versão utilizando React.

## Autor

Desenvolvido por Juan Oliveira.

GitHub: [juandeoliveira147-sys](https://github.com/juandeoliveira147-sys)
