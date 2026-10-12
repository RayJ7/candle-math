# Batch math: finished target vs wax-only

There are two different starting points, and they give different answers.

## Finished mixture target (wax + fragrance)

Let `T` be the finished wax-and-fragrance weight you want (excluding the vessel and wick), `N` the number of identical candles, and `r` the fragrance load as a fraction (oil ÷ wax).

```
W = T / (1 + r)
F = T - W
```

where `W` is wax and `F` is fragrance oil.

Worked example — four candles of 180 g finished mixture at `r = 0.08`:

```
T = 4 × 180 = 720 g
W = 720 / 1.08 = 666.666... g
F = 720 - 666.666... = 53.333... g
```

Displayed to two decimals: 666.67 g wax + 53.33 g fragrance. Keep unrounded values while calculating.

## Wax-only input

If you start from a weighed wax amount, fragrance is added **on top**:

```
F = W × r
T = W + F = W × (1 + r)
```

Example: 200 g wax at 6% → `F = 12 g`, `T = 212 g`. This is not a 200 g candle; the starting wax already weighs 200 g.

## Mixed container sizes, one recipe

When the wax product, fragrance and load stay the same, sum the finished targets first:

```
T = Σ (fill_i × count_i)
```

Example — three fills of 180 g + two fills of 120 g:

```
T = (3 × 180) + (2 × 120) = 780 g
W = 780 / 1.08 = 722.222... g
F = 780 - 722.222... = 57.777... g
```

The rule comes from linearity: dividing a sum of finished masses by the same constant equals dividing each mass first and adding.

Different loads cannot share one pitcher as a uniform recipe: a combined mixture has a single resulting oil-to-wax ratio and preserves neither original load. Keep different loads as separate recipe groups.

## Volume to weight

```
mass = volume (mL) × density (g/mL)
```

Use a density measured at matching temperature and composition. There is no universal wax density — "soy" does not determine one, and a water-weight experiment is not a wax measurement. See `data/wax-supplier-reference.csv` for which suppliers publish density data and which leave it unpublished.

## What this math does not do

No allowance for residue, spills or rejected pours is included. It does not select wicks, verify scent throw or validate a formulation. Test your wax, fragrance, wick and vessel together before making a production quantity.
