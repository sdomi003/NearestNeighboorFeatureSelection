'''
input
data - the data
N - number of data points
features - list of features to run NN on
new_feature - the newest feature to add to the test

ouput
an decimal value representing accuracy after adding this new feature
'''
import LoadData 
import copy
import math
def Accuracy(data, N, features, new_feature):
	features = copy.deepcopy(features)
	features.append(new_feature)
	num_correct = 0
	for i in range(N):
		best = float("inf")
		best_location = None
		for j in range(N):
			if (i != j):
				distance = 0
				for f in features:
					distance += (data[i][f] - data[j][f])**2
				distance = math.sqrt(distance)
				if (distance < best):
					best = distance
					best_location = j
		if (data[i][0] == data[best_location][0]):
			#print("Node ", i, "'s NN is " ,best_location , " and they are the same class.")
			num_correct += 1
	return num_correct / N




