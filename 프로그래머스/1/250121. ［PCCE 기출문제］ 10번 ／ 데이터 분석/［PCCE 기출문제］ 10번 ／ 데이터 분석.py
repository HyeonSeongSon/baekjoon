def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {'code':0,'date':1,'maximum':2,'remain':3}
    for i in range(len(data)):
        if data[i][dic[ext]] < val_ext:
            answer.append(data[i])
    answer = sorted(answer, key=lambda x: x[dic[sort_by]])
    return answer