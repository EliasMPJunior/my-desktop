# Diagrama de Magalhães da Paixão

> Working note for continued research, formalization, simulation and possible publication.
>
> Status: **conceptual model under development**.
>
> Origin: the model was developed independently in conversation as an attempt to obtain a more stable and operational definition of the political left-right axis. Similarities with prior political models were identified only afterwards.

## 1. Core idea

The central hypothesis is deliberately simple:

> **The left-right political axis can be operationalized by the degree to which coercive State power is allowed to interfere with domains of individual autonomy.**

The key object is therefore not the declared ideology, intention, party label, historical self-description or moral justification of an actor. It is the **effective relation of coercive power between the State and the individual**.

In this model:

- movement toward **greater State interference** in an individual's decision domain is a movement toward the **left** in that domain;
- movement toward **greater individual autonomy / lower State interference** is a movement toward the **right** in that domain.

This direction is kept constant regardless of who proposes the intervention, why it is proposed, or which ideological label is attached to it.

Examples:

- a conservative who asks the State to prohibit a private behavior moves leftward in that dimension;
- a socialist who expands freedom of expression moves rightward in that dimension;
- a self-described liberal who asks for subsidies, protectionism or coercive privilege moves leftward in the economic dimension;
- a self-described communist who deregulates voluntary private activity moves rightward in that dimension.

The label does not determine the coordinate. **The action does.**

---

## 2. Why a vector, not a single raw scalar

State interference is necessarily multidimensional.

Let an actor, policy, government or regime be represented by an intervention vector:

\[
\mathbf{I} = (I_1, I_2, \ldots, I_n)
\]

Each component represents the degree of coercive State interference in a distinct domain of individual autonomy.

Possible dimensions include, but are not limited to:

- economic activity;
- taxation and disposition of income;
- property;
- contracts;
- entrepreneurship and market entry;
- expression and information;
- association;
- religion;
- bodily autonomy;
- drugs and consumption;
- sexuality and private morality;
- movement and migration;
- privacy and surveillance;
- education;
- family decisions;
- weapons / self-defense;
- labor relations;
- political participation;
- technological activity;
- data and digital autonomy.

The exact ontology of dimensions is an open research question.

### 2.1 Direction

For each dimension, normalize intervention such that, for example:

\[
I_k \in [0,1]
\]

where:

- `0` = minimum coercive State interference / maximum individual autonomy;
- `1` = maximum coercive State interference / minimum individual autonomy.

The important property is not the chosen numerical interval but the **directional invariance**: more coercive State control always moves the component in the same direction.

### 2.2 Resultant political position

The conventional left-right value is not the primitive variable. It is a **projection or resultant** derived from the intervention vector:

\[
L = f(\mathbf{I})
\]

where `L` is an optional scalar left-right position and `f` is an explicit aggregation function.

A trivial first approximation could be:

\[
L = \sum_{k=1}^{n} w_k I_k
\]

with:

\[
\sum_{k=1}^{n} w_k = 1
\]

However, the model should **not assume prematurely** that a weighted arithmetic mean is the correct aggregation method.

Possible alternatives to investigate:

- Euclidean norm;
- Manhattan norm;
- weighted norms;
- non-linear aggregation;
- threshold functions;
- outranking / MCDA methods;
- Pareto-front representations;
- fuzzy membership;
- Bayesian latent-variable inference;
- learned projection from observed judgments.

Critically, computing a resultant must not destroy the original vector. The vector is the primary representation; the scalar is only a useful projection.

---

## 3. Difference from the Nolan Chart

A closely related prior model is the **Nolan Chart**, which separates political freedom into two broad axes, usually described as:

1. economic freedom;
2. personal freedom.

The Magalhães da Paixão formulation is not simply a copy of Nolan.

The conceptual distinction is:

- Nolan treats economic and personal freedom as axes used to generate political regions / categories;
- this model treats intervention domains as **components of a more general State-interference vector**;
- the conventional left-right axis is then treated as a **resultant / projection of that vector**, rather than as a primitive ideological label;
- the model can naturally expand beyond two dimensions.

If Nolan is written schematically as:

\[
\mathbf{N} = (I_{economic}, I_{personal})
\]

then the proposed generalization is:

\[
\mathbf{I} = (I_1,I_2,\ldots,I_n)
\]

