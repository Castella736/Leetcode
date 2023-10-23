class Solution:
    def isValid(self, s: str) -> bool:
        table = {"(","[","{"};
        seen = [];

        for symbol in s:
            if symbol in table:
                seen.append(symbol);
            else:
                if seen:
                    match seen.pop():
                        case "(":
                            check = ")";
                        case "[":
                            check = "]";
                        case "{":
                            check = "}";
                    if symbol!=check:
                        return False;
                else:
                    return False;
        
        return not bool(seen);