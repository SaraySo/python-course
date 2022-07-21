
#########################################
# Question 1 
#########################################
def sum_divisible_by_k(lst, k):
    sum = 0
    for i in range(len(lst)):
        if lst[i]%k==0:
            sum+= lst[i]
        else:
            continue
    return sum    


#########################################
# Question 2 
#########################################
def mult_odd_digits(n):
    mult = 1
    list_n = list(str(n))
    for i in range(len(str(n))):
        if int(list_n[i])%2!=0:
            mult*=int(list_n[i])
        else:
         continue
    return mult


#########################################
# Question 3 
#########################################
def count_longest_repetition(s, c):
    count=0
    max_count=0
    for elem in s:
       if elem==c:
           count+=1
       elif count>=max_count:
           max_count = count
           count=0
           continue
       else:
           count = 0
           continue   
    return max(max_count, count)


#########################################
# Question 4 
#########################################
def upper_strings(lst):
    my_list = [5,6]
    my_string = 'hello'
    if type(lst)==type(my_list):
       for i in range(len(lst)):
           if type(lst[i])==type(my_string):
               lst[i]=lst[i].upper()
           else:
               continue
    else:
        return int('-1')


#########################################
# Question 5 
#########################################
def div_mat_by_scalar(mat, alpha):
   new_mat = []
   num_rows = len(mat)
   num_columns = len(mat[0])
   for i in range(num_rows):
       new_mat.append([])
       for j in range(num_columns):
           new_mat[i].append(mat[i][j]//alpha)
   return new_mat 


#########################################
# Question 6 
#########################################
def mat_transpose(mat):
   mat_T = []
   num_rows_T = len(mat[0])
   num_columns_T = len(mat)
   for i in range(num_rows_T):
       mat_T.append([])
       for j in range(num_columns_T):
           mat_T[i].append(mat[j][i])
   return mat_T

      
#########################
# main code 
# Tests have been added for your convenience.
# You can add more tests below.
#########################

print(sum_divisible_by_k([3, 6, 4, 10, 9], 3) == 18)
print(sum_divisible_by_k([45.5, 60, 73, 48], 4) == 108)


print(mult_odd_digits(5638) == 15)
print(mult_odd_digits(2048) == 1)
print(mult_odd_digits(54984127) == 315)


print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
print(count_longest_repetition ('cccccc','c') == 6)
print(count_longest_repetition ('abcde', 'z') == 0)


vals = [11, 'TeSt', 3.14, 'cAsE']
upper_strings(vals)
print(vals == [11, 'TEST', 3.14, 'CASE'])

vals = [-5, None, True, [1, 'dont change me', 3]]
upper_strings(vals)
print(vals == [-5, None, True, [1, 'dont change me', 3]])

print(upper_strings(42) == -1)
print(upper_strings('im not a list') == -1)
print(upper_strings(False) == -1)


mat1 = [[2, 4], [6, 8]]
mat2 = div_mat_by_scalar(mat1, 2)
print(mat1 == [[2, 4], [6, 8]])
print(mat2 == [[1, 2], [3, 4]])

print(div_mat_by_scalar([[10,15], [-3,6]], -5) == [[-2, -3], [0, -2]])


mat = [[1,2],[3,4],[5,6]]
mat_T = mat_transpose(mat)
print(mat == [[1, 2], [3, 4], [5, 6]])
print(mat_T == [[1, 3, 5], [2, 4, 6]])

mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
mat2_T = mat_transpose(mat2)
print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])


# ============================== END OF FILE =================================