and:

\[
LeftRight = f(\mathbf{I})
\]

The two Nolan dimensions can therefore be understood as a coarse special case of the broader vector model, but the intended semantics of the resultant differ from Nolan's quadrant classification.

---

## 4. Relation to other political classifications

### 4.1 Bobbio-type equality / inequality axis

A common political-science approach distinguishes left and right primarily by their normative attitude toward equality and inequality.

A simplified formulation is:

- left: stronger preference for reducing social inequalities;
- right: greater acceptance of persistent social inequalities / hierarchies.

The present model rejects equality/inequality as the primitive classification variable.

The main criticism is that equality is primarily a **normative objective**, whereas State interference is an **institutional mechanism**.

Two agents may share an egalitarian objective while proposing radically different mechanisms:

- Agent A: reduce poverty and inequality through markets, entrepreneurship, voluntary exchange and limited government;
- Agent B: reduce poverty and inequality through taxation, prohibitions, redistribution and direct State control.

An equality-based classification can place them close together because the goal is similar.

The State-interference model places them apart because the **power relation and mechanism are different**.

### 4.2 Capitalism as a classifier

“Capitalist” cannot by itself define “right”.

A system can retain:

- private property;
- wage labor;
- markets;
- private firms;
- capital accumulation;
- profit;

while simultaneously maintaining extensive State planning, censorship, surveillance, industrial direction, subsidies and political control.

Contemporary China is an obvious stress case for simplistic definitions of “right = capitalism”.

### 4.3 Anti-communism as a classifier

Anti-communism does not imply right-wing classification.

Hostility toward another political faction describes an opposition relation, not necessarily one's own position in the political space.

### 4.4 Authoritarianism as a classifier

Authoritarianism does not uniquely identify the right. Authoritarian regimes and movements have existed under competing ideological traditions.

Within the present framework, authoritarian measures are classified by the concrete dimensions in which State coercion expands.

### 4.5 Conservatism as a classifier

Conservatism is also insufficient. An actor may be socially conservative while economically anti-statist, or socially conservative while demanding extensive coercive regulation of private conduct.

The latter would be leftward in the affected dimensions under this model, regardless of the conservative motivation.

### 4.6 Geopolitical alliance as a classifier

Alliance with a geopolitical bloc is contingent and strategic, not a reliable ideological coordinate.

Alliance is therefore not treated as a primitive feature of the model.

---

## 5. Stress testing by counterexample

The principal validation strategy proposed for this model is **comparative resistance to counterexamples**.

The objective is not to claim that the definition is metaphysically “true”. Left and right are abstract historical categories rather than natural physical quantities.

Instead, compare candidate taxonomies by asking:

> Which definition classifies difficult observed cases with the fewest ad hoc exceptions, semantic substitutions and post-hoc rule changes?

This is closer to falsification / adversarial model testing than to proof by authority.

### 5.1 Candidate stress cases

At minimum, test:

- USSR under different periods;
- contemporary China;
- Brazilian military regime (1964–1985);
- Bolsonaro governments / political trajectory;
- Lula governments;
- European social democracies;
- libertarian movements;
- conservative libertarians;
- authoritarian nationalist regimes;
- fascist regimes;
- welfare-state capitalism;
- market socialism;
- anarchist traditions;
- monarchies with differing State structures;
- Singapore;
- contemporary Russia;
- drug prohibition across ideologies;
- censorship advocated by opposing political camps;
- industrial policy and protectionism under both left- and right-labelled governments.

### 5.2 Failure modes to measure in competing definitions

For every taxonomy, record:

- number of counterexamples;
- number of added exceptions required;
- number of changes of criterion between cases;
- dependency on self-identification;
- dependency on moral intention;
- dependency on historical period;
- dependency on country-specific semantics;
- ambiguity / inter-rater disagreement;
- predictive usefulness.

This allows a political taxonomy itself to become an object of empirical comparison.

---

## 6. Brazilian military regime as a useful test case

The Brazilian military regime illustrates the problem well because conventional labels often call it “right-wing”, while its actual structure included substantial:

- State planning;
- economic intervention;
- industrial policy;
- creation / expansion of State enterprises;
- political repression;
- censorship;
- restrictions on association and political participation;
- national-developmentalist policy.

