# -*- coding: utf-8 -*-

rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
rdfs='http://www.w3.org/2000/01/rdf-schema#'
sosa='http://www.w3.org/ns/sosa/'
ssn='http://www.w3.org/ns/ssn/'
qudt='http://qudt.org/2.1/schema/qudt/'
unit='http://qudt.org/2.1/vocab/unit/'
xsd='http://www.w3.org/2001/XMLSchema#'




def create_sosa_feature_of_interest_instance(
        feature_of_interest_uri,
        observable_property_instance_uri=None,
        ):
    """Creates rdf for a sosa FeatureOfInterest instance.
    
    """
    st=''
    st+=f'<{feature_of_interest_uri}> <{rdf}type> <{sosa}FeatureOfInterest>.\n'
    
    if not observable_property_instance_uri is None:
        st+=f'<{feature_of_interest_uri}> <{sosa}hasProperty> <{observable_property_instance_uri}>.\n'
    
    return st
    


def create_sosa_observable_property_instance(
        observable_property_instance_uri,
        observable_property_subclass_uri=None,
        ):
    """Creates rdf for a sosa ObservableProperty instance.
    
    :param observable_property_instance_uri: The uri of the ObservableProperty instance.
    :type observable_property_instance_uri: str
    
    :param observable_property_subclass_uri: The uri of the ObservableProperty 
        subclass which the ObservableProperty instance is derived from.
    :type observable_property_subclass_uri: str
    
    """
    st=''
    st+=f'<{observable_property_instance_uri}> <{rdf}type> <{sosa}ObservableProperty>.\n'
    st+=f'<{observable_property_instance_uri}> <{rdf}type> <{ssn}Property>.\n'
    
    if not observable_property_subclass_uri is None:
        st+=f'<{observable_property_instance_uri}> <{rdf}type> <{observable_property_subclass_uri}>.\n'
    
    return st
    


def create_sosa_observable_property_subclass(
        observable_property_subclass_uri,
        label=None,
        comment=None,
        ):
    """Creates rdf for a sosa ObservableProperty subclass.
    
    :param observable_property_subclass_uri: The uri of the ObservableProperty subclass.
    :type observable_property_subclass_uri: str
    
    :param qudt_quantity_kind_uri: A uri for a qudt QuantityKind instance that 
         relates to the ObservableProperty subclass.
    :type qudt_quantity_kind_uri: str
    
    :param label: A label for the ObservableProperty subclass.
    :type label: str
    
    :param comment: A comment for the ObservableProperty subclass.
    :type comment: str
    
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    st+=f'<{observable_property_subclass_uri}> <{rdfs}subClassOf> <{sosa}ObservableProperty>.\n'
    st+=f'<{observable_property_subclass_uri}> <{rdfs}subClassOf> <{ssn}Property>.\n'
    
    if not label is None:
        st+=f'<{observable_property_subclass_uri}> <{rdfs}label> "{label}".\n'    
        
    if not comment is None:
        st+=f'<{observable_property_subclass_uri}> <{rdfs}comment> "{comment}".\n'    
    
    return st

    

def create_sosa_observation_instance(
        observation_instance_uri,
        feature_of_interest_instance_uri=None,
        observable_property_instance_uri=None,
        result_instance_uri=None,
        sensor_instance_uri=None,
        procedure_instance_uri=None,
        result_time_literal_value=None,
        phenomenon_time_instance_uri=None,
        simple_result_literal_lexical_value=None,
        simple_result_literal_datatype_uri=None,
        label=None,
        comment=None,
        ):
    """
    
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    st+=f'<{observation_instance_uri}> <{rdf}type> <{sosa}Observation>.\n'
    
    if not feature_of_interest_instance_uri is None:
        st+=f'<{observation_instance_uri}> <{sosa}hasFeatureOfInterest> <{feature_of_interest_instance_uri}>.\n'
    
    if not observable_property_instance_uri is None:
        st+=f'<{observation_instance_uri}> <{sosa}observedProperty> <{observable_property_instance_uri}>.\n'
    
    if not result_instance_uri is None:
        st+=f'<{observation_instance_uri}> <{sosa}hasResult> <{result_instance_uri}>.\n'
        
    if not sensor_instance_uri is None:
        st+=f'<{observation_instance_uri}> <{sosa}madeBySensor> <{sensor_instance_uri}>.\n'
        
    if not procedure_instance_uri is None:
        st+=f'<{observation_instance_uri}> <{sosa}usedProcedure> <{procedure_instance_uri}>.\n'
        
    if not result_time_literal_value is None:
        st+=f'<{observation_instance_uri}> <{sosa}resultTime> "{result_time_literal_value}"^^<{xsd}dateTime>.\n'
    
    if not phenomenon_time_instance_uri is None:
        st+=f'<{observation_instance_uri}> <{sosa}phenomenonTime> <{phenomenon_time_instance_uri}>.\n'
    
    if not simple_result_literal_lexical_value is None:
        if not simple_result_literal_datatype_uri is None:
            st+=(f'<{observation_instance_uri}> <{sosa}hasSimpleResult> '
                 + f'"{simple_result_literal_lexical_value}"^^<{simple_result_literal_datatype_uri}>.\n')
        else:
            raise ValueError()
    
    if not label is None:
        st+=f'<{observation_instance_uri}> <{rdfs}label> "{label}".\n'    
        
    if not comment is None:
        st+=f'<{observation_instance_uri}> <{rdfs}comment> "{comment}".\n'    
    
    return st


def create_sosa_result_instance(
        result_instance_uri,
        observation_instance_uri=None,
        ):
    """Creates rdf for a sosa Result instance.
    
    :param result_instance_uri: The uri of the Result instance.
    :type result_instance_uri: str
    
    :returns: A string of rdf in ntriples format.
    :rtype: str 
    
    """
    st=''
    st+=f'<{result_instance_uri}> <{rdf}type> <{sosa}Result>.\n'
    
    if not observation_instance_uri is None:
        st+=f'<{result_instance_uri}> <{sosa}isResultOf> <{observation_instance_uri}>.\n'
    
    return st


    