#10809

s = list(input())
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in alpha:
  if i in s: # alphabet중 baekjoon 포함될 경우.
    print(s.index(i)) 
  else:
    print(-1)
