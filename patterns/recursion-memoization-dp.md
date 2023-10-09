# References
1. https://www.enjoyalgorithms.com/blog/top-down-memoization-vs-bottom-up-tabulation
2. https://takeuforward.org/recursion/introduction-to-recursion-understand-recursion-by-printing-something-n-times/
3. https://takeuforward.org/data-structure/dynamic-programming-introduction/

# Recursion
1. function calls itself, can be described pictorically in tree format known as recursion tree.
2. base condition leads to stack unwinding and return to previous call.
3. can be implemented as
    1. parameterised recursion(extra param to store/calculate the output)
    2. functional recursion(calls self with modified arg. until base case reached)
5. Try to represent the given problem in terms of index.
6. Do all possible operations on that index according to the problem statement.
7. To count all possible ways - sum of all stuff.
   To find minimum/maximum - Take Minimum/maximum of all stuff.

# Memoization 
Top down - focus on main problem and arrive to base case with intermediate results cache. Since all possible subproblems are solved
once, time complexity is O(N). Extra space for caching leads to space complexity of O(n)
![1 rCch4Ju3PcPPMpvFireFyQ](https://github.com/khatwaniNikhil/ds_algo/assets/3686308/22106184-c851-4dcf-8c38-8909a2a8e98b)

IF BASE CASE ---RETURN ANSWER
IF ALREADY COMPUTED - RETURN FROM CACHE
RECURSIVELY SOLVE USING SUBPROBLEMS & STORE in dp[] 

```
public class MyClass {
    public static void main(String args[]) {
      int n =6;
      int dp[] = new int[n+1];
      Arrays.fill(dp, -1);
      System.out.println(fibonacciMemoization(n, dp));
    }
    
    static int fibonacciMemoization(int n, int[] dp) {
        if(n<=1) return n;
        if(dp[n] !=-1)
            return dp[n];
        dp[n] = fibonacciMemoization(n-1, dp) + fibonacciMemoization(n-2, dp);
        return dp[n];
    }
}
```
   	
# Tabulation 
Bottom up - iterative, loop over index and build over existing solved subproblems
![1 9YUE1V0fYhFujaXEcmX3wg](https://github.com/khatwaniNikhil/ds_algo/assets/3686308/c78ebf3a-b0a5-4ca1-9d02-cfc24514f513)

1. DP array init with -1 as values
2. BASE CASE -- STORE ANSWERS IN dp[]
3. ITERATE from: index after base case till: n
4. build dp[i] using previous solved subproblems
5. return dp[n]

```
public class MyClass {
    public static void main(String args[]) {
      int n =6;
      int dp[] = new int[n+1];
      Arrays.fill(dp, -1);
      System.out.println(fibonacciTabulation(n, dp));
    }
    
    static int fibonacciTabulation(int n, int[] dp) {
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2;i<=n;i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
```

#### Space optimized Tabulation 
    check if can avoid storing all subproblems results

# Greedy versus Dynamic 
https://www.baeldung.com/cs/greedy-approach-vs-dynamic-programming

#### Greedy
decision is made on the basis of current information only
need to establish before proceeding that local optimality leads to an optimal global solution

#### Dynamic
it optimises the recursive backtracking  
gives optimal solution
requires more space at times to store the intermediate states in dp[]

# DP Problems
#### 1. stairs climb 
https://www.enjoyalgorithms.com/blog/climbing-stairs-problem

###### dp approach - similar to fibbonacci series but after i=3
```
dp[0] = 0
dp[1] = 1
dp[2] = 2
i>=3 till n-1
dp[i] = dp[i-1]+ dp[i-2];
return dp[n-1]
```
###### space optimised dp - keep only last two values
```
if(n<=2)
     return n;
else {
int prev = 2;
int prev2 = 1;
for(int i=3;i<=n;i++)
{
	int cur_i = prev + prev2;
	prev2 = prev;
	prev = cur_i;
}
return prev;
} 
```

#### 2. frog energy spent - frog jump 1 or 2, min energy spent cost to reach destination
https://www.codingninjas.com/studio/problems/frog-jump_3621012 

###### Greedy not applicable
local optima does not guarantee global optima(some jumps can be low cost but now restricted on next jumps to take which might increase overall cost of the path)
 
 ###### Recursive + memoization 
```
// 1. problem in terms of index
// 2. cache intermediate results
// 3. all operations on index
static int frogJumpMemoization(int ind,int[] height,int[] dp) {
        if(ind ==0) return 0;
        if(dp[ind] !=-1) return dp[ind];
        int reachIndWithOneJumpCost = frogJumpMemoization(ind-1, height, dp) + Math.abs(height[ind] - height[ind-1]);
        int reachIndWithTwpoJumpCost = Integer.MAX_VALUE;
        if(ind >1)
            reachIndWithTwpoJumpCost = frogJumpMemoization(ind-1, height, dp) + Math.abs(height[ind] - height[ind-1]);             
        
        dp[ind] = Math.min(reachIndWithOneJumpCost, reachIndWithTwpoJumpCost);
        return dp[ind];
}
```

###### Tabularization
```
static int frogJumpTabulization(int ind,int[] height,int[] cost) {
        cost[0] = 0;
        
        for(int reachIndex=1;reachIndex<=ind;reachIndex++) {
            int reachIndWithOneJumpCost = cost[reachIndex-1] + Math.abs(height[ind] - height[ind-1]);
            int reachIndWithTwpoJumpCost = Integer.MAX_VALUE;
            if(ind >1)
                reachIndWithTwpoJumpCost = cost[reachIndex-2] + Math.abs(height[ind] - height[ind-2]);  
            cost[reachIndex] = Math.min(reachIndWithOneJumpCost, reachIndWithTwpoJumpCost);
        }
        return dp[ind];
    }
```

###### space optimised dp 
```
static int frogJumpTabulization(int ind,int[] height) {
        int prev  = 0;
        int prev2 = 0;
        
        for(int reachIndex=1;reachIndex<=ind;reachIndex++) {
            int reachIndWithOneJumpCost = prev + Math.abs(height[ind] - height[ind-1]);
            int reachIndWithTwpoJumpCost = Integer.MAX_VALUE;
            if(ind >1)
                reachIndWithTwpoJumpCost = prev2 + Math.abs(height[ind] - height[ind-2]);  
            int current = Math.min(reachIndWithOneJumpCost, reachIndWithTwpoJumpCost);
            prev2 = prev;
            prev = current;
        }
        return prev;
    }
```
        
#### 3. dynamic-programming-frog-jump-with-k-distances-dp-4
https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-distances-dp-4/
```
class Solution {
   public int minEnergy(int arr[], int N, int K) {
	int[] dp = new int[N];
	Arrays.fill(dp, -1);
	dp[0] = 0;
	
	for(int i=1;i<N;i++) {
		int minEnergy = Integer.MAX_VALUE;
	
		for(int jumpSteps=1; jumpSteps<=K; jumpSteps++) {
			
			if(i-jumpSteps>=0){
				 int jumpCost = dp[i-jumpSteps] + Math.abs(arr[i], arr[i-jumpSteps]);
				 minEnergy  = Math.min(minEnergy, jumpCost);
			}
		
		}
		dp[i] = minEnergy;
	}
	return dp[N-1];
   }

}
```
#### 4. Print subsequence problem
###### Rules of a valid subsequence
for each subsequence conmbination - order of picked elements(one or more elements) is same as they were in original array(irrespective all elements(contigous) are picked or some are picked(non contigous))
###### approach
for each element, either we take or not take that element in the current subsequence
```
public static void main(String[] args) {
    int[] nums = {1,2,3};
    List<List<Integer>> result=new ArrayList<>();
    printAllSubSequencesInternal(result,0,nums,new ArrayList<>());
    for(List<Integer> subSeq:result) {
        System.out.println(subSeq);
    }
}
```
```
public static void printAllSubSequencesInternal(List<List<Integer>> result, int startIndex, int[] arr, List<Integer> currSubSequence) {
    // base case index>=n, return current element
    if(startIndex == arr.length) {
        result.add(new ArrayList<>(currSubSequence));
        return;
    }
    // pick current and then solve subproblems
    currSubSequence.add(arr[startIndex]);
    printAllSubSequencesInternal(result, startIndex+1, arr, currSubSequence);

    // not pick current and then solve subproblems
    currSubSequence.remove(currSubSequence.size()-1);
    printAllSubSequencesInternal(result, startIndex+1, arr, currSubSequence);

}
```

#### 5. Maximum sum of non-adjacent elements
https://leetcode.com/problems/house-robber

```
public int rob(int[] nums) {
        int dp[] = new int[nums.length];
        dp[0] = nums[0];
        if(nums.length>=2) {
            dp[1] = Math.max(nums[0], nums[1]);
            for(int i=2;i<nums.length; i++) {
                dp[i] = Math.max(dp[i-1], dp[i-2]+nums[i]);
            }    
        }
        return dp[nums.length-1];
        
    }
```
