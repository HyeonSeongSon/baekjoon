def solution(board, moves):
    answer = 0
    pocket = []
    for i in moves:
        # print(f'i={i}')
        for f in range(len(board)):
            # print(f'f={f}')
            if board[f][i-1] != 0:
                # print(f'target={board[f][i-1]}')
                pocket.append(board[f][i-1])
                board[f][i-1] = 0
                break
        if len(pocket) >=2:
            # print(pocket)
            # print(pocket[-1])
            # print(pocket[-2])
            # print(pocket[-1] - pocket[-2])
            if pocket[-1] - pocket[-2] == 0:
                pocket.pop(-1)
                pocket.pop(-1)
                answer +=2
                
    
        
    
    return answer