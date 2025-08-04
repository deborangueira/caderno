# Descrição

- Construção de um **sistema Web** seguindo a arquitetura MVC

- Servidor configurado com Node.js e Express.js
    instalar as dependências:
    1. npm init: adiciona o arquivo package.json que guarda as dependências
    2. npm install express: cria a pasta node_modules e o arquivo package-lock.json

- Interface desenvolvida com EJS

# Tecnologias

### Supabase  <img src="https://skillicons.dev/icons?i=supabase,postgresql" height="25"/>

- Plataforma de desenvolvimento em núvem que :
    - Utiliza como padrão o banco de dados PostgreSQL**, que trás para a aplicação os benefícios de:
        1. Se tornar capaz de lidar com grandes volumes de dados e ser altamente escalável, permitindo que cresçam de acordo com as necessidades do negócio sem comprometer a integridade dos dados ou a performance.
        2. Utilizar o SQL (structured queries language)
    - API RESTful: permitem que diferentes plataformas e sistemas se comuniquem 
    - Permite autenticação
    - Atualiza de forma síncrona conforme os dados do banco de dados são atualizados
    
    > **PostgreSQL** é um tipo de **sistema gerenciador de banco de dados objeto-relacional**

    > **SQL - Structured Query language** (*linguagem de consulta estruturada*)
    - Linguagem de consulta de banco de dados universal (utilizada para fazer consulta e manipulação)
    - É universal: funciona em qualquer programa (postgre, mySQL,  oracle...)
    - Comandos:

        | Comando SQL  | Pergunta / Descrição                                      | Frequência   |
        |--------------|------------------------------------------------------------|--------------|
        | `SELECT`     | Quais **CAMPOS** você quer retornar com sua query          | SEMPRE       |
        | `FROM`       | Quais **TABLES** (tabelas) você quer usar?                 | SEMPRE       |
        | `WHERE`      | Quais **FILTROS** você deseja aplicar                      | FREQUENTE    |
        | `GROUP BY`   | Quais **CAMPOS** você deseja agrupar                       | FREQUENTE    |
        | `ORDER BY`   | Quais **CAMPOS** você quer usar para ordenar               | ÀS VEZES     |
        | `JOIN`       | Junta ou agrega 2 ou mais tabelas                          | ÀS VEZES     |
        | `CASE`       | Condicional                                                | ÀS VEZES     |
        | `SUBSELECT`  | Aplicar subtabelas                                         | ÀS VEZES     |
        | `LIMIT`      | **QUANTAS LINHAS** você deseja retornar?                   | ÀS VEZES     |

        >Obs.: ler sobre paginação

    - exemplos:
        ```Javascript
        SELECT nome, idade FROM clientes WHERE Estado ='São Paulo' and genero = "Feminino";

        SELECT count(*) FROM clientes; // Calcula o total das linhas presentes na tabela

        SELECT escolaridade, count(*) FROM clientes GROUP BY escolaridade // calcula o total de linhas da tabela, agrupando os dados de acordo com a escolaridade.
        ```
        > `*` significa "todas"

- **node.js**
    - Ambiente de execução do código JavaScript específica para back-end. 

- **npm/pip** <img src="https://skillicons.dev/icons?i=npm" height="25"/> 
    - gerenciador de pacotes

- **Json**
    - 

# Bibliotecas
dotenv: salva as informações do banco de dados para que seja possível manter a conexão\
ejs: permite gerar HTML dinâmico usando JavaScript\
express: usado para aplicação web, em específico REST API\
nodemon: monitora o diretório do seu projeto e reinicia automaticamente o aplicativo Node quando detecta qualquer alteração.\

# Estrutura de pastas

O projeto foi organizado seguindo o **padrão MVC** (Model-View-Controller)\
    Benefício: facilita o desenvolvimento, pois cada parte do sistema tem sua função clara (projeto fica mais legível e escalável), e ajuda na manutenção do código


