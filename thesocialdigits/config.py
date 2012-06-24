"""
Configuration for The Social Digits API.
"""

# Your API key.
key = ''

# Request timeout in seconds for that only return a single result set.
timeout_single = 1

# Request timeout in seconds for that only return multiple result sets.
timeout_mult = 3600

# The API server.
server = 'api.thesocialdigits.com/v1'

# Returns the customers visitor id. Ideally a md5 hash of the IP and user agent.
def get_visitor_id():
    return None
