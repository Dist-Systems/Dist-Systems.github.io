---
# Automatically generated by bib2md.py
title: "Jackdaw: Towards Automatic Reverse Engineering of Large Datasets of Binaries"
slug: "Polino2015Jackdaw_Towards"
date: "2015-07-09"
publishdate: "2000-01-01"

authors:
  - "Mario Polino"
  - "Andrea Scorti"
  - "Federico Maggi"
  - "Stefano Zanero"

category: conference
venue: "Proceedings of the 12th Detection of Intrusions and Malware, and Vulnerability Assessment (Lecture Note in Computer Science)"


slides: no
paper: no
text: no
external_url: https://doi.org/10.1007/978-3-319-20550-2_7
video_url: no

bibtex: |
    @inproceedings{Polino2015Jackdaw_Towards,
      title     = {{Jackdaw: Towards Automatic Reverse Engineering of Large Datasets of Binaries}},
      author    = {Polino, Mario and Scorti, Andrea and Maggi, Federico and Zanero, Stefano},
      booktitle = {Proceedings of the 12th Detection of Intrusions and Malware, and Vulnerability Assessment},
      series    = {Lecture Note in Computer Science},
      month     = {July},
      year      = {2015},
      copyright = {©2015 Springer International Publishing Switzerland},
      doi       = {10.1007/978-3-319-20550-2_7},
      isbn      = {978-3-319-20549-6 978-3-319-20550-2},
      language  = {en},
      pages     = {121--143},
      publisher = {Springer International Publishing},
      url       = {https://doi.org/10.1007/978-3-319-20550-2_7}
    }




---

When analyzing an untrusted binary, reverse engineers usually rely on ad-hoc collections of interesting dynamic patterns—known as behaviors in the malware-analysis community—and static patterns—known as signatures in the antivirus community. Such patterns are often part of the skill set of the analyst, sometimes implemented in manually-created post-processing scripts. It would be desirable to be able to automatically find such behaviors, present them to analysts, and create a systematic catalog of matching rules and relevant implementations. We propose Jackdaw, a system that finds interesting dynamic patterns, and ranks them to unveil potentially interesting behaviors. Then, it annotates them with static information, capturing the distinct implementations of each across different malware families. Finally, Jackdaw associates semantic information to the behaviors, so as to create a descriptive summary that helps the analysts in querying the catalog of behaviors by type. To do this, it leverages the dynamic information and an indexed Web-based knowledge databases. We implement and demonstrate Jackdaw on the Win32 API (even if the technique can be generalized to any OS). On a dataset of 2,136 distinct binaries, including both malicious and benign libraries and executables, we compared the behaviors extracted automatically against a ground truth of 44 behaviors created manually by expert analysts. Jackdaw found 77.3 % of them and was able to exclude spurious behaviors in 99.6 % cases. We also discovered 466 novel behaviors, among which manual exploration and review by expert reverse engineers revealed interesting findings and confirmed the correctness of the semantic tagging.