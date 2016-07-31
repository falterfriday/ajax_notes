"""
Sample Controller File

"""
from system.core.controller import *

class Notes(Controller):
	def __init__(self, action):
		super(Notes, self).__init__(action)

		self.load_model('Note')
		self.db = self._app.db

	def index(self):
		notes = self.models['Note'].all_notes()
		print '^'*100
		print notes
		return self.load_view('index.html', notes=notes)

	def add_note(self):
		info = {
		'title':request.form['title'],
		'description':request.form['description']
		}
		notes = self.models['Note'].add_note(info)
		print "#"*100
		print notes
		return self.load_view('partials/notes_partial.html', notes=notes)

	def delete_note(self, note_id):
		info = {
		'note_id':note_id
		}
		notes = self.models['Note'].delete_note(info)
		return redirect('/')
