import evernote.edam.type.ttypes as Types

class Note(object):
	"""Allows the user to perform different operations on note like creating a new note"""
	
	def initialize_note(self):
		return Types.Note()

	def create_note(self, note_store, note):
		return note_store.createNote(note)

	def set_title(self, title):
		return title

	def set_content(self, content):
		return content

	def get_title(self, note):
		return note.title

	def get_content(self, note):
		return note.content

	def set_note_content(self, content):
		return '<en-note>' + self.set_content(content) +'<br/></en-note>'

	def set_xml_header(self, content):
		"""Defines the xml header information for creating a new note"""
		xml_header = '<?xml version="1.0" encoding="UTF-8"?>'
		xml_header += '<!DOCTYPE en-note SYSTEM ' \
		                '"http://xml.evernote.com/pub/enml2.dtd">'
		xml_header += self.set_note_content(content)
		# xml_header += '<en-media type="image/png" hash="{}"/>'
		return xml_header