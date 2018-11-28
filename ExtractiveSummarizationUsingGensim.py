# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
## Install gensim from pip install -U gensim
from gensim.summarization import summarize 
import xml.etree.ElementTree as ET
# import pandas as pd
tree = ET.parse('contentfullbody.xml', ET.XMLParser(encoding="utf-8"))
root = tree.getroot()
text = []
# To get the content enclosed in the tag <content>
print("===========================================")
for content in root.iter('content'):
    text.append(content.text)
#print(type(text[:1]))
text = [str(x) for x in text] #Converting all the content tags to string

for text in text:
    if text.count('.') + text.count('?') > 9: #To check if we have more than 10 sentences
        print('Content:')
        print(text)
        print('Summary:')
        print(summarize(text))
        print("===========================================")
