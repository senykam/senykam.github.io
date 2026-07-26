---
layout: archived-post
title: "Restructuring the NSA Metadata Program"
date: 2014-03-10
categories: [Policy, Encrypted Search]
slug: restructuring-the-nsa-metadata-program
source: https://esl.cs.brown.edu/blog/restructuring-the-nsa-metadata-program/
tags: [NSA, Section 215, Metadata, MPC]
---

![](/assets/img/esl/design.jpg)

 I just got back from Barbados where I attended the [Financial Cryptography and Data Security](http://fc14.ifca.ai/) conference. It was a great event overall with many interesting talks and two great workshops.

One workshop was on [Bitcoin](http://fc14.ifca.ai/bitcoin/index.html) and was the most successful Financial Crypto workshop in history! Though I haven't personally worked on Bitcoin, one of the things I enjoyed most about the conference and workshops was the presence of the Bitcoin community. The interaction between the academic and Bitcoin communities led to some very interesting discussions and ideas. I really hope the two communities keep interacting.

The other workshop was on [applied homomorphic cryptography](https://www.dcsec.uni-hannover.de/4556.html). Homomorphic in the context of this workshop is to be understood broadly and is meant to include all cryptographic technologies that allow for some form of computation on encrypted data. As such this includes secure multi-party computation and encrypted search.

I was invited to give the keynote at this workshop and I chose to talk about how to restructure the NSA metadata program. My slides are [here](http://research.microsoft.com/en-us/um/people/senyk/slides/metacrypt.pdf). They describe---at a very high-level---a new design I refer to as MetaCrypt whose goal is to enable some of the functionality the current NSA metadata program supports but in a privacy-preserving manner. I first started thinking about this problem in July 2013 when I wrote [this blog post](http://outsourcedbits.org/2013/07/23/are-compliance-and-privacy-always-at-odds/).

Since I only had one hour, there are many details missing in the talk. Also, since this was a talk aimed at a general crypto audience, [^1] I included a variant of the protocol that is easy to describe as opposed to variants that are perhaps more efficient and/or provide stronger security guarantees. The details and alternative designs will appear later in an accompanying paper but I hope that even this high-level description is interesting.

**Update:** my talk and the MetaCrypt project was recently covered by MIT Tech Review. See [here](http://www.technologyreview.com/news/526121/cryptography-could-add-privacy-protections-to-nsa-phone-surveillance/) for the article.


[^1]: The audience included people who focus on number-theoretic primitives, hardware crypto implementations, lattice-based cryptography etc. The ideas I described in the talk, however, required mostly background on secure multi-party computation, [searchable symmetric encryption](http://eprint.iacr.org/2006/210.pdf) and especially [structured encryption](http://eprint.iacr.org/2011/010.pdf), which are more recent and not as well-known.
