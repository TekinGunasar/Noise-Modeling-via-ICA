import numpy as np

def cn(n,time,y,period = 2* np.pi):
   c = y*np.exp(-1j*2*n*np.pi*time/period)
   return c.sum()/c.size