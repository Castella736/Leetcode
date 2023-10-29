class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Track left and right characters.
        l, r = 0, len(s)-1;
        alphanumeric = string.ascii_letters+"1234567890";
        
        # While two pointers not meet yet.
        while l < r:
            # Skip if not alpha-numeric ascii char.
            if not s[l] in alphanumeric:
                l += 1;
                continue; # Re-check if meet.
            if not s[r] in alphanumeric:
                r -= 1;
                continue;
            
            # Return False if two letter not the same in lowercase
            if s[l].lower() != s[r].lower():
                return False;
            # Advance to next.
            l += 1;
            r -= 1;
        
        # Return True if it pass all verifications.
        return True;
    