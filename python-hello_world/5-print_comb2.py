for num in range(100):
    print(str(num).zfill(2), end=", " if num < 99 else "\n")
