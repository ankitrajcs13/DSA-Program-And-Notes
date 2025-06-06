# method 1: 
# will only work if there is no zero.

# logic: We just need to take product of all numbers & also keep tracking the largest negative number.
# Check if the product is negative then devide it by the largest negative number. 
# ( Basically we want to remove the largest negative number or you can say smallest abs valued negative number)

# time: O(n)

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mul= 1
        largestNegative= -9 # will give the largest negative number considering sign i.e -1 > -2
        for num in nums:
            if num < 0:
                largestNegative= max(largestNegative, num)
            mul*= num
        if mul >= 0:
            return mul
        # if negative then remove the largest negtaive ele from the multiplication.
        return abs(mul) // abs(largestNegative)


# method 2: Handling all the corner cases 
"""
We need to handle : When array contains only zero. 
For this keep track of largest_number in array and number_of_negative_number.

Other everything is same , just update multiplication when num != 0.
"""
# Time: O(n)


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mul= 1  # will store the multiplication of whole array except zero.
        largest= max(nums) # will give the max ele in whole array. This will be useful if array contains only zero.
        negativeCount= 0
        largestNegative= -9 # will give the largest negative number considering sign i.e -1 > -2
        for num in nums:
            if num < 0:
                largestNegative= max(largestNegative, num)
                negativeCount+= 1
            if num != 0:
                # for handling the cases when there is '0' with len(arr) >= 2.
                mul*= num
        if largest == 0 and negativeCount <= 1:
            # for handling the cases like [0], [0, -1]
            return 0
        if mul > 0:
            return mul
        # if negative then remove the largest negtaive ele from the multiplication.
        return abs(mul) // abs(largestNegative)

# Java
"""
class Solution {

    public long maxStrength(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        long mul = 1; // Store the multiplication of the whole array except zero
        int largest = Integer.MIN_VALUE;
        int negativeCount = 0;
        int largestNegative = Integer.MIN_VALUE;
        boolean hasNonZero = false; // To check if there's any non-zero element

        for (int num : nums) {
            if (num < 0) {
                largestNegative = Math.max(largestNegative, num);
                negativeCount++;
            }
            if (num != 0) {
                mul *= num;
                hasNonZero = true;
            }
            largest = Math.max(largest, num);
        }

        if (!hasNonZero) {
            // If all elements are zero or there’s no valid multiplication
            return 0;
        }

        if (negativeCount == 1 && largest == 0 && negativeCount <= 1) {
            // Case like [0], [0, -1]
            return 0;
        }

        if (mul > 0) {
            return mul;
        }

        // If negative, remove the largest negative element from the multiplication
        return mul / largestNegative;
    }
}
"""
