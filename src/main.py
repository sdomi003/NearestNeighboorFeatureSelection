import matplotlib.pyplot as plt
import ForwardSelection
import BackwardDeletion
import SamSelection
import LoadData 
def formatFeatures(features):
	formatted = "{"
	for f in range(len(features) - 1):
		formatted += str(features[f]) + ","
	formatted += str(features[len(features) - 1])
	formatted += "}"
	return formatted
def userPrompt():
	print("Welcome to Sam's Feature Selection Algorithm.")
	file_loc = input("Type in the path of the file to test: ")
	algorithm_choice = int(input("Enter the number for the algorithm you would like to run.\n	1) Forward Selection\n	2) Backward Elimination\n	3) Sam's Algorithm\n\n"))
	return file_loc, algorithm_choice

def plot(accuracy_at_level):
	fig = plt.figure()
	l = list(range(1,len(accuracy_at_level) + 1))
	plt.plot(l, accuracy_at_level, 'go')	
	plt.savefig('/Users/samueldominguez/Downloads/2dplt.png')

if __name__ == "__main__":
	file_loc, algorithm_choice = userPrompt()
	data = LoadData.loadData(file_loc)
	LoadData.normalizeData(data)
	N = len(data)
	M = len(data[0])
	print("There are " + str(N) + " datapoints with " + str(M) + " features.")
	print("Data has been normalized...")
	algos = ["Forward Selection","Backward Elemination","Sam's Algorithm"]
	print("Running Nearest Neighboor with " + algos[algorithm_choice - 1] + " on the dataset.\n")
	accuracy_at_level = []	
	features = []
	accuracy = -1
	if (algorithm_choice == 1):
		# forward
		features, accuracy, accuracy_at_level = ForwardSelection.forwardSelection(data)
		print("A plot of accuracy over number of features is being made and saved.")
		plot(accuracy_at_level)
	elif (algorithm_choice == 2):
		# backwards
		features, accuracy, accuracy_at_level = BackwardDeletion.backwardDeletion(data)
		print("A plot of accuracy over number of features is being made and saved.")
		plot(accuracy_at_level)
	else:
		# sam's
		features, accuracy = SamSelection.samSelection(data);
	formatted_features = formatFeatures(features)
	print("Finished search!! The best feature subset is " + formatted_features +  " which has an accuracy of " + str(accuracy*100) + "%")
