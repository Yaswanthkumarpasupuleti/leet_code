class Solution {
    public int searchInsert(int[] nums, int target) {
        int res =0;
        int n = nums.length;
        if(nums[0] > target){
            return 0;
        }
        if(nums[n-1] < target){
            return n;
        }
        for(int i =0 ; i < n-1 ; i++){
            if(nums[i] < target  && nums[i+1] >= target){
                res = i+1;
                break;
            }
        }
        return res;
        
    }
}