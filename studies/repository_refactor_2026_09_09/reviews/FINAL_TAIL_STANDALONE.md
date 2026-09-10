# Standalone scientific library validation

Only the accepted 27 scientific files are present, without studies, data, exporter or historical dependencies.

```text
Library boundary and local links checked: 25 files.
..........................................................................................................
----------------------------------------------------------------------
Ran 106 tests in 0.878s

OK
[ 0.00585987 -0.00357566 -0.00585987]
[[ 0.08579212  0.05179866 -0.08579212]
 [ 0.05179866  0.0781826  -0.05179866]
 [-0.08579212 -0.05179866  0.08579212]]
0.7410221085761991 0.7398799811970899
[0.23145472 0.62056291 0.26424555 0.17584787]
[0.23145472 0.62056291 0.5284911  1.05508723]
[0.0346     0.07703125 0.1140625 ] [0.00843756 0.05290351 0.19226667]
8 maintained guide examples passed.
```

All seven scientific test modules and all eight maintained Python guide examples were executed with Python -B and one BLAS/OpenMP thread.
