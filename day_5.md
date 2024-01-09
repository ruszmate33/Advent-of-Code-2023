# Possible strategies
- create the union of all ranges
`set(range(3)).union(set(range(7, 10)))`
{0, 1, 2, 7, 8, 9}

- I could check the lowest number from this set


```py
from functools import reduce

def get_union(*ranges):
    return reduce(lambda x, y: set(x).union(set(y)), ranges)

range1 = range(1, 10)
range2 = range(8, 20)
range3 = range(15, 25)

result = get_union(range1, range2, range3)
print(f"The union of {len(result)} elements is {result}")
```