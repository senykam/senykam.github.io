---
layout: post
title: "Notes on Power #1: Power Systems"
short_title: Power Systems
description: 
date: 2026-07-26
permalink: /power/notes/power-systems/
kind: note
project: power
series_order: 1
related_posts: false
---

In my [last post](https://senykamara.substack.com/p/what-is-power), I described a situation that highlighted the difference between acting inside a system and controlling it. That was an informal distinction and in this post I want to try to make it more formal. I will define *power systems* and apply the definition to two situations: a robbery and a job. The claim is that power is control over the rules of a process and over whether it runs at all, and that how much power someone holds is a matter of what they *could* bring about, not of the outcomes they bring about.  

## Coercion

When we think about power, coercion is usually what first comes to mind. A threat backed by force is the most familiar form of power, so it is also a good place to start. The standard example of coercion in legal philosophy is from H.L.A. Hart's book *The Concept of Law*. In it, a gunman walks into a bank and tells the clerk to hand over the money or be shot. In the plainest sense of the word, the gunman has power over the clerk because he can make the clerk hand over the money. But that description is not quite right; or rather, it is too simplistic. The gunman cannot really *make* the clerk hand over anything because the clerk can refuse. What is happening is more specific. The gunman has determined what the clerk can and cannot do in this encounter because he has attached consequences to its actions: hand over the money and the gunman leaves or refuse and get shot.

But the gunman has also done something more basic because before he walked in, there was no robbery. He created that situation and put the clerk in it. So the gunman had several distinct abilities. He initiated the encounter, he chose the clerk to take part in it, he determined the clerk's possible actions and he set the consequences of those actions. The clerk did the only thing left to do and chose among the options the gunman fixed.

Each of these abilities is a form of *power* over the encounter: an ability to determine some part of it. These powers are distinct, and an agent could hold any one of them without the others. The power to decide who is in the encounter is not the same as the power to set its consequences, and neither is the power to fix what the participants can and cannot do. But what they do have in common is that they *control* some part of the process that is unfolding.

## Power Systems

For our purposes, we can model the encounter as a state machine together with functions that determine who participates, what consequences actions have and what the participants see. We can further model each of the gunman's abilities as control over one of these functions in the sense of having the ability to replace it. Power over a process will then be the ability to replace one of its parts or to initiate its execution.

We will refer to these processes as *power systems*. A power system among agents $$\mathcal{N}_1, \dots, \mathcal{N}_n$$ is a pair $$\mathsf{Sys} = (\Pi, \mathcal{S})$$ composed of a *process* $$\Pi$$, which captures the components of the system and the rules according to which it unfolds, and of a *power structure* $$\mathcal{S}$$, which determines which agents control which of those components.

**States.** The encounter runs over a state space

$$\Sigma = \{st_0\} \cup \Sigma_I \cup \Sigma_F$$

with an initial state $$st_0$$, intermediate states $$\Sigma_I$$ and final states $$\Sigma_F$$. It begins at $$st_0$$, advances one round at a time and halts once it reaches a final state. In the robbery example, $$st_0$$ is the situation the gunman creates when he makes his demand, and the final states are the ways it can end.

**Actions and reactions.** In each round, every agent chooses an action from its own action set $$A_i$$, and these choices together form an action vector in the action space $$\bar{A} = A_1 \times \cdots \times A_n$$. Each $$A_i$$ contains a distinguished null action $$\bot_i$$ so that an agent that does nothing in a round still contributes a coordinate. What the agents do has consequences, and we collect that into a reaction vector in the reaction space $$\bar{R} = R_1 \times \cdots \times R_n$$. More precisely, a reaction function

$$\mathsf{rct} : \bar{A} \to \bar{R}$$

maps each action vector to the reactions that follow from it. This is the component that attaches consequences to actions. 

**How the state advances.** Given a round's actions and the reactions to them, a transition function

$$\mathsf{trns} : \Sigma \times \bar{A} \times \bar{R} \to \Sigma$$

determines the next state. Because it determines which state follows each round, the transition function also determines when the process reaches a final state and therefore how long the encounter lasts.

**How it ends.** Once the process reaches a final state, an output function

$$\mathsf{out} : \Sigma_F \to \bar{O}$$

assigns an outcome to each agent, where $$\bar{O} = O_1 \times \cdots \times O_n$$ is the outcome space. The clerk's outcome in the robbery is whether it keeps the money  or whether it is harmed.

**Who takes part.** Not every agent is in every encounter, so an admission function

$$\mathsf{adm} : \{\mathcal{N}_1,\dots,\mathcal{N}_n\} \to \{0,1\}$$

determines which agents participate. The gunman exercised control over this component when he selected the clerk rather than someone else in the bank.

**What participants see.** In the model, agents do not perceive a round directly. An observation function

$$\mathsf{obs} : \bar{R} \to \bar{Y}$$

maps reaction vectors to observation vectors, and each admitted agent receives its own coordinate of that vector. Notice that, since $$\mathsf{obs}$$ is applied to reactions rather than to actions, the things an agent learns about what anyone did is determined by the system itself rather than the framework. 

**What the agents want.** Each agent evaluates the outcome it receives through a utility function

$$\mathsf{util}_i : \bar{O} \to \mathbb{R}$$

that maps outcome vectors to real-valued payoffs. Our framework treats these functions as components of the process itself rather than as exogenous data. This allows agents to replace them, which captures the ability of one agent to change what another agent wants. 

**The process.** The process is therefore

$$\Pi = (\Sigma, \mathsf{trns}, \mathsf{out}, \mathsf{adm}, \mathsf{rct}, \mathsf{obs}, \overline{\mathsf{util}}),$$

where $$\overline{\mathsf{util}} = (\mathsf{util}_1, \dots, \mathsf{util}_n)$$. Its state machine is $$(\Sigma, \mathsf{trns}, \mathsf{out})$$ and its component functions are $$(\mathsf{adm}, \mathsf{rct}, \mathsf{obs}, \mathsf{util}_1, \dots, \mathsf{util}_n)$$, each of which determines one aspect of the encounter.

**Powers.** An agent controls a component of the process if it has the authority to replace that component's function with an alternative. Not every alternative is available, so each power carries the set of functions its holder may choose from. A power

$$\mathfrak{p} = (\mathsf{dom}_{\mathfrak{p}}, \mathsf{cod}_{\mathfrak{p}}, \Phi_{\mathfrak{p}})$$

consists of a domain $$\mathsf{dom}_{\mathfrak{p}}$$, a codomain $$\mathsf{cod}_{\mathfrak{p}}$$ and a replacement set $$\Phi_{\mathfrak{p}}$$ whose members all have that domain and codomain. The domain and codomain specify the type of function the power can replace, and $$\Phi_{\mathfrak{p}}$$ specifies which functions of that type are admissible.

**First-order and second-order powers.** Our framework distinguishes two kinds of power and collects them in a power set $$\mathfrak{P} = \mathfrak{P}_1 \cup \mathfrak{P}_2$$. The *first-order powers*

$$\mathfrak{P}_1 = \{\mathfrak{p}_{\mathsf{adm}}, \mathfrak{p}_{\mathsf{str}}, \mathfrak{p}_{\mathsf{rct}}, \mathfrak{p}_{\mathsf{obs}}\}$$

control the components that determine how the encounter runs, and consist of admission power, structural power, reaction power and observational power. The *second-order powers*

$$\mathfrak{P}_2 = \{\mathfrak{p}_{\mathsf{alc}}, \mathfrak{p}_{\mathsf{cog},1}, \dots, \mathfrak{p}_{\mathsf{cog},n}\}$$

consist of allocation power and of a cognitive power for each agent. A cognitive power $$\mathfrak{p}_{\mathsf{cog},i}$$ controls $$\mathsf{util}_i$$ and therefore the preferences under which $$\mathcal{N}_i$$ evaluates its outcome, whereas allocation power $$\mathfrak{p}_{\mathsf{alc}}$$ controls which agents hold which powers.

**Allocation and control.** Two further functions specify who holds each power and which component it controls. An allocation function

$$\mathsf{alc} : \{\mathcal{N}_1,\dots,\mathcal{N}_n\} \to 2^{\mathfrak{P}}$$

maps each agent to the set of powers it holds, and no power can be held by more than one agent, though a power can be held by none. A control map $$\chi$$ then maps each power to the component function it controls: $$\mathfrak{p}_{\mathsf{adm}} \mapsto \mathsf{adm}$$, $$\mathfrak{p}_{\mathsf{str}} \mapsto \mathsf{trns}$$, $$\mathfrak{p}_{\mathsf{rct}} \mapsto \mathsf{rct}$$, $$\mathfrak{p}_{\mathsf{obs}} \mapsto \mathsf{obs}$$, $$\mathfrak{p}_{\mathsf{cog},i} \mapsto \mathsf{util}_i$$ and $$\mathfrak{p}_{\mathsf{alc}} \mapsto \mathsf{alc}$$. An agent that holds a power $$\mathfrak{p}$$ exercises it by replacing $$\chi(\mathfrak{p})$$ with a function of its choice from $$\Phi_{\mathfrak{p}}$$.

**The power structure.** The power structure is therefore

$$\mathcal{S} = (\mathfrak{P}, \mathsf{alc}, \chi),$$

which specifies what can be replaced, who may replace it and which component each power controls.

## The Robbery as a Power System

**The gunman's powers.** In the robbery, the agents are the gunman and the clerk. The gunman's ability to decide that the clerk will take part in the encounter is admission power, which is the authority to replace $$\mathsf{adm}$$. His threat appears in the model as the reaction function, which maps the "handing over the money" action to the "clerk loses the money and lives" reaction, and the "refusal" action to the "clerk loses both" reaction. The gunman's ability to attach these consequences is reaction power, which is the authority to replace $$\mathsf{rct}$$. The transition function determines how the encounter proceeds and when it ends, and the gunman's control over how it unfolds is structural power, which is the authority to replace $$\mathsf{trns}$$.

**The remaining components.** There is no power over the action space $$\bar{A}$$ because $$\bar{A}$$ is the domain of the reaction and transition functions, so an agent that can replace those functions already determines how the process responds to every action. The clerk's utility function $$\mathsf{util}_{\text{clerk}}$$ captures the clerk's preferences. Note that the gunman relies on the clerk's utility function since the threat works only if the clerk values its life over money. In a robbery, the observation function is simple because every agent can see everything that happens.

**The power structure.** The power structure of this example is simple. The gunman holds

$$\mathsf{alc}(\text{gunman}) = \{\mathfrak{p}_{\mathsf{adm}}, \mathfrak{p}_{\mathsf{str}}, \mathfrak{p}_{\mathsf{rct}}\}$$

and the clerk holds nothing; that is, $$\mathsf{alc}(\text{clerk}) = \emptyset$$. This is how the framework models being subject to a system. The clerk can act inside the process, but there is nothing about it that it can control.

**Initiation.** We have now modeled three of the gunman's four abilities but not his ability to start the robbery. Starting the robbery cannot come about by replacing of any component, so none of the powers we have defined captures it. To model it properly, it is important to notice that the robbery does not run on its own. It runs inside a larger system that models the ordinary operation of the bank. In that larger system, starting the robbery is an action that moves the system from a state in which there is no robbery to a state in which the robbery is occurring. We refer to the ability to start a system from the outside as *initiation power*. It is power over the robbery even though it doesn't replace any part of it. We will define it formally in a later post, after we formalize systems that run inside other systems; until then, we count it as the fourth of the gunman's powers.

## How a System Runs

A power system as we have defined it is a static object, but it is meant to model a process that unfolds so we also have to define how a system runs. A run has two phases: a replacement phase in which the agents change the system and an execution phase in which the changed system runs as a machine.

**The replacement phase.** During the replacement phase, the agents exercise their powers  by replacing the component functions they control. The result is the system that will actually govern the encounter. The powers are exercised in a fixed order: allocation power first, since replacing $$\mathsf{alc}$$ changes who holds the other powers; the cognitive powers second, which determines the utility functions; and the first-order powers last. The components that are not replaced keep their defaults. We write $$\mathsf{Sys}^+$$ for the resulting system and $$\mathsf{adm}^+$$, $$\mathsf{rct}^+$$, $$\mathsf{trns}^+$$, $$\mathsf{obs}^+$$ and $$\overline{\mathsf{util}}^+$$ for its components.

**The execution phase.** The execution phase starts at the initial state $$st_0$$ and proceeds in rounds. In each round, every admitted agent---every $$\mathcal{N}_i$$ such that $$\mathsf{adm}^+(\mathcal{N}_i) = 1$$---chooses an action from its action set $$A_i$$, and every agent that is not admitted is assigned $$\bot_i$$. Together these form the action vector $$\bar{a}$$ and the process computes the reactions

$$\bar{r} := \mathsf{rct}^+(\bar{a}),$$

advances the state to

$$st_{t+1} := \mathsf{trns}^+(st_t, \bar{a}, \bar{r}),$$

and computes the observations

$$\bar{y} := \mathsf{obs}^+(\bar{r}).$$

Each admitted agent $$\mathcal{N}_i$$ then receives its observation $$y_i$$. When the state is final, the process outputs the outcome vector $$\bar{o} := \mathsf{out}(st_{t+1})$$, each agent receives its payoff $$\mathsf{util}_i^+(\bar{o})$$ and the process halts.

Notice that the gunman's power is exercised entirely in the replacement phase. Once he has walked in and made his demand, the system is in place and what remains for the clerk is to act inside it.

## What Power Is Not

Two features of the robbery could be mistaken for the gunman's power: the outcome and the gun.

**Power is not the outcome.** Note that we haven't discussed how to determine how much power an agent holds. A natural answer to this question is to focus on the outcomes of the system. In our example, this would be the idea that the gunman has power over the clerk because he walked away with the money. But the outcome is not produced by the gunman alone. The clerk's utility function is a component the gunman does not control and relies on. He set the consequences of the clerk's actions so that, given the clerk's preferences, handing over the money is the clerk's best choice. The outcome of the robbery is therefore produced jointly by the components the gunman set and by the choice the clerk makes in response.

Since outcomes are produced jointly, they reflect the clerk's choices as much as
the gunman's control. If a clerk refuses and is shot, the gunman's control is
the same as what it was a moment earlier; it just met a different response. If we
determined power from outcomes, the gunman would hold less power over a clerk
that refuses than over a clerk that complies, even though the encounters differ
only in the actions the clerks chose. An outcome describes how one encounter went,
whereas, in our framework, power is what its holder can determine. More precisely, the gunman's powers determine a whole set of possible encounters, since each way of exercising them produces a different one, and the outcome describes only the encounter that occurred.

**Power is not the gun.** Nothing in this analysis depends on the gun. The same structure appears whenever an agent controls a process that others act inside, and in most cases the control is legal and ordinary. Consider your job. Your employer cannot make you do anything, just as the gunman cannot make the clerk hand over the money. But your employer decides who is hired, sets the consequences of what you do at work (e.g., raises, write-ups and dismissal) and determines what is monitored and recorded about your work. In our model, the employer holds admission power, reaction power and observational power over the employment process, and it holds them through the employment contract and the law instead of through a weapon. You can act inside the process and you can leave it, but you cannot change its components.

## Observation

One line of the execution rules is a deliberate modeling choice, and it
determines what agents inside the system can know. Specifically, notice that
observations are computed from reactions,

$$\bar{y} = \mathsf{obs}(\mathsf{rct}(\bar{a})),$$

never from the actions themselves. In other words, no participant perceives an action directly, not even the reaction to its own action. Everything an agent learns, it learns through $$\mathsf{obs}$$ and $$\mathsf{obs}$$ is applied to reactions not to actions.

**Visibility is a property of the system.** To see this, fix the actions of every agent except $$\mathcal{N}_i$$. We'll write this as $$\bar{a}_{-i}$$ and write $$(a_i, \bar{a}_{-i})$$ for the action vector in which $$\mathcal{N}_i$$ chooses $$a_i$$ and the other agents choose $$\bar{a}_{-i}$$. Now consider what another agent $$\mathcal{N}_j$$ can learn about what $$\mathcal{N}_i$$ did. Under our setup, information about the action $$a_i$$ reaches $$\mathcal{N}_j$$ only if the function

$$f_{\bar{a}_{-i}}(a_i) = \big(\mathsf{obs}(\mathsf{rct}(a_i, \bar{a}_{-i}))\big)_j$$

is non-constant, and $$\mathcal{N}_j$$'s observation determines $$a_i$$ if $$f_{\bar{a}_{-i}}$$ is injective. Both conditions depend on the pair $$(\mathsf{rct}, \mathsf{obs})$$ and vary from system to system, so what can be seen in a system is determined by the system rather than by the framework. In a mail service, where $$\mathsf{rct}$$ delivers your message to the recipient and $$\mathsf{obs}$$ shows the recipient what arrived, the function is injective and the recipient knows what was sent. If instead two actions produce the same reactions, no observation function can tell them apart because the difference between them does not appear in the reaction vector that $$\mathsf{obs}$$ is applied to. A consequence can even attach to an agent without it being shown to the agent, since knowledge of a reaction passes through $$\mathsf{obs}$$. 

**Reaction power is two abilities in one.** Notice also that reaction power has a material side that determines what happens to the participants and an epistemic side that determines what can be known about what happened. Control over reactions includes control over evidence. A process can punish and leave no record, mislabel one act as another or deliver a faithful copy and which of these it does is determined by components someone controls. If participants perceived actions directly, evidence could not be manipulated and the institutions whose power consists of controlling what is known could not be modeled. Observational power, which is the power over $$\mathsf{obs}$$ itself, will be discussed in the next post.

## Conclusion

A power system $$\mathsf{Sys} = (\Pi, \mathcal{S})$$ is a process with replaceable components together with a power structure that specifies who can replace each of them. A run of the system includes a replacement phase followed by an execution phase, and observations are computed from reactions rather than from actions. Three features of power appeared in both the robbery and the job examples: (1) power is plural, since it consists of distinct abilities that can be held separately; (2) power is counterfactual, since how much of it an agent holds depends on what the agent *could* bring about rather than on what it is seen to do; and (3) power is exercised before actions, since the replacement phase precedes the execution phase, which is also why the outcome of an encounter does not reveal the power dynamics behind it.

The next post will focus on observational power and the power span, which is the set of systems that an agent can bring about by exercising its powers and which lets us compare how much power an agent holds.
