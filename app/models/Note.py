"""
MODEL File
"""
from system.core.model import Model

class Note(Model):
	def __init__(self):
		super(Note, self).__init__()

	def all_notes(self):
		query = "SELECT * FROM notes"
		return self.db.query_db(query)

	def add_note(self, info):
		query = "INSERT INTO notes (title, description, created_at, updated_at) VALUES (:title, :description, NOW(), NOW() )"
		data = {
		'title':info['title'],
		'description':info['description']
		}
		self.db.query_db(query, data)
		notes_query = "SELECT * FROM notes"
		return self.db.query_db(notes_query)

	def delete_note(self, info):
		query = "DELETE FROM notes WHERE id = :id"
		data = {
		'id':info['note_id']
		}
		self.db.query_db(query, data)
