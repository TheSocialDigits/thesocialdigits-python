#!/usr/bin/env python
"""
Simple unit testing of all the API methods. Ment to be run as an interactive
program.
"""
import unittest
import api



class TheSocialDigitsAPITest(unittest.TestCase):   
    def test_alternative(self):
        basic_result = api.alternative([1,2,3], 10)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 10)
    
    def test_being_watched(self):
        basic_result = api.being_watched(10)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 10)
    
    def test_bundle(self):
        basic_result = api.bundle(-1)
        
        self.assertEqual(type(basic_result), list)
    
    def test_campaign_customers(self):
        basic_result = api.campaign_customers('', 'english', [], 'strong')
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 0)
    
    def test_category_popular(self):
        basic_result = api.category_popular(-1, 10)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 0)
    
    def test_customer_related(self):
        basic_result = api.related([1,2,3], 10)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 10)
    
    def test_popular(self):
        basic_result = api.popular(10)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 10)
    
    def test_purchase(self):
        pass
    
    def test_related(self):
        basic_result = api.related([1,2,3], 10)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 10)
    
    def test_search(self):
        basic_result = api.search('', 'english', 0)
        
        self.assertEqual(type(basic_result), tuple)
        self.assertEqual(type(basic_result[0]), list)
        self.assertEqual(type(basic_result[1]), int)
        self.assertEqual(len(basic_result[0]), 0)
    
    def test_search_suggestions(self):
        basic_result = api.search_suggestions('', 'english', 5)
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 0)
    
    def test_visitor_related(self):
        basic_result = api.visitor_related(10, visitor='dummy-visitor')
        
        self.assertEqual(type(basic_result), list)
        self.assertEqual(len(basic_result), 10) 



if __name__ == '__main__':
    api.config.key = 'xSrDcW401rnXiBkEfjOKAs2YPaGMFW0q'#raw_input('API key: ')
    unittest.main()
