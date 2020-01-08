import itertools
import random

#I created a generator function utilizing lists to identify each possible solution to the n-queens problem, for any n (includes non-distinct solutions from rotations).
def solve(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a

#To obtain different results each time, I simply defined a random index value, and issued a print command to the output of the generator function at that index
index = random.randint(1, 10000) #39,029,188,884 = total number of solutions to the n-queens problem at n=20
#index set to the range 10000 due to excessive runtime for generator to iterate to the millionth index, for example
print(next(itertools.islice(solve(20, 0, [], [], []), index, None)))
