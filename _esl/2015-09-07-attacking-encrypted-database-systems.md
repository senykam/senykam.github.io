---
layout: archived-post
title: "Attacking Encrypted Database Systems"
date: 2015-09-07
categories: [Encrypted Search, Inference Attacks]
slug: attacking-encrypted-database-systems
source: https://esl.cs.brown.edu/blog/attacking-encrypted-database-systems/
tags: [PPE, CryptDB, OPE, DTE]
---

![](/assets/img/esl/edb.png)

 [Muhammad Naveed](http://cryptoonline.com/), [Charles Wright](http://web.cecs.pdx.edu/~cvwright/) and I recently posted a paper that describes inference attacks on encrypted database (EDB) systems like [CryptDB](http://css.csail.mit.edu/cryptdb/), [Cipherbase](http://research.microsoft.com/en-us/projects/cipherbase/), [Google's Encrypted BigQuery demo](https://github.com/google/encrypted-bigquery-client) and [Microsoft SQL Server 2016 Always Encrypted](https://msdn.microsoft.com/en-us/library/mt163865.aspx?f=255&MSPPError=-2147217396). These systems are based on property-preserving encryption (PPE) schemes which are a class of encryptions schemes that leak certain properties of their plaintexts. Examples include [deterministic encryption](https://en.wikipedia.org/wiki/Deterministic_encryption) (DTE) and order-preserving encryption (OPE).

The paper is [here](http://research.microsoft.com/en-us/um/people/senyk/pubs/edb.pdf) and will be presented in October at the [ACM Conference on Computer and Communication Security](http://www.sigsac.org/ccs/CCS2015/index.html).

This was an interesting project for several reasons. For one thing, it was fun to do cryptanalysis! Even though we make use of old and basic ideas like frequency analysis and of even more obvious ideas like plain sorting, we did get the chance to work on some non-trivial attacks based on combinatorial optimization. We hope to post more about this in the future and we have upcoming work that explores new interesting technical questions that came out of this.

We also got to work with real medical data and we believe our results provide a fair, accurate and realistic security evaluation of these PPE-based EDB systems. In particular, it provides a concrete and real-world analysis of the security one would get if one were to use them in an electronic medical records (EMR) setting, which is an important motivating scenario for these systems (see, e.g., \[[PRZB11](http://people.csail.mit.edu/nickolai/papers/raluca-cryptdb.pdf)\]).

## Rebuttals

The results of the paper were recently covered by the media (e.g., [Forbes](http://www.forbes.com/sites/thomasbrewster/2015/09/03/microsoft-dumb-attacks-cracks-next-gen-cryptography/) and [Ars Technica](http://arstechnica.com/security/2015/09/ms-researchers-claim-to-crack-encrypted-database-with-old-simple-trick/) and on Microsoft Research's own [blog](http://blogs.technet.com/b/inside_microsoft_research/archive/2015/09/03/database-security-arms-race-researchers-make-advances.aspx)). Some of the designers of these systems found our work important, even saying that it is

> valuable because it gives database customers a better understanding of the security precautions they need to consider, especially if they are charged with handling very sensitive data such as electronic medical records.

Others, however, dispute our results. The three arguments we have seen so far (in the Forbes and Ars Technica pieces) are that: (1) we did not break the systems; (2) we used them in a way they were not intended for; and (3) that users are warned on how to use them correctly.

The high-level point we would like to make here is that *we absolutely did use them in the way they were intended* and if you read this entire post you will see why. You will also see why the user warnings mentioned in the articles (which we could not find in the referenced paper) do not prevent the attacks.

## How We Used the Systems

First, we should be clear that we never claimed to have broken anything. But in our opinion, this is not a meaningful question anyways due to the way these PPE-based EDB systems and their underlying cryptography phrase their security claims. Roughly speaking, these systems are usually claimed to be secure under what I will refer to as *functionality assumptions*. [^1]

The problem here is that these assumptions essentially cripple the functionality of these systems in a way that make them a lot less useful and interesting than what most people believe or expect. In fact, in some cases these assumptions can almost obviate the systems' entire purpose.

For example, PPE-based EDB systems are typically claimed to be secure if a database administrator labels all "sensitive" fields (for some undefined notion of sensitivity) so that they are encrypted with standard encryption schemes. But of course, this also means that these fields then cannot be queried at all---ever. So this leaves us with an EDB system that only works over *non-sensitive* data. If it's non-sensitive, one could ask how much value we are getting from encrypting it at all. Is this really the point of an encrypted DB system? To do SQL over encrypted *non-sensitive* data? Is this really consistent with how these systems are motivated and understood?

The point is that to claim that these systems are secure, you effectively have to cripple them until you have to use regular plain encryption---at least for the kinds of data you actually care to protect.

What's going on is that there is an underlying tradeoff in these systems between security and utility and the *technical* (i.e., the fine print) security claims these systems make essentially cripples their utility. Yet, the crippled version of these systems is not what will be used in practice and it is not how these systems are understood by most people (engineers and researchers alike). Indeed, the main claim these systems make is that one can run real-world applications on top of them. In particular, applications like electronic medical records (EMR).

So in our work, we were not interested in "breaking" these systems because, under the right *functional assumptions* one can always claim they are secure. That would be a meaningless exercise.

What we set out to do was to answer a different question that is actually relevant to practice: "what security do we get when we run an EMR application on top of these systems?" In our opinion, this is not only a fair question; it is the most basic question one should ask about these systems. This is a concrete and real-world question that cannot be dismissed using assumptions and caveats.

So how do we answer such a question? Our approach was to analyze
 attributes that are relevant to EMR systems.

To support the EMR system, the EDB needs to support queries on these attributes which means that they need to be encrypted with the appropriate PPE scheme (i.e., their onion needs to be peeled to either order-preserving encryption or deterministic encryption depending on the type of query). And when this happens, the question is: "what information is leaked?"

That is what our paper explores and this is not only a fair question it is a question that has been asked about other encrypted search solutions.

Of course, in choosing attributes to analyze we were limited by our data. That is, there are many attributes used in EMR systems but we didn't have data for all of them. We felt it was important to use real data here and not synthetic data so we preferred to limit the attributes we analyzed than to compromise the integrity of the experiments. In the end, the set of attributes that are relevant to EMRs and that we had data for were: sex, race, age, admission month, whether the patient died, primary payer, length of stay, mortality risk, disease severity, major diagnostic category, admission type and admission source.

We believe it is fair to say that any reasonable EMR system would need to query these attributes. We even confirmed that the [OpenEMR](http://www.open-emr.org/) system (which is used as motivation in \[[PRZB11](http://people.csail.mit.edu/nickolai/papers/raluca-cryptdb.pdf)\] queries sex, race, age, admission month, patient died and primary payer. So the claim that we are using these systems in a way they were not intended to is completely unfounded.

## How Should They be Used?

In the rebuttal from the Forbes article, we also see the following claim:

> OPE encryption should be used for "high-entropy values" where the order does not reveal much and that CryptDB was still a worthy way to protect information. "This is how the CryptDB paper says it should be used."

First, there is no such statement in the CryptDB paper---at least we could not find one. Second, even if this warning were given to users and DB administrators, *the system would still be vulnerable to the attacks we describe!* In fact, the attacks would still work even if the data had the *maximum* possible entropy.

Let's see how. In Section 6.1 of our paper, we describe a really obvious "attack" we refer to as the *sorting attack*. Here is how it works. Suppose we are analyzing some attribute, say age, which can range over a given number of values. In the case of age, this would be from 0 to 124. Now suppose I give you an OPE-encrypted column of ages; that is, a set of OPE encryptions of the ages in the DB. Now further suppose that every possible age is represented in this column. In such a case, we say that the column is *dense*. Now to recover the plaintext values from this OPE-encrypted column, one simply needs to sort it---which can be done since OPE reveals order. At this point, it simply follows that the smallest ciphertext will correspond to 0, the second smallest to \(1\) and so on and so forth.

Of course, the statement "OPE should be used for high-entropy values" is a bit vague. In fact, it could be interpreted in two different ways but, as we will see, in each case it leads to problems. Note that by entropy, in cryptography we usually mean [min-entropy](https://en.wikipedia.org/wiki/Min_entropy).

**Interpretation #1.** The values themselves are sampled from some arbitrary distribution (perhaps even with low min-entropy) but the adversary knows nothing about them so we treat them as high min-entropy. This is completely unrealistic. Designing and using cryptography against adversaries with no auxiliary information is meaningless since auxiliary information is available. In particular, our paper implicitly makes this point since we were able to leverage publicly-available auxiliary information to mount our attacks.

**Interpretation #2.** Each value in the column is actually sampled from a high min-entropy distribution. Let' s assume this is the case and suppose the range of the attribute space is \(n\) . Furthermore, let's go as far as saying that the values are sampled uniformly at random---which has *maximum* min-entropy.

By the [coupon collector](https://en.wikipedia.org/wiki/Coupon_collector%27s_problem) problem, we can expect to see all values after \(\theta(n \log n)\) samples. More concretely, this means that we can expect the OPE-encrypted column to be dense after \(\theta(n \log n)\) patients are registered in the DB. So for example, for the "age" attribute which has \(n = 125\) , we should expect the column to be dense---and therefore vulnerable to sorting---after 604 patients appear in the DB. To give you an idea of how small that is, the largest hospital in our dataset had 121,664 patients and exactly 827 out of 1050 hospitals in our dataset had more than 604 patients (i.e., 79%).

This discussion highlights some of the pitfalls with the kind of functional assumptions used in the security claims of these systems. They are often vague, hard to interpret, hard to make actionable and, as above, sometimes do not even provide security.

## Are EDB Systems Doomed?

We personally do not think so. There are alternative ways of designing EDB systems that are currently being investigated in various research labs. What our work shows is that the EDB systems *we* looked at do not provide the level of security required for EMR systems and, most likely, other databases with similar demographic information. More generally, our work does suggest that *PPE-based* EDB systems (i.e., based on deterministic and order-preserving encryption) might not be the way to go but this does not mean that reasonably secure and efficient EDB systems are impossible to design.


[^1]: Please note that I am not trying to define a formal concept here, I am only using the term *functional assumption* for ease of exposition. Also, these assumptions are very different than, e.g., computational assumptions as typically used in cryptography. Computational assumptions usually do not limit the utility of a primitive whereas the kind of assumptions we are talking about here do. So the argument that, e.g., high min-entropy assumptions are perfectly fine because we typically use assumptions anyways does not hold.
