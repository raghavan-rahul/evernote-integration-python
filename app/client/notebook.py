class NoteBook(object):
	"""Specifies the notebooks associated with a particular user"""

	def get_all_notebooks(self, note_store):
		"""Returns all notebooks"""
		return note_store.listNotebooks()