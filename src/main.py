import ForwardSelection
import BackwardDeletion
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
	
	features = []
	accuracy = -1
	if (algorithm_choice == 1):
		# forward
		features, accuracy = ForwardSelection.forwardSelection(data)
	elif (algorithm_choice == 2):
		# backwards
		features, accuracy = BackwardDeletion.backwardDeletion(data)
	else:
		# sam's
		print("TODO: Sam's algo.")
	formatted_features = formatFeatures(features)
	print("Finished search!! The best feature subset is " + formatted_features +  " which has an accuracy of " + str(accuracy*100) + "%")
