import os
import sys

from shutil import copyfile
import pandas as pd


def get_tag_from_name(rec):
    tag= f"{rec['first_name'][0]}{rec['last_name']}"
    return(tag.lower())

def make_file(tag,rec, current=False):
    file = open(f'../_members/{tag}.md', 'w+')

    print(file.name)

    if(isinstance(rec['picture'],(float))):
        rec['pic'] = 'alias.jpeg'
    else:
        rec['pic'] = rec['picture']

    if(current):
        file.write(f"---\ntitle: {rec['first_name']} {rec['last_name']}\nlayout: single\navatar: assets/images/members/{rec['pic']}\ndate: 2019-03-30 17:46:27\nportfolio-item-category:\n- people\nportfolio-item-tag:\n- {rec['rank']}\n- current member\n---\n{rec['description']}")
    else:
        file.write(f"---\ntitle: {rec['first_name']} {rec['last_name']}\nlayout: single\navatar: assets/images/members/{rec['pic']}\ndate: 2019-03-30 17:46:27\nportfolio-item-category:\n- people\nportfolio-item-tag:\n- {rec['rank']}\n---\n{rec['description']}")
    file.close()

def make_md_files(ppl_file):
    df = pd.read_csv(ppl_file)
    for index, record in df.iterrows():
        tag = get_tag_from_name(record)
        if(record['current']):
          make_file(tag,record,True)
        else:
          make_file(tag,record)

make_md_files('clean_lab.csv')
