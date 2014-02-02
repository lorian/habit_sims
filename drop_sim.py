# Simulates time to collect all pets and all mounts.
#Running 1000 simulations:
#Collecting all pets took an average of 101.3812 +/- 13.4512553689 days
#Collecting all mounts took an average of 477.7754 +/- 28.1716055453 days

import random
import collections
import numpy

#drop chance is currently 4:3:3 food:eggs:potions
# 9 different eggs (need 10 of each), 10 different potions (need 9 of each), 10 different foods (need 90 of each)
# drop 1-9 is egg, 10-19 is potion, 20-29 is food
all_drops = []
print "Running 1000 simulations:"

for i in xrange(0,1000):
	inv = collections.Counter({k:0 for k in xrange(1,30)})
	drops = 0
	while (inv[1] < 10) or (inv[2] < 10) or (inv[3] < 10) or (inv[4] < 10) or (inv[5] < 10) or (inv[6] < 10) or (inv[7] < 10) or (inv[8] < 10) or (inv[9] < 10) or (inv[10] < 9) or (inv[11] < 9) or (inv[12] < 9) or (inv[13] < 9) or (inv[14] < 9) or (inv[15] < 9) or (inv[16] < 9) or (inv[17] < 9) or (inv[18] < 9) or (inv[19] < 9):
		type = random.randint(1,10)
		if type <= 3: # egg
			drop = random.randint(1,9)
		elif type <= 6: # potion
			drop = random.randint(10,19)
		else:  # food
			drop = random.randint(20,29)
		inv.update([drop])
		drops = drops +1
	all_drops.append(drops)

print "Collecting all pets took an average of {0} +/- {1} days".format(numpy.mean(numpy.array(all_drops))/5,numpy.std(numpy.array(all_drops)/5))

all_drops = []
for i in xrange(0,1000):
	inv = collections.Counter({k:0 for k in xrange(1,30)})
	drops = 0
	while (inv[20] < 81) or (inv[21] < 81) or (inv[22] < 81) or (inv[23] < 81) or (inv[24] < 81) or (inv[25] < 81) or (inv[26] < 81) or (inv[27] < 81) or (inv[28] < 81) or (inv[29] < 81):
		type = random.randint(1,10)
		if type <= 3: # egg
			drop = random.randint(1,9)
		elif type <= 6:  # potion
			drop = random.randint(10,19)
		else:  # food
			drop = random.randint(20,29)
		inv.update([drop])
		drops = drops +1
	all_drops.append(drops)

print "Collecting all mounts took an average of {0} +/- {1} days".format(numpy.mean(numpy.array(all_drops))/5,numpy.std(numpy.array(all_drops)/5))
