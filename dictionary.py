
#########################################
# Question 1 
#########################################
def most_popular_character(my_string):
    d = {}
    max_v = 0
    for i in range(len(my_string)):
        if my_string[i] in d :
            d[my_string[i]] += 1
        else:
            d[my_string[i]] = +1
    for key in d:
        if d[key]>max_v :
          max_v = d[key]
          min_k = key
        elif d[key] == max_v:
            min_k = min(min_k,key)
        else:    
            continue
    return min_k


#########################################
# Question 2 
#########################################
def diff_sparse_matrices(lst):
   new_mat = {}
   i=0
   for mat in lst :
       for place in mat:
          if place in new_mat:
              new_mat[place]= new_mat[place] - mat[place]
          else:
              if i == 0:
                  new_mat[place] = mat[place]
              else:      
                  new_mat[place] = -mat[place]
       i =+ 1 
   new_mat_f = new_mat.copy()   
   for key in new_mat:
        if new_mat[key]==0:
           del new_mat_f[key]
        else:
           continue      
   return new_mat_f       
    

#########################################
# Question 3 
#########################################
def find_substring_locations(s, k):
    dict = {}
    for i in range(len(s) - k + 1):
        A = s[i:i+k]
        if A not in dict:
            dict[A] = [i]
        else:
            dict[A].append(i)
    return dict


#########################################
# Question 4 
#########################################
def courses_per_student(tuples_lst):
    dict_what_courses = {}
    for lst in tuples_lst:
        lower1 = lst[0].lower()
        lower2 = lst[1].lower()
        if lower1 not in dict_what_courses:
            dict_what_courses[lower1] = [lower2]
        else:
            dict_what_courses[lower1].append(lower2)
    return dict_what_courses             
             


def students_per_course(tuples_lst):
    count = 0
    dict_how_many_course = {}
    dict = courses_per_student(tuples_lst)
    for i in dict:
        for course in dict[i]:
            count +=1    
        dict_how_many_course[i] = count
        count = 0
    return dict_how_many_course


if __name__ == '__main__':
    # Q1
    assert most_popular_character('aabbAA') == 'A'

    # Q2
    assert diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1}

    # Q3
    assert find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3],
                                                             'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]}

    # Q4
    assert courses_per_student([('Rina', 'Math'), ('Yossi', 'Chemistry'),
                                ('Riki', 'python'), ('Rina', 'pYthon'), ('Yossi', 'biology')]) == \
           {'rina': ['math', 'python'], 'yossi': ['chemistry', 'biology'], 'riki': ['python']}

    assert students_per_course([('Rina', 'Math'), ('Yossi', 'Chemistry'),
                               ('Riki', 'python'), ('Rina', 'pYthon'), ('Yossi', 'biology')]) == \
           {'rina': 2, 'yossi': 2, 'riki': 1}

# ============================== END OF FILE =================================
