def findPair(arr, k):
    s = set()
    for i in arr:
        t = k - i
        if t in s:
            return 'Yes'
        s.add(i)
    return 'No'

def main():
    t = int(input())
    while t:
        t -= 1
        n, k = input().split()
        n, k = int(n), int(k)
        arr = input().split()
        arr = [int(i) for i in arr]
        
        print(findPair(arr, k))

if __name__ == '__main__':
    main()
