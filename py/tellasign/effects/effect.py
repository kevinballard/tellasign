"""Interface for classes that implement Effects, which drive top level
animations on a set of channels.
"""
import abc

class Effect(object):
  """Interface for classes that implement Effects, which drive top level
  animations on a set of channels.
  """
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def run(self):
    """Start running the animation. This blocks indefinitely.
    """
    raise NotImplementedError()

  def step(self):
    """Execute a single frame of the animation.
    """
    raise NotImplementedError()
