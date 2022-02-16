# -*- coding: utf-8 -*-

from bot_functions import (create_bot_building_instance,
                           create_bot_space_instance)

import unittest
from rdflib import Graph, URIRef

def TestGraph():
    "returns an RDFLib graph with bound prefixes"
    g=Graph()
    g.namespace_manager.bind('ex', URIRef("http://www.example.com/"))
    g.namespace_manager.bind('bot', URIRef("https://w3id.org/bot#"))
    return g
    

class TestBotFunctions(unittest.TestCase):
    ""
    
    def test_create_bot_building_instance(self):
        ""
        result=create_bot_building_instance(
            'http://www.example.com/building1',
            space_instance_uris=['http://www.example.com/space1',
                                 'http://www.example.com/space2'],
            label='my_building',
            comment='This is my building.'
            )
        #print(result)
        g=TestGraph().parse(data=result, format='ntriples')
        print(g.serialize(format="turtle"))
        
        
    def test_create_bot_space_instance(self):
        ""
        result=create_bot_space_instance(
            'http://www.example.com/space1',
            label='my_space',
            comment='This is my space.'
            )
        #print(result)
        g=TestGraph().parse(data=result, format='ntriples')
        print(g.serialize(format="turtle"))
        
        
        
if __name__=='__main__':
    
    unittest.main()