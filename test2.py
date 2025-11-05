import tabula as tabl
import os
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-25'



file_directory = 'alarms_2.pdf'

tabl.convert_into(file_directory, "test_2.csv", output_format="csv", pages='all')

