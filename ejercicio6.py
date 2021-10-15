
from mpi4py import MPI
comm = MPI.COMM_WORLD

r = comm.Get_rank()

def mulChunk(fromA, toB):
   sum = 1
   for i in range(fromA, toB+1):
      sum = sum * i
   return sum
NODES = 2
if r == 0:
   comm.send((6, 10), dest = 1)
   suma = mulChunk(1, 5)
   suma2 = comm.recv()
   print "el factorial de 10 es: "
   print suma * suma2   
elif r == 1:
   s = comm.recv()
   sum = mulChunk(s[0], s[1])
   comm.send(sum, dest = 0)
   
    

	