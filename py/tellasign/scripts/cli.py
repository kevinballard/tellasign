"""
"""

import commandr

from tellasign.hardware_map import CHS_ALL
from tellasign.manager.SignManager import TellASign

@commandr.command('all-off')
def all_off(universe=1, channels=list(CHS_ALL)):
  """
  """
  manager = TellASign(universe)
  manager.set(channels, 0)
  manager.flush()

@commandr.command('all-on')
def all_off(universe=1, channels=list(CHS_ALL), value=255):
  """
  """
  manager = TellASign(universe)
  manager.set(channels, value)
  manager.flush()

if __name__ == '__main__':
  commandr.Run()
