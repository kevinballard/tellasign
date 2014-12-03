"""Adapter which adjusts intensity for the Human Visual System (HVS) perceived
intensity.
"""

import math

from tellasign.adapters.adapter import Adapter
from tellasign.hardware_map import MAX_VALUE

class HvsIntensityAdapter(Adapter):
  """Adapter which adjusts intensity for the Human Visual System (HVS) perceived
  intensity. Linear intensity inputs are transformed to an exponential space of
  the form:

    f(i) = alpha^i / C

  where C is calculated to scale the output to the range [0, 255].
  """

  def __init__(self, child, alpha=2):
    """
    Args:
      child - Child Adapter or Manager.
      alpha - Base used in exponentiation.
    """
    self.child = child
    self.alpha = alpha
    self.scale = float(MAX_VALUE) / math.pow(MAX_VALUE, self.alpha)

  def set(self, channels, value):
    """See interface definition.
    """
    if value == 0:
      adj_value = 0
    else:
      adj_value = math.pow(value, self.alpha) * self.scale

    self.child.set(channels, adj_value)
