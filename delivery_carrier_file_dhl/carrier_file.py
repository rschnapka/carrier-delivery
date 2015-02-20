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

from openerp.osv import orm, fields


class carrier_file(orm.Model):
    _inherit = 'delivery.carrier.file'

    def get_type_selection(self, cr, uid, context=None):
        result = super(carrier_file, self
                       ).get_type_selection(cr, uid, context=context)
        if 'dhl_shipper' not in result:
            result.append(('dhl_shipper', 'DHL Shipper'))
        return result

    _columns = {
        'type': fields.selection(get_type_selection, 'Type', required=True),
        'dhl_account': fields.char('DHL Account', size=9),
    }

carrier_file()
