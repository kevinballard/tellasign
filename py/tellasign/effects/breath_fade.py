"""
"""

import time

from ola.DMXConstants import DMX_MAX_SLOT_VALUE, DMX_MIN_SLOT_VALUE

class BreathFader(object):
  """
  """

  def __init__(self,
      manager,
      channels,
      cycle_period_sec=10,
      dwell=0.20,
      resolution_ms=10,
      min_value=DMX_MIN_SLOT_VALUE,
      max_value=DMX_MAX_SLOT_VALUE):
    """
    """
    assert(cycle_period_sec > 0)
    assert(min_value <= max_value)

    self._manager = manager
    self._channels = list(channels)

    self._refresh = resolution_ms
    self._cycle_period = cycle_period_sec * 1000
    self._cycle_start = 0
    self._dwell = dwell
    self._reverse_cycle = False

    self._max = max_value
    self._min = min_value

    self._stop = False

  def run(self):
    """
    """
    while not self._stop:
      self.step()
      time.sleep(self._refresh / 1000)

  def step(self):
    """
    """
    now = time.time() * 1000
    if now > self._cycle_start + self._cycle_period:
      self._cycle_start = now
      self._reverse_cycle = not self._reverse_cycle

    fraction = (now - self._cycle_start) / (self._cycle_period * (1 + self._dwell))
    if self._reverse_cycle:
      fraction = 1 + self._dwell - fraction

    baseline_value = fraction * (self._max - self._min) + self._min


    for i, channel in enumerate(self._channels):
      channel_offset = float(i) / len(self._channels) * self._dwell * self._max
      self._manager.set(
          channel,
          min(baseline_value, self._max) - channel_offset)

