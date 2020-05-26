# Tada! - SpeedSurprises Result tables

## Algorithms

- [Sorting](https://github.com/Tada-Project/speed-surprises/blob/master/speedsurprises/lists/sorting.py)

  - [Insertion Sort](#insertion-sort)
  - [Bubble Sort](#bubble-sort)
  - [Merge Sort](#merge-sort)
  - Tim Sort I
  - Tim Sort II
  - [Python Sort](#python-sort)
  - [Wiggle Sort](#wiggle-sort)
  - [Heap Sort](#heap-sort)
  - [Quick Sort](#quick-sort)
  - [Random Partition Quick Sort](#random-partition-quick-sort)
  - [Intro Sort](#intro-sort)


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

### Python Sort

**Expect Worst-case time complexity: O(nlogn)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function python_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to indicator:  0.002434314893605747`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 3.189960465113322e-07  | 2.993960437774658e-07  |         0          |
|  2   | 3.1744674434661866e-07 | 3.1756691646575926e-07 | 0.9951431932098931 |

`O(1) constant or O(logn) logarithmic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function python_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 25
```

`Quit due to researched max size`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  25  | 6.164247662862142e-07  | 6.013342647552489e-07  |         0          |
|  50  | 9.188426554361979e-07  |  8.91502170562744e-07  | 1.4905998358436607 |
| 100  | 1.529599284998576e-06  | 1.5124425735473634e-06 | 1.664702085769447  |
| 200  | 3.1618267959594726e-06 | 2.751934463500976e-06  | 2.067094844361421  |
| 400  |  5.91229665629069e-06  | 4.958955535888672e-06  | 1.8698989659541339 |
| 800  | 1.1246859719848633e-05 | 9.330470489501956e-06  | 1.9022827124011044 |

`O(n) linear or O(nlogn) linearithmic`

---

### Wiggle Sort

**Expect Worst-case time complexity: O(n)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function wiggle_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to indicator:  0.011277950513701127`

| Size |          Mean         |         Median        |       Ratio        |
|------|-----------------------|-----------------------|--------------------|
|  1   | 8.366020188649495e-07 | 7.986261291503908e-07 |         0          |
|  2   | 8.556875771840414e-07 | 8.149755401611328e-07 | 1.0228131870216928 |

`O(1) constant or O(logn) logarithmic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function wiggle_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 25
```

`Quit due to researched max size`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  25  | 3.938760516357422e-06  | 3.7966550140380852e-06 |         0          |
|  50  | 6.843358874511718e-06  | 6.6236741638183585e-06 | 1.7374396960900982 |
| 100  | 1.4840771779378255e-05 | 1.3946045104980469e-05 | 2.1686385372325168 |
| 200  | 3.3553052827962235e-05 | 3.0738537963867175e-05 | 2.2608698069587807 |
| 400  | 5.604745706380208e-05  | 5.4768426025390626e-05 | 1.6704130426276325 |
| 800  | 0.00013075716440429688 | 0.00012391347851562498 | 2.332972292667059  |

`O(n) linear or O(nlogn) linearithmic`

---

### Heap Sort

**Expect Worst-case time complexity: O(nlogn)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function heap_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to indicator:  0.09065803189023482`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 1.1722028593699138e-06 | 1.0418929595947265e-06 |         0          |
|  2   | 1.4059314409891764e-06 | 1.2337477989196774e-06 | 1.1993926049155836 |

`O(1) constant or O(logn) logarithmic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function heap_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 25
```

`Quit due to researched max size`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  25  |  7.13459870707194e-06  | 6.963895294189453e-06  |         0          |
|  50  | 1.406882550048828e-05  | 1.4043482360839843e-05 | 1.9719154612778729 |
| 100  | 2.9160663700358075e-05 | 2.8793668823242185e-05 | 2.072714861616985  |
| 200  |  6.52137589029948e-05  | 6.253267602539063e-05  | 2.2363605840080387 |
| 400  | 0.00017103164934895835 | 0.00015168834082031243 | 2.6226313622462283 |
| 800  |  0.000322172528515625  | 0.00030969022460937504 | 1.8837012315673325 |

`O(n) linear or O(nlogn) linearithmic`

---

### Quick Sort

**Expect Worst-case time complexity: O(n^2)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function quick_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to over maximum time: 211.9507429599762`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 3.546292347272237e-07  | 3.3944345378875735e-07 |         0          |
|  2   | 1.3590765644073487e-06 | 1.3167702255249024e-06 | 3.832387269066334  |
|  4   |  3.83002790629069e-06  | 3.804722564697266e-06  | 2.818110477801408  |
|  8   | 1.1098425689697265e-05 | 1.0788862243652343e-05 | 2.8977401630595123 |
|  16  | 3.178052498372396e-05  | 3.0381406372070318e-05 | 2.8635164907421067 |
|  32  | 0.00010787689663085937 | 0.00010373415966796875 | 3.394434065708711  |
|  64  | 0.0003954205560872396  | 0.00035954054492187514 | 3.6654795274683973 |
| 128  |  0.001451803187109375  |  0.00137220704296875   | 3.671542019654313  |
| 256  |  0.005399346281770833  |   0.005262021140625    | 3.7190621495474514 |
| 512  |     0.021974467325     |  0.021032632250000002  | 4.069838491224347  |

`O(n^2) quadratic`

---

### Random Partition Quick Sort

**Expect Worst-case time complexity: O(n^2)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function random_quick_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to over maximum time: 202.9476158618927`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 3.7572151136398314e-07 | 3.4565737056732173e-07 |         0          |
|  2   | 2.982754879506429e-06  | 2.4417830047607426e-06 | 7.9387386383018725 |
|  4   | 5.340259534200032e-06  | 4.988395141601563e-06  | 1.7903782744238477 |
|  8   | 1.2775530756632487e-05 | 1.1613666534423824e-05 | 2.3923052194028345 |
|  16  |  3.19691664835612e-05  | 3.085918701171874e-05  |  2.50237482047188  |
|  32  | 0.00010278333562011718 | 9.811109472656249e-05  | 3.2150771172895354 |
|  64  | 0.00034891050032552083 | 0.00034443401855468753 | 3.3946212994592737 |
| 128  | 0.0013947162506510416  |  0.00129523112109375   | 3.9973467389196427 |
| 256  |   0.0054021078515625   |  0.004992947187499999  | 3.8732665866916243 |

`O(n^2) quadratic`

--

### Intro Sort

**Expect Worst-case time complexity: O(nlogn)**

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function intro_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
```

`Quit due to indicator:  0.07103254756469535`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  1   | 2.1118265579223633e-06 | 2.0123853302001957e-06 |         0          |
|  2   | 5.682626615905762e-06  | 5.651774230957033e-06  | 2.690858581443539  |
|  4   | 1.3066739489746093e-05 | 1.1926759429931644e-05 |  2.29941897874692  |
|  8   |  2.13048064839681e-05  | 2.0168315856933586e-05 | 1.6304607971014264 |
|  16  | 1.8478870552571614e-05 | 1.8240897155761724e-05 | 0.8673568833623058 |

`O(1) constant or O(logn) logarithmic`

---

```bash
pipenv run python tada_a_bigoh.py
  --directory ../speed-surprises/
  --module speedsurprises.lists.sorting
  --function intro_sort
  --types hypothesis
  --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json
  --startsize 25
```

`Quit due to researched max size`

| Size |          Mean          |         Median         |       Ratio        |
|------|------------------------|------------------------|--------------------|
|  25  | 4.7666535156250004e-05 | 4.252998876953126e-05  |         0          |
|  50  | 6.397039845377604e-05  | 6.138071313476561e-05  | 1.3420400338325889 |
| 100  | 0.00015452709407552082 | 0.00013641595214843751 | 2.4156031197332557 |
| 200  | 0.00031080462353515626 | 0.00029767779199218753 | 2.0113276923673924 |
| 400  | 0.0007214549737630208  | 0.0006940638359375002  | 2.321249167908258  |
| 800  |  0.00170539784453125   | 0.0016033724531250007  | 2.3638312944688753 |

`O(n) linear or O(nlogn) linearithmic`
