
import datetime

last_id = 0 #store the next available ID for all the notes

class Note:
    '''Repr a note in the notebook.Mathch against a string 
    in searches and store tags for each note'''
    def __init__(self,memo, tags = ''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1
        self.id = last_id

    def match(self,filter): 
        '''Determine if this note matches the filter text.Return True if
        it does, otherwise False. Search for case sensitive and match both
        text and tags'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Repr a colllection of notes that can be tagged, searched and modified'''

    def __init__(self):
        self.notes = []

    def new_note(self,memo, tags = ''):
        'create a new note and add it to the list'
        self.notes.append(Note(memo,tags)) 

    def modify_memo(self,note_id,memo):
        '''find the note with the giving id and change its tags to the given value'''
        for note in self.notes:
            if note.id == note.id:   
                note.memo = memo
                break

    def modify_tags(self,note_id, tags):
        '''find the note with the giving id and change its tags to the given value'''
        for note in self.notes:
            if note.id == note.id:
                note.tags = tags
                break

    def search(self, filter):
        '''Find all notes that match the given filter string'''
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self,note_id):
        '''Locate the note with the given id'''
        for note in self.note:
            if note.id == note_id:
                return note
        return None 

    def modify_memo(self,note_id,memo):
        '''find the note with a giving id and change its memo to the given value'''
        self._find_note(note_id).memo = memo    


