from code.classes import protein, molecule


#here you choose what protein you want to have made

if __name__ == "__main__":

    data = str(input("Insert sequence here: "))

    Example = protein.Protein(data)

    for molecule in Example.molecules:
        print(f"{molecule.nucleotide}, {molecule.molecule_number}")
    


