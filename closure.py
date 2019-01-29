def count():
    fs = []
    for i in range(1, 5):
        def f():
             return i*i
        fs.append(f)
    return fs

print(count())