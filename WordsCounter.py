
# coding: utf-8

# In[1]:

from collections import Counter
import argparse


def WordCounter(sentence):
    listofwords = sentence.split()
    col_count = Counter(listofwords)
    for keys in col_count:
        print("Key: " + keys + " Count: " + str(col_count[keys]))
        
        
def main():
    parser = argparse.ArgumentParser(description='Taking input sentence')
    parser.add_argument("--input_sentence", type=str, help='The sentence to count words')
    args = parser.parse_args()
    WordCounter(args.input_sentence)

if __name__ == "__main__":
    main()


# In[ ]:




# In[ ]:



