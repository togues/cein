#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Departamentos(osv.Model):
	_name = "cein.geodepartamentos"
	_columns = {
		'name': fields.char(string="Departamento",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Departamento",	 size=256, required=False,help="Nombre con acentos a mostrar"),
		'code': fields.char(string="Code",	 size=2, required=True,help="Codigo de dos digitos EJ[01]"),
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Apuntes", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	