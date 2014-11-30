"""Test script for the BreathFader.
"""
import time

from tellasign.effects.breath_fade import BreathFader
from tellasign.manager import mock_manager

manager = mock_manager.MockManager(5)
effect = BreathFader(
    manager,
    [1, 2, 3, 4, 5],
    cycle_period_sec=4,
    dwell=.50)

for _ in range(1000):
  effect.step()
  time.sleep(.1)
