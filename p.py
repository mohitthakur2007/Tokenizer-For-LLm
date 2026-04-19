import  re 
text = "The world is the stage, and all the men and women merely players."

y= re.split(r'([,.:;?_!"()\']|--|\s)', text) #split the text into tokens based on punctuation and whitespace
y=[item.strip() for item in y if item.strip()] #remove any empty tokens and strip whitespace from the tokens

# print(y)
# print(len(y)) #length of the list of tokens


def unique_tokens(y):
    unique = set(y) #convert the list to a set to remove duplicates
    return list(unique) #convert the set back to a list
unique_tokens_list = unique_tokens(y)
print(unique_tokens_list)