import java.util.HashMap;
import java.util.List;

class Solution {
    public String destCity(List<List<String>> paths) {
        HashMap<String, String> route = new HashMap<>();
        for (List<String> path: paths)
            route.put(path.get(0), path.get(1));
        
        String cur = paths.get(0).get(0);
        while (route.containsKey(cur))
            cur = route.get(cur);

        return cur;
    }
}