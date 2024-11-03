# cook your dish here
n = int(input())
cumulative_score_p1 = 0
cumulative_score_p2 = 0
max_lead = 0
winner = 0

for _ in range(n):
    Si, Ti = map(int, input().split())
    cumulative_score_p1 += Si
    cumulative_score_p2 += Ti
    current_lead = abs(cumulative_score_p1 - cumulative_score_p2)
    
    if current_lead > max_lead:
        max_lead = current_lead
        winner = 1 if cumulative_score_p1 > cumulative_score_p2 else 2

print(winner, max_lead)