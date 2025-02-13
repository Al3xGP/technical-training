{
    'name': 'Tech Tr Estate',   # The name that will appear in the App list
    'version': '16.0.0',        # Version
    'application': True,        # This line says the module is an App, and not a module
    'depends': ['base'],        # dependencies
    'data': [
        'views/estate_views.xml',
        'views/estate_menus.xml',
        'views/estate_list_view.xml',        
        'views/estate_form_view.xml',
        'views/estate_search_view.xml',        
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'license': 'LGPL-3',
}