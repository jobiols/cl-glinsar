# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
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
# -----------------------------------------------------------------------------------
{
    'name': 'GLINSAR',
    'version': '9.0.4.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Glinsar srl',
    'author': 'jeo Software',
    'depends': [
        'support_branding_jeosoft',

        # modulos instalados
        'sale', 'l10n_ar_aeroo_sale',  # ventas
        'purchase', 'l10n_ar_aeroo_purchase',  # compras
        'account_accountant',  # permisos para contabilidad
        'l10n_ar_aeroo_stock',
        # requeridos por el cliente
        'hr_expense',
        'crm',
        'website',  # constructor de sitios web
        'project',  # project
        'product_unique',
        'meli_oerp',
        'account_invoice_tax_wizard'
    ],

    'data': [
        'views/custom_reports.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-glinsar', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'meli_oerp', 'branch': 'master'},
    ],
    'docker': [
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'}
    ]
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
