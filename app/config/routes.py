
from system.core.router import routes


routes['default_controller'] = 'Notes'
routes['POST']['/add_note'] = 'Notes#add_note'
routes['/delete'] = 'Notes#delete_note'