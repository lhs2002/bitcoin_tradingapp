# #functions

## Questions

1. Hash function suggests that if string starts with uppercase letters, to offset by constant ascii equivalent of 'A'. Else, to offset by 'a'. Since S is entirely alphabetical, there would only be
52 different hash codes possible. For a decent size data, there is a relatively high likelihood of collision. As cluster grows with linear probing, search, insert would be slow.

2. Theoretically, the hash function is perfect because
    1) the entire data is utilized, decreasing the likelihood of collisions
    2) it is deterministic since the conversion to decimal from binary equivalent of string is standard. It does not involve random variables.
However in reality, since strings are char*, having C converting "AB" to decimal is converting the addresses. Hence, the hash would become independent of data of
string, and depends on randomly assigned addresses in memory when string is saved. Iterating over the characters and converting would also not result in
the same outcome as in theory.


3. Hashing the 50 file produces 50 pieces of unique hash codes which can be stored in hash table with less memory. In terms of search, it is also faster as its a O(1) constant look up time compared
to case where each students' file has to be compared iteratively over the 50 original files. Hashing also eliminates the need to open 50 original files for comparison, reducing the codes required.

4. Since the data in trie is a roadmap to the data itself within the trie, there are no collisions and each word would have an unique path to traverse through. Words can be found based on
the letters in them and is independent of other words stored in the trie. Its hence, a O(1). Hash tables on the other hand, may have collisions due to hash function used. In linear probing and severe clustering(which is probable for
large number of words in existence), the word in question may be stored far away from its hash value such that big O regresses to O(n).

## Debrief

1. Lectures, google

2. 20min
