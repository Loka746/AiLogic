def minWindow(s,t):
  for i in range(len(s)):

    for j in range(i+1,len(s)+1):

      window = s[i:j]

      if all(window.count(c) >= t.count(c) for c in set(t)):
        return window

  return ""

s = input()
t = input ()

print(minWindow(s,t))
