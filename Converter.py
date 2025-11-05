import tabula as tabl
import os
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-25'






file_directory = 'alarms_1.pdf'

tabl.convert_into(file_directory, "test.csv", output_format="csv")


