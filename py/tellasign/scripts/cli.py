"""CLI utilities.
"""

import commandr

from tellasign.hardware_map import CHS_ALL_ALL
from tellasign.manager.dmx_manager import DmxManager

@commandr.command('all-off')
def all_off(universe=1, channels=list(CHS_ALL_ALL)):
  """Turn a set of channels off.

  Args:
    universe - DMX universe to drive.
    channels - Collection of channels to turn off. Defaults to all channels.
  """
  manager = DmxManager(universe)
  manager.set(channels, 0)
  manager.flush()

@commandr.command('all-on')
def all_off(universe=1, channels=list(CHS_ALL_ALL), value=255):
  """Turn on a set of channels.

  Args:
    universe - DMX universe to drive.
    channels - Collection of channels to turn on. Defaults to all channels.
    value - Intensity to set the channels to. Default to maximum (255)
  """
  manager = DmxManager(universe)
  manager.set(channels, value)
  manager.flush()

if __name__ == '__main__':
  commandr.Run()
