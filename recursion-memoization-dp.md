# Recursion tricks 
1. Try to represent the given problem in terms of index.
2. Do all possible operations on that index according to the problem statement.
3. To count all possible ways - sum of all stuff.
   To find minimum/maximum - Take Minimum/maximum of all stuff.

# Memoization
	IF BASE CASE ---RETURN ANSWER
	IF ALREADY COMPUTED - RETURN FROM CACHE
	RECURSIVELY SOLVE USING SUBPROBLEMS & STORE in dp[] 

# Tabularization
1. DP array init with -1 as values
2. BASE CASE -- STORE ANSWERS IN dp[]
3. ITERATE from: index after base case till: n
4. build dp[i] using previous solved subproblems
5. return dp[n] 

# space optimized Tabularization 
    check if can avoid storing all subproblems results

# greedy versus dynamic https://www.baeldung.com/cs/greedy-approach-vs-dynamic-programming
## greedy
decision is made on the basis of current information only
need to establish before proceeding that local optimality leads to an optimal global solution

## Dynamic
it optimises the recursive backtracking  
gives optimal solution
requires more space at times to store the intermediate states in dp[]

# DP Problems
#### stairs climb https://www.enjoyalgorithms.com/blog/climbing-stairs-problem
dp - similar to fibbonacci series but after i=3
dp[0] = 0
dp[1] = 1
dp[2] = 2
i>=3 till n-1
dp[i] = dp[i-1]+ dp[i-2];
return dp[n-1]
space optimised dp - keep only last two values
if(n<=2)
     return n;  else {      int prev = 2;      int prev2 = 1;      for(int i=3;i<=n;i++){          int cur_i = prev + prev2;          prev2 = prev;          prev = cur_i;      }      return prev;  } 

frog energy spent - frog jump 1 or 2, min energy spent cost to reach destination
https://www.codingninjas.com/studio/problems/frog-jump_3621012 
Greedy not applicable
local optima does not guarantee global optima(some jumps can be low cost but now restricted on next jumps to take which might increase overall cost of the path)
recursive - refer recursion(with memoziation) tricks first and then later convert to tabulization 
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
Recursive + memoization 
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
space optimised dp 

  
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
        
  } https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-distances-dp-4/  
 
