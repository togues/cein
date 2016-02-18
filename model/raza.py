#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Raza(osv.Model):
	_name = "cein.raza"
	_columns = {
		'name': fields.char(string="Nombre",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),		
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	
