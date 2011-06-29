#!/usr/bin/env python
from resources.lib.xbmcswift.plugin import XBMCSwiftPlugin
from resources.lib.xbmcswift.common import download_page
from BeautifulSoup import BeautifulSoup as BS, SoupStrainer as SS
from urlparse import urljoin
import re

__plugin__ = '{plugin_name}'
__plugin_id__ = '{plugin_id}'

plugin = XBMCSwiftPlugin(__plugin__, __plugin_id__)

#### Write your handlers here ####

# Default Handler
#@plugin.route('/', default=True)
#def show_categories():
    #pass

if __name__ == '__main__': 
    plugin.run()





