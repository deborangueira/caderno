### Roadmap

1. pega o 1º índice e soma com todos os outros a frente dele até o final da lista.
2. pega o termo e se a soma entre o termo e o próximo der igual ao target: 
    - retorna o índice dos valores
    - para de tentar

### How the roadmap translated into the code


```Javascript

    for (let i=0; i<nums.length;i++){    
        term = nums[i] // pega o termo
        index = i // pega o 1º índice

        for (let i = (index+1); //soma com todos os outros a frente dele
        i <nums.length; //até o final da lista.
        i++){
            if(term + nums[i] == target){ //se a soma entre o termo e o próximo der igual ao target
                return [index,i] //retorna o índice dos valores
                break; //para de tentar
            }
        }
    }

```