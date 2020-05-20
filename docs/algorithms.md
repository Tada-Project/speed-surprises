# Tada!- SpeedSurprises Result tables

## Algorithms

- [Sorting](https://github.com/Tada-Project/speed-surprises/blob/master/speedsurprises/lists/sorting.py)

  - [Insertion Sort](#insertion-sort)
  - [Bubble Sort](#bubble-sort)
  - [Merge Sort](#merge-sort)
  - Tim Sort I
  - Tim Sort II
  - Python Sort
  - Wiggle Sort
  - Heap Sort
  - Quick Sort
  - Random Partition Quick Sort
  - Intro Sort


## Result tables

Experiments of this [Tada! version](https://github.com/Tada-Project/tada/tree/20604e14bac7372b44986d548768cdb51bde605d)

### Insertion Sort

**Expect Worst-case time complexity: O(n^2)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function insertion_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to over maximum time: 203.07405996322632`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 4.643168546676636e-07  | 4.450835990905762e-07  |         0          |
|  2   | 6.460382616678874e-07  | 6.451994781494143e-07  | 1.391373703481627  |
|  4   | 9.154775557200114e-07  | 9.105169792175296e-07  | 1.4170639883720018 |
|  8   | 1.5158671759287517e-06 | 1.4726710510253907e-06 | 1.6558212339094884 |
|  16  | 2.6584736086527507e-06 | 2.4242303085327154e-06 | 1.7537642155381716 |
|  32  | 4.777526183064779e-06  | 4.690438034057617e-06  | 1.7970937035127883 |
|  64  | 9.149888982137044e-06  | 8.693221557617186e-06  | 1.9151938956548844 |
| 128  | 2.0039083243815103e-05 | 1.7955304870605473e-05 | 2.190090315077766  |
| 256  | 3.5275877490234375e-05 | 3.448298645019532e-05  | 1.7603538575609232 |
| 512  | 7.409860479329427e-05  | 7.314252661132812e-05  | 2.100546040670637  |

`O(n) linear or O(nlogn) linearithmic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function insertion_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 50
```

`Quit due to researched max size`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  50  |  6.86418919169108e-06  | 6.7079568176269555e-06 |         0          |
| 100  | 1.3429081990559896e-05 |  1.33376830444336e-05  | 1.9563974149802639 |
| 200  | 2.685947581380208e-05  | 2.6571040039062493e-05 | 2.000097685953754  |
| 400  | 5.669337211914063e-05  | 5.5352308593749995e-05 | 2.1107400796708036 |
| 800  | 0.00012105304228515625 | 0.00012028778124999998 | 2.1352238852676524 |

`O(n) linear or O(nlogn) linearithmic`

---

### Bubble Sort

**Expect Worst-case time complexity: O(n^2)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function bubble_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to end of rounds:  11`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 4.7392406183878577e-07 | 4.7124644088745097e-07 |         0          |
|  2   | 8.561745708465576e-07  | 8.538008766174317e-07  | 1.8065648904271114 |
|  4   | 1.7488648396809896e-06 | 1.7435311355590823e-06 | 2.0426498277702514 |
|  8   | 4.399077105204264e-06  |  4.38573974609375e-06  | 2.5153899863449136 |
|  16  | 1.3239032981363932e-05 | 1.3203352661132812e-05 | 3.0095023716910276 |
|  32  |  4.51899614461263e-05  | 4.514854736328124e-05  |  3.41338838793879  |
|  64  |  0.00017171766640625   | 0.00016586233935546874 | 3.7999073447089584 |
| 128  | 0.0006569106720703125  | 0.0006353636425781249  | 3.8255275989844395 |
| 256  | 0.0024867630861979168  |    0.0024761861875     | 3.7855422235121576 |
| 512  |  0.010728671450000001  |  0.010694278156249997  | 4.314311849627531  |

`O(n^2) quadratic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function bubble_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 50
```

`Quit due to researched max size`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  50  | 0.00011229182244466147 | 0.00010693458007812501 |         0          |
| 100  | 0.00044776060846354166 | 0.00043188963671874996 | 3.9874729852585884 |
| 200  |   0.001762315134375    |  0.001692661609374999  | 3.9358422805933237 |
| 400  |    0.00714774113125    |  0.007069810312499999  | 4.055881375486754  |
| 800  |  0.029786691587499997  |  0.028603233874999995  | 4.167287404586082  |

`O(n^2) quadratic`

---

### Merge Sort

**Expect Worst-case time complexity: O(nlogn)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function merge_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to over maximum time: 200.50391101837158`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 3.2961307608286543e-07 | 3.112082653045655e-07  |         0          |
|  2   | 1.4179184763590493e-06 | 1.4083027648925777e-06 | 4.301766462695132  |
|  4   | 4.043484283955892e-06  | 4.029210723876953e-06  | 2.851704347868297  |
|  8   | 1.0108870196533203e-05 | 1.0092437133789059e-05 | 2.5000394428745785 |
|  16  | 2.4568441996256512e-05 | 2.3833852050781252e-05 | 2.430384555207976  |
|  32  | 5.630571494954427e-05  | 5.464788330078124e-05  | 2.2917902143784112 |
|  64  | 0.00012407299747721354 | 0.00012184436376953128 | 2.2035595780711734 |
| 128  | 0.00026786790729166663 | 0.0002656025546874999  | 2.1589541055527537 |
| 256  |  0.000585954976953125  | 0.0005837114316406249  | 2.1874773386537525 |
| 512  | 0.0012947370872395832  |   0.0013044111171875   | 2.2096187218547323 |

`O(n) linear or O(nlogn) linearithmic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function merge_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 50
```

`Quit due to researched max size`

| Size |          Mean         |         Median         |       Ratio        |
|------|-----------------------|------------------------|--------------------|
|  50  | 9.028379369303385e-05 | 8.892282495117187e-05  |         0          |
| 100  | 0.0001965161314127604 | 0.00019620048632812496 | 2.1766490238648806 |
| 200  | 0.0004328957044921875 |    0.0004317573125     | 2.2028507348485196 |
| 400  | 0.0009842246173177084 | 0.0009445349179687502  | 2.2735836995016214 |
| 800  | 0.0020790521080729166 |   0.002064142390625    | 2.112375642197331  |

`O(n) linear or O(nlogn) linearithmic`

---