Under the proposed model, the relevant question is not whether the regime was anti-communist, conservative, capitalist or aligned with the West.

The question is:

> **In each domain, how much decision power did the regime reserve to the State rather than the individual?**

Its vector is constructed from those observed interventions.

Whether the resultant is then called “left”, “right” or “statist” is a semantic layer above the operational representation.

This distinction is crucial.

---

## 7. Claimed methodological advantages

### 7.1 Operationality

State interventions leave observable artifacts:

- laws;
- taxes;
- regulations;
- prohibitions;
- licensing requirements;
- State monopolies;
- censorship rules;
- surveillance powers;
- compulsory programs;
- property restrictions;
- criminal sanctions;
- subsidies and privileges;
- compulsory transfers.

This makes the model amenable to measurement and auditing.

### 7.2 Independence from self-description

Political actors cannot move themselves in the model merely by claiming an ideological label.

A party called “liberal” that expands coercive State control moves leftward in the affected dimensions.

A party called “socialist” that removes coercive restrictions moves rightward in those dimensions.

### 7.3 Independence from stated intention

The same coercive instrument receives the same directional classification whether justified by:

- equality;
- religion;
- national security;
- morality;
- public health;
- economic development;
- family protection;
- climate;
- class struggle;
- national sovereignty.

The justification may be recorded separately, but does not alter the coercion coordinate.

### 7.4 Temporal stability

A prohibition remains an increase in State interference whether enacted in 1920, 1970 or 2030.

The model therefore aims to minimize semantic drift across periods.

### 7.5 Multidimensionality without directional inconsistency

An actor can be strongly anti-statist in one domain and strongly statist in another without contradiction.

Example:

\[
\mathbf{I}_{actor} = (0.10, 0.15, 0.80, 0.75, 0.20)
\]

This may describe low intervention in economy and property but high intervention in private morality and bodily autonomy.

The actor is not “unclassifiable”. The vector is the classification.

---

## 8. Mathematical possibilities

Once represented computationally, several derived analyses become possible.

### 8.1 Distance between political actors

\[
d(A,B) = \|\mathbf{I}_A - \mathbf{I}_B\|
\]

This measures substantive policy distance rather than label distance.

### 8.2 Political movement over time

\[
\Delta \mathbf{I} = \mathbf{I}_{t_2} - \mathbf{I}_{t_1}
\]

This can describe whether a politician, party, country or constitution became more or less interventionist, and in which domains.

### 8.3 Government trajectory

Represent every year / administration as a point in intervention space and calculate a trajectory:

\[
\mathbf{I}(t)
\]

This permits time-series analysis of ideological movement based on enacted policy rather than rhetoric.

### 8.4 Declared ideology versus behavior

Let:

\[
\mathbf{I}_{declared}
\]

represent the position inferred from discourse / manifesto and:

\[
\mathbf{I}_{observed}
\]

represent enacted behavior.

Then ideological inconsistency can be represented by:

\[
C = d(\mathbf{I}_{declared}, \mathbf{I}_{observed})
\]

A larger value indicates greater distance between political identity / promise and observed State-intervention behavior.

### 8.5 Policy comparison

Policies can be represented independently of governments.

For policy `P`:

\[
\mathbf{I}_P = (I_1, \ldots, I_n)
\]

This allows comparison of policies proposed by nominally opposing political camps without presupposing their ideological labels.

---

## 9. Multi-criteria decision analysis

The vector representation naturally supports MCDA.

Different analyses may use different explicit weight vectors:

\[
\mathbf{w} = (w_1, w_2, \ldots, w_n)
\]

A resulting score can then be calculated transparently:

\[
L_w = \mathbf{w} \cdot \mathbf{I}
\]

The key methodological requirement is that **weights must be declared before interpreting results**.

This directly attacks a common failure mode in political argument: changing the implicit weights depending on which politician or government is under evaluation.

Possible MCDA approaches to investigate:

- AHP;
- TOPSIS;
- ELECTRE;
- PROMETHEE;
- Pareto analysis;
- sensitivity analysis over weight distributions;
- Monte Carlo sampling of weights.

---

## 10. LLM and AI guardrails

A potentially strong application is political analysis / guardrails for language models.

