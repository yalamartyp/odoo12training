# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Person(models.Model):
    _name = 'open_academy.person'
    _description = 'Students and Teachers'
    
    first_name = fields.Char(string="Person's First Name", required=True)
    last_name = fields.Char(string="Person's Last Name", required=True)
    person_type = fields.Selection([
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ], string="Type")
    
    @api.multi
    def name_get(self):
        return [
            (rec.id, "{} {}".format(rec.first_name, rec.last_name))
            for rec in self
        ]