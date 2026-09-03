# Knowledge + OWL Engineer — tiny interview demo

A deliberately small example that shows the whole semantic-engineering chain without turning interview preparation into another project.

## Story

- `taskB` depends on `taskA`
- `taskC` depends on `taskB`
- `dependsOn` is transitive in OWL, so a reasoner can infer that `taskC` also depends on `taskA`
- a SPARQL query asks which tasks depend directly or indirectly on `taskA`
- SHACL requires every task to have exactly one status
- `taskC` intentionally violates that rule

## Files

- `ontology.ttl` — OWL vocabulary
- `data.ttl` — small RDF instance graph
- `query.rq` — SPARQL query
- `shapes.ttl` — SHACL constraint
- `run_demo.py` — optional executable demo

## Optional Python setup

```bash
pip install rdflib owlrl pyshacl
python run_demo.py
```

## Talking point

"Here is the knowledge model, here are the facts, here is a useful question over the graph, here is a semantic inference, and here is a data-quality rule."
