from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate_property'
    _description = 'Estate Property main attributes'
    _order = 'date_availability'

    name = fields.Char('Property Name', required=True, translate=True, default="Unknown")
    description = fields.Text('Property Description', translate=True, default="Unknown")
    postcode = fields.Char('Property ZIP', required=True, size=5)
    date_availability = fields.Date('Available From', copy=False, default=fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Property Area (mts.)')
    facades = fields.Integer()
    garage = fields.Boolean('Has Garage', default=False)
    garden = fields.Boolean('Has Garden', default=False)
    garden_area = fields.Integer('Garden Area (mts.)')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'),
                   ('south', 'South'),
                   ('west', 'West'),
                   ('east', 'East')]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='Property Status',
        selection=[('new', 'New'),
                   ('offered', 'Offer Received'),
                   ('accepted', 'Offer Accepted'),
                   ('sold', 'Sold'),
                   ('canceled', 'Canceled')],
        copy=False,
        default='new'
    )