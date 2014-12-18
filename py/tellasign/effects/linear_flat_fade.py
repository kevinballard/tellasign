"""Effect which implements a looping in and out fading animation with linear
intensity scaling.
"""

import time

from tellasign.effects.effect import Effect
from tellasign.hardware_map import MIN_VALUE, MAX_VALUE

class LinearFlatFader(Effect):
  """Effect which implements a looping in and out fading animation with linear
  intensity scaling.
  """

  def __init__(self,
      manager,
      channels,
      cycle_period_sec=10,
      resolution_ms=10,
      min_value=MIN_VALUE,
      max_value=MAX_VALUE):
    """
    Args:
      manager - Manager of Adapter class to drive the animation into.
      channels - Set of channels to apply the animation to.
      cycle_period_sec - Number of seconds the effect should run before looping.
      resolution_ms - Time width of each frame.
      min_value - Minimum value to fade to.
      max_value - Maximum value to fade to.
    """
    assert(cycle_period_sec > 0)
    assert(min_value <= max_value)

    self._manager = manager
    self._channels = channels

    self._refresh = resolution_ms
    self._cycle_period = cycle_period_sec * 1000 / 2
    self._cycle_start = time.time() * 1000
    self._reverse_cycle = False

    self._max = max_value
    self._min = min_value

    self._stop = False

  def run(self):
    """See interface definition.
    """
    while not self._stop:
      self.step()
      time.sleep(self._refresh / 1000)

  def step(self):
    """See interface definition.
    """
    now = time.time() * 1000

    # Determine whether we're on the forward or reverse phase of the fade.
    while now > self._cycle_start + self._cycle_period:
      self._cycle_start += self._cycle_period
      self._reverse_cycle = not self._reverse_cycle

    # Calculate the fraction through the loop we're at.
    fraction = (now - self._cycle_start) / self._cycle_period
    if self._reverse_cycle:
      fraction = 1.0 - fraction

    # Calculate the final value and set the channels.
    value = fraction * (self._max - self._min) + self._min
    self._manager.set(self._channels, value)
