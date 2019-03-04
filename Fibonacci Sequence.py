def main():
    x = 0
    y = x + 1
    z = x + y
    print(x)
    print(y)
    print(z)
    for side in range (20):
        x = y + z
        y = x + z
        z = x + y
        print(x)
        print(y)
        print(z)
main()
