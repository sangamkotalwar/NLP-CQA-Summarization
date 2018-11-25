import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
## Installing gensim from pip install -U gensim
from gensim.summarization import summarize 
import xml.etree.ElementTree as ET
#import pandas as pd
tree = ET.parse('contentfullbody.xml', ET.XMLParser(encoding="utf-8"))
root = tree.getroot()
text = ["I keep getting annoying Winfixer Pop Ups . I have tried all sorts of ad removal programs to get rid of them but without success . How can I get rid of them ?"]
# To get the content enclosed in the tag <content>
print("===========================================")
for content in root.iter('content'):
    text.append(content.text)
print(type(text[:1]))
text = [str(x) for x in text]
print(text[:1])
#textDf = pd.DataFrame(text)
#print(textDf.head())
for text in text[:1]:
    #print(type(text))
    #print(len(text))
    print('Summary:')
    print(summarize(text))
#print(summarize(text[:1]))