n = input()
cnt = 0

for h in range(int(n)+1):
    if '3' in str(h):
        cnt += 1*60*60
        continue

    for m in range(60):
        if '3' in str(m):
            cnt += 1*60
            continue

        for s in range(60):
            if '3' in str(s):
                cnt += 1
                # print(str(h)+str(m)+str(s))
print(cnt)