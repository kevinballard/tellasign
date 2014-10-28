import array
from ola.ClientWrapper import ClientWrapper

PERIOD = 100  # 0.5 seconds
FRAME_SIZE = 253

level = 0
wrapper = None

def SendFrame():
  global level
  global wrapper

  wrapper.AddEvent(PERIOD, SendFrame)

  data = array.array('B')
  for _ in range(FRAME_SIZE):
    data.append(254)#level % 255)

  level += 1

  print "Setting level %d" % (level % 255)
  wrapper.Client().SendDmx(1, data, lambda x: None)

if __name__ == '__main__':
  wrapper = ClientWrapper()
  wrapper.AddEvent(PERIOD, SendFrame)
  wrapper.Run()

