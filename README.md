# Text Summarization
This is the  process of shortening long pieces of text to create a coherent and fluent summary having only the main points outlined in the document.
Extractive summarization means identifying important sections of the text and generating them verbatim producing a subset of the sentences from the original text.
This model was built with NLTK libraries using the extractive process using the following five steps:
1. Creating the word frequency table.
2. Tokenize the sentences.
3. Score the sentences using the term frequency method.
4. Find the threshold value which the average score of the sentences.
5. Generate the summary.

# Next step is creating a summarizer API using flask framework.
The necessary libraries used for this can be found in the requirements.txt file.
An API is an application programmable interface that enables communication between two applications.
This api uses a POST request method to get stories inputed on the form which is created in the index.html file and summarizes the text, the summary is displayed to the user thus: 'Sumnmarized Text is: ...'
# How to test this API locally 
1.Fork and clone this repo
2.Install all the dependencies used which will be found in the requirements.txt file.
3.Run the app.py file using the command: python app.py

# Sumtext using Summy APK
This summarizer was created using the summy apk and it was deployed to google cloud.
To test: using postman, send a post request  to the https address as shown in the example when you click on this link: https://docufixsumtext.appspot.com/
When using this api, you can send a post request using any language format as shown in the example.

