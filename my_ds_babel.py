import sqlite3
import csv
import pandas as pd
from io import StringIO




def sql_to_csv(database, table_name):
    # Connect to the database
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # Retrieve column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_names = [row[1] for row in cursor.fetchall()]

    # Retrieve table data
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Create CSV string
    csv_string = ','.join(column_names) + '\n'
    for row in rows:
        csv_string += ','.join(map(str, row)) + '\n'

    # Close the database connection
    connection.close()

    # Remove the extra empty line at the end
    csv_string = csv_string.strip()

    return csv_string


# Part II: CSV to SQL
def csv_to_sql(csv_content: str, database_name: str, table_name: str) -> None:
    """
    Convert the CSV content to SQL format and insert into the specified table in the SQLite database.
    Args:
        csv_content (str): CSV content as a string in the format "ColA,ColB,ColC\n1,2,3\n4,5,6\n".
        database_name (str): Filename of the SQLite database to insert the data.
        table_name (str): Name of the table in the database to insert the data.
    """
    # Read the CSV content using pandas
    data = pd.read_csv(csv_content)
    
    # Connect to the SQLite database
    with sqlite3.connect(database_name) as conn:
        # Insert the data into the specified table in the database
        data.to_sql(table_name, conn, if_exists='replace', index=False)




if __name__ == "__main__":
    csv_data = sql_to_csv('all_fault_line.db', 'fault_lines')
    print("CSV Data:")
    #print(csv_data)

    # # Part III: Convert list of all volcanoes from CSV to SQL
    # csv_content = open("list_volcano.csv")
    # csv_to_sql(csv_content, 'list_volcanos.db', 'volcanos')

    # print("Conversion from CSV to SQL for volcanos is done.")

    # # Part III: Convert list of all fault lines from SQL to CSV
    # csv_content = sql_to_csv('all_fault_line.db', 'fault_lines')
    # with open("all_fault_lines.csv", 'w') as out_file:
    #     out_file.write(csv_content)

    # print("Conversion from SQL to CSV for fault lines is done.")
    #print(sql_to_csv('sourse_all_fault_line.db','fault_lines'))

#csv_content = open("sourse_list_volcano.csv")
#csv_to_sql(csv_content, 'list_volcanos.db','volcanos')