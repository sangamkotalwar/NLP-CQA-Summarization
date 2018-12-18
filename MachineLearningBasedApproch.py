import xml.etree.ElementTree as ET
from rouge import Rouge
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import numpy as np
tree = ET.parse('small_sample.xml', ET.XMLParser(encoding="utf-8"))
root = tree.getroot()
texts = []
subjects = []
summarizedText = ''
LeadQuestion = []
LeadSentence = []
LastQuestion = []
# To get the content enclosed in the tag <content>
print("===========================================")
for content in root.iter('content'):
    texts.append(content.text)
for subject in root.iter('subject'):
    subjects.append(subject.text)
#print(type(text[:1]))
texts = [str(x) for x in texts] #Converting all the content tags to string
textsdummy = texts
subjects = [str(x) for x in subjects]
subjects = list(subjects)

for subjectdummy in subjects:
    if len(subjectdummy) <= 0:
        subjectdummy = 'No sentence found.'
    if subjectdummy.count('.') == 0:
        subjectdummy += '.'

for text in texts:
    if len(text) <= 0:
        text = 'No sentence found.'
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
    if text == '':
        text = 'No sentence found.'
    summarizedText = text
    if text.count('.') + text.count('?') == 0: # If no full stop or question
        summarizedText = text + '.'
        print("Lead Sentence: "+ summarizedText)
        LeadSentence.append(summarizedText)
        print("Lead Question: "+ summarizedText)
        LeadQuestion.append(summarizedText)
        print("Last Question: "+ summarizedText)
        LastQuestion.append(summarizedText)

    elif text.count('.') > 0 and text.count('?') == 0: # If at least one full stop and no question question
        indexOfDot = text.find('.') + 1
        summarizedText = text[:indexOfDot]
        if summarizedText == '':
            summarizedText = text + '.'
        print("Lead Sentence: "+ summarizedText)
        LeadSentence.append(summarizedText)
        print("Lead Question: "+ summarizedText)
        LeadQuestion.append(summarizedText)
        print("Last Question: "+ summarizedText)
        LastQuestion.append(summarizedText)

    elif text.count('.') == 0 and text.count('?') > 0: # If no full stop and at least on question
        summarizedText = text + '.'
        indexOfQuestion = text.find('?') + 1
        summarizedText = text[:indexOfQuestion]
        if summarizedText == '':
            summarizedText = text + '.'
        print("Lead Sentence: "+ summarizedText)
        LeadSentence.append(summarizedText)
        if summarizedText == '':
            summarizedText = text + '.'
        print("Lead Question: "+ summarizedText)
        LeadQuestion.append(summarizedText)
        if text.count('?') > 1:                 # if questions like "? sentence ?" comes without "."
            secondLastQuestion = text.rfind("?", 0, text.rfind("?")) + 1
            indexOfQuestion = text.rfind('?') + 1            
            summarizedText = text[secondLastQuestion:indexOfQuestion]
            if summarizedText == '':
                summarizedText = text + '.'
            print("Last Question: "+ summarizedText)
            LastQuestion.append(summarizedText)
        else:
            if summarizedText == '':
                summarizedText = text + '.'
            print("Last Question: "+ summarizedText)
            LastQuestion.append(summarizedText)            

    elif text.count('.') > 0 and text.count('?') > 0: # If both dot and question present
        if text.find('.') < text.find('?'):
            index = text.find('.') + 1
            summarizedText = text[:index]
            if summarizedText == '':
                summarizedText = text + '.'
            print("Lead Sentence: "+ summarizedText)
            LeadSentence.append(summarizedText)
        else:
            index = text.find('?') + 1
            summarizedText = text[:index]
            if summarizedText == '':
                summarizedText = text
            print("Lead Sentence: "+ summarizedText)
            LeadSentence.append(summarizedText)           
        if text.count('?') > 0: #To check if we have atleast one lead question/sentence
            indexOfQuestion = text.find('?')
            if text.find('.') > indexOfQuestion: # If we've a lead question
                indexOfQuestion += 1
                summarizedText = text[:indexOfQuestion]
                if summarizedText == '':
                    summarizedText = text
                print("Lead Question: "+ summarizedText)
                LeadQuestion.append(summarizedText)
            else: 
                indexOfDot = text.find('.') + 1
                indexOfQuestion += 1
                summarizedText = text[indexOfDot:indexOfQuestion]
                if summarizedText == '':
                    summarizedText = text
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
                        if summarizedText == '':
                            summarizedText = text
                    else:
                        summarizedText = ""
                        if summarizedText == '':
                            summarizedText = text
                else:        
                    summarizedText = text[secondLastDot:indexOfQuestion]
                    if summarizedText == '':
                        summarizedText = text
                print("Last Question: "+ summarizedText)
                LastQuestion.append(summarizedText)
            else: 
                indexOfDot = text.rfind('.') + 1
                indexOfQuestion = text.rfind('?') + 1
                summarizedText = text[indexOfDot:indexOfQuestion]
                if summarizedText == '':
                    summarizedText = text
                print("Last Question: "+ summarizedText)
                LastQuestion.append(summarizedText)
    else:
        summarizedText = text + '.'
        LeadSentence.append(summarizedText)
        LeadQuestion.append(summarizedText)
        LastQuestion.append(summarizedText)
    print("===========================================")

