t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    nu = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        nu = n//h
        floor = h
    print(f'{floor*100+nu}')
