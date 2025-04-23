res = []
while True:
    try:
        a = int(input())
        res.append(a)
    except:
        print(max(res))
        print(res.index(max(res))+1)
        break