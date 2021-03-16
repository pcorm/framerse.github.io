def main():
  fam = [40, 55, 62, 72, 65]
  t = tallest(fam)
  s = smallest(fam)
  print("The tallest is ", t)
  print("The smallest is ", s)

def tallest(l):
  m = l[0]
  for h in l:
    if h > m:
      m = h
  return m

def smallest(l):
    m = l[0]
    for h in l:
        if h < m:
            m = h
    return m

main()
