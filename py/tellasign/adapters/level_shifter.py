"""Adapter which applies an absolute shift to a set of channels.
"""

from tellasign.adapters.adapter import Adapter

class LevelShifter(Adapter):
  """Adapter which applies an absolute shift to a set of channels.
  """

  def __init__(self, child, channels, amount):
    """
    Args:
      child - Child Adapter of Manager.
      channels - Set of channels to scale. All other channels will be passed
          through unmodified.
      amount - Amount (positive or negative) to shift channels by.
    """
    self.child = child
    self.channels = set(channels)
    self.amount = amount

  def set(self, channels, value):
    """See interface definition.
    """
    channels = set(channels)
    shift_channels = channels.intersection(self.channels)
    pass_channels = channels - shift_channels

    self.child.set(shift_channels, value + self.amount)
    self.child.set(pass_channels, value)
