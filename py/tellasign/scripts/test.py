from tellasign.adapters.hvs_intensity_adapter import HvsIntensityAdapter
from tellasign.effects.breath_fade import BreathFader
from tellasign.effects.compound_effect import CompoundEffect
from tellasign.effects.linear_flat_fade import LinearFlatFader
from tellasign import hardware_map
from tellasign.manager.SignManager import TellASign

def main():
  manager = TellASign(1)

  adapter = manager
  adapter = HvsIntensityAdapter(adapter)

  effect = LinearFlatFader(adapter,hardware_map.CHS_ALL, min_value=32)

  manager.start_background()
  effect.run()

def main_breath():
  manager = TellASign(1)

  adapter = manager
  adapter = HvsIntensityAdapter(adapter)

  effect_logo = LinearFlatFader(adapter, hardware_map.CHS_LOGO, min_value=32)
  effect_tell = BreathFader(
      adapter, 
      [   hardware_map.CHS_LETTER_L2,
          hardware_map.CHS_LETTER_L1,
          hardware_map.CHS_LETTER_E1,
          hardware_map.CHS_LETTER_T1],
      min_value=32)

  effect_apart = BreathFader(
      adapter,
      [   hardware_map.CHS_LETTER_A1,
          hardware_map.CHS_LETTER_P1,
          hardware_map.CHS_LETTER_A2,
          hardware_map.CHS_LETTER_R1,
          hardware_map.CHS_LETTER_T2],
      min_value=32)

  manager.start_background()

  effect = CompoundEffect([effect_logo, effect_tell, effect_apart])
  effect.run()

if __name__ == '__main__':
  main()
