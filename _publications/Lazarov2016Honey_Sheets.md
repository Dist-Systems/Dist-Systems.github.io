---
# Automatically generated by bib2md.py
title: "Honey Sheets: What Happens to Leaked Google Spreadsheets?"
slug: "Lazarov2016Honey_Sheets"
date: "2016-08-01"
publishdate: "2000-01-01"

authors:
  - "Martin Lazarov"
  - "Jeremiah Onaolapo"
  - "Gianluca Stringhini"

category: workshop
venue: "Proceedings of the 2016 USENIX Workshop on Cyber Security Experimentation and Test (CSET)"


slides: no
paper: no
text: no

video_url: no

bibtex: |
    @inproceedings{Lazarov2016Honey_Sheets,
      title     = {{Honey Sheets: What Happens to Leaked Google Spreadsheets?}},
      author    = {Lazarov, Martin and Onaolapo, Jeremiah and Stringhini, Gianluca},
      booktitle = {Proceedings of the 2016 USENIX Workshop on Cyber Security Experimentation and Test (CSET)},
      month     = {August},
      year      = {2016},
      address   = {Austin, TX},
      publisher = {USENIX}
    }




---

Cloud-based documents are inherently valuable, due to the volume and nature of sensitive personal and business content stored in them. Despite the importance of such documents to Internet users, there are still large gaps in the understanding of what cybercriminals do when they illicitly get access to them by for example compromising the account credentials they are associated with. In this paper, we present a system able to monitor user activity on Google spreadsheets. We populated 5 Google spreadsheets with fake bank account details and fake funds transfer links. Each spreadsheet was configured to report details of accesses and clicks on links back to us. To study how people interact with these spreadsheets in case they are leaked, we posted unique links pointing to the spreadsheets on a popular paste site. We then monitored activity in the accounts for 72 days, and observed 165 accesses in total. We were able to observe interesting modifications to these spreadsheets performed by illicit accesses. For instance, we observed deletion of some fake bank account information, in addition to insults and warnings that some visitors entered in some of the spreadsheets. Our preliminary results show that our system can be used to shed light on cybercriminal behavior with regards to leaked online documents.