'''
This module represents a class for converting celsius to fahrenheit
'''

from dataclasses import dataclass

@dataclass(order=True)

class DataClassTemperature(object):
    temp_c: int

    @property
    def temp_c(self):
        print('getting temp')
        return self.__temp_c

    @temp_c.setter
    def temp_c(self, temp_c):
        '''
        This function sets / mutates the object to a specified temperature

        Args:
            temp_c (int): set or mutate the temperature

        Returns:
            confirmtion of setting temperature
        
        '''
        print('setting temp')
        self.__temp_c = temp_c

    @temp_c.deleter
    def temp_c(self):
        '''
        This function deletes current value of the temperature from the objects' properties

        Args:
            NONE

        Returns:
            confirmtion of deletion through print statement
        
        '''
        print('deleting temp')
        del self.__temp_c

    @staticmethod
    def convert_celsius_to_fahrenheit(temp_c):
        '''
        This function converts any value from celsius to tempperature

        Args:
            temp_c (int): input to be converted to fahrenheit

        Returns:
            (int): fahrenheit value
        
        '''        
        return (temp_c*1.8)+32

    @staticmethod
    def temp_validity_check(temp_c):
        '''
        This function checks that the celsius temperature given is within 2 bounds

        Args:
            temp_c (int): temp to be checked for validity
        
        Returns:
            temp_c (int): submitted celsius temp if valid otherwise a value error

        
        '''
        if temp_c <-273 or temp_c >3000:
            raise ValueError('invalid temp')
        return temp_c
    
    @classmethod
    def convert_fahrenheit_to_celsius(cls, temp_f):
        '''
        This function is class methof to convert fahrenheit to celsius

        Args:
            temp_f (int): temp is f to be converted
        
        Returns:
            int: celsius
        '''
        return cls(temp_f-32)*5/9
    
    @classmethod
    def standard(cls, temp_c=0):
        '''
        This function converts a preset value for celsius (0) to fahrenheit

        Args:
            temp_c (int): set at freezing point of water

        Returns:
            (int): fahrenheit conversion of 0 celsius
        
        '''        
        return (temp_c*1.8)+32

if __name__ == '__main__':
    DataClassTemperature().main()