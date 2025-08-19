import numpy as np  # use Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns

def calculate(list): # function called calculate that will return a dictionary. The matrix is organized in a list with 9 numbers.

    if(len(list) !=9): # The input of the function should be a list containing 9 digits
        raise ValueError("List must contain nine numbers.")
    
    ls = np.array(list) #The function should convert the list into a 3 x 3 Numpy array

    mean_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()] #linhas
    mean_columns = [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()] #colunas
    
    var_rows = [ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()] #linhas
    var_columns = [ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var()] #colunas

    std_rows = [ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std()] #linhas
    std_columns = [ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std()] #colunas

    max_rows = [ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()] #linhas
    max_columns = [ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max()] #colunas

    min_rows = [ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()] #linhas
    min_columns = [ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min()] #colunas

    sum_rows = [ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum()] #linhas
    sum_columns = [ls[[0,3,6]].sum(), ls[[1,4,7]].sum(), ls[[2,5,8]].sum()] #colunas

    return { # and then return a dictionary
        'mean': [mean_columns, mean_rows, ls.mean()],
        'variance': [var_columns, var_rows, ls.var()],
        'standard deviation': [std_columns, std_rows, ls.std()],
        'max': [max_columns, max_rows, ls.max()],
        'min': [min_columns, min_rows, ls.min()],
        'sum': [sum_columns, sum_rows, ls.sum()]
    }
     
