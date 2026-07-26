---
layout: archived-post
title: "How Not to Learn Cryptography"
date: 2014-11-11
slug: how-not-to-learn-cryptography
source: https://esl.cs.brown.edu/blog/how-not-to-learn-cryptography/
tags: [Learning]
---

![](/assets/img/esl/studying.jpg)

 People often ask me how to get started in cryptography. What's interesting is that most of the time they also want to know how I *personally* got started. This is interesting to me because it suggests that people are looking for more than a list of books or papers to read or set of exercises to solve; they're really looking for a broader *strategy* on how to learn the subject. In this post I'll discuss some possible strategies.

First, let me stress that I am only considering strategies for learning crypto design and theory. Also, what I have in mind when I say "learning crypto" is not getting to the point of understanding an average paper, but getting to the point of generating such papers yourself (or at least the ideas in them). If your end goal is crypto engineering then the strategies may or may not be helpful---I'm not an expert so I can't really say either way ( though I'd like to think that improving your understanding of how primitives and protocols are designed can be helpful).

I should say from the outset that the way I personally got started in cryptography is probably one of the worst possible ways to do it. It was highly inefficient and had a very low probability of success. This was mainly because I didn't have the proper background when I started and I didn't have the right resources at my disposal. These two things are very important and one of two things is likely to happen if you don't have them: (1) it will take you so long that you'll get fed up and give up; or (2) you'll become a crank (and believe me, there are a ton of cranks out there selling crypto products).

When devising and implementing your strategy, you should keep these outcomes in mind because it will be very important to avoid them at all costs.

## How to Do It

The best strategy for learning crypto design and theory is to get a Ph.D. at a University with a cryptography group. Getting a Ph.D. in some random field like mechanical engineering or biology does not count! If you are interested in symmetric cryptography (i.e., block cipher and hash function design and cryptanalysis), then a good place to start are European Universities since a large fraction of the experts are there. If you're interested in crypto theory then the US or Israel. Of course there are strong groups in each area everywhere.

If you have found a University and are trying to evaluate the group is, then a *very rough* sanity check is to look at their publication record. If this is a theory group then you should be looking for CRYPTO, Eurocrypt, Asiacrypt, TCC, FOCS, STOC publications. If this is a more applied group, then you should be looking for publications at CCS, CHES, IEEE Security and Privacy (also known as Oakland) and Usenix Security. CRYPTO, Eurocrypt and Asiacrypt are not particularly good indicators of quality for applied crypto. If this is a symmetric crypto and cryptanalysis group then you should look for papers at Fast Software Encryption (FSE) and Selected Areas in Cryptography (SAC). Similarly to applied crypto, CRYPTO, Eurocrypt and Asiacrypt are not necessarily good indicators of quality in this area.

But you shouldn't get too caught up in this, however. The publication system in cryptography is screwed up so you shouldn't necessarily dismiss group $$A$$ because it has less STOC papers than group $$B$$; or less CCS papers than group $$C$$. This is just a very coarse metric that---absent of any other signals---can be used to distinguish between very good groups and very bad ones. Another good thing to check is where the students that graduate from that group end up. Do they end up with jobs that you would like?

So why is getting a Ph.D. from a good group the best strategy? Simply because it is the most efficient way to learn the material. The background needed for crypto is not part of a traditional education, neither in math nor in computer science, so it's unlikely that you'll have learned what you need in undergrad. So you have two choices: (1) learn it on you own; or (2) learn it in graduate school.

In grad school you will have a set of classes carefully chosen and prepared for you. You'll have an advisor that will guide you through the process, telling you what you need to learn, what you don't need to learn, what your weaknesses are, what you need to improve, what problems to work on and the best strategies to solve those problems. You'll also have fellow students that will help and motivate you throughout.

Note that for most Ph.D. programs in computer science you don't have to pay anything. Your tuition is taken care of by the department or by your advisor's grants. In addition, you receive a stipend which takes care of housing, food etc. So if you're in a position to devote $$5$$ years of your life to learning cryptography, then I think grad school in a crypto group is by far the best strategy.

## How Not to Do It

So you can't go to grad school or you can but somewhere without a crypto group and you still really want to learn crypto design and theory. Here is one possible strategy---the one I used.

I'll assume you have a standard systems-focused computer science undergrad degree. In my case, for example, I had a strong systems background in undergrad (e.g., compilers, OS, networking, architecture) and a very weak theory background (just calculus, intro to algorithms and a linear algebra class so bad no one ever attended). To be brutally honest, this kind of background is useless for cryptography and if this is the point at which you're at then you have to understand that you'll be starting from scratch.

There are three things you should be shooting for: (1) developing mathematical maturity; $$(2)$$ learning how to debug; (3) acquiring the basics.

By mathematical maturity, I mean the ability to understand and use basic mathematical language, notation and concepts. It's basically having the right context in place for doing math. Knowing how to parse mathematical statements and proofs and generally-speaking, knowing how to read between the lines and how to fill in the missing pieces.

By debugging, what I mean is that you have to get to a point where you can reliably tell whether you have fully understood some idea or not. When you are starting out and working alone, this is extremely difficult especially for an area like cryptography which can be so subtle. If you don't acquire this skill, however, you will end up a crank: that is, someone that has read a lot, understood very little, and is completely unaware of how confused and wrong they are. Many people who are self-taught end up like this so you have to be careful.

The problem with most of the advice given for learning a hard subject is that they focus on the third stage; typically by pointing to papers or books. But papers and books are useless if you don't have the first two skills.

## Acquiring Mathematical Maturity

Of course, the easiest way to acquire mathematical maturity is to get an undergraduate education in math. [^1]

Maturity is probably the skill that takes the longest to acquire. Math and theoretical areas of computer science are expressed through definitions, theorems and proofs. A definition is a precise description of some object or process. A theorem is a precise statement concerning some object or process and a proof is an argument as to why the statement is true. You should be comfortable with this paradigm because everything you will see further down the line will be expressed this way. But understanding this paradigm means you'll have to be comfortable with basic notions like quantifiers (i.e., existential and universal), basic proof structures (e.g., direct and by contradiction), basic logic, elementary probability, etc.

By comfortable, I don't mean a casual, superficial understanding of these things. What I mean is you should be able to properly formulate definitions, theorem statements and proofs yourself and be able understand why some formulations are better than others.

You shouldn't think of mathematical formalisms as pedantic, boring and academic. Yes, in some cases they can be overkill because you may have a good intuitive understanding of an idea, but there will be times where your intuition fails and that's when having a good grasp of the formal approach will help you. Cryptography, in particular, is very unintuitive so formalism is even more important---especially when you are starting out.

Most books on cryptography will not help you acquire mathematical maturity because it is assumed that the reader has it. If you are coming from a purely systems background though, you may not have had the opportunity to develop it (as was my case, for example). And reading math books is usually even worse since mathematicians learn this stuff very early on.

So what can you do? The approach I took was to just read everything I could find in math, theoretical computer science and cryptography. Once in a while, I would get lucky and find a paper with a decent explanation of some basic concept (e.g., some basic probability argument or a slightly more detailed proof structure) but most of the time I had to reconstruct the missing the pieces and context on my own.

Obviously, this is easy to do when you have the basics but it is incredibly difficult and frustrating when you don't. As you can imagine it took forever to fill in the gaps in my knowledge. Therefore, the ideal approach would be to find a book or lecture notes that focus on this stuff. And---luckily for you---Timothy Gowers has written an excellent series of blog posts on these very things so you should read them:

1. Basic Logic
 1. [And & Or](http://gowers.wordpress.com/2011/09/25/basic-logic-connectives-and-and-or/)
 2. [Not](http://gowers.wordpress.com/2011/09/26/basic-logic-connectives-not/)
 3. [Implies](http://gowers.wordpress.com/2011/09/28/basic-logic-connectives-implies/)
 4. [Quantifiers](http://gowers.wordpress.com/2011/09/30/basic-logic-quantifiers/)
 5. [Negation](http://gowers.wordpress.com/2011/10/02/basic-logic-relationships-between-statements-negation/)
 6. [Converse and contrapositive](http://gowers.wordpress.com/2011/10/05/basic-logic-relationships-between-statements-converses-and-contrapositives/)
 7. [Handling variables](http://gowers.wordpress.com/2011/10/07/basic-logic-tips-for-handling-variables/)
 8. [Summary](http://gowers.wordpress.com/2011/10/09/basic-logic-summary/)
2. Functions
 1. [Injections, surjections, etc.](http://gowers.wordpress.com/2011/10/11/injections-surjections-and-all-that/)
 2. [Co-domains, ranges, images](http://gowers.wordpress.com/2011/10/13/domains-codomains-ranges-images-preimages-inverse-images/)
3. [Permutations](http://gowers.wordpress.com/2011/10/16/permutations/)
4. Definitions
 1. [Definitions](http://gowers.wordpress.com/2011/10/23/definitions/)
 2. [Alternative definitions](http://gowers.wordpress.com/2011/10/25/alternative-definitions/)
5. [Equivalence relations](http://gowers.wordpress.com/2011/10/30/equivalence-relations/)

## Debugging

Being able to detect whether you've made a mistake is an important and difficult skill to acquire in any subject. This is exacerbated in security and cryptography since we cannot ascertain the security of something experimentally. Luckily, in crypto we do have a methodology for debugging: namely, *provable security*. The provable security paradigm (or more appropriately, the reductionist paradigm) consists of the following steps. One first formulates a security definition that captures the security properties/guarantees that are expected from the system. Then, one describes a cryptographic scheme/protocol for the problem at hand. Finally, one proves that the scheme/protocol satisfies the security definition (usually, under some assumption).

The provable security paradigm originated in the 80s' and has been used ever since in the cryptography community to analyze the security of many primitives. There are many benefits to this paradigm but one of the main ones is that it is a great debugging tool. When trying to prove the security of your primitive, you will sometimes find that the proof will not go through for some reason and, more often than not, it is because of a subtle weakness in your protocol that you did not pick up when first designing it.

I want to stress that the provable security paradigm is not foolproof and that it has its limits. For example, there are entire areas of cryptography like block cipher and hash function design where its usefulness has, historically, been very limited. Also, problems can occur if the definition being used is wrong or too weak for the application being considered. And, of course, there could be errors in the proofs of security. So the framework should be used with these limitations in mind because a blind adherence to it could lead you astray.

In my opinion the best place to start learning the provable security paradigm (and crypto in general) is the textbook [*Introduction to Modern Cryptography*](http://www.amazon.com/Introduction-Cryptography-Chapman-Network-Security/dp/1466570261/ref=sr_1_1?ie=UTF8&qid=1415685096&sr=8-1&keywords=katz+lindell) by Jonathan Katz and Yehuda Lindell. I really wish this book was out when I was learning crypto because it would have saved me a huge amount of time. The book teaches you all the basics of cryptography while explaining how security definitions work and how to prove various constructions secure. Unlike many mathematically-inclined books it goes over the details of proofs and doesn't just leave everything as an exercise (which can be incredibly frustrating for people who are trying to learn the material alone and without any background). After Katz-Lindell, I would recommend *Foundations of Cryptography* Vol. [1](http://www.amazon.com/Foundations-Cryptography-1-Basic-Tools/dp/0521035368/ref=sr_1_2?ie=UTF8&qid=1415685162&sr=8-2&keywords=oded+goldreich) and [2](http://www.amazon.com/Foundations-Cryptography-Volume-Basic-Applications/dp/052111991X/ref=pd_bxgy_b_img_y)" by Oded Goldreich. These texts, however, are a *lot* more advanced and you likely won't need the material unless you are doing research.

## Learning the Basics

Of course, another crucial step is learning the basics. The simplest thing to do here is to just read Katz-Lindell. In addition you can also watch Jonathan Katz' and Dan Boneh's MOOCS which are [here](https://www.coursera.org/course/cryptography) and [here](https://www.coursera.org/course/crypto), respectively.

## Putting it All Together

So you've read Timothy Gowers' blog posts and acquired the basic mathematical concepts, you've read Katz-Lindell and understood the basics of provably security and you've watched the MOOCs so you know all the basic cryptographic primitives and what they are used for. At this point you should be able to read crypto papers and follow along. What you may not be able to do, however, is design and analyze your own crypto protocols.

To make the jump from understanding other people's work to creating your own, I think the only thing you can really do is to formulate your own problem and try to solve do it. Whether you succeed is not important, what matters is that you will be applying everything you learned at once and this will force you to understand how these ideas relate to each other and interact.

While I think it's a good idea to work on your own problems at this stage to gain experience in applying what you've learned, it is very important to keep in mind that *you don't know what you're doing yet*. In particular, you may have gained a false sense of confidence after reading the books and watching the MOOCs so if you're not careful you'll be headed down the path of crankdom. To avoid this, it is crucial that you get feedback on your ideas from people who are more experienced than you. This is not an option, it is crucial! [^2]

But how do you get experts to give you feedback if you don't know any? This is a difficult question that I faced as well at one point. Here's the trick I used. I basically got to the point where I could hold a semi-intelligent conversation with a professional cryptographer. This does not mean that I could impress them. Just that I knew enough of the basic concepts and techniques that I could have a reasonable $$10$$ minute conversation about some crypto paper I had read. Once I could do this, I tried my luck. For example, I attended crypto seminars at Universities close by. This lead to me talking about research with professors there and eventually starting to work on projects together.

What is important to realize here is that people---especially successful people---are very busy and they just don't have the time to teach you cryptography. If they are professors, then they already have students they are working with and if they work in industry then they have interns and an employer they are committed to. So if you want to learn from them you should have something to offer.

But what can you offer if you are just starting out? Well, if you think about it you have one thing that they don't: namely, *time*. Remember that these experts are very busy so they probably have a ton of project ideas they would like to work on but that will never see the light of day. What you can offer to them is your time. You can start by implementing their ideas and evaluating them experimentally (this is assuming you have a strong engineering background). By doing this you are providing value to them and, most importantly, you get a chance to demonstrate that you have a good work ethic, that you are committed and that you are easy to work with. On your end, you will learn and internalize their ideas better and put yourself in a position to possibly improve upon them. Once you have a good working relationship and some preliminary ideas on how to improve their work, you are well on your way.

## Conclusions

So these were my high-level strategies for learning cryptography. If you can, just get a Ph.D. at a place with a good crypto group (remember that Ph.D.'s in computer science are effectively free). If you really can't do that for some reason, then you can try out the second strategy I outlined. But you should realize that it will be painful.

Good luck!


[^1]: A math education will teach you the building blocks from which most cryptographic protocols are built (e.g., number theory, algebra etc.) but it won't teach you specifically how to design crypto primitives and protocols or how to understand and analyze their security.

[^2]: At one point when I was just starting to learn crypto I wrote up some ideas I had. Someone I knew agreed to do an introduction with a well-known cryptographer so I could send him my ideas. After reading my ideas, he (very politely) told me that what I was doing made no sense, explained why and then (again very politely) proceeded to explain why working together would be too difficult given the stage at which I was. This was one (by far) of the most important stages in my development. This small feedback that he provided made me realize that I had acquired a false sense of confidence and that I still had a *huge* amount of work to do! Looking back, this was invaluable and I'm grateful to him to this day.
