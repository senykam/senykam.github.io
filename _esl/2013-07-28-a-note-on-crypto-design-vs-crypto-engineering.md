---
layout: archived-post
title: "A Note on Crypto Design vs Crypto Engineering"
date: 2013-07-28
categories: [Applied Crypto]
slug: a-note-on-crypto-design-vs-crypto-engineering
source: https://esl.cs.brown.edu/blog/a-note-on-crypto-design-vs-crypto-engineering/
---

![](/assets/img/esl/hand.jpg)

 In my [previous post](http://outsourcedbits.org/2013/07/23/are-compliance-and-privacy-always-at-odds/), I described a cryptographic protocol that could allow a telecommunications company to keep its data, and the NSA to legally access it (i.e., with authorization from a FISA court) without revealing its queries.

In response to the post, a few people have asked me whether the protocol was implemented and, if not, where they could get implementations of the underlying components. My response is that *I did not implement it*. These questions about implementations, however, made me realize that I should provide some context since I'm afraid the way I described the protocol might have made it looked easy to implement---which is definitely not the case! So in this post, I'd like to discuss the differences (as I see them) between the various aspects of cryptography.

## Theory vs. Design vs. Engineering

When one is doing cryptography, there are roughly three different types of work that are of interest: studying cryptography (theory), constructing cryptography (design) and implementing cryptography (engineering). The problem is that each task requires a lot of experience to master and each one requires a different combination of skillsets. For this reason, most people specialize in just one or at most two of these tasks.

*Theory* is mostly about understanding the limits of cryptography---what can and can't be done and why. This includes trying to understand what it means for cryptosystems to be secure and understanding the relationships between various cryptographic objects. Often this requires understanding of theoretical computer science (i.e., complexity theory and algorithms) and math (i.e., probability theory, combinatorics and algebra).

*Design* is mostly about constructing (relatively) efficient primitives and protocols. This usually requires understanding of crypto theory and math (especially number theory and algebra).

*Engineering* is mostly about implementing the primitives and protocols securely and efficiently and about integrating them in larger useful systems. This usually requires an understanding of crypto design, algorithms and data structures, software engineering and system design/engineering.

Of course this is a very coarse description, but I think it captures the differences at a high-level and explains why there is such little overlap and so many disputes between the communities: there are just too few people who possess the skills needed to work in more than a single area.

## Crypto Abstractions

My [previous](http://outsourcedbits.org/2013/07/23/are-compliance-and-privacy-always-at-odds/) was an exercise in *design* and for the purpose of design it is useful to abstract/hide away many details that are crucial for engineering. As a concrete example, consider the part of the post where I casually say:

> More formally, we would write that for all $$i$$, $$F_K(w_i) = (\ell_i, p_i),$$ where $$F$$ is a pseudo-random function (PRF). A PRF is sort of like a keyed hash.

A statement like this is hard to work with form an engineering perspective. First of all what the hell is a PRF? Are there any implementations of it in crypto library $$X$$? If not, how do I implement one? Is there a limit to how long PRF inputs can be? If so, what happens if $$w_i$$ is longer than that limit? What does "sort of" mean?

The answers to all these questions are non-trivial and it takes quite a bit of expertise to ask these types of questions properly and to solve them. This is partly why crypto engineering is so difficult and why it's usually advised to let experts do it.

But understanding cryptography through these abstractions is very useful for the task of design. The process of designing a protocol (or primitive) for a given problem mostly requires one to isolate and understand the security challenges imposed by the problem and then to use, invent or combine, crypto building blocks to overcome these challenges. To do this properly, one is not interested in how the building blocks are implemented (though as I'll discuss below, this can have severe consequences). What one cares about is what *security properties* the building blocks possess so that they can be used and combined to overcome a particular challenge.

This is why "crypto designers" usually talk about things like pseudo-random functions, pseudo-random permutations, hash functions, signatures and zero-knowledge proofs and not about HMAC, AES, SHA2, DSA, or Schnorr signatures. These abstractions are useful for design because they focus on, and make very explicit, the security properties one gets from the object. For example, HMAC is a PRF but HMAC is other things as well. If, in my previous post I had said:

> More formally, we would write that for all $$i$$, $$\textrm{HMAC}_K(w_i) = (\ell_i, p_i),$$

one might wonder why I' m using HMAC. Which property exactly of HMAC are we taking advantage of? What is the problem we're trying to solve by using HMAC here? Why HMAC and not something else?

## Limitations of Abstractions

So there are benefits to thinking in terms of theoretical abstractions for the purpose of design. Unfortunately there are also serious downsides.

The most obvious one is that it makes the jump from design to engineering harder. As discussed above, one has to know or figure out what the abstraction corresponds to in practice and sometimes the abstraction can be more than one level deep (e.g., a PRF should be instantiated with HMAC and HMAC should be instantiated with SHA2).

The second problem is efficiency. It might not matter how a primitive is instantiated for the purpose of a design exercise, but it does matter for practice since different primitives achieve different levels of efficiency.

And finally, it matters for security. The reason is that many of the abstractions we have created over the years to make the task of design and theory easier to achieve, hide details that---it turns out---have an important impact on security.

The best example of this are [side-channel attacks](http://en.wikipedia.org/wiki/Side_channel_attack) which were not captured by the abstractions until very recently [^1]. This has had the bizarre consequence that one could design protocols that looked fine from a design perspective but that were completely broken in reality.

The fact that side-channels were ignored for so long at the theory and design levels also meant that engineers had to take it upon themselves to fix the problem. So side-channel expertise has really become a skillset that crypto engineers need to have (which adds another layer of complexity to crypto engineering) and that designers and theorists severely lack.

## Conclusions

So all this to say that for most posts, I'll be discussing design-level problems and solutions and using design-level abstractions to do so but it's important to keep in mind the limitations of and consequences of this approach.

The main reasons for this decision are that: (1) I only have basic knowledge of crypto engineering so I wouldn't have anything interesting to say about it; and (2) there are others with more expertise who do have interesting things to say.

So if you are interested in crypto engineering, the first thing you should do is read Matt Green's [blog](http://blog.cryptographyengineering.com/) (though Matt also discusses design and theory issues). Other good blogs to read are [Imperial Violet](https://www.imperialviolet.org/), [Daeomic Dispatches](http://www.daemonology.net/blog/) and [Root Labs](http://rdist.root.org/). Good resources are the Matasano [crypto challenges](http://www.matasano.com/articles/crypto-challenges/) and the [NaCl project](http://nacl.cr.yp.to/index.html). Finally, the [CHES](http://www.chesworkshop.org/}) and [Real-World Cryptography](http://realworldcrypto.wordpress.com/) workshops are good events to attend.

If you are interested in theory and/or design I would recommend the [MPC Lounge](http://mpclounge.wordpress.com/), the [Bristol Cryptography Blog](http://bristolcrypto.blogspot.com/) and [Random Bits](http://jonkatz.wordpress.com/}) (it hasn't been updated in a while but the archives are worth reading).

If you're interested in theory I would recommend [Windows on Theory](http://windowsontheory.org/) and [In Theory](http://lucatrevisan.wordpress.com/) (though these cover a lot more than crypto).

[^1]: There is a recent line of work in cryptographic theory called *leakage-resilient cryptography* that tries to study the impact of side-channels and tries to inform crypto design. The area is relatively new and a bit late considering side-channels were first demonstrated in 1996 in [this paper](http://www.cryptography.com/public/pdf/TimingAttacks.pdf) by Paul Kocher. So far it's not clear whether the work in this area will have any significant impact on crypto design or engineering but I hope it will.
