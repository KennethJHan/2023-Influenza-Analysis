from Bio import Entrez


def download_amino_acid_sequence(accession_id: str):
    Entrez.email = "your@email.mail"
    handle = Entrez.efetch(
        db="protein", id=accession_id, rettype="fasta", retmode="text"
    )
    record = handle.read()
    handle.close()
    return record


def main():
    accession_id_list = ["YP_308875.1", "YP_529486.1", "YP_009121768.1", "YP_163735.1"]
    for accession_id in accession_id_list:
        record = download_amino_acid_sequence(accession_id)
        print(record)


if __name__ == "__main__":
    main()
