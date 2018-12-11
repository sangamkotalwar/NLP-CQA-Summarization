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
LeadQuestion = []
LeadSentence = []
LastQuestion = []
# To get the content enclosed in the tag <content>
print("===========================================")
for content in root.iter('content'):
    text.append(content.text)
#print(type(text[:1]))
text = [str(x) for x in text] #Converting all the content tags to string

for text in text:
    print('Content: ')
    text = text.replace("...",".")
    text = text.replace("???","?")
    text = text.replace("!!!","!")
    text = text.replace("!!","!")
    text = text.replace("..",".")
    text = text.replace("??","?")
    text = text.replace('\r', '').replace('\n', '')
    print(text)
    print('Summary: ')
    if text.count('.') + text.count('?') == 0: # If no full stop or question
        summarizedText = text
        print("Lead Sentence: "+ summarizedText)
        LeadSentence.append(summarizedText)
        print("Lead Question: "+ summarizedText)
        LeadQuestion.append(summarizedText)
        print("Last Question: "+ summarizedText)
        LastQuestion.append(summarizedText)

    if text.count('.') > 0 and text.count('?') == 0: # If at least one full stop and no question question
        indexOfDot = text.find('.') + 1
        summarizedText = text[:indexOfDot]
        print("Lead Sentence: "+ summarizedText)
        LeadSentence.append(summarizedText)
        print("Lead Question: "+ summarizedText)
        LeadQuestion.append(summarizedText)
        print("Last Question: "+ summarizedText)
        LastQuestion.append(summarizedText)

    if text.count('.') == 0 and text.count('?') > 0: # If no full stop and at least on question
        summarizedText = text
        indexOfQuestion = text.find('?') + 1
        summarizedText = text[:indexOfQuestion]
        print("Lead Sentence: "+ summarizedText)
        LeadSentence.append(summarizedText)
        print("Lead Question: "+ summarizedText)
        LeadQuestion.append(summarizedText)
        if text.count('?') > 1:                 # if questions like "? sentence ?" comes without "."
            secondLastQuestion = text.rfind("?", 0, text.rfind("?")) + 1
            indexOfQuestion = text.rfind('?') + 1            
            summarizedText = text[secondLastQuestion:indexOfQuestion]
            print("Last Question: "+ summarizedText)
            LastQuestion.append(summarizedText)
        else:
            print("Last Question: "+ summarizedText)
            LastQuestion.append(summarizedText)            

    if text.count('.') > 0 and text.count('?') > 0: # If both dot and question present
        if text.find('.') < text.find('?'):
            index = text.find('.') + 1
            summarizedText = text[:index]
            print("Lead Sentence: "+ summarizedText)
            LeadSentence.append(summarizedText)
        else:
            index = text.find('?') + 1
            summarizedText = text[:index]
            print("Lead Sentence: "+ summarizedText)
            LeadSentence.append(summarizedText)           
        if text.count('?') > 0: #To check if we have atleast one lead question/sentence
            indexOfQuestion = text.find('?')
            if text.find('.') > indexOfQuestion: # If we've a lead question
                indexOfQuestion += 1
                summarizedText = text[:indexOfQuestion]
                print("Lead Question: "+ summarizedText)
                LeadQuestion.append(summarizedText)
            else: 
                indexOfDot = text.find('.') + 1
                indexOfQuestion += 1
                summarizedText = text[indexOfDot:indexOfQuestion]
                print("Lead Question: "+ summarizedText)
                LeadQuestion.append(summarizedText)
            if text.rfind('.') > text.rfind('?'): # If we've a last question
                indexOfQuestion = text.rfind('?') + 1
                secondLastDot = text.rfind(".", 0, text.rfind("."))
                secondLastQuestion = text.rfind("?", 0, text.rfind("?"))
                if secondLastDot == -1:
                    if secondLastQuestion != -1:
                        index = secondLastQuestion + 1
                        summarizedText = text[index:indexOfQuestion]
                    else:
                        summarizedText = ""
                else:        
                    summarizedText = text[secondLastDot:indexOfQuestion]
                print("Last Question: "+ summarizedText)
                LastQuestion.append(summarizedText)
            else: 
                indexOfDot = text.rfind('.') + 1
                indexOfQuestion = text.rfind('?') + 1
                summarizedText = text[indexOfDot:indexOfQuestion]
                print("Last Question: "+ summarizedText)
                LastQuestion.append(summarizedText) 
    print("===========================================")