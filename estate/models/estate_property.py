from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate_property'
    _description = 'Estate Property main attributes'
    _order = 'date_availability'

    name = fields.Char('Property Name', required=True, translate=True)
    description = fields.Text('Property Description', translate=True)
    postcode = fields.Char('Property ZIP', required=True, size=5)
    date_availability = fields.Date('Availability')
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer('Total area')
    facades = fields.Integer()
    garage = fields.Binary()
    garden = fields.Binary()
    garden_area = fields.Integer('Garden area')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'),
                   ('south', 'South'),
                   ('west', 'West'),
                   ('east', 'East')]
    )     