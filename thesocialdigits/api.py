"""
This is a generic python interface for communication with The Social Digits API
version 1.

Se more: www.thesocialdigits.com/documentation/language-binding/python
"""
import urllib2, json, string, random
import config



# Exceptions (http://www.thesocialdigits.com/documentation/api/occuring-errors)
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



### API Methods ###

def add_product(id, name, description, price, category, rating=.5, **attributes):
    """
    Adds a product. If the product already exists it is updated with the given
    information.
    """
    args = {'id': id,
            'name': name,
            'description': description,
            'price': price,
            'category': category,
            'rating': rating}
    args.update(attributes)
    
    __call('add_product', args, config.timeout_single)

def add_sale(customer, sale, products, visitor=None):
    """
    Adds a sale made by a visitor.
    """
    args = {'customer': customer,
            'visitor': visitor,
            'sale': sale,
            'products': products}
    
    __call('add_sale', args, config.timeout_single)
    
def alternative(products, limit, visitor=None, exclude=None, filter=None):
    """
    Returns a list of product alternatives.
    """
    args = {'products': products,
            'limit': limit,
            'visitor': visitor,
            'exclude': exclude,
            'filter': filter}

    result = __call('alternative', args, config.timeout_single)
    
    return result['result']

def being_watched(limit, visitor=None, exclude=None):
    """
    Returns a list of products currently being watched.
    """
    args = {'limit': limit,
            'visitor': visitor,
            'exclude': exclude}

    result = __call('being_watched', args, config.timeout_single)
    
    return result['result']

def bundle(product, visitor=None, exclude=None):
    """
    Returns products that may be sold as a bundle with the given product if 
    such products exists.
    """
    args = {'product': product,
            'visitor': visitor,
            'exclude': exclude}

    result = __call('bundle', args, config.timeout_single)
    
    return result['result']  

def campaign_customers(keywords, language, products, strength, exclude=None):
    """
    Resurns a list of customers that are likely to be interested in the
    campaign as described by it's keywords and sample products.
    """
    args = {'keywords': keywords,
            'language': language,
            'products': products,
            'strength': strength,
            'exclude': exclude}

    result = __call('campaign_customers', args, config.timeout_mult)

    return result['results']

def category_popular(category, limit, visitor=None, exclude=None, filter=None):
    """
    Returns the most popular products in the category.
    """
    args = {'category': category,
            'limit': limit,
            'visitor': visitor,
            'exclude': exclude,
            'filter': filter}

    result = __call('category_popular', args, config.timeout_single)
    
    return result['result']

def customer_related(customers, limit, exclude=None, filter=None):
    """
    Returns a dict of related products for each customer.
    """
    args = {'customers': customers,
            'limit': limit,
            'exclude': exclude,
            'filter': filter}

    result = __call('customer_related', args, config.timeout_multi)
    
    return result['results']

def popular(limit, visitor=None, exclude=None, filter=None):
    """
    Returns the most popular products.
    """
    args = {'limit': limit,
            'visitor': visitor,
            'exclude': exclude,
            'filter': filter}

    result = __call('popular', args, config.timeout_single)
    
    return result['result']

def related(products, limit, visitor=None, exclude=None, filter=None):
    """
    Returns a list of related products.
    """
    args = {'products': products,
            'limit': limit,
            'visitor': visitor,
            'exclude': exclude,
            'filter': filter}

    result = __call('related', args, config.timeout_single)
    
    return result['result']  

def remove_product(id):
    """
    Removes a product.
    """
    
    args = {'id': id}
    
    result = __call('remove_product', args, config.timeout_single)

def search(query, language, limit, longtail=False, visitor=None, exclude=None, filter=None):
    """
    Returns the products the customer is most likely to by based on the query.
    """
    args = {'query': query,
            'language': language,
            'limit': limit,
            'longtail': longtail,
            'visitor': visitor,
            'exclude': exclude,
            'filter': filter}

    result = __call('search', args, config.timeout_single)
    
    return (result['result'], result['hits'])

def search_suggestions(query, language, limit):
    """
    Returns a list of search suggestions for a partial query.
    """
    args = {'query': query,
            'language': language,
            'limit': limit}

    result = __call('search_suggestions', args, config.timeout_single)
    
    return result['result']

def visitor_related(limit, visitor=None, exclude=None, filter=None):
    """
    Returns products related to the visitor.
    """
    args = {'visitor': visitor,
            'limit': limit,
            'exclude': exclude,
            'filter': filter}

    result = __call('visitor_related', args, config.timeout_single)
    
    return result['result']   



### Lowlevel stuff ###

def __call(method, args, timeout):
    """
    Function to tale care of the RPC and handle any error that may occur.
    """
    # remove unset values
    for k, v in args.items():
        if v == None:
            del args[k]

    # automaticly get visitor id
    if 'visitor' not in args:
        vid = config.get_visitor_id()
        
        if vid:
            args['visitor'] = vid

    # build request
    args['key'] = config.key
    url = 'http://%s/%s' % (config.server, method)
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

