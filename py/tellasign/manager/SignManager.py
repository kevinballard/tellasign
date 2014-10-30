"""
"""
import array
import copy
import threading

from ola.ClientWrapper import ClientWrapper
from ola.DMXConstants import DMX_MIN_SLOT_VALUE, DMX_MAX_SLOT_VALUE, DMX_UNIVERSE_SIZE

from tellasign.hardware_map import NUM_CHANNELS

class TellASign(object):
  """
  """

  def __init__(self, universe, frame_period_ms=50):
    """
    """
    self._wrapper = ClientWrapper()
    self._client = self._wrapper.Client()

    self._thread = None

    self._thread = None

    self._universe = universe
    self._refresh = frame_period_ms

    self._data = array.array('B', [DMX_MIN_SLOT_VALUE] * NUM_CHANNELS)

  def start_background(self):
    """
    """
    self._thread = threading.Thread(target=self.start)
    self._thread.daemon = True
    self._thread.start()

  def start(self):
    """
    """
    self._wrapper.AddEvent(self._refresh, self._send)
    self._wrapper.Run()

  def stop(self):
    """
    """
    if self._wrapper:
      self._wrapper.Stop()

  def flush(self):
    """
    """
    self._client.SendDmx(self._universe, copy.copy(self._data))

  def set(self, channels, value):
    """
    """
    clean_value = int(min(DMX_MAX_SLOT_VALUE, max(DMX_MIN_SLOT_VALUE, value)))

    for channel in channels:
      if channel < len(self._data):
        self._data[channel - 1] = clean_value

  def flush(self):
    """
    """
    self._client.SendDmx(self._universe, copy.copy(self._data))

  def _send(self):
    """
    """
    self._wrapper.AddEvent(self._refresh, self._send)
    self._client.SendDmx(self._universe, copy.copy(self._data), self._result)

  def _result(self, response):
    """
    """
    if response.state != response.SUCCESS:
      print "ERROR in TellASign (%s): %s" % (response.state, response.message)
      print "Restarting client"
      self.stop()
      self.start()
