###### DATA COLLECTION TYPE : DICTIONARY ######
itemList = {
    'A101':{'Tumblr' : 5}, 
    'A102':{'Box' : 3},
    'A103':{'Plastic' : 4},
    }



###### READ DATA FUNCTION ######
def stockRead() :
    while True:
        stockReadMenu = input('''
        Sub Menu : Stock Overview
    
        1. Stock Overview
        2. Search by Item Code
        3. Back to Main Menu
    
        Please Select Menu: ''')

        ### MENU 1. STOCK OVERVIEW : Menampilkan seluruh data item code, item name, dan juga qty
        if (stockReadMenu == '1') :
            print('''
            \n=============== Item List & Stock ===============
            \nCode     \t| Name     \t| Qty     \t|''')
            for key, value in itemList.items() :
                print('{}     \t| {}     \t| {} pcs     \t|'.format(key,*value.keys(),*value.values()))

        ### MENU 2. SEARCH BY ITEM CODE : Menampilkan data tertentu dengan kode unik item code
        elif (stockReadMenu == '2') :

            itemCode = input('\nPlease enter item code : ')
            
            if itemCode in itemList.keys() : 
                itemName = (str(*itemList[itemCode].keys())) 
                itemQty = (int(*itemList[itemCode].values()))
                print('''
                \n=============== Stock data for {} ===============
                \nCode     \t| Name     \t| Qty     \t|\n{}     \t| {}     \t| {} pcs     \t|'''.format(itemCode,itemCode,itemName,itemQty))

            else:
                return(print('\nError(s):\n*** Item code {} does not exist ***'.format(itemCode)),stockRead())
        
        ### MENU 3. BACK TO MAIN MENU : keluar dari sub menu
        elif (stockReadMenu == '3'):

            stockOverviewExit = input('\nAre you sure want to exit this sub menu? (Yes/No) : ').capitalize()

            if stockOverviewExit == 'Yes':
                break
            elif stockOverviewExit == 'No':
                return(stockRead())
            else:
                print('''\nError(s):\n*** Please enter 'Yes' or 'No' ***''')

        ### JIKA TIDAK MEMILIH MENU 1, 2 ATAU 3 MAKA AKAN KELUAR NOTIFIKASI "MENU YANG DIPILIH TIDAK ADA"
        else:
            print('\nError(s):\n*** Menu {} is unavailable ***'.format(stockReadMenu))
        return(stockRead())   



