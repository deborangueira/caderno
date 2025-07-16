# 🧠 Anotações sobre Git e GitHub via Terminal (PowerShell + VS Code)

- "PS C:" → indica que estou usando o terminal PowerShell (característico do Windows) e estou no disco C.
- "\Users\Inteli\Documents\Inteli": indica em que diretório estou e a rota até ele. 


## 📁 Criar e navegar entre pastas

```
mkdir nome_da_pasta         # Cria uma nova pasta
cd nome_da_pasta            # Entra na pasta
cd ..                       # Volta uma pasta
```

## 🔗 Clonar repositório do GitHub

0. Certifique-se de que você está no diretório onde quer que o repositório seja armazenado
1. Crie o repositório no GitHub e copie o link do navegador  
2. No terminal, clone o repositório com:

```powershell
git clone https://github.com/deborangueira/[nomeRepositorio].git
```

## 🌿 Criar, excluir ou mudar de branch

```powershell

git switch nomeBranch          # Troca para branch existente
git switch -c novaBranch       # Cria e já troca para nova branch
git push -u origin             # sobe a branch nova para o GitHub

git push origin --delete       # exclui a branch no GitHub
git branch -D nomeBranch       # exclui a branch local
```
## 🌳 Ver branches

```powershell
git branch                     # Mostra branches locais (o * indica a atual)
git branch -r                  # Mostra branches remotas
git branch -a                  # Mostra todas as branches
```

## 🚀 Dar push (enviar para o GitHub)

```powershell
git pull origin nomeBranch           # Traz atualizações antes de começar
git add .                      # Adiciona todas as mudanças
git status                     # Verifica o que será enviado
git commit -m "mensagem"       # Cria o commit com mensagem
git push origin nomeBranch     # Envia para o GitHub
```

## 🫱🏼‍🫲🏼 Dar merge



## 🚀 Restaurar arquivos

```powershell
git restore .        # Desfaz todas as mudanças não comitadas
```