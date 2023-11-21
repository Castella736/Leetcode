class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        farthest = {};
        res = 0;
        
        finder = len(garbage)-1;
        # Find latest position each char appears.
        while finder >= 0:
            for char in "GPM":
                if char in garbage[finder] and char not in farthest:
                    farthest[char] = finder;
            
            if (
                'G' in farthest
                and 'P' in farthest
                and 'M' in farthest
            ):
                break;
            finder -= 1;
            
        for char in 'GPM':
            if char not in farthest:
                farthest[char] = 0;
        
        # Sum traveling times of 'G','P','M' required and add it to res.
        stage = [
            farthest[key] for key in farthest
        ];
        stage.sort();
        
        res += (
            sum(travel[stage[1]:stage[2]])
            + 2*sum(travel[stage[0]:stage[1]])
            + 3*sum(travel[:stage[0]])
        );
        
        # Add total length of garbage to res.
        for house in garbage[:stage[2]+1]:
            res += len(house);
        
        return res;