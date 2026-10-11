def permutations(s):

  res = []

  def backtrack(current,remaining):

    if len(remaining) == 0:

      res.append(current)

      return 

    for i in range(len(remaining)):

      backtrack(current + remaining[i],remaining[:i] + remaining[i+1:])
  backtrack("",s)
  return res


s = input()

print(permutations(s))
