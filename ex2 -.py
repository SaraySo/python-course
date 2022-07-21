''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a 
#########################################
def four_bonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    else:
        fb = four_bonacci_rec(n-1) + four_bonacci_rec(n-2) + four_bonacci_rec(n-3) + four_bonacci_rec(n-4)
    return fb 
    


#########################################
# Question 1.b 
#########################################
def four_bonacci_mem(n, memo=None):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if memo == None:
        memo = {}
    memo_key = n
    if memo_key not in memo:
        memo[memo_key] = four_bonacci_mem(n-1, memo)+four_bonacci_mem(n-2, memo)+four_bonacci_mem(n-3, memo)+four_bonacci_mem(n-4, memo)
    return memo[memo_key] 


#########################################
# Question 2 
#########################################
def climb_combinations_memo(n, memo=None):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    if memo == None:
        memo = {}     
    if n not in memo:
        memo[n] = climb_combinations_memo(n-1, memo)+climb_combinations_memo(n-2, memo)
    return memo[n]
    


#########################################
# Question 3 
#########################################
def catalan_rec(n,memo=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if memo == None:
        memo = {}
    if n not in memo:
        sum = 0
        for i in range(0,n):
            sum += catalan_rec(i,memo)*catalan_rec(n-1-i,memo)
        memo[n] = sum
    return memo[n]   
    

#########################################
# Question 4.a 
#########################################
def find_num_changes_rec(n, lst):
    if n==0:
        return 1
    if n<0:
        return 0
    if lst == []:
        return 0 
    else:
        shortlist=lst.copy()
        shortlist.remove(max(shortlist))
        return find_num_changes_rec(n,shortlist)+find_num_changes_rec(n- max(lst),lst)
    

#########################################
# Question 4.b 
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n==0:
        return 1
    if n<0:
        return 0
    if lst == []:
        return 0 
    if memo == None:
        memo = {}    
    memo_key = (n,repr(lst))    
    if memo_key not in memo:
        shortlist=lst.copy()
        shortlist.remove(max(shortlist))
        memo[memo_key]=find_num_changes_mem(n,shortlist, memo)+find_num_changes_mem(n- max(lst),lst,memo)
    return memo[memo_key]    
  


#########################
# main code 
# You can add more validation cases below
#########################
if __name__ == "__main__":
    #Question 1.a tests - you can and should add more    
    """
    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)
    """
    #Question 1.b tests - you can and should add more
    """
    print(four_bonacci_mem(0) == 0)
    print(four_bonacci_mem(5) == 12)
    print(four_bonacci_mem(8) == 85)
    """
    #Question 2 tests - you can and should add more
    """
    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    """
    #Question 3 tests - you can and should add more
    """
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    """
    #Question 4.a tests - you can and should add more
    """
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0.9,[1,2,5,6]) == 0)
    """
    #Question 4.b tests - you can and should add more
    """
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(0.9,[1,2,5,6]) == 0)
    """
    pass
# ============================== END OF FILE =================================
