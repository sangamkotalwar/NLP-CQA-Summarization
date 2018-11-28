# As rule-based approaches, we used three rules to
# compare: “Lead Sentence”, “Lead Question”, and
# “Last Question”. The first sentence presented
# (Lead Sentence) is known as a strong baseline
# for generic summarization tasks. However, in the
# question summarization, the summaries should be
# also questions. Therefore, we adopted methods to
# select a question in the input by heuristic rules,
# choosing the first question (Lead Question) and
# the last question (Last Question). A sentence was
# determined to be a question if the last character is
# “?” or the first word is an interrogative word. 
import xml.etree.ElementTree as ET
tree = ET.parse('contentfullbody.xml', ET.XMLParser(encoding="utf-8"))
root = tree.getroot()
text = []
summarizedText = ''
# To get the content enclosed in the tag <content>
print("===========================================")
for content in root.iter('content'):
    text.append(content.text)
#print(type(text[:1]))
text = [str(x) for x in text] #Converting all the content tags to string

for text in text:
    if text.count('?') > 0: #To check if we have atleast one lead question/sentence
        print('Content:')
        print(text)
        print('Summary:')
        indexOfQuestion = text.find('?')
        if text.find('.') > indexOfQuestion: # If we've a lead question
            indexOfQuestion += 1
            summarizedText = text[:indexOfQuestion]
            print(summarizedText)
        elif text.find('.') < indexOfQuestion: # To find next/last question
            indexOfDot = text.find('.') + 1
            indexOfQuestion += 1
            summarizedText = text[indexOfDot:indexOfQuestion]
            print(summarizedText)
        else:
            print('No output since no Lead question available')
        print("===========================================")