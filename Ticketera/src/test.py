import os
import json

def getConnectionString():
    with open(os.path.join(os.getcwd(), "src", "data", "server_data.json"), "r", encoding='utf-8') as file:
        json_file= json.load(file)
        old_con_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=GONZALO\DBGON;'
        r'DATABASE=turnos;'
        r'Trusted_Connection=yes;'
        )
        if (json_file['TRUSTED_CONNECTION']=='yes'):
            connection_string = (f"DRIVER={json_file['DRIVER']};"
                                f"SERVER={json_file['SERVER']};"
                                f"DATABASE={json_file['DATABASE']};"
                                f"Trusted_Connection={json_file['TRUSTED_CONNECTION']};")

        else:
            connection_string = (f"DRIVER={json_file['DRIVER']};"
                                f"SERVER={json_file['SERVER']};"
                                f"DATABASE={json_file['DATABASE']};"
                                f"USERNAME={json_file['USERNAME']};"
                                f"PASSWORD={json_file['PASSWORD']};")
        return connection_string

    
getConnectionString()