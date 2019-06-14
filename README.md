# Goal
System models can be boiled down to a graph of nodes and edges.
e.g.
[A: Software System] --[:calls]--> [B: API]

If this looks good, we also want to define the expectation of a well defined system model.

This for example is not what we can expect in a C4 diagram.
[A: Software System] --[:gives-satisfaction]--> [B: CEO]

This schema definition will tell that the last example is not appropriate for a C4 diagram.
