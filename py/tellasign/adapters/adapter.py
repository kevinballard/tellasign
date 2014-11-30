"""Interface definition for Adapter classes, which are composed with a Manager
or another Adapter and apply transformations to some or all channels.
"""

import abc

class Adapter(object):
  """Interface for Adapter classes which transform input channel intensities to
  another output space.
  """
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def set(self, channels, value):
    """Set the output of a set of channels to a value.

    Args:
      channels - Set of channel numbers to set the value of.
      value - Input value to set the channels to.
    """
    raise NotImplementedError()
