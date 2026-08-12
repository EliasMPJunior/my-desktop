# InfoBIM — buildingSMART International Summit Tokyo 2026

## Status

Workspace created to consolidate the submission and paper/presentation material for the buildingSMART International Summit Tokyo 2026.

- Event: buildingSMART International Summit Tokyo 2026
- Location: Tokyo, Japan
- Event dates: 6–8 October 2026
- Presentation day: 7 or 8 October 2026 (TBC by organizers)
- CFP deadline previously identified: 14 August 2026
- Project/tool: InfoBIM
- InfoBIM status: open-source and free

## Working title

**Data with Brains: Towards Executable OpenBIM Information with InfoBIM and a No-Vendor-Lock-In Approach**

## Core thesis

InfoBIM explores an OpenBIM information architecture in which ordinary engineering files remain usable in their original formats and locations while an explicit semantic layer inventories, identifies and connects them computationally.

Rather than treating interoperability as the migration of all project information into a single vendor-controlled environment, the approach separates **storage from meaning**. IFC models, PDFs, spreadsheets, images, communications and other information resources may remain distributed while their relationships, context and applicable operations are represented through open, machine-readable structures.

The central proposition is that engineering information can become **semantically connected, queryable and executable without ceasing to be ordinary engineering information resources**.

This is the basis of the phrase **Data with Brains**.

## What InfoBIM is

InfoBIM is not intended to be another monolithic BIM application or a replacement for authoring software. It is a semantic layer and toolset applied over heterogeneous project information.

The architecture aims to:

- preserve original project files;
- inventory and identify information resources;
- represent explicit semantic relationships between them;
- connect BIM and non-BIM information;
- support deterministic queries, validation and executable capabilities;
- remain portable across tools and information environments;
- operate locally and, where the workflow permits, offline;
- avoid dependence on a proprietary data model or vendor-controlled repository.

## Standards context

### openBIM

The presentation must clearly demonstrate or focus on openBIM. InfoBIM should be framed as an implementation and experimental architecture within that context, not merely as a standalone software demonstration.

### IFC

IFC is one structured information resource that can participate in the InfoBIM mesh, but InfoBIM is not dependent on IFC alone. The point is precisely to connect IFC with the information that normally remains outside the model: PDFs, spreadsheets, photographs, schedules, communications and other project records.

### ISO 21597 / ICDD

ISO 21597 is a major architectural reference because it formalizes information containers for linked document delivery and explicit linksets between heterogeneous information resources.

The paper should emphasize the conceptual continuity between ICDD linksets and InfoBIM's semantic linking approach: relationships can exist independently of the source documents and therefore do not require modification or conversion of the original engineering files.

### ISO 19650

ISO 19650 provides the information-management context in which project information is produced, reviewed, shared and used.

InfoBIM should not be presented as replacing ISO 19650 processes. The stronger argument is that it adds a computational semantic layer over the information resources governed by those processes.

## CDE position

A deliberate research/design question behind InfoBIM is whether a Common Data Environment must necessarily be understood primarily as a centralized repository.

The alternative explored here is a **distributed semantic information mesh**:

- files may remain where they already reside;
- the semantic relationships between them are explicit;
- the information can be queried across heterogeneous resources;
- the semantic context can remain portable across environments;
- local/offline operation becomes possible;
- the value of the information does not depend exclusively on one vendor platform.

This does **not** require claiming that conventional CDEs are invalid or obsolete. The paper can instead argue that storage centralization and semantic integration are separate architectural concerns.

## InfoBIM versus “SharePoint with AI”

This question is useful for clarifying the architectural distinction.

A SharePoint + AI stack is primarily an information platform: storage, permissions, collaboration, indexing, search, agents and automation live inside the Microsoft ecosystem.

InfoBIM addresses a different layer. Its objective is that identity, context, relationships and executable semantics remain portable with — or independently addressable from — the engineering information itself.

The important distinction is therefore not simply **AI versus semantics**, but **platform intelligence versus portable information semantics**.

A useful framing question is:

> If an AI must reconstruct the meaning and relationships of project documents each time they are encountered, do we have structured project knowledge, or merely well-indexed documents?

InfoBIM attempts to make those relationships explicit and reusable rather than repeatedly inferred.

This is not necessarily SharePoint **or** InfoBIM. SharePoint can remain the storage/collaboration environment while InfoBIM supplies semantic identity, relationships, interoperability and executable capabilities over those resources.

## Neutrality requirement for Tokyo 2026

The Summit submission requirements explicitly state that presenters must maintain neutrality regarding their own solutions, competitor offerings and alternative technologies.

Therefore:

- InfoBIM **can and should be named and demonstrated**;
- its open-source and free nature should be stated clearly;
- the talk must not become a commercial pitch;
- competitor products should not be attacked or dismissed;
- comparisons should be architectural and evidence-based;
- limitations and current implementation boundaries should be explicit;
- the contribution should be framed as an OpenBIM approach demonstrated through InfoBIM.

The appropriate posture is not “InfoBIM is better than SharePoint/Bonsai/CDE X”, but something closer to:

