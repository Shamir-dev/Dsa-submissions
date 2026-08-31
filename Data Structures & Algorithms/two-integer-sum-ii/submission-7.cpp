class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res(2);
        unordered_map<int, int> seen;
        for( int i =0; i<numbers.size(); i++){
            int required = target - numbers[i];
            if (seen.count(required)) {
                res = {seen[required]+1, i+1};
                return res;
            }
            else{
                seen[numbers[i]] = i;
            }

            // for (int j = i+1;j<numbers.size(); j++) {
            //     if (numbers[i] + numbers[j] == target){
            //         res = {i+1,j+1};
            //         return res;
            //     }
            // }
        }
        return res;
      
    }
};
