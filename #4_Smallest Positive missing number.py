#code

def findSmallestPositiveMissing(a, n):
    test = [0]*(n+1)
    for j in range(0, n):
        if int(a[j]) > 0 and int(a[j]) < n+1:
            test[int(a[j])] = 1
    
    for i in range(1, n+1):
        if test[i] == 0:
            return i;
            
    return n+1
    
def main():
    t = int(input())
    while(t):
        t -= 1
        n = int(input())
        a = input().strip().split()
        #arr = [int(i) for i in a]
        
        print(findSmallestPositiveMissing(a, n))

if __name__ == '__main__':
    main()
