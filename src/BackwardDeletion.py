import LoadData
import Accuracy

def backwardDeletion(data):
	answer_set = []
	answer_accuracy = 0
	N = len(data)
	M = len(data[0])
	# start with all of the features
	features = list(range(1,M))	
	for count in range(1, M):
		best_accuracy = 0
		feature_to_omit = -1
		for i in range(len(features)):
			# take out i'th feature
			temp = []
			if (i < len(features) - 1):
				temp = features[:i] + features[i+1:]		
			else:
				temp = features[:-1]
			temp_accuracy = Accuracy.Accuracy(data, N, temp, None)
			if (temp_accuracy > best_accuracy):
				best_accuracy = temp_accuracy
				feature_to_omit = i
		print("Omitting feature", features[feature_to_omit])
		if (feature_to_omit < len(features) - 1):
			features = features[:feature_to_omit] + features[feature_to_omit+1:]
		else:
			features = features[:-1]	
		print("This leaves us with", features, "and an accuracy of ", best_accuracy)
		if (best_accuracy > answer_accuracy):
			answer_accuracy = best_accuracy
			answer_set = features
	return answer_set, answer_accuracy
'''
# just to test
data = LoadData.loadData("../data/CS170_SMALLtestdata__80.txt")
LoadData.normalizeData(data)
N = len(data)
backwardDeletion(data)
'''