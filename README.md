# NLP-CQA-Summarization
Project in NLP Course


## Task List
- [x] Read the paper : Uploaded on [GitHub](https://github.com/sangamkotalwar/NLP-CQA-Summarization/blob/master/I17-1080.pdf)
- [ ] Get Dataset from Yahoo Answers
  - [x] Check status at [Yahoo Answers - Sangamesh's Account](https://webscope.sandbox.yahoo.com/myrequests.php) 
  - [x] Permission granted to download dataset
  - [x] Download [dataset](https://drive.google.com/open?id=1QppmizkKt7NULxvyacwe-KbeMZxDscrf)
  - [x] Rule Based Extractive Summarization using Gensim
  - [ ] Find functions to train our model according to the paper

## Dataset 
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

## Rule Based Extractive Summarization using Gensim

### Update 25/11/2018
We cannot do extractive summarization using Gensim since the summarization function requires input should be a string, and must be longer than INPUT_MIN_LENGTH sentences for the summary to be extracted. And from [documentation](https://github.com/summanlp/gensim/blob/develop/gensim/summarization/summarizer.py#L17) we see that INPUT_MIN_LENGTH is 10 sentences. And none of our input data from <content> tag is longer like 10 sentenses. <b><i>So we cannot apply Gensim for lengthy question summarization for our curated data.</i></b>
<br/>File can be found [here](https://github.com/sangamkotalwar/NLP-CQA-Summarization/blob/master/RuleBasedExtractiveSummarizationUsingGensim.py) with name: RuleBasedExtractiveSummarizationUsingGensim.py
<br/>When we run the code in command prompt:
  ```python
  python3 RuleBasedExtractiveSummarizationUsingGensim.py
  ```
  It gives blank output since we don't have any input text with number of sentences more than 10
  Here is the Output:<br/>
  ![Imgur](https://i.imgur.com/KTlPJMv.jpg?1)
  
### Update 27/11/2018
We're now able to extract summarization by tweaking with some parameteres of the input. We've by-passed the the input limit and now we're able to get results for content with more than 10 sentences. We're not getting that proper results; accuracy of the results is low. We get output of summarizing questions as some statements but not a question. This is a big disadvantage of using rule based <b> Extractive Approacha</b>. As we can see in the following output photos:
<br/>When we run the code in command prompt:
  ```python
  python3 RuleBasedExtractiveSummarizationUsingGensim.py
  ```
  ![Output 1 -Gensim](https://i.imgur.com/jMNr438.jpg?1)
  The first output does not correctly summarize the question but in the second one we're able to get the desired output. We dn't say it to be completely corrrect but the output is giving some insight about the original content question.

## Deadlines
Submission | Deadline
-------|---------
First Report submission | October 4th, 2018
Second Report Submission | November 13th, 2018
Final Presentation | December 19th and 20th, 2018
Final Report | December 26th, 2018
