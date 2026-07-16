# Reverse Words

## Pattern
String Manipulation

## Optimized Solution
Split the string into individual words using `split(" ")`. Iterate through each word, 
reverse it using Python slicing (`[::-1]`), store the reversed words in a new list, and join
them back together with `" ".join()`.

## Time Complexity
O(n)

Where `n` is the total number of characters in the string. 
Every character is processed once while splitting, reversing, and joining.

## Space Complexity
O(n)

A new list is created to store the reversed words before joining them into the final string.

def reverse_words(text):
    reversedText = text.split(" ")
    reverseList = []
    for word in reversedText:
        reversedWord = word[::-1]
        reverseList.append(reversedWord)
    
  return (" ".join(reverseList))
    

print(reverse_words('The quick brown fox jumps over the lazy dog.')) # 'ehT kciuq nworb xof spmuj revo eht yzal .god', "Input: 'The quick brown fox jumps over the lazy dog.'")
print(reverse_words('apple')) # 'elppa', "Input: 'apple'"
print(reverse_words('a b c d')) # 'a b c d', "Input: 'a b c d'"
print(reverse_words('  double  spaced  words  ')) #'  elbuod  decaps  sdrow  ', "Input: '  double  spaced  words  '"