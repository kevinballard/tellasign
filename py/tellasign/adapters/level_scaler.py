"""
"""

from tellasign.adapters.adapter import BaseAdapter

class LevelScaler(BaseAdapter):

  def __init__(self, child, channels, factor):
    """
    """
    self.child = child
    self.channels = set(channels)
    self.factor = factor

  def set(self, channels, value):
    """
    """
    channels = set(channels)
    scale_channels = channels.intersection(self.channels)
    pass_channels = channels - scale_channels

    self.child.set(scale_channels, value * self.factor)
    self.child.set(pass_channels, value)
