#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Anubhav Kundu 
# MSc.IT
# Lovely Professional University ,jalandhar 
# Passing out year -2023
# Phone number- 77206005591
# email id:- 1anubhavkundu@gmail.com
def gprice (pd):
    if (pd[0]>=500):
        pd[0]=pd[0]*0.95
    return (pd[0]*pd[1]*pd[2])/100

lt= [1100,18,1]
um= [900,12,2]
ci= [200,28,3]
hn= [100,0,4]
#discount if unit prce is more than 500
#gst lt = gst (lt)
#gst um = gst (um)
#gst ci= gst (ci)
#gst_hn = gst (hn)
prc_lt = gprice(lt) + lt[0]*lt[2]
prc_um = gprice(um) + um[0]*um[2]
prc_ci = gprice(ci) + ci[0]*ci[2] 
prc_hn = gprice(hn) + hn[0]*hn[2]
total_price = prc_lt + prc_um + prc_ci + prc_hn
print(total_price)


# In[ ]:




