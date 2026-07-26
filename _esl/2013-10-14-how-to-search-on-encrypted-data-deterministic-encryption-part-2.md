---
layout: archived-post
title: "How to Search on Encrypted Data: Deterministic Encryption (Part 2)"
date: 2013-10-14
categories: [Encrypted search]
slug: how-to-search-on-encrypted-data-deterministic-encryption-part-2
source: https://esl.cs.brown.edu/blog/how-to-search-on-encrypted-data-deterministic-encryption-part-2/
tags: [deterministic encryption, PPE]
---

*This is the second part of a series on searching on encrypted data. See parts [1](/encrypted-systems-lab/how-to-search-on-encrypted-data-introduction-part-1/), [3](/encrypted-systems-lab/how-to-search-on-encrypted-data-functional-encryption-part-3/), [4](/encrypted-systems-lab/how-to-search-on-encrypted-data-oblivious-rams-part-4/), [5](/encrypted-systems-lab/how-to-search-on-encrypted-data-searchable-symmetric-encryption-part-5/).*

![](/assets/img/esl/search.jpg)

 In this post we'll cover the simplest way to search on encrypted data. This is usually the solution people come up with when they first think of the problem of encrypted search and, as we'll see this, this approach has some nice properties but also some limitations.

To make this work we' ll need a special type of encryption scheme called a *property-preserving encryption* (PPE) scheme. PPE schemes encrypt messages in a way that leaks certain properties of the underlying message.

There are different types of PPE schemes that each leak different properties. The simplest form is *deterministic* encryption which always encrypts the same message to the same ciphertext [^1]. The property preserved by deterministic encryption is *equality* since, given two encryptions

\[ c_1 = {\sf Enc}_K(m_1) \textrm{ and } c_2 = {\sf Enc}_K(m_2), \]

