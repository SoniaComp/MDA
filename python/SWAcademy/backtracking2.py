def backtracking(depth, sub_sum):
  global my_min
  for i in range(N):
    if check[i] is False: # 중복 아님
      check[i] = True
      sub_sum += chart[depth][i]
      if sub_sum < my_min: # 가치 있으면
        if depth == N - 1: # 끝 노드
          my_min = sub_sum # 최소값 갱신
        else:
          backtracking(depth + 1, sub_sum)
      sub_sum -= chart[depth[i]]
      check[i] = False
        



T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  chart = [list(map(int, input().split())) for _ in range(N)]
  check = [False] * N
  my_min = 1500
  backtracking(0, 0)
  print('#{} {}'.format(test_case, my_min))