###### CREATE DATA FUNCTION ######          
def stockAdd() :
    while True :
        stockAddMenu = input('''
        Sub Menu : Create Item & Add Stock
    
        1. Create Item & Add Stock
        2. Back to Main Menu
    
        Please Select Menu: ''')

        ### MENU 1. CREATE Item & Add Stock : Mencari data tertentu.
        ### Jika data yang di input berupa data duplikasi atau sudah ada, maka dapat memilih menambahkan stock.
        ### Jika data yang di input bukan berupa data duplikasi atau belum ada atau berupa data baru, maka dapat membuat item name dan stock awal.
        ### In flow: Jika data berupa data duplikasi maka langsung kembali ke menu create data kembali.
        ### In Here: Jika data berupa data duplikasi maka ada opsi tambahan yang dapat dilakukan.
        if (stockAddMenu == '1') :

            itemCode = input('\nPlease enter item code : ')
            
            ## Jika data duplikasi
            if itemCode in itemList.keys() : 
                itemName = (str(*itemList[itemCode].keys())) 
                itemQty = (int(*itemList[itemCode].values()))
                print('''
                \nNote(s):\n*This item already exist!
                \n=============== Stock data for {} ===============
                \nCode     \t| Name     \t| Qty     \t|\n{}     \t| {}     \t| {} pcs     \t|'''.format(itemCode,itemCode,itemName,itemQty)) 

                askAddQty = input('\nWould you like to increase the qty for this item? (Yes/No) : ').capitalize() 

                if askAddQty == 'Yes':  
                    itemAddQty = int(input('\nEnter qty to be added into this item : ')) #Variable input untuk mendapatkan angka yang ingin digunakan untuk menambahkan value dalam value original
                    orgQty = (int(*itemList[itemCode].values())) #Variable untuk mengakses value dalam value original
                    newQty = {itemName : itemAddQty+orgQty} #Variable baru dengan rumus value : angka yang di input + dengan angka value dalam value original
                    itemList[itemCode].update(newQty) #Mengupdate value dalam value dengan variable rumus di atas
                    print('''
                    \nNote(s):\n*{} pcs qty has been added to item code {}!\n*Displaying remaining stock for all item codes:
                    \n=============== Item List & Stock ===============
                    \nCode     \t| Name     \t| Qty     \t|'''.format(itemAddQty,itemCode))
                    for key, value in itemList.items() :
                        print('{}     \t| {}     \t| {} pcs     \t|'.format(key,*value.keys(),*value.values()))

                elif askAddQty == 'No': 
                    return(stockAdd())
                
                else :  
                    print('''\nError(s):\n*** Please enter 'Yes' or 'No' ***''')

            ## Jika data baru    
            else :
                print('\nNote(s):\n*New item code has been registered!')
                itemName = input('\nEnter item name : ').capitalize()
                itemAddQty = int(input('Enter qty to add into this item : '))

                askAddItem = input('Would you like to add this new item to the e-Storage? (Yes/No) : ').capitalize()

                if askAddItem == 'Yes':
                    newItem = {itemName : itemAddQty}
                    itemList[itemCode] = (newItem)
                    print('''
                    \nNote(s):\n*New item code {} has been added to the e-Storage!\n*Displaying remaining stock for all item codes:
                    \n============== Item List & Stock ===============
                    \nCode     \t| Name     \t| Qty     \t|'''.format(itemCode))
                    for key, value in itemList.items() :
                        print('{}     \t| {}     \t| {} pcs     \t|'.format(key,*value.keys(),*value.values()))

                elif askAddItem == 'No':
                    return(stockAdd())
                
                else:
                    print('''\nError(s)\n*** Please enter 'Yes' or 'No' ***''')
            
        ### MENU 2. BACK TO MAIN MENU : keluar dari sub menu
        elif (stockAddMenu == '2'):

            stockAddExit = input('\nAre you sure want to exit this sub menu? (Yes/No) : ').capitalize()

            if stockAddExit == 'Yes':
                break
            elif stockAddExit == 'No':
                return(stockAdd())
            else:
                print('''\nError(s):\n***Please enter 'Yes' or 'No' ***''')

        ### JIKA TIDAK MEMILIH MENU 1 ATAU 2 MAKA AKAN KELUAR NOTIFIKASI "MENU YANG DIPILIH TIDAK ADA"
        else:
            print('\nError(s):\n*** Menu {} is unavailable ***'.format(stockAddMenu))
        return(stockAdd())



