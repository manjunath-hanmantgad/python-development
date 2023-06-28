def compress(chars):
    #initialize a variable write to keep track of the position where the compressed characters will be stored in the array.
    write = 0
    #initialize a variable count to count the consecutive occurrences of each character.
    count = 0
    #iterate through the chars array using a for loop, starting from index 1.
    for i in range(1, len(chars) + 1):
        #check if the current character (chars[i]) is the same as the previous character (chars[i-1]). If it is, we increment the count variable.
        if i < len(chars) and chars[i] == chars[i-1]:
            count += 1
            #If the current character is different from the previous character or we have reached the end of the array, it means we have completed counting a group of consecutive occurrences.
            # store the previous character (chars[i-1]) at the position write in the array, as it represents a compressed character.
            
        else:
            chars[write] = chars[i-1]
            write += 1
            
            #If the count is greater than 1, it means the character occurred consecutively multiple times.
            if count > 1:
                # convert the count to a string (count_str) 
                # and store its individual digits in the array 
                # starting from the current write position.
                count_str = str(count)
                chars[write:write+len(count_str)] = list(count_str)
                #update the write pointer to the position after the inserted count digits.
                write += len(count_str)
            count = 1
    return write

chars = ["a", "a", "b", "b", "c", "c", "c"]
output_length = compress(chars)
print(output_length)
                
                            