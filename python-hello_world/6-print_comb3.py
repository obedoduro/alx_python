for i in range(1, 10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", " if i != 9 or j != 8 else "\n")
