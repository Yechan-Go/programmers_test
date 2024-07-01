def solution(n):
  m = n**(0.5)
  if m % 1 == 0:
    return int((m+1)*(m+1))
  else:
    return -1
print(solution(121))
print(solution(3))