one can test if the underlying messages are equal by just checking if \(c_1 = c_2\) [^2]. More complex PPE schemes include [order-preserving encryption](http://www.cc.gatech.edu/~aboldyre/papers/bclo.pdf) (OPE) and [orthogonlity-preserving encryption](http://www.cs.utexas.edu/~jrous/documents/191.pdf).

The approach we'll describe here works with any PPE scheme but is easier to explain with deterministic encryption so that's what we'll use. PPE-based encrypted search was first proposed in the Database community and later studied more formally in the Cryptography community. The first paper to provide a cryptographic treatment of this approach was a 2006 paper by Bellare, Boldyreva and O' Neill \[[BBO06](http://eprint.iacr.org/2006/186.pdf)\].

The authors formally study the notion of deterministic encryption and show how to apply it to the problem of encrypted search. While Bellare et al. were motivated in part by searching on encrypted data, the notion of deterministic encryption is interesting to cryptographers in its own right and the formal study of deterministic encryption that was initiated by this paper has led to other applications and deepened our understanding of encryption.

As mentioned above, another
 important type of PPE is OPE which was introduced by Agrawal, Kiernan, Srikant and Xu in \[[AKSX04](http://rsrikant.com/papers/sigmod04.pdf)\] and studied more formally by Boldyreva, Chenette, Lee and O' Neill \[[BCLO09](http://www.cc.gatech.edu/~aboldyre/papers/bclo.pdf)\] and \[[BCO11](http://www.cc.gatech.edu/~aboldyre/papers/operev.pdf)\].

## The High-Level Idea

Suppose we have both a deterministic encryption scheme \({\sf Enc}^D\) and a standard [CPA-secure](http://en.wikipedia.org/wiki/Ciphertext_indistinguishability) (i.e., randomized) encryption scheme \({\sf Enc}^R\) .

We can then create an encrypted database \({\sf EDB}\) as follows. For each document \(D_i\) in the collection \((D_1, \dots, D_n)\) , the client computes deterministic encryptions of each keyword of \(D_i\) . Assuming each document \(D_i\) has \(m\) keywords \((w_{i,1}, \dots, w_{i,m})\) , the {\sf EDB} then simply consists of \(n\) tuples

\[ r_i = (d_{i,1}, \dots, d_{i,m}, {\sf ptr}(c_i)), \]

where \(d_{i,j} = {\sf Enc}^D_{K_2}(w_{i,j})\) , \(c_i = {\sf Enc}^R_{K_1}(D_i)\) and \({\sf ptr}(c_i)\) is a pointer to ciphertext \(c_i\) .

Recall that in our setting, the client sends the encrypted database

\[ {\sf EDB} = (r_1, \dots, r_n) \]

to the server along with the randomized encryptions of the documents \((c_1, \dots, c_n)\) .

To search for keyword \(w\) , the client just sends a deterministic encryption of \(w\) to the server. This encryption of the keyword, \(d_w = {\sf Enc}^D_{K_1}(w)\) , will serve as the token. Now all the server has to do is compare \(d_w\) to all the deterministic encryptions in \({\sf EDB}\) . If \(d_w\) is equal to any of them, the server follows the corresponding pointer and returns the encrypted document. In other words, for all \(1 \leq i \leq n\) and \(1 \leq j \leq m\) , the server tests if \(d_w = d_{i,j}\) and if they are equal it follows \({\sf ptr}(c_i)\) and returns \(c_i\) .

This clearly works but there is a limitation in the way the scheme is described: the search time for the server is \(O(nm)\) , i.e., linear in the number of documents (let's just assume \(m\) is very small here). Obviously, linear-time search is too slow for practice but in reality this is not a problem because we can just store the deterministic encryptions of \({\sf EDB}\) in data structures that support fast search (e.g., a binary search tree) so that search can be performed very quickly (e.g., in time \(O(\log(n))\) .

## Is This Secure?

As we've seen, PPE-based solutions can achieve fast (i.e., sub-linear) server-side encrypted search. They do, however, have some limitations with respect to security as discussed and formalized by Bellare et al.

The first problem is that the encrypted database \({\sf EDB}\) leaks quite a bit of information to the server about the data collection---even before the client has performed any searches. In particular, recall that the keywords in \({\sf EDB}\) are encrypted using a deterministic encryption scheme so the same keyword \(w\) will always encrypt to the same ciphertext.

This means that if the server sees two or more equal ciphertexts in \({\sf EDB}\) it knows that the corresponding encrypted documents contain a keyword in common. In addition, the server learns the frequency with which keywords appear which makes the encrypted database vulnerable to [frequency analysis](http://en.wikipedia.org/wiki/Frequency_analysis).

Another issue is that since tokens are deterministic encryptions of the search terms, the server will always know whether the client is repeating a search a not.

A third issue occurs when the deterministic encryption scheme (or any form of PPE scheme) is public-key. In this case, all the deterministic encryptions (both in \({\sf EDB}\) and in the tokens) are encrypted under the client's public key which is, obviously, public and available to the server. The server can then mount a dictionary attack on the encrypted database by encrypting a list of possible keywords and comparing them to the ones found in \({\sf EDB}\) and in the tokens. If it gets a match then it knows the keyword.

This attack clearly shows that public-key PPE-based solutions should probably not be used for "normal" data (e.g., text, emails, PII etc.). But does it mean we can't use it all? Not quite. As Bellare et al. observe in their paper, such a solution can be used when the data has high min-entropy, which is a way of saying that the data looks random to the server.

The problem of course is that it's not clear when this applies in practice. Also, note that even if the keywords do have high min-entropy, the other two issues still remain.

## Conclusions

So we've seen one approach to searching on encrypted data based on property-preserving encryption. It results in a solution that supports fast search on encrypted data but, unfortunately, leaks quite a bit of information to the server. In the next post we'll go over another solution that provides a different tradeoff: it leaks less information to the server but achieves slower search time.


[^1]: In general it is a terrible idea to encrypt with deterministic encryption since we've known since \[[GM84](http://theory.lcs.mit.edu/~cis/pubs/shafi/1984-jcss.pdf}{this})\] that any [secure](http://en.wikipedia.org/wiki/Semantic_security) encryption scheme has to be randomized. The point here, however, is that we may be willing to use weaker primitives in order to design more functional encryption schemes.

[^2]: Technically, we do not need a deterministic *encryption* scheme since we'll never need to decrypt so (in the symmetric setting) one could use a [pseudo-random function](http://en.wikipedia.org/wiki/Pseudorandom_function_family).
