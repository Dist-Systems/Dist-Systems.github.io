---
# Automatically generated by bib2md.py
title: "PExy: The Other Side of Exploit Kits"
slug: "Maio2014PExy_The"
date: "2014-07-10"
publishdate: "2000-01-01"

authors:
  - "Giancarlo De Maio"
  - "Alexandros Kapravelos"
  - "Yan Shoshitaishvili"
  - "Christopher Kruegel"
  - "Giovanni Vigna"

category: conference
venue: "Proceedings of the 15th Detection of Intrusions and Malware, and Vulnerability Assessment (DIMVA)"


slides: no
paper: no
text: no
external_url: https://doi.org/10.1007/978-3-319-08509-8_8
video_url: no

bibtex: |
    @inproceedings{Maio2014PExy_The,
      title     = {{PExy: The Other Side of Exploit Kits}},
      author    = {Maio, Giancarlo De and Kapravelos, Alexandros and Shoshitaishvili, Yan and Kruegel, Christopher and Vigna, Giovanni},
      booktitle = {Proceedings of the 15th Detection of Intrusions and Malware, and Vulnerability Assessment},
      series    = {DIMVA},
      month     = {July},
      year      = {2014},
      copyright = {©2014 Springer International Publishing Switzerland},
      doi       = {10.1007/978-3-319-08509-8_8},
      isbn      = {978-3-319-08508-1 978-3-319-08509-8},
      language  = {en},
      pages     = {132--151},
      publisher = {Springer International Publishing},
      url       = {https://doi.org/10.1007/978-3-319-08509-8_8}
    }




---

The drive-by download scene has changed dramatically in the last few years. What was a disorganized ad-hoc generation of malicious pages by individuals has evolved into sophisticated, easily extensible frameworks that incorporate multiple exploits at the same time and are highly configurable. We are now dealing with exploit kits. In this paper we focus on the server-side part of drive-by downloads by automatically analyzing the source code of multiple exploit kits. We discover through static analysis what checks exploit-kit authors perform on the server to decide which exploit is served to which client and we automatically generate the configurations to extract all possible exploits from every exploit kit. We also examine the source code of exploit kits and look for interesting coding practices, their detection mitigation techniques, the similarities between them and the rise of Exploit-as-a-Service through a highly customizable design. Our results indicate that even with a perfect drive-by download analyzer it is not trivial to trigger the expected behavior from an exploit kit so that it is classified appropriately as malicious.