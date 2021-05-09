
BASE = 2
for i in range(2**3):
  weight = []
  for j in xrange(3):
    weight.append(i%(BASE))
    i /= BASE
  weight.reverse()
  print weight