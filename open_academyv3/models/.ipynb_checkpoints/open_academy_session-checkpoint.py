# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Course Sessions'
    
    name = fields.Char(string="Session Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string = "End Date", required=True)
    course = fields.Many2one('open_academy.course', required=True ) #ondelete default is set null
    teacher = fields.Many2one('open_academy.person', required=True)
