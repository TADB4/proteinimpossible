# Protein Impossible
Programmingtheorie project for team protein impossible in which we aim to find a near-optimal solution for the "Protein pow(d)er case.

The goal of this case is to built certain protein's in such a manner that the protein is as stable as possible. In this case proteins are built out of polaire nucleotides(P), hydrofobe nucleutides(H) and extreme hydrofobe nucleotides called Cysteine(C). Stability can be achieved by having two hydrofobe nucleotides or two Cysteine nucleotides being each other's neighbour while not being bound. When this happens hydrogen bridges are formed which causes the protein to become more stable. When hydrofobe nucleotides neighbour this causes the protein to become more stable with the value of -1, the same goes for Cysteine and a hydrofobe nucleotide neigboring. But when two Cysteine nucleotides neighbour it causes the protein to become more stable with the value of -5. Therefore, our program builds proteins and tries to find the proteins in which the stability value is the lowest which means that the most hydrogen bridges were formed.

## Get started

### Requirements

This code is written in Python 3.7. To succesfully run the code, matplotlib needs to be installed. This can be achieved via pip by running the following command: 

```
python -m pip install -U matplotlib
```

### Usage

An example of the output can be created by running:

```
python main.py
```

### Structure
The following list describes the most important maps and files in this project, and where to find them:

- **/code**: contains the code for this project
  - **/code/algorithms**: contains the code for the algorithms 
  - **/code/classes**: contains the two necesairy classes for this case
  - **/code/visualisation**: contains the matplotlib code for the visualisation
- **/data**: contains the nucloetide order of the different proteins which can be built and visualised
- **/doc**: contains a visual representation of the used datastructure

## Autors
- Tim de Boer
- Nick Tennekes
- Sofie Peeters
