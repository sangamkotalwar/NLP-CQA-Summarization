# NLP-CQA-Summarization
Project in NLP Course


# Task List
- [x] Read the paper : Uploaded on [GitHub](https://github.com/sangamkotalwar/NLP-CQA-Summarization/blob/master/I17-1080.pdf)
- [ ] Get Dataset from Yahoo Answers
  - [x] Check status at [Yahoo Answers - Sangamesh's Account](https://webscope.sandbox.yahoo.com/myrequests.php) 
  - [x] Permission granted to download dataset
  - [x] Download [dataset](https://drive.google.com/open?id=1QppmizkKt7NULxvyacwe-KbeMZxDscrf)
  - [ ] Find functions to train our model according to the paper

# Dataset 
* Divided into subjects and content data. Sample data can be found by name - small_sample.xml <br/>
* Data has been extracted and stored by <content> and <subject> tags as contentfullbody.xml and subjectsfullbody.xml 
* If you want to parse the data; Sample code can be be found [here](https://github.com/sangamkotalwar/NLP-CQA-Summarization/blob/master/ElementParsing.py)<br/><br/>
  Also part of code can be seen below:
  ```{python}
  import xml.etree.ElementTree as ET
  tree = ET.parse('dataFileName.xml')
  root = tree.getroot()
  for subject in root.iter('subject'):
      print(subject.text)
  ```

# Deadlines
Submission | Deadline
-------|---------
First Report submission | October 4th, 2018
Second Report Submission | November 13th, 2018
Final Presentation | December 19th and 20th, 2018
Final Report | December 26th, 2018
