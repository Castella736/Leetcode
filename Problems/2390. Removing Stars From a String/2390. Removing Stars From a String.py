class Solution:
    def removeStars(self, s: str) -> str:
        # Create a empty stack.
        track = [];
        # Annihilate the top if the current is a "*".
        # Due to the description, the leading char. is always not a "*".
        for word in s:
            if word == "*":
                track.pop();
            else:
                track.append(word);
        
        # Cast the list into string.
        return "".join(track);