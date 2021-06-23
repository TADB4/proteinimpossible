# Protein Impossible
Programmingtheorie project for team protein impossible in which we aim to find a near-optimal solution for the "Protein pow(d)er case.

The goal of this case is to built certain protein's in such a manner that the protein is as stable as possible. In this case proteins are built out of polaire aminoacids (P), hydrofobe aminoacids(H) and extreme hydrofobe aminoacids called Cysteine(C). Stability can be achieved by having two H's, two C's or an H with a C being each other's neighbour while not being bound. When this happens hydrogen bridges are formed which causes the protein to become more stable. A H-H hydrogen brigde causes the protein to become more stable with the value of -1, the same goes for C-H neigboring. But when two C's neighbour it causes the protein to become more stable with the value of -5. Therefore, our program builds proteins and tries to find the proteins in which the stability value is the lowest which means that the most hydrogen bridges were formed. To find the protein configuration with the highest stability, we implemented several algorithms. 

## Get started

### Requirements

This code is written in Python 3.7. To succesfully run the code, matplotlib needs to be installed. This can be achieved via pip by running the following command: 

```
python -m pip install -U matplotlib
```

### Usage

An example of the output can be created by running:

```
python main.py or python3 main.py
```
Next, the user will be asked for the protein sequence. You can type the order of aminoacids of your choice, e.g. 'HHPHHHPHPHHHPH' and press enter. Mind that you only use the aminoacids H, P or C and write them in uppercase. 

Consequently, the user will be asked for an algorithm. Type 'randomise', 'greedy', 'breadthfirst', 'breadthfirst_pruning', 'depthfirst' or 'depthfirst_pruning' and press enter. Note that you write them in lowercase and with no witespace. 

If your algorithm is 'randomise' or 'greedy', you will also be asked for the amount of times that you want to run the algorithm. Enter a number, like '10'. The output result will be the protein configuration with the best stability out of the 10 times the algorithm has run. If your algorithm is 'breadthfirst', 'breadthfist_pruning', 'depthfirst' or 'depthfirst_pruning', the algorithm will run as long as needed to find the best solution, so you will not be asked for an amount of times.

You can find the output files in the folder 'results'. The file 'all_scores.csv' contains a list of the stability of all protein configurations of the last run. The file 'output.csv' contains a summary of the protein with the best stability (i.e. the folding per aminoacid and the final stability score). The file 'bestprotein.png' contains a representation picture of the protein with the best stability. 


### Structure
The following list describes the most important maps and files in this project, and where to find them:

- **/code**: contains the code for this project
  - **/code/algorithms**: contains the code for the algorithms 
  - **/code/classes**: contains the two necesairy classes for this case
  - **/code/visualisation**: contains the matplotlib code for the visualisation
- **/data**: contains the nucloetide order of the different proteins which can be built and visualised
- **/doc**: contains a visual representation of the used datastructure
- **/results**: here the output.csvs and png's wil put when running the program

## Authors
- Tim de Boer
- Nick Tennekes
- Sofie Peeters
