class Solution:
    def simplifyPath(self, path: str) -> str:
        """Input a path, return canonical form.

        Args:
            path (str): Path consist of regular dir., filename, '.' and '..'.
                        Each subdir is separated by one or multiple '/'

        Returns:
            str: Canonical path. No '.' or '..' as subdir. and subdir. are
                 separated by single '/'
        """
        # Then process subdir. with a stack.
        stack = [];
        
        # Split subdir. as str.
        # Start read the path in subdir.
        for dir in path.split('/'):
            match dir:
                case "." | '': # Ignore unused.
                    continue;
                case "..": # level up.
                    if stack:
                        stack.pop();
                case _: # regular name.
                    stack.append(dir);

        
        # Transform the stack to the path (as str.)..
        return "/"+"/".join(dir for dir in stack);