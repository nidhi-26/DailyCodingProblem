def prod(a, n):
    left = [1] * n
    right = [1] * n
    prodArr = [1] * n
    
    for i in range(1, n):
        left[i] = a[i-1] * left[i-1]
        
    for i in range(n-2, -1, -1):
        right[i] = a[i+1] * right[i+1]
        
    for i in range(0, n):
        prodArr[i] = left[i] * right[i]
        
    return prodArr

def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = input().split()
        a = [int(i) for i in a]
        
        prodArr = prod(a, n)
        for i in prodArr:
            print(i, end = ' ')
        print()
        
        
if __name__ == '__main__':
    main()
