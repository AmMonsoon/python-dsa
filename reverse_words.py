def reverse_words(text):
    reversedText = text.split(" ")
    reverseList = []
    for word in reversedText:
        reversedWord = word[::-1]
        reverseList.append(reversedWord)
    
    print(" ".join(reverseList))
    

print(reverse_words('The quick brown fox jumps over the lazy dog.')) # 'ehT kciuq nworb xof spmuj revo eht yzal .god', "Input: 'The quick brown fox jumps over the lazy dog.'")
print(reverse_words('apple')) # 'elppa', "Input: 'apple'"
print(reverse_words('a b c d')) # 'a b c d', "Input: 'a b c d'"
print(reverse_words('  double  spaced  words  ')) #'  elbuod  decaps  sdrow  ', "Input: '  double  spaced  words  '"