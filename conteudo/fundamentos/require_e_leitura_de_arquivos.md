# Entendendo require e Leitura de Arquivos no Node.js

No contexto do beecrowd, a primeira linha de javaScript contém informações importantes de serem entendidas, por isso guardei aqui a compreenção do uso da função `require`, o acesso a `métodos` e como funciona a `leitura de arquivos` no Node.js.


##  require('fs').readFileSync('./dev/stdin', 'utf8')

### 📘 Como ler

"Importe o módulo fs e acesse o método readFileSync (leitura de arquivos de forma síncrona) para ler o conteúdo do arquivo localizado em "./dev/stdin" com codificação 'utf8'."

### 🧩 Significado de cada parte

| Parte                          | Significado                                                                 |
|-------------------------------|------------------------------------------------------------------------------|
| `require()`                    | Função usada para importar módulos no Node.js                               |
| `'fs'`                         | Módulo nativo para manipulação de arquivos                                  |
| `.readFileSync`               | Método síncrono para leitura de arquivos                                    |
| `'./dev/stdin'`                | Caminho para acessar os dados de entrada          |
| `'utf8'`                       | Tipo de codificação dos dados lidos como texto                     |

