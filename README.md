# Goal
[![Build Status](https://travis-ci.org/zalum/system-model-schema.svg?branch=master)](https://travis-ci.org/zalum/system-model-schema)

System models can be boiled down to a graph of nodes and edges.
```
[A: Software System] --[:calls]--> [B: API]
```

We also want to define the expectation of a well defined system model.

This, for example is not what we can expect in a C4 diagram.
```
[A: Software System] --[:gives-satisfaction]--> [B: CEO]
```
A schema definition will tell that the last example is not appropriate for a C4 diagram.
