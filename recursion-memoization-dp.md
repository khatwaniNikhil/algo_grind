# Recursion
https://takeuforward.org/recursion/introduction-to-recursion-understand-recursion-by-printing-something-n-times/
1. function calls itself, can be described pictorically in tree format known as recursion tree.
2. base condition leads to stack unwinding and return to previous call.
3. can be implemented as
    1. parameterised recursion(extra param to store/calculate the output)
    2. functional recursion(calls self with modified arg. until base case reached)
5. Try to represent the given problem in terms of index.
6. Do all possible operations on that index according to the problem statement.
7. To count all possible ways - sum of all stuff.
   To find minimum/maximum - Take Minimum/maximum of all stuff.

## Print subsequence problem
https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6&pp=iAQB
https://www.youtube.com/watch?v=eQCS_v3bw0Q

### Rules - valid subsequence
for each subsequence conmbination - order of picked elements(one or more elements) is same as they were in original array(irrespective all elements(contigous) are picked or some are picked(non contigous))
### approach
for each element, either we **take or not take that element** in the current subsequence

#### pseudo code - print all possible sequences
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


#### pseudo code - print all possible sequences with sum k
```
f(index, inputArr, outlist, sum, k) {
  if(index >=n && sum==k) {
     print(outlist);
     return;
  }
  outlist.add(inputArr[i]);
  sum += inputArr[i];
  f(index+1,inputArr, sum, outlist);
  outlist.remove(inputArr[i]);
  sum -= inputArr[i];
  f(index+1,inputArr, sum, outlist);
```

#### pseudo code - print any one of the possible sequences with sum k
```
f(index, inputArr, outlist, sum, k) {
  if(index >=n) {
     if(sum==k) {
        print(outlist);
        return true;
     }
     else 
       return false;
 }

outlist.add(inputArr[i]);
sum += inputArr[i];
if(f(index+1,inputArr, sum, outlist) == true) {
    return true;
}
outlist.remove(inputArr[i]);
sum -= inputArr[i];
if(f(index+1,inputArr, sum, outlist) == true) {
    return true;
}
return false;
```

#### pseudo code - print count of the possible sequences with sum k
```
int f(index, inputArr, outlist, sum, k) {
  if(index >=n) {
     if(sum==k) {
        print(outlist);
        return 1;
     }
     else 
       return 0;
 }

outlist.add(inputArr[i]);
sum += inputArr[i];
int l = f(index+1,inputArr, sum, outlist);

outlist.remove(inputArr[i]);
sum -= inputArr[i];

int r = f(index+1,inputArr, sum, outlist)
return l + r;
```


# Dynamic programming
Overlapping/interdependent sub problems. 

## Memoization (Recursion with cache - top down)
	IF BASE CASE ---RETURN ANSWER
	IF ALREADY COMPUTED - RETURN FROM CACHE
	RECURSIVELY SOLVE USING SUBPROBLEMS & STORE in dp[] 

## Tabulation (bottom up, iterative)
1. DP array init with -1 as values
2. BASE CASE -- STORE ANSWERS IN dp[]
3. ITERATE from: index after base case till: n
4. build dp[i] using previous solved subproblems
5. return dp[n] 

## space optimized Tabulation 
    check if can avoid storing all subproblems results

## greedy versus dynamic 
https://www.baeldung.com/cs/greedy-approach-vs-dynamic-programming

### greedy
at each step choose best option with hope of optimal solution at the end.
suitable for problems where local optimality leads to an optimal global solution.

#### Greedy Example
Say that we are given a set of activities. Each activity has a start and an end time. We’re asked to find the maximum number of activities that don’t intersect, or, in other words, that can be performed by a single person. 

#### The greedy approach is to always choose the activity with the earliest ending time

### Dynamic
it optimises the recursive backtracking  
gives optimal solution
requires more space at times to store the intermediate states in dp[]

# DP Problems
## 1. stairs climb 
https://www.enjoyalgorithms.com/blog/climbing-stairs-problem
### dp approach - similar to fibbonacci series but after i=3
```
dp[0] = 0
dp[1] = 1
dp[2] = 2
i>=3 till n-1
dp[i] = dp[i-1]+ dp[i-2];
return dp[n-1]
```
### space optimised dp - keep only last two values
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

## 2. frog energy spent - frog jump 1 or 2, min energy spent cost to reach destination
https://www.codingninjas.com/studio/problems/frog-jump_3621012 

### Greedy not applicable
local optima does not guarantee global optima(some jumps can be low cost but now restricted on next jumps to take which might increase overall cost of the path)
#### recursive - refer recursion(with memoziation) tricks first and then later convert to tabulization 
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

#### Recursive + memoization 
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

#### space optimised dp 
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
        
## 3. dynamic-programming-frog-jump-with-k-distances-dp-4
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

## 4. climbing-stairs
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

## 5. https://practice.geeksforgeeks.org/problems/geek-jump/1
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

## House robber
https://leetcode.com/problems/house-robber/

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


##
Printing Subsequences(contigous as well as non contiguous)
elements order has to be maintained

public static void main(String[] args) {
    int[] nums = {1,2,3};
    List<List<Integer>> result=new ArrayList<>();
    printAllSubSequencesInternal(result,0,nums,new ArrayList<>());
    for(List<Integer> subSeq:result) {
        System.out.println(subSeq);
    }
}

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
Maximum sum of non-adjacent elements
//base case i==0
dp[0] = arr[0];

for(int i=1;


//pick current elem, then can’t pick adjacent and solve i-2 subproblem
if(i>1)
pick = arr[i] + call(i-2)

// do not pick current elem, solve i-1 subproblem
not_pick = 0+call(i-1)

return max(pick, not_pick)










