---
layout: archived-post
title: "Is the NSA Metadata Program Legal?"
date: 2014-04-29
categories: [Policy]
slug: is-the-nsa-metadata-program-legal
source: https://esl.cs.brown.edu/blog/is-the-nsa-metadata-program-legal/
tags: [FISA, NSA, Section 215, Metadata]
---

![](/assets/img/esl/justice.jpg)

 One of the most interesting aspects of the NSA metadata program is whether it is legal or not. Unlike the questions we usually think about in computer science, this question has no definitive answer. The program is legal in some sense, but the logic needed for the argument to go through is so questionable that you could just as well say that it's not.

Recall that the program requires telephone providers to hand to the NSA (each day) the metadata of every US-to-foreign, foreign-to-US and US-to-US call. This metadata consists of the origin and destination numbers, the time and duration of the call, the international mobile subscriber identity (IMSI) number, the trunk identifier and telephone calling card numbers. This data is stored and queried by the NSA and each record has to be deleted after 5 years.

I had decided to include a high-level overview of this question in an invited paper I wrote for the [Workshop on Applied Homomorphic Cryptography](http://www.dcsec.uni-hannover.de/wahc14.html) but I had to take it out due to space restrictions. Even though I'll eventually include the overview in the full version of the paper, in the meantime, I thought it might make for a useful blog post; especially for computer scientists who are curious about the legal aspects of this issue but don't have the background to make sense of it.

The question of whether the NSA metadata program is legal reduces to the following two questions: (1) does the program violate the Fourth Amendment of the US Constitution?; and (2) is the program compliant with the amendments to the Foreign Intelligence Surveillance Act (FISA) put forth in the USA PATRIOT Act of 2001 which, in the Government's view, authorize this program.

## Does it Violate the Fourth Amendment?

The [Fourth Amendment](https://en.wikipedia.org/wiki/Fourth_Amendment_to_the_United_States_Constitution) protects the privacy of American citizens. The Amendment states:

> The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.

Roughly speaking, it protects citizens against unreasonable search and seizures by requiring the Government to obtain a warrant supported by probable cause from an independent [magistrate](https://en.wikipedia.org/wiki/Magistrate#United_States).

Historically, courts tended to limit the protections of the Fourth Amendment to a person's physical property, including their home and personal effects, but in 1967, in [Katz v. United States](https://en.wikipedia.org/wiki/Katz_v_United_States), the Supreme Court greatly widened the scope of the Fourth Amendment. In particular, the Court decided that Fourth Amendment protections apply to "people, not places" and that a person is afforded protection as long as they have a "reasonable expectation of privacy" in the items or location to be searched.

Warrantless searches are per se unreasonable under the Fourth Amendment, unless they fall within a recognized exception. Given that a warrant embodies the notion of of "reasonableness" under the Fourth Amendment, the Government would bear a heavy burden to explain exactly how the metadata program---which collects metadata on individuals without a warrant---involves a "reasonable" search under the Fourth Amendment.

Following Katz v. United States, however, there were two important cases that solidified what is now known as the third party doctrine, which holds that Fourth Amendment protections do not apply to information that is voluntarily disclosed to a third party since there is then *no reasonable expectation of privacy with respect to such information*. These Supreme Court decisions were [United States v. Miller](https://en.wikipedia.org/wiki/United_States_v_Miller) in 1976 and [Smith v. Maryland](https://en.wikipedia.org/wiki/Smith_v_Maryland) in 1979. In the Miller decision, the Supreme Court ruled that the Government did not violate the Fourth Amendment by obtaining Miller's bank records without a warrant. In the Smith decision, the Court found no Fourth Amendment violation when the Government obtained records of phone numbers dialed by Smith from the phone company without a warrant. Though these decisions were issued in the 1970's and concerned bank records and telephone companies, an argument could be made that the third party doctrine also extends to ISPs, mobile networks and cloud providers.

So in light of the third party doctrine, the warrantless collection of metadata on (potentially) every American may not violate the Fourth Amendment, because such metadata has been voluntarily provided by users to their service providers.

This issue is highly controversial, however, and at least [one judge](http://en.wikipedia.org/wiki/Richard_J._Leon) has found that the scale of the program and the massive technological changes that have occurred in the last 30 years mean that the Miller and Smith decisions are not necessarily controlling (i.e., completely binding).

## Is it Compliant with the FISA/PATRIOT Act?

The second question is whether the program exceeds the scope of [Section 215](http://en.wikipedia.org/wiki/Section_summary_of_the_Patriot_Act,_Title_II#Section_215:_Access_to_records_and_other_items_under_FISA) of the [PATRIOT Act](http://en.wikipedia.org/wiki/Patriot_act), which amended Section 501 of the [Foreign Intelligence Surveillance Act](http://en.wikipedia.org/wiki/FISA) (FISA).

FISA is a law from 1978 that prescribes how the Government can conduct domestic surveillance for national security-related investigations. The law was initially passed to curb the domestic surveillance activities of the Government which included abuses such as [Watergate](http://en.wikipedia.org/wiki/Watergate), as well as the FBI [COINTELPRO](http://en.wikipedia.org/wiki/Cointel_Pro) and the NSA [MINARET](https://en.wikipedia.org/wiki/Project_MINARET) programs.

One of the law's provisions was to create a court, referred to as the [FISA](http://en.wikipedia.org/wiki/FISA_Court), which was assigned the role of providing judicial oversight over the Government's domestic surveillance activities in national security-related investigations. To protect national security, public visibility into the court's activities was limited. [^1]

FISA has been amended several times since its introduction but perhaps the most controversial amendment was in Section 215 of the USA PATRIOT Act of 2001. Roughly speaking, Section 215 allows the Government to compel a third-party provider---without a warrant---to hand over "business records" about a customer "if there are reasonable grounds to believe that the tangible things sought are relevant to an authorized investigation".

Part of the argument for the legality of the NSA metadata program rests on the meaning of the term relevant. Indeed, as explained in a [declassified opinion](https://www.aclu.org/files/natsec/nsa/br13-09-primary-order.pdf) from the FISA Court, the court decided to interpret the term "relevant" to mean bearing upon or being pertinent to an investigation, as opposed to directly related to a specific investigation target (e.g., the records of the specific individual being investigated).

The former interpretation of "relevant" combined with submissions from the NSA that their investigative tools required the metadata of all customers in order to work properly in any investigation, led the FISA court to hold that the program is legal.


[^1]: If you're curious about the FISA court and, especially about what it's door looks like, see this [post](https://konklone.com/post/the-door-to-the-fisa-court) by Eric Mill.
