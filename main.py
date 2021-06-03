from code.classes import protein, molecule


#here you choose what protein you want to have made

if __name__ == "__main__":

    data = str(input("Insert sequence here: "))

    Example = protein.Protein(data)

    for molecule in Example.molecules:
        print(f"nucleotide: {molecule.nucleotide}, molecule number: {molecule.molecule_number}, fold: {molecule.fold}, location: {molecule.location}")
    


