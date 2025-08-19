import numpy as np

def calculate(list): # function called calculate that will return a dictionary. The matrix is organized in a list with 9 numbers.

    if len(list) !=9: # The input of the function should be a list containing 9 digits
        ValueError:
        print("List must contain nine numbers.")
    else:
        ls = np.array(list) #The function should convert the list into a 3 x 3 Numpy array
        
        mean_rows = [ls[0,1,2].mean(), ls[3,4,5].mean(), ls[6,7,8].mean()]
        mean_columns = [ls[0,3,6].mean(), ls[1,4,7].mean(), ls[2,5,8].mean()]
        
        mean_rows = [ls[0,1,2].mean(), ls[3,4,5].mean(), ls[6,7,8].mean()]
        mean_columns = [ls[0,3,6].mean(), ls[1,4,7].mean(), ls[2,5,8].mean()]
        
        
        
        
        
        return {
            'mean': [mean_rows, mean_columns, ls.mean],
            'variance': [axis1, axis2, flattened],
            'standard deviation': [axis1, axis2, flattened],
            'max': [axis1, axis2, flattened],
            'min': [axis1, axis2, flattened],
            'sum': [axis1, axis2, flattened]
        }
     