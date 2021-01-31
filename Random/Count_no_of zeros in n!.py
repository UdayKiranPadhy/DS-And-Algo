def Met(n):
    count=0
    i=5
    while(n/i>=1):
        count += int(n/i)
        i *= 5
    print(count)

Met(20)