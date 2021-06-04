# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mmd(models.Model):
    _name = 'mmd'
    _description = 'Multi Media'
    
    name = fields.Char(string='Name', required='true')
    beschreibung = fields.Text(string='Beschreibung')
    
    auswahl = fields.Selection(string='Level',
                    selection=[('anfänger', 'Anfänger'),
                              ('fortgeschrittener','Fortgeschrittener'),
                              ('profi', 'Profi')],
                              copy=True)
    
    
    anwesend = fields.Boolean(string='Anwesend',default='true')