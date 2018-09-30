import numpy as np
import insti
import matplotlib.pyplot as plt

inst_list = insti.get_institutions_list()
counter = np.load('institution_counter.npy')




good_counter = []
good_inst = []
for n,inst in enumerate(inst_list):
    if inst == 'DeepMind':
        good_counter[good_inst.index('Google')] += counter[n]
        pass
    elif inst == 'Beijing':
        good_counter[good_inst.index('Peking')] += counter[n]
        pass     
    else:
        good_inst += [inst]
        good_counter += [counter[n]]


counter = good_counter
inst_list = insti.get_institutions_complete_name()
indeces = np.argsort(counter)
nb_inst = len(inst_list)


sorted_inst = []
sorted_counter = []
nb_inst_good = 0
for i in range(0,nb_inst):
    print(inst_list[indeces[i]]+': '+str(counter[indeces[i]]))
    if counter[indeces[i]] >= 15:
        sorted_inst += [inst_list[indeces[i]]]
        sorted_counter += [counter[indeces[i]]]
        nb_inst_good += 1



plt.bar(np.arange(0,nb_inst_good),sorted_counter)
plt.xticks(np.arange(0,nb_inst_good),sorted_inst,rotation=45,ha='right')
plt.ylabel('Number of papers')
plt.tight_layout()
plt.show()