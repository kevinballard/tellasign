"""
"""
import array
import copy

from ola.ClientWrapper import ClientWrapper
from ola.DMXConstants import DMX_MIN_SLOT_VALUE, DMX_MAX_SLOT_VALUE, DMX_UNIVERSE_SIZE

from tellasign.hardware_map import NUM_CHANNELS

class TellASign(object):
  """
  """

  def __init__(self, universe, frame_period_ms=50):
    """
    """
    self._wrapper = None
    self._client = None

    self._universe = universe
    self._refresh = frame_period_ms

    self._data = array.array('B', [DMX_MIN_SLOT_VALUE] * NUM_CHANNELS)

  def start(self):
    """
    """
    self._wrapper = ClientWrapper()
    self._client = self._wrapper.Client()
    self._wrapper.AddEvent(self._refresh, self._send)

  def stop(self):
    """
    """
    if self._wrapper:
      self._wrapper.Stop()

  def set(self, channels, value):
    """
    """
    clean_value = min(DMX_MAX_SLOT_VALUE, max(DMX_MIN_SLOT_VALUE, value))

    for channel in channels:
      if channel < len(self._data):
        self._data[channel] = clean_value

  def _send(self):
    """
    """
    self._wrapper.AddEvent(self._refresh, self._send)
    self._client.SendDmx(self._universe, copy.copy(self._data), self._on_error)

  def _on_error(self, message):
    """
    """
    print "ERROR in TellASign: %s" % message
    print "Restarting client"
    self.stop()
    self.start()
