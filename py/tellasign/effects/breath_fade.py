"""Effect which implements a looping in and out fade with ordered channels,
where 'lower' channels fade in later and fade out sooner.
"""

from collections import Iterable
import time

from tellasign.effects.effect import Effect

DMX_MAX_SLOT_VALUE = 255
DMX_MIN_SLOT_VALUE = 0

class BreathFader(Effect):
  """Effect which implements a looping in and out fade with ordered channels,
  where 'lower' channels fade in later and fade out sooner.
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
    Args:
      manager - Manager or Adapter object to drive.
      channels - Ordered list of channels to drive.
      cycle_period_sec - Period in seconds at which the animation should repeat.
      dwell -
      resolution_ms - Time width of each animation frame.
      min_value - Minimum value to fade to.
      max_value - Maximum value to fade to.
    """
    assert(cycle_period_sec > 0)
    assert(min_value <= max_value)

    self._manager = manager
    self._channels = list(channels)

    self._refresh = resolution_ms
    self._cycle_period = cycle_period_sec * 1000. / 2
    self._cycle_start = 0
    self._dwell = dwell
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

    # Determine whether we've hit a cycle boundary (either a forward to backward
    # transition, or a restart transition).
    if now > self._cycle_start + self._cycle_period:
      self._cycle_start = now
      self._reverse_cycle = not self._reverse_cycle

    # Calculate where in the cycle we are.
    t = now - self._cycle_start
    if self._reverse_cycle:
      t = self._cycle_period - t

    for i, channel in enumerate(self._channels):
      # Calculate the channel value, based on the equation:
      #
      #   i_c = I/T(1-d) * [t - dT(c/N)]
      #
      # where:
      #   i_c := the intensity of channel c
      #   I   := Maximum intensity
      #   T   := Cycle period (forward only)
      #   d   := 'dwell' fraction
      #   t   := time offset within the cycle
      #   N   := number of channels
      scale = self._max / (self._cycle_period * (1. - self._dwell))
      channel_offset = self._dwell * self._cycle_period * i / len(self._channels)
      value = scale * (t - channel_offset)

      # Cap the channel value to within the min and max.
      value = max(self._min, min(self._max, value))

      if not isinstance(channel, Iterable):
        channel = [channel]

      self._manager.set(channel, value)
