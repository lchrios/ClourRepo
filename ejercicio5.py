
from mpi4py import MPI
comm = MPI.COMM_WORLD

r = comm.Get_rank()

def mulChunk(fromA, toB):
   sum = 0
   for i in range(fromA, toB+1):
      sum = sum + i
   return sum
NODES = 2
if r == 0:
   comm.send((51, 100), dest = 1)
   suma = mulChunk(1, 50)
   suma2 = comm.recv()
   print "la suma es: "
   print suma + suma2   
elif r == 1:
   s = comm.recv()
   sum = mulChunk(s[0], s[1])
   comm.send(sum, dest = 0)
   
    

	