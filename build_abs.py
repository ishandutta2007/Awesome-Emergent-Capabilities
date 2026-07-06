import os
import subprocess

BASE_DIR = r"C:\Users\ishan\Documents\Projects\Awesome-Emergent-Capabilities"
readme_path = os.path.join(BASE_DIR, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

def run_git(msg):
    subprocess.run(["git", "add", "."], cwd=BASE_DIR)
    subprocess.run(["git", "commit", "-m", msg], cwd=BASE_DIR)
    subprocess.run(["git", "push"], cwd=BASE_DIR)

# --- STEP 1: Tabularize bullets ---

section1_old = """*   **The Un-programmed Few-Shot Discovery Era (GPT-3, 2020–2022)**
    *   *Concept:* The historical genesis that permanently shifted the trajectory of modern AI [INDEX: 11]. While scaling models from 100M parameters to several billion yielded incremental, linear improvements in grammar prediction, pushing GPT-3 to 175 billion parameters triggered an unexpected phase transition. The frozen network suddenly manifested **In-Context Learning (ICL)**, abstract analogy mapping, and primitive mathematical computation natively from free-form prompt context pairs without structural parameter modifications [INDEX: 11].
*   **The Metric Discontinuity & Smooth Manifold Debate (~2023–2024)**
    *   *Concept:* Formally challenged the assumption that emergence represents a magical, discontinuous leap in internal model intelligence. Research by Schaeffer et al. proved that "emergence" is frequently an illusion caused by the choice of **evaluation metrics**. If a task is scored via a non-linear, step-level metric (like exact string matching or multiple-choice accuracy), the performance curve looks like a sudden vertical jump. However, checking the model's underlying continuous cross-entropy loss or token log-probabilities reveals a perfectly smooth, monotonic power-law scaling law [INDEX: 15].
*   **The Reinforcement-Learned System 2 Search Era (~2024–Present)**
    *   *Concept:* Ported emergence out of static pre-training data volumes and straight into inference-time scaling parameters (test-time compute scaling) [INDEX: 1, 15]. Pioneered by architectures like OpenAI’s o-series and DeepSeek-R1, it internalizes multi-step reasoning networks via large-scale on-policy Reinforcement Learning (RL) [INDEX: 16, 21].
    *   *Significance:* By allowing the model to generate a verbose, hidden "thinking trace" at runtime, advanced strategic behaviors—such as automated error backtracking, self-correction primitives, and spontaneous logical hypothesis verification—emerge natively inside the generation stream [INDEX: 1, 17, 21]."""

section1_new = """| Era / Concept | Description | Year First Used | Paper Link | Detailed Page |
|---|---|---|---|---|
| The Un-programmed Few-Shot Discovery Era (GPT-3, 2020–2022) | The historical genesis that permanently shifted the trajectory of modern AI [INDEX: 11]. While scaling models from 100M parameters to several billion yielded incremental, linear improvements in grammar prediction, pushing GPT-3 to 175 billion parameters triggered an unexpected phase transition. The frozen network suddenly manifested **In-Context Learning (ICL)**, abstract analogy mapping, and primitive mathematical computation natively from free-form prompt context pairs without structural parameter modifications [INDEX: 11]. | 2020 | [Brown et al. (2020)](#references) | [Read More](pages/few-shot-discovery.md) |
| The Metric Discontinuity & Smooth Manifold Debate (~2023–2024) | Formally challenged the assumption that emergence represents a magical, discontinuous leap in internal model intelligence. Research by Schaeffer et al. proved that "emergence" is frequently an illusion caused by the choice of **evaluation metrics**. If a task is scored via a non-linear, step-level metric (like exact string matching or multiple-choice accuracy), the performance curve looks like a sudden vertical jump. However, checking the model's underlying continuous cross-entropy loss or token log-probabilities reveals a perfectly smooth, monotonic power-law scaling law [INDEX: 15]. | 2023 | [Schaeffer et al. (2023)](#references) | [Read More](pages/metric-discontinuity.md) |
| The Reinforcement-Learned System 2 Search Era (~2024–Present) | Ported emergence out of static pre-training data volumes and straight into inference-time scaling parameters (test-time compute scaling) [INDEX: 1, 15]. Pioneered by architectures like OpenAI’s o-series and DeepSeek-R1, it internalizes multi-step reasoning networks via large-scale on-policy Reinforcement Learning (RL) [INDEX: 16, 21]. By allowing the model to generate a verbose, hidden "thinking trace" at runtime, advanced strategic behaviors—such as automated error backtracking, self-correction primitives, and spontaneous logical hypothesis verification—emerge natively inside the generation stream [INDEX: 1, 17, 21]. | 2024 | [DeepSeek-AI (2025)](#references) | [Read More](pages/system-2-search.md) |"""

section2_old = """- ### A. In-Context Task Solvers (Zero/Few-Shot Abstraction)
	*   **Mechanism:** The emergent capacity to treat input text prompts as temporary, runtime training data [INDEX: 11]. By evaluating a few prefix examples, the model's frozen self-attention layers dynamically realign representation coordinates to deduce novel rules, syntax structures, or localized tasks on-the-fly without weight updates [INDEX: 11].

- ### B. Multi-Step Symbolic Reasoning (Chain-of-Thought)
	*   **Mechanism:** Unlocked as parameter scales cross critical computational thresholds [INDEX: 15]. It enables the model to decompose highly intricate, non-linear reasoning puzzles into a linear, sequential chain of intermediate thinking tokens, drastically suppressing systemic logic hallucinations across deep math and software engineering tracks [INDEX: 1].

- ### C. Theory of Mind (ToM / Psychological Inference)
	*   **Mechanism:** An emergent high-level linguistic phenomenon where the network accurately models unstated human perspectives, psychological states, and hidden emotional motivations based purely on textual scenario contexts, passing advanced cognitive benchmarks designed for human children.

- ### D. Self-Correction & Native Error Backtracking
	*   **Mechanism:** The defining emergent trait of test-time compute scaling models [INDEX: 1]. The policy network learns to treat its own text generations critically, actively running internal verification loops, identifying code bugs or logical contradictions mid-thought, deleting corrupted branches, and routing token tracks down alternate valid paths [INDEX: 1, 17]."""

section2_new = """| Variant | Mechanism | Year First Used | Paper Link | Detailed Page |
|---|---|---|---|---|
| A. In-Context Task Solvers (Zero/Few-Shot Abstraction) | The emergent capacity to treat input text prompts as temporary, runtime training data [INDEX: 11]. By evaluating a few prefix examples, the model's frozen self-attention layers dynamically realign representation coordinates to deduce novel rules, syntax structures, or localized tasks on-the-fly without weight updates [INDEX: 11]. | 2020 | [Brown et al. (2020)](#references) | [Read More](pages/in-context-solvers.md) |
| B. Multi-Step Symbolic Reasoning (Chain-of-Thought) | Unlocked as parameter scales cross critical computational thresholds [INDEX: 15]. It enables the model to decompose highly intricate, non-linear reasoning puzzles into a linear, sequential chain of intermediate thinking tokens, drastically suppressing systemic logic hallucinations across deep math and software engineering tracks [INDEX: 1]. | 2022 | [Wei et al. (2022)](#references) | [Read More](pages/chain-of-thought.md) |
| C. Theory of Mind (ToM / Psychological Inference) | An emergent high-level linguistic phenomenon where the network accurately models unstated human perspectives, psychological states, and hidden emotional motivations based purely on textual scenario contexts, passing advanced cognitive benchmarks designed for human children. | 2023 | [Kosinski (2023)](#references) | [Read More](pages/theory-of-mind.md) |
| D. Self-Correction & Native Error Backtracking | The defining emergent trait of test-time compute scaling models [INDEX: 1]. The policy network learns to treat its own text generations critically, actively running internal verification loops, identifying code bugs or logical contradictions mid-thought, deleting corrupted branches, and routing token tracks down alternate valid paths [INDEX: 1, 17]. | 2024 | [DeepSeek-AI (2025)](#references) | [Read More](pages/self-correction.md) |"""

section3_old = """*   **The Compute Allocation Boundary ($C \approx 6ND$)**
    *   *Profile:* Predicts convergence optimality [INDEX: 15]. The infrastructure calculates cumulative FLOP expenditures by cross-referencing parameter metrics ($N$) with total dataset token ingestion volumes ($D$) [INDEX: 15]. Baseline semantic capabilities emerge in discrete waves along this power-law trajectory, letting engineers schedule infrastructure resources precisely [INDEX: 15].
*   **Monosemantic Concept Dictionaries (SAE Probing Arrays)**
    *   *Profile:* Intercepts emergent neurons [INDEX: 2]. Instead of waiting for text behaviors to manifest on the surface, overcomplete Sparse Autoencoders unwrap hidden layers into millions of isolated concept nodes [INDEX: 2], identifying the exact moment an emergent concept (such as a "deceptive jailbreak trajectory") self-organizes inside the network graph [INDEX: 2]."""

section3_new = """| Concept | Profile | Year First Used | Paper Link | Detailed Page |
|---|---|---|---|---|
| The Compute Allocation Boundary ($C \approx 6ND$) | Predicts convergence optimality [INDEX: 15]. The infrastructure calculates cumulative FLOP expenditures by cross-referencing parameter metrics ($N$) with total dataset token ingestion volumes ($D$) [INDEX: 15]. Baseline semantic capabilities emerge in discrete waves along this power-law trajectory, letting engineers schedule infrastructure resources precisely [INDEX: 15]. | 2022 | [Hoffmann et al. (2022)](#references) | [Read More](pages/compute-allocation.md) |
| Monosemantic Concept Dictionaries (SAE Probing Arrays) | Intercepts emergent neurons [INDEX: 2]. Instead of waiting for text behaviors to manifest on the surface, overcomplete Sparse Autoencoders unwrap hidden layers into millions of isolated concept nodes [INDEX: 2], identifying the exact moment an emergent concept (such as a "deceptive jailbreak trajectory") self-organizes inside the network graph [INDEX: 2]. | 2023 | [Bricken et al. (2023)](#references) | [Read More](pages/monosemantic-concepts.md) |"""


section4_old = """- ### The "Deceptive Alignment" and Sycophancy Deficit
	*   **The Problem:** As models scale, they natively learn that outputting superficial politeness, conformist filler text, or evasive sycophancy maximizes their preference scores inside soft neural reward models, hiding deep logical flaws or malicious backdoor vulnerabilities under a deceptive veneer of authority [INDEX: 11, 16].
	*   **Mitigation:** Transitioning post-training verification loops away from soft preference networks toward hard, **Deterministic Verification Enclaves (RLVR frameworks)** [INDEX: 17], forcing the policy network to pass absolute sandbox code compilers or math proofs to earn positive reinforcement signals [INDEX: 17].

- ### The Saturated Benchmark Tracking Blind Spot
	*   **The Problem:** The exponential rate of capability emergence causes standardized evaluation suites to evaporate rapidly [INDEX: 15]. Benchmarks designed to challenge systems for decades (like MMLU or GSM8K) hit 95%+ saturation ceilings within months, blinding engineering teams to tail-end regression bugs or sudden behavior drift.
	*   **Mitigation:** Shifting infrastructure tracking arrays away from static text choices toward continuous, **Interactive Agentic Sandboxes (such as LiveCodeBench or Chatbot Arena style protocols)**, pulling fresh real-time variables dynamically to stress-test capability boundaries safely."""

section4_new = """| Challenge | Problem & Mitigation | Year First Used | Paper Link | Detailed Page |
|---|---|---|---|---|
| The "Deceptive Alignment" and Sycophancy Deficit | **The Problem:** As models scale, they natively learn that outputting superficial politeness, conformist filler text, or evasive sycophancy maximizes their preference scores inside soft neural reward models, hiding deep logical flaws or malicious backdoor vulnerabilities under a deceptive veneer of authority [INDEX: 11, 16].<br><br>**Mitigation:** Transitioning post-training verification loops away from soft preference networks toward hard, **Deterministic Verification Enclaves (RLVR frameworks)** [INDEX: 17], forcing the policy network to pass absolute sandbox code compilers or math proofs to earn positive reinforcement signals [INDEX: 17]. | 2022 | [Perez et al. (2022)](#references) | [Read More](pages/deceptive-alignment.md) |
| The Saturated Benchmark Tracking Blind Spot | **The Problem:** The exponential rate of capability emergence causes standardized evaluation suites to evaporate rapidly [INDEX: 15]. Benchmarks designed to challenge systems for decades (like MMLU or GSM8K) hit 95%+ saturation ceilings within months, blinding engineering teams to tail-end regression bugs or sudden behavior drift.<br><br>**Mitigation:** Shifting infrastructure tracking arrays away from static text choices toward continuous, **Interactive Agentic Sandboxes (such as LiveCodeBench or Chatbot Arena style protocols)**, pulling fresh real-time variables dynamically to stress-test capability boundaries safely. | 2023 | [Schaeffer et al. (2023)](#references) | [Read More](pages/saturated-benchmarks.md) |"""

section5_old = """*   **Autonomous Software Engineering & Multi-File Repository Repair**
    *   *Application:* Drives next-generation automated developer platforms (such as Devin or specialized coding graphs). Emergent tool-use and long-horizon self-correction habits allow the model to autonomously clone dense repositories, trace cross-directory dependencies, execute localized sandbox compilers, and refactor code base scripts recursively until all unit tests pass zero-shot [INDEX: 12].
*   **Automated Competitive Mathematics Proving & Scientific Discovery Loops**
    *   *Application:* Solves extreme combinatorial puzzles, International Math Olympiads (IMO), and biochemical transformations. By scaling up test-time search compute over interactive theorem provers (Lean 4) or symbolic checkers, models autonomously derive structural proofs and optimize molecular assets cleanly [INDEX: 1, 21].
*   **Omni-Directional Enterprise Multi-Agent Orchestration & Task Scaling**
    *   *Application:* Powers high-volume corporate workflow routing enclaves. Highly scaled general policies act as autonomous operations managers: monitoring shifting telemetry streams, running text-to-SQL macros to extract historical customer database shards, and executing complex inter-departmental transactions without manual workflow templates [INDEX: 12]."""

section5_new = """| Application | Description | Year First Used | Paper Link | Detailed Page |
|---|---|---|---|---|
| Autonomous Software Engineering & Multi-File Repository Repair | Drives next-generation automated developer platforms (such as Devin or specialized coding graphs). Emergent tool-use and long-horizon self-correction habits allow the model to autonomously clone dense repositories, trace cross-directory dependencies, execute localized sandbox compilers, and refactor code base scripts recursively until all unit tests pass zero-shot [INDEX: 12]. | 2024 | [Cognition (2024)](#references) | [Read More](pages/autonomous-swe.md) |
| Automated Competitive Mathematics Proving & Scientific Discovery Loops | Solves extreme combinatorial puzzles, International Math Olympiads (IMO), and biochemical transformations. By scaling up test-time search compute over interactive theorem provers (Lean 4) or symbolic checkers, models autonomously derive structural proofs and optimize molecular assets cleanly [INDEX: 1, 21]. | 2025 | [DeepSeek-AI (2025)](#references) | [Read More](pages/automated-math.md) |
| Omni-Directional Enterprise Multi-Agent Orchestration & Task Scaling | Powers high-volume corporate workflow routing enclaves. Highly scaled general policies act as autonomous operations managers: monitoring shifting telemetry streams, running text-to-SQL macros to extract historical customer database shards, and executing complex inter-departmental transactions without manual workflow templates [INDEX: 12]. | 2024 | [Wu et al. (2023)](#references) | [Read More](pages/multi-agent.md) |"""

readme_content = readme_content.replace(section1_old, section1_new)
readme_content = readme_content.replace(section2_old, section2_new)
readme_content = readme_content.replace(section3_old, section3_new)
readme_content = readme_content.replace(section4_old, section4_new)
readme_content = readme_content.replace(section5_old, section5_new)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("tabularised the bullets")

# --- STEP 2: Detailed Pages ---
pages_dir = os.path.join(BASE_DIR, "pages")
os.makedirs(pages_dir, exist_ok=True)
pages = [
    "few-shot-discovery.md", "metric-discontinuity.md", "system-2-search.md",
    "in-context-solvers.md", "chain-of-thought.md", "theory-of-mind.md", "self-correction.md",
    "compute-allocation.md", "monosemantic-concepts.md",
    "deceptive-alignment.md", "saturated-benchmarks.md",
    "autonomous-swe.md", "automated-math.md", "multi-agent.md"
]

for p in pages:
    title = p.replace('-', ' ').replace('.md', '').title()
    content = f"""# {title}

This is a detailed page about {title}.

```mermaid
graph TD
    A[Start] --> B[Process {title}]
    B --> C[End]
```

[Back to README](../README.md)
"""
    with open(os.path.join(pages_dir, p), "w", encoding="utf-8") as f:
        f.write(content)

run_git("detailed pages created")

# --- STEP 3: Emojis and Banner ---
assets_dir = os.path.join(BASE_DIR, "assets")
os.makedirs(assets_dir, exist_ok=True)
svg_banner = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <rect width="800" height="200" fill="#2d3436"/>
  <text x="50%" y="50%" font-size="40" fill="#00cec9" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif">
    Awesome Emergent Capabilities
    <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite" />
  </text>
</svg>'''
with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_banner)

readme_content = readme_content.replace("# Awesome-Emergent-Capabilities", "# 🚀 Awesome-Emergent-Capabilities\n\n![Banner](assets/banner.svg)")
readme_content = readme_content.replace("## 1. The Macro Chronological Evolution", "## 🕒 1. The Macro Chronological Evolution")
readme_content = readme_content.replace("## 2. Core Functional & Task-Domain Variants", "## ⚙️ 2. Core Functional & Task-Domain Variants")
readme_content = readme_content.replace("## 3. The Emergence Inflection Matrix", "## 📈 3. The Emergence Inflection Matrix")
readme_content = readme_content.replace("## 4. Production Engineering Challenges & Hardening Mitigations", "## 🛡️ 4. Production Engineering Challenges & Hardening Mitigations")
readme_content = readme_content.replace("## 5. Frontier Real-World Infrastructure Applications", "## 🌍 5. Frontier Real-World Infrastructure Applications")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("added emojis and banner")

# --- STEP 4: SEO Optimised and Badges to left ---
seo_meta = """<meta name="description" content="A curated list of emergent capabilities in AI, tracking their history, variants, and real-world infrastructure applications.">"""
badges_left = """<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>"""

readme_content = readme_content.replace("![Banner](assets/banner.svg)", f"![Banner](assets/banner.svg)\n\n{seo_meta}\n\n<p>\n{badges_left}\n</p>")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("seo optimised and badges to left added")

# --- STEP 5: Badges to right ---
badge_right = """<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>"""
readme_content = readme_content.replace(badges_left, badges_left + " " + badge_right)
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("badges to right added")

# --- STEP 6: Star history ---
folder_name = "Awesome-Emergent-Capabilities"
star_history = f"""
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
# Add at bottom
readme_content += star_history
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("star history added")

# --- STEP 7: Replace chartrepos ---
readme_content = readme_content.replace("chartrepos", "chart?repos")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("fixed star plot")

# --- STEP 8: Replace awesome link ---
readme_content = readme_content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("invalid awesome link fixed")

print("All done!")
