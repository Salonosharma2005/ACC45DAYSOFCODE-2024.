# cook your dish here
import sys
input = sys.stdin.read

def calculate_total_time(n, a, b):
    
    rounds = n.bit_length() - 1
    
    total_time = (rounds * a) + ((rounds - 1) * b)
    return total_time

def main():
    data = input().strip().split()
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        n = int(data[index])
        a = int(data[index + 1])
        b = int(data[index + 2])
        index += 3
        
        result = calculate_total_time(n, a, b)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()