```

projeto-individual/
│
├── 📁 assets/                    # Recursos gráficos e estáticos do projeto
│   ├── 📁 wad-assets/           # Imagens usadas na documentação WAD
│   └── 📄 favicon.ico           # Ícone da aplicação para o navegador
│
├── 📁 config/                    # Configurações do sistema
│   └── 📄 db.js                 # Configuração de conexão com o banco de dados
│
├── 📁 controllers/               # Controladores MVC
│   ├── 📄 userController.js     # Gerencia operações de usuário
│   ├── 📄 earningsController.js # Gerencia operações de ganhos
│   ├── 📄 expensesController.js # Gerencia operações de despesas
│   ├── 📄 goalsController.js    # Gerencia operações de metas
│   └── 📄 to_do_list_itemController.js # Gerencia operações de tarefas
│
├── 📁 documents/                 # Documentação do projeto
│   └── 📄 WAD.md                # Web Application Document detalhado
│
├── 📁 models/                    # Modelos de dados (camada de acesso ao banco)
│   ├── 📄 userModel.js          # Modelo para tabela de usuários
│   ├── 📄 earningsModel.js      # Modelo para tabela de ganhos
│   ├── 📄 expensesModel.js      # Modelo para tabela de despesas
│   ├── 📄 goalsModel.js         # Modelo para tabela de metas
│   └── 📄 to_do_list_itemModel.js # Modelo para tabela de tarefas
│
├── 📁 public/                    # Arquivos acessíveis diretamente pelo navegador
│   ├── 📁 css/                  # Folhas de estilo CSS
│   │   └── 📄 style.css         # Estilos principais da aplicação
│   └── 📁 js/                   # Scripts JavaScript do cliente
│
├── 📁 routes/                    # Definição das rotas da aplicação
│   ├── 📄 frontRoutes.js        # Rotas para renderização de páginas
│   ├── 📄 userRoutes.js         # Rotas de API para usuários
│   ├── 📄 earningsRoutes.js     # Rotas de API para ganhos
│   ├── 📄 expensesRoutes.js     # Rotas de API para despesas
│   ├── 📄 goalsRoutes.js        # Rotas de API para metas
│   └── 📄 to_do_list_itemRoutes.js # Rotas de API para tarefas
│
├── 📁 scripts/                   # Scripts de banco de dados e utilitários
│   ├── 📄 init.sql              # Script SQL inicial para criar tabelas
│   └── 📄 runSQLScript.js       # Script para executar comandos SQL
│
├── 📁 services/                  # Camada de serviços (lógica de negócios)
│   ├── 📄 userService.js        # Serviços relacionados a usuários
│   ├── 📄 earningsService.js    # Serviços relacionados a ganhos
│   ├── 📄 expensesService.js    # Serviços relacionados a despesas
│   ├── 📄 goalsService.js       # Serviços relacionados a metas
│   └── 📄 to_do_list_itemService.js # Serviços relacionados a tarefas
│
├── 📁 tests/                     # Testes automatizados
│   ├── 📄 user.test.js          # Testes para operações de usuário
│   └── 📄 earnings.test.js      # Testes para operações de ganhos
│
├── 📁 views/                     # Templates de visualização (EJS)
│   ├── 📁 pages/                # Páginas completas da aplicação
│   │   ├── 📄 dashboard.ejs     # Página inicial (resumo)
│   │   ├── 📄 earnings.ejs      # Página de gerenciamento de ganhos
│   │   ├── 📄 expenses.ejs      # Página de gerenciamento de despesas
│   │   ├── 📄 goals.ejs         # Página de gerenciamento de metas
│   │   ├── 📄 login.ejs         # Página de login
│   │   ├── 📄 profile.ejs       # Página de perfil do usuário
│   │   ├── 📄 register.ejs      # Página de registro de usuário
│   │   └── 📄 to_do_list_items.ejs # Página de gerenciamento de tarefas
│   │
│   └── 📁 partials/             # Componentes reutilizáveis
│       ├── 📄 header.ejs        # Cabeçalho com navegação
│       └── 📄 footer.ejs        # Rodapé da página
│
├── 📄 .env                      # Variáveis de ambiente (não versionado)
├── 📄 .gitattributes            # Configurações de atributos do Git
├── 📄 .gitignore                # Lista de arquivos ignorados pelo Git
├── 📄 app.js                    # Configuração da aplicação Express
├── 📄 jest.config.js            # Configuração do framework de testes Jest
├── 📄 package.json              # Dependências e scripts do projeto
├── 📄 package-lock.json         # Versões exatas das dependências
├── 📄 README.md                 # Documentação principal do projeto
├── 📄 rest.http                 # Arquivo para testar endpoints HTTP via extensão REST Client
└── 📄 server.js                 # Ponto de entrada principal da aplicação

```


