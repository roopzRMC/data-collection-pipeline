# %%
import os
import time
import sys
# %%
# write a timing decorator

def timer(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        total_time = time.time() - start_time
        print(f' this has taken {total_time}')
    return wrapper

# %%
@timer
def my_func(idx):
    for i in range(idx):
        pass
# %%
my_func(1000)
# %%

## create a decorator 
def word_dec(func):
    def wrapper(*args):
        print('starting word dec')
        func(*args)
        print('end word dec')
    return wrapper

# %%
@word_dec
def my_func_2(idx):
    for i in range(idx):
        pass
# %%
my_func_2(1200)
# %%

## creating a chain of decorators
def star_dec(func):
    def wrapper(*args):
        print('***********')
        func(*args)
        print('***********')
    return wrapper

def perc_dec(func):
    def wrapper(*args):
        print("%%%%%%%%%%%")
        func(*args)
        print("%%%%%%%%%%%")
    return wrapper



# %%
@star_dec
@perc_dec
def my_func_3(idx):
    for i in range(idx):
        pass
# %%
my_func_3(1000)
# %%
#Create a decorator that saves the string output from a simple function to a file using a context manager

def save_str_dec(func):
    def wrapper(*args):
        with open('string_dec_output.txt', 'w') as outfile:
            outfile.write(func(*args))
        outfile.close()
    return wrapper

@save_str_dec
def text_tester(echos):

    return str('hello world ') * echos

# %%
text_tester(3)
# %%
### Unpacking the decorator
def with_job_title(func):
    def wrapper(*args):
        job_title = 'ML Engineer'
        return func(job_title, *args)
    return wrapper

@with_job_title
def employment(job_title, start_date, finish_date):
    return job_title, start_date, finish_date
    
# %%
emp_list = [employment('02/10/22', '03/12/32')]

# %%
emp_list
# %%
## Create a temperature class

"""
Create a Temperature class that has a constructor that takes a temperature in Celsius and stores it as an attribute.
Add a method to convert the temperature of the instance to Fahrenheit
Add a static method that converts the temperature from Fahrenheit to Celsius
Add a static method that check if a temperature is valid (i.e. between -273 and +3000)
Add a class method that creates a new instance of the Temperature class given a temperature in Fahrenheit
Add a class method named standard that creates a new instance of the Temperature class with a value of 0 Celsius
Make the temperature attribute a property than can be set, get and deleted
Use the dataclass decorator to substitute the constructor

"""

class Temperature(object):
    def __init__(self, temp_c):
        self.__temp_c = temp_c

    @property
    def temp_c(self):
        print('getting temp')
        return self.__temp_c

    @temp_c.setter
    def temp_c(self, temp_c):
        print('setting temp')
        self.__temp_c = temp_c

    @temp_c.deleter
    def temp_c(self):
        print('deleting temp')
        del self.__temp_c

    @staticmethod
    def convert_celsius_to_fahrenheit(temp_c):
        return (temp_c*1.8)+32

    @staticmethod
    def temp_validity_check(temp_c):
        if temp_c <-273 or temp_c >3000:
            raise ValueError('ivalid temp')
        return temp_c
    
    @classmethod
    def convert_fahrenheit_to_celsius(cls, temp_f):
        return cls(temp_f-32)*5/9
    
    @classmethod
    def standard(cls, temp_c=0):
        return (temp_c*1.8)+32

    


# %%
myT = Temperature(3)
# %%
myT.temp_validity_check(3)
# %%
myT.standard()
# %%
del myT.temp_c
# %%

## as above but using dataclass to remove constructor
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
# %%
my_dct = DataClassTemperature(13)
# %%
my_dct.standard()
# %%

del my_dct.temp_c
# %%
my_dct = DataClassTemperature(14)
# %%
my_dct.temp_c = 13
# %%
my_dct.temp_c
# %%
