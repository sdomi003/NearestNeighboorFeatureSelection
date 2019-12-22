<h2>Introduction</h2>

I figured out how to determine the best features to use in a Nearest
Neighboor algorithm implementation.
I implemented 3 algorithms for narrowing down the best features to use out of a set of up to 100 features, assuming
no expert knowledge or intuition available on the data.
1. Forward Selection
2. Backwards Elemination
3. Sam's Algorithm

<h2>Forward Selection</h2>

Forward Selection starts off with no features and gradually adds features. It's a greedy approach, meaning
that at each iteration, forward search runs with the best looking answer so far. Forward search allows me
to identify promising features early without having to run an algorithm to check all the features. Thus, it's
an efficient way of identifying features that are significant early.

<h2>Backward Elimination</h2>

The intuintion behind backwards elimination is that not all features make any significant difference. I start
with all the features, and then pick one off at a time using the accuracy function.

<h2>Sam's Algorithm</h2>

Nearest Neighboor is sensitive to outleirs and can be overfit. Therefore, to determine which features are
actually significant, I run the algorithms on the same slightly altered dataset.

I start by taking the original dataset and creating 5 datasets out of it. I do this by randomly getting rid of
5% of the elements from the original dataset.
Then, I run the Forward Selection algorithm on all 5 datasets.
I am left with 5 sets of features and accuracies. I take the most common features among all datasets and
consider them the strongest features.
This algorithm improves accuracy because I am more likely to weed out lucky features. If a feature
consistently appears across the datasets, then it is more likely to be a strong feature.

<h2>Setup: Data Ingestion and Normalization</h2>

To begin, my python scripts ingest the .txt files containing floats. Afterwards, I normalize the data such
that all features are distributed amond their mean. To do this, I replace every element with:
new = (old - average)/standard_deviation
After the data is ingested and normalized the data is sent to its appropriate python script to execute one of
the three algorithms.

<h2>Graphing</h2>

I used matplotlib to plot (depth vs accuracy) for my algorithms.
Each accuracy plot should be interpreted as the MAX accuracy for that depth.

<h2>The Data</h2>

I was tasked with working on SMALL DATA #96 and LARGE DATA #98.
The smaller data is about 300 entries of 10 features each.

The larger data is much larger, coming in at 100 features.

<h2>Forward Search Results</h2>

<h3>Small Dataset #96</h3>

Pictured: x-axis is the number of features and y-axis is the max accuracy at
that depth
The small data set #96 resolved quickly. The feature set with the highest accuracy is {7,3}. Its accuracy is
95.6666..%.
It's worth noting that feature 8 is also a good match. It's hard to know though, since we'd have to run the
multi-dataset analysis to find out if 8 is significant enough.

<h3>Large Dataset #98</h3>

Pictured: x-axis is the number of features and y-axis is the max accuracy at
that depth
The best feature set based off of accuracy is {78,30,34}, which has an accuracy of arounf 96.66666...%.
It's hard to know if the next-most-accurate group (which includes feature 29) actaully contains a feature
that is important for generalization.
As said above however, that's what Sam's Algorithm is for.
It is clear that generally, the more features, the worse. On level 100 of this algorithm, I added feature 82
which gave a low accuracy of 0.67.

<h2>Backward Elimination Results</h2>
  
Because backwards elimination beginds by adding and testing all of the features, this algorithm begins as
the most computationally challenging.

<h3>Small Dataset #96</h3>

Pictured: x-axis is the number of features and y-axis is the max accuracy at
that depth

<h3>Large Dataset #98</h3>

The first feature this algorithm chose to omit is 62. Next was 60, followed by 74. Since I wrote my code
with lots of functions and files in python, my code ran quite slow.
Something interesting is that even after 14 deletions from the feature set, each new deletion brought
significant gains.

<h2>Sam's Algorithm Results</h2>

<h3>Small Dataset #96</h3>
  
As expected, for smaller datasets, the results are generally conclusive.
The best solution set is {7,3} for all 5 datasets. This is conclusive evidence that {7,3} is a good feature set for
Small Dataset #96.
The best accuracy reached is 95.6666.

<h3>Large Dataset #98</h3>

For this dataset, {78,30,34} is oncd again favored. However, feature 29 appears consistently enough in each
result across datasets such that I believe it is a weaker but valid feature which can add generality.

<h2>Did It Work?</h2>

Yes, my algorithm choice helped me understand that some important features may not strinctly increase
accuracy. For example, in the above large dataset, feature 29 brings down the average accuracy, and yet it
is consistent as a feature.

<h2>What I'd Improve Upon</h2>

I would like to make my algorithms run faster by adding in pruning. I also want to see if I can mash
together Forward Selection and Backward Elimination. Imagine this:
eliminate a feature using backward elimination

run forward search WITHOUT the eliminated feature
run backward elimination WITHOUT the chosen node from forward search
repeat
Although the answer may not be complete, it may be a heuristic attempt at getting a not-terrible solution
quickly.

<h2>Implementation</h2>

I used python and matplotlib. I created a file for each type algorithm. My main python script gets user
input and calls the appropriate python files.

<h3>Some Output Samples</h3>

<h4>Prompt/Greeting</h4>

Welcome to Sam's Feature Selection Algorithm.
Type in the path of the file to test: some_input.txt
Enter the number for the algorithm you would like to run.
1) Forward Selection
2) Backward Elimination
3) Sam's Algorithm

Small Dataset Forward Search

On level 8 I added feature 9 which gave an accuracy of 0.7933333333333333

On search-tree level number 9

Considering feature number 1

Considering feature number 5

On level 9 I added feature 5 which gave an accuracy of 0.7866666666666666

On search-tree level number 10

Considering feature number 1

On level 10 I added feature 1 which gave an accuracy of 0.7866666666666666

A plot of accuracy over number of features is being made and saved.

Finished search!! The best feature subset is {7,3} which has an accuracy of 95.66666666666667%


<h4>Small Dataset Sam's Algorithm</h4>

.... ....

On level 8 I added feature 9 which gave an accuracy of 0.7933333333333333

On search-tree level number 9

Considering feature number 1

Considering feature number 5

On level 9 I added feature 5 which gave an accuracy of 0.7866666666666666

On search-tree level number 10

Considering feature number 1

On level 10 I added feature 1 which gave an accuracy of 0.7866666666666666

7 is seen 100.0 percent of time.

3 is seen 100.0 percent of time.

[7, 3]

[7, 3]

[7, 3]

[7, 3]

[7, 3]

Finished search!! The best feature subset is {7,3} which has an accuracy of 95.66666666666667%
