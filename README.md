Python bindings for The Social Digits API
=========================================

This is a simple language binding for accessing The Social Digits API from Python.


Setup
=====

Installation
------------

Install the plugin via distutils with the following command:

    sudo python setup.py install


Configuration
-------------

The plugin can either be configured statically or dynamically. To configure it statically
simply insert your API key in the file _thesocialdigits/api/config.py_ file before 
installing. The API key can also be given dynamically upon the initialization of the
API object:

```python
from thesocialdigits.api import TheSocialDigitsAPI

api = TheSocialDigitsAPI('your_api_key')
```


Usage
=====

After the initialization of the API object each API method is accessible as an normal
object method. All arguments must be given as keyword arguments.

Here is a simple usage example:

```python
from thesocialdigits.api import TheSocialDigitsAPI

api = TheSocialDigitsAPI('your_api_key')

# Returns a list of the 20 most popular products with a price lower than 200.
api.popular(limit=20,
            filter='price < 200')

# Returns a list of the 16 product that is most likely to be bought with 
# products 1, 2 and 3.
api.related(products=[1,2,3],
            limit=16)

# Raises an exception since the API does not have an API name 'no_such_method'.
api.no_such_method()
```