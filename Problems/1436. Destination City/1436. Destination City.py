class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = set();
        for start, _ in paths:
            departure.add(start);
            
        for _, dest in paths:
            if dest not in departure: return dest;