❇️ETAPAS

Modelo físico (script SQL) e relacional (imagem -- dbdiagram.io )
Configurar o servidor e criar o arquivo (server.js)

❇️UTILIDADES

instalações
npm init
npm install express
npm jest
npm test

comandos no terminal
npm install: instala todas as dependencias(pacotes) - vê no package.json
npm run init-db: atualiza o supabase
npm run dev: sobe as atualizações no servidor automaticamente a medida que são feitas
npm start: sobe o servidor
npm run migration

comentarios
 js: /**{...}*/
EJS: <!-- -->

conceitos
entidade = tabela
parâmetro = propriedades
migração => criar as tabelas da db direto no projeto, por isso a ideia de migração.
casting => criar objeto a partir da classe do model
query => presentes no model/service. Responsáveis pelas consultas ao banco de dados (consultar nesse contexto significa tudo que mexe no banco de dados)
try e catch =>

<tr> linha
<td> célula

❇️ ENTENDIMENTO DE CÓDIGO

-- {} define um objeto

-- () define uma função: linhas de código que realizam uma ação na aplicação

-- querySelector: element = document.querySelector(selectors);
element é um objeto (tipo uma variável) e o selectors é um seletor CSS (#, .) que acessa um ou mais elementos HTML no código (qualquer tipo de <div>)

-- é no server onde a gente encontra o que colocar depois do "localhost:3000" para cessar uma db específica

--é no controller que a gente descobre se pode fazer o acesso direto na URL(req. params) -utilizando o postgrees como nocaso do delete, get User e getAllUsers - ou pelo backend (req.body) - utilizando o Dbeaver como no caso de update e o postgrees como no caso do create.

--é no route que descobrimos se precisamos colocar algo depois do / e o que seria isso


❇️ CARACTERÍSTICAS DO CÓDIGO

async - try e catch: boa prática para lidar com erros

❇️ ROADMAP PARA CONFIGURAR API COM DB

💠 init.sql
Aloca o ScriptSQL

💠 MVC - MODELS

É a fundação de tudo pois define as querys para acesso ao banco de dados que ficam alocadas em funções (que podem ser acessadas por outros arquivos devido ao module.exports): 
const result = await db.query('SELECT * FROM [nome da database]')

dentro desse arquivo temos que: ajustar o nome das funções e variáveis para fazer sentido com o tipo de bd que estamos usando; definir o FROM para a database que quemos utilizando o nome que definimos para ela no scriptSQL; definir as propriedades em create e update; e atualizar o module.exports{} do final do arquivo.

💠 MVC - Controller

é a lógica do servidor, define tudo que deve ser feito a partir da fundação que foi definida no service. É aqui que temos o CRUD e identificamos a forma de acesso as infos: body, params, query (?q=banana)

getAllUsers(exibe todas as linhas) - Método GET nas routes
- confere o nome da const
- testa no postman

getUserById (exibe 1 linha) - Método GET nas routes
- confere o nome da const
- testa no postman

CreateUser (cria linha) - Método POST nas routes
- confere o nome da const
- adiciona as propriedades todas menos id
- cria no postman e vê no Dbeaver
- acesso é diretamente no body, ou seja, [...].

UpdateUser (atualiza infos da linha) - Método PUT nas routes
- confere o nome da const
- adiciona as propriedades todas menos id
- acesso é diretamente no body, ou seja, [...].
- Atualiza e vê pelo Dbeaver com a linha de código: 
UPDATE public.usuario SET "nome" = 'yan', "email" = 'febwyuf', "senha" = '4321' where "id"=1

deleteUser (deleta linha) - Método DELETE nas routes
- confere o nome da const
- acesso é através de parâmetros diretamente no body, ou seja, pela barra do navegador onde você acessa através do id.

💠 routes (endpoints)

tem conecção direta com o controler. Aqui precisamos colocar os nomes corretos das funções que escrevemos para aquele BD específico.
(você sempre associa uma rota a um controller específico)

💠 Server

cria um app.use para cada db
nele você vê como pode escrever na barra do navegador para a cessar a bd que você quer.


❇️ COMO CONFIGURAR O ACESSO AOS MÉTODOS PELO FRONT 

CREATE/POST 
---
1. Criar a view da página
2. Configurar rota pra essa página em frontRoutes.ejs
3. criar um forms na View da página com a action acessando a rota daquela base de dados que está definida em server.ejs e definindo o médodo que será utilizado

**para o usuário ser redirecionado após interagir com o botão, usa-se o res.redirect("/[view que vc quer]") no controller dentro da função que configura o create.

GET
---

❇️NAVEGAÇÃO DINÂMICA ENTRE VIEWS

res.redirect("/page") ~ controller.js

❇️ CSS

Seletor CSS
Seleciona pelo id: #
Seleciona pela classe: .

//exemplo 01: pega o main
<main id="principal" class="body">
main#principal.body

//exemplo 02: pega o tbody
<main>
<table id="principal">
<tbody class="body"></tbody
</table>
</main>

css selector
main #principal .body

❇️ DBEAVER
Importante para editar infos no banco de dados através de comandos e ver a tabela em si.

// para alterar a info de uma propriedade da tabela pelo DBeaver
UPDATE public.atividades A SET concluido = 'em andamento' WHERE A.concluido LIKE '0'

// acessa o método update de inputs que já existem na nossa tabela
UPDATE public.usuario SET "nome" = 'yan', "email" = 'febwyuf', "senha" = '4321' where "id"=1

obs.: sem o WHERE, a edição é aplicada a toda a tabela sem que haja a chance de resgate das infos anteriores então é essencial que tenha o Where.

❇️ POSTMAN

Importante para acessar informações do banco de dados e criar novos.

//Sintax

{  
    "título": "ajudar fulano" , -- varchar  
    "descricao": "ela precisa",-- varchar  
    "prazo": "2025-09-12" ,-- date  
    "prioridade": 5, --integer  
    "concluido": false -- boolean  
}

# Referências

**NIELD, Thomas**. Introdução à Linguagem SQL: Abordagem prática para iniciantes. 1. ed. Rio de Janeiro: Novatec Editora, 2016. 144 p. ISBN 978‑85‑7522‑501‑1

**HASHTAG PROGRAMAÇÃO**. O que é o SQL e Por Que Você Deveria Aprender? YouTube, 2022. Disponível em: https://www.youtube.com/watch?v=LaoIlFhULvY. Acesso em: 28 jul. 2025.

**HASHTAG PROGRAMAÇÃO**. Saia do zero em SQL em apenas 5 minutos. YouTube, 2025. Disponível em: https://www.youtube.com/watch?v=KKxwFVk8bsg. Acesso em: 28 jul. 2025.

**POSTGRESQL GLOBAL DEVELOPMENT GROUP**. PostgreSQL Documentation. Disponível em: https://www.postgresql.org/docs/. Acesso em: 28 jul. 2025.

**FIRESHIP. PostgreSQL in 100 Seconds**. YouTube, 2023. Disponível em: https://www.youtube.com/watch?v=n2Fluyr3lbc. Acesso em: 28 jul. 2025.


