def addBinary( a: str, b: str) -> str:

    ans = [int(i) for i  in (str(int(a) + int(b)))]
    ans.insert(0,0)
    ans.insert(0,0)
    ans.insert(0,0)
    tar = []

    for n in range(len(ans)-1, -1, -1):
        if ans[n] < 2:
            tar.append(ans)
        elif ans[n] >= 2:
            ans[n -1] += ans[n] // 2
            ans[n] = ans[n] % 2
    while True:
        if ans[0] == 0:
            ans.pop(0)
        else:
            break
    ans = ''.join([str(n) for n in ans])
    return ans

print(addBinary('1010','1011'))
        
