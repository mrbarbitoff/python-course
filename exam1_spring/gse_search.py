#!/usr/bin/env python3

import argparse
from Bio import Entrez as e

e.email = 'barbitoff@bk.ru'

parser = argparse.ArgumentParser(description='Collect info about GSEs associated with the provided search term in NCBI GDS')

parser.add_argument("query",
                    type=str,
                    help='Query string for NCBI GDS')

parser.add_argument("taxon",
                    type=str,
                    default='',
                    nargs='?',
                    help='Taxon to search for (default: All)')

args = parser.parse_args()

formatted_taxon = '' if args.taxon == '' else args.taxon + '[Organism]'
formatted_query = '%s AND GSE[Entry Type]%s' % (args.query, formatted_taxon)
result = e.read(e.esearch(db='gds', term=formatted_query, retmax=1000000))

ids = result['IdList']
for this_id in ids:
    gse = e.read(e.esummary(db='gds', id=this_id))[0]
    out_str = '%s\t%s\t%s' % (gse['Accession'], gse['taxon'], gse['title'])
    print(out_str)


