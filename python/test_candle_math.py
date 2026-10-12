#!/usr/bin/env python3
"""Reproduces the worked examples published in the docs (and on waxweigh.com).

Run:  cd python && python -m unittest -v
"""
import unittest

from candle_math import (
    batch_from_finished,
    batch_from_wax,
    wax_based_to_total_pct,
    total_based_to_wax_pct,
    split_blend,
    melt_yield,
    melt_batch_for_target,
    cost_batch,
    convert_mass,
    convert_volume,
)


class TestBatch(unittest.TestCase):
    def test_finished_split_220g_10pct(self):
        r = batch_from_finished(220, 1, 10)
        self.assertAlmostEqual(r["wax_g"], 200.0, places=9)
        self.assertAlmostEqual(r["fragrance_g"], 20.0, places=9)

    def test_four_180g_8pct(self):
        r = batch_from_finished(180, 4, 8)
        self.assertAlmostEqual(r["finished_g"], 720.0, places=9)
        self.assertAlmostEqual(r["wax_g"], 666.66666666, places=6)
        self.assertAlmostEqual(r["fragrance_g"], 53.33333333, places=6)

    def test_mixed_sizes(self):
        a = batch_from_finished(180, 3, 8)
        b = batch_from_finished(120, 2, 8)
        t = a["finished_g"] + b["finished_g"]
        self.assertAlmostEqual(t, 780.0)
        m = batch_from_finished(t, 1, 8)
        self.assertAlmostEqual(m["wax_g"], 722.22222222, places=6)
        self.assertAlmostEqual(m["fragrance_g"], 57.77777778, places=6)

    def test_wax_only(self):
        r = batch_from_wax(200, 1, 6)
        self.assertAlmostEqual(r["fragrance_g"], 12.0)
        self.assertAlmostEqual(r["finished_g"], 212.0)


class TestBasis(unittest.TestCase):
    def test_wax_to_total(self):
        self.assertAlmostEqual(wax_based_to_total_pct(6), 5.660377358, places=8)
        self.assertAlmostEqual(wax_based_to_total_pct(8), 7.407407407, places=8)
        self.assertAlmostEqual(wax_based_to_total_pct(10), 9.090909091, places=8)
        self.assertAlmostEqual(wax_based_to_total_pct(12), 10.714285714, places=8)

    def test_total_to_wax(self):
        self.assertAlmostEqual(total_based_to_wax_pct(8), 8.695652174, places=8)

    def test_roundtrip(self):
        self.assertAlmostEqual(total_based_to_wax_pct(wax_based_to_total_pct(8)), 8.0, places=9)


class TestBlend(unittest.TestCase):
    def test_70_30_breakdown(self):
        r = batch_from_finished(200, 3, 6)
        self.assertAlmostEqual(r["wax_g"], 566.03773585, places=6)
        self.assertAlmostEqual(r["fragrance_g"], 33.96226415, places=6)
        b = split_blend(r["fragrance_g"], 70)
        self.assertAlmostEqual(b["a_g"], 23.77358491, places=6)
        self.assertAlmostEqual(b["b_g"], 10.18867925, places=6)


class TestMelt(unittest.TestCase):
    def test_yield_with_retention(self):
        r = melt_yield(600, 60, 8, 3)
        self.assertAlmostEqual(r["available_g"], 582.0)
        self.assertEqual(r["complete_molds"], 9)
        self.assertAlmostEqual(r["remainder_g"], 42.0)
        self.assertAlmostEqual(r["wax_g"], 555.55555556, places=6)
        self.assertAlmostEqual(r["fragrance_g"], 44.44444444, places=6)

    def test_backward_target(self):
        r = melt_batch_for_target(600, 8, 3)
        self.assertAlmostEqual(r["prepared_g"], 618.55670103, places=6)
        self.assertAlmostEqual(r["wax_g"], 572.73768577, places=6)
        self.assertAlmostEqual(r["fragrance_g"], 45.81901526, places=6)


class TestCost(unittest.TestCase):
    def test_worked_example(self):
        r = cost_batch(666.66666666, 53.33333333, 0.01, 0.12, 2.50, 4, 4, 30, 12, 2)
        self.assertAlmostEqual(r["batch_cost"], 31.066666666, places=6)
        self.assertAlmostEqual(r["per_sellable"], 7.766666666, places=6)

    def test_yield_denominator(self):
        r = cost_batch(666.66666666, 53.33333333, 0.01, 0.12, 2.50, 4, 3, 30, 12, 2)
        self.assertAlmostEqual(r["per_sellable"], 10.355555555, places=6)


class TestUnits(unittest.TestCase):
    def test_mass(self):
        self.assertAlmostEqual(convert_mass(1, "oz", "g"), 28.349523125)
        self.assertAlmostEqual(convert_mass(1, "lb", "g"), 453.59237)

    def test_volume(self):
        self.assertAlmostEqual(convert_volume(1, "floz", "ml"), 29.5735295625)


if __name__ == "__main__":
    unittest.main()
