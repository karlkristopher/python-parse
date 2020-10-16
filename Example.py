#!/usr/bin/env python3
import xml.etree.ElementTree as ET


mytree = ET.parse('Sample.xml')

myroot = mytree.getroot()

print(mytree)

