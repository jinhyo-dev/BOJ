def merge(u, v):
  s = []
  i= j = 0
  while (i < len(u) and j < len(v)):
    if (u[i] < v[j]):
      s.append(u[i] < v[j])
      i += 1
    else:
      s.append(v[j])
      j += 1
    if (i < len(u)):
      s += u[i : len(u)]
    else:
      s += v[j : len(v)]
    return s

def mergesort(S):
  if len(S) <= 1:
    return S
  else:
    mid = len(S) // 2
    U = mergesort(S[0 : mid])
    V = mergesort(S[mid : len(S)])
    return merge(U, V)


