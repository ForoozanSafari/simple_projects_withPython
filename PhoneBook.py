class contact :
    
    Contact_list=[['foroozan','0124905462','no']]
    
    def __init__(self, name ,number, extra ):
        self.Name = name
        self.NUM = number
        self.extra = extra
        
    def Contact (self ):
        newContact = [self.Name ,self.NUM, self.extra]
        self.Contact_list.append(newContact)
        print('added ')
        return newContact
    
    def edit(self,contact,name ,number, extra):
        contact = contact
        self.Name = name
        self.NUM = number
        self.extra = extra
        
        if CC in Contact_list :
            Contact_list.pop(CC)
            edited_contact = [self.Name ,self.NUM, self.extra]
            self.Contact_list.append(edited_contact)
            print('edited')
        else :
            print('not in list')
            

        return edited_contact


print('<< welcome to phone book >>','\n'\
        '1 - if you want to save a new contact, enter : "new"','\n'\
        '2 - if you want to edit an exisintg contact , enter : "edit"','\n'\
        '3 - if you want to seach a contact by name, enter : "name"','\n'\
        '4 - if you want to search a contact by number , enter : "number"')

while 1 :
    choice = input('enter : ')

    if choice.lower() == 'new':
        a = input('name ')
        b = input('num ')
        c = input('extra') 
        new = contact(a,b,c)
        print(new.Contact())

    if choice.lower() == 'edit':
        CC = input('name to edit')
        a = input('name ')
        b = input('num ')
        c = input('extra') 
        edit_C = contact(a,b,c)
        print(edit_C.edit(CC,a,b,c))    
    
