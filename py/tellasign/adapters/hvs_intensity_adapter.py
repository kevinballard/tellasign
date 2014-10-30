"""Adapter which adjusts intensity for the Human Visual System (HVS) percieved
intensity.
"""

import math

from tellasign.adapters.adapter import BaseAdapter
from ola.DMXConstants import DMX_MAX_SLOT_VALUE

class HvsIntensityAdapter(BaseAdapter):
  """
  """

  def __init__(self, child, alpha=2):
    """
    """
    self.child = child
    self.alpha = alpha
    self.scale = \
        float(DMX_MAX_SLOT_VALUE) / math.log(DMX_MAX_SLOT_VALUE, self.alpha)

  def set(self, channels, value):
    """
    """
    if value == 0:
      adj_value = 0
    else:
      adj_value = int(math.log(value, self.alpha) * self.scale)

    self.child.set(channels, adj_value)
