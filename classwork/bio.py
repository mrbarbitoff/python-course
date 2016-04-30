#!/usr/bin/env python3


# Importing entrez from biopython
from Bio import Entrez as e
e.email = 'barbitoff@bk.ru'

handle = e.einfo()
print(handle.read())

# Doing things like a week ago
query = 'Mycoplasma genitalium[Orgn] AND GSE[Entry Type]'
handle = e.esearch(db='gds', term=query, retmax=10000)
mg_gds = e.read(handle)
mg_ids = mg_gds["IdList"]

for this_id in mg_ids:
    handle = e.esummary(db="gds", id=this_id)
    mg_data = e.read(handle)[0]
    print('\t'.join([mg_data["title"], mg_data["Accession"]]))

# More accurately it can be done with Entrez.epost()
handle = e.epost(db='gds', id=','.join(mg_ids))
ret_data = e.read(handle)
qkey = ret_data["QueryKey"]
webenv = ret_data["WebEnv"]
print(qkey)
print(webenv)

handle = e.esummary(db='gds', webenv=webenv, query_key=qkey)
fancy_data = e.read(handle)

# Taking all gene symbols from expression dataset
with open('/home/barbitoff/Downloads/sc_rnaseq.tsv', 'r') as ifile:
    with open('output.tsv', 'w') as ofile:
        for line in ifile:
            if 'Sample' in line:
                ofile.write('EID\tGenename\t' + line.strip() + '\n')
                continue
            data = line.strip().split('\t')
            eid = data[0]
            handle = e.esummary(db='gene', id=eid)
            gene_data = e.read(handle)['DocumentSummarySet']['DocumentSummary'][0]['NomenclatureSymbol']
            ofile.write(data[0] + '\t' + gene_data + '\t' + '\t'.join(data[1:]) + '\n')
