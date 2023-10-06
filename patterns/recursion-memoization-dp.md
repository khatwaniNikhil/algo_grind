# References
https://www.enjoyalgorithms.com/blog/top-down-memoization-vs-bottom-up-tabulation
https://takeuforward.org/recursion/introduction-to-recursion-understand-recursion-by-printing-something-n-times/
https://takeuforward.org/data-structure/dynamic-programming-introduction/

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
###### recursive - refer recursion(with memoziation) tricks first and then later convert to tabulization 
```
Try to represent the given problem in terms of index. 
F(n): min energy spent to reach from step 0 to step n. 
F(0) = 0 
Do all possible operations on that index according to the problem statement. 
if (n==0) return 0 
jumpOneCost = f(n-1) + abs(h[n-1], h[n]) 
if n>=2 
jumpTwoCost  =  f(n-2) + abs(h[n-2], h[n])   
Take the minimum of all the choices  
return min(jumpOneCost, jumpTwoCost) recursive to dp  
```

###### Recursive + memoization 
```
int dp[]=new int[n]
Arrays.fill(dp,-1);
dp[0]=0;
if(dp[n]!=-1) return dp[n];
jumpTwoCost = Integer.MAX_VALUE;
jumpOneCost = f(n-1) + abs(h[n-1], h[n]) 
if n>=2 
jumpTwoCost  =  f(n-2) + abs(h[n-2], h[n])   
Take the minimum of all the choices  
dp[n] = min(jumpOneCost, jumpTwoCost) 
return dp[n]
Tabularization
int dp[]=new int[n]
Arrays.fill(dp,-1);
dp[0]=0;
i>=1 till n-1
jumpOneCost 
jumpTwoCost 
dp[ind] = Math.min(jumpOneCost, jumpTwoCost) 
Return dp[n-1]
```

###### space optimised dp 
```
int n=height.length;
   int prev=0;
  int prev2=0;
  for(int i=1;i<n;i++){
      
      int jumpTwo = Integer.MAX_VALUE;
      int jumpOne= prev + Math.abs(height[i]-height[i-1]);
      if(i>1)
        jumpTwo = prev2 + Math.abs(height[i]-height[i-2]);
    
      int cur_i=Math.min(jumpOne, jumpTwo);
      prev2=prev;
      prev=cur_i;
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
			
			if(i-jumpSteps>0){
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

#### 4. climbing-stairs
https://leetcode.com/problems/climbing-stairs/description/
```
class Solution {
    public int climbStairs(int n) {
        // 1 <= n <= 45
        // dp[n] = dp[n-1] + dp[n-2]
        // base cases:
        // dp[0] = 0
        // dp[1] = 1
        // dp[2] = 2
        if(n<=2)
            return n;
        else {
            int prev = 2;
            int prev2 = 1;
            for(int i=3;i<=n;i++){
                int cur_i = prev + prev2;
                prev2 = prev;
                prev = cur_i;
            }
            return prev;
        }
    }
}
```

#### 5. https://practice.geeksforgeeks.org/problems/geek-jump/1
```
class Solution{
    public int minimumEnergy(int arr[],int N){
        int dp[] = new int[N];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        
        for(int i=1;i<N;i++) {
            int jumpTwoCost = Integer.MAX_VALUE;
            //jumpOneCost
            int jumpOneCost = dp[i-1] + Math.abs(arr[i] - arr[i-1]);    
            
            //jumpTwoCost
            if(i>=2) {
                jumpTwoCost = dp[i-2] + Math.abs(arr[i] - arr[i-2]);    
            }
            dp[i] = Math.min(jumpOneCost, jumpTwoCost);
        }
        return dp[N-1];
    }
}
```

#### 6. Print subsequence problem
###### Rules of a valid subsequence
for each subsequence conmbination - order of picked elements(one or more elements) is same as they were in original array(irrespective all elements(contigous) are picked or some are picked(non contigous))
###### approach
for each element, either we take or not take that element in the current subsequence
###### pseudo code
```
f(index, inputArr, outlist) {
  if(index >=n) {
     print(outlist);
     return;
  }
  outlist.add(inputArr[i]);
  f(index+1,inputArr, outlist);
  outlist.remove(inputArr[i]);
  f(index+1,inputArr, outlist);
```
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
    // // pick current and then solve subproblems
    currSubSequence.add(arr[startIndex]);
    printAllSubSequencesInternal(result, startIndex+1, arr, currSubSequence);

    // // not pick current and then solve subproblems
    currSubSequence.remove(currSubSequence.size()-1);
    printAllSubSequencesInternal(result, startIndex+1, arr, currSubSequence);

}
```

#### 7. Maximum sum of non-adjacent elements
//base case i==0
dp[0] = arr[0];

for(int i=1;
//pick current elem, then can’t pick adjacent and solve i-2 subproblem
if(i>1)
pick = arr[i] + call(i-2)

// do not pick current elem, solve i-1 subproblem
not_pick = 0+call(i-1)

return max(pick, not_pick)










