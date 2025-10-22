nums = [1,4,5]
k = 1
numOperations = 2

def compare(list):

    frequencia_maxima = 0 # que um número tem numa lista

    # Etapa 1: fazer a primeira checagem para identificar repetições na lista 

    for i,n in enumerate(nums):
        print(f'{nums[i]}')

    # Etapa 2: comparar os elementos após a operação

    for i, n in enumerate(list):

        for t in range(-k,k+1):

            print(f'Comparamos o resultado de {list[i]} +{t} com:')

            for n in list: 
                if n != list[i]:
                    y = list[i] + t

                    print(f'{n}')

                    if y == n:
                        frequencia_maxima +=1
                        print(f'o {n} se repete nessa lista!')

    print (f'frequencia maxima: {frequencia_maxima}')
                    

compare(nums)

        

    
    