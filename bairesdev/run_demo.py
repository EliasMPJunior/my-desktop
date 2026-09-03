from pathlib import Path

from rdflib import Graph, Namespace
from owlrl import DeductiveClosure, OWLRL_Semantics
from pyshacl import validate

BASE = Path(__file__).parent
EX = Namespace("https://example.org/bairesdev/demo#")

# Load ontology + data into one RDF graph.
graph = Graph()
graph.parse(BASE / "ontology.ttl", format="turtle")
graph.parse(BASE / "data.ttl", format="turtle")

print("1) OWL inference")
print("Before reasoning, taskC dependsOn taskA:", (EX.taskC, EX.dependsOn, EX.taskA) in graph)
DeductiveClosure(OWLRL_Semantics).expand(graph)
print("After reasoning,  taskC dependsOn taskA:", (EX.taskC, EX.dependsOn, EX.taskA) in graph)

print("\n2) SPARQL")
query = (BASE / "query.rq").read_text(encoding="utf-8")
for row in graph.query(query):
    print("-", row.task)

print("\n3) SHACL validation")
conforms, report_graph, report_text = validate(
    graph,
    shacl_graph=str(BASE / "shapes.ttl"),
    inference="rdfs",
    abort_on_first=False,
)
print("Conforms:", conforms)
print(report_text)
