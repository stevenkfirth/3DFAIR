# -*- coding: utf-8 -*-

rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
rdfs='http://www.w3.org/2000/01/rdf-schema#'
bot='https://w3id.org/bot#'


def create_bot_building_instance(
        building_instance_uri,
        space_instance_uris=None,
        label=None,
        comment=None
        ):
    """Creates rdf for a bot Building instance.
    
    :param building_instance_uri: The uri of the Building instance.
    :type building_instance_uri: str
    
    :param space_instance_uris: A list of uris of the spaces contained by the building.
    :type space_instance_uris: list
    
    :param label: A label for the Building instance.
    :type label: str
    
    :param comment: A comment for the Building instance.
    :type comment: str
        
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    st+=f'<{building_instance_uri}> <{rdf}type> <{bot}Building>.\n'
    st+=f'<{building_instance_uri}> <{rdf}type> <{bot}Zone>.\n'
    
    if not space_instance_uris is None:
        for space_instance_uri in space_instance_uris:
            st+=f'<{space_instance_uri}> <{rdf}type> <{bot}Space>.\n'
            st+=f'<{space_instance_uri}> <{rdf}type> <{bot}Zone>.\n'
            st+=f'<{building_instance_uri}> <{bot}hasSpace> <{space_instance_uri}>.\n'
            st+=f'<{building_instance_uri}> <{bot}containsZone> <{space_instance_uri}>.\n'

    if not label is None:
        st+=f'<{building_instance_uri}> <{rdfs}label> "{label}".\n'    
        
    if not comment is None:
        st+=f'<{building_instance_uri}> <{rdfs}comment> "{comment}".\n'    

    return st



def create_bot_space_instance(
        space_instance_uri,
        label=None,
        comment=None
        ):
    """Creates rdf for a bot Space instance.
    
    :param space_instance_uri: The uri of the Space instance.
    :type space_instance_uri: str
    
    :param label: A label for the Space instance.
    :type label: str
    
    :param comment: A comment for the Space instance.
    :type comment: str
        
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    st+=f'<{space_instance_uri}> <{rdf}type> <{bot}Space>.\n'
    st+=f'<{space_instance_uri}> <{rdf}type> <{bot}Zone>.\n'
    
    if not label is None:
        st+=f'<{space_instance_uri}> <{rdfs}label> "{label}".\n'    
        
    if not comment is None:
        st+=f'<{space_instance_uri}> <{rdfs}comment> "{comment}".\n'    

    return st









# def create_bot_building(graph,
#                         building_uriref,
#                         space_urirefs):
#     ""
#     graph.add((building_uriref, RDF.type, bot.Building)) 
#     graph.add((building_uriref, RDF.type, bot.Zone))
#     for space_uriref in space_urirefs:
#         graph.add((building_uriref, bot.hasSpace, space_uriref))
#         graph.add((building_uriref, bot.containsZone, space_uriref))
        