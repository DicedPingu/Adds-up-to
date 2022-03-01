from itertools import combinations, product


def upto(wanted_sum, cells, num_list = False, must_include = False):
  if not num_list:
    num_list = list(range(1, 10))
  if not must_include:
    must_include = []
  
  
  combs = combinations(num_list, cells)
  matches = []
  for c in combs:
    includes = 0
    for n in c:
      if n in must_include:
        includes += 1
    
    if sum(c) == wanted_sum and includes == len(must_include):
      print(c, '=', sum(c))
      matches.append(c)
      
  if not matches:
    print('No matches for', wanted_sum)
  return matches

def multito(wanted_sums, cells, num_list = False):
  sums = []
  lens = []
  for i in range(len(wanted_sums)):
    s = wanted_sums[i]
    c = cells[i]
    u = upto(s, c, num_list)
    sums[i] = u
    lens.append(len(wanted_sums))
    
  if not num_list:
    num_list = range(1, 10)
  
  iters = product(lens)
  for n in range(iters):
    comb = []
    #for k in sums:
      
    
  
  
  
  

# upto(36, 7)
# upto(16, 4, False, [2])

want = 16
nums = 3
choices = range(want,nums)

upto(17, 3, [1,4,5,7,8])
# pto(want, nums, choices)
# upto(17,3,choices)
# multito([16, 22], [3, 3], [3,5,6,7,8,9])
#multito([7,8,11,19], [2,2,2,3], [1,2,3,4,5,6,7,8,9])