###### UPDATE DATA FUNCTION ######   
def stockUpdate() :
    while True :
        stockUpdateMenu = input('''
        Sub Menu : Edit Item Name & Adjust Stock
    
        1. Edit Item Name
        2. Adjust Stock
        3. Back to Main Menu
    
        Please Select Menu: ''')

        ### MENU 1. EDIT ITEM NAME : Mengubah item name.
        ### Dictionary : {Key:Value} --> {Key:{Key:Value}} 
        ### Mengubah 'Key' yang dalam 'Value' Dictionary.
        ### Tetapi karena value-nya berupa dictionary yang terdiri dari key dan value juga, maka kita harus membuat variable baru untuk membuat sebuah data dengan bentuk dictionary.
        ### Lalu men-delete value lama dan memasukan value baru dengan varibale baru tadi.
        if (stockUpdateMenu == '1') :

            itemCode = input('\nPlease enter item code : ')

            if itemCode in itemList.keys() : 
                itemName = (str(*itemList[itemCode].keys()))
                itemQty = (int(*itemList[itemCode].values()))
                print('Item name is : {}'.format(itemName))                 
                itemNewName = input('Please input new name for this item : ').capitalize() 

                askNewName = input('Would you like to proceed with this new item name? (Yes/No) : ').capitalize() 

                if askNewName == 'Yes':  
                    renameditem = {itemNewName : itemQty} #Variable baru untuk value baru dengan bentuk dictionary
                    itemList[itemCode].update(renameditem)
                    itemList[itemCode].pop(itemName)   
                    print('\nNote(s):\n*Item Code {} has been renamed!\n**Prev Name \t: {} \n**New Name \t: {} \n'.format(itemCode,itemName,itemNewName))  

                elif askNewName == 'No': 
                    return(stockUpdate())
                
                else :  
                    print('''\nError(s):\n*** Please Enter 'Yes' or 'No' ***''')

            else:
                print('\nError(s):\n*** Item code {} does not exist ***'.format(itemCode))
            return(stockUpdate())

        ### MENU 2. ADJUST STOCK : Mengubah item qty.
        ### Dictionary : {Key:Value} --> {Key:{Key:Value}} 
        ### Mengubah 'Value' yang dalam 'Value' Dictionary.
        ### Tetapi karena value-nya berupa dictionary yang terdiri dari key dan value juga, maka kita harus membuat variable baru untuk membuat sebuah data dengan bentuk dictionary.
        ### Lalu men-delete value lama dan memasukan value baru dengan varibale baru tadi.
        if (stockUpdateMenu == '2') :

            itemCode = input('\nPlease enter item code : ')

            if itemCode in itemList.keys() : 
                itemName = (str(*itemList[itemCode].keys())) 
                itemQty = (int(*itemList[itemCode].values()))
                print('Item name is : {}, with current qty {} pcs'.format(itemName,itemQty)) 
                itemNewQty = int(input('Please input new qty for this item : '))

                askNewQty = input('Would you like to proceed with this new item qty? (Yes/No) : ').capitalize() 

                if askNewQty == 'Yes':   
                    renewQty = {itemName : itemNewQty} #Variable baru untuk value baru dengan bentuk dictionary
                    itemList[itemCode].update(renewQty)  
                    print('\nNote(s):\n*Qty for Item Code {} has been adjusted!\n**Prev Qty \t: {} \n**New Qty \t: {} \n'.format(itemCode,itemQty,itemNewQty))

                elif askNewName == 'No': 
                    return(stockUpdate())    
                          
                else :  
                    print('''\nError(s):\n*** Please enter 'Yes' or 'No' ***''')  

            else:
                print('\nError(s):\n*** Item code {} does not exist ***'.format(itemCode))
            return(stockUpdate()) 

        ### MENU 3. BACK TO MAIN MENU : keluar dari sub menu
        elif (stockUpdateMenu == '3'):
            stockAddExit = input('\nAre you sure want to exit this sub menu? (Yes/No) : ').capitalize()
            if stockAddExit == 'Yes':
                break
            elif stockAddExit == 'No':
                return(stockUpdate())
            else:
                print('''\nError(s):\n*** Please Enter 'Yes' or 'No' ***''')

        ### JIKA TIDAK MEMILIH MENU 1, 2 ATAU 3 MAKA AKAN KELUAR NOTIFIKASI "MENU YANG DIPILIH TIDAK ADA"
        else:
            print('\nError(s):\n*** Menu {} is unavailable ***'.format(stockUpdateMenu))
        return(stockUpdate())




