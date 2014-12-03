"""Adapter which applies a linear scaling to a set of channels.
"""

from tellasign.adapters.adapter import Adapter

class LevelScaler(Adapter):
  """Adapter which applies a linear scaling to a set of channels.
  """

  def __init__(self, child, channels, factor):
    """
    Args:
      child - Child Adapter of Manager.
      channels - Set of channels to scale. All other channels will be passed
          through unmodified.
      factor - Scaling factor to apply.
    """
    self.child = child
    self.channels = set(channels)
    self.factor = float(factor)

  def set(self, channels, value):
    """See interface definition.
    """
    channels = set(channels)
    scale_channels = channels.intersection(self.channels)
    pass_channels = channels - scale_channels

    self.child.set(scale_channels, value * self.factor)
    self.child.set(pass_channels, value)
