from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
m ="Mensaje de broadcast para todes"
d = comm.bcast(m,root=0)
print d
if r != 0:
   s = comm.recv()
   print "Mensaje de %d: %s" % (r, s)
   
    

	