---
# Automatically generated by bib2md.py
title: "Dowsing for Overflows: A Guided Fuzzer to Find Buffer Boundary Violations"
slug: "Haller2013Dowsing_for"
date: "2013-08-13"
publishdate: "2000-01-01"

authors:
  - "Istvan Haller"
  - "Asia Slowinska"
  - "Matthias Neugschwandtner"
  - "Herbert Bos"

category: conference
venue: "Proceedings of the 22nd Symposium on USENIX Security"


slides: no
paper: no
text: no

video_url: no

bibtex: |
    @inproceedings{Haller2013Dowsing_for,
      title     = {{Dowsing for Overflows: A Guided Fuzzer to Find Buffer Boundary Violations}},
      author    = {Haller, Istvan and Slowinska, Asia and Neugschwandtner, Matthias and Bos, Herbert},
      booktitle = {Proceedings of the 22nd Symposium on USENIX Security},
      month     = {August},
      year      = {2013}
    }




---

Dowser is a ‘guided’ fuzzer that combines taint tracking, program analysis and symbolic execution to find buffer overflow and underflow vulnerabilities buried deep in a program’s logic. The key idea is that analysis of a program lets us pinpoint the right areas in the program code to probe and the appropriate inputs to do so.  Intuitively, for typical buffer overflows, we need consider only the code that accesses an array in a loop, rather than all possible instructions in the program. After finding all such candidate sets of instructions, we rank them according to an estimation of how likely they are to contain interesting vulnerabilities. We then subject the most promising sets to further testing. Specifically, we first use taint analysis to determine which input bytes influence the array index and then execute the program symbolically, making only this set of inputs symbolic. By constantly steering the symbolic execution along branch outcomes most likely to lead to overflows, we were able to detect deep bugs in real programs (like the nginx webserver, the inspircd IRC server, and the ffmpeg videoplayer). Two of the bugs we found were previously undocumented buffer overflows in ffmpeg and the poppler PDF rendering library.