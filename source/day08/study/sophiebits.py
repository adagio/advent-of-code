import collections
import re

with open('data/input1.plain') as f:
  lines = [l.rstrip('\n') for l in f]
  lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

  nums = lines[0]
  all_meta = []

  # def read(i):
  #   children = nums[i]
  #   meta = nums[i + 1]
  #   i += 2
  #   for j in xrange(children):
  #     i = read(i)
  #   for j in xrange(meta):
  #     all_meta.append(nums[i + j])
  #   return i + meta
  #
  # read(0)
  # print sum(all_meta)

  def read(i):
    children = nums[i]
    meta = nums[i + 1]
    i += 2
    vals = {}
    for j in xrange(children):
      (i, val) = read(i)
      vals[j + 1] = val
    local_meta = []
    for j in xrange(meta):
      local_meta.append(nums[i + j])
      all_meta.append(nums[i + j])
    i += meta
    if children:
      return (i, sum(vals.get(m, 0) for m in local_meta))
    else:
      return (i, sum(local_meta))
  
  (i, tval) = read(0)
  print sum(all_meta)
  print tval

