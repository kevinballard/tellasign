"""Main entry-point for the TellASign "Breath" effect.
"""

import commandr

from tellasign.adapters.hvs_intensity_adapter import HvsIntensityAdapter
from tellasign.adapters.level_scaler import LevelScaler
from tellasign.adapters.level_shifter import LevelShifter
from tellasign.effects.breath_fade import BreathFader
from tellasign.effects.compound_effect import CompoundEffect
from tellasign.effects.linear_flat_fade import LinearFlatFader
from tellasign.hardware_map import *
from tellasign.manager.dmx_manager import DmxManager

def main(universe=1, cycle_sec=10):
  """Entry-point for the TellASign "Breath" effect.

  Args:
    universe - DMX universe to drive.
  """

  # Setup the DMX driver interface.
  manager = DmxManager(universe)

  # Setup the animation stack.
  adapter = manager
  adapter = LevelShifter(adapter, CHS_ALL, 4)
  adapter = HvsIntensityAdapter(adapter)
  adapter = LevelScaler(adapter, CHS_TELL, 0.85)

  effect_tell = BreathFader(
      adapter,
      [CHS_LETTER_L2, CHS_LETTER_L1, CHS_LETTER_E1, CHS_LETTER_T1, set()],
      cycle_period_sec=cycle_sec,
      dwell=0.50)
  effect_apart = BreathFader(
      adapter,
      [CHS_LETTER_A1, CHS_LETTER_P1, CHS_LETTER_A2, CHS_LETTER_R1, CHS_LETTER_T2],
      cycle_period_sec=cycle_sec,
      dwell=0.50)
  effect_logo = LinearFlatFader(
      adapter,
      CHS_LOGO,
      cycle_period_sec=cycle_sec)
  effect = CompoundEffect([effect_tell, effect_apart, effect_logo])

  # Run forever.
  manager.start_background()
  effect.run()

if __name__ == '__main__':
  commandr.RunFunction(main)
