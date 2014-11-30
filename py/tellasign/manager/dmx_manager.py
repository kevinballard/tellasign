"""
"""

import array
import copy
import math
import sys
import threading
import time

from ola.ClientWrapper import ClientWrapper
from tellasign.hardware_map import MIN_VALUE, MAX_VALUE

from tellasign.hardware_map import NUM_CHANNELS

SUBFRAME_WIDTH = 3

class DmxManager(object):
  """Manager class which drives a set of channels through DMX.
  """

  def __init__(self, universe, frame_period_ms=.0001):
    """
    Args:
      universe - DMX universe to drive.
      frame_frame_period_ms - Time width of each frame.
    """
    self._wrapper = ClientWrapper()
    self._client = self._wrapper.Client()

    self._thread = None

    self._thread = None

    self._universe = universe
    self._refresh = frame_period_ms
    self._subframe = 0

    self._frame = 0
    self._start = 0

    self._data = [MIN_VALUE] * NUM_CHANNELS

  def start_background(self):
    """Start driving the DMX channels on a background thread.
    """
    self._thread = threading.Thread(target=self.start)
    self._thread.daemon = True
    self._thread.start()

  def start(self):
    """Start driving the DMX channels. This will block indefinitely.
    """
    self._start = time.time()
    self._wrapper.AddEvent(self._refresh, self._send)
    self._wrapper.Run()

  def stop(self):
    """Stop driving the DMX channels.
    """
    if self._wrapper:
      self._wrapper.Stop()

  def flush(self):
    """Flush the current channel buffer to the DMX universe.
    """
    self._client.SendDmx(self._universe, copy.copy(self._data))

  def set(self, channels, value):
    """Set the value of a collection of channels to a value in the buffer.

    Args:
      channels - Collection of channels to set.
      value - Value to set the chanels to.
    """
    for channel in channels:
      if channel <= len(self._data):
        self._data[channel - 1] = value

  def _send(self):
    """Send the channel buffer to the DMX universe.
    """
    self._frame += 1

    self._wrapper.AddEvent(self._refresh, self._send)

    self._subframe += 1
    self._subframe %= SUBFRAME_WIDTH

    packet = array.array('B', [MIN_VALUE] * NUM_CHANNELS)

    for i, logical_value in enumerate(self._data):
      fraction, whole = math.modf(logical_value)
      if self._subframe / float(SUBFRAME_WIDTH) < fraction:
        value = whole + 1
      else:
        value = whole

      packet[i] = int(min(MAX_VALUE, max(MIN_VALUE, value)))

    print >> sys.stderr, "FPS: %.2f | SEND: %s" % (
        self._frame / (time.time() - self._start),
        packet)
    self._client.SendDmx(self._universe, packet, self._result)

  def _result(self, response):
    """Callback for the DMX operation. Checks for and prints any errors.

    Args:
      response - Response object from the DMX driver.
    """
    if response.state != response.SUCCESS:
      print "ERROR in TellASign (%s): %s" % (response.state, response.message)
      print "Restarting client"
      self.stop()
      self.start()
