# Divide and conquer
## 1. longest-nice-substring
https://leetcode.com/problems/longest-nice-substring/
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. Input: s = "YazaAay" Output: "aAa"

### Approach
1. Maintain an set of all unique characters by case.
2. Iterate input string and stop at char for which both upper and lowercase are not found. Current char is somewhat the divide and conquer criteria as it cannot be part of any nice string.
3. So we need to search for nice strings in left side or right side.
4. Return one with larger size and in case both nice string from left and right has same size, return left for earliest occurence.
5. Base case, input less than 2 return empty string.
https://www.youtube.com/watch?v=20mjBSByOaQ


# Sliding window https://leetcode.com/tag/sliding-window/

## 1. Substrings of Size K with Distinct Characters/Good substrings
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


### Approach
1. For each sliding window of size k, check all chars are distinct or not
2. code
   1. start = 0, end = 0, count = 0
   2. iterate till first k size window reached:
       1. increment end and keep adding to set
       2. 1st window size reached - check for distinct
       3. when window size==k, check all the k chars distinct or not. update count
   3. iterate over other sliding windows until end is not equal to end index of string
       1. then start++, end++, update set and check all the k chars distinct or not. update count 
        
   
## 2. Find the K-Beauty of a Number
https://leetcode.com/problems/find-the-k-beauty-of-a-number/
Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.

Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.


### Approach
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

### Approach
same as above problem, just check for divisor   

## 4. Minimum Recolors to Get K Consecutive Black Blocks
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks. In one operation, you can recolor a white block such that it becomes a black block. Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.


Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.


### Approach
optimise for finding a sliding window with max black boxes present
   
## 5. Minimum Difference Between Highest and Lowest of K Scores
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized. Return the minimum possible difference.

Example 1:

Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.


### Approach  
If only two elements to be picked up from the array and difference to be reduced - we could have sorted the array and compared each consecutive pair difference to find the min. difference.
But here we need to pick K elements(not necessarily two) and as soon as K elements are picked-max and min among them will be dynamic. Applying the pattern of closest two above, here we need to pick closest K elements. So we can sort the elements and look for K consecutive and take diff of first and last of each window and compare across window

## 11. Find metric(avg./sum) of each sub array of size K(followed by max value of metric)
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
   1. maintain last sliding window sum
   2. move sliding window by 1 
   3. to calculate current sub-array sum - last sum is adjusted(basis elem. removed and added)


      
