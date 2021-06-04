from code.classes import protein, molecule


#here you choose what protein you want to have made

if __name__ == "__main__":
    # promt user for sequence
    data = str(input("Insert sequence here: "))
    


    # initialize protein class
    Example = protein.Protein(data)

    # TEST: print each nucleotide and details
    for molecule in Example.molecules:
        print(f"nucleotide: {molecule.nucleotide}, molecule number: {molecule.molecule_number}, fold: {molecule.next_fold}, location: {molecule.location}")
    


