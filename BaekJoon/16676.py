# 백준16676: 근우의 다이어리 꾸미기
def joyGo(N: str) -> int: 
  if len(N) == 1: 
      return 1
  elif int(N) >= int('1' * len(N)): 
      return len(N)
  else: 
      return len(N) - 1

if __name__ == "__main__": 
  print(joyGo(input()))
