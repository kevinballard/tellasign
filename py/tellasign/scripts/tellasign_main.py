"""Main entry-point for the TellASign.
"""

import commandr

from tellasign import hardware_map
from tellasign.adapters.hvs_intensity_adapter import HvsIntensityAdapter
from tellasign.adapters.level_scaler import LevelScaler
from tellasign.adapters.level_shifter import LevelShifter
from tellasign.effects.linear_flat_fade import LinearFlatFader
from tellasign.manager.dmx_manager import DmxManager

def main(universe=1):
  """Entry-point for the TellASign

  Args:
    universe - DMX universe to drive.
  """

  # Setup the DMX driver interface.
  manager = DmxManager(universe)

  # Setup the animation stack.
  adapter = manager
  adapter = LevelShifter(adapter, hardware_map.CHS_ALL, 4)
  adapter = HvsIntensityAdapter(adapter)
  adapter = LevelScaler(adapter, hardware_map.CHS_TELL, 0.85)

  effect = LinearFlatFader(
      adapter,
      hardware_map.CHS_ALL,
      cycle_period_sec=12)

  # Run forever.
  manager.start_background()
  effect.run()

if __name__ == '__main__':
  commandr.RunFunction(main)
