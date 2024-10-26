# cook your dish here
def count_tuesdays_in_spooky_days(T, cases):
    results = []
    for N in cases:
        if N < 2:
            results.append(0)
        else:
            
            tuesdays = 1 + (N - 2) // 7
            results.append(tuesdays)
    return results

T = int(input())
cases = [int(input()) for _ in range(T)]
results = count_tuesdays_in_spooky_days(T, cases)
for res in results:
    print(res)
