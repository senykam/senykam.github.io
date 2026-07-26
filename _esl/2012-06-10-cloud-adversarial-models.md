---
layout: archived-post
title: "Cloud Adversarial Models"
date: 2012-06-10
categories: [Cloud Computing]
slug: cloud-adversarial-models
source: https://esl.cs.brown.edu/blog/cloud-adversarial-models/
---

![](/assets/img/esl/sith.jpg)

 Last April I attended a workshop organized by the NSF on cloud security (see [here](http://www.cccblog.org/2012/04/20/cise-researchers-discuss-security-for-cloud-computing/) for an overview from the Computing Community Consortium blog). The goal was to get a few people to think about the most interesting and important future research directions in cloud security.

The attendees came from a wide range of backgrounds: operating systems, networking, computer architecture, security and cryptography. It was really interesting to see how people from different communities think about and approach the same issues.

I was asked to think about adversarial models for the cloud. My slides are [here](http://illinois.edu/blog/dialogFileSec/2437.pdf). They are a bit concise (as some have already [pointed out](https://twitter.com/zooko/status/194435090087034880)) so I'd like to expand. Note that by cloud here I mean public infrastructure clouds like Amazon EC2 and Microsoft Azure.

**Traditional adversaries.** Like any system, public clouds have to be secured against the usual adversaries: spammers, hackers, malware, criminals, foreign governments etc. There isn't much new here so mitigating these attacks will require familiar tools like intrusion detection, isolation, firewalls, authentication, access control, logs etc.

**Rogue employees.** Another kind of adversary that providers have to protect against are rogue employees. Of course, malicious employees are also a threat in private networks and private clouds but in a public cloud they have the power to not only affect their employer (i.e., the cloud provider) but also their employer's customers. Most providers go to great lengths to make sure their infrastructure is secure against this threat. Current approaches include background checks for data center operators, logging and audits.

**Tenants.** A more interesting and new kind of adversary in public clouds are malicious tenants. These fall under a different adversarial model than traditional attackers since they are paying customers and have authorized access to the infrastructure. Theoretically this access should make it easier for them to carry out attacks. On the other hand, if the attacks originate from inside the cloud they are running on the provider's infrastructure which could (if secured and instrumented properly) provide visibility into the attacks and in turn improve detection. An advantage tenants have over traditional adversaries is that their attacks may be more difficult to detect since they could try to disguise it as authorized (or even buggy) behavior.

**Cloud providers.** The most difficult adversary to protect against in a public cloud is the cloud provider itself. It controls everything: the data center, the network, the hypervisor, the hardware and the employees! And as discussed in my previous post, traditional security mechanisms aren't much help here since most of them rely on the integrity of the OS or hypervisor and these are under the control of the provider. As far as I can tell there are really only a handful of approaches that can work here. The first is cryptography which doesn't rely on anything the provider controls. Others could include secure hardware (though here you have to trust the manufacturer) and third party audits.

Currently, it looks like audits are a popular way of providing assurance against an untrusted provider. There are dozens of these (as a function of industry and compliance issues) so I won't go into details. An important research direction in cloud security will be to provide new mechanisms that are cheaper and more secure than third party audits. There is already some interesting work in this direction which I hope to discuss in future posts.

**Governments.** While providers may be the strongest cloud adversary, the one I find the most interesting are governments. Here I don't mean foreign governments that try to infiltrate the cloud---this would fall under the traditional adversarial models---but the governments in whose jurisdiction a provider's data center is located. Depending on the country, governments can be very powerful adversaries since they can compel providers to reveal keys, logs and data and can do so without customers ever knowing about it. It's not quite clear how to relate government adversaries to malicious providers. A government adversary cannot do everything that a malicious provider can do (again this depends on the country) so they are weaker in one sense. On the other hand, they can do some things that a malicious provider cannot do like obtain information from multiple providers. Also, providers may have economic incentives not to act too maliciously whereas governments don't. Protecting against governments is hard and will require a mix of technology and policy. The technology solutions cannot rely on traditional security since that can be trivially circumvented with a warrant or subpoena.

**Update (09/29/12):** The final report of the workshop is posted [here](https://illinois.edu/blog/dialogFileSec/2667.pdf).
