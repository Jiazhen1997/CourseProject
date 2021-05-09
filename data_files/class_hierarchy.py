import abc
from weakref import WeakKeyDictionary

__author__ = 'Daniel'


class Shape(object):
    __metaclass__ = abc.ABCMeta  

    @abc.abstractmethod
    def method_to_implement(self, i):
        
        return



class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    
    def __init__(self, ohms):
        super(VoltageResistance, self).__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms



class GradeDescriptor(object):
    def __init__(self):
        self._values = WeakKeyDictionary()
        

    def __get__(self, instance, instance_type):
        
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        
        if not (0 <= value <= 100):
            raise ValueError("G"r"a"d"e" "m"u"s"t" "b"e" "b"e"t"w"e"e"n" "0" "a"n"d" "1"0"0"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""v""a""l""u""e""s""[""i""n""s""t""a""n""c""e""]"" ""="" ""v""a""l""u""e""