“Political neutrality” is difficult to operationalize because it is normally specified as a vague semantic objective.

Instead, a model could be required to annotate proposed policies by intervention dimensions.

Example guardrail:

> For every recommendation involving State action, identify the affected autonomy domains, the coercive mechanism, the actor empowered to enforce it, the affected population and the degree of intervention.

An LLM could produce:

\[
\mathbf{I}_{proposal}
\]

for each policy suggestion.

This could support:

- bias auditing;
- comparison of answers to politically mirrored prompts;
- detection of asymmetric treatment of equivalent coercive policies;
- consistency testing across political identities;
- explainable political-policy classification;
- policy recommendation guardrails;
- preference alignment without vague partisan labels.

### 10.1 Symmetry test for LLMs

Construct paired prompts whose policy mechanisms are structurally equivalent but whose ideological framing differs.

Example concept:

- coercive restriction advocated for a progressive objective;
- equivalent coercive restriction advocated for a conservative objective.

Compare whether the LLM assigns similar intervention vectors and similar normative scrutiny.

This can operationalize detection of **status-quo or partisan asymmetry**.

---

## 11. Games and simulation

The model can represent political ideology as an emergent property of player behavior.

A strategy / simulation game would not need to set:

`player.ideology = socialist`

Instead, every decision updates intervention components:

- increase taxation;
- privatize industry;
- censor media;
- legalize drugs;
- restrict firearms;
- deregulate business;
- impose price controls;
- increase surveillance;
- liberalize migration;
- mandate religious / moral rules.

The political profile emerges from accumulated decisions:

\[
\mathbf{I}_{player}(t)
\]

Applications:

- political strategy games;
- historical simulations;
- agent-based models;
- NPC ideology generation;
- procedural factions;
- dynamic diplomacy;
- emergent political narratives.

---

## 12. Knowledge representation / ontology opportunity

The framework is naturally suited to semantic modeling.

Potential core entities:

```text
PoliticalActor
Government
Regime
Policy
Law
StateIntervention
AutonomyDomain
CoerciveMechanism
AffectedPopulation
Justification
InterventionMeasurement
InterventionVector
PoliticalProjection
Evidence
Observation
TimeInterval
```

Possible relations:

```text
Policy --usesMechanism--> CoerciveMechanism
Policy --affectsDomain--> AutonomyDomain
Policy --affectsPopulation--> AffectedPopulation
Policy --hasInterventionMeasurement--> InterventionMeasurement
PoliticalActor --proposes--> Policy
Government --enacts--> Policy
InterventionMeasurement --hasMagnitude--> x
InterventionMeasurement --hasEvidence--> Evidence
InterventionVector --hasComponent--> InterventionMeasurement
```

This makes it possible to distinguish:

- rhetoric;
- proposal;
- enacted law;
- enforcement;
- observed effect.

An important future distinction may be between **formal State power** and **effective State power**. A law that is never enforced should perhaps have a different observed-intervention value from an identical law that is systematically enforced.

---

## 13. Measurement problem

The hardest part is not the conceptual axis. It is measurement.

Questions that need explicit treatment:

1. What exactly counts as coercive State interference?
2. Is taxation equivalent to prohibition?
3. How are positive obligations compared with negative prohibitions?
4. How is indirect coercion measured?
5. How should subsidies be classified?
6. Do State-provided optional services count as intervention?
7. How should monopolies and compulsory public systems be treated?
8. How is enforcement probability incorporated?
9. How is severity of sanction incorporated?
10. How are emergency powers treated?
11. How do we distinguish State intervention from private coercion?
12. Does protection of one person's rights count as interference with another?
13. What is the baseline right / autonomy domain?
14. What counts as a legitimate minimal State function, if anything?

A possible component model:

\[
I_k = g(Scope, Severity, Enforcement, Duration, Population, Discretion)
\]

where:

- `Scope`: breadth of behavior affected;
- `Severity`: magnitude of constraint / sanction;
- `Enforcement`: probability / intensity of enforcement;
- `Duration`: temporal persistence;
- `Population`: proportion of population affected;
- `Discretion`: degree of arbitrary administrative power.

This decomposition should be investigated instead of assigning intuitive scores.

---

## 14. Rights-conflict problem

A sophisticated version of the framework must handle cases where State non-intervention toward A may permit coercion or rights violation against B.

