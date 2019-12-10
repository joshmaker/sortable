# Cython Sortable

This package includes implementations of three different sorting algorithms:
`insertion`, `quicksort`, and `bubble`. Each exist in this repo as standard
Python and as compiled Cython code to demonstrate how Cython can speedup Python
code with only minimal changes.

Pure Python versions of sort algorithms can be imported from `sortable.py.*` and
the compiled Cython version can be imported from `sortable.c.*` (after running
the build / installation steps in `setup.py`)

```
├── src/
│   └── sortable/
│       ├── c/
│       │   ├── __init__.py
│       │   └── algorithms.pyx
│       ├── py/
│       │   ├── __init__.py
│       │   └── algorithms.py
│       ├── __init__.py
│       └── benchmark.py
└── tests/
    ├── __init__.py
    └── test_sortable.py
```

## Installing

- Clone repo
- Create and activate virtual env
- Build Cython `$ python setup.py build_ext --inplace`
- Install `$ python setup.py install`

## Running performance tests

python src/sortable/benchmark.py {path to sort algorithm} {times to run}

Examples:

```bash
$ python src/sortable/benchmark.py sortable.py.quicksort 25
0.190979612

$ python src/sortable/benchmark.py sortable.c.quicksort 25
0.098417668

$ python src/sortable/benchmark.py sortable.py.insertion 25
3.468736676

$ python src/sortable/benchmark.py sortable.c.insertion 25
1.543984818

$ python src/sortable/benchmark.py sortable.py.bubble 25
13.509278025

$ python src/sortable/benchmark.py sortable.c.bubble 25
6.3449919910
```

## Running tests

Requires installing `pytest`

```bash
$ pytest
============================================= test session starts =============================================
platform darwin -- Python 3.8.0, pytest-5.3.1, py-1.8.0, pluggy-0.13.1
rootdir: /Users/josh/www/sortable
collected 24 items

tests/test_sortable.py ........................                                                         [100%]

============================================= 24 passed in 0.42s ==============================================
```
