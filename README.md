# candle-math

Candle batch math you can check: wax and fragrance weights, fragrance-load basis conversion, blend splits, melt yield, and cost formulas — plus supplier-sourced reference data.

Everything here is plain arithmetic with worked examples. The Python module is dependency-free; the CSV and Markdown files can be lifted into your own docs, sheets or worksheet tools.

> The same formulas power the free in-browser calculators at [WAX / WEIGHT](https://waxweigh.com).

## What's inside

| Path | Contents |
|---|---|
| `data/wax-supplier-reference.csv` | Density / specific gravity, melting data and fragrance guidance as published in supplier documents — with source links and gaps left visible. |
| `data/fragrance-basis-conversion.csv` | Wax-based ↔ total-based fragrance load conversions. |
| `data/unit-conversions.csv` | US customary mass and volume factors (NIST-cited). |
| `docs/batch-math.md` | Splitting a finished target into wax and fragrance; wax-only mode; mixed sizes. |
| `docs/fragrance-basis.md` | Why "8%" needs a denominator; conversion formulas and table. |
| `docs/blend-and-melt.md` | 70/30 blend splits; melt yield with retained mixture; backward planning. |
| `docs/cost-math.md` | Batch cost, cost per sellable unit, leftovers, markups. |
| `python/candle_math.py` | Library + CLI implementing all of the above. |
| `python/test_candle_math.py` | Tests reproducing the worked examples in the docs. |

## Quick start

```bash
# Split a 4-candle batch: 180 g finished fill each at an 8% wax-based load
python python/candle_math.py batch --finished 180 --count 4 --load 8
# -> wax 666.67 g, fragrance 53.33 g, finished 720.00 g

# Convert a basis label
python python/candle_math.py basis --wax-based 8
# -> 8% of wax = 7.4074% of the finished mixture

# Melt yield with 3% retained mixture
python python/candle_math.py melt --prepared 600 --fill 60 --load 8 --retained 3
# -> 9 complete molds, 42.00 g usable remainder

# Cost a batch
python python/candle_math.py cost --wax 666.6667 --oil 53.3333 \
  --wax-rate 0.01 --oil-rate 0.12 --other 2.50 \
  --poured 4 --sellable 4 --labor-min 30 --hourly 12 --overhead 2
# -> batch 31.07, per sellable 7.77
```

Run the tests:

```bash
cd python && python -m unittest -v
```

## Conventions

- **Fragrance load** `r` is oil mass ÷ wax mass (the wax-based convention). Total-based labels are converted, not substituted — see `docs/fragrance-basis.md`.
- **Weights are arithmetic.** This is a calculation reference, not a validated candle recipe. Wick choice, burn behavior and safety need their own testing.
- Amounts are shown rounded to two decimals for display; calculations keep full precision.

## Limitations

This repository performs mass-balance and cost arithmetic. It does not validate candle recipes, determine a safe fragrance load or wick size, predict scent throw or burn time, or replace supplier instructions, IFRA documentation, or physical burn testing. Hypothetical examples are calculation inputs, not measured results or production recommendations.

Supplier reference values apply only to their cited products and documents; missing values remain unknown. The data is not a universal water-to-wax density conversion. Cost outputs use the rates and sellable-unit counts provided by the caller and do not establish market prices or guarantee profit.

## Data & sources

Reference rows cite the exact supplier documents they were compiled from (SDS sheets, product pages, handling sheets), including which values are *not* published. Unit factors follow NIST SP 811 Appendix B.8. Compiled October 2026; always check the current supplier document before production.

## Contributing

Corrections and additional sourced rows are welcome — open an issue or pull request with the source document link.

## License

MIT — see [LICENSE](LICENSE). The reference data belongs to its original publishers; each row links to the source document.
