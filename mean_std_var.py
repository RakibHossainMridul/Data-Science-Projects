import numpy as np

def calculate(x):
  #x has to be a nine numbers, list
    if len(x)!= 9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(x).reshape([3,3])
        #print(a)
        means_row = np.mean(a, axis = 1)
        #print(means_row)
        means_col = np.mean(a , axis = 0)
        #print(means_col)
        means_all = np.mean(a)
    #print(means_all)
    #std deviation
        std_row = np.std(a, axis = 1)
    #print(std_row)
        std_col = np.std(a , axis = 0)
    #print(std_col)
        std_all = np.std(a)
    #print(std_all)
    #variance
        var_row = np.var(a, axis = 1)
    #print(var_row)
        var_col = np.var(a , axis = 0)
    #print(var_col)
        var_all = np.var(a)
    #print(var_all)
    #max
        max_row = np.max(a, axis = 1)
    #print(max_row)
        max_col = np.max(a , axis = 0)
    #print(max_col)
        max_all = np.max(a)
    #print(max_all)
    #min
        min_row = np.min(a, axis = 1)
        #print(min_row)
        min_col = np.min(a , axis = 0)
    #print(min_col)
        min_all = np.min(a)
    #print(min_all)
    #sum
        sum_row = np.sum(a, axis = 1)
    #print(sum_row)
        sum_col = np.sum(a , axis = 0)
    #print(sum_col)
        sum_all = np.sum(a)
    #print(sum_all)


    #returning output
        calculations = {
        'mean' : [means_col.tolist(), means_row.tolist(), means_all.tolist()],
        'variance' : [var_col.tolist(),var_row.tolist(),var_all.tolist()],
        'standard deviation' : [std_col.tolist(),std_row.tolist(),std_all.tolist()],
        'max' : [max_col.tolist(), max_row.tolist(), max_all.tolist()],
        'min' : [min_col.tolist(), min_row.tolist(), min_all.tolist()],
        'sum' : [sum_col.tolist(),sum_row.tolist(),sum_all.tolist()]
        }
     

        return calculations


x= [2,6,2,8,4,0,1,5,7]
output = calculate(x)
print(output)