from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
if r == 1:
   m = 4
   comm.send(m, dest=0)
   s = comm.recv(source=0)
   print "Mensaje desde %d: %s" % (r, s)
elif r == 0:
   comm.send(8, dest=1)
   s = comm.recv(source=1)
   print "Mensaje desde %d: %s" % (r, s)