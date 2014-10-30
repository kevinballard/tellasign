from tellasign.adapters.hvs_intensity_adapter import HvsIntensityAdapter
from tellasign.effects.linear_flat_fade import LinearFlatFader
from tellasign.hardware_map import CHS_ALL
from tellasign.manager.SignManager import TellASign

def main():
  manager = TellASign(1)

  adapter = manager
  adapter = HvsIntensityAdapter(adapter)

  effect = LinearFlatFader(adapter, CHS_ALL)

  manager.start_background()
  effect.run()

if __name__ == '__main__':
  main()
