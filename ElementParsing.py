import xml.etree.ElementTree as ET
tree = ET.parse('small_sample.xml')
root = tree.getroot()
# To get the content if the tag <subject>
for subject in root.iter('subject'):
    print(subject.text)
# To get the content enclosed in the tag <content>
print("===========================================")
for content in root.iter('content'):
    print(content.text)