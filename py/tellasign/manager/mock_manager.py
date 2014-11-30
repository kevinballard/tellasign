"""Mock Manager which prints channels to stdout.
"""

import os

class MockManager(object):
  """Mock Manager which prints channels to stdout.
  """

  def __init__(self, num_channels):
    """
    Args:
      num_channels - Number of channels.
    """
    self.data = [0] * num_channels

    _, width  = os.popen('stty size', 'r').read().split()
    self.width = int(width) - 10

  def start_background(self):
    """See interface definition.
    """
    pass

  def start(self):
    """See interface definition.
    """
    pass

  def stop(self):
    """See interface definition.
    """
    pass

  def flush(self):
    """See interface definition.
    """
    for i, val in enumerate(self.data):
      print "%3d: " + "=" * int(val / 255.0 * self.width)
    print ""

  def set(self, channels, value):
    """See interface definition.
    """
    for channel in channels:
      self.data[channel - 1] = value
    self.flush()
