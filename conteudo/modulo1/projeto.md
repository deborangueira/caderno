❇️DESCRIÇÃO

- Construção de um **sistema Web**

- Projeto organizado seguindo o **padrão MVC** (Model-View-Controller)
    Benefício: facilita o desenvolvimento, pois cada parte do sistema tem sua função clara (projeto fica mais legível e escalável), e ajuda na manutenção do código

- Servidor configurado com Node.js e Express.js
    instalar as dependências:
    1. npm init: adiciona o arquivo package.json que guarda as dependências
    2. npm install express: cria a pasta node_modules e o arquivo package-lock.json

Interface desenvolvida com EJS

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

❇️ TECNOLOGIAS

supabase: núvem que hospeda o bd e permite que ele seja acessado pela internet
Postgrees: sistema gerenciador de db
npm: gerenciador de pacotes
node.js
Json: 
--
Arquitetura MVC: 
model, view, controller
---
Bibliotecas
dotenv: salva as informações do banco de dados para que seja possível manter a conexão
ejs: permite gerar HTML dinâmico usando JavaScript
express: usado para aplicação web, em específico REST API
nodemon: monitora o diretório do seu projeto e reinicia automaticamente o aplicativo Node quando detecta qualquer alteração.

❇️ CARACTERÍSTICAS DO CÓDIGO

assic - try e catch: boa prática para lidar com erros

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