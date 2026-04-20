# import  re 
# text = "The world is the stage, and all the men and women merely players."

# y= re.split(r'([,.:;?_!"()\']|--|\s)', text) #split the text into tokens based on punctuation and whitespace
# y=[item.strip() for item in y if item.strip()] #remove any empty tokens and strip whitespace from the tokens

# # print(y)
# # print(len(y)) #length of the list of tokens


# def unique_tokens(y):
#     unique = set(y) #convert the list to a set to remove duplicates
#     return list(unique) #convert the set back to a list
# unique_tokens_list = unique_tokens(y)
# print(unique_tokens_list)

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
                                
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
tokenizer = SimpleTokenizerV1(vocab)
text = "The world is the stage, and all the"
ids = tokenizer.encode(text)
print(ids)
