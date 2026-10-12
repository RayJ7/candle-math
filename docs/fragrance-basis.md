# Fragrance load: the denominator matters

"8% fragrance" is incomplete without its reference weight. Two conventions are common:

- **Wax-based**: oil as a percentage of wax weight — `F = r × W`.
- **Total-based**: oil as a percentage of the finished mixture — `F = q × T`.

A label that only says "8%" does not tell you which one; two calculators can return different amounts while each follows its own stated formula.

## Converting between the two

Given wax-based fraction `r` and total-based fraction `q`:

```
total-based % = 100 × r / (1 + r)
wax-based %   = 100 × q / (1 - q)
```

## Worked comparison — 200 g finished mixture

| Stated convention | Wax | Fragrance | Total |
|---|---|---|---|
| 8% of wax | 185.19 g | 14.81 g | 200.00 g |
| 8% of total | 184.00 g | 16.00 g | 200.00 g |

Wax-based: `W = 200 / 1.08 = 185.185...`, `F = 200 − W = 14.814...`
Total-based: `F = 0.08 × 200 = 16`, `W = 184`

Same target weight, different recipes — the total-based one contains about 1.19 g more oil.

## Conversion table

| Wax-based load | Equivalent total-based load | Oil for a 200 g finished mixture |
|---|---|---|
| 6% | 5.6604% | 11.32 g |
| 8% | 7.4074% | 14.81 g |
| 10% | 9.0909% | 18.18 g |
| 12% | 10.7143% | 21.43 g |

Machine-readable copy: `data/fragrance-basis-conversion.csv`.

## Recover the convention from a recorded recipe

For a record of 184 g wax + 16 g oil (200 g mixture):

- wax-based = `16 / 184 = 8.6957%`
- total-based = `16 / 200 = 8%`

Both labels describe the same recorded mixture. When a note only lists weights and no convention, calculate both labels instead of guessing what the author meant.

## Record-keeping

Name the denominator on every saved recipe, next to the weighed wax and oil. A supplier figure that does not state its basis should be clarified with that supplier, not silently assumed.

## Sources behind the examples

- CandleWaxCalculator.com fragrance calculator — wax-weight denominator.
- Midwest Fragrance Company fragrance-load guide — total-mixture denominator.
- CandleScience Golden Brands 464 application table — container 10% / tealight 6%, wax-based (see `data/wax-supplier-reference.csv`).

Numerical comparisons here are arithmetic, not laboratory results or safe-use recommendations.
