import xml.etree.ElementTree as ET
import csv

#Load the xml File
tree = ET.parse('myMusic.xml')
root = tree.getroot()

#open the csv file and write to it
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:

    #define csv writer
    csvWriter = csv.writer(csvfile)

    #write header
    #**OPTIONAL**
    csvWriter.writerow(["Name", "Artist"])

    #Find the element that holds all the songs
    arr = root[0][17]


    #Iterate through the array and find write the song information to the file
    for element in arr:
        if element.tag == 'dict':
            csvWriter.writerow([element[3].text, element[5].text])

print("CSV file created succesfully")
