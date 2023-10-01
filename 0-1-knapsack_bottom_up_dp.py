def knapsack(weights, values, goal_weight):
    n = len(weights)
    # validation
    if n != len(values):
        return 0
    # build tabular subproblems with x as indices to pick and y as goal_weight
    dp = [[0 for y in range(goal_weight+1)] for x in range(n+1)]
    for upto_index in range(n+1):
        for sub_problem_goal_weight in range(goal_weight+1):
            if upto_index==0 or sub_problem_goal_weight==0:
                dp[upto_index][sub_problem_goal_weight] = 0
            elif weights[upto_index-1] <= sub_problem_goal_weight:
                picked_prev_index_sub_problem = values[upto_index-1]+dp[upto_index-1][sub_problem_goal_weight-weights[upto_index-1]]
                not_picked_prev_index_sub_problem = dp[upto_index-1][sub_problem_goal_weight]
                dp[upto_index][sub_problem_goal_weight] = max(picked_prev_index_sub_problem, not_picked_prev_index_sub_problem)
            else:
                dp[upto_index][sub_problem_goal_weight] = dp[upto_index-1][sub_problem_goal_weight]
    return dp[n][goal_weight]
