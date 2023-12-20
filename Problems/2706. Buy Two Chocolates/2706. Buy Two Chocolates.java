class Solution {
    public int buyChoco(int[] prices, int money) {
        int[] smallest = {Integer.MAX_VALUE, Integer.MAX_VALUE};
        for (int price : prices) {
            smallest[1] = Math.min(price, smallest[1]);
            if (smallest[1] < smallest[0]) {
                int tmp = smallest[0];
                smallest[0] = smallest[1];
                smallest[1] = tmp;
            }
        }

        if (money-smallest[0]-smallest[1] < 0) return money;
        return money-smallest[0]-smallest[1];
    }
}