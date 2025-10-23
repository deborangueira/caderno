nums = [1,4,5]
k = 1
numOperations = 2

def compare(list):

    frequencia_maxima = 0 # que um número tem numa lista

    # Etapa 1: comparar os elementos após a operação

    if numOperations > 0: 
        for i, n in enumerate(list):

            for t in range(-k,k+1):

                print(f'Comparamos o resultado de {list[i]} +{t} com:')

                for n in list: 
                    if n != list[i]:
                        y = list[i] + t

                        print(f'{n} // {y}')

                        if y == n:
                            frequencia_maxima +=1
                            print(f'o {n} se repete nessa lista!')

    # Etapa 2: conferir se tem repetições na lista original
    for i,n in enumerate(nums):
            if nums.count(n) > 1:
                frequencia_maxima += 1

    # Etapa 3: se não há repetições e na lista existem números, a frequência máxima é de 1
    if frequencia_maxima == 0 and len(nums) >0:
        frequencia_maxima += 1

    print (f'frequencia maxima: {frequencia_maxima}')
                    

compare(nums)

        

    
    