> InfoBIM explores an alternative architecture in which semantic context remains portable across information environments.

## Summit submission requirements captured from the form

The submission form states:

1. **Presentation Content** — the presentation must focus on and/or include a demonstration of openBIM®.
2. **Neutrality and Conduct** — presenters must maintain neutrality regarding their own solutions, competitor offerings and alternative technologies and comply with the buildingSMART International Code of Conduct.
3. **Event Attendance** — approved presenters must purchase a ticket covering at least the presentation day (Wednesday 7 or Thursday 8 October, TBC).
4. **Travel and Expenses** — flights, accommodation, subsistence and other travel costs are the responsibility of the presenter(s).
5. Further presentation details and deadlines will be provided if accepted and must be followed strictly.
6. buildingSMART International may request revisions or withdraw approval if the presentation does not meet expectations, including after initial acceptance.
7. Requested changes to approved content are not guaranteed and no changes are accepted after the final submission deadline.
8. Submission does not guarantee a presentation slot.
9. Organizer decisions are final.

## Presentation narrative — current direction

A plausible narrative for the abstract and eventual presentation is:

1. Engineering projects already contain rich information, but it is fragmented across IFC, PDFs, spreadsheets, images, schedules, communications and other resources.
2. Current interoperability frequently focuses on moving or federating these resources into another environment.
3. ISO 21597 demonstrates that heterogeneous resources can instead be connected through explicit link structures.
4. InfoBIM extends this idea toward a semantic information mesh in which resources remain usable in their original formats.
5. Semantic identity and relationships enable deterministic queries and reusable operations over distributed project information.
6. This opens a path toward executable OpenBIM information — **Data with Brains**.
7. A local-first implementation demonstrates that this semantic layer does not inherently require a vendor-specific centralized runtime.

## Claims to support carefully

The following claims are central but should be evidenced in the paper/presentation rather than asserted rhetorically:

- semantic context can remain portable independently of a particular CDE/vendor;
- heterogeneous project resources can be linked without modifying their original contents;
- local-first execution is viable for meaningful engineering workflows;
- explicit semantics reduce dependence on repeated AI inference;
- executable capabilities can operate over semantically identified information resources;
- the approach can interoperate with existing CDEs rather than requiring their replacement.

## Demo candidates

Potential demonstration flow:

1. Start with ordinary project resources in their existing folder structure.
2. Inventory IFC, PDF, spreadsheet, image and/or schedule resources.
3. Show semantic identities and explicit links between resources.
4. Query relationships across different file types.
5. Demonstrate one deterministic capability operating on those linked resources.
6. Move/copy the project/container and repeat the query locally to demonstrate portability.
7. If practical, perform the final step offline to demonstrate independence from a central service.

## FAQ material relevant to the paper

### Why use InfoBIM instead of simply SharePoint with AI?

Because they address different architectural layers. SharePoint with AI provides intelligent services within a collaboration and information-management platform. InfoBIM aims to make semantic identity, context, relationships and executable operations explicit and portable across environments.

### Is InfoBIM a CDE?

Not exactly. It can operate with information managed by a CDE but explores a semantic layer that is not inherently tied to the physical location of the resources.

### Does InfoBIM replace a CDE?

Not necessarily. A CDE may continue providing storage, collaboration, permissions and workflow while InfoBIM supplies portable semantic relationships and executable information capabilities.

### Does InfoBIM modify the source files?

The intended model is to preserve source resources and represent semantic relationships externally.

### Is InfoBIM an AI tool?

No. AI can participate in some capabilities, but the architectural foundation is explicit semantics and deterministic processing. AI is a consumer/producer of structured context, not the sole mechanism by which meaning exists.

### What does “Data with Brains” mean?

Engineering information is not merely stored content: identities, relationships, constraints and applicable operations can also be computationally represented, queried and executed.

### What happens if InfoBIM disappears?

The architectural objective is that original resources remain usable and semantic structures rely on open representations, minimizing dependence on the continued existence of one application or vendor.

## Existing source material to consolidate next

- `infobim-whitepaper.pdf` — current InfoBIM local-first semantic mesh whitepaper.
- Current InfoBIM implementation/repositories and examples.
- OntoBDC architecture relevant to semantic capabilities and portable execution.
- ISO 21597 references and ICDD/linkset implementation evidence.
- ISO 19650 framing.
- Existing InfoBIM demo/project material.
- Current FAQ/site language, especially CDE, SharePoint + AI, portability and local-first positioning.

## Immediate objective

Prepare and submit a strong Tokyo 2026 abstract that presents InfoBIM as an open-source implementation of a broader OpenBIM architectural proposition:

**project information does not need to be physically centralized or converted into a proprietary environment in order to become semantically connected, queryable and computationally actionable.**

The paper/presentation should demonstrate that proposition rather than merely describe it.

---

Created from the InfoBIM / buildingSMART Tokyo 2026 working discussion on 12 August 2026. This document is intended to be continuously expanded as the abstract, evidence, implementation details and presentation are refined.
