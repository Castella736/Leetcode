class Solution:
    # Decode the input segment.
    # A segment is of the form "num_part[char_part]".
    # Return "char_part" * num_part.
    def triggerDecode(self, code: list[str]) -> list[str]:
        num_part = 0;
        char_part = [];
        p = 0;
        res = [];
        
        # Calculate num_part.
        while code[p] != "[":
            num_part = 10*num_part + int(code[p]);
            p += 1;
        p += 1; # Skip "[".
        
        # Find char_part.
        while code[p] != "]":
            char_part.append(code[p]);
            p += 1;
        
        # Build "char_part" * num_part.
        for i in range(num_part):
            res += char_part;
        
        return res;
        
    def decodeString(self, s: str) -> str:
        stack = [];
        
        # Read the string.
        for char in s:
            stack.append(char);
            
            # Trigger decode of a segment.
            if char == "]":
                # Prepare the segment, find the numeric part.
                p = len(stack)-2;
                while stack[p] != "[":
                    p -= 1;
                p -= 1;
                while p>=0 and stack[p].isdigit():
                    p -= 1;
                
                # Decode the segment and replace the encrypted with the decoded.
                temp = self.triggerDecode(stack[p+1:]);
                del stack[p+1:];
                stack += temp;               
                
        return "".join(stack);