# Algorithms for Cubical Surfaces

This repository contains the Python implementations of the algorithms
presented in the paper

> Discrete movies for cubical knotted surfaces: An algorithm

The programs were developed to compute and visualize cubical knotted
surfaces and their sections.

## Repository contents

The repository contains the following files and folders:

* `CUBGRAPH.py`: Python implementation of the algorithms used to graph
  cubical knotted surfaces.
* `LIST OF BARYCENTERS/`: collection of barycenter lists corresponding
  to examples of cubical 2-knots.

## Requirements

The programs require Python 3 and the following package:

* `matplotlib`

## Running the program

To graph a cubical knotted surface from a given list of barycenters,
copy the list of barycenters and paste it into the
`LoadListBarycenters()` function in `CUBGRAPH.py`.

Then run the program.

The program produces a three-dimensional visualization of the
corresponding cubical knotted surface.

## Examples

The folder `LIST OF BARYCENTERS/` contains barycenter lists for
trivial and nontrivial cubical 2-knots, including the examples
presented in the paper.

## Relation to the algorithms in the paper

The Python programs in this repository implement the algorithms
described in the paper. The algorithms are presented in pseudocode in
the paper, while their computational implementations are provided here.

## License

Apache License 2.0
