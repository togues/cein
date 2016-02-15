#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Municipios(osv.Model):
	_name = "cein.geomunicipios"
	_columns = {
		'name': fields.char(string="Municipio",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Municipio",	 size=256, required=True,help="Nombre con acentos a mostrar"),
		'code': fields.char(string="Code",	 size=2, required=True,help="Codigo de dos digitos EJ[01]"),
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Apuntes", required=False, help="Descripcion"),
		'departamento_id': fields.many2one('cein.geodepartamentos','Departamento', required=True),								
	}
	_defaults = {
		'activo': True,	
	}

	