import xml.etree.ElementTree as ET
from xml.dom import minidom

def createXML( values ):
    date = values[0]
    # length = values[1]
    # seconds = values[2]
    # pulse = values[3]
    # weight = values[4]
    # weather = values[5]
    # notes = values[6]
    # shoe  = values[7]
    


#date,length,seconds,pulse,weight,weather,notes,shoe 
f = open('Laufergebnisse.txt','r')

root = ET.Element('TrainingCenterDatabase')
activities = ET.SubElement(root, "Activities")

for line in f:
    values = line.rstrip().split(';')
    createXML(values)
    
f.close()

t = minidom.parseString(ET.tostring(root)).toprettyxml() # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
tree = ET.ElementTree(ET.fromstring(t))

tree.write("MyRun.tcx")
