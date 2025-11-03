def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        for row in range(len(board)):
            if board[row][move - 1] != 0:
                doll = board[row][move - 1]
                board[row][move - 1] = 0

                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                break
    return answer
                
    
        
    
    return answer