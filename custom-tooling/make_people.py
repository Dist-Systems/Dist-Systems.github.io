#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import os
import sys

from shutil import copyfile
import pandas as pd
import jinja2

__author__ = "Noah Spahn <ncs@cs.ucsb.edu>"
__description__ = """Generates people entries from a data file"""
__version__ = "0.0.0"


def main(ppl_file, template_filename, out_directory, archive_location):
    print(f"reading from:{ppl_file}")
    print("template: {template_filename}")
    print(f"out directory:{out_directory}")
    print("archive_location{archive_location}")
    with open(template_filename, "r") as template_file:
        template_red = template_file.read()
        template = jinja2.Template(template_red)
        
    os.makedirs(out_directory, mode=0o700, exist_ok=True)

    df = pd.read_csv(ppl_file)
    for index, record in df.iterrows():

        # Just show the current folks for now
        if record["public"]: #and record["current"]:

            key = "{}{}".format(record["first_name"][0], record["last_name"])
            key = key.lower()
            person_directory = os.path.normpath(out_directory + "/" + key)
            # Make directory
            print("making", person_directory)
            os.makedirs(person_directory, mode=0o700, exist_ok=True)

            # Find photo
            file_name = record["picture"]
            print("\tfile_path:", file_name)
            if isinstance(file_name, str):
                files_to_display = [name for name in os.listdir(archive_location)]
                if file_name in files_to_display:
                    copyfile(
                        os.path.join(archive_location, file_name),
                        os.path.join(person_directory, file_name),
                    )
                else:
                    record["picture"] = float("NaN")
                    print("\tNOT found")

            if(record["current"]):
                rank = record["rank_id"] + 10
            else:
                rank = record["rank_id"] + 60

            record["rank_id"] = str(rank) + record["rank"]

            with open("{}/{}.md".format(person_directory, "index"), "w+") as f:
                f.write(template.render(record))
                print("\t", index, record["first_name"], record["last_name"])

if __name__ == "__main__":
    print(len(sys.argv),"arguments passed")
    pepl_file = "tools/clean_lab.csv"
    template_fn = 'tools/person_template.j2'
    out_dir = os.path.normpath(sys.argv[2])
    archive_dir = os.path.normpath(sys.argv[3])
    main(pepl_file, template_fn, out_dir, archive_dir)
