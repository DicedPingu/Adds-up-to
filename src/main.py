from itertools import combinations, product


def upto(wanted_sum, cells, num_list=range(1, 10), display_results=False):
  if not num_list:
    num_list = list(range(1, 10))

  combs = combinations(num_list, cells)
  matches = []
  for c in combs:
    if sum(c) == wanted_sum:
      matches.append(c)
      if display_results:
        print(c, '=', sum(c))

  if not matches and display_results:
    print('No matches for', wanted_sum)
  return matches

def multito(wanted_sums, cells, num_list=range(1, 10), display_results=True):
  nums = len(wanted_sums)
  sums = []
  lens = []
  for i in range(nums):
    s = wanted_sums[i]
    c = cells[i]
    u = upto(s, c, num_list)
    sums.append(u)
    lens.append(len(u))

  if not num_list:
    num_list = range(1, 10)

  iters = product(*sums)
  solutions = []
  for i in iters:
    digits = [s for n in i for s in n]
    wants = [n for n in num_list]
    right_sequence = True
    for d in digits:
      if d in wants:
        wants.remove(d)
      else:
        right_sequence = False
        break
    if right_sequence:
      solutions.append(i)

  if display_results:
    # print(f"{len(solutions)} solution{'s'*(len(solutions)!=1)} for {[wanted_sums[n] for n in range(nums)]}{':'*bool(solutions)}")
    print(len(solutions), 'solution' + 's'*(len(solutions)!=1) + ' for', end=' ')
    print(*wanted_sums, end=' (', sep=', ')
    print(*cells, end=')\n', sep=', ')

    for s in solutions:
      for i in range(nums):
        print(f"{wanted_sums[i]} = {s[i]}", end='   ')
      print()
    print()


multito([21, 15, 9], [3, 3, 3])
multito([6, 7], [2, 2])
multito([6, 7], [2, 2], [1, 2, 3, 4, 5])
