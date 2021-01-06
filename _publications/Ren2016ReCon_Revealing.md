---
# Automatically generated by bib2md.py
title: "ReCon: Revealing and Controlling PII Leaks in Mobile Network Traffic"
slug: "Ren2016ReCon_Revealing"
date: "2016-05-26"
publishdate: "2000-01-01"

authors:
  - "Jingjing Ren"
  - "Ashwin Rao"
  - "Martina Lindorfer"
  - "Arnaud Legout"
  - "David Choffnes"

category: conference
venue: "Proceedings of the International Conference on Mobile Systems, Applications and Services (MobiSys)"


slides: no
paper: no
text: no

video_url: no

bibtex: |
    @inproceedings{Ren2016ReCon_Revealing,
      title     = {{ReCon: Revealing and Controlling PII Leaks in Mobile Network Traffic}},
      author    = {Ren, Jingjing and Rao, Ashwin and Lindorfer, Martina and Legout, Arnaud and Choffnes, David},
      booktitle = {Proceedings of the International Conference on Mobile Systems, Applications and Services},
      series    = {MobiSys},
      month     = {May},
      year      = {2016},
      address   = {Singapore}
    }




---

It is well known that apps running on mobile devices extensively track and leak users’ personally identifiable information (PII); however, these users have little visibility into PII leaked through the network traffic generated by their devices, and have poor control over how, when and where that traffic is sent and handled by third parties. In this paper, we present the design, implementation, and evaluation of ReCon: a cross-platform system that reveals PII leaks and gives users control over them without requiring any special privileges or custom OSes. ReCon leverages machine learning to reveal potential PII leaks by inspecting network traffic, and provides a visualization tool to empower users with the ability to control these leaks via blocking or substitution of PII. We evaluate ReCon’s effectiveness with measurements from controlled experiments using leaks from the 100 most popular iOS, Android, and Windows Phone apps, and via an IRB-approved user study with 92 participants. We show that ReCon is accurate, efficient, and identifies a wider range of PII than previous approaches.