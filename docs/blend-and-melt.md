# Blends and melt yield

## Splitting a fragrance blend (e.g. 70/30)

The fragrance load decides the combined oil amount (see `docs/fragrance-basis.md`). The blend ratio divides that oil — it never multiplies the load.

Given combined oil `F` and the fraction `p` going to oil A:

```
A = F × p
B = F - A
```

Worked example — three candles of 200 g finished mixture at 6% wax-based:

```
T = 600 g
W = 600 / 1.06 = 566.037735... g
F = 600 - W = 33.962264... g
A = F × 0.70 = 23.773584... g
B = F - A = 10.188679... g
```

Displayed: wax 566.04 g, A 23.77 g, B 10.19 g. Total check: 600.00 g.

Do **not** apply the 6% once to each oil — that would produce 12% combined oil relative to wax. Changing the split ratio alone (70/30 → 50/50) does not change the combined oil weight or the wax amount.

If you premix 100 g of a 70/30 blend, the batch still takes only the oil portion it needs (33.96 g here); the rest stays unused. Putting the whole 100 g into 566.04 g of wax would give 100 / 566.037735... = 17.67% oil relative to wax — no longer this recipe.

## Melt yield with retained mixture

Prepared mixture `B`, oil fraction `r`, retained fraction `l` (of the prepared mixture — jug residue, un-pourable material):

```
U = B × (1 - l)                  # available to pour
complete molds = floor(U / fill)
remainder = U - complete × fill
W = B / (1 + r)                  # wax in the prepared batch
F = B - W                        # oil in the prepared batch
```

Worked example — `B = 600 g`, fill 60 g, `r = 0.08`, `l = 0.03`:

```
U = 582 g → 9 complete molds, 42 g usable remainder
wax 555.555... g, oil 44.444... g
```

Nine complete molds is not "ten slightly short molds": ten molds require 600 g *delivered*, and only 582 g is available. Counts are floored before displayed weights are rounded.

## Backward: how much to prepare for a target

```
B = T / (1 - l)
```

Example — deliver 600 g (ten 60 g molds) at 3% retention:

```
B = 600 / 0.97 = 618.556701... g
W = 572.737686... g
F = 45.819015... g
```

Adding 3% instead (`600 × 1.03 = 618 g`) delivers only ~599.46 g after the same retention — short of the target. Dividing by (1 − l) is not the same as multiplying by (1 + l).

## Retention does not change the ratio

If the retained material has the same composition as the poured mixture, both portions keep the same oil-to-wax ratio (0.08 above). Do not add extra fragrance to compensate for retained mixture — loss changes the amount available, not the ratio.

## Assumptions to state

The retained fraction is an input you measure or declare; the 3% above is a hypothetical worked example, not an expected loss rate. Product suitability, fragrance restrictions and burn performance are outside this math.
