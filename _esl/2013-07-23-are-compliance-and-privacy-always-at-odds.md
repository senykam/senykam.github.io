---
layout: archived-post
title: "Are Compliance and Privacy Always at Odds?"
date: 2013-07-23
categories: [Surveillance, Encrypted search]
slug: are-compliance-and-privacy-always-at-odds
source: https://esl.cs.brown.edu/blog/are-compliance-and-privacy-always-at-odds/
tags: [MPC, OT, PIR, SSE]
---

![](/assets/img/esl/obey.jpg)

 Chris Soghoian [points](https://twitter.com/csoghoian/status/358613839094362112) to an interesting [article](http://http//online.wsj.com/article/SB10001424127887324448104578615881436052760.html) in the Wall Street Journal. It describes mounting pressure on the NSA to re-design its phone-data program---the program under which it compels telecommunications companies (telcos) like Verizon to turn over their phone record data.

In the article, Timothy Edgar, a former privacy lawyer who served in the Bush and Obama administrations is quoted as saying:

> Privacy technology under development would allow for anonymous searches of databases, keeping data out of government hands but also preventing phone companies from learning the purpose of NSA searches. Overhauling the surveillance program would provide a reason to speed up the technology's deployment.

So this motivates the following interesting technical question: *how would one design such a privacy-preserving phone-data program exactly?*

The first thing we need is that the telcos keep their data, as opposed to sending it all to the NSA. The issue with such an approach, of course, is that the NSA would have to disclose its queries to the telco in order to retrieve any information---which for obvious reasons is not going to happen.

So what we need is a mechanism with which the telcos can keep their data and the NSA can access it without disclosing its queries. This might sound impossible, but it turns out we've known how to do this (in theory at least) for over *15* years!

## Private Information Retrieval

One answer to this problem could be to use something called [private information retrieval](http://en.wikipedia.org/wiki/Private_information_retrieval) (PIR). With PIR, a client can retrieve information from a server *without the server learning anything about which item is being retrieved*. Standard PIR protocols only allow the client to retrieve information by memory location but there are more sophisticated variants that also support retrieval based on [keywords](http://eprint.iacr.org/1998/003).

PIR was first introduced in 1995 in a [paper](http://people.csail.mit.edu/madhu/papers/1995/pir-journ.pdf) by Chor, Kushilevitz, Goldreich and Sudan. Initially, PIR only worked if the data could be stored on two (or more) servers that could not collude. In a breakthrough paper, Kushilevitz and Ostrovsky showed in 1997 that PIR could be achieved even with a single server. Since then, there has been a lot of work and many advances on PIR and, recently, Ian Goldberg from the University of Waterloo and his students have been trying to make PIR practical (improving both efficiency and functionality). If you are interested in this topic (especially in the practical aspects) I highly recommend the thesis of [Olumofin](http://uwspace.uwaterloo.ca/bitstream/10012/6142/1/Olumofin_Femi.pdf).

So a simple idea to solve our problem is to have the telco keep its data and to have the NSA query it through a PIR protocol. While this might seem like a good solution, there are two important problems.

The first is that while PIR will protect the query of the NSA (i.e., the telco will not learn anything about the query) it will not necessarily protect the telco's dataset from the NSA; that is, the NSA could learn information about individuals that are not included in its query.

The second problem is that the telco has no way of knowing if the NSA' s query is legitimate. What if the NSA keeps submitting queries indiscriminately and eventually just learns the entire database? How does the telco know whether a particular query is even legal?

Fortunately, both problems can be addressed!

## Oblivious Transfer

To handle the first problem, we need a stronger form of PIR called [oblivious transfer](http://en.wikipedia.org/wiki/Oblivious_transfer) (OT). With an OT protocol, a client can select an item from a server's dataset while maintaining the following guarantees: (1) the server learns nothing about the client's query; and (2) the client learns nothing about the items it does not query. So unlike PIR, OT protects both parties; which is why it is sometimes called symmetric PIR.

Like PIR, standard OT protocols only allow clients to retrieve items by their location in memory so, in practice, we would prefer to use a keyword-based OT; that is, an OT protocol where items can be labeled with keywords and where the clients can retrieve them based on search terms. Fortunately, we already know how to design such protocols. The first keyword OT is due to Ogata and Kurosawa (see this [paper](http://seculab.cis.ibaraki.ac.jp/~kurosawa/2004/OKS.pdf)) but their scheme does not scale very well (each query would require the NSA to do work that is linear in the size of the dataset). A more efficient approach is due to Freedman, Ishai, Pinkas and Reingold and is described in this [paper](https://www.cs.princeton.edu/~mfreed/docs/FIPR05-ks.pdf).

## Keyword OT

The high-level idea of Freedman et al.'s keyword OT is as follows. As before, the server is the telco and the client is the NSA. Suppose the telco's dataset consists of \(n\) pairs \((w_1, d_1), \dots, (w_n, d_n)\) , where \(w_i\) is a keyword and \(d_i\) is some data associated to \(w_i\) . In practice, the keywords could be names and the data could be phone, address, etc. The telco starts by encrypting this dataset by replacing each pair \((w_i, d_i)\) by a label/ciphertext pair \((\ell_i, d_i \oplus p_i)\) , where the label \(\ell_i\) and the pad \(p_i\) are (pseudo-)random strings generated from \(w_i\) using a pseudo-random function with a secret key \(K\) . More formally, we would write that for all \(i\) ,

\[ F_K(w_i) = (\ell_i, p_i), \]

where \(F\) is the PRF. A PRF is sort of like a keyed hash. [^1] The main property of PRFs is that if we evaluate them with a random key \(K\) on any input, they output a random looking string.

Note that this new encrypted dataset reveals no information about the real dataset since the \(\ell_i\) values are pseudo-random (and therefore effectively independent of the \(w_i\) 's) and because the ciphertexts \(d_i\oplus p_i\) are effectively one-time pad (OTP) encryptions of the \(d_i\) 's. [^2] The telco now sends this encrypted dataset to the NSA who stores it. Remember: it reveals no information whatsoever about the real dataset so this is OK!

Now suppose the NSA needs to lookup information related to some keyword \(w\) and remember that the encrypted dataset it holds consists of labels \(\ell_i\) and ciphertexts \(d_i \oplus p_i\) . To extract the information it needs from the encrypted dataset, it therefore needs to figure out: (1) the label for keyword \(w\) (so it can lookup the appropriate OTP ciphertext); and (2) the pad \(p_i\) used in the associated ciphertext.

Of course the NSA cannot do this on its own because it does not know the telco's secret key \(K\) for the PRF used to generate these items. But we have a problem. If the NSA sends its keyword w to the telco so that the latter computes and returns \(F_K(w)\) , the telco will learn the keyword. And if the telco sends its key \(K\) to the NSA so that it computes \(F_K(w)\) on its own, the NSA will be able to decrypt the entire dataset.

The solution here is to use another amazing cryptographic technology called [secure two-party computation](http://en.wikipedia.org/wiki/Secure_multi-party_computation#Two-party_computation) (2PC). I won't try to explain how 2PC works but if you are interested a good place to start is the [MPC Lounge](http://mpclounge.au.dk/). The important thing to know about 2PC is that we can use it to solve our problem. In other words, the telco and the NSA can execute a 2PC protocol that will result in the NSA learning \(F_K(w)\) and therefore the label and the pad for \(w\) , without it learning anything about the telco's key and without the telco learning anything about \(w\) [^3].

## Authorized Queries

Now on to the second problem: how does the telco know if the NSA' s query is legitimate? To address this we first need to incorporate an extra party into our model that has the power to decide if an NSA query is legitimate or not. In practice, this would be the [FISA court](http://en.wikipedia.org/wiki/United_States_Foreign_Intelligence_Surveillance_Court) [^4] and we' ll assume this court can digitally sign, i.e., it has a secret signing key and a public verification key that is known to the telco.

Now suppose the NSA wants to retrieve information about a user Alice from the telco. It first sends its query to the court. If the court approves the query, it signs it and returns the signature to the NSA. At this point, we only need to make a small change to the protocol described above. Instead of executing a 2PC that evaluates the PRF so as to generate a label and pad for the NSA's query; the parties will execute a 2PC that first verifies the court's signature and then (if the signature checks out) evaluates the PRF (i.e., generates the label and pad for the keyword). The properties of the 2PC will hide the signature and the keyword from the telco, and the secret key \(K\) from the NSA. [^5]

## Is this really possible?

The design described above is possible in theory. But of course the interesting question is whether something like this could be used in practice.

I don't really know how large telco datasets are but I would guess on the order of hundreds of millions of users. Encrypting such a dataset and sending it to the NSA would be expensive but definitely possible as the encryption process here would consist of relatively cheap operations like PRF evaluations and XORs. The query stage, however would be very inefficient due to the execution of the 2PC protocol. But if we look at things carefully, the bottlenecks would likely be (1) the verification of the signature (due to the complexity of signature verification); and (2) the generation of the pads (since they have to be as long as the data they will be XORed with).

Fortunately there are a few things we can do to mitigate these problems. Instead of using a signature scheme, we could use a message authentication code (MAC). This would require the court to share a secret key with the telco but this doesn't seem like such a severe requirement. MACs are much simpler computationally than signatures so the 2PC verification would be much faster [^6].

With respect to the length of the pads, we could use the PRF to generate a short string instead (say 128 bits long) and use that as a seed to a pseudo-random generator to generate a larger pad. This would change how the telco and NSA encrypt and decrypt items of the dataset but it is a minor change that would not effect the efficiency of encryption and decryption much.

With these changes, the 2PC would only have to compute two PRF evaluations and one equality check which is definitely within practical reach.

**Update:** For a high-level description of the protocol I designed in this post see [this](http://boingboing.net/2014/03/01/trustycon-how-to-redesign-nsa.html) great talk by Ed Felten.

*Thanks to Matt Green and Payman Mohassel for comments on a draft of this post and to Chris Soghoian for motivating me to think about this problem.*


[^1]: PRFs are like keyed hash functions only in idealized models like the random oracle model.

[^2]: Technically, since the labels and pads are pseudo-random (as opposed to random), \(\ell_i\) is not independent of \(w_i\) and \(d_i \oplus p_i\) is not a one-time pad. More precisely, \(\ell_i\) and \(d_i \oplus p_i\) reveal no partial information about \(w_i\) and \(d_i\) to a computationally-bounded adversary.

[^3]: Protocols that evaluate PRFs in this manner are usually called oblivious PRF (OPRF) protocols. The 2PC-based OPRF protocol is the simplest to understand conceptually but we know of more efficient OPRF protocols not based on 2PC (e.g., the Freedman et al. paper describes one such construction).

[^4]: There is debate as to whether the FISA court exercises proper oversight over the NSA or not (for example see [this article](http://www.nytimes.com/2013/07/26/us/politics/robertss-picks-reshaping-secret-surveillance-court.html?_r=0) from the New York Times), but for the purpose of this exercise we'll just assume that it does.

[^5]: The reason we also need to hide the signature from the telco is that signatures can leak information about their message.

[^6]: Here we also assume the data is hashed with a collision-resistant hash function before being MACed.
