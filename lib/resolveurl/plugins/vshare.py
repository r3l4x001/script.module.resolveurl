"""
    resolveurl XBMC Addon
    Copyright (C) 2011 t0mm0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __resolve_generic__ import ResolveGeneric

class VshareResolver(ResolveGeneric):
    name = "vshare"
    domains = ['vshare.io']
    pattern = '(?://|\.)(vshare\.io)/\w?/(\w+)'

    def get_url(self, host, media_id):
        return 'http://vshare.io/v/%s/width-620/height-280/' % media_id
