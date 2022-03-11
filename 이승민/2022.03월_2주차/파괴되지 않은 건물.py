def solution(board, skill):
    answer = 0
    row = len(board) 
    col = len(board[0])
    sum_board = list([0]*(col+1) for _ in range(row+1))
    for type,a,b,c,d,degree in skill :
        if type == 1 :
            degree = -degree
        sum_board[a][b] += degree
        sum_board[a][d+1] += -degree
        sum_board[c+1][b] += -degree
        sum_board[c+1][d+1] += degree
        
    for i in range(row) :
        for j in range(col) :
            sum_board[i][j+1] += sum_board[i][j]
            
    for j in range(col) :
        for i in range(row) :
            sum_board[i+1][j] += sum_board[i][j]
    
    for i in range(row):
        for j in range(col):
            board[i][j] += sum_board[i][j]
            if board[i][j] > 0: answer += 1
            
    return answer