# print(type(LeadSentence))
# print(type(subjects))
rouge = Rouge()
rouge2fLeadSentence = []
rouge2fLeadQuestion = []
rouge2fLastQuestion = []
# print(len(LeadSentence))
# print(len(LeadQuestion))
# print(len(LastQuestion))
# print(len(subjects))
scoresLeadSentenceJSON = rouge.get_scores(LeadSentence, subjects)
scoresLeadQuestionJSON = rouge.get_scores(LeadQuestion, subjects)
scoresLastQuestionJSON = rouge.get_scores(LastQuestion, subjects)

for item in scoresLeadSentenceJSON:
    json_strLeadSentence = json.dumps(item)
    #load the json to a string
    respLeadSentence = json.loads(json_strLeadSentence)
    #extract an element in the response
    rouge2fLeadSentence.append(respLeadSentence['rouge-2']['f'])

for item in scoresLeadQuestionJSON:
    json_strLeadQuestion = json.dumps(item)
    #load the json to a string
    respLeadQuestion = json.loads(json_strLeadQuestion)
    #extract an element in the response
    rouge2fLeadQuestion.append(respLeadQuestion['rouge-2']['f'])

for item in scoresLastQuestionJSON:
    json_strLastQuestion = json.dumps(item)
    #load the json to a string
    respLastQuestion = json.loads(json_strLastQuestion)
    #extract an element in the response
    rouge2fLastQuestion.append(respLastQuestion['rouge-2']['f'])

print('Lead Sentence: ', rouge2fLeadSentence)
print('Lead Question: ', rouge2fLeadQuestion)
print('Last Question: ',rouge2fLastQuestion)
print('===================================')
RougeScore = pd.DataFrame({'LeadSentence':rouge2fLeadSentence, 'LeadQuestion':rouge2fLeadQuestion, 'LastQuestion':rouge2fLastQuestion})
RougeScore['max_value'] = RougeScore.max(axis=1)
RougeScore['max_question'] = RougeScore.idxmax(axis=1)
print(RougeScore)
print('===================================')

BestRougeSummary = []
intialSentence = []
intialQuestion = []
print('Best Summary according to Rouge-2 F Score: ')
for i in range(len(subjects)):
    if RougeScore['max_question'].iloc[i] == 'LeadSentence':
        BestRougeSummary.append(LeadSentence[i])
        intialSentence.append(1)
        intialQuestion.append(0)
    elif RougeScore['max_question'].iloc[i] == 'LeadQuestion':
        BestRougeSummary.append(LeadQuestion[i])
        intialSentence.append(0)
        intialQuestion.append(1)
    else:
        BestRougeSummary.append(LastQuestion[i])
        intialSentence.append(0)
        intialQuestion.append(0) 

SVMSet = pd.DataFrame({'content':textsdummy, 'subject':BestRougeSummary, 'initialSentence': intialSentence, 'initialQuestion': intialQuestion})
print(SVMSet)
classified = []
for i in range(len(SVMSet)):
    if SVMSet['subject'].iloc[i].count(' ') > 4:
        classified.append(1)
    else:
        classified.append(0)
SVMSet['classified'] = pd.Series(classified).values

print(SVMSet['content'], SVMSet['subject'], SVMSet['classified'])
features = ['initialSentence', 'initialQuestion']
X = SVMSet.loc[:, features].values
y = SVMSet.loc[:,['classified']].values
# print(type(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = svm.SVC(kernel='linear')
model.fit(X_train, np.ravel(y_train,order='C'))
print(model.score(X_train, y_train))
predicted= model.predict(X_test)
print(predicted)