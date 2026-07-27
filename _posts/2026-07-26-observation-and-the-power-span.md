---
layout: post
title: "Notes on Power #2: Observation and the Power Span"
short_title: Observation and the Power Span
description:
date: 2026-07-26 12:00:00
permalink: /power/notes/observation-and-the-power-span/
kind: note
project: power
series_order: 2
related_posts: false
---

In my [last post](/power/notes/power-systems/), I defined power systems and the rules by which they run. That post left two things open. It claimed that how much power an agent holds is a matter of what the agent *could* bring about rather than what it is seen to do, but it did not make that precise. It also introduced the observation function and showed that what an agent can learn is determined by the reaction and observation functions together, but it neither classified systems by what their participants can know nor defined the power over what they see. We first classify systems by what their participants can see and know, and we then define the *power span* of an agent, which is the set of systems the agent can produce by exercising its powers.

## Four Kinds of Systems

Recall how observations are produced. In each round of an execution, the reaction function is applied to the round's actions and, in turn, the observation function is applied to the reactions. Each agent $$\mathcal{N}_i$$, therefore, receives the observation $$y_i = \big(\mathsf{obs}(\mathsf{rct}(\bar{a}))\big)_i$$. What an agent can know about the actions of others, and about the reactions to its own actions, is therefore determined by the pair $$(\mathsf{rct}, \mathsf{obs})$$, and different pairs produce different kinds of systems.

**Transparent systems.** At one extreme, an agent's observation can reveal the entire round. We say that a power system is *transparent* if, for every admitted agent $$\mathcal{N}_i$$, the function

$$f_i(\bar{a}) = \big(\mathsf{obs}(\mathsf{rct}(\bar{a}))\big)_i$$

is injective, which means that different action vectors produce different observations. Note that $$f_i$$ is applied to the entire action vector, whereas the function $$f_{\bar{a}_{-i}}$$ of the last post fixed every action except one. In a transparent system, an agent can recover the round's action vector $$\bar{a} = f_i^{-1}(y_i)$$ from its own observation and, from the action vector, the reaction vector $$\mathsf{rct}(\bar{a})$$. A board game played in the open is transparent, since every player sees every move.

**Opaque systems.** At the other extreme, an agent's observation reveals at most what happened to the agent itself. We say that a power system is *opaque* if, for every admitted agent $$\mathcal{N}_i$$ and all reaction vectors $$\bar{r}$$ and $$\bar{r}'$$ such that $$r_i = r'_i$$, we have $$\big(\mathsf{obs}(\bar{r})\big)_i = \big(\mathsf{obs}(\bar{r}')\big)_i$$. Each agent's observation then depends on its own reaction alone, and possibly on less, since $$\big(\mathsf{obs}(\bar{r})\big)_i$$ may be constant. A sealed-bid auction is opaque, since each bidder learns its own result and nothing about the other bids. So is the police interrogation of suspects held in separate rooms.

**Public and secret systems.** We also classify systems by whether the agents know how the system works. We say that a power system is *public* if its description, which consists of the process and the power structure, is known to every admitted agent, and *secret* if its description is not known to the agents. A chess match is public, since both players know the rules and know that no one can change them mid-game. Both classifications leave room in between, since a system whose description is known to some agents and not others is neither public nor secret, and a system whose observations reveal part of a round is neither transparent nor opaque. The in-between cases are common; for example, an agency that maintains a no-fly list runs a system whose rules the agency knows and the travelers it screens do not.

**Public and transparent systems.** If a system is public and transparent, then every admitted agent can recover the state of the system at every step of the execution. The agent knows the initial state $$st_0$$ and the component functions because the system is public. In each round, it recovers the action vector $$\bar{a} = f_i^{-1}(y_i)$$ from its observation because the system is transparent, then the reaction vector $$\bar{r} = \mathsf{rct}(\bar{a})$$ and finally the next state $$st_{t+1} = \mathsf{trns}(st_t, \bar{a}, \bar{r})$$. In such a system, no agent is ever uncertain about the state.

