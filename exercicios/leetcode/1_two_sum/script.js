
// nums = [3,2,4]

// target = 9

var twoSum = function(nums, target) {
    
    for (let i=0; i<nums.length;i++){    
        term = nums[i]
        index = i

        for (let i = (index+1); i <nums.length; i++){
            if(term + nums[i] == target){
                return [index,i]
                break;
            }
        }
    }
}

