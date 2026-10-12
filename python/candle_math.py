#!/usr/bin/env python3
"""candle_math - batch, fragrance, blend, melt and cost math for candle making.

Companion to the free web calculators at https://waxweigh.com. Pure standard library.

Conventions
- Fragrance load r = oil mass / wax mass (wax-based), unless a function says otherwise.
- Functions return raw floats; round only for display.
- Weights are arithmetic, not recipe validation.
"""
from __future__ import annotations

import argparse
import math

G_PER_OZ = 28.349523125
G_PER_LB = 453.59237
ML_PER_FLOZ = 29.5735295625

_MASS_TO_G = {"g": 1.0, "oz": G_PER_OZ, "lb": G_PER_LB, "kg": 1000.0}
_VOL_TO_ML = {"ml": 1.0, "floz": ML_PER_FLOZ, "l": 1000.0}


def batch_from_finished(finished_g, count=1, load_pct=6.0):
    """Split a finished wax+oil target into wax and fragrance.

    T = finished_g * count; W = T / (1 + r); F = T - W.
    """
    r = load_pct / 100.0
    t = finished_g * count
    wax = t / (1.0 + r)
    return {"finished_g": t, "wax_g": wax, "fragrance_g": t - wax}


def batch_from_wax(wax_g, count=1, load_pct=6.0):
    """Fragrance added on top of a weighed wax amount. F = W*r; T = W*(1+r)."""
    w = wax_g * count
    f = w * load_pct / 100.0
    return {"wax_g": w, "fragrance_g": f, "finished_g": w + f}


def wax_based_to_total_pct(wax_pct):
    """8% of wax -> % of the finished mixture: 100*r/(1+r)."""
    r = wax_pct / 100.0
    return 100.0 * r / (1.0 + r)


def total_based_to_wax_pct(total_pct):
    """% of the finished mixture -> % of wax: 100*q/(1-q)."""
    q = total_pct / 100.0
    return 100.0 * q / (1.0 - q)


def split_blend(oil_g, a_pct=70.0):
    """Split combined fragrance oil into two weighed components."""
    a = oil_g * a_pct / 100.0
    return {"a_g": a, "b_g": oil_g - a}


def melt_yield(prepared_g, fill_g, load_pct=8.0, retained_pct=0.0):
    """Complete-mold yield from a prepared batch.

    U = B*(1-l); complete = floor(U/fill); remainder = U - complete*fill.
    """
    r = load_pct / 100.0
    l = retained_pct / 100.0
    u = prepared_g * (1.0 - l)
    complete = int(math.floor(u / fill_g)) if fill_g > 0 else 0
    remainder = u - complete * fill_g
    wax = prepared_g / (1.0 + r)
    return {
        "prepared_g": prepared_g,
        "available_g": u,
        "retained_g": prepared_g - u,
        "complete_molds": complete,
        "remainder_g": remainder,
        "wax_g": wax,
        "fragrance_g": prepared_g - wax,
    }


def prepared_for_target(target_g, retained_pct=0.0):
    """B = T/(1-l): amount to prepare in order to deliver target_g."""
    l = retained_pct / 100.0
    return target_g / (1.0 - l)


def melt_batch_for_target(target_g, load_pct=8.0, retained_pct=0.0):
    """Backward planning: prepare amount and its wax/fragrance split."""
    b = prepared_for_target(target_g, retained_pct)
    r = load_pct / 100.0
    wax = b / (1.0 + r)
    return {"prepared_g": b, "wax_g": wax, "fragrance_g": b - wax}


def cost_batch(wax_g, oil_g, wax_rate, oil_rate, other_per_poured,
               poured, sellable, labor_min=0.0, hourly=0.0, overhead=0.0):
    """Batch cost and cost per sellable unit (rates: currency per gram)."""
    wax_cost = wax_g * wax_rate
    oil_cost = oil_g * oil_rate
    materials = other_per_poured * poured
    labor = labor_min / 60.0 * hourly
    batch = wax_cost + oil_cost + materials + labor + overhead
    per = batch / sellable if sellable else None
    return {
        "wax_cost": wax_cost, "oil_cost": oil_cost, "materials": materials,
        "labor": labor, "overhead": overhead,
        "batch_cost": batch, "per_sellable": per,
    }


def convert_mass(value, frm, to):
    f, t = frm.lower(), to.lower()
    if f not in _MASS_TO_G or t not in _MASS_TO_G:
        raise ValueError("mass units: " + ", ".join(sorted(_MASS_TO_G)))
    return value * _MASS_TO_G[f] / _MASS_TO_G[t]


def convert_volume(value, frm, to):
    f, t = frm.lower(), to.lower()
    if f not in _VOL_TO_ML or t not in _VOL_TO_ML:
        raise ValueError("volume units: " + ", ".join(sorted(_VOL_TO_ML)))
    return value * _VOL_TO_ML[f] / _VOL_TO_ML[t]


