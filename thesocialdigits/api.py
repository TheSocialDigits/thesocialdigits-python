"""
This is a generic python interface for communication with The Social Digits API
version 1.

Se more: https://github.com/TheSocialDigits/thesocialdigits-python
"""
import urllib2, json, string, random
import config



class TheSocialDigitsAPI(object):
    def __init__(self, key=None, server=None):
        """
        Initializes the API object with a given configuration. If none is provided
        the default values in the module thesocialdigits.config is used.

        Keyword arguments:
        key -- Your API key (default thesocialdigits.config.key)
        server -- The destination server (default thesocialdigits.config.server)

        """
        self.__key = key if key else config.key
        self.__server = server if server else config.server

    def __getattr__(self, name):
        def __call(**kwargs):
            timeout = kwargs.pop('timeout', None)
            
            response = self.__call(name, kwargs, timeout)

            if 'result' in response:
                return response['result']
            elif 'results' in response:
                return response['results']

        return __call

    def __call(self, method, args, timeout=1):
        # build request
        args['key'] = self.__key
        url = 'http://%s/%s' % (self.__server, method)
        data = json.dumps(args)
        request = urllib2.Request(url, data, {'Content-type': 'application/json'})
        
        # call the server and fetch/decode response
        response = json.load(urllib2.urlopen(request, timeout=timeout))

        # handle response
        if response['status'] == 'ok':
            return response
            
        elif response['status'] == 'error':
            t = response['type']
            m = response['message']
            
            if t == 'AuthenticationError':
                raise AuthenticationError(m)
            elif t == 'ParsingError':
                raise ParsingError(m)
            elif t == 'LogicalError':
                raise LogicalError(m)
            elif t == 'DownForMaitenence':
                raise DownForMaitenence(m)
            else:
                raise InternalError(m)
                
        else:
            raise InternalError('Unknown response!')



# Exceptions 
class AuthenticationError(Exception):
    pass

class ParsingError(Exception):
    pass

class LogicalError(Exception):
    pass

class InternalError(Exception):
    pass

class DownForMaitenence(Exception):
    pass

