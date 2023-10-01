# Ways to formulate longest_non_consecutive_sum are:
# 1. We have a flower box with a few places to plant flowers. Each location has nutrients that influence how tall the flower will be. You can't plant flowers next to each other, and we want to maximize the total height of all the planted flowers ?
# 2. you are a robber who has found a block of houses to rob. Each house 𝑖 has a non-negative 𝑣𝑖 worth of value inside that you can steal. However, due to the way the security systems of the houses are connected, you’ll get caught if you rob two adjacent houses. What’s the maximum value you can steal from the block?

# Breaking into sub problems, here i means, all elements from index 0 to ith index are considered
# max_non_consec_sum(i) = max(
#                            v(i)+ max_non_consec_sum(i-2),
#                            max_non_consec_sum(i-1)    

# since we want to consider elements at each index from 0 to n-1, so problem we need to solve is max_non_consec_sum(n-1)

if __name__ == "__main__":
    from timeit import Timer
    
    # bottom up: sub problems represent as DAG and executed in order dependencies of sub problems as per directions of edges in DAG - this avoids storing all results in cache, just store last two executed sub problems results to solve future sub problems. It leads to space efficiency
    # solve max_non_consec_sum(n-1)
    def max_non_consecutive_sum(values):
        # f(i-2)
        a = 0
        # f(i-1)
        b = 0
        for val in values:
            a,b = b,max(val + a, b)
        return b
    t = Timer(lambda: fib_bottom_up(30))
    print(t.timeit(number=100))