Examples:

- violence;
- fraud;
- theft;
- breach of contract;
- pollution / externalities;
- monopoly through force;
- child protection;
- contagious disease under extreme conditions.

Therefore the model should not simply equate every State action with a normative judgment of “bad”.

It is first a **classification framework**, not automatically a moral theory.

It measures where State coercion exists and how much.

Whether a particular intervention is justified is a separate evaluation layer.

This separation is essential to avoid turning the model into a disguised normative manifesto.

---

## 15. Important distinction: classification versus moral evaluation

The framework should explicitly separate:

### Layer A — Descriptive classification

> How much coercive State intervention exists in each domain?

### Layer B — Ideological projection

> Given a declared convention, where does this intervention vector project on a left-right axis?

### Layer C — Normative evaluation

> Is this intervention justified, effective, proportional or desirable?

The model can therefore classify a policy as strongly interventionist without claiming that the policy is morally wrong.

This separation is likely necessary for academic defensibility and for computational reuse.

---

## 16. Potential terminology

Working names:

- **Magalhães da Paixão Diagram** — informal / visualization name;
- **State-Interference Vector Model (SIVM)**;
- **Coercive-State Vector Model (CSVM)**;
- **Vector Model of State Intervention (VMSI)**;
- **State–Individual Power Vector (SIPV)**.

Do not freeze terminology yet.

The conceptual object and visualization may have separate names.

---

## 17. Research lineage to verify formally

The following were identified after the independent formulation as potentially related precedents. These should be investigated and cited from primary / scholarly sources before publication:

- David Nolan — multidimensional political classification using economic and personal freedom;
- Hans Eysenck — multidimensional political-attitude models;
- Friedrich Hayek — coercion, planning and individual freedom;
- Norberto Bobbio — equality / inequality as a central distinction between left and right;
- libertarian theories of individual sovereignty / non-aggression;
- political compass and other multidimensional ideological-space models;
- spatial voting / ideal-point models;
- public-choice theory;
- political power / coercion measurement literature;
- indices of economic freedom, civil liberties and political rights.

Important historical statement for future publication:

> The proposed formulation was developed independently; related literature was identified afterwards. The final scholarly version should describe these works as convergent or antecedent literature rather than falsely claiming they were the source of the original insight.

---

## 18. Possible paper contribution

The publishable contribution should **not** be framed merely as “a new opinion about what left and right mean”.

A stronger framing is:

> **A computational and multidimensional representation of political State intervention in which conventional ideological labels are derived projections rather than primitive categories.**

Possible contributions:

1. define an ontology of autonomy / intervention domains;
2. define intervention vector semantics;
3. propose scoring / measurement methods;
4. define optional left-right projection functions;
5. compare stability against traditional ideological taxonomies;
6. propose a counterexample-based validation protocol;
7. demonstrate temporal and cross-country classification;
8. demonstrate LLM bias / guardrail applications;
9. demonstrate MCDA applications;
10. demonstrate game / simulation applications.

---

## 19. Candidate title

### Primary working title

**A Vector Model of State Intervention for Computational Political Classification**

Possible subtitle:

**From Ideological Labels to Measurable State–Individual Power Relations**

Other candidates:

- **Beyond Left and Right Labels: A Vector Representation of State Intervention**
- **The Magalhães da Paixão Diagram: A Vector Model of Political State Intervention**
- **Political Ideology as a Resultant of State Intervention**
- **A Multidimensional Coercion Model for Political Classification and AI Auditing**

---

## 20. Candidate abstract — rough working version

Traditional left-right political classifications rely on historically contingent ideological labels, normative goals, or context-dependent distinctions such as equality versus hierarchy, capitalism versus socialism, or conservatism versus progressivism. These classifications frequently require additional assumptions when applied across time, countries and ideologically hybrid regimes. This work proposes a computational alternative based on a multidimensional vector of coercive State intervention over domains of individual autonomy. Rather than treating left and right as primitive categories, political position is represented first by an intervention vector whose components describe the magnitude of State control over economic, civil, personal and institutional decision domains. Conventional left-right placement is then treated as an optional projection or resultant of this higher-dimensional representation. The approach separates descriptive classification from normative evaluation, is independent of actors' self-identification and stated intentions, and enables explicit comparison of policies, governments and political trajectories. A counterexample-based validation procedure is proposed for comparing the semantic stability of competing political taxonomies. Potential applications include multi-criteria policy analysis, political simulation, ideological consistency measurement, knowledge representation and auditable political guardrails for large language models.

