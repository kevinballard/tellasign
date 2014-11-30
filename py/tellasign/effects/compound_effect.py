"""Effect which is composed of multiple Effects (e.g. running on separate sets
of channels).
"""

import time

from tellasign.effects.effect import Effect

class CompoundEffect(Effect):
  """Effect which is composed of multiple Effects. Each effect should run on its
  own set of channels.
  """

  def __init__(self, effects, refresh_ms=10):
    """
    Args:
      effects - Collection of Effects to drive.
      refresh_ms - Time witch of each frame.
    """
    self.effects = effects
    self.stop = False
    self.refresh = refresh_ms

  def run(self):
    """See interface definition.
    """
    while not self.stop:
      self.step()
      time.sleep(self.refresh / 1000)

  def step(self):
    """See interface definition.
    """
    for effect in self.effects:
      effect.step()
