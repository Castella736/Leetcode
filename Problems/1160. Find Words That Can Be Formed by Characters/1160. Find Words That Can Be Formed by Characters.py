from collections import defaultdict;
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Record all available characters.
        table = defaultdict(int);
        for char in chars:
            table[char] += 1;
        
        res = 0; # variable to record the resutl.
        # Verify if the word can be formed.
        for word in words:
            for char in word:
                if word.count(char) > table[char]:
                    break;
            else:
                res += len(word);
        
        return res;