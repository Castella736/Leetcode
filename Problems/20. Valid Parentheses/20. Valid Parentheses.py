class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            "(":")",
            "[":"]",
            "{":"}"};
        seen = [];

        for symbol in s:
            if symbol in table:
                seen.append(symbol);
            else:
                if not seen: return False;
                if symbol!=table[seen.pop()]: return False;
        
        return not bool(seen);