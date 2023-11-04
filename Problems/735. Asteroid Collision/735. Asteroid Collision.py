class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Create a stack.
        track = [];
        # Check each asteroid
        for newAsteroid in asteroids:
            # Collision check until end.
            while True:
                if track and track[-1]>0 and newAsteroid<0:
                    # The input always satisfies "left > 0 > right".
                    # To check mass of which one is larger, is equivalent to compare "left" and "-right".
                    # quivalently compare "left-(-right)" and "0".
                    merge = track[-1] + newAsteroid;
                    if merge==0:
                        track.pop();
                        break;
                    elif merge>0:
                        break;
                    else:
                        track.pop();
                else:
                    track.append(newAsteroid);
                    break;
                    
        return track;