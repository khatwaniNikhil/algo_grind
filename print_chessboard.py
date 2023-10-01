def get_chessboard(dim):
    chessboard = [['W' for _ in range(dim)] for _ in range(dim)]
    
    for i in range(dim):
        for j in range(dim):
            if (i + j) % 2 == 0:
                chessboard[m][n] = 'B'
    return chessboard
