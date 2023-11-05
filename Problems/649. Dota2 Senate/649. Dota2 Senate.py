class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Create two queue, for 'R' and 'D' respectively.
        rad = [i for i, ele in enumerate(senate) if ele=='R'];
        dir = [i for i, ele in enumerate(senate) if ele=='D'];
        
        # Simulate until members of one of the parties are all banned.
        # If there is a member of the opposite party to the right of senate,
        # Although the senator can claim victory or banned them,
        # The senate should always banned them.
        while rad and dir:
            n = len(rad)+len(dir);
            if rad[0]<dir[0]:
                dir.pop(0);
                rad.append(rad.pop(0)+n);
            else:
                rad.pop(0);
                dir.append(dir.pop(0)+n);
                
        return "Radiant" if rad else "Dire";