**Transparency is a per-agent condition.** Note that transparency requires each $$f_i$$ to be injective on its own, which is stronger than requiring that the composition $$\mathsf{obs} \circ \mathsf{rct}$$ be injective. If the composition is injective, then the full observation vector $$\bar{y}$$ has a unique pre-image; but recall no agent receives the full vector, only a coordinate of it. For example, consider a two-agent system in which the reaction and observation functions are both the identity, so that $$y_1 = a_1$$ and $$y_2 = a_2$$. The composition is injective, yet each agent observes only its own action. Under our definitions, this system is not transparent but opaque, since $$f_1$$ maps action vectors that differ only in $$a_2$$ to the same observation and each $$y_i$$ depends on $$r_i$$ alone.

**Observational power.** These classifications describe a system as it currently is, but $$\mathsf{rct}$$ and $$\mathsf{obs}$$ are components, and components can be controlled. The holder of observational power can replace $$\mathsf{obs}$$ and, with it, change what every agent can know. It can make a system transparent, make it opaque or reveal a round to some agents and not others. In the employment system of the last post, the employer holds observational power, and it exercises that power when it installs workplace monitoring system, seals a personnel file or shares a reference. In our framework, surveillance and privacy are questions about who holds observational power, and later posts will return to this.

## The Power Span

In the last post, we argued that outcomes do not determine power because an agent's powers determine a whole set of possible encounters and an outcome describes only the one that occurred. The power span makes this precise. Let $$\mathcal{N}_i$$ be an agent in a power system and consider what it can do *to* the system rather than *inside* it. The agent can replace any of the component functions it controls with an alternative from that power's replacement set, and each choice of replacements produces a different system. We refer to the set of all systems that the agent can produce this way as its *power span*, and we compare agents' power by comparing their spans.

**Replacement notation.** If $$\mathfrak{p}$$ is a power in a power system $$\mathsf{Sys}$$ and $$g \in \Phi_{\mathfrak{p}}$$ is an admissible replacement for $$\mathfrak{p}$$, we write $$\mathsf{Sys}[\mathfrak{p} \mapsto g]$$ for the system obtained from $$\mathsf{Sys}$$ by replacing the component function $$\chi(\mathfrak{p})$$ with $$g$$. The set of powers $$\mathfrak{P}$$ and the allocation function are unchanged. For simultaneous replacements we write $$\mathsf{Sys}[\mathfrak{p}_1 \mapsto g_1, \dots, \mathfrak{p}_m \mapsto g_m]$$. 

**Which allocations are available.** An agent that holds allocation power can change which powers it holds before it replaces anything else, so the span has to range over the allocation functions the agent can install as well as over the component functions it can replace. We write

$$\mathsf{Alc}_{\mathsf{Sys}}(\mathcal{N}_i) = \begin{cases} \{\mathsf{alc}\} & \text{if } \mathfrak{p}_{\mathsf{alc}} \notin \mathsf{alc}(\mathcal{N}_i),\\[1mm] \{\mathsf{alc}\} \cup \Phi_{\mathfrak{p}_{\mathsf{alc}}} & \text{if } \mathfrak{p}_{\mathsf{alc}} \in \mathsf{alc}(\mathcal{N}_i),\end{cases}$$

for the allocation functions available to $$\mathcal{N}_i$$. The current allocation function $$\mathsf{alc}$$ belongs to this set in both cases, because an agent that holds allocation power may decline to exercise it.

**One replacement phase.** We write

$$\mathsf{Sys} \xrightarrow{\ \mathcal{N}_i\ } \mathsf{Sys}'$$

when $$\mathcal{N}_i$$ can produce $$\mathsf{Sys}'$$ from $$\mathsf{Sys}$$ in a single replacement phase and acting alone. This holds when there is an allocation function $$\mathsf{alc}^+ \in \mathsf{Alc}_{\mathsf{Sys}}(\mathcal{N}_i)$$, a set of powers

