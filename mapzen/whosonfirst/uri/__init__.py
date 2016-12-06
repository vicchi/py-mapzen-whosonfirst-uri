import logging
import os
import types
import mapzen.whosonfirst.sources

def id2abspath(root, id, **kwargs):

    rel = id2relpath(id, **kwargs)

    path = os.path.join(root, rel)
    return path

def id2relpath(id, **kwargs):

    fname = id2fname(id, **kwargs)
    parent = id2path(id)

    path = os.path.join(parent, fname)
    return path

def id2fname(id, **kwargs):

    # alt-geometry documentation: https://github.com/whosonfirst/whosonfirst-cookbook/blob/master/how_to/creating_alt_geometries.md
    alt = kwargs.get('alt', None)
    source = kwargs.get('source', None)
    function = kwargs.get('function', None)
    extras = kwargs.get('extras', [])    
    strict = kwargs.get('strict', False)
    
    display = kwargs.get('display', None)    # deprecated

    if type(alt) == types.StringType:
        logging.warning("please stop passing alt as a string!")
        source = alt
        alt = True
        
    if display:
        logging.warning("please stop passing display as a kwarg!")
        function = display
    
    parts = [ str(id) ]
    
    if alt and source:
    
        # this code does not exist yet
        
        """
        src = mapzen.whosonfirst.source.source(source)
        
        if src:
            if function and !src.is_valid_function(function):
                logging.warning("%s is not a valid function for source %s" % (function, source))
        else:
            logging.warning("%s is not a valid source" % source)
        """
            
        if not mapzen.whosonfirst.sources.is_valid_source(source):
            logging.warning("%s is not a valid (or known) source" % source)
    
            if strict:
                raise Exception, "invalid filename options"
                        
    if alt and source:
        # TO DO: test source against mapzen.whosonfirst.sources.is_valid_source
        # TO DO: test function against... something?
        # TO DO: if either scenario fails then... what? more than a warning?
        
        parts.append("alt")
        parts.append(source)
        
        if function:
            parts.append(function)

            extras = map(str, extras)
            parts.extend(extras)
            
    elif alt:
        logging.warning("insufficient parameters for alt name")
        
        if strict:
            raise Exception, "Invalid filename options"
            
    else:
        pass
        
    fname = "-".join(parts)
    fname = fname + ".geojson"

    return fname

def id2path(id):

    tmp = str(id)
    parts = []
    
    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]

    if len(tmp):
        parts.append(tmp)

    return "/".join(parts)