###### DELETE DATA FUNCTION ######
def stockDelete():
    while True :
        stockDeleteMenu = input('''
        Sub Menu : Delete Item & Stock Out Request
    
        1. Delete Item
        2. Stock Out Request
        3. Back to Main Menu
    
        Please Select Menu: ''')

        ### MENU 1. DELETE ITEM : Delete data berdasarkan item code.
        ### Men-delete berdasakan keys : akses key by input, menampilkan datanya, mendelete dengan .pop
        if (stockDeleteMenu == '1') :

            itemCode = input('\nPlease enter item code : ')

            if itemCode in itemList.keys() : 
                itemName = (str(*itemList[itemCode].keys())) 
                itemQty = (int(*itemList[itemCode].values()))
                print('''
                \n=============== Stock data for {} ===============
                \nCode     \t| Name     \t| Qty     \t|\n{}     \t| {}     \t| {} pcs     \t|'''.format(itemCode,itemCode,itemName,itemQty))

                askDelItem = input('\nWould you like to delete this item? (Yes/No) : ').capitalize() 

                if askDelItem == 'Yes':   
                    itemList.pop(itemCode)  
                    print('\nNote(s):\n*Item Code {} has been deleted!\n'.format(itemCode))

                elif askDelItem == 'No': 
                    return(stockDelete())             
                 
                else :  
                    print('''\nError(s):\n*** Please Enter 'Yes' or 'No' ***''')  

            else:
                print('\nError(s):\n*** Item code {} does not exist ***'.format(itemCode))
            return(stockDelete()) 

        ### MENU 2. STOCK OUT REQUEST: Mengurangi item qty yang ada di dalam gudang.
        ### Konsepnya hampir sama dengan menambahkan qty yang sudah ada (Menu Create Data), hanya saja dalam variablenya memiliki rumus yang berbeda.
        if (stockDeleteMenu == '2') :

            itemCode = input('\nPlease enter item code : ')

            if itemCode in itemList.keys() : 
                itemName = (str(*itemList[itemCode].keys())) 
                itemQty = (int(*itemList[itemCode].values()))
                print('''
                \n=============== Stock data for {} ===============
                \nCode     \t| Name     \t| Qty     \t|\n{}     \t| {}     \t| {} pcs     \t|'''.format(itemCode,itemCode,itemName,itemQty))

                askOutQty = input('\nWould you like to request stock out for this item? (Yes/No) : ').capitalize() 

                if askOutQty == 'Yes':  
                    itemOutQty = int(input('\nEnter qty to be requested from this item : ')) #Variable untuk mendapatkan angka yang ingin digunakan untuk mengurangi value dalam value original
                    orgQty = (int(*itemList[itemCode].values())) #Variable untuk mengakses value dalam value original
                    newQty = {itemName : orgQty-itemOutQty} #Variable baru dengan rumus value : dengan angka value dalam value original - angka yang di input

                    ## Jika stock Cukup
                    if int(*newQty.values()) >= 0:
                        itemList[itemCode].update(newQty) #Mengupdate value dalam value dengan variable rumus di atas
                        print('''
                        \nNote(s):\n*{} pcs qty has been taken out for Item Code {}!\n*Displaying remaining stock for All Item Code:
                        \n=============== Item List & Stock ===============
                        \nCode     \t| Name     \t| Qty     \t|'''.format(itemOutQty,itemCode))
                        for key, value in itemList.items() :
                            print('{}     \t| {}     \t| {} pcs     \t|'.format(key,*value.keys(),*value.values()))

                    ## Jika stock tidak cukup
                    elif int(*newQty.values()) < 0:
                        print('''
                        \nNote(s):\n*Rejected, stock qty is not enough!
                        \n=============== Stock data for {} ===============
                        \nCode     \t| Name     \t| Qty     \t|\n{}     \t| {}     \t| {} pcs     \t|'''.format(itemCode,itemCode,itemName,itemQty))

                elif askOutQty == 'No': 
                    return(stockDelete())
                
                else :  
                    print('''\nError(s):\n*** Please Enter 'Yes' or 'No' ***''')

            else:
                print('\nError(s):\n*** Item code {} does not exist ***'.format(itemCode))
            return(stockDelete()) 

        ### MENU 3. BACK TO MAIN MENU : keluar dari sub menu
        elif (stockDeleteMenu == '3'):
            stockAddExit = input('\nAre you sure want to exit this sub menu? (Yes/No) : ').capitalize()
            if stockAddExit == 'Yes':
                break
            elif stockAddExit == 'No':
                return(stockDelete())
            else:
                print('''\nError(s):\n*** Please Enter 'Yes' or 'No' ***''')

        ### JIKA TIDAK MEMILIH MENU 1, 2 ATAU 3 MAKA AKAN KELUAR NOTIFIKASI "MENU YANG DIPILIH TIDAK ADA"
        else:
            print('\nError(s):\n*** Menu {} is unavailable ***'.format(stockDeleteMenu))
        return(stockDelete())


while True :
    tumblrMainMenu = input('''
    +-+-+-+-+- Welcome to Tumblr.co e-Storage! -+-+-+-+-+
        
    Main Menu:
    1. Stock Overview
    2. Create Item & Add Stock 
    3. Edit Item Name & Adjust Stock
    4. Delete Item & Request Stock
    5. Exit e-Storage
        
    Please Select Menu : ''')
    
    if(tumblrMainMenu == '1') :
        stockRead()
    elif(tumblrMainMenu == '2') :
        stockAdd()
    elif(tumblrMainMenu == '3') :
        stockUpdate()
    elif(tumblrMainMenu == '4') :
        stockDelete()
    elif(tumblrMainMenu == '5') :
        print('\n+-+-+-+-+- Thank you for using Tumblr.co e-Storage! -+-+-+-+-+\n')
        break
    else:
        print('\nError(s):\n*** Menu {} is unavailable ***'.format(tumblrMainMenu))
