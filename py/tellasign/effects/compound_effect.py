"""
"""

import time

class CompoundEffect(object):
  """
  """

  def __init__(self, effects, refresh_ms=10):
    self.effects = effects
    self.stop = False
    self.refresh = refresh_ms

  def run(self):
    while not self.stop:
      for effect in self.effects:
        effect.step()
      time.sleep(self.refresh / 1000)
