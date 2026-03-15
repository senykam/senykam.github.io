# Research Idea: Television as World Model Installation

## Core Insight

Television (and media more broadly) functions as a world-model-installation mechanism operating on billions of people. Different national media ecosystems install different generative models of reality — different graphical structures, different likelihood functions — in their viewers. We now have the AI tools (video world models) to make these implicit models explicit and comparable.

## Background

### Gerbner's Cultivation Theory (1960s-70s)
- Heavy TV viewers build their world model from television
- "Mean world syndrome": TV viewers overestimate violence because TV overrepresents it
- "Mainstreaming": heavy viewers from diverse backgrounds converge on a shared (TV-derived) worldview
- "Resonance": when real experience aligns with TV content, the TV-installed model is reinforced
- In Bayesian terms: TV installs a distorted likelihood function, causing incorrect posterior inference from real-world observations

### Connection to Insight Framework
- In my framework, insight depends on having an accurate generative model (graphical structure / likelihood function)
- Television systematically installs *inaccurate* generative models in viewers
- People can't easily detect the distortions because they're inside the model — their TV-trained likelihood function feels like "common sense"
- Cross-cultural comparison makes distortions visible: where models trained on different media diets diverge reveals where each media environment is installing different structure

## Experimental Design

### Core Experiment
Train the same world model architecture on curated media diets from different countries:
- **US television** (network TV, cable news, streaming)
- **French television**
- **Indian television**
- **Chinese television/state media**
- **Control: raw real-world footage** (dashcams, security cameras, documentary footage — unscripted, unedited)

Then compare the resulting world models along multiple dimensions.

### Analysis Layers

**Surface level (automating Gerbner at scale):**
- What do models predict about frequency of events? (violence, wealth, romance, demographic distributions)
- Compare predicted distributions against real-world base rates
- Quantify the "cultivation differential" for each media diet

**Structural level (the novel contribution):**
- What *causal structure* do the models learn?
- Given an ambiguous social situation, what does each model predict happens next?
- Do models trained on different media diets learn different causal chains for the same type of event?
- This is extracting the implicit likelihood functions that each media environment installs

**Temporal dimension:**
- Train on US television from different decades (1970s, 1990s, 2020s)
- How has the installed world model changed over time?
- Quantifies cultural shift more precisely than discursive media criticism

**Cross-media comparison:**
- TV vs. social media (TikTok, YouTube) vs. news media
- Does the medium itself (not just the content) introduce systematic distortions?
- Binge-watching / streaming as a more intense cultivation mechanism

### Key Comparisons
- Where models disagree across media diets → media environment is installing different structure
- Where ALL models agree but diverge from reality → distortions inherent to television as a medium
- Where the real-world-footage model differs from all TV models → the "fiction gap"

## Why This Matters

1. **Makes implicit explicit**: We've known since Gerbner that TV shapes perception, but we've never had tools to precisely characterize *what model* TV installs. World model training makes the implicit graphical structure extractable and comparable.

2. **AI safety angle**: If we're worried about what world models AI systems learn from internet video, we should be at least as worried about what world models humans have been learning from TV for decades. The AI problem makes the human problem legible.

3. **Media literacy**: Cross-cultural comparison reveals that "common sense" is a locally installed model. The American viewer doesn't know their world model is American — it just feels like reality. Comparison makes distortion visible.

4. **Connects classic social science to frontier AI**: Bridges a 60-year-old communication theory to state-of-the-art world model research in a way nobody has done.

## Publication Strategy

### Blog post (safe to publish — shares output, not formal model):
- Frame as: "What if we could extract the world model that TV installs in viewers?"
- Use the cross-cultural comparison as the hook
- Reference Gerbner, connect to current AI world models work
- DO NOT expose any formal framework — just the specific reframing and experimental idea

### Paper:
- Could target multiple venues depending on framing:
  - NeurIPS/ICML workshop (AI + society, world models)
  - Communication studies journal (computational cultivation theory)
  - Interdisciplinary (PNAS, Nature Human Behaviour)
- The experimental results themselves are the contribution
- Could attract collaborators who have access to large media corpora and compute

## Practical Considerations

- Need curated, representative media corpora for each country
- Need to decide on world model architecture (JEPA-style? Diffusion-based? Sora-like?)
- Need evaluation methodology for comparing model "beliefs"
- Probing techniques from mechanistic interpretability could be useful for extracting model beliefs
- May need to start with a smaller pilot (e.g., just US vs. one other country, or just one dimension like violence)

## Related Work to Check
- Gerbner's Cultural Indicators Project
- Cultivation theory meta-analyses and extensions to social media
- OpenAI's Sora technical report ("Video generation models as world simulators")
- LeCun's JEPA and V-JEPA work
- Any work on bias in video generation models trained on internet data
- Williams (2006) — cultivation effects of video games