def _r2(x):
    return "%.2f" % x


def main(argv=None):
    p = argparse.ArgumentParser(description="Candle batch math (companion to waxweigh.com).")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("batch", help="split a finished target into wax + fragrance")
    b.add_argument("--finished", type=float, required=True)
    b.add_argument("--count", type=float, default=1)
    b.add_argument("--load", type=float, default=6.0)

    w = sub.add_parser("wax", help="fragrance on top of a weighed wax amount")
    w.add_argument("--wax", type=float, required=True)
    w.add_argument("--count", type=float, default=1)
    w.add_argument("--load", type=float, default=6.0)

    c = sub.add_parser("basis", help="convert fragrance load bases")
    g = c.add_mutually_exclusive_group(required=True)
    g.add_argument("--wax-based", type=float)
    g.add_argument("--total-based", type=float)

    s = sub.add_parser("blend", help="split combined oil into A/B")
    s.add_argument("--oil", type=float, required=True)
    s.add_argument("--a", type=float, default=70.0)

    m = sub.add_parser("melt", help="melt yield from a prepared batch")
    m.add_argument("--prepared", type=float, required=True)
    m.add_argument("--fill", type=float, required=True)
    m.add_argument("--load", type=float, default=8.0)
    m.add_argument("--retained", type=float, default=0.0)

    mb = sub.add_parser("melt-target", help="prepare amount for a delivered target")
    mb.add_argument("--target", type=float, required=True)
    mb.add_argument("--load", type=float, default=8.0)
    mb.add_argument("--retained", type=float, default=0.0)

    co = sub.add_parser("cost", help="batch cost and per-sellable cost")
    co.add_argument("--wax", type=float, required=True)
    co.add_argument("--oil", type=float, required=True)
    co.add_argument("--wax-rate", type=float, required=True)
    co.add_argument("--oil-rate", type=float, required=True)
    co.add_argument("--other", type=float, default=0.0)
    co.add_argument("--poured", type=float, default=1)
    co.add_argument("--sellable", type=float, default=1)
    co.add_argument("--labor-min", type=float, default=0.0)
    co.add_argument("--hourly", type=float, default=0.0)
    co.add_argument("--overhead", type=float, default=0.0)

    u = sub.add_parser("units", help="mass/volume unit conversion")
    u.add_argument("value", type=float)
    u.add_argument("frm")
    u.add_argument("to")
    u.add_argument("--kind", choices=["mass", "volume"], default="mass")

    a = p.parse_args(argv)

    if a.cmd == "batch":
        r = batch_from_finished(a.finished, a.count, a.load)
        print("wax %s g + fragrance %s g = finished %s g" % (_r2(r["wax_g"]), _r2(r["fragrance_g"]), _r2(r["finished_g"])))
    elif a.cmd == "wax":
        r = batch_from_wax(a.wax, a.count, a.load)
        print("wax %s g + fragrance %s g = finished %s g" % (_r2(r["wax_g"]), _r2(r["fragrance_g"]), _r2(r["finished_g"])))
    elif a.cmd == "basis":
        if a.wax_based is not None:
            print("%g%% of wax = %.4f%% of the finished mixture" % (a.wax_based, wax_based_to_total_pct(a.wax_based)))
        else:
            print("%g%% of the mixture = %.4f%% of wax" % (a.total_based, total_based_to_wax_pct(a.total_based)))
    elif a.cmd == "blend":
        r = split_blend(a.oil, a.a)
        print("A %s g + B %s g = combined %s g" % (_r2(r["a_g"]), _r2(r["b_g"]), _r2(a.oil)))
    elif a.cmd == "melt":
        r = melt_yield(a.prepared, a.fill, a.load, a.retained)
        print("available %s g -> %d complete molds, remainder %s g (wax %s g, fragrance %s g)" % (
            _r2(r["available_g"]), r["complete_molds"], _r2(r["remainder_g"]), _r2(r["wax_g"]), _r2(r["fragrance_g"])))
    elif a.cmd == "melt-target":
        r = melt_batch_for_target(a.target, a.load, a.retained)
        print("prepare %s g -> wax %s g + fragrance %s g" % (_r2(r["prepared_g"]), _r2(r["wax_g"]), _r2(r["fragrance_g"])))
    elif a.cmd == "cost":
        r = cost_batch(a.wax, a.oil, a.wax_rate, a.oil_rate, a.other, a.poured, a.sellable, a.labor_min, a.hourly, a.overhead)
        per = _r2(r["per_sellable"]) if r["per_sellable"] is not None else "undefined (0 sellable)"
        print("batch %s; per sellable %s" % (_r2(r["batch_cost"]), per))
    elif a.cmd == "units":
        conv = convert_mass if a.kind == "mass" else convert_volume
        print("%g %s = %.10g %s" % (a.value, a.frm, conv(a.value, a.frm, a.to), a.to))


if __name__ == "__main__":
    main()
