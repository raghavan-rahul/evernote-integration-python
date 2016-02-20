class Tag(object):
	"""Specifies the tags associated with a particular user and also tags associated with a notebook"""

	def get_all_tags(self, note_store):
		"""Returns all tags"""
		return note_store.listTags()

	def get_all_tags_by_notebook(self, note_store):
		"""Returns tags based on a particular notebook"""
		return note_store.listTagsByNotebook()

		