$$P \subseteq \mathsf{alc}^+(\mathcal{N}_i) \setminus \{\mathfrak{p}_{\mathsf{alc}}\}$$

and a replacement $$g_{\mathfrak{p}} \in \Phi_{\mathfrak{p}}$$ for each $$\mathfrak{p} \in P$$, such that $$\mathsf{Sys}'$$ is obtained from $$\mathsf{Sys}$$ by installing $$\mathsf{alc}^+$$ when it differs from $$\mathsf{alc}$$ and then replacing each component $$\chi(\mathfrak{p})$$ with $$g_{\mathfrak{p}}$$, simultaneously for every $$\mathfrak{p} \in P$$. All other component functions are unchanged.

The powers in $$P$$ are the ones the agent chooses to exercise, and $$P$$ is a subset of what the agent holds rather than the whole of it because exercising a power is optional and an agent may change some components while leaving the rest as they are.

**The span.** The *power span* of $$\mathcal{N}_i$$ in $$\mathsf{Sys}$$ is the set of systems it can produce in one such phase,

$$\mathsf{Sys}\langle \mathcal{N}_i \rangle = \big\{ \mathsf{Sys}' : \mathsf{Sys} \xrightarrow{\ \mathcal{N}_i\ } \mathsf{Sys}' \big\}.$$

**The span in words.** Taking $$\mathsf{alc}^+ = \mathsf{alc}$$ and $$P = \emptyset$$ changes nothing, so $$\mathsf{Sys}$$ itself belongs to every agent's span. An agent that holds no powers has $$\mathsf{Sys}\langle \mathcal{N}_i \rangle = \{\mathsf{Sys}\}$$, since the only system it can produce is the one it is in. An agent that holds a single power $$\mathfrak{p}$$ can either leave $$\chi(\mathfrak{p})$$ in place or install an admissible function from $$\Phi_{\mathfrak{p}}$$. An agent that holds several powers chooses which of them to exercise and, for each one, which admissible function to install. Every such choice produces an element of the span. In the robbery of the last post, the clerk's span is $$\{\mathsf{Sys}\}$$, since the clerk holds no powers whereas the gunman's span contains every version of the encounter he could produce by changing who is in it, what follows from each action and how it proceeds.

**Spans compare power.** The larger an agent's span, the more systems the agent can bring about and when one agent's span contains another's, the first can produce every system the second can produce and more. The span is also counterfactual by construction. Most of its elements are systems that are never produced. It consists of the systems an agent *could* bring about whether or not it ever does and this is what a definition of power framed in terms of the actions agents take and the outcomes they reach leaves out.

**What the span leaves out.** Note that the span captures an agent's power within a running system. It accounts for the gunman's admission, structural and reaction powers but not for his initiation power which is exercised in the surrounding system rather than inside the robbery. We return to it in the next post.

## The Same Decision, Different Power

One use of the span is that it distinguishes agents that behave identically. Consider a claims adjuster at an insurance company and the executive who wrote the policy the adjuster applies. The adjuster denies a claim by applying the policy exactly as written. The executive would have denied the same claim for the same reason, so on this specific claim the two took the same actions, and a definition of power in terms of actions cannot distinguish them. 

There spans, however, can. The adjuster doesn't control any component of the claims process and applies whatever policy is in place, so the adjuster's span contains exactly one system. The executive, on the other hand, can change what the policy covers, who the company insures and what a claim is worth. So the executive's span is a large set of systems that can be produced by rewriting those terms. 

## Conclusion

A power system determines two different kinds of facts. What its agents can know is determined by the pair $$(\mathsf{rct}, \mathsf{obs})$$ and by whether its description is known and what each agent can change is captured by its span and neither is defined in terms of the system's execution. 

The next post will focus on systems that run inside other systems and that will allow us to define initiation power formally.  
