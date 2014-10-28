from tellasign.effects.linear_flat_fade import LinearFlatFader
from tellasign.hardware_map import CHS_ALL
from tellasign.manager.SignManager import TellASign

def main():
  manager = TellASign(1)
  effect = LinearFlatFader(manager, CHS_ALL)
  manager.start()
  effect.run()

if __name__ == '__main__':
  main()