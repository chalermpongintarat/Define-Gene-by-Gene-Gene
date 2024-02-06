with open("description_accession_number.txt", "r") as file: 
    description_accession_number = file.read().split("\n")

with open("gene_gene.txt", "r") as file: 
    gene_gene = file.read().split("\n")

accession_genes = []
for gene in gene_gene:
    gene = gene.split("\t")
    accession_genes.append(gene)

define_genes = []
for accession in description_accession_number:
    genes = []
    for gene in accession_genes:
        if gene[0] == accession:
            genes.append(gene[1])
    define_genes.append(genes)

f = open("define_gene_list.txt", "w")
for gene in define_genes:
    define_gene = ', '.join(map(str, gene))
    f.write(str(define_gene))
    f.write("\n")
f.close()