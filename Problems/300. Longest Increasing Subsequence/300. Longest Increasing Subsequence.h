# include <vector>
using namespace std;

class Solution {
private:
    int binarySearch(vector<int>& seq, int target) {
        int l = 0, r = seq.size()-1;

        while (l <= r) {
            int m = (r+l)/2; // Or l + (r-l)/2
            if (seq[m] == target) return m;
            else if (seq[m] < target) l = m+1;
            else if (seq[m] > target) r = m-1;
        }

        return l;
    }

public:
    int lengthOfLIS(vector<int>& nums) {
        // Note that when we see a new num, either it can be new element of a subsequence if
        // if it is larger than the last element of the subsequence or it can replace the
        // (pos)-th position number in the subsequence. Since we construct the invariance that
        // the sub sequence is strictly increasing, the above operation maintains the invariance
        // and can find the longest strictly subsequence.
        vector<int> subseq = {};

        for (int num: nums) {
            int pos = binarySearch(subseq, num);
            if (pos == subseq.size()) subseq.push_back(num);
            else subseq[pos] = num;
        }

        return subseq.size();
    }
};