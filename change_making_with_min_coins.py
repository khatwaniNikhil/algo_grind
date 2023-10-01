# f(i,t) 
# where t is target
#  i => available denominations to choose among indexes 0 to i

# f(i,t) =  min_coins_among(
#            pick largest denomination & solve reduced target subproblem, 
#            skip largest denomination & solve same target subproblrm)

#           min. no. coins(
#                1 + f(i, t-A[i])  
#                f(i-1, t))

# since two inputs are there, dependency DAG is not straightforward and all some sub problems do not required to be solved, we will go top down with memoization
if __name__ == "__main__":
    import math
    from timeit import Timer

    def change_making_memoization(denominations, target):
        cache = {}

        def subproblem(i,t):
            if (i,t) in cache: return cache[(i,t)]
            # choice_take: largest denomination & solve reduced target subproblem
            val = denominations[i]
            if val > t:
                choice_take = math.inf
            elif val == t:
                choice_take = 1
            else:
                choice_take = 1 + subproblem(i, t - val)

            #chose_leave: skip largest denomination & solve same target subproblrm)    
            if i==0:
                choice_leave = math.inf
            else:
                choice_leave = subproblem(i-1, t)

            optimal = min(choice_take, choice_leave)    
            cache[(i, t)] = optimal
            return optimal
         
        return subproblem(len(denominations)-1, target)
    t = Timer(lambda: change_making_memoization([1,5,12,19],16))
    print(t.timeit(number=100)) 
