import numpy as np
import matplotlib.pyplot as plt
import os

output_dir = os.path.dirname('/lustre/lysun/models/Ocean-LETKF-gyre1-test3/mom4/OUTPUT/EXP2/')
num_days = 105 
temp = np.zeros([num_days,5])
salt = np.zeros([num_days,5])
uvel = np.zeros([num_days,5])
vvel = np.zeros([num_days,5])
da_cycle = np.arange(1,num_days+1,1)

tfile = os.path.join(output_dir,'temp_3d.txt')
sfile = os.path.join(output_dir,'salt_3d.txt')
ufile = os.path.join(output_dir,'uvel_3d.txt')
vfile = os.path.join(output_dir,'vvel_3d.txt')

temp = np.loadtxt(tfile,usecols=range(0,5),skiprows=1)
salt = np.loadtxt(sfile,usecols=range(0,5),skiprows=1)
uvel = np.loadtxt(ufile,usecols=range(0,5),skiprows=1)
vvel = np.loadtxt(vfile,usecols=range(0,5),skiprows=1)

plt.figure(1)
plt.plot(da_cycle,temp[:,0],label='true - forecast',c='b')
plt.plot(da_cycle,temp[:,1],label='true - analysis',c='r')
plt.plot(da_cycle,temp[:,4],label='true - control',c='g')
plt.plot(da_cycle,temp[:,2],label='forecast spread',linestyle='--',c='b')
plt.plot(da_cycle,temp[:,3],label='analysis spread',linestyle='--',c='r')
plt.xlabel('time (days)')
plt.ylabel('RMSE (C)')
plt.yscale('log')
plt.title('Temperature')
plt.legend()
plt.tight_layout()
plt.savefig('RMSE_t.png')

plt.figure(2)
plt.plot(da_cycle,salt[:,0],label='true - forecast',c='b')
plt.plot(da_cycle,salt[:,1],label='true - analysis',c='r')
plt.plot(da_cycle,salt[:,4],label='true - control',c='g')
plt.plot(da_cycle,salt[:,2],label='forecast spread',linestyle='--',c='b')
plt.plot(da_cycle,salt[:,3],label='analysis spread',linestyle='--',c='r')
plt.xlabel('time (days)')
plt.ylabel('RMSE (psu)')
plt.yscale('log')
plt.title('Salinity')
plt.legend()
plt.savefig('RMSE_s.png')

plt.figure(3)
plt.plot(da_cycle,uvel[:,0],label='true - forecast',c='b')
plt.plot(da_cycle,uvel[:,1],label='true - analysis',c='r')
plt.plot(da_cycle,uvel[:,4],label='true - control',c='g')
plt.plot(da_cycle,uvel[:,2],label='forecast spread',linestyle='--',c='b')
plt.plot(da_cycle,uvel[:,3],label='analysis spread',linestyle='--',c='r')
plt.xlabel('time (days)')
plt.ylabel('RMSE (m/s)')
plt.yscale('log')
plt.title('U')
plt.legend()
plt.savefig('RMSE_u.png')

plt.figure(4)
plt.plot(da_cycle,vvel[:,0],label='true - forecast',c='b')
plt.plot(da_cycle,vvel[:,1],label='true - analysis',c='r')
plt.plot(da_cycle,vvel[:,4],label='true - control',c='g')
plt.plot(da_cycle,vvel[:,2],label='forecast spread',linestyle='--',c='b')
plt.plot(da_cycle,vvel[:,3],label='analysis spread',linestyle='--',c='r')
plt.xlabel('time (days)')
plt.ylabel('RMSE (m/s)')
plt.yscale('log')
plt.title('V')
plt.legend()
plt.savefig('RMSE_v.png')

plt.show()

