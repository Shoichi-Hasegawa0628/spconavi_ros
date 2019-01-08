#c-od-i-n-:-ut-f---8
#!/usr/bin/env python

import sys
import string
#from sklearn.metrics.cluster import adjusted_rand_score
#import matplotlib.pyplot as plt
import numpy as np
#import math
from __init__ import *

trialname = raw_input("data_name?(**_NUM) > ")
data_num1 = raw_input("data_start_num?(DATA_**) > ")
data_num2 = raw_input("data_end_num?(DATA_**) > ")
N = int(data_num2) - int(data_num1) +1
#filename = raw_input("Read_Ct_filename?(.csv) >")"001" #"010" #
S = int(data_num1)

step = 50

#MI_M = [[] for c in xrange(N)]
#ARI_M = [[] for c in xrange(N)]  
#PARs_M = [[] for c in xrange(N)]
#PARw_M = [[] for c in xrange(N)]
PRR_M = [[] for c in xrange(N)]
#MM = [ np.array([[] for m in xrange(10) ]) for n in xrange(N)]
#MM_M = 

fp = open(datafolder + '/Evaluation/' + trialname + '_' + data_num1 + '_' + data_num2 + '_EvaluationPRR2.csv', 'w')
#fp.write('MI,ARI,PARs,PARw\n')
fp.write('PRR\n')

i = 0
#MI_MAX = [[0,0]]
#ARI_MAX = [[0,0]]
#PARs_MAX = [[0,0]]
#PARw_MAX = [[0,0]]
PRR_MAX = [[0,0]]

for s in range(N):
  i = 0
  for line in open(datafolder + trialname + str(s+1).zfill(3) + '/' + trialname + str(s+1).zfill(3) +'_EvaluationPRR2.csv', 'r'):
    itemList = line[:-1].split(',')
    if (i != 0) and (itemList[0] != '') and (i <= step):
      #print i,itemList
      #MI_M[s] = MI_M[s] + [float(itemList[0])]
      #ARI_M[s] = ARI_M[s] + [float(itemList[1])]
      #PARs_M[s] = PARs_M[s] + [float(itemList[2])]
      #PARw_M[s] = PARw_M[s] + [float(itemList[3])]
      PRR_M[s] = PRR_M[s] + [float(itemList[0])]
      #if (float(itemList[0]) > MI_MAX[0][1]):
      #    MI_MAX = [[s+1,float(itemList[0])]] + MI_MAX
      #if (float(itemList[1]) > ARI_MAX[0][1]):
      #    ARI_MAX = [[s+1,float(itemList[1])]] + ARI_MAX
      #if (float(itemList[3]) > PARw_MAX[0][1]):
      #    PARw_MAX = [[s+1,float(itemList[3])]] + PARw_MAX
    i = i + 1
    #print MI_M[s]
    #for i in xrange(len(itemList)):
    #   if itemList[i] != '':
         
    #MM[s] = MM[s] + [[float(itemList[0]),float(itemList[1]),float(itemList[2]),float(itemList[3])]]
    #ARI = adjusted_rand_score(CtC, Ct)
    #print str(ARI)
    #ARI_M = ARI_M + ARI
  #MI_M[s] = np.array(MI_M[s])
  #ARI_M[s] = np.array(ARI_M[s])
  #PARs_M[s] = np.array(PARs_M[s])
  #PARw_M[s] = np.array(PARw_M[s])
  PRR_M[s] = np.array(PRR_M[s])
  #if (MI_M[s][-1] > MI_MAX[0][1]):
  #        MI_MAX = [[s+1,MI_M[s][-1]]] + MI_MAX
  #if (ARI_M[s][-1] > ARI_MAX[0][1]):
  #        ARI_MAX = [[s+1,ARI_M[s][-1]]] + ARI_MAX
  #if (PARw_M[s][-1] > PARw_MAX[0][1]):
  #        PARw_MAX = [[s+1,PARw_M[s][-1]]] + PARw_MAX
  #if (PARs_M[s][-1] > PARs_MAX[0][1]):
  #        PARs_MAX = [[s+1,PARs_M[s][-1]]] + PARs_MAX
  #if (PRR_M[s][-1] > PRR_MAX[0][1]):
  #        PRR_MAX = [[s+1,PRR_M[s][-1]]] + PRR_MAX
          
#print "MI_MAX:",MI_MAX
#print "ARI_MAX:",ARI_MAX
#print "PARw_MAX:",PARw_MAX
#print "PARs_MAX:",PARs_MAX
#print " PRR_MAX:", PRR_MAX
#print MI_M
#MM_M = sum(MM)/N
#MI_MM = sum(MI_M)/N
#ARI_MM = sum(ARI_M)/N
#PARw_MM = sum(PARw_M)/N
#PARs_MM = sum(PARs_M)/N
PRR_MM = sum(PRR_M)/N
#print MI_MM
#MI,ARI,PARs,PARw,

for iteration in xrange(len( PRR_MM)):
  fp.write( str( PRR_MM[iteration]) ) #str(MI_MM[iteration])+','+ str(ARI_MM[iteration])+','+ str(PARs_MM[iteration])+','+str(PARw_MM[iteration]) )
  fp.write('\n')
fp.write('\n')

#for iteration in xrange(10):
#  MI_MS = np.array([MI_M[s][iteration] for s in xrange(N)])
#  MI_std = np.std(MI_MS, ddof=1)
#  #print MI_std

for iteration in xrange(len( PRR_MM)):
  #MI_MS = np.array([MI_M[s][iteration] for s in xrange(N)])
  #ARI_MS = np.array([ARI_M[s][iteration] for s in xrange(N)])
  #PARs_MS = np.array([PARs_M[s][iteration] for s in xrange(N)])
  #PARw_MS = np.array([PARw_M[s][iteration] for s in xrange(N)])
  PRR_MS = np.array([ PRR_M[s][iteration] for s in xrange(N)])
  #print iteration,np.std(MI_MS, ddof=1)
  fp.write( str(np.std( PRR_MS, ddof=1)) ) #str(np.std(MI_MS, ddof=1))+','+ str(np.std(ARI_MS, ddof=1))+','+ str(np.std(PARs_MS, ddof=1))+','+str(np.std(PARw_MS, ddof=1)) )
  fp.write('\n')
#np.std
#float(ARI_M / N)
#print "ARI mean"
#print str(ARI_M)
print "close."
  
fp.close()
