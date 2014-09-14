# -*- coding: utf-8 -*-
# Author: Igor Támara igor@tamarapatino.org
# Date: 01/07/2013
# No warranties.
"""
  MoinMoin - Geo Json github
  Embeds a geojson map from github inside moinmoin

  Inputs: Receieves a Github URL containing a geojson file, it must be
  of the kind embed

  For instance:
  <<GithubGeoJson(https://embed.github.com/view/geojson/ikks/moinmoin-github-osm/master/samples/colombiatermal.geojson)>>

  would show a nice map with openstreetmap as it base layers and all
  the geometries in a nice leaflet container by github and mapbox.

  For instructions on how to build the URL for embedding, take a look at
  https://help.github.com/articles/mapping-geojson-files-on-github
"""


def execute(macro, args):
    if not args.startswith('https://embed.github.com/view/geojson/'):
        return "you must offer something that starts with https://embed.git"
    return macro.formatter.rawHTML('<script src="{0}"></script>'.format(args))
