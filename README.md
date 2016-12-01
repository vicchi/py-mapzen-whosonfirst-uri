# py-mapzen-whosonfirst-uri

Shared utilities for working with URIs for Who's On First documents

## IMPORTANT

This library is provided as-is, right now. It lacks proper
documentation which will probably make it hard for you to use unless
you are willing to poke and around and investigate things on your
own.

## Installation

The usual Python dance:

```
sudo python setup.py install
```    

## Usage

```
import mapzen.whosonfirst.uri

mapzen.whosonfirst.uri.id2fname(2179537)
'2179537.geojson'

mapzen.whosonfirst.uri.id2fname(2179537, 'alt', 'source')
'2179537-alt-source.geojson'

mapzen.whosonfirst.uri.id2fname(2179537, 'alt', 'source', 'function')
'2179537-alt-source-function.geojson'

mapzen.whosonfirst.uri.id2relpath(2179537)
'217/953/7/2179537.geojson'

mapzen.whosonfirst.uri.id2abspath('https://whosonfirst.mapzen.com/data', 2179537)
'https://whosonfirst.mapzen.com/data/217/953/7/2179537.geojson'
```

## See also

* https://github.com/whosonfirst/whosonfirst-data/

