import array
import functools

import commandr
from ola.ClientWrapper import ClientWrapper
from ola.DMXConstants import DMX_MIN_SLOT_VALUE, DMX_MAX_SLOT_VALUE, DMX_UNIVERSE_SIZE

DELAY = 100

client = None
wrapper = None

@commandr.command('set')
def Set(address=0, value=DMX_MAX_SLOT_VALUE):
  global client
  global wrapper
  wrapper = ClientWrapper()
  client = wrapper.Client()
  wrapper.AddEvent(DELAY, functools.partial(SendFrame, address, value))
  wrapper.Run()

def SendFrame(address, value):
  global client
  global wrapper
  
  data = array.array('B')
  for i in range(35):
    if i == address:
      data.append(value)
    else:
      data.append(DMX_MIN_SLOT_VALUE)

  #print "Setting %d to %d" % (address, value)
  def x(r):
    print r.state, r.message
  client.SendDmx(1, data, x)
  print data
  wrapper.AddEvent(DELAY, functools.partial(SendFrame, address, value))

if __name__ == '__main__':
  commandr.Run()

