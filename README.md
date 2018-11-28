# NLP-CQA-Summarization
Project in NLP Course


## Task List
- [x] Read the paper : Uploaded on [GitHub](https://github.com/sangamkotalwar/NLP-CQA-Summarization/blob/master/I17-1080.pdf)
- [x] Get Dataset from Yahoo Answers
  - [x] Check status at [Yahoo Answers - Sangamesh's Account](https://webscope.sandbox.yahoo.com/myrequests.php) 
  - [x] Permission granted to download dataset
  - [x] Download [dataset](https://drive.google.com/open?id=1QppmizkKt7NULxvyacwe-KbeMZxDscrf)
- [x] Rule Based Extractive Summarization
- [x] Extractive Summarization using Gensim
- [ ] ROUGE-2 : Machine Learning based approach

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

## Rule Based extractive summarization

### Update 29/11/2018

We've abide by the rules given in the paper : As rule-based approaches, we used three rules to compare: “Lead Sentence”, “Lead Question”, and “Last Question”. The first sentence presented (Lead Sentence) is known as a strong baseline for generic summarization tasks. However, in the question summarization, the summaries should be
also questions. Therefore, we adopted methods to select a question in the input by heuristic rules, choosing the first question (Lead Question) and the last question (Last Question). A sentence was determined to be a question if the last character is “?”.<br/>
That is the lead question will be our summary for the content. We were successfull in implementing the rule.<br/>
When we run the code in command prompt:
  ```python
  python3 RuleBasedExtractive.py
  ```
  We get the following output:<br/><br/>
  ![Rule based output](https://i.imgur.com/7XWYogk.jpg)
  
  Here we can see that since the lead question is itself the summary we actually are not getting a quite positive result. In some cases the question may actually have the complete essence of the content like the 3rd &4th one from the given output; but in most of the cases this is least likely.
  
## Extractive Summarization using Gensim

### Update 25/11/2018
We cannot do extractive summarization using Gensim since the summarization function requires input should be a string, and must be longer than INPUT_MIN_LENGTH sentences for the summary to be extracted. And from [documentation](https://github.com/summanlp/gensim/blob/develop/gensim/summarization/summarizer.py#L17) we see that INPUT_MIN_LENGTH is 10 sentences. And none of our input data from <content> tag is longer like 10 sentenses. <b><i>So we cannot apply Gensim for lengthy question summarization for our curated data.</i></b>
<br/>File can be found [here](https://github.com/sangamkotalwar/NLP-CQA-Summarization/blob/master/ExtractiveSummarizationUsingGensim.py) with name: ExtractiveSummarizationUsingGensim.py
<br/>When we run the code in command prompt:
  ```python
  python3 ExtractiveSummarizationUsingGensim.py
  ```
  It gives blank output since we don't have any input text with number of sentences more than 10
  Here is the Output:<br/>
  ![TRY1 No output](https://i.imgur.com/KTlPJMv.jpg?1)
  
### Update 27/11/2018
We're now able to extract summarization by tweaking with some parameteres of the input. We've by-passed the the input limit and now we're able to get results for content with more than 10 sentences. We're not getting that proper results; accuracy of the results is low. We get output of summarizing questions as some statements but not a question. This is a big disadvantage of using <b> Extractive Approacha</b>. As we can see in the following output photos:
<br/>When we run the code in command prompt:
  ```python
  python3 ExtractiveSummarizationUsingGensim.py
  ```
  ![Output 1 -Gensim](https://i.imgur.com/jMNr438.jpg?1)
  The first output does not correctly summarize the question but in the second one we're able to get the desired output. We don't say it to be completely corrrect but the output is giving some insight about the original content question. 
  
## Deadlines
Submission | Deadline
-------|---------
First Report submission | October 4th, 2018
Second Report Submission | November 13th, 2018
Final Presentation | December 19th and 20th, 2018
Final Report | December 26th, 2018
