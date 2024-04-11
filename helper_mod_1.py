'''
this module is a support module for main modules. It will contain some pre-defined
tasks like pattern making and other stuff which will support main file !

|| LOG-1 09-04-2024 TUE 16:46 FILE CREATED !
|| LOG-2 10-04-2024 WED 12:03 ADDED max_lden()
|| LOG-3 10-04-2024 WED 13:17 ADDED horz_pat()

'''

# making pattern from obtained data 

'''
as i already know the format, i have have to read it and print the obtained data
so that printing will be easier in an ordered format.

for reference, the format is :
->
-> [<name : str>,<nickname : list>,{<default_number> : <list of numbers>,<division>
-> : <list of number> if any},{dictionary of email with division},{address with div
-> -ision},<work_info>,[<list of websites associated>],[list of groups]]
->

columns are : name, nickname, phone, email, address, work_info, websites, group !

'''

# and demo data to test

li=["Rakesh Singh",["nennu bhaiya","mantudjbjbbcbbjbdj"],{"default":[9653829521,3524719482]},{"default":["duckie.od@xyz.com"]},{"default":[],"home":["beside alam bagh mosque, jabalpur"]},"advocate",["rbhaatfirm.com"],["friend"]]

# listing all column names for reference

# [" name ", " nickname ", " phone ", " email ", " address ", " work_info ", " websites ", " group "]

# function max_lden() to get maximum length required for all column

def max_lden(li:list):
    len_lis=[]
    for elem in li:

        # finding maximum length of key form dictionary type data !

        if type(elem)==dict:
            
            # checking if elem is phone number
            
            if li.index(elem)==2:

                # a temporary list to store length

                temp_len=[]

                # appending len of each key in temp_len list

                for div_nme in elem.keys():
                    temp_len.append(len(div_nme))

                # appending to main list

                if max(temp_len)+2 > 12:
                    len_lis.append(max(temp_len)+2)
                else:
                    len_lis.append(12)

                del temp_len
            
            # checking if elem is list of emails as it should not exceed 40 characters
                    
            elif li.index(elem) == 3:

                # a temporary list to store length

                temp_len=[]

                # appending len of each element of each key in temp_len list

                for div_nme in elem.keys():
                    for temp_elem in elem[div_nme]:
                        temp_len.append(len(temp_elem))

                # appending len to main list (len_lis)

                if max(temp_len)+2 < 42 or max(temp_len)+2 > 7:
                    len_lis.append(max(temp_len)+2)
                elif max(temp_len)+2 < 7:
                    len_lis.append(7)
                else:
                    len_lis.append(42)

                del temp_len

                            
            # checking if elem is list of addresses as its should not exceed 40 chars

            elif li.index(elem) == 4:
                
                # a temporary list to store length

                temp_len=[]

                # appending len of each element of each key in temp_len list

                for div_nme in elem.keys():
                    for temp_elem in elem[div_nme]:
                        temp_len.append(len(temp_elem))

                # appending len to main list (len_lis)

                if max(temp_len)+2 < 42 or max(temp_len)+2 > 9:
                    len_lis.append(max(temp_len)+2)
                elif max(temp_len)+2 < 9:
                    len_lis.append(9)
                else:
                    len_lis.append(42)

                del temp_len,temp_elem,div_nme


            else:
                pass


        # finding maximum length of element form list type data !
        
        elif type(elem)==list:
            
            temp_len=[]

            for li_elem in elem:
                temp_len.append(len(li_elem))

            len_lis.append(max(temp_len)+2)

            del temp_len,li_elem

        # finding maximum length of string
        
        elif type(elem)==str:

            len_lis.append(len(elem)+2)

        else:
            pass

    return len_lis
    

# print(max_lden(li))

# max_lden() completed

# creating a function to print the horizontal division

def horz_pat(li:list):
    for i in max_lden(li):
        print("+"+"-"*i,end="")
    print("+")

# horz_pat() completed