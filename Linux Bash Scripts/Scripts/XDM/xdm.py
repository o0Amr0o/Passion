#!/usr/bin/env python
# coding: utf-8

# In[62]:


import os
import sys

# In[ ]:


os.system('xdotool search --onlyvisible --name xdm > /mnt/F/Scripts/XDM/visible.txt')
os.system('xdotool search --name xdm > /mnt/F/Scripts/XDM/check.txt')


# In[63]:


path1 = '/mnt/F/Scripts/XDM/visible.txt'
path2 = '/mnt/F/Scripts/XDM/check.txt'
visible = open('/mnt/F/Scripts/XDM/visible.txt', 'r')
check = open('/mnt/F/Scripts/XDM/check.txt', 'r')
visr = open('/mnt/F/Scripts/XDM/vis.txt', 'r')
#visw = open('/mnt/F/Scripts/XDM/vis.txt', 'w')


# In[67]:


# visible 1 item


# In[58]:


show = 'xdotool windowmap {}; xdotool windowactivate {}'
hide = 'xdotool windowunmap {}'


# In[18]:


chpid = check.readlines()
print(chpid)

# In[54]:


ch_t = list(map(lambda x: x.split()[0], chpid))
op = True
try:
    vis_t = visible.readlines()[0].split()[0]
except:
	op = False


print(ch_t)



m = visr.readline()
print(m)

visr.close()
print('op = {}'.format(op))
if op:
	print('hide')
	final = hide.format(vis_t)
	visw = open('/mnt/F/Scripts/XDM/vis.txt', 'w')
	visw.write(vis_t)
elif m:
	if m in ch_t:
		print('match')
		final = show.format(m,m)
else:
	sys.exit()
        
        
print(final)
os.system(final)
        



