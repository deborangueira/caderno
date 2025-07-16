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

1. Crie o repositório no GitHub e copie o link do navegador  
2. No terminal, clone o repositório com:

```powershell
git clone https://github.com/deborangueira/[nomeRepositorio].git
```

## 🌿 Criar ou mudar de branch

```powershell
git branch                     # Mostra branches locais (o * indica a atual)
git branch -r                  # Mostra branches remotas

git switch nomeBranch          # Troca para branch existente
git switch -c novaBranch       # Cria e já troca para nova branch
```


## 🚀 Dar push (enviar para o GitHub)

```powershell
git pull origin main           # Traz atualizações antes de começar
git add .                      # Adiciona todas as mudanças
git status                     # Verifica o que será enviado
git commit -m "mensagem"       # Cria o commit com mensagem
git push origin nomeBranch     # Envia para o GitHub
```

