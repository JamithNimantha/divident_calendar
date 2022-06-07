########################################################################################
FILES
    1 - nasdaq_daily_Amex.py (main file)
        a - api links are fecthed from SETTINGS file.
        b - Parameter are read from Nasdaq_daily_parameters.csv and SETTINGS file is updated.
        c - sql in initialized
        d - datas are fecthed from each API
            i - iterates through the data
            ii - convert each data into Entry object using EntryGenerator class and check if condition is matched.
            iii - Entry is saved to db if condition is matched else ignores.
    2 - entry_generator.py
        a - takes single data(dict) object as a Parameter and condition are checked using the valid method and retuns and status and Entry object
            eg:-
                EntryGenerator(data: dict).valid() -> Status:bool, entry:Entry
        b - data in the Entry is converted into db requied format before returung. 
    3 - entry.py
        a - Entry class object definition
        b - contains condition methods. 
        c - a method 'transform' to change data to db requied format.
    4 - postgreSQL.py
        a - postgreSQL base class
    5 - postgreSql_client.py
        a - specialised class for this project with requied custom methods. 
        b - inherites 'postgreSql' class. 
    6 - SETTINGS.py
        a - setting file with required static Parameter needed for this product.
    7 - tools.py
        a - few support functions.
    8 - logger.py
        a - logger for loggin info and warnings.
########################################################################################