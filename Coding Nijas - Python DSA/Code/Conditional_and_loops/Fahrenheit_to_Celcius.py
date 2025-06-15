# Read input as sepcified in the question
# Print output as specified in the question
S = int(input())
E = int(input())
W = int(input())
while E != S:
    S = W + S
print(S, " ", ((32 * S - 32) * 5) / 9)
