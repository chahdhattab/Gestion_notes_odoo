{
    'name': "gestion_notes",
    'version': '1.0',
    'author': "chahd Leila Sanae Chaymae",
    'category': 'Category',
    'description': "Description de mon module",
    'depends': ['base'],
    'data': [
        'security/gestion_notes_security.xml',
        'security/ir.model.access.csv',
        'views/gestion_notes_menu.xml',
        'views/gestion_notes_views.xml',
    ],
    'installable': True,
    'application': True,
}
