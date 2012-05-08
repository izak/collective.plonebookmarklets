##################################################################################
#    Copyright (c) 2004-2009 Utah State University, All rights reserved.
#    Portions copyright 2009 Massachusetts Institute of Technology, All rights reserved.
#                                                                                 
#    This program is free software; you can redistribute it and/or modify         
#    it under the terms of the GNU General Public License as published by         
#    the Free Software Foundation, version 2.                                      
#                                                                                 
#    This program is distributed in the hope that it will be useful,              
#    but WITHOUT ANY WARRANTY; without even the implied warranty of               
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                
#    GNU General Public License for more details.                                 
#                                                                                 
#    You should have received a copy of the GNU General Public License            
#    along with this program; if not, write to the Free Software                  
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA    
#                                                                                 
##################################################################################

__author__  = '''Brent Lambert, David Ray, Jon Thomas, Shane Graber'''
__version__   = '$ Revision 0.0 $'[11:-2]

from urlparse import urlparse
from Products.Five.browser import BrowserView

class BookmarkletsView(BrowserView):
    """ Render the bookmarklets view """

    def getSites(self):
        """ returns bookmarking sites. """
        portal = self.context.restrictedTraverse(
            '@@plone_portal_state').portal()
        pp = portal.portal_properties
        props = pp.bookmarklets_properties
        displayed_sites = props.displayed_sites 
        sites = []
        for name, url, icon in [getattr(props, x) for x in displayed_sites]:
            icon = '%s/%s' % (portal.absolute_url(), icon)
            sites.append((name, url, icon))

        return sites
