#!/usr/bin/env python

from jinja2 import Template
import pandas as pd
from subprocess import call

def main():
    with open('template.tex') as f:
        template = f.read()
    env = Template(template)

    with open('papers.txt') as f:
        papers = f.read().split('\n')

    df = pd.read_csv('co-authors.txt', sep=',', header=0)

    for _, row in df.iterrows():

        co_authored = []
        for paper in papers:
            # this is not going to work for repeated last names
            if row.last_name in paper:
                co_authored.append(paper)

        if len(co_authored) == 0:
            raise ValueError('Could not find a paper for %s %s. There may be a'
                             ' typo or you might not have any publications '
                             ' with this author.'%
                             (row.first_name, row.last_name))

        filename = row.email.replace('@', 'AT')
        with open(filename + '.tex', 'w') as f:
            data = env.render(first_name=row.first_name,
                              last_name=row.last_name, papers=co_authored)
            f.write(data)
        call(["pdflatex", filename])

if __name__ == '__main__':
    main()
