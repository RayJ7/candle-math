# Cost math: from weights to cost per sellable candle

## Rates from purchase packs

```
rate = pack cost / pack net mass
implied pack cost = rate × pack net mass
```

The second formula is a check: multiply your entered rate back by the pack mass — it should reproduce the pack price. Example: a 1000 g pack at 6 currency units → rate 0.006/g. A typed 0.06/g implies a 60-unit pack: a tenfold decimal error, caught before it prices a batch.

## Batch cost

```
batch cost = wax consumed × wax rate
           + fragrance consumed × oil rate
           + other materials per poured unit × poured
           + active labor minutes / 60 × hourly
           + allocated overhead
per sellable candle = batch cost / sellable count
```

Notes:

- Other materials are a per-poured-unit bundle (vessel, wick, label, packaging actually consumed).
- Active labor excludes passive curing time unless you are actually working during it.
- No taxes, sales fees or shipping-to-customer are included unless you enter them.

## Worked example

Inputs (declared, illustrative — not supplier quotes): wax 666.666... g at $0.01/g; fragrance 53.333... g at $0.12/g; other materials $2.50 per poured candle × 4; 30 active minutes at $12/h; $2 overhead.

| Cost line | Formula | Batch USD |
|---|---|---|
| Wax | 666.666... × $10 / 1000 g | 6.666... |
| Fragrance | 53.333... × $12 / 100 g | 6.40 |
| Other materials | 4 × $2.50 | 10.00 |
| Active labor | 30/60 h × $12/h | 6.00 |
| Overhead | allocated | 2.00 |
| **Batch total** | sum | **31.066...** |
| **Per sellable** | 31.066... / 4 | **7.766...** |

Rounded for display: $31.07 per batch, $7.77 per sellable candle.

## Leftover value

Buying a pack and consuming a pack are different events. In the example, 333.333... g of wax ($3.33) and 46.666... g of oil ($5.60) remain in the packs — not part of batch cost while they stay usable. Charging the full $22 pack spend to four candles would report $10.00 each instead of $7.77; the difference is exactly the leftover value divided by four.

## Yield changes the denominator

Four poured candles do not guarantee four sellable candles. With the same $31.066... batch cost: 4 units → $7.77; 3 units → $10.36; 2 units → $15.53 each. Rejected units do not remove consumed material from the numerator.

## Markup vs margin

```
markup = (price - cost) / cost
margin (before omitted charges) = (price - cost) / price
```

A candle sold at twice its recorded cost has a 100% markup but a 50% margin. Neither number establishes actual profit when expenses were omitted.

## Scope

This is a cost record method, not a pricing recommendation. Sales commissions, payment fees, postage, returns and discounts are outside it.

Illustrative inputs follow the worked batch in the batch-math and blend docs; underlying supplier cost-method references: CandleScience pricing and wholesale guides (see the web guide's source list).
