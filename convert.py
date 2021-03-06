import xml.etree.ElementTree as ET
from xml.dom import minidom
import io as io

def createXML( values, activities ):
    date = values[0]
    dateValues = date.split(" ")
    day = dateValues[0]
    month = dateValues[1]
    year = dateValues[2]
    length = values[1].strip()
    seconds = values[2].strip()
    # pulse = values[3]
    # weight = values[4]
    # weather = values[5]
    notes = values[6].strip()
    # shoe  = values[7]
    activity = ET.SubElement(activities, "Activity", Sport="Running")
    id = ET.SubElement(activity, "Id")
    id.text = '20%s-%s-%sT12:00:00Z'%(year,month,day)
    lap = ET.SubElement(activity, "Lap", StartTime='20%s-%s-%sT12:00:00Z'%(year,month,day))
    tts = ET.SubElement(lap, "TotalTimeSeconds")
    tts.text = seconds
    dm = ET.SubElement(lap, "DistanceMeters")
    dm.text = length
    if notes:
      notesEle = ET.SubElement(activity, "Notes")
      notesEle.text = notes

#date,length,seconds,pulse,weight,weather,notes,shoe 
f = io.open('Laufergebnisse.txt','r', encoding='iso-8859-1')

root = ET.Element('TrainingCenterDatabase')
activities = ET.SubElement(root, "Activities")

for line in f:
    values = line.rstrip().split(';')
    createXML(values, activities)
    
f.close()

t = minidom.parseString(ET.tostring(root)).toprettyxml(encoding="iso-8859-1") # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
tree = ET.ElementTree(ET.fromstring(t))

tree.write("MyRun.tcx", encoding="iso-8859-1")
