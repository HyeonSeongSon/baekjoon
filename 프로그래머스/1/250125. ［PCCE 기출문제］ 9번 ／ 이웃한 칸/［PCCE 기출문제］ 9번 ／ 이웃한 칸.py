def solution(board, h, w):
    n = len(board)  # 보드 크기
    count = 0       # 같은 색의 이웃 칸 수
    color = board[h][w]  # 기준 색상

    # 방향: 우, 하, 상, 좌
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        # 보드 경계 조건 확인
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h_check][w_check] == color:
                count += 1

    return count
    

        