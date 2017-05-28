# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rover_msgs/Battery_level.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Battery_level(genpy.Message):
  _md5sum = "193ae58d2bb8491f232609244038c21e"
  _type = "rover_msgs/Battery_level"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 batt1
float64 batt2
float64 batt3
int32 batt
"""
  __slots__ = ['batt1','batt2','batt3','batt']
  _slot_types = ['float64','float64','float64','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       batt1,batt2,batt3,batt

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Battery_level, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.batt1 is None:
        self.batt1 = 0.
      if self.batt2 is None:
        self.batt2 = 0.
      if self.batt3 is None:
        self.batt3 = 0.
      if self.batt is None:
        self.batt = 0
    else:
      self.batt1 = 0.
      self.batt2 = 0.
      self.batt3 = 0.
      self.batt = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3di.pack(_x.batt1, _x.batt2, _x.batt3, _x.batt))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 28
      (_x.batt1, _x.batt2, _x.batt3, _x.batt,) = _struct_3di.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3di.pack(_x.batt1, _x.batt2, _x.batt3, _x.batt))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 28
      (_x.batt1, _x.batt2, _x.batt3, _x.batt,) = _struct_3di.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3di = struct.Struct("<3di")