# Research Question
Rap is a unique form of vocal artistry which straddles the boundary between song and poetry. Recently being prevalent not only in authentic Hip-Hop music, but in Pop music as well, rap has undoubtably become an imperative part of contemporary music. Having deemphasized pitch structures in favor of rhythmic and poetic structure, the sonic texture of rap music is highly related to the linguistics, such as rhymes, pronunciations, and phrasing. 

Several studies on rap music have already been done. In sociology and media studies, understanding rhetoric and code of rap music was one way to understand contemporary street culture, which is mainly done by semantically analyzing a small collection of rap lyrics. On the other hand, in computational musicology, some studies have come up with the computational definition of rhythmic rap flow as well as the way to encode them. However, not much work has been done on different rhythmic stress in rap music between languages, neither on small collection of dataset or large-scale dataset. 

In our study, we aim to compare the rhythmic flow of rap music in different languages, in particular, English and French. By statistically analyzing sonic musicalities of different rap music, we aim to discover and compare the ‘norm’ of anglophone and francophone rap. Furthermore, by analyzing stressed syllables and words, we aim to relate the English and French linguistics to our corpus-based rhythmic analysis.

# Concepts and Data
The concrete focus of our project is the rhythmic flow of rap music, which will be defined by syllabic onset, rhythmic stress, , inter-onset interval, pitch accents, measures, and lyrical phrasing. In order to operationalize this, we will adopt the encoding methodology used in MCFlow database, which is created by the researchers of Ohio University in 2015 and now publically available at www.rapscience.net. This database contains a corpus of 124 popular American rap songs, where flow of a rapper is encoded into a symbolic rhythmic representation that summarizes speed, rhyme density, metric position of stressed syllables, metric position of rhymes, phrase length and the metric position of phrases. We will use this data for the anglophone part of our studies.

Since there is no publically available dataset for the francophone counterpart, we will manually encode a collection of popular francophone rap songs with the aforementioned encoding system, which will be done as following:
 1. Select 100~150 songs that will compose our francophone corpus. In order to keep the consistency between the two dataset, several factors, such as popularity, publication year, and artist, will be taken into account. 
 2. Transcribe syllabic onsets of each song. This will be done with a Digital Audio Workstation software, Logic Pro X.
 3. Add rhythmic stress and corresponding syllable to each onset.
 4. Export the data in MCFlow format.
We might control or modify the features to be encoded or the selection of dataset throughout our study if necessary.

# Methods
Considering the relatively small size of the corpus, we will focus more on basic statistics of rap flow rather than taking any machine-learning based approach. This may include probability distribution of phrasal length/tempo/syncopation/stressed syllable, etc, which will summarize rhythmic characterisics of anglophone and francophone rap. 
Then the result will be combined with lyrics to discover if rhythmic differences are related to semantics of lyrics or syntacticall difference between two languages. In this stage, we might use some of anglophone/francophone natural language processing libraries to manipulate the lyrics in a consistent and well-established way. 

# Literature
Our study is strongly related to the following publications:
1. MCFlow: A Digital Corpus of Rap Transcriptions (Condit-Schultz, 2015): Provided the dataset and encoding scheme of rap flow. Histocial analysis on rhythmic features of anglophone rap music. 
2. Anticipatory syncopation in a rock: a corpus study (Tan, Lustig, Temperly, 2018): Provided the methodology to define and measure a certain rhythmic feature 
3. Second-Position Syncopation in European and American Vocal Music (Temperley, 2019): Corpus analysis on second-position syncopation in 19th-century English, Scottish, Euro-American, African-American, French, German, and Italian vocal music. 

Those publications provides the key methodology and liguistic-musicology perspective for our study. Above all these, we will add a specific comparative analysis between only two languages in a certain genre of music and aim for a deeper understanding on sonic and semantical musicality of rap music.


# Additional Remark
Since we have to build our francophone corpus from scratch, we might need some support in how to choose the songs that is similar enough with its anglophone counterpart. We alsso suppose that we might need some support or guidance while analyzing the encoded result or determining the relevant features of music, in the latter part of our study. 
