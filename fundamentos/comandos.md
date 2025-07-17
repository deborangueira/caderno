# Git, GitHub e comandos via Terminal (PowerShell + VS Code)

> Nesse documento reuni os comandos que mais utilizo para o fluxo de trabalho com Git utilizando terminal do VS Code. Ele foi pensado para ser um documento de consulta, a fim de que não seja mais necessário utilizar o GitHub Desktop.

## 📁 Navegar entre pastas

```powershell
cd nomePasta            # Entra na pasta
cd ..                   # Volta uma pasta
```

## 🔗 Clonar repositório do GitHub

0. Certifique-se de que, no Vscode, você está no diretório onde quer que o repositório seja armazenado
1. Crie o repositório no GitHub e copie o link do navegador  
2. No terminal, clone o repositório com:

```powershell
git clone https://github.com/deborangueira/[nomeRepositorio].git
```

## 🚀 Fazer commit e push (enviar para o GitHub)

```powershell
git branch                                 # Se certifique que está na branch certa.
git pull origin nomeBranch                 # Atualiza a branch
git add .                                  # Guarda todas as mudanças
git status                                 # Verifica alterações
git commit -m "comentário descritivo"      # O commit em si
git push origin nomeBranch                 # Atualiza no GitHub
```

## 🕰️ Abrir histórico de commits

```powershell
git log
```

## ⚠️ Desfazer alterações

```powershell
0. git status        # verifica alterações
1. git restore .     # Desfaz TODAS as mudanças 
```

Obs.: Se as alterações não tiverem sido commitadas, não dá pra reverter a ação! Por isso usar o git status é importante: ao ver as mudanças, você pode conferir se há algo novo que é importante para o código ou não.

## 🌿 Criar, excluir ou mudar de branch

```powershell
git switch nomeBranch          # Troca branch 

git switch -c novaBranch       # Cria e já troca para nova branch
git push -u origin             # sobe a branch nova para o GitHub

git push origin --delete       # exclui a branch no GitHub
git branch -D nomeBranch       # exclui a branch no seu computador
```
## 🌳 Ver branches

```powershell
git branch                     # Mostra branches locais (o * indica a atual)
git branch -r                  # Mostra branches remotas
git branch -a                  # Mostra todas as branches
```

## 🫱🏼‍🫲🏼 Fazer merge

```powershell
git switch branchDestino          # vai para a branch que recebrá as mudanças
git pull origin branchDestino     # atualiza-a
git merge branchAMergir           # Indica a branch que será incorporada e realiza-se o merge em si
git push origin branchDestino     # atualiza no GitHub
```

# Infos extras

### Powershell

- É um **terminal** (interface onde digito comandos para interagir com o sistema operacional) e um **shell** (programa que interpreta e executa os comandos).
- Padrão e mais moderno do Windows

### Como interpretar a linha de comando do terminal

**🔹 `PS C:`**

- O `PS` indica que o terminal em uso é o **PowerShell** (padrão no Windows).
- O `C:` mostra que você está no **disco local C** (unidade do computador onde ficam instalados o sistema e os arquivos do usuário)  

> Curiosidade: Discos locais são partições físicas ou lógicas do computador que armazenam arquivos, programas e o sistema operacional. Cada disco (ou partição) é identificado por uma letra.

**🔹 `\Users\Inteli\Documents\Inteli`**

- Mostra o **caminho completo (diretório atual)**, e serve para indicar **onde estou** dentro da estrutura de arquivos do sistema.

---

> _Atualizado em: 16/07/2025_