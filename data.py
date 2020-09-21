import nltk; nltk.download('stopwords')

import re
import numpy as np
import pandas as pd
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
%matplotlib inline

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

# df1 = pd.read_json('https://raw.githubusercontent.com/selva86/datasets/master/newsgroups.json')
# print(df1.target_names.unique())
# df1.head()
# df1.columns
# df.columns = df1.columns 
# df1 = pd.concat([df, df1], ignore_index=True)
# df1.head()
# df1.info()

###
df1 = pd.read_csv('data.csv')


from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'line'])

# Convert to list
data = df1.content.values.tolist()


#lowercase

data = [sent.lower() for sent in data]


# Remove Emails
data = [re.sub('\S*@\S*\s?', '', sent) for sent in data]

# Remove new line characters
data = [re.sub('\s+', ' ', sent) for sent in data]

# Remove distracting single quotes
data = [re.sub("\'", "", sent) for sent in data]

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

data_words = list(sent_to_words(data))

print(data_words[0])

bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
# trigram = gensim.models.Phrases(bigram[data_words], threshold=100)  

# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod = gensim.models.phrases.Phraser(bigram)
# trigram_mod = gensim.models.phrases.Phraser(trigram)

# See trigram example
# print(trigram_mod[bigram_mod[data_words[0]]])

# Define functions for stopwords, bigrams, trigrams and lemmatization
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

# def make_trigrams(texts):
#     return [trigram_mod[bigram_mod[doc]] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out



# Remove Stop Words
data_words_nostops = remove_stopwords(data_words)

# Form Bigrams
data_words_bigrams = make_bigrams(data_words_nostops)

# Initialize spacy 'en' model, keeping only tagger component (for efficiency)
# python3 -m spacy download en
nlp = spacy.load('en', disable=['parser', 'ner'])

# Do lemmatization keeping only noun, adj, vb, adv
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

print(len(data_lemmatized))
from gensim.corpora import Dictionary
dictionary = Dictionary(data_lemmatized)

# Filter out words that occur less than 20 documents, or more than 50% of the documents.
dictionary.filter_extremes(no_below=10, no_above=0.6)

# dictionary.save_as_text('dictionary.txt')

#d = Dictionary.load_from_text('dictionary.txt')






# Create Dictionary
temp = dictionary[0]
id2word = dictionary.id2token
# id2word = corpora.Dictionary(data_lemmatized)
print(len(id2word))
id2word

# Create Corpus
texts = data_lemmatized

# import json
# with open('texts.txt','w')as f:
#     f.write(json.dumps(texts))

# with open('texts.txt', 'r') as f:
#     t = json.loads(f.read())



# Term Document Frequency
# corpus = [id2word.doc2bow(text) for text in texts]
corpus = [dictionary.doc2bow(doc) for doc in texts]

print(len(corpus))

from gensim.models.ldamulticore import LdaMulticore
num_topics = 35
chunksize = 2000
passes = 20
iterations = 400
eval_every = None  # Don't evaluate model perplexity, takes too much time.



lda_multicore = LdaMulticore(
    corpus=corpus,
    id2word=id2word,
    chunksize=2000,
    alpha='asymmetric',
    eta='auto',
    iterations=400,
    num_topics=15,
    passes=20,
    workers=3,
    eval_every=eval_every)

model =  LdaMulticore(
                corpus=corpus,
                id2word= id2word,
                alpha='asymmetric',
                eta='auto',
                num_topics=15,
                passes=10,
                workers=3,
                eval_every=None,
                per_word_topics=True)

# lda_multicore = LdaMulticore(
#     corpus=corpus,
#     id2word=id2word,
#     chunksize=2000,
#     alpha='asymmetric',
#     eta='auto',
#     iterations=400,
#     num_topics=num_topics,
#     passes=20,
#     workers=3,
#     eval_every=eval_every)

# lda_multicore = LdaMulticore(
#     corpus=corpus,
#     id2word=id2word,
#     chunksize=2000,
#     alpha='asymmetric',
#     eta='auto',
#     iterations=400,
#     num_topics=20,
#     passes=20,
#     workers=3,
#     eval_every=eval_every)

# Build LDA model
# lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
#                                            id2word=id2word,
#                                            num_topics=35, 
#                                            random_state=100,
#                                            update_every=1,
#                                            chunksize=100,
#                                            passes=10,
#                                            alpha='auto',
#                                            per_word_topics=True)


pprint(lda_multicore.print_topics())
doc_lda = lda_multicore[corpus]

# Compute Perplexity
print('\nPerplexity: ', lda_multicore.log_perplexity(corpus))  # a measure of how good the model is. lower the better.

