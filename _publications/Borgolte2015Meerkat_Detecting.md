---
# Automatically generated by bib2md.py
title: "Meerkat: Detecting Website Defacements through Image-based Object Recognition"
slug: "Borgolte2015Meerkat_Detecting"
date: "2015-08-13"
publishdate: "2000-01-01"

authors:
  - "Kevin Borgolte"
  - "Christopher Kruegel"
  - "Giovanni Vigna"

category: conference
venue: "Proceedings of the 24th USENIX Security Symposium (USENIX Security)"


slides: yes
paper: no
text: no

video_url: no

bibtex: |
    @inproceedings{Borgolte2015Meerkat_Detecting,
      title     = {{Meerkat: Detecting Website Defacements through Image-based Object Recognition}},
      author    = {Borgolte, Kevin and Kruegel, Christopher and Vigna, Giovanni},
      booktitle = {Proceedings of the 24th USENIX Security Symposium},
      series    = {USENIX Security},
      month     = {August},
      year      = {2015},
      publisher = {USENIX}
    }




aliases:

- "publications/usesec2015-meerkat"

---

Website defacements and website vandalism can inflict significant harm on the website owner through the loss of sales, the loss in reputation, or because of legal ramifications.  Prior work on website defacements detection focused on detecting unauthorized changes to the web server, e.g., via host-based intrusion detection systems or file-based integrity checks. However, most prior approaches lack the capabilities to detect the most prevailing defacement techniques used today: code and/or data injection attacks, and DNS hijacking. This is because these attacks do not actually modify the code or configuration of the website, but instead they introduce new content or redirect the user to a different website.  In this paper, we approach the problem of defacement detection from a different angle: we use computer vision techniques to recognize if a website was defaced, similarly to how a human analyst decides if a website was defaced when viewing it in a web browser. We introduce MEERKAT, a defacement detection system that requires no prior knowledge about the website’s content or its structure, but only its URL. Upon detection of a defacement, the system notifies the website operator that his website is defaced, who can then take appropriate action. To detect defacements, MEERKAT automatically learns high-level features from screenshots of defaced websites by combining recent advances in machine learning, like stacked autoencoders and deep neural networks, with techniques from computer vision. These features are then used to create models that allow for the detection of newly-defaced websites.  We show the practicality of MEERKAT on the largest website defacement dataset to date, comprising of 10,053,772 defacements observed between January 1998 and May 2014, and 2,554,905 legitimate websites. Overall, MEERKAT achieves true positive rates between 97.422% and 98.816%, false positive rates between 0.547% and 1.528%, and Bayesian detection rates (the likelihood that if we detect a website as defaced, it actually is defaced; P(true positive|positive)) between 98.583% and 99.845%, thus significantly outperforming existing approaches.