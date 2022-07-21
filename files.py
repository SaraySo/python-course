
#########################################
# Question 1 
#########################################
def sum_nums(file):
    f=open(file,'r')
    sum=0
    str=f.read()
    lst=str.split()
    for i in lst:
      sum+=int(i)
    f.close()
    return sum



#########################################
# Question 2 
#########################################
def count_lines(in_file, out_file):
    infile=open(in_file,'r')
    text=infile.read()
    infile.close()
    lines=text.count('\n')
    #write to out_file
    outfile=open(out_file,'x')
    outfile.write(str(lines))
    outfile.close()



#########################################
# Question 3 
#########################################
def simple_sent_analysis(in_file):
    items= {} #try to read from file 
    try:
        infile=open(in_file,'r')
        text=infile.read()
        infile.close()
    except: 
        print("Cannot encode {} due to IO error".format(in_file))
        return(items)
    text=text.lower()
    char_to_throw=['.','%','$',';','-',',','?','!','(',')']
    #replace every instance with " "
    for char_t in char_to_throw:
        text=text.replace(char_t," ")
    #split String
    textlist=text.split()
    #create dictionary
    items['happy'] = textlist.count('happy');
    items['sad'] = textlist.count('sad');
    return(items)


#########################################
# Question 4 
#########################################
def calc_profit_per_group(in_file):
    import csv

    try:
        infile = open(in_file,'r')
        csv_data=csv.reader(infile)
        list_data=list(csv_data)
        infile.close()

  #erorr if cannot read
    except: 
        print("Cannot load {} due to IO error".format(in_file))

    #return empty dict
        return()
  
  #Check data
    for row in list_data:
    #check that there are 3 elements
        if (len(row) != 3): raise ValueError("Invalid input.") from None
    
    #check that column 3 is a legal word
        if (row[2]=='sad' or row[2]=='happy' or row[2]=='neutral'): pass 
        else: raise ValueError('Invalid input.') from None

    #check that element 2 is a float
        try:
          float(row[1])
        except: raise ValueError("Invalid input.") from None
    
  #calculate average profit
    appeared=list() #list for titles who have appeared
    category_counter={"happy":0,"sad":0,"neutral":0} #category counter
    profit={"happy":0, "sad":0, "neutral":0} #dict to hold profit values

    for row in list_data:
    #check that the series hasn't appeared yet
        if row[0] in appeared: # if serise name is in appeared list
      #raise value error
          raise ValueError('The series {} appears more than once.'.format(row[0])) from None
          return ({})
      

    # if it hasn't appeared yet
        else:
          appeared.append(row[0])
    
    #add profit to the correct category in the dictionary
        profit[row[2]] += float(row[1])
    #add 1 to the category counter
        category_counter[row[2]] += 1;
  
    for key in profit:
    #calcualte average
    #if there have been no entries for this category
        if (category_counter[key] == 0):
          profit[key]="NA"
    
    #if there have been entires
        else:
          profit[key] = profit[key]/category_counter[key]

  #close file and return
    return (profit)


#########################################
# Question 5 
#########################################
def decode(in_file, out_file):
    output=""

  #try to load file
    try:
        infile=open(in_file,'rt')
        cipher=infile.read()
        infile.close() 

  #error if cannot read
    except: 
        print("Can’t decipher {} due to an IO Error".format(in_file))

  #Decipher code
    for letter in cipher:
    #find the letter ASCII value
        letter_value=ord(letter)

    #if it is a lowercase 
        if((97 < letter_value <= 122) or (65 < letter_value <= 90)):
          output += (chr(letter_value-1))

        elif(letter_value==97):
          output += 'z'
    
        elif(letter_value==65):
          output += 'Z'

        else:
          output += letter
  
  #write output to File
    try:
        outfile=open(out_file,'x')
        outfile.write(output)
        outfile.close()

    except:
        print("Can’t decipher {} due to an IO Error".format(out_file))

    decode("piton/q5.txt","dict/bb.txt")


#########################
# main code 
# You can add more validation cases below
#########################
if __name__ == "__main__":
	#you can add tests for your code here.
	pass
# ============================== END OF FILE =================================
