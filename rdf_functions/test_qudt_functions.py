# -*- coding: utf-8 -*-

from qudt_functions import (
    create_qudt_quantity_value_instance,
    )

import unittest
from rdflib import Graph, URIRef

def TestGraph():
    "returns an RDFLib graph with bound prefixes"
    g=Graph()
    g.namespace_manager.bind('ex', URIRef("http://www.example.com/"))
    g.namespace_manager.bind('bot', URIRef("https://w3id.org/bot#"))
    g.namespace_manager.bind('qudt', URIRef("http://qudt.org/2.1/schema/qudt/"))
    g.namespace_manager.bind('quantitykind', URIRef("http://qudt.org/vocab/quantitykind/"))
    g.namespace_manager.bind('unit', URIRef("http://qudt.org/vocab/unit/"))

    return g
    

class TestBotFunctions(unittest.TestCase):
    ""
    
    def test_create_sosa_observable_property_subclass(self):
        ""
        result=create_sosa_observable_property_subclass(
            'http://www.example.com/HouseholdElectricityConsumption',
            qudt_quantity_kind_uri='http://qudt.org/vocab/quantitykind/Energy',
            label='Household electricity consumption',
            comment='This refers to total household electricity consumption.'
            )
        #print(result)
        g=TestGraph().parse(data=result, format='ntriples')
        print(g.serialize(format="turtle"))
        
        
    def test_create_sosa_observable_property_instance(self):
        ""
        result=create_sosa_observable_property_instance(
            'http://www.example.com/opi1',
            'http://www.example.com/HouseholdElectricityConsumption'
            )
        #print(result)
        g=TestGraph().parse(data=result, format='ntriples')
        print(g.serialize(format="turtle"))
        
        
        
if __name__=='__main__':
    
    unittest.main()
