class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> dict = new HashMap<>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++){
            if(dict.containsKey(nums[i])){
                    if(target == 2*nums[i]){
                    res[0] = dict.get(nums[i]);
                    res[1] = i;
                    return res;
                }
            }
            dict.putIfAbsent(nums[i], i);
        }

        for(int i: dict.keySet()){
            if(dict.containsKey(target - i)){
                res[0] = dict.get(i);
                res[1] = dict.get(target - i);
                break;
            }
        }

        return res;
    }
}