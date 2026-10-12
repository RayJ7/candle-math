# Wax-melt batch yield: a reproducible arithmetic reference

This worksheet explains a mass balance for candle-making educators and wax-melt makers. All numerical inputs below are **hypothetical calculation examples**, not measured production data or recommended formulations.

Source guide: https://waxweigh.com/guides/wax-melt-calculator  
Main calculator: https://waxweigh.com/  
Published by WAX / WEIGHT. The existing repository MIT license applies.

## Name each input

- B: prepared wax-plus-oil mixture, in grams.
- r: oil mass divided by wax mass, expressed as a fraction.
- l: the fraction of prepared mixture retained and unavailable to pour.
- m: net finished mixture per complete mold, in grams.

The model assumes retained and poured material have the **same composition**. It assumes equal target mold fills and counts complete molds only. It does not approve any load, temperature, wick, cure time, scent performance, reuse of leftovers or product safety.

## Reproduce the answer

Wax W = B / (1 + r)  
Oil F = B - W  
Available mixture U = B * (1 - l)  
Complete molds N = floor(U / m)  
Available remainder R = U - N * m  

Check: N * m + R + B * l = B.

For the declared inputs B = 600 g, r = 0.08, l = 0.03 and m = 60 g:

- W = 555.555555... g; F = 44.444444... g.
- U = 582 g; N = 9; R = 42 g.
- 540 + 42 + 18 = 600 g closes the ledger.

These example values are not supplier recommendations.

## Conditional comparison table

All rows use B = 600 g and m = 60 g. Each retained fraction is a chosen illustration, not an observed loss rate. Counts use unrounded values.

| Hypothetical retained fraction | Available mixture (g) | Complete molds | Available remainder (g) | Prepared mixture needed for ten molds (g) |
| --- | ---: | ---: | ---: | ---: |
| 0% | 600.00 | 10 | 0.00 | 600.00 |
| 1% | 594.00 | 9 | 54.00 | 606.06 |
| 3% | 582.00 | 9 | 42.00 | 618.56 |
| 5% | 570.00 | 9 | 30.00 | 631.58 |

To plan backward, target poured mixture T = N * m; prepare B = T / (1 - l). Adding l to the target is a different operation. At the illustrative 3% retention, 600 * 1.03 = 618 g delivers 599.46 g; 600 / 0.97 = 618.556701... g delivers the target 600 g.

## Do not count one batch twice

A hypothetical 60 g mold containing six equal cavities gives a 10 g target per cavity. With 582 g available, one packing plan yields 58 pieces with 2 g remaining. Those pieces form nine complete six-piece packs plus four loose pieces. Do not add nine molds to 58 pieces: these are alternative representations of the same mixture.

For unequal shapes, use each shape's own net fill and a packing list rather than an average weight.

## Printable record

| Mold ID | Empty tare (g) | Filled gross mass (g) | Net finished fill = gross - tare (g) | Target quantity |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |

Record formulation ID, fill line, weighing date and instrument increment alongside the table. A water measurement is not automatically a wax-mixture measurement; no universal density multiplier is supplied here.

## What this reference does not establish

No candles or wax melts were manufactured or tested for this reference. It is arithmetic, not a validated recipe or a measurement of production waste. Consult the exact supplier documents for the intended material and product, and perform your own appropriate product checks.

The source guide contains additional worked examples, illustrations and source-linked limitations. Cite this file or the source guide when reusing the method; do not describe the hypothetical retention as a measured benchmark.
