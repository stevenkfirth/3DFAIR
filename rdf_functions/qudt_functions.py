# -*- coding: utf-8 -*-

rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
rdfs='http://www.w3.org/2000/01/rdf-schema#'
qudt='http://qudt.org/2.1/schema/qudt/'
unit='http://qudt.org/2.1/vocab/unit/'


def create_qudt_quantity_instance(
        quantity_instance_uri,
        #quantity_subclass_uri=None,
        quantity_value_instance_uri=None,
        quantity_kind_instance_uri=None,
        label=None,
        comment=None,
        ):
    """Creates rdf for a qudt Quantity instance.
    
    :param quantity_instance_uri: The uri of the Quantity instance.
    :type quantity_instance_uri: str
    
    :param quantity_value_instance_uri: The uri of a QuantityValue instance
        associated with the Quantity instance.
    :type quantity_value_instance_uri: str
    
    :param quantity_kind_instance_uri: Ths uri of a QuantityKind instance
        associated with the Quantity instance.
    :type quantity_kind_instance_uri: str
    
    :param label: A label for the Quantity instance.
    :type label: str
    
    :param comment: A comment for the Quantity instance.
    :type comment: str
    
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    
    st+=f'<{quantity_instance_uri}> <{rdf}type> <{qudt}Quantity>.\n'
    
    #if not quantity_subclass_uri is None:
    #    st+=f'<{quantity_instance_uri}> <{rdf}type> <{quantity_subclass_uri}>.\n'
    
    if not quantity_value_instance_uri is None:
        st+=f'<{quantity_instance_uri}> <{qudt}quantityValue> <{quantity_value_instance_uri}>.\n'
        
    if not quantity_kind_instance_uri is None:
        st+=f'<{quantity_instance_uri}> <{qudt}hasQuantityKind> <{quantity_kind_instance_uri}>.\n'
    
    if not label is None:
        st+=f'<{quantity_instance_uri}> <{rdfs}label> "{label}".\n'    
        
    if not comment is None:
        st+=f'<{quantity_instance_uri}> <{rdfs}comment> "{comment}".\n'    
    
    return st




# def create_qudt_quantity_subclass(
#         quantity_subclass_uri,
#         label=None,
#         comment=None):
#     """Creates rdf for a qudt Quantity subclass.
    
#     :param quantity_subclass_uri: The uri of the Quantity subclass.
#     :type quantity_subclass_uri: str
    
#     :param label: A label for the Quantity subclass.
#     :type label: str
    
#     :param comment: A comment for the Quantity subclass.
#     :type comment: str
    
#     :returns: A string of rdf in ntriples format.
#     :rtype: str 
    
#     """
#     st=''
    
#     st+=f'<{quantity_subclass_uri}> <{rdfs}subClassOf> <{qudt}Quantity>.\n'
    
#     if not label is None:
#         st+=f'<{quantity_subclass_uri}> <{rdfs}label> "{label}".\n'    
        
#     if not comment is None:
#         st+=f'<{quantity_subclass_uri}> <{rdfs}comment> "{comment}".\n'   
    
#     return st





def create_qudt_quantity_value_instance(
        quantity_value_instance_uri,
        value_literal_lexical_value,
        value_literal_datatype_uri,
        qudt_unit_uri,
        label=None,
        comment=None,
        ):
    """Creates rdf for a qudt QuantityValue instance.
    
    :param quantity_value_instance_uri: The uri of the QuantityValue instance.
    :type quantity_value_instance_uri: str
    
    :param value: The value of the QuantityValue instance, represented as a 
        string.
    :type value: str
    
    :param value_datatype_uri: Ths uri of the datatype for the value.
    :type value_datatype_uri: str
    
    :param qudt_unit_uri: The uri of the qudt Unit instance for 
        the QuantityValue instance.
    :type qudt_unit_uri: str
    
    :param label: A label for the QuantityValue instance.
    :type label: str
    
    :param comment: A comment for the QuantityValue instance.
    :type comment: str
    
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    st+=f'<{quantity_value_instance_uri}> <{rdf}type> <{qudt}QuantityValue>.\n'
    st+=f'<{quantity_value_instance_uri}> <{qudt}value> "{value_literal_lexical_value}"^^<{value_literal_datatype_uri}>.\n'
    st+=f'<{quantity_value_instance_uri}> <{qudt}unit> <{qudt_unit_uri}>.\n'
    
    if not label is None:
        st+=f'<{quantity_value_instance_uri}> <{rdfs}label> "{label}".\n'    
        
    if not comment is None:
        st+=f'<{quantity_value_instance_uri}> <{rdfs}comment> "{comment}".\n'    
    
    return st
