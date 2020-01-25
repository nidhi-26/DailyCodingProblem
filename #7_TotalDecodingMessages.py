#code

def countDecodingPatterns(s, n):
    if n != 0 and s[0] == '0':
        return 0
    if n == 0 or n == 1:
        return 1
    
    count = 0
    if s[n-1] > '0':
        count = countDecodingPatterns(s, n-1)
    if s[n-2] == '1' or (s[n-2] == '2' and s[n-1] < '7'):
        count += countDecodingPatterns(s, n-2)
        
    return count
    
def countDecodingPatternsDP(s, n):
    count = [0]*(n+1)
    count[0] = 1
    count[1] = 1
    
    for i in range(2, n+1):
        if s[i-1] > '0':
            count[i] = count[i-1]
        if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
            count[i] += count[i-2]
            
    return 0 if s[0] == '0' else count[n]
            

def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        s = input()
        #print(countDecodingPatterns(s, n))
        print(countDecodingPatternsDP(s, n))


if __name__ == '__main__':
    main()
