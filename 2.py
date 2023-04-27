
n, x = map(int, input().split())
n_list = list(map(int, input().split()))
answer_list = []

for i in range(n_list):
    if n_list[i] > x:
        answer_list.append(n_list[i])

answer=" ".join([str(_) for _ in answer_list])
print(answer)