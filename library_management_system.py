'''
Features 
1. Add books
2. View books
3. Borrow books 
4. Return books 
5. Save
6. exit 
'''

books = [] 

# Load the file 
try: 
    f = open('library.txt', 'r')
    for line in f: 
        data = line.strip().split(',')
        
        book = {
            'name' : data[0], 
            'status' : data[1]
        }    
        books.append(book)
    f.close()
except: 
    print('File not found.')\
        
choice = '0'

while choice != '6': 
    print("*"*50)
    print('1. Add book')
    print('2. View book')
    print('3. Borrow book')
    print('4. Return book')
    print('5. Save')
    print('6. Exit')
    print("*"*50)

    choice = input('Enter your choice = ')
    
    # Add book
    if choice == '1':
        name = input('Enter book name : ')
        
        book = {
            'name' : name, 
            'status' : 'Available'
        }
        
        books.append(book)
        print("*"*50)
        print('BOOK ADDED !!!')
        print("*"*50)
    
    # View Book 
    elif choice == '2':
        if len(books) == 0:
            print("*"*50)
            print('No books added')
            print("*"*50)
        else: 
            for b in books:
                print(b['name'], '-', b['status'])
                
    # Borrow Book 
    elif choice == '3':
        name = input('Enter book name : ')
        found = False
        
        for b in books:
            if b['name'] == name:
                found = True 
                
                if b['status'] == 'Available':
                    b['status'] == 'Borrowed'
                    print("*"*50)
                    print('Borrowed')
                    print("*"*50)
                
                else: 
                    print("*"*50)
                    print('Already Borrowed !')
                    print("*"*50)
        if found == False:
            print("*"*50)
            print('Book not found !!!')
            print("*"*50)
    
    # Return Book 
    elif choice == '4':
        name = input('Enter book name to return : ')
        
        found = False 
        
        for b in books:
            if b['name'] == name:
                found = True 
                
                if b['status'] == 'Borrowed':
                    b['status'] == 'Available'
                    print('Returned')
                    
                else: 
                    print("*"*50)
                    print('Already available !!!')
                    print("*"*50)
            
            if found == False:
                print("*"*50)
                print('Book not found !!!')        
                print("*"*50)
    
    # Save 
    elif choice == '5': 
        f = open('library.txt', 'w')
        
        for b in books: 
            line = b['name'] + ',' + b['status'] + '\n'  
            f.write(line)
        f.close()
        print("*"*50)
        print('FILE HAS BEEN SAVED !!!')    
        print("*"*50)
        
    # Exit 
    elif choice == '6': 
        f = open('library.txt', 'w')
        
        for b in books: 
            line = b['name'] + ',' + b['status'] + '\n'  
            f.write(line)
        f.close()
        
        print('Data saved Sucessfully !!!')
        
    else:
        print('Invalid Choice !')
        
              
                
                
    
    
    
    
    