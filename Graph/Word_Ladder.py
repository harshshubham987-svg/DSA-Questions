'''127. Word Ladder
Hard
Topics
premium lock icon
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''

# solution
from collections import deque

def main():
    beginword = "hit"
    endword = "cog"
    wordlist = ["hot","dot","dog","lot","log","cog"]

    wordset = set()

    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q', 'r','s','t','u','v','w','x','y','z']

    for word in wordlist:
        wordset.add(word)

    q = deque()

    q.append(beginword)
    

    count = 1
    if endword not in wordset:
        return 0
    

    while q:
        size = len(q)
        
        
        for _ in range(size):
            word = q.popleft()

            for i in range(len(word)):
                f = word[:i]
                en = word[i+1:]

                for c in alpha:
                    
                    if c == word[i]:
                        continue

                    neb = f+c+en

                    if neb in wordset:
                        q.append(neb)
                        wordset.remove(neb) 
                        if neb == endword:
                            return count + 1
        count += 1       

    return count


if __name__ == "__main__":
    print(main())


