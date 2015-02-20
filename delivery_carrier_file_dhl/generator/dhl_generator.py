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

import csv

from openerp.addons.base_delivery_carrier_files.generator import (
    CarrierFileGenerator
)
from openerp.addons.base_delivery_carrier_files.generator import BaseLine
from openerp.addons.base_delivery_carrier_files.csv_writer import UnicodeWriter


class DHLLine(BaseLine):
    fields = (('send_name1', 50),
              ('send_name2', 50),
              ('send_street', 50),
              ('send_housenumber', 11),
              ('send_plz', 11),
              ('send_city', 38),
              ('send_country', 9),
              ('recv_name1', 50),
              ('recv_name2', 50),
              ('recv_street', 50),
              ('recv_housenumber', 11),
              ('recv_plz', 11),
              ('recv_city', 38),
              ('recv_country', 9),
              ('product', 30),)


class DHLFileGenerator(CarrierFileGenerator):

    @classmethod
    def carrier_for(cls, carrier_name):
        return carrier_name == 'dhl_shipper'

    def _get_rows(self, picking, configuration):
        """
        Returns the rows to create in the file for a picking

        :param browse_record picking: the picking for which we generate a row
               in the file
        :param browse_record configuration: configuration of the file to
               generate
        :return: list of rows
        """
        line = DHLLine()
        line.reference = picking.name
        if picking.address_id:
            line.send_name1 = picking.address_id.name
            line.send_street = picking.address_id.street 
            line.send_plz = picking.address_id.zip
            line.send_city = picking.address_id.city
            line.send_country = picking.address_id.country_id.code
            line.recv_name1 = (picking.address_id.partner_id
                         and picking.address_id.partner_id.name)
            line.recv_street = (picking.address_id.partner_id
                         and picking.address_id.partner_id.street)
            line.recv_plz = (picking.address_id.partner_id
                         and picking.address_id.partner_id.zip)
            line.recv_city = (picking.address_id.partner_id
                         and picking.address_id.partner_id.city)
            line.recv_country = (picking.address_id.partner_id
                         and picking.address_id.partner_id.country_id.code)
            line.product = picking.carrier_id and picking.carrier_id.name or '*'
        return [line.get_fields()]

    def _write_rows(self, file_handle, rows, configuration):
        """
        Write the rows in the file (file_handle)

        :param StringIO file_handle: file to write in
        :param rows: rows to write in the file
        :param browse_record configuration: configuration of the file to
               generate
        :return: the file_handle as StringIO with the rows written in it
        """
        writer = UnicodeWriter(file_handle, delimiter=';', quotechar='"',
                               lineterminator='\n', quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
        return file_handle
