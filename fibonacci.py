if __name__ == "__main__":
    from timeit import Timer
    # top down with memoization
    def fib_top_down_with_memoization(n, cache=None):
	    if n==0: return 1
	    if n==1: return 1
	    if cache is None: cache = {}
	    if n in cache: return cache[n]
	    result =  fib_top_down_with_memoization(n-1, cache) + fib_top_down_with_memoization(n-2, cache)
	    cache[n] = result
	    return result
    t = Timer(lambda: fib(30))
    print(t.timeit(number=100))
    
    # bottom up: sub problems represent as DAG and executed in order dependencies of sub problems as per directions of edges in DAG - this avoids storing all results in cache, just store last two executed sub problems results to solve future sub problems. It leads to space efficiency
    def fib_bottom_up(n):
        a = 1
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
    t = Timer(lambda: fib_bottom_up(30))
    print(t.timeit(number=100))
