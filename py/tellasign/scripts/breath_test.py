import time
from tellasign.effects.breath_fade import BreathFader

class MockAdapter(object):
  def __init__(self):
    self.data = [0] * 5
  def set(self, channels, value):
    for channel in channels:
      self.data[channel - 1] = value
adapter = MockAdapter()
effect = BreathFader(adapter, [1, 2, 3, 4, 5])

for _ in range(1000):
  effect.step()
  time.sleep(.1)
  print adapter.data
