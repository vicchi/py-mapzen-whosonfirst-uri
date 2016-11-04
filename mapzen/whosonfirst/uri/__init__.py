import logging
import os

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

    # See this. It doesn't really allow for new "alternate" names
    # to be added. For example a bespoke reverse geocoding polygon.
    # That's not ideal but it's also by design to force us to
    # actually think about what/how we want to do that...
    # (20151217/thisisaaronland)

    alt = kwargs.get('alt', None)
    display = kwargs.get('display', None)

    if alt:
        return "%s-alt-%s.geojson" % (id, alt)
    elif display:
        return "%s-display-%s.geojson" % (id, display)
    else:
        return "%s.geojson" % id

def id2path(id):

    tmp = str(id)
    parts = []
    
    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]

    if len(tmp):
        parts.append(tmp)

    return "/".join(parts)
