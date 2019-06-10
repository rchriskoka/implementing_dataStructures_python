#Implementing use of pop and analyzing running time.
import timeit
from timeit import Timer

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(2000))
print popzero.timeit(number=1000)

x = list(range(2000))
print popend.timeit(number=1000)
