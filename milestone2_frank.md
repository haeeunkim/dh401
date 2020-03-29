# Data gathering and preprocessing
The requirement for this milestone is an Jupyter notebook* in which you present the data that you will be using for your project. It is not the exploratory analysis of the full data set, which is milestone 3. Rather, the idea is to prove--based on milestone 1 and on the feedback that you have received for it--a deepened reflection on your project goal (section 1) and to present technical details (sections 2 & 3). Submit your notebook to your git repository in a form, that all outputs are present, i.e. that we don't have to rerun the notebook.

* Depending on the tools you use, you can also provide some other notebook format. In this case, make sure that we can read this format by converting it to PDF/HTML/Markdown.

# 1. Narrowing down the research question
As discussed in the feedback session, your research question needs to be pinned down to one or several concrete and attainable goals. In the first section of the notebook please address the following points:

- Name your concrete questions and explain them briefly:

How different is the rhythmic part of flow between 2 (or 3) rap genres/styles for the same language and for different languages, here English (U.S.) and French? 

- Analyse how these questions relate to your original idea, that is, in what way they narrow it down:

Our original idea was to analyze the differences between U.S. and French rap but without any conditions on the songs excepted that it should be “famous”. Here we narrowed it down by selecting 2 to 3 different rap genres/styles that are all spaced in time (old school: 1990-2000 | gangsta: 2000-2015 | trap: 2015-2020) so we will on focus on these styles and we can restrict more our database. Moreover, we determined the features that seemed important for us to describe the flow and we discarded the ones that were less important and/or too much time consuming. Indeed, since we don’t have all the time we want and since we want to encode data for our database, we cannot encode all the same features as the MCFlow corpus. Here are the features we want to encode and analyze: the metrical duration and position of the syllables (including the rest), the metrical position of a new phrase/sub-phrase, the metrical position of the rhymes and the corresponding lyrics. We are still hesitating with one feature which takes a lot of time but which is also an important feature: the metrical position of stressed/unstressed syllables. We would require your help to determine if this feature should be taken into account or not.

- Describe the dataset you selected and the information represented in it:

For the US part, we will take the data from the MCFlow corpus. We selected the songs that were on one of our desired genre/style (the classification is totally subjective).
On the other hand, we will encode the French part into MusicXML files which is a standart XML file but modified to contain the musical information we need (see section 2 for further explanations). We selected the French songs based on the popularity of the songs in each genre/style. For now we have a list of 20 songs per genre but we will at first restrict to 10 songs per genre.

- Discuss how the data enables you to answer your questions:

With the help of all the features, we will be enable to determine the syllable rate, the rhyme density, the average rhyme chain, syncopation (if we implement the syllables stress), the proportion of the metric position of syllables and rhymed syllables and so on for each song, artist, genre or languages. These results will lead us to some differences between genre and languages.

- Formulate educated guesses on your outcomes based on this data:

From what we eared and from the results of the MCFLow study, we think that flow features will vary significantly between different genres/stlyes of rap but these flow features will vary less between the two languages (we have more differences between genres than language). We also think that we will observe a “standardization of the flow” for the trap genre and that it does not depend on the language (we think that the French rap adapted his language to fit the U.S. flow for the trap genre). 

- Reason on how you can tell in the end whether these outcomes have manifested or not and how confident you will possibly be:

Our guesses are based on all the rap songs we eared and we could “feel” these differences specially for the trap genre where the rapper’s flows seem all the same so we guess, for example, that there will be less entropy on the metric placement of rhymed syllables for the trap genre than for the old school genre. We also observed that flow depends strongly on the genre/style so instead of comparing artists, we think that comparing genre will lead to a better “classification of flow”. 

There is no point in answering to these points one after another. Rather, your grade will partly be based on how well the structure of your text reveals and supports your reflection. (Hint: A good advice could be to draft concrete answers to every point and to then look at the full picture in order to design a compelling argumentative structure. Think about how a hypothetical reader can understand the text without already knowing what you want to say.)

# 2. Gathering the data
The other two sections are more technical. Here you can show that you understand your data and know how to use it. You can be brief in your answers. Section 2 may be supported with (an) informative plot(s).

- Where do you get your data from:

For the U.S. part: the MCFlow corpus: http://www.rapscience.net/Data/downloads.html 
For the French part: We will do our own data base.

- How do you get it:

For the U.S. part: 

For the French part: After the songs’s selection, we will encode them like this: First you download the mp3 version of the song (from youtube for example), then you add this song to a new track on a musical producing software (here it will be Logic pro). Then, you determine its tempo and you synchronize the beat on the song. After this, we add a new track and we tap the same note (A for example) on a pad (or keyboard) when we ear a syllable. We do this for the entire song and then we add the lyrics to each syllables on another note (G for example) and we do the same for the rhyme position and the breaks (and maybe the stress position of the syllables). Finally, we can export it as a MusicXML file and we will get the data with the help of a XML parser.


- What is the maximum available amount in theory (in the case of incomplete data aquisition):

For the U.S part we restricted the corpus depending on the genre so now we have around 52 songs instead of 124. For the French part, we selected 20 songs per genre so 60 songs in total. 

- How much can you actually hope to lay hand on for milestone 3 on April 20th:

We did an encoding test of a song without encoding the (un)stressed syllables and it took us an entire day. But we think that we can do one song in one afternoon (it depends on the genre of the song) so we can maybe have 15 to 20 songs in total until April 20th but it is still not the right timing estimation…

# 3. Data format
This section is the main reason why this milestone is to be delivered in a Jupyter notebook: Give insightful examples for every question by loading and transforming data samples.

- What format(s) does the raw data come in / How is the information that the dataset represents encoded in this format:

For the US part, the data are encoded in "kern format" and where each column correspond to as specific feature. For example, column number one correspond to the rhythmic position and duration of the syllables, the second is the metrical position of the stressed/unstressed syllables and so on… We have one file for each song and each verse is separated in the file. Here is an example of the file:
METTRE IMAGE 1!!!


For the French part, we will have a MusicXML file for each song. We will need to implement an XML parser to get the data. Here you can see the result of the encoding for one song: a part of the resulting partition and a part of the corresponding MusicXML file:
METTRE IMAGE 2!!!

METTRE IMAGE 3!!!


- How is the information that the dataset represents encoded in this format?
- Load your dataset and show examples of how you access the information that you are interested in. 
- Give an overview of your dataset by plotting some basic statistics of the relevant features and/or metadata. 
