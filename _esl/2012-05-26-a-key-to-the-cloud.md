---
layout: archived-post
title: "A Key to the Cloud"
date: 2012-05-26
categories: [Cloud Computing]
slug: a-key-to-the-cloud
source: https://esl.cs.brown.edu/blog/a-key-to-the-cloud/
---

![](/assets/img/esl/cloud.jpg)

 At this point most people would agree that cloud computing represents a major shift in computing. Consider, for example, that many tech companies are entirely cloud-based. This includes the more established like Netflix and startups like Instagram and Pinterest. Instead of building and maintaining their own computing infrastructure, they can scale on-demand, save money and focus on improving their services.

Scientists and engineers whose research was limited by the computing resources they had at their disposal (usually whatever their departments could afford) can now use the cloud to process huge amounts of data and run large-scale simulations cheaply [^1].

For computer scientists such as myself, the cloud introduces new and intriguing challenges. Problems like minimizing energy consumption, designing data centers and optimally pricing computation require skills that are not part of a traditional computer science education. So to solve these problems (among many others) we' ll have to acquire new skills and work closely with electrical engineers, architects and economists. Cloud computing also makes us think about old problems in new ways. Many fields like databases, cryptography, operating systems, security and distributed systems are re-evaluating some of their basic assumptions in order to adapt to the cloud.

## Outsourcing vs. Control

One of the essential aspects of public clouds is outsourcing (the other being multi-tenancy). Outsourcing is why we want cloud computing in the first place but it comes with a loss of control. This is one of the main shortcomings of public clouds and possibly the biggest barrier to adoption.

So what's the solution? How can I secure my data/workload from someone that completely controls the hardware, the network, and the operating system? Standard security mechanisms like firewalls, intrusion detection systems, VM isolation all rely on the integrity of the underlying OS or hypervisor but in a public cloud these are under the control of the adversary.

One thing we can do is use cryptography. Modern crypto tends to rely on three things: (1) that some computational problem is hard; (2) that keys and randomness are generated securely; and (3) that secret keys are kept secure (though recent work has shown that this can be relaxed a bit). So as long as we can generate and store keys securely (i.e., in a manner that is not controlled by the cloud provider), cryptography is a potential solution to our problem (there are others of course, but I'll leave that to future posts).

## Crypto & Paradoxes

Unfortunately, many problems come with using cryptography. The first is that crypto can be destructive. It'll get the job done but it will destroy everything in the process. This is an issue because in the context of outsourcing we might like the cloud provider to do something useful for us. Another problem is overhead. We can do a lot using very sophisticated cryptographic techniques but often the cost makes it a non-starter.

So before crypto can be a useful solution to our outsourcing vs. control problem we need mechanisms that: (1) protect our data/workloads without relying on things the provider can control; (2) offer utility by allowing the provider to do things we deem useful with our data; and (3) are efficient.

These are tough requirements to satisfy and some of them may even seem contradictory. But one of the interesting aspects of crypto is that it is very good at solving paradoxical problems. In fact, crypto research is full ideas that should not be possible but somehow are. The most well-known are zero-knowledge proofs (ZKP) invented by Goldwasser, Micali and Rackoff. With a ZKP I can prove to you that a mathematical theorem is true without ever showing you the proof. This is should seem inconsistent but it's not if you think of the problem in the right way [^2].

## Crypto & Infrastructure

This ability to provide solutions to apparent paradoxes is what gives cryptography its real power and what can make it so useful in practice. This is what enabled electronic commerce on the Internet. In the 70's, Whitfield Diffie and Martin Hellman realized that if communications were to be secured on a global network, the standard way of encrypting data had to be replaced. Up until then, encryption was a symmetric process: the person sending the message and the person receiving it had to share a common secret key in order to communicate securely.

Diffie and Hellman realized that this would not scale. How could a retailer exchange keys with all its potential customers? To resolve this, they invented public-key cryptography which enabled people to communicate securely even if they had never interacted before. This breakthrough, together with the invention of RSA by Rivest, Shamir and Adleman got rid of the main shortcoming of (symmetric-key) encryption and played a major role in making the Internet secure enough for financial transactions and electronic commerce.

## Future Directions

The reason I'm retelling this story is because---once again---cryptography has the opportunity to play a crucial role in how a major technology evolves. Like the Internet, cloud computing represents a major shift in infrastructure and just as public-key encryption had to be invented for us to secure the Internet, new advances in cryptography will have to be made for us to secure the cloud.

This blog will be (in part) about some of these advances---the ones that have already been made and the ones that are in progress.

[^1]: The company CycleComputing recently built a 50,000 core HPC cluster on Amazon EC2 called Naga. They ran a computational chemistry job for 3 hours at roughly 5000 per hour. They estimate the same job would require roughly 20 million dollars in infrastructure. Also, checkout CycleComputing's Big Science challenge.

[^2]: An interesting applications of ZKPs is described by Boaz Barak in this talk. Barak explains how he and his co-authors designed a physical version of a ZKP to prove that a nuclear warhead is authentic without revealing its design.
