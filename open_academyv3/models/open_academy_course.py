# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course (models.Model):
    _name = "open_academy.course"
    _description = "Courses defined"
    

    name = fields.Char(string="Title", required=True )
    level = fields.Selection([
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
        ('extreme', 'Extreme'),
    ], string="Difficulty")

    