# Compute Coherence Score
coherence_model_lda = CoherenceModel(model=model, texts=data_lemmatized, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)

pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_multicore, corpus, dictionary)
vis

mallet_path = '/home/ubuntu/Signal/mallet-2.0.8/bin/mallet'
ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=35, id2word=id2word)

coherence_model_ldamallet = CoherenceModel(model=ldamallet, texts=data_lemmatized, dictionary=dictionary, coherence='c_v')
coherence_ldamallet = coherence_model_ldamallet.get_coherence()
print('\nCoherence Score: ', coherence_ldamallet)

def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = LdaMulticore(
                id2word= id2word,
                alpha='asymmetric',
                eta='auto',
                num_topics=num_topics,
                passes=10,
                workers=3,
                per_word_topics=True,
                eval_every=None)
        # model = gensim.models.ldamodel.LdaModel(corpus=corpus,
        #                                    id2word=id2word,
        #                                    num_topics=num_topics, 
        #                                    random_state=100,
        #                                    update_every=1,
        #                                    passes=10,
        #                                    alpha='auto',
        #                                    )
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values


model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=corpus, texts=data_lemmatized, start=5, limit=41, step=5)
# model_list1, coherence_values1 = compute_coherence_values(dictionary=dictionary, corpus=corpus, texts=data_lemmatized, start=5, limit=41, step=5)


limit=41; start=5; step=5;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()
coherence_values

for m, cv in zip(x, coherence_values):
    print("Num Topics =", m, " has Coherence Value of", round(cv, 4))

optimal_model = lda_multicore
model_topics = optimal_model.show_topics(formatted=False)
pprint(optimal_model.print_topics(num_words=10))

def format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=data):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)


df_topic_sents_keywords = format_topics_sentences(ldamodel=optimal_model, corpus=corpus, texts=data)
df_topic_sents_keywords

# Format
df_dominant_topic = df_topic_sents_keywords.reset_index()
df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']

# Show
df_dominant_topic.head(10)

sent_topics_sorteddf_mallet = pd.DataFrame()

sent_topics_outdf_grpd = df_topic_sents_keywords.groupby('Dominant_Topic')

for i, grp in sent_topics_outdf_grpd:
    sent_topics_sorteddf_mallet = pd.concat([sent_topics_sorteddf_mallet, 
                                             grp.sort_values(['Perc_Contribution'], ascending=[0]).head(1)], 
                                            axis=0)

# Reset Index    
sent_topics_sorteddf_mallet.reset_index(drop=True, inplace=True)

# Format
sent_topics_sorteddf_mallet.columns = ['Topic_Num', "Topic_Perc_Contrib", "Keywords", "Text"]

# Show
sent_topics_sorteddf_mallet.tail()

# Number of Documents for Each Topic
topic_counts = df_topic_sents_keywords['Dominant_Topic'].value_counts()
topic_counts

# Percentage of Documents for Each Topic
topic_contribution = round(topic_counts/topic_counts.sum(), 4)
topic_contribution

# Topic Number and Keywords
topic_num_keywords = sent_topics_sorteddf_mallet[['Topic_Num', 'Keywords']]
topic_num_keywords

# Concatenate Column wise
df_dominant_topics = pd.concat([topic_num_keywords, topic_counts, topic_contribution], axis=1)

# Change Column names
df_dominant_topics.columns = ['Dominant_Topic', 'Topic_Keywords', 'Num_Documents', 'Perc_Documents']

# Show
df_dominant_topics
# gensim.models.wrappers.ldamallet.malletmodel2ldamodel(ldamallet)
lda1 = gensim.models.wrappers.ldamallet.malletmodel2ldamodel(optimal_model, gamma_threshold=0.001, iterations=50)



all_top_vecs = [optimal_model.get_document_topics(corpus[n], minimum_probability=0) \
                    for n in range(len(corpus))]


def find_most_similar(sim_vec, all_top_vecs, title_lst, vec_in_corp='Y', n_results=7):                
    '''
    Calculates cosine similarity across the entire corpus and returns 
    the n_results number of most similar documents
    '''
    
    cos_sims = [gensim.matutils.cossim(sim_vec, vec) for vec in all_top_vecs]
    
    if vec_in_corp == 'N':
        most_similar_ind = np.argsort(cos_sims)[::-1][:n_results]
    if vec_in_corp == 'Y':
        most_similar_ind = np.argsort(cos_sims)[::-1][:n_results+1][1:]
        #exclude 'self', in the case that it is a book in the corpus
    
    for ind in most_similar_ind:
        print (title_lst[ind], cos_sims[ind])


