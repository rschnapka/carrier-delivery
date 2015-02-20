# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Delivery Carrier File: DHL',
    'version': '1.0',
    'category': 'Generic Modules/Warehouse',
    'description': """
Sub-module for Base Delivery Carrier Files.

Definition of the delivery carrier file for "DHL Online Frankierung".

File specifications on :
https://www.efiliale.de/efiliale/pop/popcsvupload.jsp
Chapter : "Adressdaten importieren "
    """,
    'author': 'GoLive',
    'license': 'AGPL-3',
    'website': 'http://www.golive-saar.de',
    'depends': ['base_delivery_carrier_files'],
    'init_xml': [],
    'update_xml': ['carrier_file_view.xml'],
    'demo_xml': [],
    'test': [],
    'images': [],
    'installable': True,
    'auto_install': False,
}
