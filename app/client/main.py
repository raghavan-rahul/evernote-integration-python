import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
from auth import Auth
from tag import Tag
from notebook import NoteBook
from note import Note

auth = Auth()
tags = Tag()
notebooks = NoteBook()
notes = Note()

#Authenticate the user using the oauth or developer toke
client = auth.authenticate()

user_store = client.get_user_store()

#Check whether the version is up to date with the latest version provided by evernote
version_ok = user_store.checkVersion(
    "Evernote",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print("Is my Evernote API version up to date? ", str(version_ok))
print("")
if not version_ok:
    exit(1)

note_store = client.get_note_store()

# List all of the tags in the user's account
all_tags = tags.get_all_tags(note_store)
print("Found ", len(all_tags), " tags:")
for tag in all_tags:
    print("  * ", tag.name)

# List all of the notebooks in the user's account
notebooks = notebooks.get_all_notebooks(note_store)
print("Found ", len(notebooks), " notebooks:")
for notebook in notebooks:
    print("  * ", notebook.name)


print()
print("Creating a new note in the default notebook")
print()

# To create a new note, simply create a new Note object and fill in
# attributes such as the note's title, notes content.
note = notes.initialize_note()
note.title = notes.set_title("Test note")

# To include an attachment such as an image in a note, first create a Resource
# for the attachment. At a minimum, the Resource contains the binary attachment
# data, an MD5 hash of the binary data, and the attachment MIME type.
# It can also include attributes such as filename and location.
image = open('C:/Users/Rahul Raghavan/Desktop/evernote-sdk-python3/sample/client/enlogo.png', 'rb').read()
md5 = hashlib.md5()
md5.update(image)
hash = md5.digest()

data = Types.Data()
data.size = len(image)
data.bodyHash = hash
data.body = image

resource = Types.Resource()
resource.mime = 'image/png'
resource.data = data

# Now, add the new Resource to the note's list of resources
note.resources = [resource]

# To display the Resource as part of the note's content, include an <en-media>
# tag in the note's ENML content. The en-media tag identifies the corresponding
# Resource using the MD5 hash.
hash_hex = binascii.hexlify(hash)
hash_str = hash_hex.decode("UTF-8")

# The content of an Evernote note is represented using Evernote Markup Language
# (ENML). The full ENML specification can be found in the Evernote API Overview
# at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
# Sample note content
# note.content = '<?xml version="1.0" encoding="UTF-8"?>'
# note.content += '<!DOCTYPE en-note SYSTEM ' \
#                 '"http://xml.evernote.com/pub/enml2.dtd">'
# note.content += '<en-note>Here is the Evernote logo:<br/>'
# note.content += '<en-media type="image/png" hash="{}"/>'.format(hash_str)
# note.content += '</en-note>'

note.content = notes.set_xml_header('Hello Evernote')

# Finally, send the new note to Evernote using the createNote method
# The new Note object that is returned will contain server-generated
# attributes such as the new note's unique GUID.
# created_note = note_store.createNote(note)
created_note = notes.create_note(note_store, note)

print("Successfully created a new note with GUID: ", created_note.guid)
