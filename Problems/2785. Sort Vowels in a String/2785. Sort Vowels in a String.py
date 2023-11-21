class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s);
        vowels = [];
        position = [];
        
        # Record vowels and their position in s.
        for i, char in enumerate(s):
            if char in {'a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'}:
                vowels.append(char);
                position.append(i);
        
        # Sort vowels in s.
        vowels.sort();
        
        # Replace vowels.
        for p, i in enumerate(position):
            s[i] = vowels[p];
            
        return "".join(s);