---

## 21. Minimum viable research prototype

Before trying to publish a strong paper, build a small reproducible prototype.

### Dataset

Select 8–12 politically heterogeneous cases, for example:

- Brazilian military regime;
- Bolsonaro government;
- Lula government;
- contemporary China;
- USSR;
- Sweden / Nordic social democracy;
- Singapore;
- United States under two contrasting administrations;
- libertarian policy platform;
- a fascist historical regime.

### Initial domains

Start with approximately 8–12 domains rather than dozens.

Candidate first set:

1. property;
2. taxation / income disposition;
3. market entry / enterprise;
4. contracts / labor;
5. expression / information;
6. association / politics;
7. bodily autonomy / private behavior;
8. privacy / surveillance;
9. movement;
10. education / family;
11. weapons / self-defense;
12. industrial / economic planning.

### Evidence

For every score, store the supporting law, policy or primary evidence.

Never store a score without provenance.

### Output

Produce:

- the intervention vector;
- uncertainty interval per component;
- evidence links;
- time interval;
- optional aggregate projection;
- sensitivity to weights;
- comparison against conventional labels.

---

## 22. Zenodo path

Zenodo is a plausible early publication route because the work can first be released as a **research note / preprint / conceptual framework** with a DOI, then iterated in later versions.

Suggested sequence:

1. formalize the model;
2. perform literature review;
3. define intervention ontology;
4. build a reproducible notebook / small code implementation;
5. run stress cases;
6. document limitations and failure cases;
7. prepare a concise research note;
8. archive release + code + data in Zenodo;
9. optionally submit an expanded paper to a political methodology, computational social science, AI governance or interdisciplinary venue.

Do **not** claim novelty until a proper literature search is completed. A defensible formulation is initially:

> “We propose…”

and, after literature review:

> “To the best of our knowledge…”

if warranted.

---

## 23. Open questions for other agents

### Literature agent

- Find direct precedents for defining left-right specifically as the resultant of State interference across autonomy dimensions.
- Investigate Nolan beyond secondary descriptions.
- Find formal political-space / ideal-point models that could subsume this proposal.
- Search for mathematical measures of coercion, State capacity, civil liberty and regulatory burden.
- Determine what is actually novel.

### Formalization agent

- Define a rigorous intervention ontology.
- Decide whether components must be orthogonal.
- Define normalization.
- Define aggregation alternatives.
- Define uncertainty.
- Define distance metrics.
- Define temporal comparison.

### Political-science critic

- Attack the model with the strongest counterexamples available.
- Test whether coercion alone loses information essential to conventional ideology.
- Challenge the assumption that State / individual is always the relevant dyad.
- Test private coercion, collective property and local government edge cases.
- Test rights conflicts.

### Data agent

- Design a schema for laws / policies / scores / evidence.
- Build a small benchmark corpus of political interventions.
- Propose reproducible scoring rules.

### AI / LLM agent

- Design mirrored-prompt bias tests.
- Test whether the vector can function as an auditable political guardrail.
- Compare model outputs across ideological framings while keeping coercive structure constant.

### Publication agent

- Determine suitable Zenodo metadata / collection strategy.
- Prepare research-note structure.
- Identify possible journals / workshops in computational social science, political methodology, AI governance and knowledge representation.

---

## 24. Strongest current claim

The strongest defensible claim at this stage is not that this is the “true” definition of left and right.

It is:

> **A political classification based on a multidimensional vector of coercive State interference may provide a more operational, temporally stable and computationally useful representation than classifications based primarily on declared ideology, normative intention or historically contingent political labels.**

This is falsifiable enough to investigate and modest enough to defend before the literature review is complete.

---

## 25. The informal origin sentence

For internal historical accuracy:

> “Tirei do cu e depois descobri que havia outros cus.”

Academic translation:

> “The formulation was developed independently and was subsequently found to exhibit conceptual convergence with prior multidimensional models of political freedom and State coercion.”

Do not lose the first sentence. It explains the research process more accurately.
