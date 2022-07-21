
#########################################
# Question 1 
#########################################

a = 8  # Replace the assignment with a positive integer to test your code.
A = [2, 4, 6, 8, 10]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 1 below here.
B = list(range(len(A)))
for i in B:
      if A[i]%a ==0:
          print(B[i])
          break
      else:
          continue
if A[i]%a !=0:
    print('-1')
# End of code for question 1

#########################################
# Question 2 
#########################################

B = ['I', 'am', 'so', 'happy', 'its','working']
# Replace the assignment with other lists of strings (str) to test your code.

sum = 0
num_of_srings1=0
num_of_srings2=0
count=0
# Write the code for question 2 using a for loop below here.
for elem in B :
    sum += len(elem)
    average = int(sum/len(B))
for elem in B:
    if len(elem)>average:
     num_of_srings1+=1
    else:
        continue
print('The number of strings longer than the average is:',num_of_srings1)
# Write the code for question 2 using a while loop below here.
while len(B)>0 and count<len(B):
    if len(B[count])>average:
      num_of_srings2+=1
    count+=1
print('The number of strings longer than the average is:',num_of_srings2)
# End of code for question 2

#########################################
# Question 3 
#########################################

C = [20, 1, 3, 7, 1,100]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
len_C = len(C)
sum = 0
for i in range(len_C-1):
    multi= C[i]*C[i+1]
    sum+=multi
if len(C)==0:
    print ('0')
elif len(C)==1:
        print(C[0])
else:
    print(sum)
# End of code for question 3


#########################################
# Question 4 
#########################################

D = [1,5,4,8,5,100]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
new_D=D.copy()
len_D=len(D)
for i in range(len_D-2):
    diff_before=abs(D[i]-D[i+1])
    diff_after=abs(D[i+1]-D[i+2])
    if diff_after>diff_before:
        continue
    else:
        new_D.remove(D[i+2])
print(new_D)
# End of code for question 4

#########################################
# Question 5 
#########################################

my_string = 'omgggsocool'  # Replace the assignment with other strings to test your code.
k = 5  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
len_str=len(my_string)
for i in range(len_str-1):
    if my_string[i:k+i]==my_string[i]*k:
       print('For length',str(k)+',','found the substring',str(my_string[i:k+i])+'!')
       break
    else:
        continue
if i==len_str-2:    
      print('Didnt find a substring of length',k)
# End of code for question 5
