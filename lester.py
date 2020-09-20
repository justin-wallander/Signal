dictionary = {
        "content": {
                "0": '''DeepSign: A Deep-Learning Architecture for Sign Language Recognition [Video Classification]
Jay Shah
Jay Shah
Follow
Mar 29,
                2019 · 6 min read
Paper Link
https: //rc.library.uta.edu/uta-ir/bitstream/handle/10106/27803/SHAH-THESIS-2018.pdf?sequence=1&isAllowed=y
Code (TensorFlow)
https: //github.com/jayshah19949596/ASL-Thesis2
Motivation
Deep Neural Networks methods achieve high accuracy; however, they need a lot of training data. Creating Sign Language data can be time-consuming and costly. 
The motivation is to achieve comparable results with limited training data using deep learning for sign language recognition. The pipeline can also be used for video classification.
DeepSign
DeepSign is a new deep-learning architecture which achieves comparable results with limited training data for Sign Language Recognition.
Problem Formulation
Given a query video say Q we want to find it’s corresponding sign S. Our final goal is to learn a function A: Q →S that maps any query video Q belonging to a domain X to its corresponding sign 
S. Query video Q is a sequence of frames = (q_1,q_2,…,q_t) . Simplifying the learning function to A:(q_1, q_2, …, q_t)→S. Many-to-one-problem because we want to map sequences of input to a single output. 
Input is sequences of frames and output is one sign.
Breaking the Problem
We want a Model-1 to learn a function E: Q → F that maps input sequences (𝑞_1,𝑞_2,…,𝑞_𝑡) to feature sequences (𝑓_1,𝑓_2,…,𝑓_𝑡).
We want a Model-2 to learn a function M: F → S maps feature sequences (𝑓_1,𝑓_2,…,𝑓_𝑡) to its sign S. By combining Model-1 and Model-2 together we wish to learn the goal function A: Q → S. Model-2 is solving Many-to-one-problem.
Model-1 Overview
Model-1 is only for feature extraction. You can see the Model-1 figure below:
Image for post
Model-1 Overview
Model-2 Overview
Model-2 is for actual predictions. The output from the encoder of Model-1 is given as input to Model-2. You can see the Model-2 figure below:
Image for post
Model-2 Overview
Dataset Used
We will use LSA64 dataset. Originally the dataset includes 3200 videos.
10 non-expert subjects were asked to execute 5 repetitions of 64 different types of signs. These 64 chosen were the signs which are commonly used in LSA lexicon which includes nouns and verbs. 
It consists of 42 one-handed signs and 22 two-handed signs. Used first 14 one-handed signs for recognition.
Image for post
Sample Images from LSA64
The first 14 signs used consists of 700 videos in total. Each sign has 50 videos.
From every sign,
                20 videos were used for testing and 30 videos were used for training. In total out of 700 videos,
                280 videos used for testing and 430 videos used for training. No extra information about gloves was used in the pipeline. The pipeline can be used for any sign language data.
Pipeline Step-1: Pre-processing
In the pre-processing step, SSD model is used which is pre-trained on COCO dataset to detect a person in an individual frame.
Image for post
Left side is the original frame. SSD model output on the right side
Background subtraction is applied to each frame to capture the motion information and pixels within the bounding box provided by the SSD model is extracted. We find the edges in the frame and combine 
the background subtraction frame with the edge frame. We finally normalize the pixel values to be either 0 or 1.
Image for post
Final output frames of Pre-processing step
Pipeline Step-2: Training Encoder-Decoder
Stage-1 training uses Model-1 for training to learn the function E: Q  F. Model-1 is an Encoder-Decoder Architecture. The Encoder learns the hidden representation from the frame and Decoder tries to 
regenerate the frame from the hidden representation. This Stage-1 Training Architecture helps in three things: alk through the problem out loud with your interviewer.
It helps in dimensionality reduction.
Captures the spatial information by learning the hidden representation of the frames.
Reduces the chances of overfitting when the training data is less.
The Encoder-Decoder Architecture forces the encoder network to learn the important features in the frames and hence, this makes this architecture best suited for a problem where you have less number of training data.
10 Layer Encoder Network
Encoder Network’s architecture is based on Inception Architecture
Image for post
Encoder Network Table
15 Layer Decoder Network
Decoder takes the hidden representation as input and up-samples them to the original input. Because the input images are used as the target and hence our Stage-1 Training is an unsupervised learning problem.
Usually, up-sampling is produced by Deconvolution operations. However, these Deconvolution operations produce Checkboard Artifacts. Hence, resize using nearest-neighbor interpolation for up-sampling to the input and then do a convolution layer.
Image for post
Decoder Network Table
Encoder-Decoder Architecture Together
Image for post
Encoder — Decoder Architecture
Pipeline Step-2: Training LSTM Architecture
Stage-2 training uses Model-2 for training to learn the function M: F → S. Model-2 is an LSTM architecture. In second stage experimentation is performed with Uni-directional LSTM and with Bidirectional LSTM.
 LSTM Architecture will help in learning temporal information in the videos which will help in making accurate predictions. LSTM Network uses LSTM cells which allows them to learn long range temporal relationships between the sequences.
LSTM Cell
Image for post
LSTM Cell
Given sequences of input x=(x_1,x_2…,x_t ) a LSTM network computes hidden state sequence h=(h_1,h_2…h_t ) and output sequence y=(y_1,y_2…,y_t ). The hidden state of a LSTM cell is calculated as follows:
i_t=σ(W_xi x_t+W_hi h_t+b_i )
2. f_t=σ(W_xf x_t+W_hf h_(t-1)+b_f )
3. c_t=f_t c_(t-1)+i_t tanh(W_xc x_t+b_c )
4. o_t=σ(W_xo x_t+W_ho h_(t-1)+b_o )
5. h_t=o_t tanh(c_t )
where i_t = input gate, f_t = forget gate, o_t = output gate, c_t = cell state, and σ = sigmoidal activation function. Input gate tells whether to update the current state using the previous state. 
Forget gate decides whether to forget the previous hidden state or not. Cell state keeps only the necessary information and forgets the unnecessary one. Output gate filters the emission of the cell state.
Unidirectional LSTM
Encoder outputs are processed forward through time and upwards through two layers of stacked LSTMs. A SoftMax layer predicts the class at each time step. The weights are shared across time.
Image for post
Unidirectional LSTM Architecture. Encoder outputs are processed forward through time and upwards through two layers of stacked LSTMs. A SoftMax layer predicts the class at each time step. The parameters of the 
Encoder network and SoftMax classifier are shared across time steps.
Bi-directional LSTM
Encoder outputs are processed forward through time and upwards through two bi-directional layers of stacked LSTMs. A SoftMax layer predicts the class at each time step. The Bi-directional LSTMs has the advantage 
over Uni-directional LSTMs of providing extra information about the future at every time step.
Image for post
Bidirectional LSTM Architecture. Encoder outputs are processed forward through time and upwards through two bidirectional layers of stacked LSTMs. A SoftMax layer predicts the class at each time step. 
The parameters of the Encoder network and SoftMax classifier are shared across time steps.
Code (TensorFlow)
https: //github.com/jayshah19949596/ASL-Thesis2''',  

"1": '''Boost your CNN image classifier performance with progressive resizing in Keras
Aleksey Bilogur
Aleksey Bilogur
Follow
Apr 1,
                2019 · 8 min read



If you’re building an image classifier these days, you’re probably using a convolutional neural network to do it. CNNs are a type of neural network which build progressively higher level features out of groups of pixels 
commonly found in the images. How an image scores on these features is then weighted to generate a final classification result. CNNs are the best image classifier algorithm we know of, and they work particularly well when
given lots and lots of data to work with.
Progressive resizing is a technique for building CNNs that can be very helpful during the training and optimization phases of a machine learning project. The technique appears most prominently in Jeremy Howard’s work,
 and he uses it to good effect throughout his terrific fast.ai course, “Deep Learning for Coders”.
In this article I’ll demonstrate how you can use progressive resizing to build an image classifier using Keras. Specifically, we’ll using progressive resizing to build a CNN that learns to distinguish between 12 different 
kinds of fruits in what I call the Open Fruits dataset — an image corpus I built based on the Google Open Images dataset (to learn more about Google Open Images, read “How to classify photos in 600 classes using nine million open images”).
You can follow along with the code and learn how to download the data on GitHub.
This post assumes familiarity with CNNs. If you’re unfamiliar, Brandon Rohrer’s “How convolutional neural networks work” is excellent background reading.
Checking out the data
Recall that our dataset consists of images of 12 different kinds of fruits taken from Google Open Images, which is in turn based on permissively-licensed images from Flickr. To get a taste, here’s 25 random images 
from the dataset:
Image for post
Right away we see that this dataset is very problematic. It includes tiny images; occluded images that only depict parts of the sample; samples depicting groups of objects instead of individual ones; and bounding 
boxes that are just plain noisy and may not even be constrained to a single type of fruit. In a few of the cases it’s difficult even for a human to distinguish what the target class is.
To add to the difficulty, the dataset is highly imbalanced, with some image classes appearing far more often than others:
Image for post
Between the low image and label quality and the class sparsity this classification problem is a very, very difficult one.
Start small to iterate quickly
Now that we understand the contents of our dataset, we need to make choices about the network we will train.
One trouble is that a single neural network can only work with standardly-sized images; too-small images must be scaled up and too-large images must be scaled down. But what image size should be pick?
If your goal is model accuracy, larger is obviously better. But there is a lot of advantage to starting small.
To understand why, we must first understand that the most important features of an image classification problem are “large”. Properly tuned gradient descent naturally favors robust, well-supported features in its decision-making. 
In the image classification case this translates into features occupying as many pixels in as many of the sample images as possible.
For example, suppose we teach a neural network to distinguish between oranges and apples. Suppose that one model classifies by distinguishing between “orange” and “red”, and another classifies by distinguishing 
between “stem shaped like an orange stem” and “stem shaped like an apple stem”. The first model is robust: any image we score, no matter how small or misshaped, will have orange pixels and red pixels usable by the model. 
The second model is not: we can image images so small that the stems are not easily distinguishable, or images with the stem cropped out, or images where the stems have been removed outright.
The practical result is that while a model trained on very small images will learn fewer features than one trained on very large images, the ones that it does learn will be the most important ones. 
Thus a model architecture that works on small images will generalize to larger ones.
Meanwhile, small-image models are much faster to train. After all an image input size twice as large has four times as many pixels to learn on!
Since small-image models generalize well to larger input sizes, and since they take less time to train, and since the first batch of models we build are going to be highly experimental anyway, why don’t we save
 time and just train our first few models on small data, and worry about scaling up the images and the models later?
In fact, that is exactly what progressive resizing is!
We now understand the main idea behind progressive resizing. Let’s see how it works in practice.
Our first tiny model
We start out by building our first small-scale model.
Here is a smoothed kernel-density plot of image sizes in our “Open Fruits” dataset:
Image for post
We see here that the images peak at around 128x128 in size. So for our initial input size we will choose 1/3 of that: 48x48.
Now it’s time to experiment! What kind of model you end up building in this phase of the project is entirely up to you. Here’s what I did (with comments in the code):

This model achieved ~53% validation accuracy:
Image for post
Not stellar, but remember, this is a very simple model trained on very small very noisy images, with a lot of classes to choose from. We could do better by working on this model further, but I only had so much time to iterate on this model.
Applying progressive resizing
We now apply progressive resizing to the problem.
We started by building a classifier that performs well on tiny n x n (48 x 48) images. The next step is scaling our model up to 2n x 2n (96 x 96) images.
We do this using transfer learning. Transfer learning is the technique of re-using layers and weights from previous models when building new ones (“Deep Learning For Beginners Using Transfer Learning In Keras” provides a good overview). In our case, this will mean taking the model we just built, freezing it (so that further training won’t make any changes to our existing weights), and injecting its layers into a new model (one which takes upscaled 96 x 96 images as input).
The work we do at this stage is limited to finding a configuration of good “feeder layers” we can prefix our old model with. These new layers can focus on finding the additional features findable in 96 x 96 pixels that weren’t in 48 x 48 pixels.
First I saved the 48 x 48 model to disk as model-48.h5. Then I created the following new model:

This script:
Downloads and instantiates our old 48 x 48 model.
Instantiates a new model with two new 96 x 96 convolutional layers.
Appends a max pooling layer, which downsamples 96 x 96 → 48 x 48—the expected input size for our old model.
Removes the first convolutional layer from our old model (by the way, this helps reduce overfit!).
Reattaches the rest of the layers of our old model onto the new one.
Freezes the old convolutional and fully-connected layer weights in place.
Basically, we’ve created a new model that trains on 96x96 pixel images which reuses our old 48 x 48 classifier internally!
This new model improves performance from ~53% to ~59%:
Image for post
We can apply progressive resizing one more time, this time moving from 96x96 to 192x192. The procedure required is the same, differing only in scale:

This new model sees data that is fully sixteen times as large as our original tiny 48x48 model. This translates into further model improvement, but this time that benefit is more modest — up from 59% to 61%:
Image for post
To summarize what we’ve done:
We started with a model that trained on tiny 48x48 pixel images, which is 53% accurate.
Next we trained a model on 96x96 pixel images, reusing our 48x48 classifier within our model and achieving 59% accuracy.
Finally, we trained a model on 192x192 pixel images, reusing our 96x96 classifier (which in turn reused our 48x48 classifier!) and achieving 61% accuracy.
Note that, in the interest of time, I did not spend much time experimenting with the new layers I added in steps 2 and 3. To improve performance further, here are some other things you could try:
Increasing or decreasing the number of new convolutional layers you add.
Increasing or decreasing the number of nodes in each new convolutional layer.
Tuning hyper-parameters like activation functions and learning rates.
Experimenting with the image preprocessing you apply.
Unfreezing the fully-connected layer and adjusting/training that as well.
Unfreezing one or more preexisting convolutional layers and (re-)training those as well.
Conclusion
We started this article off by discussing the fact that convolutional neural networks trained on small images are both fast and easy to train and readily generalizable to larger image inputs. This makes them good models to build during the early experimental phase of a project, when you’re still just trying to get to grips with a basic network architecture that works well. We can concentrate on dashing off quick one-off models now, and on scaling them up and fine-tuning performance later. Finally, we heard that models trained this way can often achieve equal or better performance than models trained from scratch.
Consider the alternative: building and tuning a full-sized 196 x 196 model from the start. This model would have an unrestricted “model finding space”: it could theoretically converge on any combination of layer weights that works best for the given problem. Progressive resizing is much more restrictive: it require that a model that works well on 2n x 2n images must subsume a model that works well on n x n.
This could in theory mean that we “miss” an even better architecture that a model built from scratch could converge on. But in practice, models built using progressive resizing principles often actually do better than models built from scratch.
The theoretical reason why is a mystery. One compelling theory, courtesy of Miguel Perez Michaus, is that it improves the ability of the model to learn “scale-dependent” patterns. He writes about this in the excellent blog post “Yes, Convolutional Neural Nets do care about Scale”; I recommend reading it if you want to learn more.
Nevertheless, progressive resizing is an interesting technique and a useful approach to image modeling problems And hopefully now that you have read this article, another useful tool in your deep learning toolbox''',

"2":'''5 Professional Projects Every Data Scientist Should Know
Customer segmentation, text classification, sentiment, time series, and recommender systems.
Matt Przybyla
Matt Przybyla
Follow
Aug 27 · 6 min read



Image for post
Photo by freestocks on Unsplash [
                        1
                ].
Table of Contents
Introduction
Customer Segmentation
Text Classification
Sentiment Analysis
Time Series Forecasting
Recommendation Systems
Summary
References
Introduction
The goal of this article is to outline projects that a professional Data Scientist will eventually perform or should perform. I have taken a lot of bootcamps and educational courses in Data Science. While they have all been useful in some way, I find that some forget to highlight real-world applications of Data Science. It is beneficial to know what to expect as you transition from educational to professional Data Scientist. Customer segmentation, text classification, sentiment analysis, time series forecasting, and recommender systems can all help your company that you are employed at tremendously. I will perform a deep dive and explain why these specific five projects come to mind, and we will hopefully motivate you to employ these where you work.
Customer Segmentation
Customer segmentation is a form of Data Science where an unsupervised and clustering modeling technique is employed to develop groups or segments of a human population or observations in data. The goal is to create groups that are separate, but the groups themselves have closely related features. The technical term for this separation and togetherness is called:
Between-groups sum of squares (BGSS)
how different the unique groups are from one another
Within-group sum of squares (WGSS)
how closely related the unique group features are
Image for post
K-means clustering. Image by Author [
                        2
                ].
As you can see in the image above, these groups are well separated — BGSS and are closely centered — WGSS. This example is ideal. Think of each of the clusters as those groups that you will target with a specific marketing advertisement: ‘we want to appeal to recent college graduates by marketing our company product as young-professional centered’. Some useful clustering algorithms are:
DBSCAN
K-means
Agglomerative Hierarchical Clustering
What happens with customer segmentation results?
— finding insights about specific groups
— marketing towards specific groups
— defining groups in the first place
— tracking metrics about certain groups
This type of Data Science project is broadly used, but most useful in the marketing industry.
Text Classification
Image for post
Feature and target of text classification example. Code by Author [
                        3
                ].
Text classification is under the umbrella of Natural Language Processing (NLP), which utilizes techniques to ingest text data. You can think of this algorithm or project as a way to categorize text labels by using text features (along with numeric features as well).
Here [
                        4
                ] is a simple example of utilizing both text and numeric features for text classification. Instead of having one word for your text feature, you could, perhaps, have hundreds and will need to perform NLP techniques, like Part-of-Speech tagging, stop word removal, tf-idf, count vectorizing, etc. A common library Data Scientists use in Python is nltk. The goal of these techniques is to clean your text data, and create the best representation of itself, so as to eliminate noise.
mprzybyla123/nlp-example
Permalink Dismiss GitHub is home to over 50 million developers working together to host and review code, manage…
github.com
What happens with text classification results?
— automatic categorization of observations
— scores associated with each category suggested
You can also categorize text documents that would otherwise take hours upon hours to manually read.
This type of project is useful in the finance or historian/librarian industry.
Sentiment Analysis
Sentiment analysis is also under the umbrella of NLP. It is a way to assign sentiment scores from the text, or more specifically, polarity and subjectivity. It is beneficial to use sentiment analysis when you have plenty of text data and want to digest it to create levels of good or bad sentiment. If you have a rating system already in place at your company, it may seem redundant, but oftentimes people can leave reviews with text that do not match their numerical score. Another benefit of sentiment analysis is that you can flag certain keywords or phrases that you would want to highlight in order to make your product better. Aligning keywords with key sentiment can be used to aggregate metrics that you can visualize what your product is lacking and where possible improvements could be made.
What happens with sentiment analysis results?
— product improvements
— sentiment flagging to for customer service
This type of project is useful in plenty of industries, especially e-commerce, entertainment, or anywhere that includes text reviews.
Time Series Forecasting
Image for post
Photo by Sonja Langford on Unsplash [].
Time series can be applied to several parts of various industries sectors. Most times, time series forecasting can be used ultimately to allocate funds or resources for the future. If you have a sales team, they would benefit from your forecast, as well as investors, as they see where your company is going (hopefully increasing in sales). More directly, if you have certain employees assigned with the forecasted target for that day, you can allocate employees in general, and to certain places. A popular example would be Amazon or any similar company where consumers have frequent behaviors and need an allocation of factories, drivers, and different locations that will merge together.
What happens with time series forecasting results?
— allocation of resources
— awareness of future sales
Some popular algorithms that utilize time series are ARIMA and LSTM.
This type of project is useful in plenty of industries as well, but usually in sales or supply management.
Recommender Systems
Image for post
Photo by Simon Bak on Unsplash [
                        6
                ].
While you may or may not be designing Netflix’s next recommendation system algorithm, you may find yourself applying similar techniques to several parts of your business. Think of using this type of project to ultimately achieve the sales of more products from users. As a consumer, if you are buying certain products or groceries, but you see some recommended ones at the end of your cart checkout, you may be inclined to quickly buy one of those recommendations. Expand this result to every user and you can make your companies millions.
Here are some common ways to approach recommendation systems in Data Science.
Collaborative-filtering — alternating least square (matrix factorization)
how similar other people are to you and recommends what they like to you
Content-based filtering — cosine similarity
how attributes or features about the product you already bought can recommend a similar product in the future
This type of project is useful in plenty of industries as well, but usually in e-commerce and entertainment.
Summary
I hope I gave you some inspiration from highlighting these key projects that you may often use already, or will use as a professional Data Scientist. The focus on Machine Learning in education is to focus on obtaining the best accuracy sometimes, but the focus of Data Science in the professional sense is to help your company to improve its product, help people, and save or make more money.
To summarize, here are five popular professional projects to practice:
customer segmentation
text classification
sentiment analysis 
time series forecasting
recommender systems
I hope you enjoyed my article. Thank you for reading! Please feel free to comment down below and suggest other professional Data Science projects you have encountered so that we can all improve our professional Data Science portfolios.
References
[
                        1
                ] Photo by freestocks on Unsplash, (2018)
[
                        2
                ] M.Przybyla, k-means visualization, (2020)
[
                        3
                ] M.Przybyla, nlp-example.ipynb, (2020)
[
                        4
                ] M.Przybyla, nlp-example, (2020)
[
                        5
                ] Photo by Sonja Langford on Unsplash, (2014)
[
                        6
                ] Photo by Simon Bak on Unsplash, (2020)''',

"3": '''Analytics is not storytelling…
On the nature of analytics, part 1 of 2
Cassie Kozyrkov
Cassie Kozyrkov
Follow
Oct 31,
                2019 · 11 min read



Image for post
From the TV show “How I Met Your Mother”
What happens in a typical analytics 101 class? You usually learn the basics of some analytics software (in R-Python-SQL-SAS-Stata-MATLAB-BigQuery-Tableau-Excel-Looker-whatever), how to load data into that software, and how to make visual summaries like the pie chart and bar graph above.
Image for post
If you forgot how to read a bar chart or a histogram, just think of the versions you find in nature. Same thing!
But that’s as much analytics as art is paintbrushes. Art will survive past paint and analytics will outlast spreadsheets. To see the nature of analytics without its typical window-dressing while celebrating today’s festivities, here’s a Halloween-flavored post for your amusement…
Disclaimer: For those of you trick-or-treating in your internet troll regalia this year, please note that some nuances are intentionally omitted because they’re coming in Part 2 or I’ve discussed them in my other articles. [
                        1
                ][
                        2
                ][
                        3
                ][
                        4
                ][
                        5
                ][
                        6
                ][
                        7
                ][
                        8
                ][
                        9
                ][
                        10
                ][
                        11
                ][
                        12
                ]
Domain expertise is important
Imagine that you’ve never celebrated Halloween before (gasp!), but you’ve just been talked into attending a party tonight. You’re the decision-maker in charge of the costume decision and I’ll be your analyst. You’re in good hands, because as an avid Halloweener, I’m oozing relevant domain knowledge.
Image for post
A tricky Priority One Bug caught and fixed at Google. (Why, what do you wear to the office?)
Domain expertise is extremely important for analysts — if I didn’t have it, I’d better scramble to get it. Analysts who’ve never even heard of Halloween will be severely hampered in their ability to help you pick a costume. They’ll probably snooze past all kinds of useful data because they won’t know what they’re looking at. It’s a bad sign to see an analyst entering a new domain without immediately asking, “Where can I find a domain guru to talk to?”
Analysts can tell stories, but they’re not storytellers
Contrary to popular belief, an analyst’s function is not to “tell stories” or to persuade with data. That’s called marketing. (Or perhaps journalism.)
There comes a time in every adult’s life where we have to market our work so that our stakeholders value us and do what we want them to, but let’s call that dark art what it is and talk about it in a different article. Sure, good analysts know a lot about human attention and can manipulate their audience, but that’s a by-product of one career that opens doors to another. Being able to tell stories is a skill analysts need to have, but their job is something else.
Analytics is not marketing. The difference is that one is about expanding the decision-maker’s perspective while the other is about narrowing it.
To put it in Halloween terms, my job as analyst is not to convince you to don a cockroach suit like the one I ran around in last year. I enjoy Halloween even more than April Fools Day and my birthday combined, so when it comes to costumes, I naturally have all kinds of opinions.
Image for post
It’s okay if you don’t get it. Measure theory isn’t for everyone.
I favor the nerdy. The more conceptual and the more obscure my outfit, the better. I only need one guffaw per year from a fellow weirdo to make the whole endeavor worthwhile. This year I’m recreating the original R.U.R. outfit, while previous years included a FORTRAN punchcard that prints “Happy Halloween” and a sigma field with a Lebesgue measure on it.
However, this project is about your tastes, not mine. My role as an analyst isn’t to manipulate you towards the conclusions I’ve already made. My opinion here isn’t the point… unless you prefer for me to just pick a costume for you. Then you can delegate decision-making to me, transforming me from analyst to decision-maker. (In that case, let’s get you suited up as a multi-armed bandit. All we need are a few pairs of long gloves, cotton wool, a toy pistol, a bandana…)
An analyst serves as your eyes
As an analyst, I’m not supposed to sell you anything. I’m here to be your eyes and get you as much inspiration per minute as possible. The reason you need an analyst in the first place is that you don’t have the time to go poking around in data, but you still want to be the one to call the shots. In this scenario, I may have more domain expertise than you… but that doesn’t necessarily mean you’ll consent to my picking your costume for you. You hired me to open your eyes, not to decide on your behalf. You don’t want to give up your power to choose and it’s my duty to respect that. That is what separates analytics from decision-making and marketing.
If a decision-maker doesn’t want to give up their power to choose, it’s an analyst’s duty to respect that. Even if the analyst knows the domain better than the decision-maker.
If I took the marketing or storytelling approach, I’d be blinkering you and impoverishing your view of the possibility space. A good analyst does the opposite, exposing you quickly to a rich variety of perspectives. Ideally, I’ll help you absorb all the information you’d look for if you were the one taking the time to roam around in the data… plus useful things you didn’t even know you should ask to see.
Tools are a means to an end
There’s Halloween information out there and it’s the analyst’s job to find it, examine it, and filter it for you, then make it easy for you to absorb as much of the most promising stuff as quickly as possible.
Whether I use R, SQL, C++, a librarian, or a search engine to surface information, it’s all analytics. If your idea of data is limited to spreadsheets and databases, you’re not thinking broadly enough. You can find my musings on the nature of data and its relationship with the maxim that “knowledge is power” here.
Try not to waste the decision-maker’s time
An expert analyst is serious about the virtue of speed. That goes beyond having quick fingers in looking things up. I should strive not to waste your time. I have an infinity of options on how to slice and surface information for you, but your party is tonight. I’d be a daft analyst if I started bombarding you with “inspiring” elaborate handmade costumes you need to order several months in advance.
Image for post
Creepy costume I saw last weekend in NYC, complete with mechanical baby arms. Probably not something you could cobble together in a day.
Before we get any further, I need to understand your relationship with the time-space continuum so I have a sense of which costume stores you can physically get to and what shipping options to eliminate. I should also ask about budget. I’d be wasting your time if I gave you too much information on outfits that cost an arm and a leg if your budget is a toenail.
Image for post
Maybe your budget is literally some toenails? Who am I to judge?
I might still show you one or two expensive options just in case these are the kinds of unknown unknowns that might inspire you to reconsider your budget.
Speed-to-inspiration is the name of the game.
The more I know about the data and your tastes, the better I can help you absorb and understand what’s possible so you can get inspired quickly.
As an analyst, I’m not here to funnel you towards my opinion. I’m here to help you form your own.
Knowing the nature of your event will help me skew my investigations towards what’s most likely to be helpful. An indoor dance party is not a great place for spiky gear that can gouge out someone’s eye, while an outdoor parade through the arctic wastes limits your choices towards the warm and bulky. If you’re heading to a work party, I’d probably avoid showing you costumes like Sexy Bayesian Posterior (complete with a bunch of heavy metallic Markov chains)… despite having seen precisely this at a statistics gathering. We statisticians are an interesting bunch.
Image for post
Cool indeed, but maybe not the best choice for a dance party.
If you didn’t give me much information, I’m on my own. I could produce a list of the three closest costume stores to your coordinates, plus their business hours. I could give you an indication of their relative prices using an index of a few items that all of them stock. I could tell you that a typical US Halloween store has everything you need to put together a full costume, except the shoes.
I could survey my friends and produce a pie chart by costume color (so you know what you’d have to pick to blend in or stand out at a gathering with my friends… which might be completely irrelevant to the event you’re actually headed to if your friends aren’t like mine).
I could try to find information on how expensive Halloweening is and how long it takes to make your own costume versus buy one. Maybe I’d make better versions of this survey’s charts (based on 1000 mysterious Americans who may or may not be expert costume makers — be careful with data whose origins you know nothing about):
Image for post
I’m not going to give a critique of these charts. Nope. Won’t even grumble about the color and legend serving no purpose.
Image for post
I could inspire you with a list of categories (and exemplars): classic monsters (vampire), animals (tiger), professions (astronaut), people (Joan of Arc), cartoon characters (Bender), concepts (sigma field), artwork (Munch’s Scream), food (carrot), objects (punchcard), etc.
I could look up the most popular keywords accompanying Halloween on Google Trends to see what the dominant categories are — some kind souls have already done this for us, producing the list below:
Image for post
Harry Potter is *still* a top 10 costume? What year is it?
Fortnite
Spider-Man
Harley Quinn
Wonder Woman
Black Panther
Deadpool
Harry Potter
Catwoman
Pennywise
Kim Kardashian
Pop culture is king, apparently. No king of mine, though.
I could go a step further and produce a list like this for your area, plotting the relative popularities for both areas… but time is limited and this is probably not what you care about. It’s only worth doing if fine-grained popularity information is likely to help you somehow. In broad strokes, though, the list above is probably enough for a Halloween newbie to form the impression that a lot of people search for pop culture costumes. I seriously doubt you’ll have additional epiphanies pursuing that line of inquiry to exhaustion, so I won’t go there either.
I’ve seen newbie analysts panic at this point. They’re poking around in the data and not finding anything that looks like an obvious gem. Oh dear! Maybe no one will notice if you start plotting the data every which way as beautifully as possible, maybe with animations too? Take a deep breath, then move along. Don’t polish a piece of rubbish. It’s a waste of —
Exactly.
Getting back to the task at hand, I could try to look for obscure costumes and compile a list of those for inspiration.
Image for post
For even more weird, you could look to AI-generated costume suggestions, such as these (courtesy of aiweirdness.com):
Image for post
If I thought you were aiming to pay as little as possible, I could look up the cheapest ready-made costumes. Poking around online retailers tells me you can get a cloak and a mask for under $10, so maybe these same items would be good bets to take a look at in your brick-and-mortar store. You could also find beaten up clothes at a vintage store plus cheap eye shadow and red lipstick for a zombie DIY operation.
I might also want to warn you if your country isn’t one of the top celebrating nations — unless you’re celebrating in one the orange zones, you might attract strange looks on your way to the party. I wear my weird proudly, but others might like to consider a coat.
Image for post
Source: Twitter. Since this is someone else’s data, we’re too smart to trust it. Good! Decision-makers, treat it as inspiration only. Want something better? Then you’ll have to invest your team’s time and effort. Analysts, make sure the decision-maker considers time spent polishing something like this a good investment before rushing off to do it. If the decision-maker hasn’t asked for better quality, don’t polish anything unless you’ve truly got nothing better you could spend your work hours on.
I could start veering off track (this year’s Halloween) towards miscellaneous flashes of curiosity, such as “When do people start searching for Halloween costume information online?” Not very useful for your costume this year, but I visualized it anywa — look, a squirrel!
Image for post
Some inspiration about when to start planning your costume next year if you want to be like the Joneses.
Image for post
Hopefully you’re beginning to see that domain expertise is important, but without knowing my decision-maker’s business, it’s hard to guess what kind of information to surface. I’ll end up spending a lot of time running about in all kinds of different directions, trying to guess what you’d like to know.
When you take analytics courses, a key component — the relationship with the decision-maker — is usually missing. It’s easier to teach data journalism, so that might be what you learned. That’s also where the storytelling emphasis comes in. The best examples of data journalism *are* storytelling and by their nature, online examples are made for the masses, so it’s easy to get a skewed impression of the real work.
Data journalism is not about helping specific individuals make decisions. It’s about presenting information with mass appeal. In fact, it’s the opposite of what an analyst brings to a project.
Data journalism is not about helping specific individuals get the data they need. It’s about presenting information with mass appeal. In fact, it’s the opposite of the tailor-made helpfulness that an analyst can bring to a project. Don’t get me wrong, there’s something beautiful about a successful one-size-fits-all story, the kind that goes viral and enlightens many people a little bit. But unless it’s completely earth-shattering news, it’ll only change your decision-maker’s life a little bit. It’s a consolation prize compared with what a skilled analyst can provide: inspiration that enables a quantum leap for your leader and your business.
It’s tricky to drive inspiration when you know nothing about the decision-maker or what their challenges and priorities are. You end up trying to engage in one-size-fits-all journalism, compensating with pretty plots and storytelling. This doesn’t fix the underlying problem. Analytics has more opportunity to add value when it’s iterative, a conversation between analyst and decision-maker. We’ll look at the iterative analytics workflow in Part 2.''',


"4":'''9 Skills You Can Get from Extraordinary Learners
Learn the extra skills you need to thrive in life from these 5 people.
Tim Denning
Tim Denning
Follow
Jul 30 · 5 min read



Image for post
Photo by Luke Jones on Unsplash
People who think they know everything rarely succeed in life. The life of a know-it-all tends to be a couch potato.
That’s why you want to become obsessed with learning. Learning is everything. To learn is a gift.
Remember what it was like to go to school for the first time. Learning was fun. There were sandpits, books about made-up worlds, and other kids to experiment with. Then university came along and made learning ugly. Learning became for many of us, a means for survival and a future strategy to put food on the table. Then life knocks you in the face.
You do a few job interviews and realize that unless you’re a doctor or a lawyer, nobody asks you about what university you went to or what grades you got. Who gives a shit.
Falling in love with learning all over again will improve your life.
These are a few extraordinary learners you can study:
Tim Ferriss — podcaster, author
Benjamin Hardy — blogger/writer
Danny Forrest — Founder, SkillUp Academy
Derek Sivers — Entrepreneurial worker bee in residence
Oprah — (you know the one)
Each of them has mastered the art of learning. They stack skills on top of each other to produce bizarre results.
Scott Adams, founder of the cartoon Dilbert, talks about skill stacking a lot. The idea is you can take two completely unrelated skills you’ve learned and produce unlikely results. That’s what Scott did when he fused drawing, writing and comedy together.
Here’s what extraordinary learners do from my study of them over the last six years.
1. Learners see skills as a way to make art.
How you see learning is crucial. Think of learning as a game. When you play the game of acquiring skills you can use them to make art. You don’t want to paint or draw or write. Okay that’s cool. Running is art. Podcasting is art.
Anything done well and with passion is art.
I have fused the skills of writing, imagery, social media and business. You can do the same. It’s straightforward.
Take 2–3 skills and stack them together = ART.
2. Learners write for clarity.
Writing reinforces an idea. It helps you put an idea into your own words.
When you take an idea and put it into your own words, you create clarity in your mind. There are many key lessons to be learned with any skill and practicing the habit of writing about them will fast-track your success rate.
If you really want to get crystal clear thoughts you can touch, have a warm shower. Your mind will be relaxed and your thoughts will be so clear you’ll want to write them down.
Use liquid chalk and write your thoughts on the shower wall.
3. Learners read.
The best way to learn is through other people’s experiences. Blog posts are nice, but books are far more in-depth. Reading about someone’s life in a book takes the information and fuses it with stories.
Stories make the learning stick.
No one will be able to stop you in life if you make the crazy decision to read a book a week.
Each extraordinary learner I have studied for the last six years is obsessed with books. I’d go as far as saying they’d rather starve than give up reading books.
Books are a purchase they view as an investment, not an expense on their balance sheet of life.
4. Learners are stupidly consistent.
You won’t find them learning for one hour a year. Or writing their learning goal down on their new year’s’ resolutions list.
Learners consistently learn because they’ve made learning a habit.
The decision to learn has been automated by their consistency. When you’re consistent, you build a pattern. You apply that pattern to your process and away you go.
I learned the skill of writing by starting out publishing four full-length blog posts a week. I was a really shit writer to begin with but it didn’t matter. I learned to write by being consistent.
Whatever skill you want to develop, find a way to be consistent. Schedule skill acquisition, as a meeting with yourself in your calendar, if you have to.
5. Learners make time to think.
Learners are thinkers first and foremost. They weren’t born thinkers. They made time to think.
Sitting at home and looking out the window in complete silence is drastically underrated. Sitting still and thinking about a problem is powerful. Daydreaming is even more powerful.
Daydreaming is where you unlock your imagination and use it to serve you. Your imagination can come up with wild ideas that lead to the best learning of your life.
Dare to dream. Stop letting society kick the learning out of you by listening to the negativity and letting it block your imagination.
6. Learners make problems their WHY.
Having a reason to learn matters. Learns use problems as their why. A problem fascinates them and they choose to learn about it.
That decision to learn leads them down a rabbit hole. Finding a solution becomes a game. And when you gamify learning, it’s really enjoyable.
Gamified learning is addictive.
7. Learners create more than they consume.
Overconsumption kills a learner’s dreams.
The point of learning is to create and apply what you’ve learned. Excessive streaming and consumption of social media takes you away from the time you need to learn. Sure, enjoy a bit of TV, but do you really need to consume the whole series?
Roughly calculate how much time you spend each week consuming vs creating. Shift the percentage split slightly in the favor of creating and you’ll see huge changes in your life.
8. Learners do this: Practice.
Without practice, all learning becomes is mental foreplay.
The whole point is to practice what you’ve learned. You’ll probably stuff up a lot or look stupid in front of a group of online strangers. Who cares Bob.
Practice doesn’t make perfect. Practice leads to more learning. Practice is the fun part. It’s where you get to explore what you’ve learned. Practice leads to action and later that could lead you to change your entire career.
What you’ve learned and then practiced could become the work you do which helps you earn a living. You may even label it as work you love.
9. Learners never stop learning.
That’s what is extraordinary about Mr Ferriss, Ben, Danny, Derek, and Lady Op’s (Oprah). They never stop learning. Learning is a game that never ends.
They keep on learning and then spread the art of learning to others. They preach learning because learning is what defined everything they achieved.
Those who never stop learning have come to terms with one truth about life: we know nothing. You will never know much about anything and that’s the paradoxical brilliance of learning.
Final Thought
Become an extraordinary learner. Follow this process:
Learn
Question what you’ve learned
Unlearn some of what you’ve learned
When your focus is to learn, your goals in life are achieved 10X faster.''',


"5":'''13 Books That Changed My Life
Chris Rackliffe
Chris Rackliffe
Follow
Jul 18,
                2019 · 26 min read



Transform your life with these groundbreaking books.
Image for post
“I think you should read this book,” my therapist said.
When she makes a recommendation, my ears perk up in reverence. “It’s called Attached,” she continued. “Some of my other clients told me they’ve found it incredibly impactful and I think it has the potential to help you, too.”
Turns out that was an understatement.
The next day, the book arrived at my apartment. I sat reading for hours on end, devouring the material as I furiously underlined important takeaways, feverishly highlighted memorable quotes and fervently bookmarked pages. My mind was like a sponge soaking up as much information as it could take in. I had a-ha moment after a-ha moment. Page after page and example after example, I saw the imprint of my past written there in black and white.
I’ve never felt more seen in my life.
All the missteps and mistakes of my dating life finally made sense. My mind stepped in and healed my heart when it needed it most.
Stephen King once wrote that, “Books are a uniquely portable magic.” If that’s true, then I was most certainly spellbound by this book’s powerful revelations about my attachment style. I started telling some of my friends about the realizations the book had inspired.
I was experiencing what I call The Shift. The Shift occurs when something so revolutionary happens in your life that you have no choice but to reorganize your thoughts and reinterpret your experiences through this new lens. Your life becomes divided into before and after The Shift occurs. Try as you may, there’s no going back to the way things were before. You have experienced an earthquake of the mind — a massive and momentous transformation of perspective that completely shakes up and changes how you approach the world.
That’s the power of The Shift. That’s the power of the written word. That’s the power of a good book.
Books are the keys that open doors to new worlds full of unexplored possibilities. Books bend the limits of language and time, helping knowledge transcend generations and centuries, oceans and latitudes. Books mirror your past, present and potential back to you — and can instantly alter the course of your life.
And so it was with Attached. But it wasn’t the only book to play a major part in my life; so far, I’ve experienced The Shift on 13 different occasions.
One of the greatest things a book can do is help you realize your limitations — and evolve beyond them. For me, that’s what these 13 books represent: Stepping stones on the path to enlightened living — light bulbs that further illuminated my life and helped guide me through the darkness. These books completely converted my convictions and led me to a deeper awareness, understanding and appreciation for my life and all its ups and downs, twists and turns.
And I hope they’ll do the same for you, too.
1. A New Earth: Awakening to Your Life’s Purpose
Author: Eckhart Tolle
Five-word synopsis: Awaken yourself, awaken the world.
Why it changed my life:
Some people spend a lifetime in pursuit of their purpose. But that’s really not necessary. Just read this masterpiece by Eckhart Tolle and the purpose of your life will start to make sense. You are meant to do one thing with your life, and that is to awaken to the fire within which is the fuel of all life. This spiritual magnum opus will help you do that. At least I know it did for me.
A New Earth restored a sense of peace within me. It helped me heal my judgment. It provided a pathway for dealing with anxiety. It showed me that there was another way other than staying trapped in the cultural conditioning that told me I needed to have more and do more and achieve more.
I read this book at least once a year for those and so many other reasons. It’s packed to the brim with existential truth and the kind of perspective and wisdom that will cause The Shift within you and completely change your life and the way you look at it. Do yourself a favor and read A New Earth, stat.
My 16 favorite quotes:
“The fire of suffering becomes the light of consciousness.”
“Driven by greed, ignorant of their connectedness to the whole, humans persist in behavior that, if continued unchecked, can only result in their own destruction.”
“You do not become good by trying to be good, but by finding the goodness that is already within you, and allowing that goodness to emerge.”
“To recognize one’s own insanity is, of course, the arising of sanity, the beginning of healing and transcendence.”
“Ego is no more than this: Identification with form, which primarily means thought forms. If evil has any reality — and it has a relative, not an absolute, reality, this is also its definition: Complete identification with form — physical forms, thought forms, emotional forms. This results in a total unawareness of my connectedness with the whole, my intrinsic oneness with every ‘other’ as well as with the Source. This forgetfulness is original sin, suffering, delusion.”
“Thinking without awareness is the main dilemma of human existence.”
“Sometimes letting things go is an act of far greater power than defending or hanging on.”
“The moment you become aware of the ego in you, it is strictly speaking no longer the ego, but just an old, conditioned mind-pattern.”
“The past has no power to stop you from being present now. Only your grievance about the past can do that. And what is a grievance? The baggage of old thought and emotion.”
“Whatever you fight, you strengthen and what you resist, persists.”
“You are the Being behind the doing.”
“There are three words that convey the secret of the art of living, the secret of all success and happiness: One With Life. Being one with life is being one with Now. You then realize that you don’t live your life, but life lives you. Life is the dancer and you are the dance.”
“Emotion in itself is not unhappiness. Only emotion plus an unhappy story is unhappiness.”
“Abundance comes only to those who already have it.”
“What is my relationship with Life? This question is an excellent way of unmasking the ego in you and bringing you into the state of Presence.”
“Nonresistance, nonjudgment and nonattachment are the three aspects of true freedom and enlightened living”
2. A Return to Love: Reflections on the Principles of A Course in Miracles
Author: Marianne Williamson
Five-word synopsis: Love is your true nature.
Why it changed my life:
Tina Turner once asked, “What’s love got to do with it?” to which Marianne Williamson replied, “Absolutely everything.” This book is that reply.
A Return to Love cuts straight to the soul. When I was reading this book, it was almost like it was with my heart and not my mind. The truth in its pages resonated with me from the inside out, not the outside in. As you can see from my favorite quotes below, Williamson navigates complex spiritual concepts and communicates them with a simple clarity that’s nearly impossible to come by.
At its core, A Return to Love is the collective story of our wrong turn into fear, negativity and uncertainty and how to reorient us back to love, forgiveness and opportunity. This book is an indispensible guide for anyone who’s struggled to relinquish control, forgive others and find a deeper sense of purpose. Based on the enlightened teachings in A Course in Miracles, A Return to Love is like a compass back to your true love nature, helping guide you at every step as you open your heart and soften your shell — and put love first in everything you think and everything you do. My only regret is that I wish I’d read it sooner. Do yourself a favor and don’t make the same mistake as me.
My 16 favorite quotes:
“The change we’re really looking for is inside our heads.”
“And that’s what a miracle is: A Parting of the mists, a shift in perception, a return to love.”
“The only thing lacking in any situation is our own awareness of love.”
“As we relinquish the fears that block the love within us, we become God’s instruments. We become His miracle workers.”
“Every situation we find ourselves in is an opportunity, perfectly planned by the Holy Spirit, to teach love instead of fear.”
“God isn’t separate from us, because He’s the love inside our minds. Every problem, inside and out, is due to separation from love on someone’s part. Thirty-five thousand people a day die of hunger on earth, and there’s no dearth of food. The question is not, ‘What kind of God would let children starve?’ but rather, ‘What kind of people let children starve?’ A miracle worker returns the world to God by making a conscious change to a more loving way of life. Waiting with cynical resignation for the world’s collapse makes us part of the problem, not the answer. We must consciously recognize that, for God, ‘there is no order of difficulty in miracles.’ Love heals all wounds. No problem is too small for God’s attention, or too big for Him to handle.”
“Forgiveness is the key to inner peace because it is the mental technique by which our thoughts are transformed from fear to love… forgiveness is ‘selective remembering’ — a conscious decision to focus on love and let the rest go.”
“Everything that someone does… is either love or a call for love.”
“It is our failure to accept people exactly as they are that gives us pain in a relationship.”
“We don’t reach the light through endless analysis of the dark. We reach the light by choosing the light. Light means understanding. Through understanding, we are healed.”
“We are not held back by the love we didn’t receive in the past, but by the love we’re not extending in the present.”
“Purity of heart creates breakthroughs.”
“Knowing that we are acting on behalf of a higher purpose than our own self-aggrandizement gives us the joy we’re all seeking.”
“A life lived for oneself alone is not liberation, but merely another form of bondage.”
“Growth is not always about getting what we think we want. Always, it’s about becoming the men and women we have the potential to be. Loving, pure, honest, clear.”
“Heaven is a conscious choice to defy the ego’s voice.”
3. Attached: The New Science of Adult Attachment and How It Can Help You Find — and Keep — Love
Authors: Dr. Amir Levine, M.D., Rachel S. F. Heller, M.A.
Five-word synopsis: Your role in a relationship.
Why it changed my life:
As I mentioned at the beginning of this post, Attached came highly recommended by my therapist — and completely changed the way I look at my life. After I finished the book, I radically reevaluated my past, not just through a romantic lens, but a parental one as well. Just like the Five Love Languages (another book that changed my life), the framework of attachment put forth in Attached helped me look at all of my relationships with a candor and clarity I didn’t have before reading it. And it helped to normalize my emotions in the process because it made me understand that I’m not alone in those feelings.
That moment — that realization — is what caused The Shift to occur within me. And I’ve never looked back. Now, I can hear the various attachment styles in song lyrics, in movie dialogue and in everyday conversation. Dysfunctional dynamics have a lucidity they lacked before I read Attached.
I love this book so much, I actually listed some of its biggest takeaways in the very first life lesson on my list of 16 Life Lessons I Wish I’d Learned Sooner. So, don’t delay — get your copy and arm yourself with this incredible intel.
My five favorite quotes:
“Attachment principles teach us that most people are only as needy as their unmet needs. When their emotional needs are met, and the earlier the better, they usually turn their attention outward. This is sometimes referred to in attachment literature as the ‘dependency paradox’: The more effectively dependent people are on one another, the more independent and daring they become.”
“The trick is not to get hooked on the highs and lows and mistake an activated attachment system for passion or love. Don’t let emotional unavailability turn you on.”
“Studies have found that the same areas in the brain that light up in imaging scans when we break a leg are activated when we split up with our mate. As part of a reaction to a breakup, our brain experiences the departure of an attachment figure in a similar way to that in which it registers physical pain.”
“True love, in the evolutionary sense, means peace of mind. ‘Still waters run deep’ is a good way of characterizing it.”
“A general word of advice: It’s always more effective to assume the best in conflict situations. In fact, expecting the worst — which is typical of people with insecure attachment styles — often acts as a self-fulfilling prophecy. If you assume your partner will act hurtfully or reject you, you automatically respond defensively — thus starting a vicious cycle of negativity.”
4. Daring Greatly: How the Courage to Be Vulnerable Transforms the Way We Live, Love, Parent, and Lead
Author: Brené Brown
Three-word synopsis: Vulnerability conquers all.
Why it changed my life:
Named after a line in Teddy Roosevelt’s famous “The Man in the Arena” speech, Daring Greatly is a groundbreaking book that turned complex topics like shame, guilt and vulnerability into household terms. Written in the wake of her viral TEDx Houston talk, “The Power of Vulnerability,” Brené Brown breaks down what a life of radical transparency and honesty means — and how to actually live it.
Daring Greatly changed the way I showed up for myself. I read it towards the beginning of my personal development journey, and it helped me tremendously by showing me that opening up and being authentic — even if it’s uncomfortable — is the most direct way to build true connections with others.
I wouldn’t be the man I am today if I didn’t read this book. I hope it moves the ground beneath your feet as much as it did for me. Truth is, we all need that kind of shakeup every now and again.
My three favorite quotes:
“We all have shame. We all have good and bad, dark and light, inside of us. But if we don’t come to terms with our shame, our struggles, we start believing that there’s something wrong with us — that we’re bad, flawed, not good enough — and even worse, we start acting on those beliefs. If we want to be fully engaged, to be connected, we have to be vulnerable. In order to be vulnerable, we need to develop resilience to shame.”
“If you own this story, you get to write the ending.”
“Vulnerability isn’t good or bad: It’s not what we call a dark emotion, nor is it always a light, positive experience. Vulnerability is the core of all emotions and feelings. To feel is to be vulnerable. To believe vulnerability is weakness is to believe that feeling is weakness. To foreclose on our emotional life out of fear that the costs will be too high is to walk away from the very thing that gives purpose and meaning to living.”
5. He’s Just Not That Into You: The No-Excuses Truth to Understanding Guys
Authors: Greg Behrendt, Liz Tuccillo
Six-word synopsis: If he likes you, you’ll know.
Why it changed my life:
This was the very first self-help book I ever read. And even though it’s been 15 years since I first cracked open the cover, I still go back from time to time to read the timeless examples and no-nonsense responses from authors Greg Behrendt and Liz Tuccillo. Part of the appeal of this book is just how practical and straightforward it is. From cheating to texting to ghosting to avoidance, He’s Just Not That Into You is a necessary, no-holds-barred smack-in-the-face for men and women alike who just can’t help making excuses for the people they date. How would I know? I used to be this person myself. Even to this day, I make some of the most common dating mistakes listed in this book. The point is: If you want to feel like you’re talking about your dating life over mimosas at brunch with some of your blunt best friends, this book is for you.
My three favorite quotes:
“Please, if you can trust one thing I say in this book, let it be this: When it comes to men, deal with us as we are, not how you’d like us to be.”
“I hate to tell you this, but here’s why he feels rushed: He’s still not sure you’re the one.”
“Thinking of yourself as the exception is what got you into this mess in the first place.”
6. How to Avoid Falling in Love with a Jerk: The Foolproof Way to Follow Your Heart Without Losing Your Mind
Author: John Van Epp, Ph.D.
6-word synopsis: Take your time falling in love.
Why it changed my life:
This book was a gift from my aunt, and is one of only three books on the list that I did not buy personally. It also happens to be one of the most fundamental books that changed my dating life.
Don’t be fooled by the catchy title; this book is all substance and zero sass. Based on Van Epp’s Relationship Attachment Model (RAM) for developing healthy, lasting relationships, How to Avoid Falling in Love with a Jerk’s primary lesson is that true romantic love takes time to build.
After falling in love with more than my fair share of guys who didn’t value my heart, this book was the slap in the face I needed to wake up to my worth and finally stop ignoring the red flags I knew were there all along.
I know it has the power to do the same for you, too. Pick it up and watch The Shift wash over you.
My nine favorite quotes:
“A commitment will only be as strong as the conscience that upholds it.”
“You should assume that the way your partner treats a stranger or a worst enemy will most likely be the way you will be treated at some point in time.”
“Communication is the key to opening doors of intimacy and closing doors of misunderstanding and hurt. But it requires joint effort.”
“Words are a window to the heart.”
“A couple must have five times as many interactions or verbal exchanges that generate positive emotions for every one that results in some negative feelings.”
“The good doesn’t always last, and the bad usually gets worse… your dating experience with a particular partner is as good as it gets in a marriage with that partner.”
“The message is clear: Fix yourself first, or your unresolved emotional problems will disrupt both your choice of a partner and the relationship you establish.”
“Your unhealthy need for idealistic love can be broken only by your individual efforts to face your pain and those who afflicted you, and to deal directly with the loss of having never been shown the love you needed, wanted, and deserved.” Many times such efforts require courage to feel the loss as well as to face those who hurt you. A better blend of reality with idealism and the caution to test the one you trust over time will help distinguish an illusion from a genuine dream.”
“Time is the ultimate proof of a promise to change.”
7. Love Does: Discover a Secretly Incredible Life in an Ordinary World
Author: Bob Goff
Three-word synopsis: Love is contagious.
Why it changed my life:
With this game-changing book, Bob Goff shows firsthand that love isn’t just a noun — it’s a verb, just like Jesus intended. Told with heartwarming personal stories from his awe-inspiring life that will make you laugh and shed more than a few tears, Love Does will fill you with a sense of possibility and wonder at the potential of what a life that places compassion at the center looks like.
When I first read it, I was moved by how easily Goff transitions from talking about the epic to the everyday — and how grace can be found in both. It continues to inspire me to be selfless and kind, and live a little more like Jesus, each and every day.
And we could all use a little more of that in our lives.
My four favorite quotes:
“When it’s a matter of the heart, the place doesn’t matter.”
“Things that go wrong can shape us our scar us.”
“That’s what love does — it pursues blindly, unflinchingly, and without end. When you go after something you love, you’ll do anything it takes to get it, even if it costs everything.”
“Words spoken by kind people have the ability to endure in our lives.”
8. Outliers: The Story of Success
Author: Malcolm Gladwell
Four-word synopsis: Success = Talent + timing + practice.
Why it changed my life: How do successful people become successful? What differentiates them from others? What can we learn from those distinguishing attributes and factors? These are the central questions that Outliers seeks to answer. Famous for its “10,
                000-Hour” Rule, Outliers is the simple yet eloquent evaluation of how a confluence of factors can influence who gets ahead and who gets left behind. The good news? You have the power — primarily through hours and hours of practice — to hone your craft, sharpen your abilities and change your position in society, all while creating a better life for yourself in the process.
Outliers reinforced a deep truth about the world that I already knew: Your inner nature is important, but it’s how you nurture it that makes all the difference. This book showed me that where I came from mattered, but how hard I prepared to go where I wanted to go mattered more.
And that’s a watershed moment I’ll never forget.
My four favorite quotes:
“Practice isn’t the thing you do once you’re good. It’s the thing you do that makes you good.”
“Achievement is talent plus preparation.”
“Superstar lawyers and math whizzes and software entrepreneurs appear at first blush to lie outside ordinary experience. But they don’t. They are products of history and community, of opportunity and legacy. Their success is not exceptional or mysterious. It is grounded in a web of advantages and inheritances, some deserved, some not, some earned, some just plain lucky — but all critical to making them who they are. The outlier, in the end, is not an outlier at all.”
“It is those who are successful, in other words, who are most likely to be given the kinds of special opportunities that lead to further success. It’s the rich who get the biggest tax breaks. It’s the best students who get the best teaching and most attention. And it’s the biggest nine- and ten-year-olds who get the most coaching and practice. Success is the result of what sociologists like to call ‘accumulative advantage.’”
9. The Alchemist
Author: Paulo Coelho
Seven-word synopsis: Keep moving forward; your life has purpose.
Why it changed my life:
The Alchemist is the only fiction book to make my list of 13 books that changed my life. And for good reason. While it might not be based in fact, it’s most certainly based in truth. This parable is a page-turning account of a young shepherd on a journey to discover that there’s more to life than meets the eye. This seismic novel is, at its crux, about how to transform the obstacles in your life into opportunities to embrace who you really are. Turns out, gratitude is alchemy for the soul, helping to heal our deepest wounds and connect us to the divinity in all things.
I’ve given this book as a gift to several friends over the years. It’s a truly beautiful story that has a poetic, lyrical quality to it. I couldn’t put it down. And I know you won’t be able to either.
My six favorite quotes:
“And, when you want something, all the universe conspires in helping you to achieve it.”
“It’s the possibility of having a dream come true that makes life interesting.”
“The secret of life, though, is to fall seven times and to get up eight times.”
“Tell your heart that the fear of suffering is worse than the suffering itself. And that no heart has ever suffered when it goes in search of its dreams, because every second of the search is a second’s encounter with God and with eternity.”
“We are travelers on a cosmic journey, stardust swirling and dancing in the eddies and whirlpools of infinity. Life is eternal. We have stopped for a moment to encounter each other, to meet, to love, to share. This is a precious moment. It is a little parenthesis in eternity.”
“Everything that happens once can never happen again. But everything that happens twice will surely happen a third time.”
10. The Five Love Languages: The Secret to Love that Lasts
Author: Gary Chapman
Six-word synopsis: How you give and receive love.
Why it changed my life:
If love is why we’re on this planet, then Gary Chapman gives us a way to understand how exactly to make sense of it. The Five Love Languages is a framework that does just that: Helps you understand how you communicate and interpret love in your life. What could be more powerful than that?
For me, reading this seminal book helped me sift through all of my memories and experiences and extract exactly why I gravitated towards certain people and not toward others. Understanding these preferences for giving and receiving love helped me approach my career, my family, my friends and my romantic partners with a newfound understanding of what made me feel close and connected to those that mattered most to me. Reading The Five Love Languages is like waking up to a world you knew existed but could never find. It’s truly that life changing. If you haven’t already, add this classic to your reading list. You won’t regret it.
My five favorite quotes:
“Forgiveness is not a feeling; it is a commitment.”
“People tend to criticize their spouse most loudly in the area where they themselves have the deepest emotional need.”
“For love, we will climb mountains, cross seas, traverse desert sands, and endure untold hardships. Without love, mountains become unclimbable, seas uncrossable, deserts unbearable, and hardships our lot in life.”
“The best thing we can do with the failures of the past is to let them be history.”
“Most of us have more potential than we will ever develop. What holds us back is often a lack of courage.”
11. The Universe Has Your Back: Transform Fear to Faith
Author: Gabby Bernstein
Four-word synopsis: You are being guided.
Why it changed my life: This book by Gabby Bernstein changed my life because it reminded me to focus on one thing and one thing only: Relinquishing fear and embracing love. Once you do that, the rest will fall into place naturally. A refresher course in surrender, trust and faith, The Universe Has Your Back re-instilled my conviction that I am always being guided to where I’m meant to be. And the Universe will always automatically correct itself in the direction of love if I allow it.
And that’s a potent lesson everyone needs to learn.
Fair warning: I finished this book in one sitting. It was just too good to put down. I hope you feel the same when you read it, too.
My eight favorite quotes:
“The miracle isn’t how well we avoid fear, the miracle is how quickly we return to love.”
“True healing occurs when you give yourself permission to feel whatever feelings live below the triggers.”
“The Universe will do for you what you cannot do for yourself.”
“What would your life be like if joy were your priority?”
“All obstacles that are perceived with love can be transformed into the greatest life lessons.”
“The best conversations begin with the words thank you.”
“People are our teachers in the classroom that is our life.”
“The simple act of asking, ‘How would you use me?’ opens the floodgates for love to transcend all doubt and limitation. Your fear cannot co-exist in the presence of this love.”
12. The Untethered Soul: The Journey Beyond Yourself
Author: Michael A. Singer
Five-word synopsis: Let it pass through you.
Why it changed my life:
The Untethered Soul is a master class in the art of letting go so that you can soar in your life. If you’re looking to promote a sense of peace and really clear the blockages within that are holding you back, this book will help you do just that. As Deepak Chopra says on the cover, “Read this book carefully and you will get more than a glimpse of eternity.”
Since reading this book, I feel lighter, calmer and more aware of my energy and myself. I feel that sense of eternity. I feel free. I know you’ll feel the same when you read these pages, too. Like many of the other books on the list, I have read and re-read this book many times when I’ve been going through a hard time or needed some spiritual transparency. Pick up a copy and keep it permanently on your nightstand. It’s just that good.
My 17 favorite quotes:
“There is nothing more important to true growth than realizing that you are not the voice of the mind — you are the one who hears it.”
“Eventually you will see that the real cause of problems is not life itself. It’s the commotion the mind makes about life that really causes problems.”
“If you want to achieve peace in the face of your problems, you must understand why you perceive a particular situation as a problem.”
“You have to break the habit of thinking that the solution to your problems is to rearrange things outside.”
“Consciousness is the highest word you will ever utter. There is nothing higher or deeper than consciousness. Consciousness is pure awareness.”
“When you are an aware being, you are no longer immersed in the events around you.”
“The more you are willing to just let the world be something you’re aware of, the more it will let you be who you are — the awareness, the Self, the Atman, the Soul.”
“Do not let anything that happens in life be important enough that you’re willing to close your heart over it.”
“As you grow spiritually, you will realize that your attempts to protect yourself from your problems actually create more problems.”
“Pain is not bad; it’s how the body talks to you.”
“The truth is, everything will be okay as soon as you are okay with everything.”
“Eventually you will understand that there is an ocean of love behind all of this fear and pain.”
“Eventually you will realize that darkness is not what’s really there. What is really there are the walls that are blocking the infinite light.”
“What it means to live spiritually is to not participate in this struggle. It means that the events that happen in the moment belong in the moment. They don’t belong to you. They have nothing to do with you. You must stop defining yourself in relationship to them and just let them come and go.”
“What actually gives life meaning is the willingness to live it. It isn’t any particular event; it’s the willingness to experience life’s events.”
“When a consciousness stops identifying itself as the ray, it comes to know itself as the sun.”
“Ecstasy is the only thing God knows. God’s nature is eternal, conscious bliss. No matter what you’ve done, you’re not going to be the one thing that ruins it.”
13. The Velvet Rage: Overcoming the Pain of Growing Up Gay in a Straight Man’s World
Author: Alan Downs, Ph.D.
6-word synopsis: Be authentic. Tolerate shame. Embrace imperfection.
Why it changed my life:
This book should be required reading for all gay men because of its direct and pointed evaluation of shame in the gay community. The Velvet Rage is a heady dose of truth about numbing, avoiding and projecting — and all the ways gay men in particular bury the pain of not quite fitting in. Honestly, this book helped me understand my anger, anguish and anxiety at a level so deep it made me cry.
If you’re a gay man, you’re likely to find more than a little bit of truth in this book. And I was no exception. At times, it felt like Alan Downs was writing a biography of my life, detailing my struggles with shame in plain language for all to see. I highly recommend it to any gay man who might be tired of the drinking and the sex and the pressure to have the perfect job and perfect body and perfect life.
Freedom awaits those brave enough to take the journey inward along with Dr. Downs. Do you dare?
My 12 favorite quotes:
“So the little boy with the big secret becomes the man who is driven to avoid shame by hiding his dark truth. Famished for authentic validation and without a reliable sense of self-direction, he develops a sophisticated radar for those things and people who will make him feel good about himself.”
“[Gay men
                ] are professionals in remodeling ugly truths into high-fashion dreams.”
“Why is authentic validation important? Because when we are validated for a pretense, the validation is hollow, it’s baseless, it’s not at all satisfying. For example, if you had someone else write your term paper for a class and you subsequently received an ‘A’ on it, that isn’t validating. Or more to the point, when a gay man presents a false, inauthentic self to the world and is subsequently validated for that façade, he will feel hollow, and the validation won’t be satisfying.”
“What eventually breaks this vicious cycle? It is the slow process of learning to tolerate and reduce shame rather than avoid it. He can learn from the mistakes of his past only if he is willing to carefully examine them. When these mistakes remain shrouded in shame, he cannot afford to investigate his own life. He keeps moving forward, trying not to look back, and as a result, finds himself going in a circle.”
“When you drop the struggle with shame and accept life as it is without judgment, you find great freedom on the other side. It is the freedom to be who you are, exactly as you are. The only real meaning in life is found in being who you are right now, without apologies.”
“No matter what you think you might gain from a particular decision, if it doesn’t ultimately contribute to your attainment of inner peace, it isn’t worth it.”
“Contentment is created when your behavior is consistent with your values.”
“When life doesn’t turn out the way you want, stop insisting that it not be so.”
“The failure to accept others for who they are only serves to increase your own distress.”
“The expression of judgment upon others is nothing less than what we deliver to ourselves.”
“See past the betrayal, anger, and dishonesty in honors to find their core innocence.”
“The secret to life isn’t an idea — it’s a behavior. You must do, not just think about, what is likely to bring you joy and peace.”
BONUS: It’s Good to See Me Again: How to Find Your Way When You Feel Lost
Author: Chris Rackliffe (that’s me!)
9-word synopsis: Our lives are defined by our relationship with Change.
Why it changed my life:
Writing this book was more than just putting pen to paper; it was a cathartic experience. Delving deep into some of my own biggest challenges like the death of my mom, being cheated on by an ex, losing my job, and enduring molestation as a child; I finally formalized how I learned to cope with all the hurt, how I was able to forgive, and how I let go — once and for all.
Change can be scary to experience, difficult to process, and harder yet to accept. But it’s also the law of life. Whether it’s a brutal breakup, a devastating death, a jarring job loss, a debilitating diagnosis, or a perilous pandemic; Change has a way of breaking open our hearts for something bigger, better, and more beautiful to enter our lives. But only if we know how to converse with it.
It’s Good to See Me Again shows you how to not just embrace Change, but completely transform your relationship with it — exploring the four steps of the RACE Model for Change:
Resist one thing only: Your resistance to Change.
Accept what you cannot Change so you may let go.
Choose to Change what you can by reclaiming your power to choose.
Embrace Change by remaining open to it in the future.
This is how we find our way back to ourselves when we feel lost. Follow the RACE model for Change and you will always find your way back home to you. Choose to embark on this journey and you will learn to befriend Change. Choose the path of highest good laid out for you and you will finally be able to say, “It’s Good to See Me Again.”
My 8 favorite quotes:
“A cracked heart isn’t a wounded heart; it’s a whole heart revealing itself.”
“The only way something can have power over you is if you surrender your own power to choose right now.”
“You can’t hold a fire in your heart and expect it not to burn you. Release the flame and you will begin to heal.”
“Awareness is a form of alchemy; it will turn all your anguish into gold.”
“One of the healthiest things you can do in life is realize when something no longer serves the light in you.”
“When I let go of my need for life to be a certain way in order to be happy, I unlock the happiness that already exists within me.”
“I see everything that happens as a signal to fear less and love more.”
“The path of highest good is a reunification with the force of highest good. And that force is love.”
Have you read any of these books? Which are you most excited to check out? Tell me in the comments below — or Tweet me @crackliffe.
Want even more wisdom on how to live a better life? Check out 17 Cognitive Distortions — and 12 Ways to Defeat Them.
Additional resources to check out:
The Velvet Rage quotes
Outliers quotes
Attached quotes
Attached FourMinuteBooks summary
Paulo Coelho quotes
The Alchemist life lessons
Understanding the Five Love Languages
Insights from Daring Greatly
How to Know the Universe Has Your Back
A Course in Miracles quotes
Teddy Roosevelt’s “The Man in the Arena” speech''',


"6":'''The Mutually Exclusive Society
Dan Jones
Dan Jones
Follow
Jul 10 · 4 min read



Our society has come to resemble our two-party system, complete with all its neuroses. Have you noticed how often we are presented with binary scenarios that don’t reflect reality? Even official political debates are littered with loaded questions punctuated by a request for a yes or no response.
Image for post
To our corporate, media, and political leaders, everything has become mutually exclusive. Black and white. Good versus evil. On the right side of history or not. Here’s a small sampling of reasonable beliefs that get packaged as bullshit false choices from which we’re forced to pick a side:
America still struggles with racism.
America is possibly the best place in the world for racial minorities.
CNN is a hyper partisan media organization that serves only to divide America.
FoxNews is a hyper partisan media organization that serves only to divide America.
American police kill too many people.
Too many people disrespect the police in America.
America still struggles with sexism.
America is possibly the best place in the world for female professionals.
Too many unqualified people own guns in America.
The second amendment is an important American civil liberty.
America has a problem with illegal immigration.
America’s immigrants should be celebrated as a source of national strength.
America is involved in too many foreign wars.
A strong military is vital to American security.
Foreign countries unfairly subsidize some industries.
America unfairly subsidizes some industries.
America has a drug problem.
Some drugs should be decriminalized.
Unions are a crucial part of a capitalist system.
Unions have occasionally led to the downfall of companies and industries.
Climate change is a real challenge.
The government may not always be the best agent for overcoming the climate challenge.
Of the 22 individual statements above, how many do you disagree with? I’ve paired each statement with what might seem to our political class to be a contradiction, only it’s not. It is a different perspective, but it is not a contradictory perspective. I think if I gave you truth serum, you’d agree with both sides of a majority of them.
Exit the factions before it’s too late
We exist in a political system where one party sees 11 of these statements as the gospel truth and the other 11 as heresy. If you’re one of the ~60% of Americans who is a member of either the Republican or Democratic Party, you’re a member of a party that deliberately seeks out contradiction and confrontation where little or none exists. You’re a member of a faction that is tearing America asunder.
You’re for unions or you’re against them. You’re a believer in science or a science denier.
Image for post
If you are a member of one of these two political parties, you are part of a problem. Not just any problem, though, you are part of the problem. You are part of the single greatest existential threat to the United States today. You are on a level with North Korea, Russia, China, Earth-bound asteroids, and COVID-19. Only you are worse, because you’re already here, you do it voluntarily, and you don’t even realize the harm you’re doing.
You’re part of a party that demands loyalty over reason and outsources official debates to dinosaur media organizations that profit off of maximum division. These debates play to an audience’s basest instincts through emotionally-charged questions that are best answered in short, TV-ready sound bites. The questions asked are prioritized not by what could have the biggest impacts on American society or the American economy, but by which raise our collective blood pressure, generate the most clicks, and sell the most papers.
You’re part of a party that had a noble beginning. One, an abolitionist party that birthed Abraham Lincoln. The other, the culmination of what began as an alliance between Messrs Thomas Jefferson and James Madison. You’re part of a party that today causes all three of these individuals to turn in their graves, that is unrecognizable from its founding principles, and for which no remaining reverence is warranted.
You’re part of something I call The Mutually Exclusive Society, an anachronistic faction that James Madison aptly warned us about in 1788 in his Federalist № 10:
AMONG the numerous advantages promised by a well-constructed Union, none deserves to be more accurately developed than its tendency to break and control the violence of faction. The friend of popular governments never finds himself so much alarmed for their character and fate, as when he contemplates their propensity to this dangerous vice. He will not fail, therefore, to set a due value on any plan which, without violating the principles to which he is attached, provides a proper cure for it. The instability, injustice, and confusion introduced into the public councils, have, in truth, been the mortal diseases under which popular governments have everywhere perished.
It’s long past time we heed the words of Madison and others by dedicating ourselves to a plan which provides a proper cure for our national malady. Today, I believe that plan is #Unity2020. Will you join us and save the Republic? https: //www.articlesofunity.com/''', 


"7":'''Introduction to Decision Intelligence
A new discipline for leadership in the AI era
Cassie Kozyrkov
Cassie Kozyrkov
Follow
Aug 2,
                2019 · 14 min read



Curious to know what the psychology of avoiding lions on the savannah has in common with responsible AI leadership and the challenges of designing data warehouses? Welcome to decision intelligence!
Image for post
Source: xijian/Getty
Decision intelligence is a new academic discipline concerned with all aspects of selecting between options. It brings together the best of applied data science, social science, and managerial science into a unified field that helps people use data to improve their lives, their businesses, and the world around them. It’s a vital science for the AI era, covering the skills needed to lead AI projects responsibly and design objectives, metrics, and safety-nets for automation at scale.
Decision intelligence is the discipline of turning information into better actions at any scale.
Let’s take a tour of its basic terminology and concepts. The sections are designed to be friendly to skim-reading (and skip-reading too, that’s where you skip the boring bits… and sometimes skip the act of reading entirely).
What’s a decision?
Data are beautiful, but it’s decisions that are important. It’s through our decisions — our actions — that we affect the world around us.
We define the word “decision” to mean any selection between options by any entity, so the conversation is broader than MBA-style dilemmas (like whether to open a branch of your business in London).
It’s through our decisions — our actions — that we affect the world around us.
In this terminology, appending a label such as cat versus not-cat to a user’s photo is a decision executed by a computer system, while figuring out whether to launch that system is a decision taken thoughtfully by the human leader (I hope!) in charge of the project.
Image for post
What’s a decision-maker?
In our parlance, a “decision-maker” is not that stakeholder or investor who swoops in to veto the machinations of the project team, but rather the person who is responsible for decision architecture and context framing. In other words, a creator of meticulously-phrased objectives as opposed to their destroyer.
What’s decision-making?
Decision-making is a word that is used differently by different disciplines, so it can refer to:
taking an action when there were alternative options (in this sense it’s possible to talk about decision-making by a computer or a lizard).
performing the function of a (human) decision-maker, part of which is taking responsibility for decisions. Even though a computer system can execute a decision, it will not be called a decision-maker because it does not bear responsibility for its outputs — that responsibility rests squarely on the shoulders of the humans who created it.
Making a calculation versus making a decision
Not all outputs/suggestions are decisions. In decision analysis terminology, a decision is only made once an irrevocable allocation of resources takes place. As long as you can change your mind for free, no decision has been made yet.
Decision intelligence taxonomy
One way to approach learning about decision intelligence is to break it along traditional lines into its quantitative aspects (largely overlapping with applied data science) and qualitative aspects (developed primarily by researchers in the social and managerial sciences).
Qualitative side: The decision sciences
The disciplines making up the qualitative side have traditionally been referred to as the decision sciences — which I’d have loved for the whole thing to be called (alas we can’t always have what we want).
Image for post
The decision sciences concern themselves with questions like:
“How should you set up decision criteria and design your metrics?” (All)
“Is your chosen metric incentive-compatible?” (Economics)
“What quality should you make this decision at and how much should you pay for perfect information?” (Decision analysis)
“How do emotions, heuristics, and biases play into decision-making?” (Psychology)
“How do biological factors like cortisol levels affect decision-making?” (Neuroeconomics)
“How does changing the presentation of information influence choice behavior?” (Behavioral Economics)
“How do you optimize your outcomes when making decisions in a group context?” (Experimental Game Theory)
“How do you balance numerous constraints and multistage objectives in designing the decision context?” (Design)
“Who will experience the consequences of the decision and how will various groups perceive that experience?” (UX Research)
“Is the decision objective ethical?” (Philosophy)
This is just a small taste… there are many more! This is also far from the complete list of disciplines involved. Think of the decision science side as dealing with decision setup and information processing in its fuzzier storage form (the human brain) rather than the kind that’s neatly written down in semi-permanent storage (on paper or electronically) which we call data.
The trouble with your brain
In the previous century, it was fashionable to praise anyone who stuffed a fat wad of math into some unsuspecting human endeavor. Taking a quantitative approach is usually better than thoughtless chaos, but there’s a way to do even better.
Strategies based on pure mathematical rationality are relatively naïve and tend to underperform.
Strategies based on pure mathematical rationality without a qualitative understanding of decision-making and human behavior can be pretty naïve and tend to underperform relative to those based on joint mastery of the quantitative and qualitative sides. (Stay tuned for blog posts on the history of rationality in the social sciences as well as examples from behavioral game theory where psychology beats mathematics.)
Humans are not optimizers, we’re satisficers, which is a fancy word for corner cutters.
Humans are not optimizers, we’re satisficers, which is a fancy word for corner cutters who are satisfied with good enough as opposed to perfect. (It’s also a concept that was enough of a shocker to our species arrogance—a punch in the face of rational Man, godlike and flawless — that it was worth a Nobel Prize.)
Image for post
Image: Source.
In reality, we humans all use cognitive heuristics to save time and effort. That’s often a good thing; working out the perfect running path to get away from a lion on the savannah would get us eaten before we’ve barely started the calculation. Satisficing also reduces the calorie cost of living, which is just as well, since our brains are ridiculously power-hungry devices as it is, gobbling up around a fifth of our energy expenditure despite weighing approximately 3 lb. (I bet you weigh more than 15 lb in total, right?)
Some of the corners we cut lead to predictably suboptimal outcomes.
Now that most of us don’t spend our days running away from lions, some of the corners we cut lead to predictably rubbish outcomes. Our brains aren’t exactly, er, optimized for the modern environment. Understanding the manner in which our species turns information into action allows you to use decision processes to protect yourself from the shortcomings of your own brain (as well as from those who intentionally prey on your instincts). It also helps you build tools that augment your performance and adapt your environment to your brain if the poor thing is Lamarckably slow to catch up a la Darwin.
If you think that AI takes the human out of the equation, think again!
By the way, if you think that AI takes the human out of the equation, think again! All technology is a reflection of its creators and systems that operate at scale can amplify human shortcomings, which is one reason why developing decision intelligence skills is so necessary for responsible AI leadership. Learn more here.
Image for post
Perhaps you’re not making a decision
Sometimes, thinking through your decision criteria carefully leads you to realize that there’s no fact in the world that would change your mind — you’ve selected your action already and now you’re just looking for a way to feel better about it. That’s a useful realization — it stops you from wasting more time and helps you redirect your emotional discomfort while doing what you were going to do anyways, data be damned.
“He uses statistics as a drunken man uses lamp-posts… for support rather than illumination.” -Andrew Lang
Unless you would take different actions in response to different still-unknown facts, there’s no decision here… though sometimes training in decision analysis helps you see those situations more clearly.
Decision-making under perfect information
Now imagine that you’d dealt very carefully with setting up a decision that is sensitive to the facts and you can snap your fingers to see the factual information you need for executing your decision. What do you need data science for? Nothing, that’s what.
The first order of business should be figuring out how we’d like to react to facts.
There’s never anything better than a fact — something you know with certainty (yes, I’m aware there’s a gaping relativist rabbit hole here, let’s move along) — so we always prefer to make decisions based on facts if we have them. That’s why the first order of business should be figuring out how we’d like to deal with facts. Which of the following uses would you want to put your ideal information to?
Image for post
Your author particularly enjoyed this wall in Jamaica.
What can you do with facts?
You can use facts to make a single important pre-framed decision. If it’s important enough, you’ll need to lean heavily on the qualitative side of things to frame your decision wisely. Psychologists know that if you allow yourself to be ambushed by surprise information, it can manipulate you in ways you wouldn’t like, so they (and others) have lots to say about how to approach selecting the information you’ll accept in advance.
You can use facts to make a special kind of pre-framed decision, called an impact (or causal) decision. If your decision is framed in terms of taking an action to cause something to happen, then you need facts about cause-and-effect relationships to make your decision. In such cases, facts about effects (e.g. “people recover from this illness”) are useless to you if they don’t come with facts about causes (e.g. “because of antibiotics”). The way to get your hands on cause-and-effect information is to do a controlled experiment. On the other hand, if you are making an execution decision framed as a response to a non-causal fact (e.g. “if I have at least x in my savings account, I will treat myself to new shoes”), then an experiment is not necessary.
You can use facts to shore up opinions (“I expect it’s sunny outside” becomes “I know it’s sunny outside”).
You can use facts to make a single important existence-based decision. Existence-based decisions (“I just found out there exists a case of ebola right next door, so I’m getting out of here pronto…”) are decisions where the existence of a formerly unknown unknown shakes the foundation of your approach so much that you realize in hindsight that your decision context was sloppily framed.
You can use facts to automate a large number of decisions. In traditional programming, a human specifies the set of instructions for converting fact inputs into appropriate actions, possibly involving something like a lookup table.
You can use facts to reveal an automation solution. By seeing the facts about the system, you can write code based on them. This is a better approach to traditional programming than coming up with the structure of a solution by thinking really hard with no information. For example, if you don’t know how to convert from Celsius to Fahrenheit, but you could use a dataset to look up the entry in Fahrenheit that goes with the Celsius input… but if you analyze that lookup table itself, you’ll discover the formula that connects them. Then you can just code up that formula (“model”) to do your dirty work for you and lose the clunky table.
You can use facts to generate an optimal solution to an automation problem that is perfectly solvable. This is traditional optimization. You’ll find many examples in the field of operations research, which covers, among other things, how to wrangle constraints to get the ideal outcome, such as the best order in which to complete a series of tasks.
You can use facts to inspire how you’ll approach future important decisions. This is part of analytics, which also belongs in the section on partial information. Hold that thought!
You can use facts to take stock of what you’re dealing with. This helps you understand the kinds of inputs you have available for future decisions and design how to curate your information better. If you’ve just inherited a big, dark (data) warehouse full of potential ingredients, you won’t know what’s inside until someone looks at it. Luckily, your analyst has a flashlight and rollerblades.
You can use facts sloppily to make unframed decisions. This is efficient when decisions have sufficiently low stakes that they do not warrant the effort required to approach them carefully, such as, “What should I eat for lunch today?” Attempting to be rigorous all the time on all decisions gives suboptimal long-run / lifetime outcomes and falls into the category of pointless perfectionism. Save your effort for the situations that are important enough for it, but please don’t forget that even if it’s efficient to use a low-quality low-effort approach, the optimal decision approach is still of low quality. You shouldn’t thump your chest or be overconfident when that’s your method… If you cut corners, you’re holding something flimsy. There are situations where flimsy gets the job done, but that doesn’t suddenly make your conclusion sturdy. Don’t lean on it. If you want high-quality decision-making, you need a more rigorous approach.
With training in the decision sciences, you learn to reduce the effort that it takes to make rigorous fact-based decisions, which means that the same amount of work now gets you higher-quality decision-making across the board. This is a very valuable skill, but it takes lots of work to hone it. For example, students of behavioral economics form the habit of setting decision criteria in advance of information. Those of us who took a beating from sufficiently demanding decision science training programs can’t help but ask ourselves, for example, what the maximum that we’d pay for a ticket is BEFORE we look up the price.
Data collection and data engineering
If we had the facts, we’d be done already. Alas, we live in the real world and often we must work for our information. Data engineering is a sophisticated discipline centered on making information available reliably at scale. In the way that going to the grocery store for a pint of ice cream is easy, data engineering is easy when all available relevant information fits in a spreadsheet.
Image for post
Things get tricky when you start asking for the delivery 2 million tons of ice cream… where it’s not allowed to melt! Things get even trickier if you have to design, set up, and maintain a huge warehouse and you don’t even know what the future will ask you to store next — maybe it’s a few tons of fish, maybe it’s plutonium… good luck!
It’s tricky to set up a warehouse when you don’t even know what you’ll be asked to store next week— maybe it’s a few tons of fish, maybe it’s plutonium… good luck!
While data engineering is a separate sister discipline and key collaborator to decision intelligence, the decision sciences include a strong tradition of expertise involved in advising the design and curation of fact collection.
Quantitative side: Data science
When you’ve framed your decision and you look up all the facts you need, using a search engine or an analyst (performing the role of a human search engine for you), all that’s left is to execute your decision. You’re done! No fancy data science needed.
What if, after all that legwork and engineering jiu-jitsu, the facts delivered are not the facts you ideally need for your decision? What if they’re only partial facts? Perhaps you want tomorrow’s facts, but you only have the past to inform you. (It’s so annoying when we can’t remember the future.) Perhaps you want to know what all your potential users think of your product, but you can only ask a hundred of them. Then you’re dealing with uncertainty! What you know is not what you wish you knew. Enter data science!
Data science gets interesting when you’re forced to make leaps beyond the data… but do be careful to avoid an Icarus-like splat!
Naturally, you should expect your approach to change when the facts you have aren’t the facts you need. Maybe they’re one puzzle piece of a much bigger puzzle (as with a sample from a larger population). Maybe they’re the wrong puzzle, but the best you have (as with using the past to predict the future). Data science gets interesting when you’re forced to make leaps beyond the data… but do be careful to avoid an Icarus-like splat!
You can use partial facts to make a single important pre-framed decision with statistical inference, supplementing the information you have with assumptions to see if you should change your action. This is Frequentist (classical) statistics. If you’re making an impact decision (framed in terms of taking an action to cause something to happen, e.g. “you’d only want to change your logo color to orange if that causes more people visit your website”), then it’s best to use data from a randomized controlled experiment. If you’re making an execution decision (e.g. “you’d only want to change your logo color to orange if at least 25% of your users consider orange to be their favorite color”), a survey or observational study is good enough.
You can use partial facts to reasonably update opinions into more informed (but still imperfect and personal) opinions. This is Bayesian statistics. If these opinions are involve cause-and-effect relationships, it’s best to use data from a controlled randomized experiment.
Your partial facts may turn out to contain facts about existence, which means you could use them in hindsight for existence-based decisions (see above).
You can use partial facts to automate a large number of decisions. That’s traditional programming using something like a lookup table where you convert something you haven’t seen before into the closest thing you that you have, then proceed as usual. (That’s what k-NN does in a nutshell… and it usually works better when that nutshell has more things in it.)
You can use partial facts to inspire an automation solution. By seeing the partial facts about the system, you can still write code based on what you’re seeing. This is analytics.
You can use partial facts to generate a decent solution to an imperfectly solvable automation problem so you don’t have to come up with it yourself. This is machine learning and AI.
You can use partial facts to inspire how you’ll approach future important decisions. This is analytics.
You can use partial facts for understanding what you’re dealing with (see above) and to accelerate the development of an automation solution with advanced analytics, for example by inspiring new ways to blend information together to make useful model inputs (the jargon for this is “feature engineering”) or new methods to try in an AI project.
You can use partial facts sloppily to make unframed decisions, but be aware that the quality is even lower than when you use facts sloppily, because what you actually know is one step removed from what you wish you knew.
For all of these uses, there are ways to integrate wisdom from a variety of previously-siloed disciplines to approach decision-making more effectively. That’s what decision intelligence is all about! It brings together diverse perspectives on decision-making which make all of us stronger, together, and gives them a new voice that’s free of the traditional constraints of their originating fields of study.
Image for post
To return to the kitchen analogy for AI, if research AI is building microwaves and applied AI is using microwaves, decision intelligence is using microwaves safely to meet your goals and using something else when you don’t need a microwave. The goal (objective) is always the starting point for decision intelligence.
If you’re curious to read more, most of my articles here on Medium.com have been written from a decision intelligence perspective. My guide to starting AI projects is probably the least subtle, so I’d recommend diving in there if you haven’t already chosen your own adventure by following the links in this article.''',


"8":'''Everything you need to become a self-taught Machine Learning Engineer
Jason Benn
Jason Benn
Follow
Mar 13 · 10 min read



Image for post
In 2011, I graduated from UVA with a degree in Economics and joined a boutique consulting firm in Virginia.
None of that is related to what I do today.
Because today, I am a Machine Learning Engineer at a well-funded ML startup in Silicon Valley, living my dream. I work on the latest in AI research, implement AI papers, and explore new product ideas in my specialty fields of NLP and ML infrastructure.
The thing you do after graduation is not always your permanent path. I absolutely hated everything about consulting. I lasted about a year and a quarter, and then I decided to quit and have a mulligan on my whole life.
I made a pros and cons list of all the possible careers I could do instead. My favorite book was Cal Newport’s “So Good They Can’t Ignore You”, which persuaded me that my career North Star should just be to learn really useful skills. By that metric, programming was at the top of my list.
“My career North Star should just be to learn really useful skills. By that metric, programming was at the top of my list.”
As I saw it, the steps to get there were: buy a bunch of textbooks, move into my mom’s basement, read those books, and program until I got a job.
ML hack: first, become a programmer
Because I was starting from scratch, I decided to join a short programming school. I signed up for Dev Bootcamp, a 3-month program designed to help me get my first job.
Dev Bootcamp has since shut down, so my #1 recommendation now is Lambda School, which is a 9-month program where you learn how to code from teachers alongside other newbies. Lambda School’s business model is special: you don’t have to pay anything upfront, you pay a percentage of your income over your first two years as a programmer. In other words, Lambda School is incentivized to find you a great job after graduation, and a lot of great companies hire out of Lambda School.
You can go from a bank teller to a programmer in 9 months.
What’s a helpful career path? I think it’s important to know that there are a broad variety of jobs that use machine learning. It would be pretty hard to go straight into machine learning engineering without a background in Computer Science (CS). But it’s not as hard to go from non-CS into Data Science (and yes, Lambda School also has a Data Science program).
This article is about machine learning engineering (MLE), but remember that the foundation of any great programming career, including MLE, is computer science. The ML in MLE is only 10% of the job. Another 10% is data science. The last 80% is computer science.
After Dev Bootcamp, I learned computer science through Bradfield, a school where working programmers can take a series of one-month courses. You can take them part-time in addition to your day job. I did six between 2015–2017 and another one in 2019, and now they’re fully online. They’re intense — 10 hours of class and 10 hours of homework a week — but worth it.
If you want to do the same without paying for their classes, they make their curriculum free online at teachyourselfcs.com.
ML hack: create a group of ML enthusiasts
Three years into my programming career, and near the end of my CS curriculum, I started looking for my next big useful skill. I picked machine learning. First, I co-organized an ML book club with a coworker. We read An Introduction to Statistical Learning: with Applications in R (which is my second choice recommendation after this one).
I wanted a group to keep me accountable to skill building, so I launched my own Paper Club, an initiative where two friends and I went through all of fast.ai in six months. Fast.ai is an online course with two parts. Each is about 15 hours with 15 hours each in homework (so,
                60 hours total). We met one night per week on Zoom or in a local park. After we finished fast.ai, we started reading research papers, and would go through each paper, page by page, and discuss blockers or challenges with the end of being able to understand any paper. It was tough — for the first few months, it took us 6 hours to read each paper (and each paper is only 10 pages long!). Paper Club lasted about two years and without that social accountability there’s no way I would have been able to keep studying for so long.
After one year of Paper Club, I decided it was time to quit my job again.
I spent two months on sabbatical, learning ML all day. I focused on diving deeper into the fundamentals and reimplementing neural nets from scratch.
If you’re wondering about helpful books, here is a 10-week course I assembled for a few friends. And here’s a post about learning to become a SWE and a MLE and the books I read/liked (scroll to the bottom for the ML content).
My top four ML books I usually recommend are:
Hands-On Machine Learning with Scikit Learn and Tensorflow
Introduction to Statistical Learning: with Applications in R
Deep Learning by Ian Goodfellow
Neural Networks by Michael Nielsen (free online!)
All of these books are 400–500 pages long, with the first two being about statistical ML and the last two being about deep learning.
Grab these books and find your people. Look for places that other curious programmers are spending time. For me, that was Bradfield. The kind of person who spends 10–20 hours/week learning is exactly the kind of person I wanted to study with.
ML hack: find great ML papers to read and implement
The gold standard of ML competence is being able to implement most research papers (and even better, implement the entire paper in one day — and last week was my first time hitting that goal!).
To do this, you first have to find great ML papers. Follow people you admire on Twitter. And when you take ML courses, be sure to note that papers the classes mentions.
My favorite spot to find ML papers to read or implement is Andrej Karpathy’s Arxiv Sanity Perserver, which aggregates recently popular papers.
Another option for hunting down a great ML paper: pick a field you’re interested in (e.g., grounded language learning) and go on a targeted search to find a “survey paper” (a review of the literature on that topic). Then follow the citations to uncover the most foundational papers on the topic, and implement those.
ML hack: keep up with the speed of innovation
Be early, but not too early.
Based on the trajectory of the research community, I would recommend learning PyTorch over Tensorflow. There are some fancy new programming languages designed from the ground up for ML, but they’re too early. Stick to Python, the language of ML.
People love asking for my go-to blogs, so here are my top recommendations: distill.pub, thegradient.pub, inference.vc, blog.acolyer.org, openai.com’s blog, and ruder.io.
Distill.pub is far and away the best blog.
ML hack: perfect your working environment
I practice deep work. Or I try to.
Deep work is an extended state of flow where you are focusing intensely and not getting distracted. It’s easy to talk about but hard to achieve reliably (much like meditation). And though it’s always hard, you can make it easier if you design your environment properly.
My average work day is structured into two deep work blocks. I start my day around 9am with a 4-hour deep work block in the morning. I stop at lunch to eat and take meetings. And then have one more deep work block until the day is done. Caffeine helps to supercharge these blocks.
I was actually profiled in Cal Newport’s Deep Work and so people often ask me how to get to this flow state. You want the secrets? I try and block all distractions. I block my favorite websites. I prefer to read books instead of blogs, which trains my brain to focus longer. I block all notifications and put my phone in airplane mode. I work in places without internet, ideally outdoors. Whenever possible, I work on pen and paper. I keep bright lighting and find that a slightly colder working temperature can feel like an extra 50mg of caffeine. I listen to brain.fm — wordless music that’s the perfect tempo for focusing.
If I’m struggling to get started, I sometimes jumpstart things with a depth ritual. I use a Macbook Pro (if you’re on a PC, install Linux) and I’ve memorized dozens (hundreds?) of hotkeys. That last one isn’t relevant to deep work, I just really love hotkeys.
“You want the secrets? I try and block all distractions.”
How do I avoid people interrupting me? It’s helpful that deep work is a cultural value at my startup, so we batch all of our meetings into the middle of the day. Otherwise, I just wear big headphones.
I also find that working with someone else is a great way to stay in flow. I love pairing (and love it more than working alone).
ML hack: get an ML project done
Hackathons might not be a go-to place to find a job, but it’s a great place to work out an ML project. During my last hackathon, my three friends and I built AI Rock Band in just under 24 hours as part of Developer Week 2020.
Find a good starter project to build up your ML skills.
Aside from homework problems and implementing little pieces of neural nets (like the sigmoid function, softmax function, or backpropagation), I would recommend picking a project with friends and hacking it out. Pick something that’s in your daily life. Example: if you live with roommates, and there are always dirty dishes in the sink, you could build (with a webcam) an image classifying network, so that whenever someone leaves a dirty dish in the sink for longer than 3 hours, the WiFi shuts off!
ML hack: know your math
I come from a lineage that is notoriously bad at statistics. My grandfather failed his stats exam four times. My dad’s only B in college (nerd) was stats. And I got a C in stats in college — and I needed a C+ to pass.
But I wasn’t deterred. And now I’m essentially a statistician.
Linear algebra is key but all you need to get started is a four-hour YouTube series by 3blue1brown.
As for calculus, it’s nice to review it a little bit. You don’t use it a lot unless you’re doing ML research. The minimum: know enough math to not be afraid of all the symbols you see in research papers.
“Know enough math to not be afraid of all the symbols you see in research papers.”
Right now, I’m doing CS294 (Deep Unsupervised Learning by Pieter Abbeel) through Berkeley, all online. It’s a second-year grad school course with four homework assignments. Each homework involves implementing multiple papers. It’s really hard, but such a great exercise (particularly because you immediately know if you’re doing the right thing).
Realistically, you don’t need this level of mathematics to get your first job. You can become a MLE and just reuse pre-trained models (which are often packaged up as libraries on Github) or Scikit Learn for statistical ML (as long as you have at least one textbook’s worth of theoretical background).
ML hack: tell everyone you’re looking for a job
Once you get your foot in the door, you’ll steadily improve at ML.
But first, you have to get that foot in.
For me, it was helpful to achieve conversational competence in ML. Once you hit conversational competence, it’s easier to find a job. And you get there by learning the fundamentals with fast.ai or textbooks (see above), reading papers, and ideally producing 1–4 Anki flashcards per hour of learning. If you haven’t yet heard the Good News about spaced repetition, read this primer from Michael Nielsen.
“Once you hit conversational competence, it’s easier to find a job.”
After that, it’s important to network and be scrappy. People knew I was a competent software engineer, and I was willing to take a short-term contract. A friend of mine was starting an ML company, so I negotiated a 3-month contract to do some early ML work for them. Funny enough, that contract ended up being a great experience, and I’m still with them over two years later!
In machine learning, building up your credibility is important. And you can do that by posting your work on Medium (check out my articles on multimodal feature representations and CNNs for text classification), Twitter, Github, and LinkedIn.
I’ve also had friends leverage their ML learnings to transfer internally at their company (from a non-ML dev role to an MLE role) or found a startup.
The biggest takeaways here are: talk about it with friends, be open to a contracting gig, embrace networking, build up implementation proof online, and establish credibility. Finding an ML job comes down to: network effects, scrappiness, and credibility.
“Finding an ML job comes down to: network effects, scrappiness, and credibility.”
ML hack: know when to do a PhD and when to skip it
If you want to go into ML research, a PhD is going to help you a lot, especially a PhD from a top program. For becoming an MLE, a PhD isn’t necessary.
Evidence of being able to implement a paper or produce high-quality writing is the right credibility to shoot for as an MLE. It shows you understand the material.
A PhD is grueling but will give you a lot of time to do original research and a support structure for doing that research, which is important for getting a job as a researcher. So if you’re inspired by the research route after MLE work, (and aren’t turned off by a six-year commitment), consider a PhD.
The final ML hack: just get started!
Machine learning is a really useful skill, and it’s not too late to start learning. I’ve armed you with the right books, blogs, papers, classes, deep work, and job search hacks. And feel free to reach out and ask any additional questions.
Excited for you all to get started (you know, so I can hire you sooner).''',


"9":'''A Supercomputer Analyzed Covid-19 — and an Interesting New Theory Has Emerged
A closer look at the Bradykinin hypothesis
Thomas Smith
Thomas Smith
Sep 1·8 min read

3d rendering of multiple coronavirus.
Photo: zhangshuang/Getty Images
Earlier this summer, the Summit supercomputer at Oak Ridge National Lab in Tennessee set about crunching data on more than 40,
                000 genes from 17,
                000 genetic samples in an effort to better understand Covid-19. Summit is the second-fastest computer in the world, but the process — which involved analyzing 2.5 billion genetic combinations — still took more than a week.
When Summit was done, researchers analyzed the results. It was, in the words of Dr. Daniel Jacobson, lead researcher and chief scientist for computational systems biology at Oak Ridge, a “eureka moment.” The computer had revealed a new theory about how Covid-19 impacts the body: the bradykinin hypothesis. The hypothesis provides a model that explains many aspects of Covid-19, including some of its most bizarre symptoms. It also suggests 10-plus potential treatments, many of which are already FDA approved. Jacobson’s group published their results in a paper in the journal eLife in early July.
According to the team’s findings, a Covid-19 infection generally begins when the virus enters the body through ACE2 receptors in the nose, (The receptors, which the virus is known to target, are abundant there.) The virus then proceeds through the body, entering cells in other places where ACE2 is also present: the intestines, kidneys, and heart. This likely accounts for at least some of the disease’s cardiac and GI symptoms.
(Sign up for Your Coronavirus Update, a biweekly newsletter with the latest news, expert advice, and analysis to keep you safe)
But once Covid-19 has established itself in the body, things start to get really interesting. According to Jacobson’s group, the data Summit analyzed shows that Covid-19 isn’t content to simply infect cells that already express lots of ACE2 receptors. Instead, it actively hijacks the body’s own systems, tricking it into upregulating ACE2 receptors in places where they’re usually expressed at low or medium levels, including the lungs.
In this sense, Covid-19 is like a burglar who slips in your unlocked second-floor window and starts to ransack your house. Once inside, though, they don’t just take your stuff — they also throw open all your doors and windows so their accomplices can rush in and help pillage more efficiently.
The renin–angiotensin system (RAS) controls many aspects of the circulatory system, including the body’s levels of a chemical called bradykinin, which normally helps to regulate blood pressure. According to the team’s analysis, when the virus tweaks the RAS, it causes the body’s mechanisms for regulating bradykinin to go haywire. Bradykinin receptors are resensitized, and the body also stops effectively breaking down bradykinin. (ACE normally degrades bradykinin, but when the virus downregulates it, it can’t do this as effectively.)
The end result, the researchers say, is to release a bradykinin storm — a massive, runaway buildup of bradykinin in the body. According to the bradykinin hypothesis, it’s this storm that is ultimately responsible for many of Covid-19’s deadly effects. Jacobson’s team says in their paper that “the pathology of Covid-19 is likely the result of Bradykinin Storms rather than cytokine storms,” which had been previously identified in Covid-19 patients, but that “the two may be intricately linked.” Other papers had previously identified bradykinin storms as a possible cause of Covid-19’s pathologies.
Covid-19 is like a burglar who slips in your unlocked second-floor window and starts to ransack your house.
As bradykinin builds up in the body, it dramatically increases vascular permeability. In short, it makes your blood vessels leaky. This aligns with recent clinical data, which increasingly views Covid-19 primarily as a vascular disease, rather than a respiratory one. But Covid-19 still has a massive effect on the lungs. As blood vessels start to leak due to a bradykinin storm, the researchers say, the lungs can fill with fluid. Immune cells also leak out into the lungs, Jacobson’s team found, causing inflammation.
Coronavirus May Be a Blood Vessel Disease, Which Explains Everything
Many of the infection’s bizarre symptoms have one thing in common
elemental.medium.com
And Covid-19 has another especially insidious trick. Through another pathway, the team’s data shows, it increases production of hyaluronic acid (HLA) in the lungs. HLA is often used in soaps and lotions for its ability to absorb more than 1,
                000 times its weight in fluid. When it combines with fluid leaking into the lungs, the results are disastrous: It forms a hydrogel, which can fill the lungs in some patients. According to Jacobson, once this happens, “it’s like trying to breathe through Jell-O.”
This may explain why ventilators have proven less effective in treating advanced Covid-19 than doctors originally expected, based on experiences with other viruses. “It reaches a point where regardless of how much oxygen you pump in, it doesn’t matter, because the alveoli in the lungs are filled with this hydrogel,” Jacobson says. “The lungs become like a water balloon.” Patients can suffocate even while receiving full breathing support.
The bradykinin hypothesis also extends to many of Covid-19’s effects on the heart. About one in five hospitalized Covid-19 patients have damage to their hearts, even if they never had cardiac issues before. Some of this is likely due to the virus infecting the heart directly through its ACE2 receptors. But the RAS also controls aspects of cardiac contractions and blood pressure. According to the researchers, bradykinin storms could create arrhythmias and low blood pressure, which are often seen in Covid-19 patients.
The bradykinin hypothesis also accounts for Covid-19’s neurological effects, which are some of the most surprising and concerning elements of the disease. These symptoms (which include dizziness, seizures, delirium, and stroke) are present in as many as half of hospitalized Covid-19 patients. According to Jacobson and his team, MRI studies in France revealed that many Covid-19 patients have evidence of leaky blood vessels in their brains.
Bradykinin — especially at high doses — can also lead to a breakdown of the blood-brain barrier. Under normal circumstances, this barrier acts as a filter between your brain and the rest of your circulatory system. It lets in the nutrients and small molecules that the brain needs to function, while keeping out toxins and pathogens and keeping the brain’s internal environment tightly regulated.
If bradykinin storms cause the blood-brain barrier to break down, this could allow harmful cells and compounds into the brain, leading to inflammation, potential brain damage, and many of the neurological symptoms Covid-19 patients experience. Jacobson told me, “It is a reasonable hypothesis that many of the neurological symptoms in Covid-19 could be due to an excess of bradykinin. It has been reported that bradykinin would indeed be likely to increase the permeability of the blood-brain barrier. In addition, similar neurological symptoms have been observed in other diseases that result from an excess of bradykinin.”
Increased bradykinin levels could also account for other common Covid-19 symptoms. ACE inhibitors — a class of drugs used to treat high blood pressure — have a similar effect on the RAS system as Covid-19, increasing bradykinin levels. In fact, Jacobson and his team note in their paper that “the virus… acts pharmacologically as an ACE inhibitor” — almost directly mirroring the actions of these drugs.
Medium Coronavirus Blog
A real-time resource for Covid-19 news, advice, and commentary.
coronavirus.medium.com
By acting like a natural ACE inhibitor, Covid-19 may be causing the same effects that hypertensive patients sometimes get when they take blood pressure–lowering drugs. ACE inhibitors are known to cause a dry cough and fatigue, two textbook symptoms of Covid-19. And they can potentially increase blood potassium levels, which has also been observed in Covid-19 patients. The similarities between ACE inhibitor side effects and Covid-19 symptoms strengthen the bradykinin hypothesis, the researchers say.
ACE inhibitors are also known to cause a loss of taste and smell. Jacobson stresses, though, that this symptom is more likely due to the virus “affecting the cells surrounding olfactory nerve cells” than the direct effects of bradykinin.
Though still an emerging theory, the bradykinin hypothesis explains several other of Covid-19’s seemingly bizarre symptoms. Jacobson and his team speculate that leaky vasculature caused by bradykinin storms could be responsible for “Covid toes,” a condition involving swollen, bruised toes that some Covid-19 patients experience. Bradykinin can also mess with the thyroid gland, which could produce the thyroid symptoms recently observed in some patients.
The bradykinin hypothesis could also explain some of the broader demographic patterns of the disease’s spread. The researchers note that some aspects of the RAS system are sex-linked, with proteins for several receptors (such as one called TMSB4X) located on the X chromosome. This means that “women… would have twice the levels of this protein than men,” a result borne out by the researchers’ data. In their paper, Jacobson’s team concludes that this “could explain the lower incidence of Covid-19 induced mortality in women.” A genetic quirk of the RAS could be giving women extra protection against the disease.
The bradykinin hypothesis provides a model that “contributes to a better understanding of Covid-19” and “adds novelty to the existing literature,” according to scientists Frank van de Veerdonk, Jos WM van der Meer, and Roger Little, who peer-reviewed the team’s paper. It predicts nearly all the disease’s symptoms, even ones (like bruises on the toes) that at first appear random, and further suggests new treatments for the disease.
As Jacobson and team point out, several drugs target aspects of the RAS and are already FDA approved to treat other conditions. They could arguably be applied to treating Covid-19 as well. Several, like danazol, stanozolol, and ecallantide, reduce bradykinin production and could potentially stop a deadly bradykinin storm. Others, like icatibant, reduce bradykinin signaling and could blunt its effects once it’s already in the body.
Interestingly, Jacobson’s team also suggests vitamin D as a potentially useful Covid-19 drug. The vitamin is involved in the RAS system and could prove helpful by reducing levels of another compound, known as REN. Again, this could stop potentially deadly bradykinin storms from forming. The researchers note that vitamin D has already been shown to help those with Covid-19. The vitamin is readily available over the counter, and around 20% of the population is deficient. If indeed the vitamin proves effective at reducing the severity of bradykinin storms, it could be an easy, relatively safe way to reduce the severity of the virus.
Other compounds could treat symptoms associated with bradykinin storms. Hymecromone, for example, could reduce hyaluronic acid levels, potentially stopping deadly hydrogels from forming in the lungs. And timbetasin could mimic the mechanism that the researchers believe protects women from more severe Covid-19 infections. All of these potential treatments are speculative, of course, and would need to be studied in a rigorous, controlled environment before their effectiveness could be determined and they could be used more broadly.
Covid-19 stands out for both the scale of its global impact and the apparent randomness of its many symptoms. Physicians have struggled to understand the disease and come up with a unified theory for how it works. Though as of yet unproven, the bradykinin hypothesis provides such a theory. And like all good hypotheses, it also provides specific, testable predictions — in this case, actual drugs that could provide relief to real patients.
The researchers are quick to point out that “the testing of any of these pharmaceutical interventions should be done in well-designed clinical trials.” As to the next step in the process, Jacobson is clear: “We have to get this message out.” His team’s finding won’t cure Covid-19. But if the treatments it points to pan out in the clinic, interventions guided by the bradykinin hypothesis could greatly reduce patients’ suffering — and potentially save lives.''',


"10":'''Remote Work Is Killing the Hidden Trillion-Dollar Office Economy
From airlines to Starbucks, a massive part of our economy hinges on white-collar workers returning to the office
Steve LeVine
Steve LeVine
Sep 1·9 min read

Image for post
Illustration: Mark Wang
For a decade, Carlos Silva has been gluing, nailing, and re-zippering shoes and boots at Stern Shoe Repair, a usually well-trafficked shop just outside the Metro entrance at Union Station in Washington, D.C. On a typical day, he would arrive at 7 a.m. and stay until 8 p.m., serving the crowds of professionals shuttling by on their way to work. But since the near-shutdown of office work and train travel, he has been closing the shop at 4 p.m. “There is no traffic, my friend. The whole station is dead,” says Silva. “Now it’s only a part-time job.”
In the five months since the coronavirus forced a lockdown of U.S. businesses, economists have focused much attention on the devastation of mom-and-pop businesses, brick-and-mortar shops, bars and restaurants, and massive chains. But they have mostly overlooked a looming threat to a vastly larger and more consequential galaxy of businesses, one worth trillions of dollars a year in GDP and revolving around a single, much underappreciated economic actor — the white-collar office worker.
As companies in cities across the U.S. postpone and even scrap plans to reopen their offices, they have transformed once-teeming city business districts into commercial ghost towns comprised of essentially vacant skyscrapers and upscale complexes. A result has been the paralysis of the rarely remarked-upon business ecosystem centering on white-collar workers, who, when you include the enterprises reliant on them, account for a pre-pandemic labor force approaching 100 million workers.
Austin Was Destined to Replace Silicon Valley. Then the Pandemic Hit
Can the hottest boomtown off the coasts survive a recession—and a Covid surge?
marker.medium.com
These workers shopped at small businesses like Silva’s shoe repair shop: dry cleaners, gyms, food carts, florists, and pharmacies. But they were also among the most vital customers and source of revenue for a slew of larger, less obvious businesses — food delivery companies like Grubhub and Uber Eats, and companies like Xerox, the maker of printing supplies. Amid Covid-19, workwear destinations Brooks Brothers and J.Crew have filed for bankruptcy protection, with Brooks Brothers selling itself last month. And, on its quarterly earnings call in late July, Starbucks attributed the loss of some $2 billion year on year to deserted urban office corridors. Starting off their day at home, remote workers are simply not queueing up in the same numbers for a morning venti latte.
It will save these companies leasing costs and their employees their commutes, but at what cost to the rest of the economy?
Meanwhile, in the air, white-collar workers previously kept a parallel economy buzzing, with business travel accounting for 60% to 70% of all airline revenue. While leisure getaways have also been obliterated, it turns out the bigger punch is the Zoomification of business meetings, a cancellation of business travel that analysts expect to persist for up to two or three years.
And the move to remote work doesn’t show signs of stopping anytime soon. In recent months, many companies, including JPMorgan Chase, Ford Motor, Twitter, and REI have announced some version of a long-term or permanent work-from-home future. On Friday, Pinterest turned heads when it announced it would pay a $89.5 million contract penalty to cancel its lease on a flashy new 490,
                000-square-foot office building planned in San Francisco, citing a permanent shift to remote work. The pandemic has convinced these and other companies that their employees can perform their jobs, perhaps even more productively, at home, allowing a massive shrinkage of corporate America’s physical office footprint. It will save these companies leasing costs and their employees their commutes, but at what cost to the rest of the economy?
White-collar workers and coffee have been intertwined since the caffeinated beverage arrived in Europe in the early 17th century. Within just a few decades, some 300 coffeehouses had sprung up in London to serve merchants of all types, brokers, and others doing business nearby. It was the same in Austria, France, Germany, Holland, and Italy. The fledgling office economy had been born.
Of course, “office work” didn’t start with the Enlightenment, nor in an office — Roman scribes kept records in public squares bound by government offices and shops. But two centuries later, the fully integrated white-collar office became a necessity with the colossal economic boom of the Industrial Revolution. Enabled by a slew of late-19th-century inventions — the skyscraper, the internal combustion engine, and the electrification of lighting, elevators, and underground trains — workers could leave relatively distant homes for the city, and stay comfortably once they got there.
But who would maintain all this new machinery? If they were no longer lunching at home, what and where would all these workers eat? And wouldn’t they need serious sartorial services since they would now be frequenting each other’s offices every working day of the year? So it was that, around the world, cities saw the rise of a new age of immense yet compact office-centered economies.
Office-dwelling road warriors — a primary profit center for the travel industry — are now homebound Zoomers, resulting in a bloodbath for airlines and hotels.
But now, suggests MIT economist David Autor in a paper last month, the office economy is under threat. The pandemic, he and his co-author, Elisabeth Reynolds, a lecturer at MIT, write, has made a permanent shift to remote work for a large part of the office workforce a near certainty. And with that, tens of thousands of workers in the office support economy — those who “feed, transport, clothe, entertain, and shelter people when they are not in their own homes” — will lose their jobs.
The implications for the office economy are stark. Office-dwelling road warriors — a primary profit center for the travel industry — are now homebound Zoomers, resulting in a bloodbath for airlines and hotels. Business travel in July was down 97% from a year earlier, the Wall Street Journal reported, and an estimated $2 trillion in corporate travel will not happen this year. Last week, American Airlines said it will eliminate service to 15 cities in October, thus reducing its flying capacity by 55%, and that, unless it receives additional bailout cash from the government, it will furlough and lay off some 19,
                000 workers, about a third of its staff. Delta says it will furlough 1,
                941 pilots if it can’t get more money as well. In August, Virgin Atlantic outright filed for bankruptcy. In the longer term, current and former airline executives say the shift in office culture to Zoom means the decline in corporate passengers is likely to be permanent.
The travel pain is broad. The hotels that typically cater to business travelers are in a crisis, with some poised for bankruptcy. As of July,
                23.4% of mortgage-backed loans extended to hotels were delinquent at least 30 days, amounting to $20.6 billion. That compares with $1.15 billion in pre-pandemic delinquent loans, and $13.5 billion at the peak of the 2008 recession. Last month, in a letter to Congress, hundreds of hoteliers, led by the American Hotel and Lodging Association, asked for forbearance on the debt. In early August, Marriott reported its worst loss ever in the second quarter, and MGM Resorts on Friday laid off 18,
                000 workers, a quarter of its pre-pandemic workforce.
Meanwhile, a less conspicuous victim of the remote revolution is companies such as Xerox, whose revenue fell 34.6% last quarter as many offices locked down and did not proceed with planned or possible equipment purchases. The lockdown also caused a 45% drop in quarterly revenue for Aramark, which provides food catering to big sports stadiums, schools, and offices. At 3M, too, for whom a sizable chunk of sales are to industries reliant on the office economy, sales fell 13% in the second quarter year on year. One culprit was the hit to airlines, which cut into 3M’s bread-and-butter abrasives and adhesives business, and a 25% plunge in demand for supplies such as Scotch tape and Post-it notes, perhaps the most iconic signifiers of the corporate workplace.
The shift in the office ecosystem is rattling the status quo in some of the most expensive cities known for potent and prestigious white-collar jobs. A conspicuous example is real estate markets. Untethered from the office, many workers are electing to leave. In an August 19 note to clients, Goldman Sachs said that droves of people are leaving New York in search of much cheaper and more spacious digs in the Carolinas, Georgia, and Florida. In Manhattan, the flight has created double the apartment vacancies of a year ago, at about 13,
                000 in July, and an average 6.1% drop in rents, the largest decrease in nine years, according to a report by Miller Samuel, a real estate appraiser. Tech and other white-collar workers are fleeing San Francisco, too, where rents for one- and two-bedroom apartments are down by 11% from last year, according to Zumper, an apartment listing site.
This flight is visible in smaller cities too, particularly in the restaurants that relied on lunch and cocktail hour traffic from the sprawling offices. Dan Georges, the owner of Lexi’s on Third, a New York-style deli in downtown Columbus, Ohio, says he has lost around half his business to Zoomification. Prior to Covid-19, Lexi’s buzzed with business from Chase Tower, the 25-story office building in which it’s located. But since March, the building has been all but empty, and now he relies on business from hard-hats working on nearby construction sites and longtime loyal customers from the suburbs. He knows that some or many of his regular white-collar clientele will not return once the pandemic has passed, but hopes Lexi’s will survive based on its quality and prices. Other restaurants will close, he says.
How Remote Work Could Destroy Silicon Valley
The tech industry is built on serendipity. If workers flee the Bay Area, what’s left?
marker.medium.com
This is the scenario in downtowns across the country. Goldman Sachs says that the number of seated diners across the country was down by 54% the week ending August 16 compared with the prior week. In New York, more than 1,
                200 restaurants are closed permanently, and analysts estimate that a third of the city’s small businesses as a whole may be shut for good.
The problem is so big that it is imperiling the economies of the cities themselves. The pandemic, MIT’s Autor and Reynolds write, will bring “a decline of the economic centrality, and even the cultural vitality, of cities.” According to a survey by the National League of Cities,
                90% of cities expect an average 13% decline in revenue next year — mostly income and sales taxes, the revenue associated with white-collar workers. It’s the highest decline in the survey since the financial crash. Houston, for instance, had a 13% drop in sales tax in May,
                17% in April, and 10% in March. “This has been a 50-state natural disaster of sorts,” says Mark Hamrick, chief economist at Bankrate, “where the buildings have been left standing and largely vacant.”
Yet the implosion of the office economy is not necessarily a black-and-white story of ruination. The resilience of cities is a pillar of economic history. Wars, economic downturns, and catastrophic natural disasters have come and gone, but very few major cities have outright disappeared or even been permanently held down. On the contrary, most have revived themselves in much the same economic and demographic shape as before their respective crises.
Regardless of the length of the recovery, it looks likely that airlines and hotels will have to shrink, die, or reinvent. And, in a profound forced makeover, the cities will have to reimagine themselves as well.
In World War II, the U.S. firebombed Tokyo and other major Japanese cities, obliterating much of the economy. But within about a decade and a half, most had essentially recovered, and in another 15 or so years, local companies and workforces were challenging the U.S. for the commanding heights of key global industries like automobiles and electronics. In an influential 2002 paper, Donald Davis and David Weinstein, both professors at Columbia University, said the Japanese recovery showed that long-lived cities undergoing great temporary shock tend to bounce back. Such cities, Davis and Weinstein asserted, have an almost innate persistence that confounds outside shocks.
Of course,
                15 years is a long recovery, a protracted period that would have its own devastating and irreversible impact on a generation of entrepreneurs and many of the workers employed by them. Regardless of the length of the recovery, it looks likely that airlines and hotels will have to shrink, die, or reinvent. And, in a profound forced makeover, the cities will have to reimagine themselves as well, with a severe potential hit to years of national GDP for the country as a whole.
But even if offices do not reopen at their same scale, many of their white-collar workers can move to less expensive places, notes Lee Branstetter, an economics professor at Carnegie Mellon. That will relieve congestion and reduce office and housing rents in so-called superstar cities like New York, San Francisco, and Boston. Businesses and middle-class white-collar workers currently priced out of these markets could then afford to live there. Many current restaurants, bars, pharmacies, and dry cleaners may not survive, but others would replace them, targeting this different clientele — perhaps “less shi shi,” Branstetter said. “But definitely not emptying out. And that doesn’t sound like the end of the world.”''',


"11":'''We Don’t Know How to Warn You Any Harder. America is Dying.
We Survivors of Authoritarianism Have a Message America Needs to Hear: This is Exactly How it Happens, and It’s Happening Here.
umair haque
umair haque
Follow
Aug 29 · 11 min read



The Trump Family Looming in front of the White House after the final night of the RNC
Source: Evan Vucci
Right about now, something terrible is happening in America. Society is one tiny step away from the final collapse of democracy, at the hands of a true authoritarian, and his fanatics. Meanwhile, America’s silent majority is still slumbering at the depth and gravity of the threat.
I know that strikes many of you as somehow wrong. So let me challenge you for a moment. How much experience do you really have with authoritarianism? Any? If you’re a “real” American, you have precisely none.
Take it from us survivors and scholars of authoritarianism. This is exactly how it happens. The situation could not — could not — be any worse. The odds are now very much against American democracy surviving.
If you don’t believe me, ask a friend. I invite everyone who’s lived under authoritarianism to comment. Those of us how have?
We survivors of authoritarianism have a terrible, terrible foreboding, because we are experiencing something we should never do: deja vu. Our parents fled from collapsing societies to America. And here, now, in a grim and eerie repeat of history, we see the scenes of our childhoods played out all over again. Only now, in the land that we came to. We see the stories our parents recounted to us happening before our eyes, only this time, in the place they brought us to, to escape from all those horrors, abuses, and depredations.
We survivors are experiencing this terrible feeling of deja vu right now as a group, as a class. We talk about it, how eerie and grim this sense of deja vu is. It’s happening all over again! Do you remember this part of your childhood? When the armed men roamed the streets? When the secret police disappeared opponents? When the fascist masses united — and that was enough to destroy democracy for good? We talk about it, believe me — but you don’t hear it because we have no real voice. America’s pundits are named Chris and Jake and Tucker. They are not named Eduardo and Ravi and Xiao and Umair. But Chris and Jake and Tucker can’t help you now. They don’t know what the hell they’re dealing with. They literally have no idea because they have no experience whatsoever.
The only people who do right now in America are us survivors. Let me remind you, by the way, what happens we speak out: we lose whatever credibility and status we have. The moment I began to warn of this, I lost my column in HBR, my cable news appearances, and so forth. Don’t cry for me. Understand me, my friend, know me. If we had a voice, we survivors, we would be warning you as loudly and strongly as we possibly could.
All of us. We would say:
This is not a joke. This is not a drill. When we survivors of authoritarianism experience, as a group, a class, a cohort, something that we never, ever should — the horrific deja vu that the horrors of our childhoods, that our parents knew, are happening, all over again, here, something is much, much more wrong than you know.
Now let me make all the above concrete. I am going to use the example of Kenosha to draw out things that perhaps only we survivors can see — or at least that we see first and easiest. Things that the “real” American is either still playing dumb about, or is still mum about, and both equate to the same thing: silence, which is complicity, in times like these.
When we look at Kenosha, we survivors, and you “real” Americans, do we see the same thing? Do we feel the same gravity, pain, urgency? You will have to tell me. Here is what I see, that I’m 100% sure every survivor sees — but I doubt “real” Americans fully see yet.
What happened there? A young man was radicalized by the movement that fascist President led. The fascist President spoke of hated minorities as animals and vermin. He led his faithful in chants of hate, moments that built the bond of the tribe between them. Soon enough, that President was speaking of peaceful protesters as anarchists and revolutionaries and seditionaries. And the question that the fascist raises was left hanging in the air. “My people, my flock — what do we do with traitors?”
The answer, to a young man like that, is what it was in Nazi Germany, in the Islamic World, in every fascist collapse since time began. We kill them. So off he went with his rifle — and killed innocent people. Perfectly innocent people.
There is a crucial lesson there. America already has an ISIS, a Taliban, an SS waiting to be born. A group of young men willing to do violence at the drop of a hat, because they’ve been brainwashed into hating. The demagogue has blamed hated minorities and advocates of democracy and peace for those young men’s stunted life chances, and they believe him. That’s exactly what an ISIS is, what a Taliban is, what an SS is. The only thing left to do by an authoritarian is to formalize it.
But when radicalized young men are killing people they have been taught to hate by demagogues right in the open, on the streets — a society has reached the beginnings of sectarian violence, the kind familiar in the Islamic world, and is at the end of democracy’s road.
How did the state’s law enforcement respond? In America, they’re simply called “the police.” They let him do it, and then they protected him. The killer was only brought to justice because there was a national outcry after the act was caught on video. If none of that had happened, he probably would never have been. The police were forced to act, in other words.
What do we survivors see in that tiny parable? Crucial institutions have already been captured by the extremist factions who stand against democracy. Do all those cops think of themselves as fascists? Of course they don’t. So what? Mullahs don’t think of themselves as hate preachers, either. What else do you call someone who gives a violent young man with a gun a free pass to kill people, though? Someone who tries to shield him after the murder? A good and decent person?
The police in America might not all think they are fascists. Certainly, not all of them are. But what is certain is that some significant number of them are captured. They are sympathetic to the forces which are now attacking democracy. They prioritize those forces over democracy, freedom, peace, justice.
Let me give you an example. My friend Ben is a London copper. He abhors the violence in America. His jaw is dropped by it. He rejects carrying a gun, or even a taser. Do you see how big the gap, the problem is?
If the police force is captured by the extremists — at least many police forces, it seems, then harder questions are raised. What about the armed forces?
They’re democracy’s last line of protection. What happens when a Trump, a Saddam, a Gaddafi, refuses to leave office? The military must remove them — or if it doesn’t, it becomes their plaything. That game of brinksmanship is exactly how Saddams and Gaddafis capture militaries. By daring them to, and when they don’t — bang! — their back is broken.
That’s another thing we survivors see very clearly right now, but “real” Americans might not. The capture of a police force is not just the capture of a police force. It threatens the whole fabric of a democracy. The monopoly on violence that the people’s agents should have is being transferred to the authoritarian. Why else would police forces beat people on the streets? Give hateful young men a free pass to kill people?
It all points to the beginnings of true violence, not just at the hands of the radicals — but aided and abetted by the state. That is the point at which a democracy finishes collapsing — and never comes back. Because once the state is free to do real violence — who is going to protest? Speak out? Even criticize?
Let me make that point crystal clear, by continuing my example. What happened next in Kenosha?
Trump threatened to send in “federal agents” — and then he did. Which “federal agents”? The ones he used just a few weeks ago, in Portland. The “Homeland Security” force which has become the precise equivalent of his Irani Republican Guard or SS: a paramilitary which isn’t accountable to the people, any democratic institution, wears no badges, can’t be identified, and is controlled only by the authoritarian, at his discretion and whim.
What did Trump’s stormtroopers do in Kenosha? They disappeared people, just like in Portland. They simply picked groups of people, roared up in unmarked cars, and…abducted them. To where? To jails. For what reason? For no reason — there were no warrants involved, no due process, no Constitutionality whatsoever. People were simply made to vanish. Like in the Soviet Union. Like in Saddam’s Iraq or Gaddafi’s Libya. Like in Nazi Germany.
Again, the “real” American will think I’m exaggerating at this point, so let me say it again. This is what more or less every survivor of authoritarianism thinks, not just me. The only people who don’t think, who still dismiss these comparisons as alarmist are the ones who have never experienced authoritarianism. Those of us who have? We know that abductions by paramilitaries in unmarked cars at the whim of a tyrant are really, really bad.
Why? They point to the complete breakdown of the rule of law. The rule of law only means something when an authoritarian can’t simply disappear people from the streets, ordering his paramilitary to do it, ignoring the constitution, discarding due process — with total impunity. But all that is exactly what Trump can do.
He now has the nascent powers of a Gaddafi or a Saddam. No, I’m not kidding. He doesn’t have the full powers, to be sure — but he certainly has the beginnings of them. Maybe he can’t have people tortured in jail yet — but he can have almost anyone he likes in America picked up and disappeared.
So how far away do you think even worse abuses of power are? When a tyrant can have almost anyone in a country they like disappeared, how far away do you really think torture is? Rape? Murder? I’m not being hyperbolic. I’m trying to speak to you like an adult. Will you listen?
Let me finish my story of Kenosha, then, before the reality of authoritarianism overwhelms us both.
What happened next?
Nothing.
There was a deafening silence. America’s intellectuals and pundits didn’t say authoritarianism, didn’t say fascism — again. America’s good cops didn’t exactly stand up for democracy. America’s generals didn’t assure the nation they’d intervene. America’s people didn’t wake up.
What happened after an authoritarian showed he had the power to have people disappeared — people who protested the killing of innocents which itself was inspired by the authoritarian, at the hands of a young radicalized man — was…
Nothing.
People didn’t pour into the streets of the capitol, by the millions. The nation’s intellectuals and columnists didn’t call for the head of state’s resignation. The opposition didn’t immediately start a global movement to observe these abuses of power.
Nothing happened.
And so the predictable is really what happened.
The authoritarian’s numbers rose in the polls. That is because there is always some significant number of people who respond to violence, brutality, hate. Unless they are reminded, sternly, forcefully, that there is something better. That this is not who we must be. That this is the wrong path.
In America, that is not happening. Not nearly enough to fight authoritarianism, and win. That’s not my opinion: it’s a factual reality. Trump is rising in the polls, and is now at the point where the slightest secret hate vote — all those polite soccer moms who say they’d never vote for him, and then do, in the heat of the voting booth — will give him an outright victory. He won’t even have to contest a loss, as he’s sure to do. He will just win.
And then American democracy will be over.
Because the last and final thing we survivors of democracy know is that truly terrible things are on the way then. Yes, really. Men who can put kids in cages and radicalize younger men to do real violence? They don’t want you to live in peace, freedom, harmony, and goodness. They want you to live in fear, despair, and terror. And they will begin using extreme violence to do it.
A second Trump term? It will involve all of the following. Shock troops on the streets. Disappearances becoming everyday events. Critics and dissidents being tortured in hidden jails. Expression and thought being monitored for any negative portrayal of the fascists. Hated minorities institutionally dehumanized and resegregated. It will involve levels of such horrific violence and brutality that Americans still cannot understand or grasp precisely because they have been lucky enough to have never yet personally experienced them.
So leave it to us. We survivors. We dispossessed ones. The exiles and orphans of modernity. The ones who have never felt like we belonged. The gift we always could have given you was to protect you from this. But even the good Americans never gave us room as true equals in their promised land. That is how America got here. By never letting us in, even though we were here. We could have told you how it happens, and what “it” means.
But it is not too late to listen to us.
This is your last chance to hear our warning.
It is happening here. Exactly — exactly — the way it happened there, to us. In our childhoods, to our parents, in all those distant, strange broken lands. This is how a democracy dies. This is how it all collapses. This is how the fanatics seize power for a generation or more. This is how the fascists win.
Kenosha. Portland. Washington, DC.
This is how it happens. We survivors feel a sense of deja vu right now terrible that most of us can’t sleep, can’t focus, can’t…breathe, sometimes. I want you to understand how powerful this feeling of deja vu is. It is one of the most frightening things we survivors have experienced. Where will we go now? What will we do now? America never really accepted us, and now, it’s collapsing. That leaves us in a worse place than anyone else, really. We feel the price of this implosion acutely. That is one reason we try to warn you — but the other one is that we can’t not warn you. Nobody — nobody — should live through the horrors we knew as children, as parents, as human beings.
Never again. It’s the vow every survivor makes. That’s why we are trying to warn you. It is happening all over again, here, exactly — exactly, precisely, absolutely — the way that we saw it happen before, and before, and before.
Hear our warning. None of us have the time left now for petty divisions, intellectualizations, the games pundits play, the way I lost my column when I began to warn of all this. I didn’t pay the bigger price — you did.
You don’t have another mistake left to make.
This is it, and you’re blowing it, sleepwalking into collapse, letting the fascists steal your futures.
Do not let it happen here.
Umair
August 2020''',


"12":'''Editor’s Note: Surveillance capitalism is everywhere. But it’s not the result of some wrong turn or a rogue abuse of corporate power — it’s the system working as intended. This is the subject of Cory Doctorow’s new book, which we’re thrilled to publish in whole here on OneZero. This is how to destroy surveillance capitalism.
The net of a thousand lies
The most surprising thing about the rebirth of flat Earthers in the 21st century is just how widespread the evidence against them is. You can understand how, centuries ago, people who’d never gained a high-enough vantage point from which to see the Earth’s curvature might come to the commonsense belief that the flat-seeming Earth was, indeed, flat.
But today, when elementary schools routinely dangle GoPro cameras from balloons and loft them high enough to photograph the Earth’s curve — to say nothing of the unexceptional sight of the curved Earth from an airplane window — it takes a heroic effort to maintain the belief that the world is flat.
Likewise for white nationalism and eugenics: In an age where you can become a computational genomics datapoint by swabbing your cheek and mailing it to a gene-sequencing company along with a modest sum of money, “race science” has never been easier to refute.
We are living through a golden age of both readily available facts and denial of those facts. Terrible ideas that have lingered on the fringes for decades or even centuries have gone mainstream seemingly overnight.
When an obscure idea gains currency, there are only two things that can explain its ascendance: Either the person expressing that idea has gotten a lot better at stating their case, or the proposition has become harder to deny in the face of mounting evidence. In other words, if we want people to take climate change seriously, we can get a bunch of Greta Thunbergs to make eloquent, passionate arguments from podiums, winning our hearts and minds, or we can wait for flood, fire, broiling sun, and pandemics to make the case for us. In practice, we’ll probably have to do some of both: The more we’re boiling and burning and drowning and wasting away, the easier it will be for the Greta Thunbergs of the world to convince us.
The arguments for ridiculous beliefs in odious conspiracies like anti-vaccination, climate denial, a flat Earth, and eugenics are no better than they were a generation ago. Indeed, they’re worse because they are being pitched to people who have at least a background awareness of the refuting facts.
Anti-vax has been around since the first vaccines, but the early anti-vaxxers were pitching people who were less equipped to understand even the most basic ideas from microbiology, and moreover, those people had not witnessed the extermination of mass-murdering diseases like polio, smallpox, and measles. Today’s anti-vaxxers are no more eloquent than their forebears, and they have a much harder job.
So can these far-fetched conspiracy theorists really be succeeding on the basis of superior arguments?
Some people think so. Today, there is a widespread belief that machine learning and commercial surveillance can turn even the most fumble-tongued conspiracy theorist into a svengali who can warp your perceptions and win your belief by locating vulnerable people and then pitching them with A.I.-refined arguments that bypass their rational faculties and turn everyday people into flat Earthers, anti-vaxxers, or even Nazis. When the RAND Corporation blames Facebook for “radicalization” and when Facebook’s role in spreading coronavirus misinformation is blamed on its algorithm, the implicit message is that machine learning and surveillance are causing the changes in our consensus about what’s true.
After all, in a world where sprawling and incoherent conspiracy theories like Pizzagate and its successor, QAnon, have widespread followings, something must be afoot.
But what if there’s another explanation? What if it’s the material circumstances, and not the arguments, that are making the difference for these conspiracy pitchmen? What if the trauma of living through real conspiracies all around us — conspiracies among wealthy people, their lobbyists, and lawmakers to bury inconvenient facts and evidence of wrongdoing (these conspiracies are commonly known as “corruption”) — is making people vulnerable to conspiracy theories?
If it’s trauma and not contagion — material conditions and not ideology — that is making the difference today and enabling a rise of repulsive misinformation in the face of easily observed facts, that doesn’t mean our computer networks are blameless. They’re still doing the heavy work of locating vulnerable people and guiding them through a series of ever-more-extreme ideas and communities.
Belief in conspiracy is a raging fire that has done real damage and poses real danger to our planet and species, from epidemics kicked off by vaccine denial to genocides kicked off by racist conspiracies to planetary meltdown caused by denial-inspired climate inaction. Our world is on fire, and so we have to put the fires out — to figure out how to help people see the truth of the world through the conspiracies they’ve been confused by.
But firefighting is reactive. We need fire prevention. We need to strike at the traumatic material conditions that make people vulnerable to the contagion of conspiracy. Here, too, tech has a role to play.
There’s no shortage of proposals to address this. From the EU’s Terrorist Content Regulation, which requires platforms to police and remove “extremist” content, to the U.S. proposals to force tech companies to spy on their users and hold them liable for their users’ bad speech, there’s a lot of energy to force tech companies to solve the problems they created.
There’s a critical piece missing from the debate, though. All these solutions assume that tech companies are a fixture, that their dominance over the internet is a permanent fact. Proposals to replace Big Tech with a more diffused, pluralistic internet are nowhere to be found. Worse: The “solutions” on the table today require Big Tech to stay big because only the very largest companies can afford to implement the systems these laws demand.
Figuring out what we want our tech to look like is crucial if we’re going to get out of this mess. Today, we’re at a crossroads where we’re trying to figure out if we want to fix the Big Tech companies that dominate our internet or if we want to fix the internet itself by unshackling it from Big Tech’s stranglehold. We can’t do both, so we have to choose.
I want us to choose wisely. Taming Big Tech is integral to fixing the internet, and for that, we need digital rights activism.
Digital rights activism, a quarter-century on
Digital rights activism is more than 30 years old now. The Electronic Frontier Foundation turned 30 this year; the Free Software Foundation launched in 1985. For most of the history of the movement, the most prominent criticism leveled against it was that it was irrelevant: The real activist causes were real-world causes (think of the skepticism when Finland declared broadband a human right in 2010), and real-world activism was shoe-leather activism (think of Malcolm Gladwell’s contempt for “clicktivism”). But as tech has grown more central to our daily lives, these accusations of irrelevance have given way first to accusations of insincerity (“You only care about tech because you’re shilling for tech companies”) to accusations of negligence (“Why didn’t you foresee that tech could be such a destructive force?”). But digital rights activism is right where it’s always been: looking out for the humans in a world where tech is inexorably taking over.
The latest version of this critique comes in the form of “surveillance capitalism,” a term coined by business professor Shoshana Zuboff in her long and influential 2019 book, The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power. Zuboff argues that “surveillance capitalism” is a unique creature of the tech industry and that it is unlike any other abusive commercial practice in history, one that is “constituted by unexpected and often illegible mechanisms of extraction, commodification, and control that effectively exile persons from their own behavior while producing new markets of behavioral prediction and modification. Surveillance capitalism challenges democratic norms and departs in key ways from the centuries-long evolution of market capitalism.” It is a new and deadly form of capitalism, a “rogue capitalism,” and our lack of understanding of its unique capabilities and dangers represents an existential, species-wide threat. She’s right that capitalism today threatens our species, and she’s right that tech poses unique challenges to our species and civilization, but she’s really wrong about how tech is different and why it threatens our species.
What’s more, I think that her incorrect diagnosis will lead us down a path that ends up making Big Tech stronger, not weaker. We need to take down Big Tech, and to do that, we need to start by correctly identifying the problem.
Tech exceptionalism, then and now
Early critics of the digital rights movement — perhaps best represented by campaigning organizations like the Electronic Frontier Foundation, the Free Software Foundation, Public Knowledge, and others that focused on preserving and enhancing basic human rights in the digital realm — damned activists for practicing “tech exceptionalism.” Around the turn of the millennium, serious people ridiculed any claim that tech policy mattered in the “real world.” Claims that tech rules had implications for speech, association, privacy, search and seizure, and fundamental rights and equities were treated as ridiculous, an elevation of the concerns of sad nerds arguing about Star Trek on bulletin board systems above the struggles of the Freedom Riders, Nelson Mandela, or the Warsaw ghetto uprising.
In the decades since, accusations of “tech exceptionalism” have only sharpened as tech’s role in everyday life has expanded: Now that tech has infiltrated every corner of our life and our online lives have been monopolized by a handful of giants, defenders of digital freedoms are accused of carrying water for Big Tech, providing cover for its self-interested negligence (or worse, nefarious plots).
From my perspective, the digital rights movement has remained stationary while the rest of the world has moved. From the earliest days, the movement’s concern was users and the toolsmiths who provided the code they needed to realize their fundamental rights. Digital rights activists only cared about companies to the extent that companies were acting to uphold users’ rights (or, just as often, when companies were acting so foolishly that they threatened to bring down new rules that would also make it harder for good actors to help users).
The “surveillance capitalism” critique recasts the digital rights movement in a new light again: not as alarmists who overestimate the importance of their shiny toys nor as shills for big tech but as serene deck-chair rearrangers whose long-standing activism is a liability because it makes them incapable of perceiving novel threats as they continue to fight the last century’s tech battles.
But tech exceptionalism is a sin no matter who practices it.
Image for post
Don’t believe the hype
You’ve probably heard that “if you’re not paying for the product, you’re the product.” As we’ll see below, that’s true, if incomplete. But what is absolutely true is that ad-driven Big Tech’s customers are advertisers, and what companies like Google and Facebook sell is their ability to convince you to buy stuff. Big Tech’s product is persuasion. The services — social media, search engines, maps, messaging, and more — are delivery systems for persuasion.
The fear of surveillance capitalism starts from the (correct) presumption that everything Big Tech says about itself is probably a lie. But the surveillance capitalism critique makes an exception for the claims Big Tech makes in its sales literature — the breathless hype in the pitches to potential advertisers online and in ad-tech seminars about the efficacy of its products: It assumes that Big Tech is as good at influencing us as they claim they are when they’re selling influencing products to credulous customers. That’s a mistake because sales literature is not a reliable indicator of a product’s efficacy.
Surveillance capitalism assumes that because advertisers buy a lot of what Big Tech is selling, Big Tech must be selling something real. But Big Tech’s massive sales could just as easily be the result of a popular delusion or something even more pernicious: monopolistic control over our communications and commerce.
Being watched changes your behavior, and not for the better. It creates risks for our social progress. Zuboff’s book features beautifully wrought explanations of these phenomena. But Zuboff also claims that surveillance literally robs us of our free will — that when our personal data is mixed with machine learning, it creates a system of persuasion so devastating that we are helpless before it. That is, Facebook uses an algorithm to analyze the data it nonconsensually extracts from your daily life and uses it to customize your feed in ways that get you to buy stuff. It is a mind-control ray out of a 1950s comic book, wielded by mad scientists whose supercomputers guarantee them perpetual and total world domination.
What is persuasion?
To understand why you shouldn’t worry about mind-control rays — but why you should worry about surveillance and Big Tech — we must start by unpacking what we mean by “persuasion.”
Google, Facebook, and other surveillance capitalists promise their customers (the advertisers) that if they use machine-learning tools trained on unimaginably large data sets of nonconsensually harvested personal information, they will be able to uncover ways to bypass the rational faculties of the public and direct their behavior, creating a stream of purchases, votes, and other desired outcomes.
The impact of dominance far exceeds the impact of manipulation and should be central to our analysis and any remedies we seek.
But there’s little evidence that this is happening. Instead, the predictions that surveillance capitalism delivers to its customers are much less impressive. Rather than finding ways to bypass our rational faculties, surveillance capitalists like Mark Zuckerberg mostly do one or more of three things:
1. Segmenting
If you’re selling diapers, you have better luck if you pitch them to people in maternity wards. Not everyone who enters or leaves a maternity ward just had a baby, and not everyone who just had a baby is in the market for diapers. But having a baby is a really reliable correlate of being in the market for diapers, and being in a maternity ward is highly correlated with having a baby. Hence diaper ads around maternity wards (and even pitchmen for baby products, who haunt maternity wards with baskets full of freebies).
Surveillance capitalism is segmenting times a billion. Diaper vendors can go way beyond people in maternity wards (though they can do that, too, with things like location-based mobile ads). They can target you based on whether you’re reading articles about child-rearing, diapers, or a host of other subjects, and data mining can suggest unobvious keywords to advertise against. They can target you based on the articles you’ve recently read. They can target you based on what you’ve recently purchased. They can target you based on whether you receive emails or private messages about these subjects — or even if you speak aloud about them (though Facebook and the like convincingly claim that’s not happening — yet).
This is seriously creepy.
But it’s not mind control.
It doesn’t deprive you of your free will. It doesn’t trick you.
Think of how surveillance capitalism works in politics. Surveillance capitalist companies sell political operatives the power to locate people who might be receptive to their pitch. Candidates campaigning on finance industry corruption seek people struggling with debt; candidates campaigning on xenophobia seek out racists. Political operatives have always targeted their message whether their intentions were honorable or not: Union organizers set up pitches at factory gates, and white supremacists hand out fliers at John Birch Society meetings.
But this is an inexact and thus wasteful practice. The union organizer can’t know which worker to approach on the way out of the factory gates and may waste their time on a covert John Birch Society member; the white supremacist doesn’t know which of the Birchers are so delusional that making it to a meeting is as much as they can manage and which ones might be convinced to cross the country to carry a tiki torch through the streets of Charlottesville, Virginia.
Because targeting improves the yields on political pitches, it can accelerate the pace of political upheaval by making it possible for everyone who has secretly wished for the toppling of an autocrat — or just an 11-term incumbent politician — to find everyone else who feels the same way at very low cost. This has been critical to the rapid crystallization of recent political movements including Black Lives Matter and Occupy Wall Street as well as less savory players like the far-right white nationalist movements that marched in Charlottesville.
It’s important to differentiate this kind of political organizing from influence campaigns; finding people who secretly agree with you isn’t the same as convincing people to agree with you. The rise of phenomena like nonbinary or otherwise nonconforming gender identities is often characterized by reactionaries as the result of online brainwashing campaigns that convince impressionable people that they have been secretly queer all along.
But the personal accounts of those who have come out tell a different story where people who long harbored a secret about their gender were emboldened by others coming forward and where people who knew that they were different but lacked a vocabulary for discussing that difference learned the right words from these low-cost means of finding people and learning about their ideas.
2. Deception
Lies and fraud are pernicious, and surveillance capitalism supercharges them through targeting. If you want to sell a fraudulent payday loan or subprime mortgage, surveillance capitalism can help you find people who are both desperate and unsophisticated and thus receptive to your pitch. This accounts for the rise of many phenomena, like multilevel marketing schemes, in which deceptive claims about potential earnings and the efficacy of sales techniques are targeted at desperate people by advertising against search queries that indicate, for example, someone struggling with ill-advised loans.
Surveillance capitalism also abets fraud by making it easy to locate other people who have been similarly deceived, forming a community of people who reinforce one another’s false beliefs. Think of the forums where people who are being victimized by multilevel marketing frauds gather to trade tips on how to improve their luck in peddling the product.
Sometimes, online deception involves replacing someone’s correct beliefs with incorrect ones, as it does in the anti-vaccination movement, whose victims are often people who start out believing in vaccines but are convinced by seemingly plausible evidence that leads them into the false belief that vaccines are harmful.
But it’s much more common for fraud to succeed when it doesn’t have to displace a true belief. When my daughter contracted head lice at daycare, one of the daycare workers told me I could get rid of them by treating her hair and scalp with olive oil. I didn’t know anything about head lice, and I assumed that the daycare worker did, so I tried it (it didn’t work, and it doesn’t work). It’s easy to end up with false beliefs when you simply don’t know any better and when those beliefs are conveyed by someone who seems to know what they’re doing.
This is pernicious and difficult — and it’s also the kind of thing the internet can help guard against by making true information available, especially in a form that exposes the underlying deliberations among parties with sharply divergent views, such as Wikipedia. But it’s not brainwashing; it’s fraud. In the majority of cases, the victims of these fraud campaigns have an informational void filled in the customary way, by consulting a seemingly reliable source. If I look up the length of the Brooklyn Bridge and learn that it is 5,
                800 feet long, but in reality, it is 5,
                989 feet long, the underlying deception is a problem, but it’s a problem with a simple remedy. It’s a very different problem from the anti-vax issue in which someone’s true belief is displaced by a false one by means of sophisticated persuasion.
3. Domination
Surveillance capitalism is the result of monopoly. Monopoly is the cause, and surveillance capitalism and its negative outcomes are the effects of monopoly. I’ll get into this in depth later, but for now, suffice it to say that the tech industry has grown up with a radical theory of antitrust that has allowed companies to grow by merging with their rivals, buying up their nascent competitors, and expanding to control whole market verticals.
One example of how monopolism aids in persuasion is through dominance: Google makes editorial decisions about its algorithms that determine the sort order of the responses to our queries. If a cabal of fraudsters have set out to trick the world into thinking that the Brooklyn Bridge is 5,
                800 feet long, and if Google gives a high search rank to this group in response to queries like “How long is the Brooklyn Bridge?” then the first eight or 10 screens’ worth of Google results could be wrong. And since most people don’t go beyond the first couple of results — let alone the first page of results — Google’s choice means that many people will be deceived.
Google’s dominance over search — more than 86% of web searches are performed through Google — means that the way it orders its search results has an outsized effect on public beliefs. Ironically, Google claims this is why it can’t afford to have any transparency in its algorithm design: Google’s search dominance makes the results of its sorting too important to risk telling the world how it arrives at those results lest some bad actor discover a flaw in the ranking system and exploit it to push its point of view to the top of the search results. There’s an obvious remedy to a company that is too big to audit: break it up into smaller pieces.
Zuboff calls surveillance capitalism a “rogue capitalism” whose data-hoarding and machine-learning techniques rob us of our free will. But influence campaigns that seek to displace existing, correct beliefs with false ones have an effect that is small and temporary while monopolistic dominance over informational systems has massive, enduring effects. Controlling the results to the world’s search queries means controlling access both to arguments and their rebuttals and, thus, control over much of the world’s beliefs. If our concern is how corporations are foreclosing on our ability to make up our own minds and determine our own futures, the impact of dominance far exceeds the impact of manipulation and should be central to our analysis and any remedies we seek.
4. Bypassing our rational faculties
This is the good stuff: using machine learning, “dark patterns,” engagement hacking, and other techniques to get us to do things that run counter to our better judgment. This is mind control.
Some of these techniques have proven devastatingly effective (if only in the short term). The use of countdown timers on a purchase completion page can create a sense of urgency that causes you to ignore the nagging internal voice suggesting that you should shop around or sleep on your decision. The use of people from your social graph in ads can provide “social proof” that a purchase is worth making. Even the auction system pioneered by eBay is calculated to play on our cognitive blind spots, letting us feel like we “own” something because we bid on it, thus encouraging us to bid again when we are outbid to ensure that “our” things stay ours.
Games are extraordinarily good at this. “Free to play” games manipulate us through many techniques, such as presenting players with a series of smoothly escalating challenges that create a sense of mastery and accomplishment but which sharply transition into a set of challenges that are impossible to overcome without paid upgrades. Add some social proof to the mix — a stream of notifications about how well your friends are faring — and before you know it, you’re buying virtual power-ups to get to the next level.
Companies have risen and fallen on these techniques, and the “fallen” part is worth paying attention to. In general, living things adapt to stimulus: Something that is very compelling or noteworthy when you first encounter it fades with repetition until you stop noticing it altogether. Consider the refrigerator hum that irritates you when it starts up but disappears into the background so thoroughly that you only notice it when it stops again.
That’s why behavioral conditioning uses “intermittent reinforcement schedules.” Instead of giving you a steady drip of encouragement or setbacks, games and gamified services scatter rewards on a randomized schedule — often enough to keep you interested and random enough that you can never quite find the pattern that would make it boring.
Intermittent reinforcement is a powerful behavioral tool, but it also represents a collective action problem for surveillance capitalism. The “engagement techniques” invented by the behaviorists of surveillance capitalist companies are quickly copied across the whole sector so that what starts as a mysteriously compelling fillip in the design of a service—like “pull to refresh” or alerts when someone likes your posts or side quests that your characters get invited to while in the midst of main quests—quickly becomes dully ubiquitous. The impossible-to-nail-down nonpattern of randomized drips from your phone becomes a grey-noise wall of sound as every single app and site starts to make use of whatever seems to be working at the time.
From the surveillance capitalist’s point of view, our adaptive capacity is like a harmful bacterium that deprives it of its food source — our attention — and novel techniques for snagging that attention are like new antibiotics that can be used to breach our defenses and destroy our self-determination. And there are techniques like that. Who can forget the Great Zynga Epidemic, when all of our friends were caught in FarmVille’s endless, mindless dopamine loops? But every new attention-commanding technique is jumped on by the whole industry and used so indiscriminately that antibiotic resistance sets in. Given enough repetition, almost all of us develop immunity to even the most powerful techniques — by 2013, two years after Zynga’s peak, its user base had halved.
Not everyone, of course. Some people never adapt to stimulus, just as some people never stop hearing the hum of the refrigerator. This is why most people who are exposed to slot machines play them for a while and then move on while a small and tragic minority liquidate their kids’ college funds, buy adult diapers, and position themselves in front of a machine until they collapse.
But surveillance capitalism’s margins on behavioral modification suck. Tripling the rate at which someone buys a widget sounds great unless the base rate is way less than 1% with an improved rate of… still less than 1%. Even penny slot machines pull down pennies for every spin while surveillance capitalism rakes in infinitesimal penny fractions.
Slot machines’ high returns mean that they can be profitable just by draining the fortunes of the small rump of people who are pathologically vulnerable to them and unable to adapt to their tricks. But surveillance capitalism can’t survive on the fractional pennies it brings down from that vulnerable sliver — that’s why, after the Great Zynga Epidemic had finally burned itself out, the small number of still-addicted players left behind couldn’t sustain it as a global phenomenon. And new powerful attention weapons aren’t easy to find, as is evidenced by the long years since the last time Zynga had a hit. Despite the hundreds of millions of dollars that Zynga has to spend on developing new tools to blast through our adaptation, it has never managed to repeat the lucky accident that let it snag so much of our attention for a brief moment in 2009. Powerhouses like Supercell have fared a little better, but they are rare and throw away many failures for every success.
The vulnerability of small segments of the population to dramatic, efficient corporate manipulation is a real concern that’s worthy of our attention and energy. But it’s not an existential threat to society.
Image for post
If data is the new oil, then surveillance capitalism’s engine has a leak
This adaptation problem offers an explanation for one of surveillance capitalism’s most alarming traits: its relentless hunger for data and its endless expansion of data-gathering capabilities through the spread of sensors, online surveillance, and acquisition of data streams from third parties.
Zuboff observes this phenomenon and concludes that data must be very valuable if surveillance capitalism is so hungry for it. (In her words: “Just as industrial capitalism was driven to the continuous intensification of the means of production, so surveillance capitalists and their market players are now locked into the continuous intensification of the means of behavioral modification and the gathering might of instrumentarian power.”) But what if the voracious appetite is because data has such a short half-life — because people become inured so quickly to new, data-driven persuasion techniques — that the companies are locked in an arms race with our limbic system? What if it’s all a Red Queen’s race where they have to run ever faster — collect ever-more data — just to stay in the same spot?
Of course, all of Big Tech’s persuasion techniques work in concert with one another, and collecting data is useful beyond mere behavioral trickery.
If someone wants to recruit you to buy a refrigerator or join a pogrom, they might use profiling and targeting to send messages to people they judge to be good sales prospects. The messages themselves may be deceptive, making claims about things you’re not very knowledgeable about (food safety and energy efficiency or eugenics and historical claims about racial superiority). They might use search engine optimization and/or armies of fake reviewers and commenters and/or paid placement to dominate the discourse so that any search for further information takes you back to their messages. And finally, they may refine the different pitches using machine learning and other techniques to figure out what kind of pitch works best on someone like you.
Each phase of this process benefits from surveillance: The more data they have, the more precisely they can profile you and target you with specific messages. Think of how you’d sell a fridge if you knew that the warranty on your prospect’s fridge just expired and that they were expecting a tax rebate in April.
Also, the more data they have, the better they can craft deceptive messages — if I know that you’re into genealogy, I might not try to feed you pseudoscience about genetic differences between “races,” sticking instead to conspiratorial secret histories of “demographic replacement” and the like.
Facebook also helps you locate people who have the same odious or antisocial views as you. It makes it possible to find other people who want to carry tiki torches through the streets of Charlottesville in Confederate cosplay. It can help you find other people who want to join your militia and go to the border to look for undocumented migrants to terrorize. It can help you find people who share your belief that vaccines are poison and that the Earth is flat.
There is one way in which targeted advertising uniquely benefits those advocating for socially unacceptable causes: It is invisible. Racism is widely geographically dispersed, and there are few places where racists — and only racists — gather. This is similar to the problem of selling refrigerators in that potential refrigerator purchasers are geographically dispersed and there are few places where you can buy an ad that will be primarily seen by refrigerator customers. But buying a refrigerator is socially acceptable while being a Nazi is not, so you can buy a billboard or advertise in the newspaper sports section for your refrigerator business, and the only potential downside is that your ad will be seen by a lot of people who don’t want refrigerators, resulting in a lot of wasted expense.
But even if you wanted to advertise your Nazi movement on a billboard or prime-time TV or the sports section, you would struggle to find anyone willing to sell you the space for your ad partly because they disagree with your views and partly because they fear censure (boycott, reputational damage, etc.) from other people who disagree with your views.
Targeted ads solve this problem: On the internet, every ad unit can be different for every person, meaning that you can buy ads that are only shown to people who appear to be Nazis and not to people who hate Nazis. When there’s spillover — when someone who hates racism is shown a racist recruiting ad — there is some fallout; the platform or publication might get an angry public or private denunciation. But the nature of the risk assumed by an online ad buyer is different than the risks to a traditional publisher or billboard owner who might want to run a Nazi ad.
Online ads are placed by algorithms that broker between a diverse ecosystem of self-serve ad platforms that anyone can buy an ad through, so the Nazi ad that slips onto your favorite online publication isn’t seen as their moral failing but rather as a failure in some distant, upstream ad supplier. When a publication gets a complaint about an offensive ad that’s appearing in one of its units, it can take some steps to block that ad, but the Nazi might buy a slightly different ad from a different broker serving the same unit. And in any event, internet users increasingly understand that when they see an ad, it’s likely that the advertiser did not choose that publication and that the publication has no idea who its advertisers are.
These layers of indirection between advertisers and publishers serve as moral buffers: Today’s moral consensus is largely that publishers shouldn’t be held responsible for the ads that appear on their pages because they’re not actively choosing to put those ads there. Because of this, Nazis are able to overcome significant barriers to organizing their movement.
Data has a complex relationship with domination. Being able to spy on your customers can alert you to their preferences for your rivals and allow you to head off your rivals at the pass.
More importantly, if you can dominate the information space while also gathering data, then you make other deceptive tactics stronger because it’s harder to break out of the web of deceit you’re spinning. Domination — that is, ultimately becoming a monopoly — and not the data itself is the supercharger that makes every tactic worth pursuing because monopolistic domination deprives your target of an escape route.
If you’re a Nazi who wants to ensure that your prospects primarily see deceptive, confirming information when they search for more, you can improve your odds by seeding the search terms they use through your initial communications. You don’t need to own the top 10 results for “voter suppression” if you can convince your marks to confine their search terms to “voter fraud,” which throws up a very different set of search results.
Surveillance capitalists are like stage mentalists who claim that their extraordinary insights into human behavior let them guess the word that you wrote down and folded up in your pocket but who really use shills, hidden cameras, sleight of hand, and brute-force memorization to amaze you.
Or perhaps they’re more like pick-up artists, the misogynistic cult that promises to help awkward men have sex with women by teaching them “neurolinguistic programming” phrases, body language techniques, and psychological manipulation tactics like “negging” — offering unsolicited negative feedback to women to lower their self-esteem and prick their interest.
Some pick-up artists eventually manage to convince women to go home with them, but it’s not because these men have figured out how to bypass women’s critical faculties. Rather, pick-up artists’ “success” stories are a mix of women who were incapable of giving consent, women who were coerced, women who were intoxicated, self-destructive women, and a few women who were sober and in command of their faculties but who didn’t realize straightaway that they were with terrible men but rectified the error as soon as they could.
Pick-up artists believe they have figured out a secret back door that bypasses women’s critical faculties, but they haven’t. Many of the tactics they deploy, like negging, became the butt of jokes (just like people joke about bad ad targeting), and there’s a good chance that anyone they try these tactics on will immediately recognize them and dismiss the men who use them as irredeemable losers.
Pick-up artists are proof that people can believe they have developed a system of mind control even when it doesn’t work. Pick-up artists simply exploit the fact that one-in-a-million chances can come through for you if you make a million attempts, and then they assume that the other 999,
                999 times, they simply performed the technique incorrectly and commit themselves to doing better next time. There’s only one group of people who find pick-up artist lore reliably convincing: other would-be pick-up artists whose anxiety and insecurity make them vulnerable to scammers and delusional men who convince them that if they pay for tutelage and follow instructions, then they will someday succeed. Pick-up artists assume they fail to entice women because they are bad at being pick-up artists, not because pick-up artistry is bullshit. Pick-up artists are bad at selling themselves to women, but they’re much better at selling themselves to men who pay to learn the secrets of pick-up artistry.
Department store pioneer John Wanamaker is said to have lamented, “Half the money I spend on advertising is wasted; the trouble is I don’t know which half.” The fact that Wanamaker thought that only half of his advertising spending was wasted is a tribute to the persuasiveness of advertising executives, who are much better at convincing potential clients to buy their services than they are at convincing the general public to buy their clients’ wares.
Image for post
What is Facebook?
Facebook is heralded as the origin of all of our modern plagues, and it’s not hard to see why. Some tech companies want to lock their users in but make their money by monopolizing access to the market for apps for their devices and gouging them on prices rather than by spying on them (like Apple). Some companies don’t care about locking in users because they’ve figured out how to spy on them no matter where they are and what they’re doing and can turn that surveillance into money (Google). Facebook alone among the Western tech giants has built a business based on locking in its users and spying on them all the time.
Facebook’s surveillance regime is really without parallel in the Western world. Though Facebook tries to prevent itself from being visible on the public web, hiding most of what goes on there from people unless they’re logged into Facebook, the company has nevertheless booby-trapped the entire web with surveillance tools in the form of Facebook “Like” buttons that web publishers include on their sites to boost their Facebook profiles. Facebook also makes various libraries and other useful code snippets available to web publishers that act as surveillance tendrils on the sites where they’re used, funneling information about visitors to the site — newspapers, dating sites, message boards — to Facebook.
Big Tech is able to practice surveillance not just because it is tech but because it is big.
Facebook offers similar tools to app developers, so the apps — games, fart machines, business review services, apps for keeping abreast of your kid’s schooling — you use will send information about your activities to Facebook even if you don’t have a Facebook account and even if you don’t download or use Facebook apps. On top of all that, Facebook buys data from third-party brokers on shopping habits, physical location, use of “loyalty” programs, financial transactions, etc., and cross-references that with the dossiers it develops on activity on Facebook and with apps and the public web.
Though it’s easy to integrate the web with Facebook — linking to news stories and such — Facebook products are generally not available to be integrated back into the web itself. You can embed a tweet in a Facebook post, but if you embed a Facebook post in a tweet, you just get a link back to Facebook and must log in before you can see it. Facebook has used extreme technological and legal countermeasures to prevent rivals from allowing their users to embed Facebook snippets in competing services or to create alternative interfaces to Facebook that merge your Facebook inbox with those of other services that you use.
And Facebook is incredibly popular, with 2.3 billion claimed users (though many believe this figure to be inflated). Facebook has been used to organize genocidal pogroms, racist riots, anti-vaccination movements, flat Earth cults, and the political lives of some of the world’s ugliest, most brutal autocrats. There are some really alarming things going on in the world, and Facebook is implicated in many of them, so it’s easy to conclude that these bad things are the result of Facebook’s mind-control system, which it rents out to anyone with a few bucks to spend.
To understand what role Facebook plays in the formulation and mobilization of antisocial movements, we need to understand the dual nature of Facebook.
Because it has a lot of users and a lot of data about those users, Facebook is a very efficient tool for locating people with hard-to-find traits, the kinds of traits that are widely diffused in the population such that advertisers have historically struggled to find a cost-effective way to reach them. Think back to refrigerators: Most of us only replace our major appliances a few times in our entire lives. If you’re a refrigerator manufacturer or retailer, you have these brief windows in the life of a consumer during which they are pondering a purchase, and you have to somehow reach them. Anyone who’s ever registered a title change after buying a house can attest that appliance manufacturers are incredibly desperate to reach anyone who has even the slenderest chance of being in the market for a new fridge.
Facebook makes finding people shopping for refrigerators a lot easier. It can target ads to people who’ve registered a new home purchase, to people who’ve searched for refrigerator buying advice, to people who have complained about their fridge dying, or any combination thereof. It can even target people who’ve recently bought other kitchen appliances on the theory that someone who’s just replaced their stove and dishwasher might be in a fridge-buying kind of mood. The vast majority of people who are reached by these ads will not be in the market for a new fridge, but — crucially — the percentage of people who are looking for fridges that these ads reach is much larger than it is than for any group that might be subjected to traditional, offline targeted refrigerator marketing.
Facebook also makes it a lot easier to find people who have the same rare disease as you, which might have been impossible in earlier eras — the closest fellow sufferer might otherwise be hundreds of miles away. It makes it easier to find people who went to the same high school as you even though decades have passed and your former classmates have all been scattered to the four corners of the Earth.
Facebook also makes it much easier to find people who hold the same rare political beliefs as you. If you’ve always harbored a secret affinity for socialism but never dared utter this aloud lest you be demonized by your neighbors, Facebook can help you discover other people who feel the same way (and it might just demonstrate to you that your affinity is more widespread than you ever suspected). It can make it easier to find people who share your sexual identity. And again, it can help you to understand that what you thought was a shameful secret that affected only you was really a widely shared trait, giving you both comfort and the courage to come out to the people in your life.
All of this presents a dilemma for Facebook: Targeting makes the company’s ads more effective than traditional ads, but it also lets advertisers see just how effective their ads are. While advertisers are pleased to learn that Facebook ads are more effective than ads on systems with less sophisticated targeting, advertisers can also see that in nearly every case, the people who see their ads ignore them. Or, at best, the ads work on a subconscious level, creating nebulous unmeasurables like “brand recognition.” This means that the price per ad is very low in nearly every case.
To make things worse, many Facebook groups spark precious little discussion. Your little-league soccer team, the people with the same rare disease as you, and the people you share a political affinity with may exchange the odd flurry of messages at critical junctures, but on a daily basis, there’s not much to say to your old high school chums or other hockey-card collectors.
With nothing but “organic” discussion, Facebook would not generate enough traffic to sell enough ads to make the money it needs to continually expand by buying up its competitors while returning handsome sums to its investors.
So Facebook has to gin up traffic by sidetracking its own forums: Every time Facebook’s algorithm injects controversial materials — inflammatory political articles, conspiracy theories, outrage stories — into a group, it can hijack that group’s nominal purpose with its desultory discussions and supercharge those discussions by turning them into bitter, unproductive arguments that drag on and on. Facebook is optimized for engagement, not happiness, and it turns out that automated systems are pretty good at figuring out things that people will get angry about.
Facebook can modify our behavior but only in a couple of trivial ways. First, it can lock in all your friends and family members so that you check and check and check with Facebook to find out what they are up to; and second, it can make you angry and anxious. It can force you to choose between being interrupted constantly by updates — a process that breaks your concentration and makes it hard to be introspective — and staying in touch with your friends. This is a very limited form of mind control, and it can only really make us miserable, angry, and anxious.
This is why Facebook’s targeting systems — both the ones it shows to advertisers and the ones that let users find people who share their interests — are so next-gen and smooth and easy to use as well as why its message boards have a toolset that seems like it hasn’t changed since the mid-2000s. If Facebook delivered an equally flexible, sophisticated message-reading system to its users, those users could defend themselves against being nonconsensually eyeball-fucked with Donald Trump headlines.
The more time you spend on Facebook, the more ads it gets to show you. The solution to Facebook’s ads only working one in a thousand times is for the company to try to increase how much time you spend on Facebook by a factor of a thousand. Rather than thinking of Facebook as a company that has figured out how to show you exactly the right ad in exactly the right way to get you to do what its advertisers want, think of it as a company that has figured out how to make you slog through an endless torrent of arguments even though they make you miserable, spending so much time on the site that it eventually shows you at least one ad that you respond to.
Image for post
Monopoly and the right to the future tense
Zuboff and her cohort are particularly alarmed at the extent to which surveillance allows corporations to influence our decisions, taking away something she poetically calls “the right to the future tense” — that is, the right to decide for yourself what you will do in the future.
It’s true that advertising can tip the scales one way or another: When you’re thinking of buying a fridge, a timely fridge ad might end the search on the spot. But Zuboff puts enormous and undue weight on the persuasive power of surveillance-based influence techniques. Most of these don’t work very well, and the ones that do won’t work for very long. The makers of these influence tools are confident they will someday refine them into systems of total control, but they are hardly unbiased observers, and the risks from their dreams coming true are very speculative.
By contrast, Zuboff is rather sanguine about 40 years of lax antitrust practice that has allowed a handful of companies to dominate the internet, ushering in an information age with, as one person on Twitter noted, five giant websites each filled with screenshots of the other four.

However, if we are to be alarmed that we might lose the right to choose for ourselves what our future will hold, then monopoly’s nonspeculative, concrete, here-and-now harms should be front and center in our debate over tech policy.
Start with “digital rights management.” In 1998, Bill Clinton signed the Digital Millennium Copyright Act (DMCA) into law. It’s a complex piece of legislation with many controversial clauses but none more so than Section 1201, the “anti-circumvention” rule.
This is a blanket ban on tampering with systems that restrict access to copyrighted works. The ban is so thoroughgoing that it prohibits removing a copyright lock even when no copyright infringement takes place. This is by design: The activities that the DMCA’s Section 1201 sets out to ban are not copyright infringements; rather, they are legal activities that frustrate manufacturers’ commercial plans.
For example, Section 1201’s first major application was on DVD players as a means of enforcing the region coding built into those devices. DVD-CCA, the body that standardized DVDs and DVD players, divided the world into six regions and specified that DVD players must check each disc to determine which regions it was authorized to be played in. DVD players would have their own corresponding region (a DVD player bought in the U.S. would be region 1 while one bought in India would be region 5). If the player and the disc’s region matched, the player would play the disc; otherwise, it would reject it.
However, watching a lawfully produced disc in a country other than the one where you purchased it is not copyright infringement — it’s the opposite. Copyright law imposes this duty on customers for a movie: You must go into a store, find a licensed disc, and pay the asking price. Do that — and nothing else — and you and copyright are square with one another.
The fact that a movie studio wants to charge Indians less than Americans or release in Australia later than it releases in the U.K. has no bearing on copyright law. Once you lawfully acquire a DVD, it is no copyright infringement to watch it no matter where you happen to be.
So DVD and DVD player manufacturers would not be able to use accusations of abetting copyright infringement to punish manufacturers who made noncompliant players that would play discs from any region or repair shops that modified players to let you watch out-of-region discs or software programmers who created programs to let you do this.
That’s where Section 1201 of the DMCA comes in: By banning tampering with an “access control,” the rule gave manufacturers and rights holders standing to sue competitors who released superior products with lawful features that the market demanded (in this case, region-free players).
This is an odious scam against consumers, but as time went by, Section 1201 grew to encompass a rapidly expanding constellation of devices and services as canny manufacturers have realized certain things:
Any device with software in it contains a “copyrighted work” — i.e., the software.
A device can be designed so that reconfiguring the software requires bypassing an “access control for copyrighted works,” which is a potential felony under Section 1201.
Thus, companies can control their customers’ behavior after they take home their purchases by designing products so that all unpermitted uses require modifications that fall afoul of Section 1201.
Section 1201 then becomes a means for manufacturers of all descriptions to force their customers to arrange their affairs to benefit the manufacturers’ shareholders instead of themselves.
This manifests in many ways: from a new generation of inkjet printers that use countermeasures to prevent third-party ink that cannot be bypassed without legal risks to similar systems in tractors that prevent third-party technicians from swapping in the manufacturer’s own parts that are not recognized by the tractor’s control system until it is supplied with a manufacturer’s unlock code.
Closer to home, Apple’s iPhones use these measures to prevent both third-party service and third-party software installation. This allows Apple to decide when an iPhone is beyond repair and must be shredded and landfilled as opposed to the iPhone’s purchaser. (Apple is notorious for its environmentally catastrophic policy of destroying old electronics rather than permitting them to be cannibalized for parts.) This is a very useful power to wield, especially in light of CEO Tim Cook’s January 2019 warning to investors that the company’s profits are endangered by customers choosing to hold onto their phones for longer rather than replacing them.
Apple’s use of copyright locks also allows it to establish a monopoly over how its customers acquire software for their mobile devices. The App Store’s commercial terms guarantee Apple a share of all revenues generated by the apps sold there, meaning that Apple gets paid when you buy an app from its store and then continues to get paid every time you buy something using that app. This comes out of the bottom line of software developers, who must either charge more or accept lower profits for their products.
Crucially, Apple’s use of copyright locks gives it the power to make editorial decisions about which apps you may and may not install on your own device. Apple has used this power to reject dictionaries for containing obscene words; to limit political speech, especially from apps that make sensitive political commentary such as an app that notifies you every time a U.S. drone kills someone somewhere in the world; and to object to a game that commented on the Israel-Palestine conflict.
Apple often justifies monopoly power over software installation in the name of security, arguing that its vetting of apps for its store means that it can guard its users against apps that contain surveillance code. But this cuts both ways. In China, the government ordered Apple to prohibit the sale of privacy tools like VPNs with the exception of VPNs that had deliberately introduced flaws designed to let the Chinese state eavesdrop on users. Because Apple uses technological countermeasures — with legal backstops — to block customers from installing unauthorized apps, Chinese iPhone owners cannot readily (or legally) acquire VPNs that would protect them from Chinese state snooping.
Zuboff calls surveillance capitalism a “rogue capitalism.” Theoreticians of capitalism claim that its virtue is that it aggregates information in the form of consumers’ decisions, producing efficient markets. Surveillance capitalism’s supposed power to rob its victims of their free will through computationally supercharged influence campaigns means that our markets no longer aggregate customers’ decisions because we customers no longer decide — we are given orders by surveillance capitalism’s mind-control rays.
If our concern is that markets cease to function when consumers can no longer make choices, then copyright locks should concern us at least as much as influence campaigns. An influence campaign might nudge you to buy a certain brand of phone; but the copyright locks on that phone absolutely determine where you get it serviced, which apps can run on it, and when you have to throw it away rather than fixing it.
Search order and the right to the future tense
Markets are posed as a kind of magic: By discovering otherwise hidden information conveyed by the free choices of consumers, those consumers’ local knowledge is integrated into a self-correcting system that makes efficient allocations—more efficient than any computer could calculate. But monopolies are incompatible with that notion. When you only have one app store, the owner of the store — not the consumer — decides on the range of choices. As Boss Tweed once said, “I don’t care who does the electing, so long as I get to do the nominating.” A monopolized market is an election whose candidates are chosen by the monopolist.
This ballot rigging is made more pernicious by the existence of monopolies over search order. Google’s search market share is about 90%. When Google’s ranking algorithm puts a result for a popular search term in its top 10, that helps determine the behavior of millions of people. If Google’s answer to “Are vaccines dangerous?” is a page that rebuts anti-vax conspiracy theories, then a sizable portion of the public will learn that vaccines are safe. If, on the other hand, Google sends those people to a site affirming the anti-vax conspiracies, a sizable portion of those millions will come away convinced that vaccines are dangerous.
Google’s algorithm is often tricked into serving disinformation as a prominent search result. But in these cases, Google isn’t persuading people to change their minds; it’s just presenting something untrue as fact when the user has no cause to doubt it.
This is true whether the search is for “Are vaccines dangerous?” or “best restaurants near me.” Most users will never look past the first page of search results, and when the overwhelming majority of people all use the same search engine, the ranking algorithm deployed by that search engine will determine myriad outcomes (whether to adopt a child, whether to have cancer surgery, where to eat dinner, where to move, where to apply for a job) to a degree that vastly outstrips any behavioral outcomes dictated by algorithmic persuasion techniques.
Many of the questions we ask search engines have no empirically correct answers: “Where should I eat dinner?” is not an objective question. Even questions that do have correct answers (“Are vaccines dangerous?”) don’t have one empirically superior source for that answer. Many pages affirm the safety of vaccines, so which one goes first? Under conditions of competition, consumers can choose from many search engines and stick with the one whose algorithmic judgment suits them best, but under conditions of monopoly, we all get our answers from the same place.
Google’s search dominance isn’t a matter of pure merit: The company has leveraged many tactics that would have been prohibited under classical, pre-Ronald-Reagan antitrust enforcement standards to attain its dominance. After all, this is a company that has developed two major products: a really good search engine and a pretty good Hotmail clone. Every other major success it’s had — Android, YouTube, Google Maps, etc. — has come through an acquisition of a nascent competitor. Many of the company’s key divisions, such as the advertising technology of DoubleClick, violate the historical antitrust principle of structural separation, which forbade firms from owning subsidiaries that competed with their customers. Railroads, for example, were barred from owning freight companies that competed with the shippers whose freight they carried.
If we’re worried about giant companies subverting markets by stripping consumers of their ability to make free choices, then vigorous antitrust enforcement seems like an excellent remedy. If we’d denied Google the right to effect its many mergers, we would also have probably denied it its total search dominance. Without that dominance, the pet theories, biases, errors (and good judgment, too) of Google search engineers and product managers would not have such an outsized effect on consumer choice.
This goes for many other companies. Amazon, a classic surveillance capitalist, is obviously the dominant tool for searching Amazon — though many people find their way to Amazon through Google searches and Facebook posts — and obviously, Amazon controls Amazon search. That means that Amazon’s own self-serving editorial choices—like promoting its own house brands over rival goods from its sellers as well as its own pet theories, biases, and errors— determine much of what we buy on Amazon. And since Amazon is the dominant e-commerce retailer outside of China and since it attained that dominance by buying up both large rivals and nascent competitors in defiance of historical antitrust rules, we can blame the monopoly for stripping consumers of their right to the future tense and the ability to shape markets by making informed choices.
Not every monopolist is a surveillance capitalist, but that doesn’t mean they’re not able to shape consumer choices in wide-ranging ways. Zuboff lauds Apple for its App Store and iTunes Store, insisting that adding price tags to the features on its platforms has been the secret to resisting surveillance and thus creating markets. But Apple is the only retailer allowed to sell on its platforms, and it’s the second-largest mobile device vendor in the world. The independent software vendors that sell through Apple’s marketplace accuse the company of the same surveillance sins as Amazon and other big retailers: spying on its customers to find lucrative new products to launch, effectively using independent software vendors as free-market researchers, then forcing them out of any markets they discover.
Because of its use of copyright locks, Apple’s mobile customers are not legally allowed to switch to a rival retailer for its apps if they want to do so on an iPhone. Apple, obviously, is the only entity that gets to decide how it ranks the results of search queries in its stores. These decisions ensure that some apps are often installed (because they appear on page one) and others are never installed (because they appear on page one million). Apple’s search-ranking design decisions have a vastly more significant effect on consumer behaviors than influence campaigns delivered by surveillance capitalism’s ad-serving bots.
Image for post
Monopolists can afford sleeping pills for watchdogs
Only the most extreme market ideologues think that markets can self-regulate without state oversight. Markets need watchdogs — regulators, lawmakers, and other elements of democratic control — to keep them honest. When these watchdogs sleep on the job, then markets cease to aggregate consumer choices because those choices are constrained by illegitimate and deceptive activities that companies are able to get away with because no one is holding them to account.
But this kind of regulatory capture doesn’t come cheap. In competitive sectors, where rivals are constantly eroding one another’s margins, individual firms lack the surplus capital to effectively lobby for laws and regulations that serve their ends.
Many of the harms of surveillance capitalism are the result of weak or nonexistent regulation. Those regulatory vacuums spring from the power of monopolists to resist stronger regulation and to tailor what regulation exists to permit their existing businesses.
Here’s an example: When firms over-collect and over-retain our data, they are at increased risk of suffering a breach — you can’t leak data you never collected, and once you delete all copies of that data, you can no longer leak it. For more than a decade, we’ve lived through an endless parade of ever-worsening data breaches, each one uniquely horrible in the scale of data breached and the sensitivity of that data.
But still, firms continue to over-collect and over-retain our data for three reasons:
1. They are locked in the aforementioned limbic arms race with our capacity to shore up our attentional defense systems to resist their new persuasion techniques. They’re also locked in an arms race with their competitors to find new ways to target people for sales pitches. As soon as they discover a soft spot in our attentional defenses (a counterintuitive, unobvious way to target potential refrigerator buyers), the public begins to wise up to the tactic, and their competitors leap on it, hastening the day in which all potential refrigerator buyers have been inured to the pitch.
2. They believe the surveillance capitalism story. Data is cheap to aggregate and store, and both proponents and opponents of surveillance capitalism have assured managers and product designers that if you collect enough data, you will be able to perform sorcerous acts of mind control, thus supercharging your sales. Even if you never figure out how to profit from the data, someone else will eventually offer to buy it from you to give it a try. This is the hallmark of all economic bubbles: acquiring an asset on the assumption that someone else will buy it from you for more than you paid for it, often to sell to someone else at an even greater price.
3. The penalties for leaking data are negligible. Most countries limit these penalties to actual damages, meaning that consumers who’ve had their data breached have to show actual monetary harms to get a reward. In 2014, Home Depot disclosed that it had lost credit-card data for 53 million of its customers, but it settled the matter by paying those customers about $0.34 each — and a third of that $0.34 wasn’t even paid in cash. It took the form of a credit to procure a largely ineffectual credit-monitoring service.
But the harms from breaches are much more extensive than these actual-damages rules capture. Identity thieves and fraudsters are wily and endlessly inventive. All the vast breaches of our century are being continuously recombined, the data sets merged and mined for new ways to victimize the people whose data was present in them. Any reasonable, evidence-based theory of deterrence and compensation for breaches would not confine damages to actual damages but rather would allow users to claim these future harms.
However, even the most ambitious privacy rules, such as the EU General Data Protection Regulation, fall far short of capturing the negative externalities of the platforms’ negligent over-collection and over-retention, and what penalties they do provide are not aggressively pursued by regulators.
This tolerance of — or indifference to — data over-collection and over-retention can be ascribed in part to the sheer lobbying muscle of the platforms. They are so profitable that they can handily afford to divert gigantic sums to fight any real change — that is, change that would force them to internalize the costs of their surveillance activities.
And then there’s state surveillance, which the surveillance capitalism story dismisses as a relic of another era when the big worry was being jailed for your dissident speech, not having your free will stripped away with machine learning.
But state surveillance and private surveillance are intimately related. As we saw when Apple was conscripted by the Chinese government as a vital collaborator in state surveillance, the only really affordable and tractable way to conduct mass surveillance on the scale practiced by modern states — both “free” and autocratic states — is to suborn commercial services.
Whether it’s Google being used as a location tracking tool by local law enforcement across the U.S. or the use of social media tracking by the Department of Homeland Security to build dossiers on participants in protests against Immigration and Customs Enforcement’s family separation practices, any hard limits on surveillance capitalism would hamstring the state’s own surveillance capability. Without Palantir, Amazon, Google, and other major tech contractors, U.S. cops would not be able to spy on Black people, ICE would not be able to manage the caging of children at the U.S. border, and state welfare systems would not be able to purge their rolls by dressing up cruelty as empiricism and claiming that poor and vulnerable people are ineligible for assistance. At least some of the states’ unwillingness to take meaningful action to curb surveillance should be attributed to this symbiotic relationship. There is no mass state surveillance without mass commercial surveillance.
Monopolism is key to the project of mass state surveillance. It’s true that smaller tech firms are apt to be less well-defended than Big Tech, whose security experts are drawn from the tops of their field and who are given enormous resources to secure and monitor their systems against intruders. But smaller firms also have less to protect: fewer users whose data is more fragmented across more systems and have to be suborned one at a time by state actors.
A concentrated tech sector that works with authorities is a much more powerful ally in the project of mass state surveillance than a fragmented one composed of smaller actors. The U.S. tech sector is small enough that all of its top executives fit around a single boardroom table in Trump Tower in 2017, shortly after Trump’s inauguration. Most of its biggest players bid to win JEDI, the Pentagon’s $10 billion Joint Enterprise Defense Infrastructure cloud contract. Like other highly concentrated industries, Big Tech rotates its key employees in and out of government service, sending them to serve in the Department of Defense and the White House, then hiring ex-Pentagon and ex-DOD top staffers and officers to work in their own government relations departments.
They can even make a good case for doing this: After all, when there are only four or five big companies in an industry, everyone qualified to regulate those companies has served as an executive in at least a couple of them — because, likewise, when there are only five companies in an industry, everyone qualified for a senior role at any of them is by definition working at one of the other ones.
While surveillance doesn’t cause monopolies, monopolies certainly abet surveillance.
Industries that are competitive are fragmented — composed of companies that are at each other’s throats all the time and eroding one another’s margins in bids to steal their best customers. This leaves them with much more limited capital to use to lobby for favorable rules and a much harder job of getting everyone to agree to pool their resources to benefit the industry as a whole.
Surveillance combined with machine learning is supposed to be an existential crisis, a species-defining moment at which our free will is just a few more advances in the field from being stripped away. I am skeptical of this claim, but I do think that tech poses an existential threat to our society and possibly our species.
But that threat grows out of monopoly.
One of the consequences of tech’s regulatory capture is that it can shift liability for poor security decisions onto its customers and the wider society. It is absolutely normal in tech for companies to obfuscate the workings of their products, to make them deliberately hard to understand, and to threaten security researchers who seek to independently audit those products.
IT is the only field in which this is practiced: No one builds a bridge or a hospital and keeps the composition of the steel or the equations used to calculate load stresses a secret. It is a frankly bizarre practice that leads, time and again, to grotesque security defects on farcical scales, with whole classes of devices being revealed as vulnerable long after they are deployed in the field and put into sensitive places.
The monopoly power that keeps any meaningful consequences for breaches at bay means that tech companies continue to build terrible products that are insecure by design and that end up integrated into our lives, in possession of our data, and connected to our physical world. For years, Boeing has struggled with the aftermath of a series of bad technology decisions that made its 737 fleet a global pariah, a rare instance in which bad tech decisions have been seriously punished in the market.
These bad security decisions are compounded yet again by the use of copyright locks to enforce business-model decisions against consumers. Recall that these locks have become the go-to means for shaping consumer behavior, making it technically impossible to use third-party ink, insulin, apps, or service depots in connection with your lawfully acquired property.
Recall also that these copyright locks are backstopped by legislation (such as Section 1201 of the DMCA or Article 6 of the 2001 EU Copyright Directive) that ban tampering with (“circumventing”) them, and these statutes have been used to threaten security researchers who make disclosures about vulnerabilities without permission from manufacturers.
This amounts to a manufacturer’s veto over safety warnings and criticism. While this is far from the legislative intent of the DMCA and its sister statutes around the world, Congress has not intervened to clarify the statute nor will it because to do so would run counter to the interests of powerful, large firms whose lobbying muscle is unstoppable.
Copyright locks are a double whammy: They create bad security decisions that can’t be freely investigated or discussed. If markets are supposed to be machines for aggregating information (and if surveillance capitalism’s notional mind-control rays are what make it a “rogue capitalism” because it denies consumers the power to make decisions), then a program of legally enforced ignorance of the risks of products makes monopolism even more of a “rogue capitalism” than surveillance capitalism’s influence campaigns.
And unlike mind-control rays, enforced silence over security is an immediate, documented problem, and it does constitute an existential threat to our civilization and possibly our species. The proliferation of insecure devices — especially devices that spy on us and especially when those devices also can manipulate the physical world by, say, steering your car or flipping a breaker at a power station — is a kind of technology debt.
In software design, “technology debt” refers to old, baked-in decisions that turn out to be bad ones in hindsight. Perhaps a long-ago developer decided to incorporate a networking protocol made by a vendor that has since stopped supporting it. But everything in the product still relies on that superannuated protocol, and so, with each revision, the product team has to work around this obsolete core, adding compatibility layers, surrounding it with security checks that try to shore up its defenses, and so on. These Band-Aid measures compound the debt because every subsequent revision has to make allowances for them, too, like interest mounting on a predatory subprime loan. And like a subprime loan, the interest mounts faster than you can hope to pay it off: The product team has to put so much energy into maintaining this complex, brittle system that they don’t have any time left over to refactor the product from the ground up and “pay off the debt” once and for all.
Typically, technology debt results in a technological bankruptcy: The product gets so brittle and unsustainable that it fails catastrophically. Think of the antiquated COBOL-based banking and accounting systems that fell over at the start of the pandemic emergency when confronted with surges of unemployment claims. Sometimes that ends the product; sometimes it takes the company down with it. Being caught in the default of a technology debt is scary and traumatic, just like losing your house due to bankruptcy is scary and traumatic.
But the technology debt created by copyright locks isn’t individual debt; it’s systemic. Everyone in the world is exposed to this over-leverage, as was the case with the 2008 financial crisis. When that debt comes due — when we face a cascade of security breaches that threaten global shipping and logistics, the food supply, pharmaceutical production pipelines, emergency communications, and other critical systems that are accumulating technology debt in part due to the presence of deliberately insecure and deliberately unauditable copyright locks — it will indeed pose an existential risk.
Image for post
Privacy and monopoly
Many tech companies are gripped by an orthodoxy that holds that if they just gather enough data on enough of our activities, everything else is possible — the mind control and endless profits. This is an unfalsifiable hypothesis: If data gives a tech company even a tiny improvement in behavior prediction and modification, the company declares that it has taken the first step toward global domination with no end in sight. If a company fails to attain any improvements from gathering and analyzing data, it declares success to be just around the corner, attainable once more data is in hand.
Surveillance tech is far from the first industry to embrace a nonsensical, self-serving belief that harms the rest of the world, and it is not the first industry to profit handsomely from such a delusion. Long before hedge-fund managers were claiming (falsely) that they could beat the S&P 500, there were plenty of other “respectable” industries that have been revealed as quacks in hindsight. From the makers of radium suppositories (a real thing!) to the cruel sociopaths who claimed they could “cure” gay people, history is littered with the formerly respectable titans of discredited industries.
This is not to say that there’s nothing wrong with Big Tech and its ideological addiction to data. While surveillance’s benefits are mostly overstated, its harms are, if anything, understated.
There’s real irony here. The belief in surveillance capitalism as a “rogue capitalism” is driven by the belief that markets wouldn’t tolerate firms that are gripped by false beliefs. An oil company that has false beliefs about where the oil is will eventually go broke digging dry wells after all.
But monopolists get to do terrible things for a long time before they pay the price. Think of how concentration in the finance sector allowed the subprime crisis to fester as bond-rating agencies, regulators, investors, and critics all fell under the sway of a false belief that complex mathematics could construct “fully hedged” debt instruments that could not possibly default. A small bank that engaged in this kind of malfeasance would simply go broke rather than outrunning the inevitable crisis, perhaps growing so big that it averted it altogether. But large banks were able to continue to attract investors, and when they finally did come a-cropper, the world’s governments bailed them out. The worst offenders of the subprime crisis are bigger than they were in 2008, bringing home more profits and paying their execs even larger sums.
Big Tech is able to practice surveillance not just because it is tech but because it is big. The reason every web publisher embeds a Facebook “Like” button is that Facebook dominates the internet’s social media referrals — and every one of those “Like” buttons spies on everyone who lands on a page that contains them (see also: Google Analytics embeds, Twitter buttons, etc.).
The reason the world’s governments have been slow to create meaningful penalties for privacy breaches is that Big Tech’s concentration produces huge profits that can be used to lobby against those penalties — and Big Tech’s concentration means that the companies involved are able to arrive at a unified negotiating position that supercharges the lobbying.
The reason that the smartest engineers in the world want to work for Big Tech is that Big Tech commands the lion’s share of tech industry jobs.
The reason people who are aghast at Facebook’s and Google’s and Amazon’s data-handling practices continue to use these services is that all their friends are on Facebook; Google dominates search; and Amazon has put all the local merchants out of business.
Competitive markets would weaken the companies’ lobbying muscle by reducing their profits and pitting them against each other in regulatory forums. It would give customers other places to go to get their online services. It would make the companies small enough to regulate and pave the way to meaningful penalties for breaches. It would let engineers with ideas that challenged the surveillance orthodoxy raise capital to compete with the incumbents. It would give web publishers multiple ways to reach audiences and make the case against Facebook and Google and Twitter embeds.
In other words, while surveillance doesn’t cause monopolies, monopolies certainly abet surveillance.
Ronald Reagan, pioneer of tech monopolism
Technology exceptionalism is a sin, whether it’s practiced by technology’s blind proponents or by its critics. Both of these camps are prone to explaining away monopolistic concentration by citing some special characteristic of the tech industry, like network effects or first-mover advantage. The only real difference between these two groups is that the tech apologists say monopoly is inevitable so we should just let tech get away with its abuses while competition regulators in the U.S. and the EU say monopoly is inevitable so we should punish tech for its abuses but not try to break up the monopolies.
To understand how tech became so monopolistic, it’s useful to look at the dawn of the consumer tech industry: 1979, the year the Apple II Plus launched and became the first successful home computer. That also happens to be the year that Ronald Reagan hit the campaign trail for the 1980 presidential race — a race he won, leading to a radical shift in the way that antitrust concerns are handled in America. Reagan’s cohort of politicians — including Margaret Thatcher in the U.K., Brian Mulroney in Canada, Helmut Kohl in Germany, and Augusto Pinochet in Chile — went on to enact similar reforms that eventually spread around the world.
Antitrust’s story began nearly a century before all that with laws like the Sherman Act, which took aim at monopolists on the grounds that monopolies were bad in and of themselves — squeezing out competitors, creating “diseconomies of scale” (when a company is so big that its constituent parts go awry and it is seemingly helpless to address the problems), and capturing their regulators to such a degree that they can get away with a host of evils.
Then came a fabulist named Robert Bork, a former solicitor general who Reagan appointed to the powerful U.S. Court of Appeals for the D.C. Circuit and who had created an alternate legislative history of the Sherman Act and its successors out of whole cloth. Bork insisted that these statutes were never targeted at monopolies (despite a wealth of evidence to the contrary, including the transcribed speeches of the acts’ authors) but, rather, that they were intended to prevent “consumer harm” — in the form of higher prices.
Bork was a crank, but he was a crank with a theory that rich people really liked. Monopolies are a great way to make rich people richer by allowing them to receive “monopoly rents” (that is, bigger profits) and capture regulators, leading to a weaker, more favorable regulatory environment with fewer protections for customers, suppliers, the environment, and workers.
Bork’s theories were especially palatable to the same power brokers who backed Reagan, and Reagan’s Department of Justice and other agencies began to incorporate Bork’s antitrust doctrine into their enforcement decisions (Reagan even put Bork up for a Supreme Court seat, but Bork flunked the Senate confirmation hearing so badly that,
                40 years later, D.C. insiders use the term “borked” to refer to any catastrophically bad political performance).
Little by little, Bork’s theories entered the mainstream, and their backers began to infiltrate the legal education field, even putting on junkets where members of the judiciary were treated to lavish meals, fun outdoor activities, and seminars where they were indoctrinated into the consumer harm theory of antitrust. The more Bork’s theories took hold, the more money the monopolists were making — and the more surplus capital they had at their disposal to lobby for even more Borkian antitrust influence campaigns.
The history of Bork’s antitrust theories is a really good example of the kind of covertly engineered shifts in public opinion that Zuboff warns us against, where fringe ideas become mainstream orthodoxy. But Bork didn’t change the world overnight. He played a very long game, for over a generation, and he had a tailwind because the same forces that backed oligarchic antitrust theories also backed many other oligarchic shifts in public opinion. For example, the idea that taxation is theft, that wealth is a sign of virtue, and so on — all of these theories meshed to form a coherent ideology that elevated inequality to a virtue.
Today, many fear that machine learning allows surveillance capitalism to sell “Bork-as-a-Service,” at internet speeds, so that you can contract a machine-learning company to engineer rapid shifts in public sentiment without needing the capital to sustain a multipronged, multigenerational project working at the local, state, national, and global levels in business, law, and philosophy. I do not believe that such a project is plausible, though I agree that this is basically what the platforms claim to be selling. They’re just lying about it. Big Tech lies all the time, including in their sales literature.
The idea that tech forms “natural monopolies” (monopolies that are the inevitable result of the realities of an industry, such as the monopolies that accrue the first company to run long-haul phone lines or rail lines) is belied by tech’s own history: In the absence of anti-competitive tactics, Google was able to unseat AltaVista and Yahoo; Facebook was able to head off Myspace. There are some advantages to gathering mountains of data, but those mountains of data also have disadvantages: liability (from leaking), diminishing returns (from old data), and institutional inertia (big companies, like science, progress one funeral at a time).
Indeed, the birth of the web saw a mass-extinction event for the existing giant, wildly profitable proprietary technologies that had capital, network effects, and walls and moats surrounding their businesses. The web showed that when a new industry is built around a protocol, rather than a product, the combined might of everyone who uses the protocol to reach their customers or users or communities outweighs even the most massive products. CompuServe, AOL, MSN, and a host of other proprietary walled gardens learned this lesson the hard way: Each believed it could stay separate from the web, offering “curation” and a guarantee of consistency and quality instead of the chaos of an open system. Each was wrong and ended up being absorbed into the public web.
Yes, tech is heavily monopolized and is now closely associated with industry concentration, but this has more to do with a matter of timing than its intrinsically monopolistic tendencies. Tech was born at the moment that antitrust enforcement was being dismantled, and tech fell into exactly the same pathologies that antitrust was supposed to guard against. To a first approximation, it is reasonable to assume that tech’s monopolies are the result of a lack of anti-monopoly action and not the much-touted unique characteristics of tech, such as network effects, first-mover advantage, and so on.
In support of this thesis, I offer the concentration that every other industry has undergone over the same period. From professional wrestling to consumer packaged goods to commercial property leasing to banking to sea freight to oil to record labels to newspaper ownership to theme parks, every industry has undergone a massive shift toward concentration. There’s no obvious network effects or first-mover advantage at play in these industries. However, in every case, these industries attained their concentrated status through tactics that were prohibited before Bork’s triumph: merging with major competitors, buying out innovative new market entrants, horizontal and vertical integration, and a suite of anti-competitive tactics that were once illegal but are not any longer.
Again: When you change the laws intended to prevent monopolies and then monopolies form in exactly the way the law was supposed to prevent, it is reasonable to suppose that these facts are related. Tech’s concentration can be readily explained without recourse to radical theories of network effects — but only if you’re willing to indict unregulated markets as tending toward monopoly. Just as a lifelong smoker can give you a hundred reasons why their smoking didn’t cause their cancer (“It was the environmental toxins”),
                true believers in unregulated markets have a whole suite of unconvincing explanations for monopoly in tech that leave capitalism intact.
Steering with the windshield wipers
It’s been 40 years since Bork’s project to rehabilitate monopolies achieved liftoff, and that is a generation and a half, which is plenty of time to take a common idea and make it seem outlandish and vice versa. Before the 1940s, affluent Americans dressed their baby boys in pink while baby girls wore blue (a “delicate and dainty” color). While gendered colors are obviously totally arbitrary, many still greet this news with amazement and find it hard to imagine a time when pink connoted masculinity.
After 40 years of studiously ignoring antitrust analysis and enforcement, it’s not surprising that we’ve all but forgotten that antitrust exists, that in living memory, growth through mergers and acquisitions were largely prohibited under law, that market-cornering strategies like vertical integration could land a company in court.
Antitrust is a market society’s steering wheel, the control of first resort to keep would-be masters of the universe in their lanes. But Bork and his cohort ripped out our steering wheel 40 years ago. The car is still barreling along, and so we’re yanking as hard as we can on all the other controls in the car as well as desperately flapping the doors and rolling the windows up and down in the hopes that one of these other controls can be repurposed to let us choose where we’re heading before we careen off a cliff.
It’s like a 1960s science-fiction plot come to life: People stuck in a “generation ship,” plying its way across the stars, a ship once piloted by their ancestors; and now, after a great cataclysm, the ship’s crew have forgotten that they’re in a ship at all and no longer remember where the control room is. Adrift, the ship is racing toward its extinction, and unless we can seize the controls and execute emergency course correction, we’re all headed for a fiery death in the heart of a sun.
Image for post
Surveillance still matters
None of this is to minimize the problems with surveillance. Surveillance matters, and Big Tech’s use of surveillance is an existential risk to our species, but that’s not because surveillance and machine learning rob us of our free will.
Surveillance has become much more efficient thanks to Big Tech. In 1989, the Stasi — the East German secret police — had the whole country under surveillance, a massive undertaking that recruited one out of every 60 people to serve as an informant or intelligence operative.
Today, we know that the NSA is spying on a significant fraction of the entire world’s population, and its ratio of surveillance operatives to the surveilled is more like 1: 10,
                000 (that’s probably on the low side since it assumes that every American with top-secret clearance is working for the NSA on this project — we don’t know how many of those cleared people are involved in NSA spying, but it’s definitely not all of them).
How did the ratio of surveillable citizens expand from 1: 60 to 1: 10,
                000 in less than 30 years? It’s thanks to Big Tech. Our devices and services gather most of the data that the NSA mines for its surveillance project. We pay for these devices and the services they connect to, and then we painstakingly perform the data-entry tasks associated with logging facts about our lives, opinions, and preferences. This mass surveillance project has been largely useless for fighting terrorism: The NSA can only point to a single minor success story in which it used its data collection program to foil an attempt by a U.S. resident to wire a few thousand dollars to an overseas terror group. It’s ineffective for much the same reason that commercial surveillance projects are largely ineffective at targeting advertising: The people who want to commit acts of terror, like people who want to buy a refrigerator, are extremely rare. If you’re trying to detect a phenomenon whose base rate is one in a million with an instrument whose accuracy is only 99%, then every true positive will come at the cost of 9,
                999 false positives.
Let me explain that again: If one in a million people is a terrorist, then there will only be about one terrorist in a random sample of one million people. If your test for detecting terrorists is 99% accurate, it will identify 10,
                000 terrorists in your million-person sample (1% of one million is 10,
                000). For every true positive, you’ll get 9,
                999 false positives.
In reality, the accuracy of algorithmic terrorism detection falls far short of the 99% mark, as does refrigerator ad targeting. The difference is that being falsely accused of wanting to buy a fridge is a minor nuisance while being falsely accused of planning a terror attack can destroy your life and the lives of everyone you love.
Mass state surveillance is only feasible because of surveillance capitalism and its extremely low-yield ad-targeting systems, which require a constant feed of personal data to remain barely viable. Surveillance capitalism’s primary failure mode is mistargeted ads while mass state surveillance’s primary failure mode is grotesque human rights abuses, tending toward totalitarianism.
State surveillance is no mere parasite on Big Tech, sucking up its data and giving nothing in return. In truth, the two are symbiotes: Big Tech sucks up our data for spy agencies, and spy agencies ensure that governments don’t limit Big Tech’s activities so severely that it would no longer serve the spy agencies’ needs. There is no firm distinction between state surveillance and surveillance capitalism; they are dependent on one another.
To see this at work today, look no further than Amazon’s home surveillance device, the Ring doorbell, and its associated app, Neighbors. Ring — a product that Amazon acquired and did not develop in house — makes a camera-enabled doorbell that streams footage from your front door to your mobile device. The Neighbors app allows you to form a neighborhood-wide surveillance grid with your fellow Ring owners through which you can share clips of “suspicious characters.” If you’re thinking that this sounds like a recipe for letting curtain-twitching racists supercharge their suspicions of people with brown skin who walk down their blocks, you’re right. Ring has become a de facto, off-the-books arm of the police without any of the pesky oversight or rules.
In mid-2019, a series of public records requests revealed that Amazon had struck confidential deals with more than 400 local law enforcement agencies through which the agencies would promote Ring and Neighbors and in exchange get access to footage from Ring cameras. In theory, cops would need to request this footage through Amazon (and internal documents reveal that Amazon devotes substantial resources to coaching cops on how to spin a convincing story when doing so), but in practice, when a Ring customer turns down a police request, Amazon only requires the agency to formally request the footage from the company, which it will then produce.
Ring and law enforcement have found many ways to intertwine their activities. Ring strikes secret deals to acquire real-time access to 911 dispatch and then streams alarming crime reports to Neighbors users, which serve as convincers for anyone who’s contemplating a surveillance doorbell but isn’t sure whether their neighborhood is dangerous enough to warrant it.
The more the cops buzz-market the surveillance capitalist Ring, the more surveillance capability the state gets. Cops who rely on private entities for law-enforcement roles then brief against any controls on the deployment of that technology while the companies return the favor by lobbying against rules requiring public oversight of police surveillance technology. The more the cops rely on Ring and Neighbors, the harder it will be to pass laws to curb them. The fewer laws there are against them, the more the cops will rely on them.
Dignity and sanctuary
But even if we could exercise democratic control over our states and force them to stop raiding surveillance capitalism’s reservoirs of behavioral data, surveillance capitalism would still harm us.
This is an area where Zuboff shines. Her chapter on “sanctuary” — the feeling of being unobserved — is a beautiful hymn to introspection, calmness, mindfulness, and tranquility.
When you are watched, something changes. Anyone who has ever raised a child knows this. You might look up from your book (or more realistically, from your phone) and catch your child in a moment of profound realization and growth, a moment where they are learning something that is right at the edge of their abilities, requiring their entire ferocious concentration. For a moment, you’re transfixed, watching that rare and beautiful moment of focus playing out before your eyes, and then your child looks up and sees you seeing them, and the moment collapses. To grow, you need to be and expose your authentic self, and in that moment, you are vulnerable like a hermit crab scuttling from one shell to the next. The tender, unprotected tissues you expose in that moment are too delicate to reveal in the presence of another, even someone you trust as implicitly as a child trusts their parent.
In the digital age, our authentic selves are inextricably tied to our digital lives. Your search history is a running ledger of the questions you’ve pondered. Your location history is a record of the places you’ve sought out and the experiences you’ve had there. Your social graph reveals the different facets of your identity, the people you’ve connected with.
To be observed in these activities is to lose the sanctuary of your authentic self.
There’s another way in which surveillance capitalism robs us of our capacity to be our authentic selves: by making us anxious. Surveillance capitalism isn’t really a mind-control ray, but you don’t need a mind-control ray to make someone anxious. After all, another word for anxiety is agitation, and to make someone experience agitation, you need merely to agitate them. To poke them and prod them and beep at them and buzz at them and bombard them on an intermittent schedule that is just random enough that our limbic systems never quite become inured to it.
Our devices and services are “general purpose” in that they can connect anything or anyone to anything or anyone else and that they can run any program that can be written. This means that the distraction rectangles in our pockets hold our most precious moments with our most beloved people and their most urgent or time-sensitive communications (from “running late can you get the kid?” to “doctor gave me bad news and I need to talk to you RIGHT NOW”) as well as ads for refrigerators and recruiting messages from Nazis.
All day and all night, our pockets buzz, shattering our concentration and tearing apart the fragile webs of connection we spin as we think through difficult ideas. If you locked someone in a cell and agitated them like this, we’d call it “sleep deprivation torture,” and it would be a war crime under the Geneva Conventions.
Afflicting the afflicted
The effects of surveillance on our ability to be our authentic selves are not equal for all people. Some of us are lucky enough to live in a time and place in which all the most important facts of our lives are widely and roundly socially acceptable and can be publicly displayed without the risk of social consequence.
But for many of us, this is not true. Recall that in living memory, many of the ways of being that we think of as socially acceptable today were once cause for dire social sanction or even imprisonment. If you are 65 years old, you have lived through a time in which people living in “free societies” could be imprisoned or sanctioned for engaging in homosexual activity, for falling in love with a person whose skin was a different color than their own, or for smoking weed.
Today, these activities aren’t just decriminalized in much of the world, they’re considered normal, and the fallen prohibitions are viewed as shameful, regrettable relics of the past.
How did we get from prohibition to normalization? Through private, personal activity: People who were secretly gay or secret pot-smokers or who secretly loved someone with a different skin color were vulnerable to retaliation if they made their true selves known and were limited in how much they could advocate for their own right to exist in the world and be true to themselves. But because there was a private sphere, these people could form alliances with their friends and loved ones who did not share their disfavored traits by having private conversations in which they came out, disclosing their true selves to the people around them and bringing them to their cause one conversation at a time.
The right to choose the time and manner of these conversations was key to their success. It’s one thing to come out to your dad while you’re on a fishing trip away from the world and another thing entirely to blurt it out over the Christmas dinner table while your racist Facebook uncle is there to make a scene.
Without a private sphere, there’s a chance that none of these changes would have come to pass and that the people who benefited from these changes would have either faced social sanction for coming out to a hostile world or would have never been able to reveal their true selves to the people they love.
The corollary is that, unless you think that our society has attained social perfection — that your grandchildren in 50 years will ask you to tell them the story of how, in 2020, every injustice had been righted and no further change had to be made — then you should expect that right now, at this minute, there are people you love, whose happiness is key to your own, who have a secret in their hearts that stops them from ever being their authentic selves with you. These people are sorrowing and will go to their graves with that secret sorrow in their hearts, and the source of that sorrow will be the falsity of their relationship to you.
A private realm is necessary for human progress.
Image for post
Any data you collect and retain will eventually leak
The lack of a private life can rob vulnerable people of the chance to be their authentic selves and constrain our actions by depriving us of sanctuary, but there is another risk that is borne by everyone, not just people with a secret: crime.
Personally identifying information is of very limited use for the purpose of controlling peoples’ minds, but identity theft — really a catchall term for a whole constellation of terrible criminal activities that can destroy your finances, compromise your personal integrity, ruin your reputation, or even expose you to physical danger — thrives on it.
Attackers are not limited to using data from one breached source, either. Multiple services have suffered breaches that exposed names, addresses, phone numbers, passwords, sexual tastes, school grades, work performance, brushes with the criminal justice system, family details, genetic information, fingerprints and other biometrics, reading habits, search histories, literary tastes, pseudonymous identities, and other sensitive information. Attackers can merge data from these different breaches to build up extremely detailed dossiers on random subjects and then use different parts of the data for different criminal purposes.
For example, attackers can use leaked username and password combinations to hijack whole fleets of commercial vehicles that have been fitted with anti-theft GPS trackers and immobilizers or to hijack baby monitors in order to terrorize toddlers with the audio tracks from pornography. Attackers use leaked data to trick phone companies into giving them your phone number, then they intercept SMS-based two-factor authentication codes in order to take over your email, bank account, and/or cryptocurrency wallets.
Attackers are endlessly inventive in the pursuit of creative ways to weaponize leaked data. One common use of leaked data is to penetrate companies in order to access more data.
Like spies, online fraudsters are totally dependent on companies over-collecting and over-retaining our data. Spy agencies sometimes pay companies for access to their data or intimidate them into giving it up, but sometimes they work just like criminals do — by sneaking data out of companies’ databases.
The over-collection of data has a host of terrible social consequences, from the erosion of our authentic selves to the undermining of social progress, from state surveillance to an epidemic of online crime. Commercial surveillance is also a boon to people running influence campaigns, but that’s the least of our troubles.
Image for post
Critical tech exceptionalism is still tech exceptionalism
Big Tech has long practiced technology exceptionalism: the idea that it should not be subject to the mundane laws and norms of “meatspace.” Mottoes like Facebook’s “move fast and break things” attracted justifiable scorn of the companies’ self-serving rhetoric.
Tech exceptionalism got us all into a lot of trouble, so it’s ironic and distressing to see Big Tech’s critics committing the same sin.
Big Tech is not a “rogue capitalism” that cannot be cured through the traditional anti-monopoly remedies of trustbusting (forcing companies to divest of competitors they have acquired) and bans on mergers to monopoly and other anti-competitive tactics. Big Tech does not have the power to use machine learning to influence our behavior so thoroughly that markets lose the ability to punish bad actors and reward superior competitors. Big Tech has no rule-writing mind-control ray that necessitates ditching our old toolbox.
The thing is, people have been claiming to have perfected mind-control rays for centuries, and every time, it turned out to be a con — though sometimes the con artists were also conning themselves.
For generations, the advertising industry has been steadily improving its ability to sell advertising services to businesses while only making marginal gains in selling those businesses’ products to prospective customers. John Wanamaker’s lament that “50% of my advertising budget is wasted, I just don’t know which 50%” is a testament to the triumph of ad executives, who successfully convinced Wanamaker that only half of the money he spent went to waste.
The tech industry has made enormous improvements in the science of convincing businesses that they’re good at advertising while their actual improvements to advertising — as opposed to targeting — have been pretty ho-hum. The vogue for machine learning — and the mystical invocation of “artificial intelligence” as a synonym for straightforward statistical inference techniques — has greatly boosted the efficacy of Big Tech’s sales pitch as marketers have exploited potential customers’ lack of technical sophistication to get away with breathtaking acts of overpromising and underdelivering.
It’s tempting to think that if businesses are willing to pour billions into a venture that the venture must be a good one. Yet there are plenty of times when this rule of thumb has led us astray. For example, it’s virtually unheard of for managed investment funds to outperform simple index funds, and investors who put their money into the hands of expert money managers overwhelmingly fare worse than those who entrust their savings to index funds. But managed funds still account for the majority of the money invested in the markets, and they are patronized by some of the richest, most sophisticated investors in the world. Their vote of confidence in an underperforming sector is a parable about the role of luck in wealth accumulation, not a sign that managed funds are a good buy.
The claims of Big Tech’s mind-control system are full of tells that the enterprise is a con. For example, the reliance on the “Big Five” personality traits as a primary means of influencing people even though the “Big Five” theory is unsupported by any large-scale, peer-reviewed studies and is mostly the realm of marketing hucksters and pop psych.
Big Tech’s promotional materials also claim that their algorithms can accurately perform “sentiment analysis” or detect peoples’ moods based on their “microexpressions,” but these are marketing claims, not scientific ones. These methods are largely untested by independent scientific experts, and where they have been tested, they’ve been found sorely wanting. Microexpressions are particularly suspect as the companies that specialize in training people to detect them have been shown to underperform relative to random chance.
Big Tech has been so good at marketing its own supposed superpowers that it’s easy to believe that they can market everything else with similar acumen, but it’s a mistake to believe the hype. Any statement a company makes about the quality of its products is clearly not impartial. The fact that we distrust all the things that Big Tech says about its data handling, compliance with privacy laws, etc., is only reasonable — but why on Earth would we treat Big Tech’s marketing literature as the gospel truth? Big Tech lies about just about everything, including how well its machine-learning fueled persuasion systems work.
That skepticism should infuse all of our evaluations of Big Tech and its supposed abilities, including our perusal of its patents. Zuboff vests these patents with enormous significance, pointing out that Google claimed extensive new persuasion capabilities in its patent filings. These claims are doubly suspect: first, because they are so self-serving, and second, because the patent itself is so notoriously an invitation to exaggeration.
Patent applications take the form of a series of claims and range from broad to narrow. A typical patent starts out by claiming that its authors have invented a method or system for doing every conceivable thing that anyone might do, ever, with any tool or device. Then it narrows that claim in successive stages until we get to the actual “invention” that is the true subject of the patent. The hope is that the patent examiner — who is almost certainly overworked and underinformed — will miss the fact that some or all of these claims are ridiculous, or at least suspect, and grant the patent’s broader claims. Patents for unpatentable things are still incredibly useful because they can be wielded against competitors who might license that patent or steer clear of its claims rather than endure the lengthy, expensive process of contesting it.
What’s more, software patents are routinely granted even though the filer doesn’t have any evidence that they can do the thing claimed by the patent. That is, you can patent an “invention” that you haven’t actually made and that you don’t know how to make.
With these considerations in hand, it becomes obvious that the fact that a Big Tech company has patented what it says is an effective mind-control ray is largely irrelevant to whether Big Tech can in fact control our minds.
Big Tech collects our data for many reasons, including the diminishing returns on existing stores of data. But many tech companies also collect data out of a mistaken tech exceptionalist belief in the network effects of data. Network effects occur when each new user in a system increases its value. The classic example is fax machines: A single fax machine is of no use, two fax machines are of limited use, but every new fax machine that’s put to use after the first doubles the number of possible fax-to-fax links.
Data mined for predictive systems doesn’t necessarily produce these dividends. Think of Netflix: The predictive value of the data mined from a million English-speaking Netflix viewers is hardly improved by the addition of one more user’s viewing data. Most of the data Netflix acquires after that first minimum viable sample duplicates existing data and produces only minimal gains. Meanwhile, retraining models with new data gets progressively more expensive as the number of data points increases, and manual tasks like labeling and validating data do not get cheaper at scale.
Businesses pursue fads to the detriment of their profits all the time, especially when the businesses and their investors are not motivated by the prospect of becoming profitable but rather by the prospect of being acquired by a Big Tech giant or by having an IPO. For these firms, ticking faddish boxes like “collects as much data as possible” might realize a bigger return on investment than “collects a business-appropriate quantity of data.”
This is another harm of tech exceptionalism: The belief that more data always produces more profits in the form of more insights that can be translated into better mind-control rays drives firms to over-collect and over-retain data beyond all rationality. And since the firms are behaving irrationally, a good number of them will go out of business and become ghost ships whose cargo holds are stuffed full of data that can harm people in myriad ways — but which no one is responsible for antey longer. Even if the companies don’t go under, the data they collect is maintained behind the minimum viable security — just enough security to keep the company viable while it waits to get bought out by a tech giant, an amount calculated to spend not one penny more than is necessary on protecting data.
Image for post
How monopolies, not mind control, drive surveillance capitalism: The Snapchat story
For the first decade of its existence, Facebook competed with the social media giants of the day (Myspace, Orkut, etc.) by presenting itself as the pro-privacy alternative. Indeed, Facebook justified its walled garden — which let users bring in data from the web but blocked web services like Google Search from indexing and caching Facebook pages — as a pro-privacy measure that protected users from the surveillance-happy winners of the social media wars like Myspace.
Despite frequent promises that it would never collect or analyze its users’ data, Facebook periodically created initiatives that did just that, like the creepy, ham-fisted Beacon tool, which spied on you as you moved around the web and then added your online activities to your public timeline, allowing your friends to monitor your browsing habits. Beacon sparked a user revolt. Every time, Facebook backed off from its surveillance initiative, but not all the way; inevitably, the new Facebook would be more surveilling than the old Facebook, though not quite as surveilling as the intermediate Facebook following the launch of the new product or service.
The pace at which Facebook ramped up its surveillance efforts seems to have been set by Facebook’s competitive landscape. The more competitors Facebook had, the better it behaved. Every time a major competitor foundered, Facebook’s behavior got markedly worse.
All the while, Facebook was prodigiously acquiring companies, including a company called Onavo. Nominally, Onavo made a battery-monitoring mobile app. But the permissions that Onavo required were so expansive that the app was able to gather fine-grained telemetry on everything users did with their phones, including which apps they used and how they were using them.
Through Onavo, Facebook discovered that it was losing market share to Snapchat, an app that — like Facebook a decade before — billed itself as the pro-privacy alternative to the status quo. Through Onavo, Facebook was able to mine data from the devices of Snapchat users, including both current and former Snapchat users. This spurred Facebook to acquire Instagram — some features of which competed with Snapchat — and then allowed Facebook to fine-tune Instagram’s features and sales pitch to erode Snapchat’s gains and ensure that Facebook would not have to face the kinds of competitive pressures it had earlier inflicted on Myspace and Orkut.
The story of how Facebook crushed Snapchat reveals the relationship between monopoly and surveillance capitalism. Facebook combined surveillance with lax antitrust enforcement to spot the competitive threat of Snapchat on its horizon and then take decisive action against it. Facebook’s surveillance capitalism let it avert competitive pressure with anti-competitive tactics. Facebook users still want privacy — Facebook hasn’t used surveillance to brainwash them out of it — but they can’t get it because Facebook’s surveillance lets it destroy any hope of a rival service emerging that competes on privacy features.
A monopoly over your friends
A decentralization movement has tried to erode the dominance of Facebook and other Big Tech companies by fielding “indieweb” alternatives — Mastodon as a Twitter alternative, Diaspora as a Facebook alternative, etc. — but these efforts have failed to attain any kind of liftoff.
Fundamentally, each of these services is hamstrung by the same problem: Every potential user for a Facebook or Twitter alternative has to convince all their friends to follow them to a decentralized web alternative in order to continue to realize the benefit of social media. For many of us, the only reason to have a Facebook account is that our friends have Facebook accounts, and the reason they have Facebook accounts is that we have Facebook accounts.
All of this has conspired to make Facebook — and other dominant platforms — into “kill zones” that investors will not fund new entrants for.
And yet, all of today’s tech giants came into existence despite the entrenched advantage of the companies that came before them. To understand how that happened, you have to understand both interoperability and adversarial interoperability.
The hard problem of our species is coordination.
“Interoperability” is the ability of two technologies to work with one another: Anyone can make an LP that will play on any record player, anyone can make a filter you can install in your stove’s extractor fan, anyone can make gasoline for your car, anyone can make a USB phone charger that fits in your car’s cigarette lighter receptacle, anyone can make a light bulb that works in your light socket, anyone can make bread that will toast in your toaster.
Interoperability is often a source of innovation and consumer benefit: Apple made the first commercially successful PC, but millions of independent software vendors made interoperable programs that ran on the Apple II Plus. The simple analog antenna inputs on the back of TVs first allowed cable operators to connect directly to TVs, then they allowed game console companies and then personal computer companies to use standard televisions as displays. Standard RJ-11 telephone jacks allowed for the production of phones from a variety of vendors in a variety of forms, from the free football-shaped phone that came with a Sports Illustrated subscription to business phones with speakers, hold functions, and so on and then answering machines and finally modems, paving the way for the internet revolution.
“Interoperability” is often used interchangeably with “standardization,” which is the process when manufacturers and other stakeholders hammer out a set of agreed-upon rules for implementing a technology, such as the electrical plug on your wall, the CAN bus used by your car’s computer systems, or the HTML instructions that your browser interprets.
But interoperability doesn’t require standardization — indeed, standardization often proceeds from the chaos of ad hoc interoperability measures. The inventor of the cigarette-lighter USB charger didn’t need to get permission from car manufacturers or even the manufacturers of the dashboard lighter subcomponent. The automakers didn’t take any countermeasures to prevent the use of these aftermarket accessories by their customers, but they also didn’t do anything to make life easier for the chargers’ manufacturers. This is a kind of “neutral interoperability.”
Beyond neutral interoperability, there is “adversarial interoperability.” That’s when a manufacturer makes a product that interoperates with another manufacturer’s product despite the second manufacturer’s objections and even if that means bypassing a security system designed to prevent interoperability.
Probably the most familiar form of adversarial interoperability is third-party printer ink. Printer manufacturers claim that they sell printers below cost and that the only way they can recoup the losses they incur is by charging high markups on ink. To prevent the owners of printers from buying ink elsewhere, the printer companies deploy a suite of anti-customer security systems that detect and reject both refilled and third-party cartridges.
Owners of printers take the position that HP and Epson and Brother are not charities and that customers for their wares have no obligation to help them survive, and so if the companies choose to sell their products at a loss, that’s their foolish choice and their consequences to live with. Likewise, competitors who make ink or refill kits observe that they don’t owe printer companies anything, and their erosion of printer companies’ margins are the printer companies’ problems, not their competitors’. After all, the printer companies shed no tears when they drive a refiller out of business, so why should the refillers concern themselves with the economic fortunes of the printer companies?
Adversarial interoperability has played an outsized role in the history of the tech industry: from the founding of the “alt.*” Usenet hierarchy (which was started against the wishes of Usenet’s maintainers and which grew to be bigger than all of Usenet combined) to the browser wars (when Netscape and Microsoft devoted massive engineering efforts to making their browsers incompatible with the other’s special commands and peccadilloes) to Facebook (whose success was built in part by helping its new users stay in touch with friends they’d left behind on Myspace because Facebook supplied them with a tool that scraped waiting messages from Myspace and imported them into Facebook, effectively creating an Facebook-based Myspace reader).
Today, incumbency is seen as an unassailable advantage. Facebook is where all of your friends are, so no one can start a Facebook competitor. But adversarial compatibility reverses the competitive advantage: If you were allowed to compete with Facebook by providing a tool that imported all your users’ waiting Facebook messages into an environment that competed on lines that Facebook couldn’t cross, like eliminating surveillance and ads, then Facebook would be at a huge disadvantage. It would have assembled all possible ex-Facebook users into a single, easy-to-find service; it would have educated them on how a Facebook-like service worked and what its potential benefits were; and it would have provided an easy means for disgruntled Facebook users to tell their friends where they might expect better treatment.
Adversarial interoperability was once the norm and a key contributor to the dynamic, vibrant tech scene, but now it is stuck behind a thicket of laws and regulations that add legal risks to the tried-and-true tactics of adversarial interoperability. New rules and new interpretations of existing rules mean that a would-be adversarial interoperator needs to steer clear of claims under copyright, terms of service, trade secrecy, tortious interference, and patent.
In the absence of a competitive market, lawmakers have resorted to assigning expensive, state-like duties to Big Tech firms, such as automatically filtering user contributions for copyright infringement or terrorist and extremist content or detecting and preventing harassment in real time or controlling access to sexual material.
These measures put a floor under how small we can make Big Tech because only the very largest companies can afford the humans and automated filters needed to perform these duties.
But that’s not the only way in which making platforms responsible for policing their users undermines competition. A platform that is expected to police its users’ conduct must prevent many vital adversarial interoperability techniques lest these subvert its policing measures. For example, if someone using a Twitter replacement like Mastodon is able to push messages into Twitter and read messages out of Twitter, they could avoid being caught by automated systems that detect and prevent harassment (such as systems that use the timing of messages or IP-based rules to make guesses about whether someone is a harasser).
To the extent that we are willing to let Big Tech police itself — rather than making Big Tech small enough that users can leave bad platforms for better ones and small enough that a regulation that simply puts a platform out of business will not destroy billions of users’ access to their communities and data — we build the case that Big Tech should be able to block its competitors and make it easier for Big Tech to demand legal enforcement tools to ban and punish attempts at adversarial interoperability.
Ultimately, we can try to fix Big Tech by making it responsible for bad acts by its users, or we can try to fix the internet by cutting Big Tech down to size. But we can’t do both. To replace today’s giant products with pluralistic protocols, we need to clear the legal thicket that prevents adversarial interoperability so that tomorrow’s nimble, personal, small-scale products can federate themselves with giants like Facebook, allowing the users who’ve left to continue to communicate with users who haven’t left yet, reaching tendrils over Facebook’s garden wall that Facebook’s trapped users can use to scale the walls and escape to the global, open web.
Fake news is an epistemological crisis
Tech is not the only industry that has undergone massive concentration since the Reagan era. Virtually every major industry — from oil to newspapers to meatpacking to sea freight to eyewear to online pornography — has become a clubby oligarchy that just a few players dominate.
At the same time, every industry has become something of a tech industry as general-purpose computers and general-purpose networks and the promise of efficiencies through data-driven analysis infuse every device, process, and firm with tech.
This phenomenon of industrial concentration is part of a wider story about wealth concentration overall as a smaller and smaller number of people own more and more of our world. This concentration of both wealth and industries means that our political outcomes are increasingly beholden to the parochial interests of the people and companies with all the money.
That means that whenever a regulator asks a question with an obvious, empirical answer (“Are humans causing climate change?” or “Should we let companies conduct commercial mass surveillance?” or “Does society benefit from allowing network neutrality violations?”), the answer that comes out is only correct if that correctness meets with the approval of rich people and the industries that made them so wealthy.
Rich people have always played an outsized role in politics and more so since the Supreme Court’s Citizens United decision eliminated key controls over political spending. Widening inequality and wealth concentration means that the very richest people are now a lot richer and can afford to spend a lot more money on political projects than ever before. Think of the Koch brothers or George Soros or Bill Gates.
But the policy distortions of rich individuals pale in comparison to the policy distortions that concentrated industries are capable of. The companies in highly concentrated industries are much more profitable than companies in competitive industries — no competition means not having to reduce prices or improve quality to win customers — leaving them with bigger capital surpluses to spend on lobbying.
Concentrated industries also find it easier to collaborate on policy objectives than competitive ones. When all the top execs from your industry can fit around a single boardroom table, they often do. And when they do, they can forge a consensus position on regulation.
Rising through the ranks in a concentrated industry generally means working at two or three of the big companies. When there are only relatively few companies in a given industry, each company has a more ossified executive rank, leaving ambitious execs with fewer paths to higher positions unless they are recruited to a rival. This means that the top execs in concentrated industries are likely to have been colleagues at some point and socialize in the same circles — connected through social ties or, say, serving as trustees for each others’ estates. These tight social bonds foster a collegial, rather than competitive, attitude.
Highly concentrated industries also present a regulatory conundrum. When an industry is dominated by just four or five companies, the only people who are likely to truly understand the industry’s practices are its veteran executives. This means that top regulators are often former execs of the companies they are supposed to be regulating. These turns in government are often tacitly understood to be leaves of absence from industry, with former employers welcoming their erstwhile watchdogs back into their executive ranks once their terms have expired.
All this is to say that the tight social bonds, small number of firms, and regulatory capture of concentrated industries give the companies that comprise them the power to dictate many, if not all, of the regulations that bind them.
This is increasingly obvious. Whether it’s payday lenders winning the right to practice predatory lending or Apple winning the right to decide who can fix your phone or Google and Facebook winning the right to breach your private data without suffering meaningful consequences or victories for pipeline companies or impunity for opioid manufacturers or massive tax subsidies for incredibly profitable dominant businesses, it’s increasingly apparent that many of our official, evidence-based truth-seeking processes are, in fact, auctions for sale to the highest bidder.
It’s really impossible to overstate what a terrifying prospect this is. We live in an incredibly high-tech society, and none of us could acquire the expertise to evaluate every technological proposition that stands between us and our untimely, horrible deaths. You might devote your life to acquiring the media literacy to distinguish good scientific journals from corrupt pay-for-play lookalikes and the statistical literacy to evaluate the quality of the analysis in the journals as well as the microbiology and epidemiology knowledge to determine whether you can trust claims about the safety of vaccines — but that would still leave you unqualified to judge whether the wiring in your home will give you a lethal shock and whether your car’s brakes’ software will cause them to fail unpredictably and whether the hygiene standards at your butcher are sufficient to keep you from dying after you finish your dinner.
In a world as complex as this one, we have to defer to authorities, and we keep them honest by making those authorities accountable to us and binding them with rules to prevent conflicts of interest. We can’t possibly acquire the expertise to adjudicate conflicting claims about the best way to make the world safe and prosperous, but we can determine whether the adjudication process itself is trustworthy.
Right now, it’s obviously not.
The past 40 years of rising inequality and industry concentration, together with increasingly weak accountability and transparency for expert agencies, has created an increasingly urgent sense of impending doom, the sense that there are vast conspiracies afoot that operate with tacit official approval despite the likelihood they are working to better themselves by ruining the rest of us.
For example, it’s been decades since Exxon’s own scientists concluded that its products would render the Earth uninhabitable by humans. And yet those decades were lost to us, in large part because Exxon lobbied governments and sowed doubt about the dangers of its products and did so with the cooperation of many public officials. When the survival of you and everyone you love is threatened by conspiracies, it’s not unreasonable to start questioning the things you think you know in an attempt to determine whether they, too, are the outcome of another conspiracy.
The collapse of the credibility of our systems for divining and upholding truths has left us in a state of epistemological chaos. Once, most of us might have assumed that the system was working and that our regulations reflected our best understanding of the empirical truths of the world as they were best understood — now we have to find our own experts to help us sort the true from the false.
If you’re like me, you probably believe that vaccines are safe, but you (like me) probably also can’t explain the microbiology or statistics. Few of us have the math skills to review the literature on vaccine safety and describe why their statistical reasoning is sound. Likewise, few of us can review the stats in the (now discredited) literature on opioid safety and explain how those stats were manipulated. Both vaccines and opioids were embraced by medical authorities, after all, and one is safe while the other could ruin your life. You’re left with a kind of inchoate constellation of rules of thumb about which experts you trust to fact-check controversial claims and then to explain how all those respectable doctors with their peer-reviewed research on opioid safety were an aberration and then how you know that the doctors writing about vaccine safety are not an aberration.
I’m 100% certain that vaccinating is safe and effective, but I’m also at something of a loss to explain exactly, precisely, why I believe this, given all the corruption I know about and the many times the stamp of certainty has turned out to be a parochial lie told to further enrich the super rich.
Fake news — conspiracy theories, racist ideologies, scientific denialism — has always been with us. What’s changed today is not the mix of ideas in the public discourse but the popularity of the worst ideas in that mix. Conspiracy and denial have skyrocketed in lockstep with the growth of Big Inequality, which has also tracked the rise of Big Tech and Big Pharma and Big Wrestling and Big Car and Big Movie Theater and Big Everything Else.
No one can say for certain why this has happened, but the two dominant camps are idealism (the belief that the people who argue for these conspiracies have gotten better at explaining them, maybe with the help of machine-learning tools) or materialism (the ideas have become more attractive because of material conditions in the world).
I’m a materialist. I’ve been exposed to the arguments of conspiracy theorists all my life, and I have not experienced any qualitative leap in the quality of those arguments.
The major difference is in the world, not the arguments. In a time where actual conspiracies are commonplace, conspiracy theories acquire a ring of plausibility.
We have always had disagreements about what’s true, but today, we have a disagreement over how we know whether something is true. This is an epistemological crisis, not a crisis over belief. It’s a crisis over the credibility of our truth-seeking exercises, from scientific journals (in an era where the biggest journal publishers have been caught producing pay-to-play journals for junk science) to regulations (in an era where regulators are routinely cycling in and out of business) to education (in an era where universities are dependent on corporate donations to keep their lights on).
Targeting — surveillance capitalism — makes it easier to find people who are undergoing this epistemological crisis, but it doesn’t create the crisis. For that, you need to look to corruption.
And, conveniently enough, it’s corruption that allows surveillance capitalism to grow by dismantling monopoly protections, by permitting reckless collection and retention of personal data, by allowing ads to be targeted in secret, and by foreclosing on the possibility of going somewhere else where you might continue to enjoy your friends without subjecting yourself to commercial surveillance.
Image for post
Tech is different
I reject both iterations of technological exceptionalism. I reject the idea that tech is uniquely terrible and led by people who are greedier or worse than the leaders of other industries, and I reject the idea that tech is so good — or so intrinsically prone to concentration — that it can’t be blamed for its present-day monopolistic status.
I think tech is just another industry, albeit one that grew up in the absence of real monopoly constraints. It may have been first, but it isn’t the worst nor will it be the last.
But there’s one way in which I am a tech exceptionalist. I believe that online tools are the key to overcoming problems that are much more urgent than tech monopolization: climate change, inequality, misogyny, and discrimination on the basis of race, gender identity, and other factors. The internet is how we will recruit people to fight those fights, and how we will coordinate their labor. Tech is not a substitute for democratic accountability, the rule of law, fairness, or stability — but it’s a means to achieve these things.
The hard problem of our species is coordination. Everything from climate change to social change to running a business to making a family work can be viewed as a collective action problem.
The internet makes it easier than at any time before to find people who want to work on a project with you — hence the success of free and open-source software, crowdfunding, and racist terror groups — and easier than ever to coordinate the work you do.
The internet and the computers we connect to it also possess an exceptional quality: general-purposeness. The internet is designed to allow any two parties to communicate any data, using any protocol, without permission from anyone else. The only production design we have for computers is the general-purpose, “Turing complete” computer that can run every program we can express in symbolic logic.
This means that every time someone with a special communications need invests in infrastructure and techniques to make the internet faster, cheaper, and more robust, this benefit redounds to everyone else who is using the internet to communicate. And this also means that every time someone with a special computing need invests to make computers faster, cheaper, and more robust, every other computing application is a potential beneficiary of this work.
For these reasons, every type of communication is gradually absorbed into the internet, and every type of device — from airplanes to pacemakers — eventually becomes a computer in a fancy case.
While these considerations don’t preclude regulating networks and computers, they do call for gravitas and caution when doing so because changes to regulatory frameworks could ripple out to have unintended consequences in many, many other domains.
The upshot of this is that our best hope of solving the big coordination problems — climate change, inequality, etc. — is with free, fair, and open tech. Our best hope of keeping tech free, fair, and open is to exercise caution in how we regulate tech and to attend closely to the ways in which interventions to solve one problem might create problems in other domains.
Ownership of facts
Big Tech has a funny relationship with information. When you’re generating information — anything from the location data streaming off your mobile device to the private messages you send to friends on a social network — it claims the rights to make unlimited use of that data.
But when you have the audacity to turn the tables — to use a tool that blocks ads or slurps your waiting updates out of a social network and puts them in another app that lets you set your own priorities and suggestions or crawls their system to allow you to start a rival business — they claim that you’re stealing from them.
The thing is, information is a very bad fit for any kind of private property regime. Property rights are useful for establishing markets that can lead to the effective development of fallow assets. These markets depend on clear titles to ensure that the things being bought and sold in them can, in fact, be bought and sold.
Information rarely has such a clear title. Take phone numbers: There’s clearly something going wrong when Facebook slurps up millions of users’ address books and uses the phone numbers it finds in them to plot out social graphs and fill in missing information about other users.
But the phone numbers Facebook nonconsensually acquires in this transaction are not the “property” of the users they’re taken from nor do they belong to the people whose phones ring when you dial those numbers. The numbers are mere integers,
                10 digits in the U.S. and Canada, and they appear in millions of places, including somewhere deep in pi as well as numerous other contexts. Giving people ownership titles to integers is an obviously terrible idea.
Likewise for the facts that Facebook and other commercial surveillance operators acquire about us, like that we are the children of our parents or the parents to our children or that we had a conversation with someone else or went to a public place. These data points can’t be property in the sense that your house or your shirt is your property because the title to them is intrinsically muddy: Does your mom own the fact that she is your mother? Do you? Do both of you? What about your dad — does he own this fact too, or does he have to license the fact from you (or your mom or both of you) in order to use this fact? What about the hundreds or thousands of other people who know these facts?
If you go to a Black Lives Matter demonstration, do the other demonstrators need your permission to post their photos from the event? The online fights over when and how to post photos from demonstrations reveal a nuanced, complex issue that cannot be easily hand-waved away by giving one party a property right that everyone else in the mix has to respect.
The fact that information isn’t a good fit with property and markets doesn’t mean that it’s not valuable. Babies aren’t property, but they’re inarguably valuable. In fact, we have a whole set of rules just for babies as well as a subset of those rules that apply to humans more generally. Someone who argues that babies won’t be truly valuable until they can be bought and sold like loaves of bread would be instantly and rightfully condemned as a monster.
It’s tempting to reach for the property hammer when Big Tech treats your information like a nail — not least because Big Tech are such prolific abusers of property hammers when it comes to their information. But this is a mistake. If we allow markets to dictate the use of our information, then we’ll find that we’re sellers in a buyers’ market where the Big Tech monopolies set a price for our data that is so low as to be insignificant or, more likely, set at a nonnegotiable price of zero in a click-through agreement that you don’t have the opportunity to modify.
Meanwhile, establishing property rights over information will create insurmountable barriers to independent data processing. Imagine that we require a license to be negotiated when a translated document is compared with its original, something Google has done and continues to do billions of times to train its automated language translation tools. Google can afford this, but independent third parties cannot. Google can staff a clearances department to negotiate one-time payments to the likes of the EU (one of the major repositories of translated documents) while independent watchdogs wanting to verify that the translations are well-prepared, or to root out bias in translations, will find themselves needing a staffed-up legal department and millions for licenses before they can even get started.
The same goes for things like search indexes of the web or photos of peoples’ houses, which have become contentious thanks to Google’s Street View project. Whatever problems may exist with Google’s photographing of street scenes, resolving them by letting people decide who can take pictures of the facades of their homes from a public street will surely create even worse ones. Think of how street photography is important for newsgathering — including informal newsgathering, like photographing abuses of authority — and how being able to document housing and street life are important for contesting eminent domain, advocating for social aid, reporting planning and zoning violations, documenting discriminatory and unequal living conditions, and more.
The ownership of facts is antithetical to many kinds of human progress. It’s hard to imagine a rule that limits Big Tech’s exploitation of our collective labors without inadvertently banning people from gathering data on online harassment or compiling indexes of changes in language or simply investigating how the platforms are shaping our discourse — all of which require scraping data that other people have created and subjecting it to scrutiny and analysis.
Persuasion works… slowly
The platforms may oversell their ability to persuade people, but obviously, persuasion works sometimes. Whether it’s the private realm that LGBTQ people used to recruit allies and normalize sexual diversity or the decadeslong project to convince people that markets are the only efficient way to solve complicated resource allocation problems, it’s clear that our societal attitudes can change.
The project of shifting societal attitudes is a game of inches and years. For centuries, svengalis have purported to be able to accelerate this process, but even the most brutal forms of propaganda have struggled to make permanent changes. Joseph Goebbels was able to subject Germans to daily, mandatory, hourslong radio broadcasts, to round up and torture and murder dissidents, and to seize full control over their children’s education while banning any literature, broadcasts, or films that did not comport with his worldview.
Yet, after 12 years of terror, once the war ended, Nazi ideology was largely discredited in both East and West Germany, and a program of national truth and reconciliation was put in its place. Racism and authoritarianism were never fully abolished in Germany, but neither were the majority of Germans irrevocably convinced of Nazism — and the rise of racist authoritarianism in Germany today tells us that the liberal attitudes that replaced Nazism were no more permanent than Nazism itself.
Racism and authoritarianism have also always been with us. Anyone who’s reviewed the kind of messages and arguments that racists put forward today would be hard-pressed to say that they have gotten better at presenting their ideas. The same pseudoscience, appeals to fear, and circular logic that racists presented in the 1980s, when the cause of white supremacy was on the wane, are to be found in the communications of leading white nationalists today.
If racists haven’t gotten more convincing in the past decade, then how is it that more people were convinced to be openly racist at that time? I believe that the answer lies in the material world, not the world of ideas. The ideas haven’t gotten more convincing, but people have become more afraid. Afraid that the state can’t be trusted to act as an honest broker in life-or-death decisions, from those regarding the management of the economy to the regulation of painkillers to the rules for handling private information. Afraid that the world has become a game of musical chairs in which the chairs are being taken away at a never-before-seen rate. Afraid that justice for others will come at their expense. Monopolism isn’t the cause of these fears, but the inequality and material desperation and policy malpractice that monopolism contributes to is a significant contributor to these conditions. Inequality creates the conditions for both conspiracies and violent racist ideologies, and then surveillance capitalism lets opportunists target the fearful and the conspiracy-minded.
Image for post
Paying won’t help
As the old saw goes, “If you’re not paying for the product, you’re the product.”
It’s a commonplace belief today that the advent of free, ad-supported media was the original sin of surveillance capitalism. The reasoning is that the companies that charged for access couldn’t “compete with free” and so they were driven out of business. Their ad-supported competitors, meanwhile, declared open season on their users’ data in a bid to improve their ad targeting and make more money and then resorted to the most sensationalist tactics to generate clicks on those ads. If only we’d pay for media again, we’d have a better, more responsible, more sober discourse that would be better for democracy.
But the degradation of news products long precedes the advent of ad-supported online news. Long before newspapers were online, lax antitrust enforcement had opened the door for unprecedented waves of consolidation and roll-ups in newsrooms. Rival newspapers were merged, reporters and ad sales staff were laid off, physical plants were sold and leased back, leaving the companies loaded up with debt through leveraged buyouts and subsequent profit-taking by the new owners. In other words, it wasn’t merely shifts in the classified advertising market, which was long held to be the primary driver in the decline of the traditional newsroom, that made news companies unable to adapt to the internet — it was monopolism.
Then, as news companies did come online, the ad revenues they commanded dropped even as the number of internet users (and thus potential online readers) increased. That shift was a function of consolidation in the ad sales market, with Google and Facebook emerging as duopolists who made more money every year from advertising while paying less and less of it to the publishers whose work the ads appeared alongside. Monopolism created a buyer’s market for ad inventory with Facebook and Google acting as gatekeepers.
Paid services continue to exist alongside free ones, and often it is these paid services — anxious to prevent people from bypassing their paywalls or sharing paid media with freeloaders — that exert the most control over their customers. Apple’s iTunes and App Stores are paid services, but to maximize their profitability, Apple has to lock its platforms so that third parties can’t make compatible software without permission. These locks allow the company to exercise both editorial control (enabling it to exclude controversial political material) and technological control, including control over who can repair the devices it makes. If we’re worried that ad-supported products deprive people of their right to self-determination by using persuasion techniques to nudge their purchase decisions a few degrees in one direction or the other, then the near-total control a single company holds over the decision of who gets to sell you software, parts, and service for your iPhone should have us very worried indeed.
We shouldn’t just be concerned about payment and control: The idea that paying will improve discourse is also dangerously wrong. The poor success rate of targeted advertising means that the platforms have to incentivize you to “engage” with posts at extremely high levels to generate enough pageviews to safeguard their profits. As discussed earlier, to increase engagement, platforms like Facebook use machine learning to guess which messages will be most inflammatory and make a point of shoving those into your eyeballs at every turn so that you will hate-click and argue with people.
Perhaps paying would fix this, the reasoning goes. If platforms could be economically viable even if you stopped clicking on them once your intellectual and social curiosity had been slaked, then they would have no reason to algorithmically enrage you to get more clicks out of you, right?
There may be something to that argument, but it still ignores the wider economic and political context of the platforms and the world that allowed them to grow so dominant.
Platforms are world-spanning and all-encompassing because they are monopolies, and they are monopolies because we have gutted our most important and reliable anti-monopoly rules. Antitrust was neutered as a key part of the project to make the wealthy wealthier, and that project has worked. The vast majority of people on Earth have a negative net worth, and even the dwindling middle class is in a precarious state, undersaved for retirement, underinsured for medical disasters, and undersecured against climate and technology shocks.
In this wildly unequal world, paying doesn’t improve the discourse; it simply prices discourse out of the range of the majority of people. Paying for the product is dandy, if you can afford it.
If you think today’s filter bubbles are a problem for our discourse, imagine what they’d be like if rich people inhabited free-flowing Athenian marketplaces of ideas where you have to pay for admission while everyone else lives in online spaces that are subsidized by wealthy benefactors who relish the chance to establish conversational spaces where the “house rules” forbid questioning the status quo. That is, imagine if the rich seceded from Facebook, and then, instead of running ads that made money for shareholders, Facebook became a billionaire’s vanity project that also happened to ensure that nobody talked about whether it was fair that only billionaires could afford to hang out in the rarified corners of the internet.
Behind the idea of paying for access is a belief that free markets will address Big Tech’s dysfunction. After all, to the extent that people have a view of surveillance at all, it is generally an unfavorable one, and the longer and more thoroughly one is surveilled, the less one tends to like it. Same goes for lock-in: If HP’s ink or Apple’s App Store were really obviously fantastic, they wouldn’t need technical measures to prevent users from choosing a rival’s product. The only reason these technical countermeasures exist is that the companies don’t believe their customers would voluntarily submit to their terms, and they want to deprive them of the choice to take their business elsewhere.
Advocates for markets laud their ability to aggregate the diffused knowledge of buyers and sellers across a whole society through demand signals, price signals, and so on. The argument for surveillance capitalism being a “rogue capitalism” is that machine-learning-driven persuasion techniques distort decision-making by consumers, leading to incorrect signals — consumers don’t buy what they prefer, they buy what they’re tricked into preferring. It follows that the monopolistic practices of lock-in, which do far more to constrain consumers’ free choices, are even more of a “rogue capitalism.”
The profitability of any business is constrained by the possibility that its customers will take their business elsewhere. Both surveillance and lock-in are anti-features that no customer wants. But monopolies can capture their regulators, crush their competitors, insert themselves into their customers’ lives, and corral people into “choosing” their services regardless of whether they want them — it’s fine to be terrible when there is no alternative.
Ultimately, surveillance and lock-in are both simply business strategies that monopolists can choose. Surveillance companies like Google are perfectly capable of deploying lock-in technologies — just look at the onerous Android licensing terms that require device-makers to bundle in Google’s suite of applications. And lock-in companies like Apple are perfectly capable of subjecting their users to surveillance if it means keeping the Chinese government happy and preserving ongoing access to Chinese markets. Monopolies may be made up of good, ethical people, but as institutions, they are not your friend — they will do whatever they can get away with to maximize their profits, and the more monopolistic they are, the more they can get away with.
Image for post
An “ecology” moment for trustbusting
If we’re going to break Big Tech’s death grip on our digital lives, we’re going to have to fight monopolies. That may sound pretty mundane and old-fashioned, something out of the New Deal era, while ending the use of automated behavioral modification feels like the plotline of a really cool cyberpunk novel.
Meanwhile, breaking up monopolies is something we seem to have forgotten how to do. There is a bipartisan, trans-Atlantic consensus that breaking up companies is a fool’s errand at best — liable to mire your federal prosecutors in decades of litigation — and counterproductive at worst, eroding the “consumer benefits” of large companies with massive efficiencies of scale.
But trustbusters once strode the nation, brandishing law books, terrorizing robber barons, and shattering the illusion of monopolies’ all-powerful grip on our society. The trustbusting era could not begin until we found the political will — until the people convinced politicians they’d have their backs when they went up against the richest, most powerful men in the world.
Could we find that political will again?
Copyright scholar James Boyle has described how the term “ecology” marked a turning point in environmental activism. Prior to the adoption of this term, people who wanted to preserve whale populations didn’t necessarily see themselves as fighting the same battle as people who wanted to protect the ozone layer or fight freshwater pollution or beat back smog or acid rain.
But the term “ecology” welded these disparate causes together into a single movement, and the members of this movement found solidarity with one another. The people who cared about smog signed petitions circulated by the people who wanted to end whaling, and the anti-whalers marched alongside the people demanding action on acid rain. This uniting behind a common cause completely changed the dynamics of environmentalism, setting the stage for today’s climate activism and the sense that preserving the habitability of the planet Earth is a shared duty among all people.
I believe we are on the verge of a new “ecology” moment dedicated to combating monopolies. After all, tech isn’t the only concentrated industry nor is it even the most concentrated of industries.
You can find partisans for trustbusting in every sector of the economy. Everywhere you look, you can find people who’ve been wronged by monopolists who’ve trashed their finances, their health, their privacy, their educations, and the lives of people they love. Those people have the same cause as the people who want to break up Big Tech and the same enemies. When most of the world’s wealth is in the hands of a very few, it follows that nearly every large company will have overlapping shareholders.
That’s the good news: With a little bit of work and a little bit of coalition building, we have more than enough political will to break up Big Tech and every other concentrated industry besides. First we take Facebook, then we take AT&T/WarnerMedia.
But here’s the bad news: Much of what we’re doing to tame Big Tech instead of breaking up the big companies also forecloses on the possibility of breaking them up later.
Big Tech’s concentration currently means that their inaction on harassment, for example, leaves users with an impossible choice: absent themselves from public discourse by, say, quitting Twitter or endure vile, constant abuse. Big Tech’s over-collection and over-retention of data results in horrific identity theft. And their inaction on extremist recruitment means that white supremacists who livestream their shooting rampages can reach an audience of billions. The combination of tech concentration and media concentration means that artists’ incomes are falling even as the revenue generated by their creations are increasing.
Yet governments confronting all of these problems all inevitably converge on the same solution: deputize the Big Tech giants to police their users and render them liable for their users’ bad actions. The drive to force Big Tech to use automated filters to block everything from copyright infringement to sex-trafficking to violent extremism means that tech companies will have to allocate hundreds of millions to run these compliance systems.
These rules — the EU’s new Directive on Copyright, Australia’s new terror regulation, America’s FOSTA/SESTA sex-trafficking law and more — are not just death warrants for small, upstart competitors that might challenge Big Tech’s dominance but who lack the deep pockets of established incumbents to pay for all these automated systems. Worse still, these rules put a floor under how small we can hope to make Big Tech.
That’s because any move to break up Big Tech and cut it down to size will have to cope with the hard limit of not making these companies so small that they can no longer afford to perform these duties — and it’s expensive to invest in those automated filters and outsource content moderation. It’s already going to be hard to unwind these deeply concentrated, chimeric behemoths that have been welded together in the pursuit of monopoly profits. Doing so while simultaneously finding some way to fill the regulatory void that will be left behind if these self-policing rulers were forced to suddenly abdicate will be much, much harder.
Allowing the platforms to grow to their present size has given them a dominance that is nearly insurmountable — deputizing them with public duties to redress the pathologies created by their size makes it virtually impossible to reduce that size. Lather, rinse, repeat: If the platforms don’t get smaller, they will get larger, and as they get larger, they will create more problems, which will give rise to more public duties for the companies, which will make them bigger still.
We can work to fix the internet by breaking up Big Tech and depriving them of monopoly profits, or we can work to fix Big Tech by making them spend their monopoly profits on governance. But we can’t do both. We have to choose between a vibrant, open internet or a dominated, monopolized internet commanded by Big Tech giants that we struggle with constantly to get them to behave themselves.
Make Big Tech small again
Trustbusting is hard. Breaking big companies into smaller ones is expensive and time-consuming. So time-consuming that by the time you’re done, the world has often moved on and rendered years of litigation irrelevant. From 1969 to 1982, the U.S. government pursued an antitrust case against IBM over its dominance of mainframe computing — but the case collapsed in 1982 because mainframes were being speedily replaced by PCs.
A future U.S. president could simply direct their attorney general to enforce the law as it was written.
It’s far easier to prevent concentration than to fix it, and reinstating the traditional contours of U.S. antitrust enforcement will, at the very least, prevent further concentration. That means bans on mergers between large companies, on big companies acquiring nascent competitors, and on platform companies competing directly with the companies that rely on the platforms.
These powers are all in the plain language of U.S. antitrust laws, so in theory, a future U.S. president could simply direct their attorney general to enforce the law as it was written. But after decades of judicial “education” in the benefits of monopolies, after multiple administrations that have packed the federal courts with lifetime-appointed monopoly cheerleaders, it’s not clear that mere administrative action would do the trick.
If the courts frustrate the Justice Department and the president, the next stop would be Congress, which could eliminate any doubt about how antitrust law should be enforced in the U.S. by passing new laws that boil down to saying, “Knock it off. We all know what the Sherman Act says. Robert Bork was a deranged fantasist. For avoidance of doubt, fuck that guy.” In other words, the problem with monopolies is monopolism — the concentration of power into too few hands, which erodes our right to self-determination. If there is a monopoly, the law wants it gone, period. Sure, get rid of monopolies that create “consumer harm” in the form of higher prices, but also, get rid of other monopolies, too.
But this only prevents things from getting worse. To help them get better, we will have to build coalitions with other activists in the anti-monopoly ecology movement — a pluralism movement or a self-determination movement — and target existing monopolies in every industry for breakup and structural separation rules that prevent, for example, the giant eyewear monopolist Luxottica from dominating both the sale and the manufacture of spectacles.
In an important sense, it doesn’t matter which industry the breakups begin in. Once they start, shareholders in every industry will start to eye their investments in monopolists skeptically. As trustbusters ride into town and start making lives miserable for monopolists, the debate around every corporate boardroom’s table will shift. People within corporations who’ve always felt uneasy about monopolism will gain a powerful new argument to fend off their evil rivals in the corporate hierarchy: “If we do it my way, we make less money; if we do it your way, a judge will fine us billions and expose us to ridicule and public disapprobation. So even though I get that it would be really cool to do that merger, lock out that competitor, or buy that little company and kill it before it can threaten it, we really shouldn’t — not if we don’t want to get tied to the DOJ’s bumper and get dragged up and down Trustbuster Road for the next 10 years.”
Image for post
20 GOTO 10
Fixing Big Tech will require a lot of iteration. As cyber lawyer Lawrence Lessig wrote in his 1999 book, Code and Other Laws of Cyberspace, our lives are regulated by four forces: law (what’s legal), code (what’s technologically possible), norms (what’s socially acceptable), and markets (what’s profitable).
If you could wave a wand and get Congress to pass a law that re-fanged the Sherman Act tomorrow, you could use the impending breakups to convince venture capitalists to fund competitors to Facebook, Google, Twitter, and Apple that would be waiting in the wings after they were cut down to size.
But getting Congress to act will require a massive normative shift, a mass movement of people who care about monopolies — and pulling them apart.
Getting people to care about monopolies will take technological interventions that help them to see what a world free from Big Tech might look like. Imagine if someone could make a beloved (but unauthorized) third-party Facebook or Twitter client that dampens the anxiety-producing algorithmic drumbeat and still lets you talk to your friends without being spied upon — something that made social media more sociable and less toxic. Now imagine that it gets shut down in a brutal legal battle. It’s always easier to convince people that something must be done to save a thing they love than it is to excite them about something that doesn’t even exist yet.
Neither tech nor law nor code nor markets are sufficient to reform Big Tech. But a profitable competitor to Big Tech could bankroll a legislative push; legal reform can embolden a toolsmith to make a better tool; the tool can create customers for a potential business who value the benefits of the internet but want them delivered without Big Tech; and that business can get funded and divert some of its profits to legal reform. 20 GOTO 10 (or lather, rinse, repeat). Do it again, but this time, get farther! After all, this time you’re starting with weaker Big Tech adversaries, a constituency that understands things can be better, Big Tech rivals who’ll help ensure their own future by bankrolling reform, and code that other programmers can build on to weaken Big Tech even further.
The surveillance capitalism hypothesis — that Big Tech’s products really work as well as they say they do and that’s why everything is so screwed up — is way too easy on surveillance and even easier on capitalism. Companies spy because they believe their own BS, and companies spy because governments let them, and companies spy because any advantage from spying is so short-lived and minor that they have to do more and more of it just to stay in place.
As to why things are so screwed up? Capitalism. Specifically, the monopolism that creates inequality and the inequality that creates monopolism. It’s a form of capitalism that rewards sociopaths who destroy the real economy to inflate the bottom line, and they get away with it for the same reason companies get away with spying: because our governments are in thrall to both the ideology that says monopolies are actually just fine and in thrall to the ideology that says that in a monopolistic world, you’d better not piss off the monopolists.
Surveillance doesn’t make capitalism rogue. Capitalism’s unchecked rule begets surveillance. Surveillance isn’t bad because it lets people manipulate us. It’s bad because it crushes our ability to be our authentic selves — and because it lets the rich and powerful figure out who might be thinking of building guillotines and what dirt they can use to discredit those embryonic guillotine-builders before they can even get to the lumberyard.
Up and through
With all the problems of Big Tech, it’s tempting to imagine solving the problem by returning to a world without tech at all. Resist that temptation.
The only way out of our Big Tech problem is up and through. If our future is not reliant upon high tech, it will be because civilization has fallen. Big Tech wired together a planetary, species-wide nervous system that, with the proper reforms and course corrections, is capable of seeing us through the existential challenge of our species and planet. Now it’s up to us to seize the means of computation, putting that electronic nervous system under democratic, accountable control.
I am, secretly, despite what I have said earlier, a tech exceptionalist. Not in the sense of thinking that tech should be given a free pass to monopolize because it has “economies of scale” or some other nebulous feature. I’m a tech exceptionalist because I believe that getting tech right matters and that getting it wrong will be an unmitigated catastrophe — and doing it right can give us the power to work together to save our civilization, our species, and our planet.''',


"13":'''Warren Buffett’s Recent Explanation of How Money Now Works Is the Most Important in History
The value of the money you have is changing. “Debt “and what it means is fundamentally changing.
Tim Denning
Tim Denning
Follow
Aug 24 · 6 min read



Image for post
Image Credit:MarketWatch/Getty Images
Watching Warren Buffett completely change what he believes about money in a matter of months has been fascinating.
He is considered the most successful investor in history, so he’s worth listening to when financial markets enter a strange period that nobody understands or can properly explain (even if, like me, you don’t love everything he says).
These two lines from Warren made me think:
“The [US
                ] debt isn’t going to be repaid; it’s going to be refunded.”
“You better own something other than debt.”
Buffett explains that when the government can just keep on printing money to pay their own debt it’s laughable to think they will ever default. He says, “The trick [for countries
                ] is to keep borrowing in your own currency.”
So if money will keep being printed out of thin air then what does that mean for your investments, assets and savings? Let’s explore the topic in simplistic terms and see what you can do about it.
The Most Important Lesson On How Money Works From Warren Buffett
This is what Warren said recently about how money works that will test everything you thought you knew about money:
If the world turns into a world where you [governments
                ] can issue more and more money and have negative interest rates over time — I’d have to see it to believe it, but I’ve seen a little bit of it. I’ve been surprised. I’ve been wrong so far.
If you can have negative interest rates and pour out money, and incur more and more debt relative to productive capacity, you’d think the world would have discovered it in the first couple of thousand years rather than just coming on it now. We will see.
It’s probably the most interesting question I’ve ever seen in economics.
Can you keep doing what we’re doing now? The world has been able to do it for now a dozen years or so [since 2008
                ]. We may be facing a period where we’re testing that hypothesis that you can continue it with a lot more force than we’ve tested it before.
This description from Warren about all the free money we’ve all been getting access to because of a health crisis may explain why Warren has sold a lot of his US bank stocks recently.
The influential finance blog Zero Hedge wrote recently that Warren “appears to now be quietly betting against the United States,” because “the famously anti-gold investor has abandoned banks — the backbone of America’s credit-driven economy — in favor of a gold miner.”
A friend said this to me the other day: “Watch what the billionaires do, not what they say.” If Warren’s actions are anything to go by then the record prices in the stock market are something to be very cautious of.
Inflation Is Taking Hold
Inflation is when prices go up and the value of your money decreases. Four dollars last year may have got you a small cup of coffee. That same cup of coffee might cost you $5 this year, as a simple example.
Inflation is a hidden tax on your money.
Warren says, “I’ve been wrong in thinking you could have the developments you’ve had without inflation taking hold.”
Warren has put his firm’s money in gold, and treasury bills which he describes as “a terrible investment over time.” (A treasury bill is an investment where you are essentially lending money to the government.)
So Warren is comfortable putting his money in terrible investments in the short-term because of what he can see in the world of finance. That decision is worth contemplating when thinking about your own money and investments.
Why All of This Matters to You?
We’ve talked a lot of finance shop in this article. Let’s break down why the change in how money now works matters to you.
Negative interest rates
Negative interest rates can be bad for you because it means you have to pay to store your money. It also means the bank you choose to bank with may face severe financial trouble that leads them to go out of business.
Yes, banks have insurance in case of such an event, but if the problem is too big then that deposit insurance is useless — many people do not understand this. They assume the government or a magic insurance policy will save them without any negative consequences.
We’re in uncharted territory and I would not be relying on anybody to come and save you and your money.
The poor are being robbed by the rich who have the data to predict their moves.
Many retail investors are buying stocks using apps like Robinhood — the data tells us this trend.
While billionaires like Warren are exiting stocks and running to safety, everyday people seem to believe they are smarter than the pros — or the high-frequency, non-human trading bots who predict the moves of the retail investor and bet against them.
Investments firms use high-frequency trading to automate their investment decisions and beat the average investor. These same firms are front-running retail Robinhood investors. What does this mean in simple terms?
Sophisticated investment firms, according to Bloomberg, are getting access to data that tells them what the retail investors (dumb money as it’s known in finance) are doing so they can take advantage of them.
This data allows investment firms to rob the poor and pay the rich — the name of the Robinhood app is kind of ironic, isn’t it?
The stock market bubble
Record unemployment. A global health crisis. Protests. Despite the world we live in stock markets are beating record highs. Crazy, or a disaster waiting to happen?
Another iconic billionaire investor, George Soros, called the stock market a bubble. “Investors are in a bubble fueled by Fed liquidity,” he says and that’s why he “no longer participates.”
Either everything is fine with markets and businesses haven’t been affected by the health crisis at all, or we’re watching a bubble that’s about to pop. I don’t have the answer so that’s why I’m sitting on the sidelines.
The change in the velocity of money
While free money is being given away through economic stimulus and large amounts of money are being printed out of thin air, the velocity of money is down. (The velocity of money just means how many times one dollar passes through multiple people’s hands.)
When large amounts of money are created out of thin air and that currency is not spent, when that money eventually is spent, it can lead to larger than normal amounts of inflation that devalue the money you’ve worked hard for.
Example of decrease in the velocity of money:
Image for post
The velocity of money is right down. Source: Federal Reserve Bank of St. Louis
Example of the extra money being printed out of thin air:
Image for post
The increase in money creation has exploded. Source: Board of Governors of the Federal Reserve System (US)
Takeaway
The way money works and functions in society has fundamentally changed. It has got some of the greatest investment minds like Warren Buffett and George Soros challenged, too. They have run to safety as a result.
What you can do about the change in how money works is this: be cautious in the short-term with your money and investing in assets.
The other critical learning you can take away from Warren is to spend some time understanding these financial concepts via a website like Investopedia:
Money Printing
M1 and M2 money supply
The Velocity of Money
Stock market bubbles (Tech Stocks Bubble in 2000)
Inflation vs. Deflation
Bailouts vs. Bail-ins — in the event of a financial crisis
If you understand these basics of how money works you can protect yourself and everything you’ve worked for. Now is not a time to panic. Now is a time to learn and prosper from what is transpiring in the global economy.
The value of the money you have is changing. The word debt and what it means is changing. Watch what the billionaire investors are doing because they tell you a lot of what you need to know.
You decide whether you donate your money to a trading app, watch it devalue because of inflation, or invest with a big safety net and act like a pro.
This article is for informational purposes only, it should not be considered Financial or Legal Advice. Consult a financial professional before making any major financial decisions.''',


"14":'''The Only Humans to Die in Space
The terrifying story of Soyuz 11 and its unfortunate fate
Calin Aneculaesei
Calin Aneculaesei
Follow
Aug 23 · 7 min read



Image for post
The original crew of Soyuz 11, Valeri Kubasov (left), Alexei Leonov(centre) and Pyotr Kolodin (right). Due to an x-ray that determined Kolodin might have tuberculosis, the crew had to be replaced.
TThe conquest of the final frontier is perhaps one of humanity’s greatest achievements. As I have written in previous articles about the history of space, I find the men and women who put their lives at risk in pursuit of human advancements to be some of the most respectable figures of human history. It takes a special kind of person to be selfless enough to put the progress of your species before the possible threat of death.
All astronauts and cosmonauts who volunteer for these space missions are at risk of death, even as technology advances, you can never be 100% sure that no device on your spacecraft will fail. Although only 19 people have died as a result of spaceflight, it is still a thought that all who go to space have at the back of their minds. Today we will explore the final voyage of the only people who had that thought in the back of their head manifest mid-flight, the Soyuz 11 crew.
Setting records
Initially, the Союз 11 (Anglicised: Soyuz 11) mission went exceptionally. Its crew, Commander Геoргий Тимофeевич Добровoльский (Anglicised: Georgy Timofeyevich Dobrovolsky), Flight Engineer Владислaв Николaевич Вoлков (Anglicised: Vladislav Nikolayevich Volkov) and Test Engineer Виктор Ивaнович Пацaев (Anglicised: Viktor Ivanovich Patsayev) docked into the first-ever space station to be put in orbit, Салют-1 (Anglicised: Salyut 1), without a hitch.
Image for post
Collage created by me using pictures courtesy of Wikicommons. Left and centre pictures were taken by the Soyuz 11 crew on departure from Salyut 1. Right picture was taken by a TsKBEM photographer satellite.
Image for post
Official emblem used in Soviet space missions: Voskhod-2, Soyuz-4, Soyuz-5, and Soyuz-11. Courtesy of Wikicommons
Soyuz 11 docked onto Salyut 1 on 7 June 1971. Its crew would remain on the station for 22 days. This, at the time, set an endurance record for the amount of time humans stayed in space. Their stay at the station was closely recorded by the Soviet newspaper Правда (Anglicised: Pravda) who reported on the cosmonauts’ every move. The crew also took part in news broadcasts beamed back home to be broadcast across the world.Due to the space station being a new concept, during their stay, the crew found many things wrong with their 22 day home. To name a few: the air filtration system broke and had to be fixed by the crew, a fire started but was quickly put out and, perhaps most comically, while using the treadmills as required by protocol to keep their muscles in shape, the entire space station started to shake.
Not something you want to feel while you hang in low earth orbit.
Overall during their stay at the station, no great mishaps happened and by the end of their 22 day stay all of the crew were healthy and eager to come home. On 29 June 1971, the spacecraft departed the station. The plan was to land the capsule in the desert of Kazakhstan where the Soviet authorities were eagerly awaiting their return. Unbeknownst to the crew, this would be their last flight.
Normal landing, abnormal crew
During the capsule’s rapid descent something went wrong. Due to an error in the decoupling from the station the landing capsule’s breathing ventilation valve was dislocated. As large forces acted on the capsule during its descent the valve was dislodged at the approximate altitude of 168 kilometres above sea level. The cabin began to quickly lose pressure, proving fatal for the crew on board. The capsule landed as planned in the Kazakhstani desert and to the surprise of the Soviet authorities, its crew was found to be dead on landing.
Post-mortem analysis of the crew found that it took around 40 seconds for the members of the mission to die as a result of the quick decompression of the crew module. One of the crew, Patsayev, was found reaching for the valve that controlled pressure within the cabin when the crew module was opened leading investigators to think that the crew was aware of their situation and Patsayev tried to save everyone by manually shutting the valve.
Image for post
Alexei Arkhipovich Leonov in 1974. Courtesy of Wikicommons.
This fault was known to the Soviet authorities as before the mission started, the man originally meant to be the commander of the mission, Алексей Архипович Леонов (Anglicised: Alexei Arkhipovich Leonov) warned the crew that the pressurisation valves were unreliable and that they should be manually adjusted after splitting off from the space station.
It is still not known why the crew chose not to listen to Leonov’s advice, what is known is that this piece of advice was ignored, something which proved fatal for the crew of Soyuz 11.
Aftermath and downplaying by the Soviets
Image for post
A Sokol-KV2 suit in the Speyer Museum in Germany. Courtesy of Wikicommons
Leonov went on to try to manually close the valve which Patsayev was attempting to close and, in perfect conditions, he could get the time down to around 1 minute to fully close the valve. This means that Patsayev’s efforts, although brave, were futile. The crew was doomed from the time they separated from the station.
Later versions of the Soyuz spacecraft were designed with only two crew spaces so the cosmonauts could wear the Cокол (Anglicised: Sokol) spacesuit. This was meant to protect crewmembers from sudden depressurisation during their travel in the capsule preventing such deaths from ever occurring.
The state media which so closely followed the crew before such as the newspaper Pravda stayed silent after their unfortunate fate was revealed. Most newspapers tried to omit the deaths of the crew from their daily reports. Even so, most of the people of the USSR learnt of the outcome of the mission quickly.
As expected the cosmonauts received a full honours funeral led by the Soviet government. They were posthumously awarded the Hero of the Soviet Union medal, one of the highest awards available in the Soviet Union, and were buried near the remains of Soviet cosmonaut Yuri Gagarin.
The US president at the time, Richard Nixon, released the following statement once he learnt of the deaths of the crew:
The American people join in expressing to you and the Soviet people our deepest sympathy on the tragic deaths of the three Soviet cosmonauts. The whole world followed the exploits of these courageous explorers of the unknown and shares the anguish of their tragedy. But the achievements of cosmonauts Dobrovolsky, Volkov and Patsayev remain. It will, I am sure, prove to have contributed greatly to the further achievements of the Soviet program for the exploration of space and thus to the widening of man’s horizons.
As Nixon mentioned, in my opinion, the death of the three brave cosmonauts was not in vain. They paved the way for the way we now conduct experiments in space through the use of orbital space stations. This experiment also allowed for future cooperation between the US and the USSR as it showed that docking in space was possible.
This cooperation came only 4 years later on in the form of the Apollo–Soyuz joint mission in July 1975. This was the first time in history the US and the USSR worked together in matters to do with space exploration. Although it was more of a gesture of goodwill this event stands in history as the start of US-Soviet cooperation, an event that couldn’t have happened without the Soyuz 11 mission.
Image for post
A USSR stamp released in 1971 commemorating the crew of the Soyuz 11 mission. Courtesy of Wikicommons.
Georgy Dobrovolsky, Vladislav Volkov and Viktor Patsayev will forever be remembered for the rest of time as some of the few that had to make the ultimate sacrifice in order for humanity to advance. Such a sacrifice should be remembered, commemorated and praised. Without such people, brave men and women willing to risk their lives in the name of progress, humanity wouldn’t be where it is now.
For any enquiries or comments make sure to contact me at aneculaeseicg@gmail.com. Note on this article: as mentioned on a previous article about space, I am not by any means an expert on the space industry and rocket science, it is inevitable that I made some mistakes with this article. If you can see any mistakes please let me know and I will amend it to the best of my abilities.''',


"15":'''Amazon Wants to Make You an ML Practitioner— For Free
The tech giant plans to speed up ML proficiency by publicizing its long-internal material
Anthony Agnone
Anthony Agnone
Follow
Aug 14 · 4 min read



Image for post
Some of the courses already available on ML University’s Youtube page
The What and Why
Amazon has long been striving to fix the issue of excess demand (vs supply) of individuals who have proficiency across the fields both Machine Learning and Software Engineering. To date, they have developed a slew of internal resources to get employees up to speed on the essentials. This is typically referred to as OJT, for “on the job training.”
OJT only goes so far — the size of your workforce. Aside from hired workers, companies depend on the education system to routinely supply capable talent to the workforce. This system has performed sufficiently for hundreds of years. However, the tide is turning. The speed of machine learning’s integration into industry workflows has largely outpaced the education system’s ability to provide fully-equipped talent. This is partially due to large systems necessarily moving slowly, but also due to a lack of convergence of dominant algorithms and tools in the field. Education systems are basically faced with a choice between overfitting on current trends versus sticking with classical techniques and allowing for OJT to solve the last-mile problem.
Amazon’s Take
Amazon has a great idea — meet halfway.
Academic institutions will largely lean towards proven classical techniques for education, and that is the correct move. To help the last-mile OJT problem even more than post-hire education, Amazon is now making available course materials from their internal “ML University”. By doing this, they will be able to educate many eventual employees even before it is interview time. This helps both sides of the table. Prospective employees can learn much more relevant material ahead of job applications and feel more equipped in job selection and commitment. On the flip side, Amazon and similar companies can then judge talent more directly in interviews than they have been able to. Since so much learning material is publicly available, there is less room for “the benefit of the doubt” when an applicant does not have experience in a certain sub-area.
Image for post
Just some of AWS’s numerous available services [source
                ]
Just three courses have been released for immediate use: natural language, computer vision, and tabular data. However, more will be rolling out through the end of 2020, with the start of 2021 having all the material public.
“By going public with the classes, we are contributing to the scientific community on the topic of machine learning, and making machine learning more democratic,” Werness adds. “This field isn’t limited to individuals with advanced science degrees, or technical backgrounds. This initiative to bring our courseware online represents a step toward lowering barriers for software developers, students and other builders who want to get started with practical machine learning.”
- Amazon Science
Check out the intro to the “Accelerated Computer Vision” course below. The entire course is available on similar Youtube pages.

Introduction for the Computer Vision course of Amazon’s ML University
Opinions and Cautions
This is great for the democratization of machine learning in the industry. Academic has long been very open and cooperative with ML research. The same can be said for the open-source software movement. Recently, in the past decade or so, we have seen these ideologies extend into the ML industry space. Its continuation will ensure that the economy’s aggregate output will rise, while still fostering healthy competition.
I’ll add a word of caution, however. The phenomenon referred to as “vendor lock-in” occurs when a service provider produces so much incentive to continue acquiring its own products across its ecosystem that the consumer effectively becomes stuck buying the provider’s goods and services, lest he/she suffer either lackluster integrations or the switching cost of starting over with a new provider. Look no further than a comparison of Apple vs Microsoft vs Google products for examples of vendor lock-in at work.
The courses at ML University indeed appear at the outset to provide a lot of general applicability across the ML and software space. It is likely that 80–90% of all of its material will do so, which is great!
However, as you go through the courses, remain keen on staying up-to-date on how other providers are accomplishing similar products and services. To be a truly marketable ML practitioner in this evolving workforce, one must stay flexible in showing ML proficiency independent of algorithm, language, framework, and platform provider.
Resources
Github pages for the NLP, Computer Vision, and Tabular Data ML courses
ML University Youtube page
ML University announcement article''',


"16":'''10 Bizarre Money Habits Making Millennials Richer
Refinery29 UK
Refinery29 UK
Follow
Aug 7 · 4 min read



By Anna Davies
Image for post
ILLUSTRATED BY JOSH MCKENNA.
Trying to save money can be hard right now — as the pandemic rolls on and we continue to feel the impact in our bank accounts, it’s hard to keep up the more high-tech ways to save money (though we absolutely advise you to try them out.) But there are some old-fashioned no-spend strategies that can make your money add up — sometimes pretty quickly. At first glance, they may sound weird, but they work. Ahead, try one (or a few) and tell us in the comments the strangest strategies you’ve used to successfully save some extra money.
Pick a denomination and save it. Always.
“I nanny, so I get paid in cash. Whenever I’d get £5 notes, I put them in a separate envelope. This money becomes my ‘fun’ money, so I know I can either take one out and buy a cappuccino, or keep adding to it and splurge for a fun dinner with friends.” — Courtney,
                32
Have a spending jar for fun stuff.
“Every week, I take out £100 for fun, which includes lunch and drinks. And I put the cash in a jar I decorated on my desk. Actually having to pull money out means I’m super conscious of how I’m spending it, and also keeps me honest. For example, I only use that money, not my debit card, for fun lunches out, so if I don’t have the money with me, then I’m going to eat the lunch I brought from home, and not go out with colleagues.” — Janie,
                27
Image for post
ILLUSTRATED BY JOSH MCKENNA.
Skip the coffee; save the cash.
“I am so bad about buying lattes ‘just because.’ And I know the £3 adds up. So whenever I feel the urge to buy a latte, I make the crappy office coffee, and make sure to move £3 from current to savings. It’s a neat trick that actually makes me ‘see’ how much I’m saving.”
— Jessica,
                23
Harness the power of recurring payments.
“I was paying £250 a month for my car payment. When I finally paid it off, I kept the ‘payments’ going into my savings account. Because I’d been paying it all along, I never missed the money, and it was so gratifying to see the money add up so fast in my savings account.” — Ramon,
                30
Do your saving in short sprints.
“I feel like I can get really into savings for only a month. So in that month, I see it as ‘training.’ I bring my breakfast and lunch to work, I only do social events that are free (one time, I had a party at my house where everyone had to bring one bottle of alcohol collecting dust in their homes), and I just really push myself. By the end of my ‘spending fast’ I have a lot more cash, and I am more conscious of how I’m spending it.” — Luke,
                27
Become your own bartender.
“When I worked at a summer camp, there was an honour system where you had to pay 50p for a drink from the fridge. I do the same thing at home to this day — £1 for a soft drink or £2 for a glass of wine. What’s funny is I made a list of my drink ‘prices’ on the fridge to remind my husband and I to be honest with it, and now, when our friends come over, they pay too…but they don’t have to!” — Rachel,
                30
Image for post
ILLUSTRATED BY JOSH MCKENNA.
Pay yourself for Instagram posts.
“This is so weird, but thinking about how much celebrities get paid for sponsored Instagrams made me decide to pay myself. For every photo I Insta, I (at least try!) to put £1 in a drawer!” — Cassie,
                22
Make it easy to visualise what you’re saving for.
“I know it sounds cheesy, but I like to see what I’m saving for, so I made a vision board of the holidays I want to take this year. ‘Seeing’ Greece every day makes it so much easier to not go out for a £10 lunch!” — Liz,
                29
Freeze your credit card. Yes, literally.
“Yes, literally, in a bag of water. I know it’s cliché, and it’s true that I could defrost it in seconds under warm water, but it did stop me from making impulse purchases.” — Marquita,
                25
Originally published at https: //www.refinery29.com.''', 


"17":'''The Third Crisis of 2020 Is Almost Here
A monstrous wave of evictions and slashed unemployment benefits threaten to put millions of Americans on the street — and Republicans don’t seem to care
Michael Arceneaux
Michael Arceneaux
Jul 15·6 min read

Image for post
Photo: Erik McGregor
Few things can terrify a person who’s struggling more than the first of the month. Some bills can be negotiated with, but when someone falls short on their rent or mortgage, the consequences are far more dire. How can they not be when what’s at risk isn’t cable TV, but having a place to lay your head?
No one deserves to worry about joining the already too high homeless population in America. But as exhausted as many of us might understandably be given the number of crises currently wreaking havoc nationwide, we’re currently on the verge of yet another. And it’s less than two weeks away.
When the coronavirus pandemic hit the U.S. in March and shutdowns began, the ensuing wave of economic woes brought record unemployment — but it didn’t bring an end to landlords demanding rent on April 1. In response, numerous states and cities across the country implemented temporary eviction moratoriums to prevent people from losing their rental homes or apartments.
It doesn’t take much to figure out what will happen to a nation when tens of millions of unemployed folks have their only source of aid stripped away.
Many of those moratoriums have since expired; only in select states, cities, and counties have they been extended by emergency order. That said, I fear even more will find themselves facing dire consequences without additional assistance. Since the attitude in the country has largely been “fuck the coronavirus, we’re capitalists,” one anticipates that lenders and landlords are waiting for their chance to oust those who can’t pay up. As housing advocates have warned, inaction could spur a “tsunami” of evictions that could lead to a spike in homelessness we haven’t seen in quite some time.
One of the few bright spots for people struggling to stave off eviction has been the extra $600 that tens of millions of unemployed Americans are presently receiving each week — and now that money is set to dry up by month’s end.
The additional payment is part of the CARES Act, a $1.8 trillion package Congress passed in March to help people weather the economic conditions brought by the then-new coronavirus pandemic. New legislation has yet to be passed, which means by the end of July, many Americans will find themselves reduced to base unemployment benefits, which, on average, amount to just over $19,
                000 a year — putting those with two children below the poverty line.
There are folks I know personally collecting unemployment benefits who didn’t know this was happening. I don’t fault them for not knowing; I fault our government for even placing them in such an avoidable predicament with little recourse. Some states are trying to extend that into the next week in light of that problem being brought to their attention, but the larger issue needs to be settled by Congress and the White House.
Much like the other messes presently consuming the nation, this is one that could be easily solved. If the U.S. government can inject more than a trillion dollars to prop up the stock market, surely it can throw some additional relief to the tens of millions of Americans who are jobless through no fault of their own? Unfortunately, between Donald Trump’s lack of leadership and the greed and callousness of the party still in control of the U.S. Senate, there is reason to doubt that a favorable result can happen in time.
When the question of extending unemployment benefits to more than 30 million Americans was raised by reporters earlier this month, many Republicans in the Senate hastily swatted the idea away. “I wasn’t supportive of the first round,” Senator Ron Johnson told NBC News at the beginning of July. “This is not a classic recession that requires financial stimulus.” I’ve always found Johnson to be both dumb and duplicitous, but you don’t have to be an economist — which he’s not — to understand that nothing about a once-in-a-century medical crisis is “classic.” Likewise, it doesn’t take much to figure out what will happen to a nation when tens of millions of unemployed folks have their only source of aid stripped away.
Politico reported that Senate Majority Leader Mitch McConnell conceded this point early on, but insisted that that the $600 weekly enhancement wouldn’t continue — and that any new legislation would need to include liability reform in order to minimize lawsuits. In other words, any money he’s willing to send to out-of-work Americans comes with the caveat that when many are forced back into the labor market, they can’t sue their employers for not providing proper safety conditions.
During an interview with the Fox Business Network this month, Donald Trump was asked if he favors another round of direct payments. “I do,” he said. “ I support it. But it has to be done properly.”
This is not the “proper” way to handle folks’ lives. (Fuck all of these people for thinking they did something sending a $1,
                200 check and an extra $600 in unemployment to begin with.)
The same can be said of Treasury Secretary Steven Mnuchin saying on CNBC last week that the administration’s priority was ensuring that future benefits amounted to “no more” than 100% of a worker’s prior wages. Yes, the Republicans are still mad that enhanced unemployment pays better than some jobs. (Specifically jobs in the accommodation and food services industry, which average a yearly salary of just $28,
                000.) The solution is to pay people more, not less, you insufferable pieces of shit.
I’m not sure what Trump is thinking here, but just to be clear: Creating a nationwide homeless crisis during the worst medical crisis in a century would not rev up the economy.
Senator Kamala Harris, who Joe Biden needs to admit he’s picking for VP and quit playing with us already, appears to understand this point as well, recently tweeting a reminder to her colleagues to focus. “Evictions may soon leave ~28M homeless in the United States,” she said. “We are on the verge of a wave of evictions if Congress doesn’t swiftly act to ban evictions and foreclosures during the pandemic — and pass my bill to provide $2,
                000 monthly payments. Time is of the essence.”
In fact, that 28 million estimate may not even cover it. In “The Government Is Walking Blind Into the Coronavirus Housing Crisis,” New Republic writer Alexis Goldstein explains, “There’s no government database to track evictions and foreclosures. That means, as it was in 2008, we’ll never truly know how many people are displaced.”
In May, House Democrats passed the HEROES Act, a $3 trillion bill that includes another round of direct deposits and checks. That was two months ago today, yet the Republicans haven’t even bothered to entertain the bill. Instead, McConnell will present a Republican plan on Monday — five days before UI benefits are set to expire.
In other words, they can’t be bothered to care. According to an analysis provided by the Covid-19 Eviction Defense Project, a Colorado-based community group, of the 110 million Americans living in rental households, as much as 20% are at risk of eviction by Sept. 30.
I don’t have the means or power to provide meaningful assistance, but I do support those taking matters into their own hands — and people are. Rent relief efforts have launched in cities like Los Angeles, but some renters in parts of Brooklyn are forging eviction blockades. I like the idea of neighbors banding together, and agree that in the interim, it might be the tenants’ best defense against landlords.
But again, this is all avoidable. When the coronavirus first started, I recall it being initially christened a “rich man’s disease” globally, but as we’ve seen, the poor have borne the greatest brunt — even in the richest country in the world. Why does this country insist on making this all so much harder than it needs to be?
I doubt Congress provides an answer, but I sure hope they provide folks with the cash they need, or else too many people will be asking themselves that question on the street.''',


"18":'''The Future Alexander Hamilton Warned About Has Arrived
Our Founding Father envisioned a Senate that was representative of the people. What we got was something else entirely.
David Litt
David Litt
Jul 3·6 min read

Image for post
The U.S. Capitol Rotunda on March 24, 2020. Photo: Chip Somodevilla/Getty Images
This weekend, Americans will gather for a Fourth of July display as highly anticipated as any fireworks show, but far more fitting for the social distancing era: Hamilton will be streaming on Disney+. My fellow Democrats, for whom Lin-Manuel Miranda’s soundtrack has become a kind of hymnal, will eagerly (and in my case tunelessly) sing their way through a founder’s revolutionary rise, political struggles, and untimely demise.
But as we celebrate America’s 244th birthday, it’s worth looking at a bit of the Founding Father’s biography that doesn’t get a musical mention. One of Alexander Hamilton’s guiding beliefs was that our republic should reflect the will of the people, not the will of the states. Today, Hamilton is more popular and respected than ever (even if his extramarital affairs are also more well known, thanks to the musical). But the kind of democracy Hamilton envisioned is increasingly under threat: More and more, America is becoming a country where states have power and people do not.
On issue after issue — gun violence prevention; climate change; taxes; responding to Covid-19; or police brutality — the states, as represented in the Senate, are standing between the will of the people and the actions of their government. This was not the future Hamilton envisioned. As fans of the musical know, he was nominated to the Constitutional Convention. There, the single most contentious issue was how to allocate lawmakers among the states in the House and Senate. High-population states, led by James Madison’s Virginia, argued that representatives in both chambers should be handed out according to population; the more people your state has, the more legislators it gets. But small states such as Delaware disagreed. They demanded equal representation, regardless of population size.
It will come as a surprise to no one that Alexander Hamilton had a strong, and quite articulate, opinion on the subject. “As states are a collection of individual men, which ought we to respect most, the rights of the people composing them, or the artificial beings resulting from the composition?” He asked his fellow delegates. Then, rather witheringly, he answered his own question. “Nothing could be more preposterous or absurd than to sacrifice the former to the latter.” Hamilton, in other words, was arguing that if the majority of people wanted to do one thing, and the majority of states wanted something else, the people’s choice should win.
Hamilton’s view went to the heart of America itself. Our republic was ultimately not a collection of places, but a collection of people. The “consent of the governed” refers not to the preferences of the states, but of the individuals who comprise them. Our most well-regarded Founders agreed with Hamilton on this point. Yet in the end, they were forced to compromise: The House was apportioned based on population, but the Senate gave each state an equal number of votes, no matter how large or small their populations grew. As a result, the sacrifice Hamilton decried as “preposterous” today increasingly defines the country. We respect the rights of the states more than we respect the rights of the people who compose them. And our democracy is just as imperiled as Hamilton thought it would be.
It’s true that the Senate’s two-votes-per-state composition, the kind of arrangement that so infuriated Alexander, has existed since the Constitution was ratified. But the consequences of that arrangement are very different than they were just 40 years ago. Partly, this is because of the manner in which America’s population has expanded: Like a gangly teenager, we’ve grown in profoundly asymmetrical ways. When the Constitution was first ratified, the smallest population state, Delaware, was about one-thirteenth the size of the largest population state, Virginia. Today, Wyoming is one sixty-eighth the size of California. The Senate has always been unfair, but it’s more unfair than it used to be.
No less important, that unfairness now clearly benefits one political party over the other. One reason Hamilton and Madison ultimately accepted a Senate that benefited small states was that when the Constitution was ratified, those states were fairly evenly distributed between North and South. Today, the most crucial fault line in American politics is no longer regional, but partisan. Because rural states tend to have smaller populations, and because Democrats are increasingly the party of cities, the basic inequality of the Senate now strongly benefits Republicans.
To understand just how much a government of the states rather than the people helps the GOP, one must look no further than the 2016 election. In that race, Donald Trump won 30 states, or 60% of the total, while losing the popular vote by approximately 2%. For Democrats to win a majority in the Senate, they need to win at least 10 seats from red states. Republicans, meanwhile, can get to 60 Senate votes without winning a single blue-state seat.
Once you know this basic fact — that the average state, and therefore the average senator — is more conservative than the average American, many political mysteries suddenly become clear. Why don’t we have universal background checks for firearms purchases? Why is beer enthusiast Brett Kavanaugh a Supreme Court justice? Why is it so hard to fight climate change, even during the brief periods when Democrats have full control of the federal government? When Americans want one thing and Washington does another, we tend to blame individual senators. But as Hamilton would surely remind us, we’d be better off blaming the structure of the Senate itself.
Fortunately, it’s not too late to restore the kind of democracy that Hamilton and his fellow founders (even the ones he rap battled in Washington’s cabinet) envisioned. The logical place to start is by granting statehood to D.C. and Puerto Rico, which would add two likely blue states into the union while enfranchising millions of Americans who currently lack representation in Congress. This wouldn’t be nearly enough to undo the Republican advantage in the Senate, but it would ameliorate it, and bring the views of the average senator closer to the views of the average American. The House of Representatives passed a D.C. Statehood bill at the end of June. If the Senate changes hands in January, there should be no higher priority than getting such a bill to a new president’s desk.
But ultimately, structural reforms are only part of the solution. As Lin-Manuel Miranda reminds us, who tells the story matters, too. For decades, Americans who care about protecting our democracy have allowed a new collection of would-be oligarchs to hijack our shared memory of our nation’s founding. We’ve stood by as terms like “tyranny of the majority” or “federalism” were redefined to provide excuses for power grab after power grab. We didn’t merely lose the debate; we didn’t even bother showing up.
That needs to change. Just as Hamilton itself reclaims a bit of American history, casting it in a new and powerful light, it’s time to tell the true, full story of how our democracy came to be, and who it’s meant to serve. Authoritarianism looms, but we are far from helpless in the face of this threat. At this moment, when history has its eyes on us, we can never be satisfied with a country that puts its artificially constructed states above flesh-and-blood people.
Like Hamilton himself, we have a chance to fight for, and to define, our democracy. Let’s not throw away that opportunity.''',


"19":'''When the U.S Dollar Collapses, the Elites Will Try to Steal Your Money
This is how you could prepare for a monetary disaster
Concoda
Concoda
Jun 28·6 min read

Image for post
Photo by James Pond on Unsplash
Throughout the ages in times of crisis, out-of-control governments, states, and empires have seized from their citizens what they perceived to be real money.
In recent history, gold has allowed citizens to protect their purchasing power from fiat currency depreciation and escape state-imposed financial repression. Though, it has been the prime asset that authorities confiscate when monetary systems fail.
In 1933, former U.S President, Franklin D. Roosevelt, enacted Executive Order 6102 banning American citizens from hoarding large amounts of gold. In 1959, the Australian Government signed the Banking Act into law allowing Aussie authorities to seize citizen’s precious metals. And in 1966, the British government blocked gold imports and banned Brits from owning more than four precious metal coins. These are just a few of the many wealth confiscation episodes over the past century.
Past governments approved these actions without their citizen’s consent to achieve “order” and remove “chaos”, but this is code-speak for theft via temporary authoritarianism. So when the U.S dollar inevitably collapses, if you think this 21st-century U.S administration won’t pursue your precious metals stash, you’ll be in for a surprise when the debtor-in-chief’s “sound-money hit squad” knocks down your door, empties your safe, and gives you nothing in return.
Unfortunately, protecting your purchasing power from a fiat currency system isn’t as straightforward as buying gold, silver, and Bitcoin, and storing it down at your local JPMorgan branch. When it matters, the state will seize your property and will remove your rights to restore — what they believe to be — monetary order, whether that’s via a government-created cryptocurrency backed by gold or a new fiat currency backed by IMF (International Monetary Fund) SDRs (Special Drawing Rights): “the international reserve currency”.
“You’ll be in for a surprise when the debtor-in-chief’s “sound money hit squad” knocks down your door, empties your safe, and gives you nothing in return.”
For the elites to create a new monetary paradigm, they will use any excuse to try to steal your hard-earned wealth when things go wrong. Italian dictator, Benito Mussolini, encouraged citizens to hand over their gold in exchange for steel wristbands bearing the inscription “Gold for the Fatherland”, the Soviet Union banned large private ownership of gold altogether, and Saddam Hussein, the deceased Iraqi dictator, cleaned out citizen’s gold, jewelry, and other valuables while holding them at gunpoint — they traded their assets for their lives.
Despite past events, elites will tell you gold is nothing more than a barbarous relic, a useless lump of shiny rock with no purpose in modern-day society while continuing to amass vast quantities of gold bullion. Since 2000, Russia has increased its reserves by 680%, China has increased its reserves by 393%, and U.S reserves remain equal despite a 100% debt-backed currency. When the time comes they will show their true feelings towards gold and will come for yours — if required.
Though, there are ways to get around a government that imposes tyrannical policies in desperate times. But you’ll have to game the system, discard patriotism, and think outside the box.
Removing all your assets from entities connected to the banking system is the first step. With “bail-in” legislation passed and enacted in several countries — the G20 bank bail-in solution was signed into supranational law in late 2014 — if you store your gold within your bank and your bank goes bust, they have the power to use your gold — and even your savings — to bail out their mistakes.
You might think to store gold in your home safe, but like anything in investing, diversification is key. Storing gold in a private vault is important, but so is the location: You must store it offshore, outside your government’s jurisdiction, otherwise they will hunt down your stash, like in 1907,
                1959, and 1966. Though you don’t need a high net worth to store your assets in other countries. Companies like Goldmoney allow their clients with small account balances to buy and store gold in various countries from Singapore to Switzerland — countries with governments that have never seized precious metals.
Though, if you’re desperate to keep some gold at home, stick to jewelry. You don’t need to hide your gold bracelets, earrings, and other wearables because the U.S government doesn’t recognize them as financial assets. As precious metals analyst, Jeff Clark, says, “History has shown, in the developed world, gold confiscations have targeted monetary metals, like coins and bars. Jewelry was spared. Only in oppressive nations, ruled by dictators, was it a target. In other words, residents of developed nations that own gold jewelry have an asset that remains [less
                ] appealing … to grab.”
“Your primary aim is to preserve your capital avoiding wealth destruction and confiscation.”
Another way to preserve your purchasing power is to use asset classes that most people shun as investments, ones you can touch, feel, and treasure, but also profit from over your lifetime. They have real uses, they tend to hold their value, and, most importantly, governments don’t need them to restore order during monetary Armageddon. “To bail out our beloved country, we’re seizing all vintage guitars, fine wine, and luxury watches,” is something you’ll never hear on the six o'clock news — hopefully.
In 1957, you could have bought a Rolex submariner watch for $1,
                265 — adjusted for inflation — compared to today’s price of $7,
                250, not only preserving both your wealth and purchasing power but netting yourself a tidy profit. Today, with that money, you could walk into any watch shop and purchase 11 of them without breaking a sweat.
Vintage guitars sell for 1000% more than their 1960s price. If you choose the right guitar, it could become part of your retirement fund. When the world goes into a prolonged recession or depression, people lose confidence in their paper wealth and shift into tangible assets, hence, guitar prices appreciate significantly. The VGP50 price index shows above-average price rises during the 2008 financial crisis.
But the most underrated and most overlooked asset of all time is fine wine. Over the past decade, the Burgundy 150 index, the broadest price measure of fine wine, has outperformed the S&P500 index by roughly 300% with an annual 12.7% growth rate. Prices vary based on rarity, exclusivity, and desirability. A bottle of Domaine Romanée Conti will set you back roughly $50,
                000 while a bottle of Fontaine Gagnard will cost you around $1,
                000. Though the fine wine market is difficult to enter with limited learning resources online — and a degree of pretentiousness — going down this rabbit hole has reaped big rewards so far.
Then, there are the “protected” asset classes: stocks, bonds, and real estate. As we have a financialized economy, not a real economy, higher prices in speculative assets maintain the stability of a broken system, so the last step the government will take is to confiscate assets that paint over American’s fake economy. They want you to keep buying these — and in bulk!
But creating a diversified portfolio of physical assets, which remain outside the protected class and have proven the test of time, will help you financially and will give you future peace of mind. You’re spoilt for choice with old-timers like precious metals, and new kids on the block like Bitcoin.
The hard part, of course, is trying to predict which assets will not only hold their value but appreciate over time, though with a few hours of research, your chances will rise dramatically. Again, it’s a bonus if an asset yields a profit. Your primary aim is to preserve your capital, avoiding wealth destruction and confiscation.
The rise of anti-fiat sentiment worldwide has caused a surge in alternate versions of wealth preservation, and with central banks and governments continuing their money printing onslaught, protecting your purchasing power through “radical” means will likely gain popularity in the next decade.
The mighty U.S dollar could survive for many years to come, and by then, the world will be a very different place: a new government, a new culture, a new society, a new way of life. But whatever the future holds, the elite’s monetary agenda remains the same. Though in the next economic collapse, if you have gone the extra mile to safeguard your real wealth, you won’t care whether the state starts seizing assets by any means necessary.
Your real wealth will be undetectable in plain sight.''',


"20":'''Why 2020 to 2050 Will Be ‘the Most Transformative Decades in Human History’
Climate change will force more people to leave their homes than at any other point in human history. Conflict is inevitable.
Eric Holthaus
Eric Holthaus
Jun 25·7 min read

Image for post
Photo: Aliraza Khatri’s Photography/Moment/Getty Images
The 30 years from 2020 to 2050 will be among the most transformative decades in all of human history. Collapsing ice sheets, the aerosol crisis, and rising sea levels will force more people to leave their homes than at any other point in human history. In some places, that means conflict is inevitable.
A study from researchers at the University of California at Berkeley found that higher temperatures and shifting patterns of extreme weather can cause a rise in all types of violence, from domestic abuse to civil wars. In extreme cases, it could cause countries to cease functioning and collapse altogether.
This ominous reality of climate change is far from fated, however. A rapidly changing environment just makes conflict more likely, not inevitable. People, ultimately, are still in control. Our choices determine whether or not these conflicts will happen. In a world where we’ve rapidly decided to embark on constructing an ecological society, we’ll have developed countless tools of conflict avoidance as part of our climate change adaptation strategies.
Still, there will be those who choose to live outside the mainstream society who may pose an existential threat to the rest of us. Some groups and a few rogue countries will try to prevent the rest of the world’s transition toward ecological and social justice. They will do this either because of the lingering influence from the dwindling fossil fuel industry, or because of a fascist ideological response to climate change that puts human rights at risk, or out of desperation.
Mary Annaïse Heglar, a climate essayist and advocate for intersectional approaches to racial and environmental justice, is inspired particularly by Octavia Butler’s Parable of the Sower for an example of how things could go very badly. In the book, Butler describes fire-obsessed cults that spring up in a post–rapid climate change world, craving some sense amid the destruction and chaos they see all around them. Heglar thinks that could be just the beginning. “The future I see is really ugly unless something very, very drastic changes,” Heglar told me. “It’s a world where people find many, many different ways, very creative ways, to be cruel to one another. Unpredictability brings out people’s cruelty if you’re not careful. And most people are not careful.”
Heglar specifically thinks of the racial massacre in East Saint Louis, Illinois, in 1917 as an example of the kind of violence that might emerge if the world is not careful. Angry white mobs murdered dozens of Black people after they were hired in place of striking workers at factories during World War I. If lifesaving technology is not distributed fairly, or if governments lean too heavily on austerity along racial lines, or if climate disasters fragment already vulnerable populations, the result could be truly ugly.
“So many things that we think are impossible today could be completely normal in 20 years,” Heglar told me. “I hear people saying now that ‘when it gets really bad, I’ll just move to New Zealand or I’ll move to Sweden, where climate change impact is not going to be that drastic.’ But it’s not going to be cute there. First of all, it’s going to be mostly the 1% living there. So if you think your regular ass is gonna be able to buy land in New Zealand, good luck.”
An escapist attitude is probably the most dangerous reaction to climate change today. It drives to the heart of how the problem of climate change came into being in the first place: By imagining ourselves as individuals who somehow exist outside the context of an interconnected, living ecosystem on a planet where all of our actions deeply affect one another, we fail to see each other’s humanity and right to simply exist. It’s the same attitude that drives the richest men in the world today to create their own private space agencies. Those who are already being affected by the climate emergency can’t and won’t simply be left to fend for themselves while the privileged few plot their escape plans — to higher ground in their neighborhood, to inland mountain refuges, to Mars.
Until we build a world that works for everyone, we’ll continue to have people whose survival is systematically erased by those in power. That’s the dystopia for the rich and powerful: a world where the rest of us finally realize the power we had all along to fight for a justice-focused society.
It will take active, conscious effort to defuse the tensions sure to arise in a warming world. Overcoming a coordinated effort by the fossil fuel industry to save itself is not going to be easy, but we know it’s coming. That effort has been going on since the fossil fuel industry began, and it won’t just go away in the 2040s, even amid two decades of radical and hopeful changes. As always, our best hope will remain that we can prepare along the way to increase the chances of a peaceful transition to a fossil-free world.
We know that the weather in the 2040s will be worse than it is today. A major, sudden change, like a collapsing ice sheet or a quick rise in global temperatures after eliminating aerosols, would make the weather even more destructive than current predictions, even if we are able to radically reduce greenhouse gas emissions. What we can control, of course, is how we decide to respond to the worsening weather.
Since my conversation years ago with Rear Admiral David Titley, I’ve repeated his idea of “catastrophic success” over and over to myself when I think things can’t get any worse, and I’ve let it shape my view of how the world could quickly change beyond our wildest imaginations — for the better. Titley sees the warming world both as a scientist (he’s a meteorologist by training) and as a former military officer. He understands that the potential for a massive increase in refugees is a heartbreaking and almost inevitable looming humanitarian crisis due to the science of the escalating severity of droughts, floods, and severe weather we’ve already seen in recent decades and the historical tendency for leaders to close borders during times of crisis. A worsening of this trend could make the world practically ungovernable in our lifetimes.
The U.S. military has been among the first large-scale entities to recognize this. That kind of makes sense if you consider its mission of ensuring U.S. safety and prosperity continues for as long as possible: Without planetary stability, there is no U.S. stability. That’s part of why U.S. military strategists at the Pentagon have begun calling climate change a “threat multiplier.”
When Titley talks about migration, though, even he struggles to put the stakes in context. In the 2040s, if global sea levels rise by three feet and droughts, fires, heat waves, and floods continue to worsen, we could see around 250 million people forced from their homes. That’s about four times as many people as are currently displaced and about 50 times as many as were displaced during the Syrian civil war. In short, it would challenge our understanding of nationality, borders, and politics as usual.
“Post–World War II,” Titley told me, “tens of millions of people within Europe were on forced migration in the 1940s. We kind of gloss over that part of history. I mean, Europe was really bad after World War II. It’s part of what got the Marshall Plan. I think it really kind of scared us that, hey, this whole place is just collapsing, basically, and something had to be done.”
An uncontrolled, unanticipated climate-related migration crisis could be even worse than the refugee crisis after World War II, which, despite its horrors, displaced less than 1% of the world’s population. Climate change could displace three times that amount just in the next two or three decades. Although displacement due to extreme weather is already becoming increasingly common, the proximate cause of displacement and migration is usually fleeing violent conflict. How do we anticipate a world that could quickly fracture and urgently work to reduce the risk of violent conflict before it occurs?
A crisis like this will require proactive harm reduction on a civilizational scale. We will need to establish policies that encourage, rather than restrict, freedom of movement. And we must establish robust social safety nets so that families are less likely to abandon their homes in search of a place where they can simply live. Also, even before we reach zero emissions globally, we will have to recognize the need to take aggressive actions to reduce the level of carbon dioxide in the atmosphere. All of this will remain just as urgent in the 2040s as in 2020.
“I’m probably wrong,” Titley said, “but I’m actually more optimistic that we are going to do real things now than I have been for a long, long time. I think there’s actual legitimate cause for optimism.”
Specifically, Titley pointed to the steady shift away from outright denial among rank-and-file members of the Republican Party as evidence that attitudes can shift toward action, no matter how meager. And once that facade of climate denial breaks, an avalanche of action could soon follow. “We may be much closer to catastrophic success right now. Things can change, and not always for the worse. They can change for the better. It can happen very, very quickly.”''',


"21": '''The Four D's That Define the Future
September 14,
                2020

When the money runs out or loses its purchasing power, all sorts of complexity that were previously viewed as essential crumble to dust.

Four D's will define 2020-2025: derealization, denormalization, decomplexification and decoherence. That's a lot of D's. Let's take them one at a time.

I use the word derealization to describe the inner disconnect between what we experience and what the propaganda / marketing complex we live in tells us we should be experiencing.

Put another way: our lived experience is derealized (dismissed as not real) by official spin and propaganda.

The current state of the economy is a good example. We see the real-world economy declining yet the officially approved narrative is that there's a V-shaped recovery underway because Big Tech stocks are hitting new highs. In other words, we don't need a real-world economy, all we need is a digital economy provided by Big Tech platforms.

This is derealization at its finest: the everyday world you experience directly no longer matters; what matters is stock prices and various statistics that all paint a rosy picture.

Meanwhile, the wealthiest class is fleeing soon-to-be-bankrupt cities. The wealthiest class has the means to buy the best advice and also has the most to lose, so I give their actions far more credence than official propaganda.

I've sketched out my thesis on denormalization in The 'New Normal' Is De-Normalization and Here's Why the 'Impossible' Economic Collapse Is Unavoidable:

This is why denormalization is an extinction event for much of our high-cost, high-complexity, heavily regulated economy. Subsidizing high costs doesn't stop the dominoes from falling, as subsidies are not a substitute for the virtuous cycle of re-investment.

The Fed's project of lowering the cost of capital to zero doesn't generate this virtuous cycle; all it does is encourage socially useless speculative predation. Collapse isn't 'impossible,' it's unavoidable.

The basic idea is that all the structures of the 'normal' economy only function at full capacity, as costs have moved higher, unproductive complexity has increased and our ability to pay these higher costs is based on ever-expanding debt.

As a result, 'normal' became extremely fragile and binary: it's either fully funded at full capacity or it collapses. The structures of everyday life (to use Braudel's apt phrase) are incapable of downsizing to 70% of their previous complexity and cost, much less 50%.

There won't be any 'new normal' because the system has become too rigid, ossified, over-regulated and controlled by entrenched interests and elites. It is incapable of reducing complexity and cost, and bailouts via borrowed money are stopgaps, not actual solutions.

Decomplexification is a mouthful, and everyone inside the machine knows the impossibility of paring organizational complexity. Everyone who is a stakeholder in the status quo (which is virtually every employee, manager, etc.) will fight to keep the status quo intact as is, for fear that any re-organization might imperil their livelihood or security. This is entirely understandable, of course.

Modern life is inherently complex. Democracy is complex and cumbersome because having a bunch of stakeholders all competing for public resources and advocating for a bigger slice of the pie is inherently messy. There must be oversight and feedback to minimize the possibility of one clique gaining complete power.

Long global supply chains are inherently complex. Managing ever-increasing regulations is inherently complex. And so on.

When the money runs out or loses its purchasing power, all sorts of complexity that were previously viewed as essential crumble to dust. We're witnessing the early stages of this in real time in healthcare and education: overly complex and costly systems are breaking down not just from the challenges of the pandemic but because they're structurally incapable of adapting or evolving beyond pseudo-reforms and policy tweaks.

As an illustration, consider the current overly complex way our healthcare system funds itself and a system in which customers pay cash for medical care: no insurance, minimal oversight auditing, etc. Regulations boil down to a requirement to publicly post prices for services and actually charge only the posted prices.

In higher education, as per the model I outline in my book The Nearly Free University, the campus and its entire bureaucracy becomes superfluous. Classes, embedded apprenticeships and in-person workshops are organized online. The entire scheme of accrediting colleges is jettisoned in favor of accrediting each student.

And so on. You can see the problem: eliminating unproductive, obsolete layers of costly complexity will eliminate millions of middle-class jobs that can't be replaced with new expansive bureaucracies.

Yes, paying cash for healthcare and campus-less, mostly automated universities are oversimplifications. So where is the middle ground between current costly complexity and some 'new normal' with half the costs and complexity? There's no way to accomplish this while retaining the payrolls, priorities, processes and structures of the existing systems.

The point here is that when the money runs out or loses much of its purchasing power, overly costly complexity collapses whether we like it or not.

Decoherence is an interesting word. In science, 'Decoherence can be viewed as the loss of information from a system into the environment, since every system is loosely coupled with the energetic state of its surroundings.'

Decoherence refers to the loss of systemic coherence between narratives, values, processes and systems. Simply put, stuff no longer works right and it no longer makes sense.

What worked in the past has been transformed by two systemic drifts:

1. Systems that evolved to function in a specific socio-political-economic context continued adding complexity and cost because debt-based funding was available, not because they were becoming more efficient or effective.

2. The socio-political-economic context has changed and so the status quo systems are mal-adapted, i.e. obsolete.

These two systemic drifts occur so slowly that we aren't even aware of the loss of coherence unless we compare the current system to a previous set point or look at it from the perspective of starting from scratch: what would the most sustainable, lowest-energy consumption, most efficient and productive system look like if we designed it from scratch? It certainly wouldn't be the system we have now,

The four Ds help us understand why the status quo is incapable of adapting / evolving fast enough and effectively enough to manage a controlled collapse to a much lower level of cost and complexity.

The status quo can't even admit the need for a controlled collapse, much less manage it.

We can add a fifth D: denial. The four Ds are already in motion and denial is only accelerating systemic decoherence.''',


"22":'''Inflation Is Stealth Austerity
September 9,
                2020

Rather than decry austerity, which demands an open political discussion of trade-offs, we should decry inflation's stealthy reduction of purchasing power.

Austerity--bad. Inflation--good. Oh wait--they're the same thing: both are a reduction in purchasing power. The only difference is a reduction via austerity is upfront while inflation is a stealth reduction, obfuscated by official distortions and Federal Reserve mumbo-jumbo.

Consider $1,
                200 in wages, unemployment, stimulus, Social Security payment, etc. If this payment gets cut by 10%--$120--as a result of austerity, pay cut, reduction in hours worked, etc., recipients scream bloody murder.

But if inflation reduces the purchasing power of the $1,
                200 by 10%, nobody does anything but grumble that 'prices keep rising while my income stays the same.' This is the classic boiled frog syndrome: inflation is like the heat being turned up so gradually that the poor frog doesn't realize he's about to expire.

Inflation is stealthy because the loss of purchasing power is difficult to monitor. Your $1,
                200 only buys what $1,
                080 bought in the recent past; 10% inflation reduced your income exactly the same as if austerity had subtracted the $120 upfront.

Governments and central banks love inflation because the theft goes unnoticed. The public tolerates inflation because it's easy to passively accept this erosion in their standard of living and difficult to generate the political heat that an outright cut would spark.

Though it's being openly engineered by the Federal Reserve, inflation appears to be a force nobody controls--unlike austerity which is so clearly a political decision. If Inflation robbed 10% of everyone's income overnight, people might be roused from their passivity to protest.

But since the theft occurs slowly--what's 1% a month?--and unevenly across a spectrum of goods and services, this theft doesn't rouse the same political storm as upfront austerity.

Inflation is a form of sacrifice that few recognize as sacrifice. It seems like everyone's income is eroded equally, but this isn't true: the wealthy closest to the Fed's money spigots are earning multiples of inflation from asset inflation, stock buybacks, etc. Inflation is a pinprick to the wealthy and a stilletto in the kidneys of the bottom 95%.

To the political Aristocracy, inflation is wonderful because they don't need to ask anyone to sacrifice 10% of their income as they do with austerity; they just steal the 10% a dribble at a time and throw up their hands as if inflation is some mystery force completely beyond their control.

Ironically, austerity--an honest, upfront political decision and sacrifice--is decried, while the dishonest, stealth cut of inflation is passively accepted, even as the Federal Reserve has made a cloaked political decision to reduce the purchasing power of everyone's income except for the New Nobility (the top 0.1%) that the Fed slavishly serves.

Rather than decry austerity, which demands an open political discussion of trade-offs, we should decry inflation's stealthy reduction of purchasing power, a Fed policy that benefits the few at the expense of the many.

Here is the Chapwood Index of inflation, which carefully measures apples to apples costs of essential goods and services in each city:



As inflation erodes purchasing power, workers' share of the economy has declined dramatically-- a double-whammy of declining purchasing power and standard of living.''',


"23":'''The Pandemic Is Accelerating Trends That Are Disrupting the Foundations of the Economy
August 25,
                2020

The problem is the economy that's left has no means of creating tens of millions of jobs to replace those lost as the 1959 economic model collapses.

Fundamentally, the economy of 2019 was not very different from the economy of 1959: people went shopping at retail stores, were educated at sprawling college campuses, went to work downtown, drove to the doctor's office or hospital, caught a flight at the airport, and so on.

The daily routine of the vast majority of the workforce was no different from 1959. In 2019, the commutes were longer, white-collar workers stared at screens rather than typewriters, factory workers tended robots and so on, but the fundamentals of everyday life and the nature of work were pretty much the same.

Beneath the surface, the fundamental change in the economy was financialization, the commodification of everything into a financial asset or income stream that could then be leveraged, bundled and sold globally at an immense profit by Wall Street financiers.

This layer of speculative asset-income mining had no relation to the actual work being done; it existed in its own derealized realm.

For decades, these two realms--the structure of everyday life (to borrow Braudel's apt term) and the abstract, derealized but oh so profitable realm of financialization--co-existed in an uneasy state of loosely bound systems.

If you squinted hard enough and repeated the mantras often enough, you could persuade yourself there was still some connection between the everyday-life economy and the realm of financialization.

The two realms have now disconnected, and the real-world economy has been ripped from its moorings, as patterns of work and every-day life that stretch back 70 years to the emergence of the postwar era unravel and dissolve.

The trends that are currently fatally disrupting retail, education, office work and healthcare have been in place for years. When I wrote my 2013 book about the digitized future of higher education in a low-cost union of high-touch and low-touch learning, The Nearly Free University, all these trends were already clearly visible to those willing to look beyond the models embedded in the economy for decades or even centuries.

Visionaries like Peter Drucker foresaw the complete disruption of the education and healthcare sectors as far back as 1994. Post-Capitalist Society.

The problem with this disruption is it eliminates tens of millions of jobs--not just the low-paying jobs in retail and dining-out, but high-paying jobs in university administration, healthcare, and other core service sectors.

The last real-world connection between everyday life and financialization was the over-supply of everything that could be financialized: the way to reap the big profits was expand whatever could be leveraged and sold. So retail and commercial space ballooned, colleges proliferated, cafes sprang up on every corner, etc.

Meanwhile, financialization's unquenchable thirst for higher profits stripped everything of the redundancy and buffers required to stabilize the system in times of crisis. So hospitals no longer kept inventory because by the logic of financialization, all that mattered was maximizing the return on capital--nothing else could possibly matter in the derealized realm of speculative profiteering.

Now healthcare finds itself trapped between the pincers of financialization's stripmining and the collapse of retail in-person demand--the financial foundation of the entire system. Under the relentless pressure of financialization's stripmining and profteering, healthcare only survives if it can bill somebody somewhere a staggering amount for everything from office visits to procedures to hospital stays to medications.

Once that avalanche of billing dries up, the entire sector implodes: a sector that accounts for almost 20% of the U.S. economy.

Higher education is also imploding, and for the same reason: its output no longer justified its enormous cost structure. The same can be said of overbuilt retail and commercial space: the financial justification for sky-high rents have imploded and will never come back. The over-supply is so monumental and the collapse of demand so permanent, the gigantic pyramid of debt and speculative excess piled on all these excesses is collapsing.

A bailout by the Federal Reserve won't change the fundamentals of the collapse of financialization; all the Fed can do is reserve scarce lifeboat seats for its billionaire banker-financier pals. (Warren, you know Bill, have you met Jamie, Jeff, Tim and the rest of the Zillionaire Rat-Pack?)

Despite the record highs in the stock market--the ultimate expression of financialization disconnected from the real-world economy--financialization is also imploding. Financialization still claimed a connection to the real world of income streams and the value of the collateral underlying all the speculative profiteering: the high rents paid by the restaurants on the ground floor and the businesses for office space above justified the high value of the collateral, the commercial building.

Foundational swaths of the real-world economy have been swept away, and so the collateral is largely worthless. Lots of people want their employer to start paying for business-class airline seats again so they can jet around the country on somebody else's dime, staying in pricey hotels and attending conferences, but these activities no longer have any financial justification.

The economy of 1959 is finally expiring. The enormous time and money sinks of transporting humans hither and yon no longer have any financial justification.

The problem is the economy that's left has no means of creating tens of millions of jobs to replace those lost as the 1959 economic model collapses. We all know that automation is replacing human labor, but the real change is the collapse of the financial justification for the enormously costly systems we now depend on to generate jobs: healthcare, retail, tourism, dining out, education, working downtown, and all the professions dependent on managing all this complexity.

While the elimination of low-skill jobs--a longstanding trend--is attracting attention, the implosion of the 1959 economic model and financialization will soon sweep away millions of high-paying professional jobs that no longer have any financial justification.

As the 1959 economy implodes, so does the tax system based on payroll taxes and property taxes. This article sketches out the perverse incentives for employers to invest in automation rather than hire workers: Covid-19 Is Dividing the American Worker (WSJ.com)

There are alternatives, but they require accepting the implosion of both the 1959 economic model and its evil offspring, financialization.

I sketched out an alternative way of organizing work, everyday life and finance in my book A Radically Beneficial World. There are alternative ways of organizing civilization other than the insanely wasteful and exploitive system we now inhabit.''',


"24":'''How Nations Collapse: Disunity
August 24,
                2020

They may just opt out of the whole insane charade and stop paying the mountains of debt and stop trying to prop up the deranging pretense of middle-class snobbery.

Though many blame Donald Trump for dividing the nation, the nation was already disunited. Trump's election simply added day-glo paint to the lines that had long been hardening between disunited, disaffected camps.

As I've explained over the years, disunity is the systemic source of collapse-- not just of nations and empires but of enterprises and families. In other words, disunity is scale invariant: it breaks down marriages, family fortunes, partnerships, corporations, nations and empires with the same dynamics.

When challenges arise--and challenges always arise--the unified family, enterprise, nation or empire can make the shared sacrifices necessary to meet the crisis head-on, and not just survive, but as befits an anti-fragile system (as per Nassim Taleb's definition of anti-fragility), become stronger as a result of adapting to the crisis.

The family, enterprise, nation or empire fragmented by profound disunity is incapable of not just shared sacrifices but of a shared consensus on how to proceed against challenges such as famine, pandemic and economic depression.

It is the nature of human existence that shared sacrifice is the glue that binds disparate individuals and groups into a unified and thus powerful entity. In the early days of the Roman Republic and Empire, the wealthiest citizens were taxed heavily to raise the money needed to defend Rome or prosecute wars of conquest.

The patrician class served as officers in the army, and it was their duty to serve in the front lines, and in some cases (such as the horrendous defeat at Cannae) suffer higher combat death rates that common soldiers.

Profound disunity is characterized by the recognition that favored elites make no sacrifices, and this injustice consumes the binds of civil unity. The elites benefit the most from the system, piling up enormous fortunes and great political power, while the disempowered masses make the sacrifices on the battlefield and pay the taxes.

This disunity is not only political; it is social, economic and cultural as the elites' wealth soars in direct correlation to their unwillingness to make any sacrifices for the common good.

Grasping for power via philanthro-capitalist foundations is not a sacrifice; it's just a PR spin on the same old elitist accumulation of self-serving influence.

Though the mechanics are obscured by the financial games of central banks and financiers, the commoners understand that the nation's elites are parasitic and predatory, rigging the financial and political systems to benefit themselves at the expense of the nation and its citizenry.

Though it's convenient to divide America into two camps, anti-Trump and pro-Trump, these camps are each fragmented into disparate interests. There is no middle ground in the nation and none within the various warring camps.

As the Federal Reserve gooses the stock market to new heights, America's billionaires add hundreds of billions in additional wealth to their already obscene piles--piles largely untouched by taxes. In America, sacrifice has long been something demanded of the commoners: they fight the wars, they pay the taxes, they do the work and they sacrifice their health in jobs that only further enrich the few who reap all the gains while sacrificing nothing.

While America's spoiled, parasitic elites indulge in financial and sexual debauchery, fraud and embezzlement, the commoners grow weary of the widening divide in wealth, income, power, health and ethics. America's spoiled, parasitic elites are not just self-serving, greedy, and predatory; they're overconfident and hubris-soaked.

As for the commoners--they've been fragmented for decades into warring camps, fighting over social mores, political theater and all the frustrations of the powerless: embittered by the erosion of security and fairness and the indignities of slaving away for corporations that enrich the few while impoverishing the many, exhausted by the insecurities of chronic under-employment and the exploitations of the gig economy, the commoners may eventually find common cause in overthrowing their exploitive elites.

Or they may just opt out of the whole insane charade and stop paying the mountains of debt and stop trying to prop up the deranging pretense of middle-class snobbery in favor of an honest, low-cost mode of living that dispenses with servitude to self-serving, greedy elites and their corporate-plantation technocrat overlords.

Could America Have a French-Style Revolution? (July 14,
                2020)

Asking this is like asking, could the Western Roman Empire fall? Yes, it could, yes it did. Based on the nation's multiple sources of profound disunity, collapse is only a matter of when, not if.''',


"25":'''This Is How Systems Collapse
May 30,
                2020

Flooding the financial system with free money only restores the illusion of stability

I updated my How Systems Collapse graphic from 2018 with a we are here line to indicate our current precarious position just before the waterfall:



For those who would argue we're nowhere near collapse, consider that over 20% of the Federal Reserve's $2 trillion spew of free money went directly into the pockets of America's billionaires: $434 billion by the latest estimates, while most of the rest went into the pockets of the top 10% who own all the assets that the Fed is goosing higher while millions of households are worried about feeding themselves: (American billionaires got $434 billion richer during the pandemic).

In America's system, the solution to soaring, destabilizing inequality is... to goose inequality to new heights. No wonder there's no middle ground left politically, socially or financially, and social disorder is so easily ignited. There are few feedback loops left in our fragile system; the rich get richer, and rather than restore some balance, our political system further empowers the parasitic and predatory financial elites. The rich and politically powerful are one group, sharing control of public and private institutions.

One way to understand middle ground is that the middle ground acts as a buffer between systemic extremes. The key concepts here are stability and buffers. Though complex systems are never static, but they can be stable: that is, they ebb and flow within relatively stable states supported by buffers.

America's social, political and economic buffers have been thinned by extremes and excesses, but nobody noticed or cared: America's reigning credo is: anything goes, winners take all.

In systems, this ebb and flow of low-level volatility generates stability and adaptation. In natural systems, feedback loops between the weather, environment and plant/animal species keep the ecosystem in a state of dynamic equilibrium. Ideal weather conditions may spark a rise in an insect population, for example, which then enables an increase in insect-predator populations (fish, birds, frogs, etc.) which then increases the consumption of the insects and reduces the impact of the higher insect population.

If the river runs low, the human populace relies on wells for reserves of water. In good harvests, grain is set aside for lean harvests; the wells and grain stores are buffers which can be drawn down to restore stability to a stressed system.

Buffers are largely invisible and of little common interest in times of abundance. When water and grain are well-supplied, who cares if the stores have spoiled and the well water tastes bad?

A system with thin buffers and few feedback loops looks robust on the surface but is highly vulnerable to collapse. In our example, the first lean harvest and low water flow completely drain the reserves, and the second year of drought triggers a collapse of the system.

In our complex socio-economic system, the buffers are largely invisible. As a general rule, money (currency created by central banks and private banks when a loan is issued) is our all-purpose buffer: if something becomes scarce and threatens the system, we print/ borrow into existence more money which is distributed to buy whatever is needed.

But money is an illusory buffer. If the well has run dry, no amount of money will restore ground water. If the fisheries have collapsed due to overfishing, no amount of currency issued by the Federal Reserve will restore the fisheries. In other words, the natural world provides hard limits that money can only fix if buffers are available for purchase.

Money is itself a system, a system with financial buffers, buffers that have been consumed by the speculative excesses of the private sector and the financial repression of central banks. These buffers are largely invisible; few know what's going on in global liquidity markets, for example. Yet when liquidity dries up, for whatever reason, markets go bidless and asset prices go into freefall.

Flooding the financial system with free money only restores the illusion of stability. As noted in my diagram, restoring and maintaining an apparent stability thins buffers to the point of dangerous fragility.

When buffers are paper-thin, a crisis that would have been overcome with ease in the past triggers the collapse of the entire system. Everyone who based their faith in the system on its surface stability is stunned by the rapidity of the collapse, for how could such a vast, apparently robust system implode with so little warning?

The financial system's buffers have been thinning for 20 long years, but nobody seems to care. The quality of risk, debt, borrowers and speculative gambles have all declined, but faith in the Fed put--that the Federal Reserve can fix anything and everything by printing endless trillions-- is quasi-religious: few doubt the limitless power of the Fed's currency-printing machinery to quickly overcome any crisis.

This is how systems collapse: misplaced faith in the visible surface of abundance generates fatal complacency and confidence, and the fragility of the buffers goes unnoticed.

Just before the collapse, central bank currency is super-abundant, but systemic stability is near-zero and all the buffers are paper-thin: the Fed's trillions create an illusion of safety, as if all we need to do to restore the lost middle ground and buffers is to hand America's most parasitic and predatory clique another $434 billion in stock market wealth.

Doing more of what has destabilized the system in the belief that new extremes will somehow restore equilibrium is simply rowing faster as we speed toward the waterfall of systemic collapse.''',


"26":'''Our Inevitable Collapse: We Can't Save a Fragile Economy With Bailouts That Increase Fragility
May 1,
                2020

By bailing out the sources of systemic fragility with trillions of dollars, the Fed has shifted the risk to the entire financial system and the nation's currency.

That the global economy is fragile is painfully obvious to all. What is less obvious is the bailouts intended to save the fragile economy actively increase its fragility, setting up an inevitable collapse of the entire precarious system.

Systems that are highly centralized, i.e. dependent on a handful of nodes that are each points of failure--are intrinsically fragile and prone to collapse. Put another way, systems in which all the critical nodes are tightly bound are prone to domino-like cascades of failure as any one point of failure quickly disrupts every other critical node that is bound to it.

Ours is an economy in which capital, wealth, power and control are concentrated in a few nodes of the network/ecosystem we call the economy. A handful of corporations own the vast majority of the media, a handful of banks control most of the lending and capital, a handful of hospital chains, pharmaceutical companies and insurers control healthcare, and so on.

Control of digital technologies is even more concentrated, in virtual monopolies: Google for search and Youtube, etc. and Facebook / Instagram and Twitter for social media, Microsoft and Apple for operating systems and services derived from OS, and so on.

The vast majority of participants in the economy are tightly bound to these concentrated nodes of capital and power, and these top-down, hierarchical dependencies generate fragility.

When unexpectedly severe variability and volatility occur, the disruption of a few nodes brings down the entire system. Thus the disruption of the subprime mortgage subsystem--a relatively small part of the total mortgage market and a tiny slice of the global financial system--nearly brought down the entire global financial system in 2008 because the GFS is a tightly bound system of centralized concentrations of capital, power and control.

Currently, we're seeing the fragility of a meat production system that has concentrated ownership and production of meatpacking into a relatively few nodes on which the entire food supply chain is totally dependent.

And so what's the status quo "fix" when this intrinsically fragile system comes apart? Increase its fragility by bailing out the most tightly bound, dominant nodes. This is what the monopoly on creating currency, the Federal Reserve, is doing on a vast scale.

Rather than reducing the fragility of the system, the Federal Reserve is increasing the fragility, guaranteeing a collapse of not just the financial system but the currency as well.

To better understand systemic fragility, we turn to Nassim Taleb's description of antifragile systems. For those who haven't read Taleb's book Antifragile: Things That Gain from Disorder, here is a partial definition: Nassim Taleb: A Definition of Antifragile and its Implications:

Some things benefit from shocks; they thrive and grow when exposed to volatility, randomness, disorder, and stressors and love adventure , risk, and uncertainty. Yet, in spite of the ubiquity of the phenomenon, there is no word for the exact opposite of fragile. Let us call it antifragile. Antifragility is beyond resilience or robustness. The resilient resists shocks and stays the same; the antifragile gets better. This property is behind everything that has changed with time: evolution, culture, ideas, revolutions, political systems, technological innovation, cultural and economic success, corporate survival, good recipes, the rise of cities, cultures, legal systems, equatorial forests, bacterial resistance...even our own existence as a species on this planet.

And we can almost always detect antifragility (and fragility) using a simple test of asymmetry: anything that has more upside than downside from random events (or certain shocks) is antifragile; the reverse is fragile.

We have been fragilizing the economy, our health, political life, education, almost everything... by suppressing randomness and volatility. Much of our modern, structured, world has been harming us with top-down policies and contraptions (dubbed 'Soviet-Harvard delusions' in the book) which do precisely this: an insult to the antifragility of systems. This is the tragedy of modernity: as with neurotically overprotective parents, those trying to help are often hurting us the most.

Given the unattainability of perfect robustness, we need a mechanism by which the system regenerates itself continuously by using, rather than suffering from, random events, unpredictable shocks, stressors, and volatility.

Does our financial system advance via unexpected shocks, extreme volatility, unknown unknowns and ceaseless variability? You're joking, right? The smallest perturbation in any node brings the system to the edge of collapse. Exhibit #1 is last Fall's spot of bother in the obscure financial node known as the repo market. This relatively modest part of the financial system almost triggered a stock market crash, and so the monopoly on creating currency, the Fed, immediately printed hundreds of billions of dollars to bail out every single player in the repo market--all behind the scenes, of course, lest the extreme fragility of the entire over-leveraged, speculative contraption become visible.

Making an incredibly fragile system more fragile via bailing out every node of concentrated capital, power and control guarantees the entire rotten structure will collapse. As I have often pointed out here, risk cannot be made to disappear, it can only be shifted. By bailing out the sources of systemic fragility with trillions of dollars, the Fed has shifted the risk to the entire financial system and the nation's currency.

Simply put: the only possible output of Fed bailouts is the complete collapse of the entire financial system, including the currency the Fed is creating with such abandon.''',


"27":'''Why Assets Will Crash
May 4,
                2020

This is how it happens that boats that were once worth tens of thousands of dollars are set adrift by owners who can no longer afford to pay slip fees.

The increasing concentration of the ownership of wealth/assets in the top 10% has an under-appreciated consequence: when only the top 10% can afford to buy assets, that unleashes an almost karmic payback for the narrowing of ownership, a.k.a. soaring wealth and income inequality: assets crash.

Most of you are aware that the bottom 90% own very little other than their labor (tradeable only in full employment) and modest amounts of home equity that are highly vulnerable to a collapse of the housing bubble. (The same can be said of China's middle class, only more so, as 75% of China's household wealth is in real estate, more than double the percentage of wealth held in housing in U.S. households.)



As the chart illustrates, the top 10% own 84% of all stocks, over 90% of all business equity and over 80% of all non-home real estate. The concentration of ownership of assets such as vintage autos, collectibles, art, pleasure craft and second homes in the top 10% is likely even greater.

The more expensive the asset, the greater the concentration of ownership, as the top 5% own roughly 2/3 of all wealth, the top 1% own 40% and the top 0.1% own 20%. In other words, the more costly the asset, the narrower the ownership. (Total number of US households is about 128 million, so the top 5% is around 6 million households and the top 1% is 1.2 million households.)



This means the pool of potential buyers is relatively small, even if we include global wealth owners.

Since price is set on the margins, and assets like houses are illiquid, then we can anticipate all the markets for assets owned solely by the wealthy to go bidless--yachts, collectibles, vacation real estate--because the pool of buyers is small, and if that pool gets cautious due to a drop in net worth/unearned income, there won't be any buyers except at the margins, at incredible discounts.

As we know, in a neighborhood of 100 homes currently valued ar $1 million each, when a desperate seller accepts $500,
                000, the value of the other 99 homes immediately drops to $500,
                000.

Since few of the current bubble-era asset valuations are supported by actual income fundamentals, then the sales price boils down to a very small number of potential buyers and what they're willing to pay.

Houses have a value based on rent, of course, but rents will drop very quickly for the same reason: prices are set on the margins. The most desperate landlords will drop rents and re-set the rental market from the margins. If demand plummets (which it will as people can no longer afford rents in hot urban markets once they lose their jobs), then vacancies will soar and rents will crash as a few desperate landlords will take $1200/month instead of $2500/month.

Due to the multi-year building boom of multi-family buildings in hot job markets (which inevitably leads to an over-supply once the boom ends), there are now hundreds of vacancies where there were once only a few dozen, and thousands where there were previously only hundreds.

As millions of wait staff, bartenders, etc. who made good money in tips find their jobs have vanished, all the urban hotspots will see mass out-migration: Seattle, Portland, the S.F. Bay Area, L.A., NYC, Denver, etc. as demand for rentals will evaporate and rents will be set on the margins by the most desperate landlords. Everyone holding out for the previous bubble-era rent will have $0 income as their units are vacant.

Tech start-ups and Unicorns are melting like ice cubes in Death Valley, and tech-sector layoffs are already in the tens of thousands. This wave of highly paid techies losing their jobs will become a tsunami, further reducing the pool of people who can afford rents of $2,
                500 to $3,
                000 for a studio or one-bedroom apartment.)

The concentration of ownership generates a self-reinforcing feedback that further depresses prices: since the top 10% own most of the assets of the nation, they are most prone to a reversal of the wealth effect. As their assets soared in value, the top 10% felt wealthier and more confident in future gains, enabling them to borrow and spend freely on second homes, pleasure craft, new vehicles, collectibles, luxury travel, etc.

Once even one class of assets plummets in value--for example, the recent decline in the stock market-- the wealth effect reverses and the top 10% feel poorer and less confident about future gains, and thus less enthused about borrowing and spending. The demand for other costly assets quickly evaporates, further reducing the wealth of the ownership class, which further reduces their desire and ability to buy bubble-era assets.

The high-priced assets owned by the top 10% will be the assets least in demand due to their high cost and potential for enormous losses: nothing loses value faster in a recession that narrowly owned assets such as vintage cars, art, vacation homes, yachts, etc.

Once assets start sliding in value, the reverse wealth effect quickly dries up demand for all asset classes with narrow ownership. Since these assets are illiquid--that is, the market for them is thin, with buyers few and far between--the prices are set by a very shallow pool of buyers and desperate sellers.

Consider a pleasure craft that retails new for $120,
                000. In the boom era of rising stocks and housing, a used boat might fetch $65,
                000. But as the wealth of the small pool of households able to buy and maintain a costly craft evaporates, the number of qualified buyers evaporates, too.

The seller might be aghast by an offer of $35,
                000 and reject it angrily. Six months later, he's praying someone will take it off his hands for $15,
                000, and in another six months, he'll accept $500 just to get out from underneath the insurance, slip-rental and licencing fees.

This is how it happens that boats that were once worth tens of thousands of dollars are set adrift by owners who can no longer afford to pay slip fees, and vacation homes are abandoned and auctioned off for overdue property taxes: the market for these luxuries dries up and blows away, i.e. goes bidless--there are no buyers at any price.

Once housing and real estate valuations fall, that will trigger a decline in the value of all other costly, narrowly owned assets, which will reinforce the reverse wealth effect.

This is the systemic payback for concentrating ownership of assets in the hands of the few: when their bubble-era priced assets plummet in value, the bottom falls out of all assets with narrow ownership. The price of superfluous assets such as boats, vintage cars, collectibles, art and vacation homes can quickly fall to a fraction of bubble-era valuations, destroying much of what was always fictional capital.

(For more on the intrinsic fragility of a system that concentrates ownership in the hands of the few, please read Our Inevitable Collapse: We Can't Save a Fragile Economy With Bailouts That Increase Fragility May 1, 2020.)

The Federal Reserve reckons it can save the bubble-era valuations of junk bonds by being the buyer of last resort, but it will end up being the only buyer, effectively making the system even more fragile and prone to collapse.

The public will eventually have to decide if the nation's central bank should be bailing out assets owned by the financial elite while the upper-middle class watches its assets collapse in value.''',


"28":'''The Wonderful Insanity of Globalization
April 1,
                2020

So here's an April Fools congrats to globalization's many fools.

The tradition here at Of Two Minds is to make use of April Fool's Day for a bit of parody or satire, but I'm breaking with tradition and presenting something that is all too real but borders on parody: the wonderful insanity of globalization.

Like the famous emperor with no clothing, globalization's countless glorious benefits have been flogged by neoliberal elites and its corporate media shills with such relentlessly manic enthusiasm (let's call it what it is: a form of greed-fueled insanity) that the average worker has come to accept the wonderfulness of globalization as a natural force much like gravity: it's inescapable.

Meanwhile, the globalization emperor has no clothes. Globalization has generated a wonderful (satire alert) insanity in which efficiencies and fragilities are ignored and fatal excesses are deemed worthy of frothy praise: look at the emperor's fine garments!

This is how we've reached the level of insanity in which 90% of essential medications and their components are manufactured by our geopolitical rival. Other examples of the insanity of globalization are too numerous to list, but let's consider the route that the vaunted supply chain actually takes to get Product A from China to an American consumer.

According to the holy scripture (pun intended) of globalization, comparative advantage overcomes any inefficiencies due to long supply routes: if the $100 product can be made in China for $50, then the enormous profits reaped by moving production to China more than make up for any transport inefficiencies or systemic fragilities created by the long supply chain.

In the happy story of globalization, cheap container ships merrily haul billions of dollars of profitable goods across thre Pacific for next to nothing in costs. Perhaps, but let's look at a real-world transport route from China to the U.S. for one not-very-costly product which was air-freighted.

Please gaze in awe at the incredible efficiencies of a global supply chain that ships the product from Beijing, China, to ZhengZhou, China, to Incheon, South Korea, to Anchorage, Alaska, to Louisville, Kentucky, to Ontario, California, and from there to its mid-Pacific destination, Honolulu, Hawaii.

The obvious efficiencies of the last 10,
                000 miles are, well, so obvious they need no further elaboration. Even with jet fuel cheaper than soft drinks, the cost of flying, staffing and maintaining aircraft costing tens of millions of dollars is non-trivial, but apparently all that flying across oceans and continents and then back again is a truly excellent means of reaping enormous profits for everyone involved.

Or not. So here's an April Fools congrats to globalization's many fools.''',


"29":'''Climate Crisis and Population Growth Will Displace 1 Billion over Next 30 Years
Posted on September 12,
                2020 by Jerri-Lynn Scofield
By Jerri-Lynn Scofield, who has worked as a securities lawyer and a derivatives trader. She is currently writing a book about textile artisans.

Yesterday was one of those days that I learned far more from the commentariat in their comments on my post about climate change and the Oregon wildfire crisis than I conveyed in my text, More than 500,
                000 People in Oregon Flee Wildfires.

A half a million people have been displaced so far by the wildfire crisis in Oregon alone.

Now, one thing the commentariat emphasised is that wildfires in the Pacific northwest are not a new phenomenon. But prevailing forest management policies have certainly worsened the problem, as has relentless dynamics of climate change.

This is an ongoing crisis in some of the most affluent parts of the country that is supposed to be the richest in the world. This year Oregon and Washington have been caught up in the crisis, as has California, for which wildfires are now an annual scourge.

I juxtaposed this crisis against some reading today in the Guardian, reporting on a study done by the Institute for Economics and Peace (IEP), that concluded that more than 1.2 billion people living in 31 countries are not sufficiently resilient to withstand ecological threats, and could find themselves as involuntary migrants by 2050, according to Climate crisis could displace 1.2bn people by 2050, report warns.

Wealthier, more developed regions in Europe and North America face fewer ecological threats and would be better able to cope with them, but most “will not be immune from wider impacts”. The report said 16 countries, Sweden, Norway, Ireland, and Iceland, faced no threat.

Tell that to the people of the Pacific northwest at the moment.

Alas, ecological catastrophe may prove to be much more devastating to poorer countries, according to the IEP’s Ecological Threat Register, which notes that “19 countries with the highest number of ecological threats are among the world’s 40 least peaceful countries including Afghanistan, Syria, Iraq, Chad, India and Pakistan.”

Over to  the Guardian again:

Many of the countries most at risk from ecological threats, including Nigeria, Angola, Burkina Faso and Uganda, are also predicted to experience significant population increases, the report noted, further driving mass displacements.

“This will have huge social and political impacts, not just in the developing world, but also in the developed, as mass displacement will lead to larger refugee flows to the most developed countries,” Steve Killelea, the institute’s founder, said.

“Ecological threats pose serious challenges to global peace. Over the next 30 years, lack of access to food and water will only increase without urgent global cooperation. In the absence of action, civil unrest, riots and conflict will most likely increase.”

Withstanding Ecological Threats

The study evaluates the exposure of 157 countries to to eight ecological threats, then analyzes their relative resilience  to withstand the threat. By 2050,
                141 countries will face at least one ecological threat , with the regions of sub-Saharan Africa, South Asia, the Middle East and North Africa those most exposed to the greatest number of threats.

According to the IEP:

By 2040, a total of 5.4 billion people – more than half of the world’s projected population – will live in the 59 countries experiencing high or extreme water stress, including India and China.
5 billion people could suffer from food insecurity by 2050; which is an increase of 1.5 billion people from today.
The lack of resilience in countries covered in the ETR will lead to worsening food insecurity and competition over resources, increasing civil unrest and mass displacement, exposing developed countries to increased influxes of refugees.
Methodology: Ecological Threat Register

The IEP is trying to predict some of the political consequences that will follow from ecological threats in part caused by climate change:

The Ecological Threat Register analyses risk from population growth, water stress, food insecurity, droughts, floods, cyclones, rising temperatures and sea levels. Over the next 30 years, the report finds that 141 countries are exposed to at least one ecological threat by 2050. The 19 countries with the highest number of threats have a combined population of 2.1 billion people, which is around 25 per cent of the world’s total population.

The ETR analyses the levels of societal resilience within countries to determine whether they have the necessary coping capacities to deal with future ecological shocks. The report finds that more than one billion people live in countries that are unlikely to have the ability to mitigate and adapt to new ecological threats, creating conditions for mass displacement by 2050.

The country with the largest number of people at risk of mass displacements is Pakistan, followed by Ethiopia and Iran. Haiti faces the highest threat in Central America. In these countries, even small ecological threats and natural disasters could result in mass population displacement, affecting regional and global security.

Resource Stress Leads to Political Unrest

I point out that these resource threats are already leading to political unrest. India and Pakistan don’t need yet another issue to fight over, as they have gone to war more than once since Partition, with the latest skirmishes occurring just last year.Now, they have been squabbling over the waters of the Indus for a very long time. Water disputes will no doubt continue and indeed accelerate.

Nor do China and India need additional areas to dispute- with stress between the countries exacerbating in recent months. leading to bloodshed. And it comes as no news that China is tying up the waters that flow through the Tibetan plateau, as well as other rivers, such as the Mekong.

The countries judged to be the most vulnerable are the least able to withstand these ecological threats.

I encourage readers to click on the following link, to see which countries the IEP deems the most vulnerable, Overall ETR Score.

Now no surprises among the weakest countries, which include Afghanistan, Pakistan, Iraq, Iran, and India. and other Middle Eastern, and Sub-saharan Africa states.

What stood out, however, was that the United States squarely among the next group of countries. Just as the rest of the world averts its eyes rather than examine closely our COVID-19 record, the wildfire crisis produces a similar response. I point out that such a reaction is not just to the unique US situation. It wasn’t so long ago that the world’s eyes were trained on the Australian wildfire crisis. And Australia is also listed in the same group as the U.S. on the Ecological Threat Register. As are Russia, China, and the Netherlands.

Whereas the next group included Canada, Turkey, Bangladesh, Vietnam, Timor-Leste, Spain, and Italy..  As someone who was quite peripatetic in the pre-CoVID-19 universe, this really comes as no shock to me. Whenever I find myself in the US, I am often stunned to see how much the infrastructure has declined. Or rather, how much the rest of the world has caught up.

I would have reproduced the complete list, except to do so includes the flags of each country, making the complete list of around 150 bulky and unwieldy. So I encourage interested readers to go to the link, which includes the full list, as well as an interactive map.

And what we are seeing in Oregon is, from what you have told me, is a combination of a natural historical cycle. Exacerbated by climate change. Made worse by our appetite for living in the wilderness – which may be a consequence of zoning ourselves out of city living space. And made much, much worse by infrastructural decline, and poor forest management.

Yves has mentioned in another context that because the United States is so relatively rich, it’s been able to tolerate high levels of political corruption, and our overpriced, less-than-universal health care system.

COVID-19 has pointed out the flaws in that model.

And, similarly, climate change is testing our infrastructure policies.

The question I think is how seriously wanting it will find us.''',


"30":'''How US Consumers Use Their Stimulus Payments
Posted on September 10,
                2020 by Yves Smith
Yves here. Although the reinforcement of the neoliberal frame (“consumers” as opposed to “citizens”) is irritating, this study of the impact of stimulus payments debunks the idea that helping the poors makes them lazy.

By Olivier Coibion, Associate Professor, UT Austin; Yuriy Gorodnichenko, Quantedge Presidential Professor, Department of Economics, University of California – Berkeley; and Michael Weber, Associate Professor of Finance, University of Chicago Booth School of Business. Originally published at VoxEU

A major component of the 27 March CARES Act in the US was a one-time transfer to all qualifying adults of up to $1200, with $500 per additional child. Using a large-scale survey of US consumers, this column studies how these large transfers affected individuals’ consumption, saving and labour supply decisions. Most respondents report that they primarily saved or paid down debts with their transfers, with only about 15% reporting that they mostly spent it. On average, individuals report having spent or planning to spend only around 40% of the total transfer. The payments appear to have had no meaningful effect on labour-supply decisions from these transfer payments, except for 20% of the unemployed who report that the stimulus payment made them search harder for a job.

Amidst the rising spread of COVID-19 and the pervasive imposition of lockdowns in March 2020, the US Federal government passed the CARES Act on 27 March 2020. This stimulus package was exceptional both in its size (over $2 trillion in allocated funds) and in the speed at which it was legislated and implemented. A major component was a one-time transfer to all qualifying adults of up to $1200, with $500 per additional child. Model-based estimates suggest that the fiscal multiplier might be as high as 2, but so far little is known how household consumption responded to the fiscal transfer (Bayer et al. 2020). While the 2001 and 2008 fiscal stimulus payments provide some guidance (Shapiro and Slemrod 2003, Agarwal et al. 2003, Johnson et al. 2006, Parker 2011), the unprecedented nature of the COVID-19 shock, the associated uncertainty about the length and severity of the pandemic, and the widespread prevalence of lockdowns which restrict in-person shopping make it ex-ante unclear how individuals used their payments.

Stimulus Cheques and Household Consumption and Savings

Using a large-scale survey of US households, in Coibion et al. (2020) we document that only 15% of recipients of this transfer say that they spent (or planned to spend) most of their transfer payment, with the large majority of respondents saying instead that they either mostly saved it (33%) or used it to pay down debt (52%). When asked to provide a quantitative breakdown of how they used their cheques, US households report having spent approximately 40% of their cheques on average, with about 30% of the average cheque being saved and the remaining 30% being used to pay down debt. Little of the spending went to hard-hit industries selling large durable goods (cars, appliances, etc.). Instead, most of the spending went to food, beauty, and other non-durable consumer products that had already seen large spikes in spending even before the stimulus package was passed because of hoarding.

Effects of Stimulus Payments on Behaviour

We report in Table 1 the response of households to the qualitative question of how they used their stimulus payment: mostly spent, mostly saved, or mostly to pay off debt.

Table 1 Distribution for the use of stimulus payment, qualitative.



Notes: the table reports the distribution of qualitative responses for the use of stimulus payment.

Column 1 focuses on the 90% of households in the survey who have already received their payment. Only 15% report that they mostly spent their transfer, even lower than the corresponding values found after the 2001 and 2008 transfers. One third report that they primarily saved the stimulus money, leaving over half of respondents answering that they primarily used the Treasury transfers to pay off debt. Column 2 presents equivalent shares for survey participants who anticipate receiving a cheque but have not received one yet. They report very similar plans to those who have already received their payments: only 12% plan to mostly spend it while more than half plan to use it primarily to pay off debt. Even those who do not qualify for a stimulus payment report similar answers when asked hypothetically what they would do if they received $1,
                000 from the Federal government: 14% report that they would primarily spend the money. However, a larger share of these individuals report that they would save the money rather than pay off debts, likely reflecting the fact that most of those who are ineligible for stimulus payments are higher-income and are less likely to be constrained by debt levels. Jointly, these qualitative responses suggest that the stimulus payments had only limited effects on spending.

In addition to qualitative questions, the survey asked participants to assign specific dollar values to different ways they used (or would use) their stimulus payments, including saving, paying off debt and different categories of spending. On average, households report having spent approximately 40% of their stimulus cheques, with the remaining 60% split almost evenly between saving (27% of stimulus) and paying off debts (31% of stimulus). Relatively little of the spending went to large durable goods or medical care (7% and 6%, respectively). Instead, most of the spending was on food and personal care products (16%) or other consumer products (13%).

Figure 1 shows heterogeneity in marginal propensities arises to most categories of using stimulus funds. For example, a little over 20% of respondents saved all of their stimulus cheques while over 60% saved none. Similarly, ≈15% of individuals reported that they had used all of their payment on paying down debt, while nearly 60% used none at all for this purpose. Spending categories are similarly dispersed: almost 90% report that they spent none of their stimulus payment on large durable goods, and 20% claim that they did not spend any extra money on medical care or other consumer goods.

Figure 1 Expenditure share for stimulus payments (effectively marginal propensities)



Notes: each panel in the figure reports the distribution for the share of stimulus payment used for saving, paying off debts, and consumer spending.

Which individuals tend to spend their stimulus payment? The question of identifying consumers whose MPCs are higher matters not just for the effectiveness of stimulus packages but more generally for understanding economic dynamics, as emphasised by Kaplan and Violante (2014). There are a number of observable factors that make it more likely that a respondent mostly spent their stimulus payment. For example, men are a little more likely to spend their cheques than women, although the difference is small in economic terms. African Americans are much more likely than whites to primarily pay off their debts, whereas Hispanics are less likely to pay off debts and more likely to spend the payment. Additional factors that make individuals more likely to spend their cheques include being out of the labour force and neither owning a home nor renting (e.g. living with parents). Finally, those who received larger payments (even after conditioning on household size) are less likely to spend their payments and more likely to save them. Given how large the COVID-related stimulus payments were relative to those in 2001 or 2008, it is consistent with consumer theory that a larger fraction would be saved compared to previous experiences.

Another source of economically large differences is liquidity constrains. Constrained households spend 10% more than unconstrained ones, which is allocated mostly to additional spending on food/beauty/personal products and medical care. We also see that those who lost earnings due to the COVID pandemic use about 5% more of the stimulus to pay off debt and 4% less to increase savings, and also spend relatively more on medical care but less on other consumer products, suggesting that their lost earnings were preventing them from getting all the medical services that they needed. We find little role for individuals’ macroeconomic expectations.

Respondents were also asked about how stimulus affected (or would affect) their labour supply decisions. The vast majority (90%) of the employed report that it had no effect on their labour supply decision. About two-thirds of those that are unemployed reported that it had no effect on their job search decision, while over 20% report that the stimulus cheque led them to search harder for a job. In short, we find evidence that some unemployed workers increase their job search effort in response to stimulus payments but otherwise find no meaningful evidence of labour supply effects from the CARES Act one-time transfers.

Conclusion

Sending money directly to households has been one of the main components of US stimulus packages in the last three recessions. We provide some of the first estimates for transfers to US households put in place under the CARES Act. US households only spent around 40% of their stimulus payments but there is significant heterogeneity in terms of how different individuals respond. Many spent their entire stimulus payment, and just as many saved their entire cheque or used it to pay off debt.''',


"31":'''Michael Hudson: How an “Act of God” Pandemic Is Destroying the West: The U.S. Is Saving the Financial Sector, Not the Economy
Posted on September 1,
                2020 by Yves Smith
Yves here. Michael Hudson explains how the American fixation on protecting creditors is making our bad response to the coronacrisis even worse. And unlike the 2008 crisis, this time the damage to the real economy is overwhelming, meaning the logic of putting financial firms at the head of the line is even weaker than back then.

By Michael Hudson, a research professor of Economics at University of Missouri, Kansas City, and a research associate at the Levy Economics Institute of Bard College. His latest book is “and forgive them their debts”: Lending, Foreclosure and Redemption from Bronze Age Finance to the Jubilee Year

Before juxtaposing the U.S. and alternative responses to the coronavirus’s economic effects, I would like to step back in time to show how the pandemic has revealed a deep underlying problem. We are seeing the consequences of Western societies painting themselves into a debt corner by their creditor-oriented philosophy of law. Neoliberal anti-government (or more accurately, anti-democratic) ideology has centralized social planning and state power in “the market,” meaning specifically the financial market on Wall Street and in other financial centers.

At issue is who will lose when employment and business activity are disrupted. Will it be creditors and landlords at the top of the economic scale, or debtors and renters at the bottom? This age-old confrontation over how to deal with the unpaid rents, mortgages and other debt service is at the heart of today’s virus pandemic as large and small businesses, farms, restaurants and neighborhood stores have fallen into arrears, leaving businesses and households – along with their employees who have no wage income to pay these carrying charges that accrue each month.

This is an age-old problem. It was solved in the ancient Near East simply by annulling these debt and rent charges. But the West, shaped as it still is by the legacy of the Roman Empire, has left itself prone to the massive unemployment, business closedowns and resulting arrears for these basic costs of living and doing business.

Western civilization distinguishes itself from its Near Eastern predecessors in the way it has responded to “acts of God” that disrupt the means of support and leave debts in their wake. The United States has taken the lead in rejecting the path by which China, and even social democratic European nations have prevented the coronavirus from causing widespread insolvency and polarizing their economies. The U.S. coronavirus lockdown is turning rent and debt arrears into an opportunity to impoverish the indebted economy and transfer mortgaged property and its income to creditors.

There is no inherent material need for this fate to occur. But it seems so natural and even inevitable that, as Margaret Thatcher would say, There Is No Alternative.

But of course there is, and always has been. However, resilience in the face of economic disruption always has required a central authority to override “market forces” to restore economic balance from “above.”

Individualistic economies cannot do that. To the extent that they have a strong state, they are not democratic but oligarchic, controlled by the financial sector in its own interest, in tandem with its symbiotic real estate sector and monopolized infrastructure. That is why every successful society since the Bronze Age has been a mixed economy. The determining factor in whether or not an economic disruption leaves a crippled economy in its wake turns out to be whether its financial sector is a public utility or is privatized from the debt-strapped public domain as a means to enrich bankers and money-lenders at the expense of debtors and overall economic balance.

China is using an age-old policy common ever since Hammurabi and other Bronze Age rulers promoted economic resilience in the face of “acts of God.” Unless personal debts, rents and taxes that cannot be paid are annulled, the result will be widespread bankruptcy, impoverishment and homelessness. In contrast to America’s financialized economy, China has shown how natural it is for society simply to acknowledge that debts, rents, taxes and other carrying charges of living and doing business cannot resume until economic normalcy is able to resume.

Near Eastern Protection of Economic Resilience in the Face of Acts of God

Ancient societies had a different logic from those of modern capitalist economies. Their logic – and the Jewish Mosaic Law of Leviticus 25, as well as classical Greek and Roman advocates of democratic reform – was similar to modern socialism. The basic principle at work was to subordinate market relations to the needs of society at large, not to enrich a financial rentierclass of creditors and absentee landowners. More specifically, the basic principle was to cancel debts that could not normally be paid, and prevent creditors from foreclosing on the land of debtors.

All economies operate on credit. In modern economies bills for basic expenses are paid monthly or quarterly. Ancient economies operated on credit during the crop year, with payment falling due when the harvest was in – typically on the threshing floor. This cycle normally provided a flow of crops and corvée labor to the palace, and covered the cultivator’s spending during the crop year. Interest typically was owed only when payment was late.

But bad harvests, military conflict or simply the normal hardships of life frequently prevented this buildup of debt from being paid. Mesopotamian palaces had to decide who would bear the loss when drought, flooding, infestation, disease or military attack prevented the payment of debts, rents and taxes. Seeing that this was an unavoidable fact of life, rulers proclaimed amnesties for taxes and these various obligations incurred during the crop year. That saved smallholders from having to work off their debts in personal bondage to their creditors and ultimately to lose their land.

For these palatial economies, resilience meant stabilization of fiscal revenue. Letting private creditors (often officials in the palace’s own bureaucracy) demand payment out of future production threatened to deprive rulers of crop surpluses and other taxes, and corvée labor or even service in the military. But for thousands of years, Near Eastern rulers restored fiscal viability for their economies by writing down debts, not only in emergencies but more or less regularly to relieve the normal creeping backlog of debts.

These Clean Slates extended from Sumer and Babylonia in the 3rdmillennium BC to classical antiquity, including the neo-Assyrian, neo-Babylonian and Persian Empires. They restored normal economic relations by rolling back the consequences of debts personal and agrarian debts – bondage to creditors, and loss of land and its crop yield. From the palace’s point of view as tax collector and seller of many key goods and services, the alternative would have been for debtors to owe their crops, labor and even liberty to their creditors, not to the palace. So cancelling debts to restore normalcy was simply pragmatic, not utopian idealism as was once thought.

The pedigree for “act-of-God” rules specifying what obligations need not be paid when serious disruptions occur goes back to the laws of Hammurabi c. 1750 BC. Their aim was to restore economic normalcy after major disruptions. §48 of Hammurabi’s laws proclaim a debt and tax amnesty for cultivators if Adad the Storm God has flooded their fields, or if their crops fail as a result of pests or drought. Crops owed as rent or fiscal payments were freed from having to be paid. So were consumer debts run up during the crop year, including tabs at the local ale house and advances or loans from individual creditors. The ale woman likewise was freed from having to pay for the ale she had received from palace or temples for sale during the crop year.

Whoever leased an animal that died by an act of god was freed from liability to its owner (§266). A typical such amnesty occurred if the lamb, ox or ass was eaten by a lion, or if an epidemic broke out. Likewise, traveling merchants who were robbed while on commercial business were cleared of liability if they swore an oath that they were not responsible for the loss (§103).

It was realized that hardship was so inevitable that debts tended to accrue even under normal conditions. Every ruler of Hammurabi’s dynasty proclaimed a Clean Slate cancelling personal agrarian debts (but left normal commercial business loans intact) upon taking the throne, and when military or other disruptions occurred during their reign. Hammurabi did this on four occasions.[
                        1
                ]

Bronze Age rulers could not afford to let such bondage and concentration of property and wealth to become chronic. Labor was the scarcest resource, so a precondition for survival was to prevent creditors from using debt leverage to obtain the labor of debtors and appropriate their land. Rulers therefore acted to prevent creditors from becoming a wealthy class seeking gains by impoverishing debtors and taking crop yields and land for themselves.

By rejecting such alleviations of debts resulting from economic disruption, the U.S. economy is subjecting itself to depression, homelessness and economic polarization. It is saving stockholders and bondholders instead of the economy at large. That is because today’s rentierinterests take the economic surplus in the form of debt service, holding labor and also corporate industry in bondage. Mortgage debt is the price of obtaining a home of one’s own. Student debt is the price of getting an education to get a job. Automobile debt is needed to buy a car to drive to the job, and credit-card debt must be run up to pay for living costs beyond what one is able to earn. This deep indebtedness makes workers afraid to go on strike or even to protect working conditions, because being fired is to lose the ability to pay debts and rents. So the rising debt overhead serves the business and financial sector by lowering wage levels while extracting more interest, financial fees, rent and insurance out of their take-home pay.

Debt Deflation and the Transition from Finance Capitalism to an Austerity Economy

By injecting $10 trillion into the financial markets (when Federal Reserve credit is added to U.S. Treasury allocation), the CARES act enabled the stock market to recover all of its 34 percent drop (as measured by the S&P 500 stocks) by June 9, even as the economy’s GDP was still plunging. The government’s new money creation was not spent to revive the real economy of production and consumption, but at least the financial One Percent was saved from loss. It was as if prosperity and living standards would somehow return to normal in a V-shaped recovery.

But what is “normal” these days? For 95 percent of the population, their share of GDP already had been falling ever since the Obama Depression began with the bank bailout in 2009, leaving an enormous bad-debt overhead in place. The economy’s long upswing since World War II was already grinding to an end as it struggled to carry its debt burden, rising housing costs, health care and related monthly “nut.”[
                        2
                ]

This is not what was expected 75 years ago. World War II ended with families and businesses rife with savings and with little debt, as there had been little to buy during the wartime years. But ever since, each business cycle recovery has started with a higher ratio of debt to income, diverting more revenue from business, households and governments to pay banks and bondholders. This debt burden raises the economy’s cost of living and doing business, while leaving less wage income and profit to be spent on goods and services.

The virus pandemic has merely acted as a catalyst ending of the long postwar boom. Yet even as the U.S. and other Western economies begin to buckle under their debt overhead, little thought has been given to how to extricate them from the debts and defaults that have accelerated as a result of the broad economic disruption.

The “business as usual” approach is to let creditors foreclose and draw all the income and wealth over subsistence needs into their own hands. Economies have reached the point where debts can be paid only by shrinking production and consumption, leaving them as strapped as Greece has been since 2015. Rejecting debt writedowns to restore social balance was implanted at the outset of modern Western civilization. Ever since Roman times it has become normal for creditors to use social misfortune as an opportunity to gain property and income at the expense of families falling into debt. Blocking the emergence of democratic civic regimes empowered to protect debtors, creditor interests have promoted laws that force debtors to lose their land or other means of livelihood to foreclosing creditors or sell it under distress conditions and have to work off their debts.

In times of a general economic disruption, giving priority to creditor claims leads to widespread bankruptcy. Yet it violates most peoples’ ideas of fairness and distributive justice to evict debtors from their homes and take whatever property they have if they cannot pay their rent arrears and other charges that have accrued through no fault of their own. Bankruptcy proceedings will force many businesses and farms to forfeit what they have invested to much wealthier buyers. Many small businesses, especially in urban minority neighborhoods, will see yeas of saving and investment wiped out. The lockdown also forces U.S. cities and states to cope with plunging sales- and income-tax revenue by slashing social services and depleting their pension funds savings to pay bondholders. Balancing their budgets by privatizing hitherto public services will create monopoly rents and new corporate empires

These outcomes are not necessary. They also are inequitable, and instead of being a survival of the fittest and most efficient economic solutions, they are a victory for the most successfully predatory. Yet such results are the product of a long-pedigreed legal and financial philosophy promoted by banks and bondholders, landlords and insurance companies reject economy-wide debt relief. They depict writing down debts and rents owed to them as unthinkable. Banks claim that forgiving personal and business rents would lead absentee landlords to default on their mortgages, threatening bank solvency. Insurance companies claim that to make their policy holders whole would bankrupt them.[
                        3
                ]So something has to give: either the population’s broad economic interests, or the vested interests insisting that labor, industry and the government must bear the cost of arrears that have built up during the economic shutdown.

As in oligarchic Rome, financial interests in today’s world have gained control of governments and captured the political and regulatory agencies, leaving democratic reformers powerless to suspend debt service, rent arrears, evictions and depression. The West is becoming a highly centrally planned economy, but its planning center is Wall Street, not Washington or state and local governments.

Rising Real Estate Arrears

Canada and many European governments are subsidizing businesses to pay up to 80 percent of employee wages even though many must stay home. But for the 40 million Americans who haven’t been employed during the closedown, the prospect is for homelessness and desperation. Already before the crisis about half of Americans reported that they were living paycheck to paycheck and could not raise $400 in an emergency. When the paychecks stopped, rents could not be paid, nor could other normal monthly living expenses.

America is seeing the end of the home ownership boom that endowed its middle class with property steadily rising in price. For buyers, the price was rising mortgage debt, as bank credit was the major factor in raising property prices. (A home is worth however much a bank will lend against it.) For non-whites, to be sure, neighborhoods were redlined against racial minorities. By the early 2000s, banks began to make loans to black and Hispanic buyers, but usually at extortionately high interest rates and stiffer debt terms. America’s white home buyers now face a fate similar to that which they have long imposed on minorities: Debt-inflated purchase prices for homes so high that they leave buyers strapped by mortgage and compulsory insurance payments, with declining public services in their neighborhoods.

When mortgages can’t be paid, foreclosures follow. That causes declines in the proportion of Americans that own their own homes. That home ownership rate already had dropped from about 58 percent in 2008 to about 51 percent at the start of 2020. Since the 2008 mortgage-fraud crisis and President Obama’s mass foreclosure program that hit minorities and low-income buyers especially hard, a more landlord-ridden economy has emerged as a result of foreclosed properties and companies bought by speculators and vast absentee-owner companies like Blackstone.

Many businesses that closed down did not pay the landlords. Realizing that if they are held responsible for paying full rents that accrued during the shutdown, it would take them over a year to make up the payment, leaving no net earnings for their efforts. That was especially the case for restaurants with compulsory limited “distance” seating and other stores obliged to restrict the density of their customers. Many restaurants and other neighborhood stores decided to go out of business. For hotels standing largely empty, some 19 percent of mortgage loans had fallen into arrears already by May, along with about 10 percent of retail stores.[
                        4
                ]

The commercial real estate sector owes $2.4 trillion in mortgage debt. About 40 percent of tenants did not pay their rents for March, April and May, from restaurants and storefronts to large national retail markets. A moratorium on evictions put them off until August or September 2020. But in the interim, quarterly state and local property taxes were due in June, which also was when the annual federal income-tax payment was owed for the year 2019, having been postponed from April in the face of the shutdown.

The prospective  break in the chain of payments of landlords to their banks may be bailed out by the Federal Reserve, but nobody can come up with a scenario whereby the debts owed by non-elites can be paid out of their own resources, any more than they were rescued from the junk-mortgage frauds that left over-mortgaged homes (mainly for low-income victims) in the wake of Obama’s decision to support the banks and mortgage brokers instead of their victims. In fact, it takes a radical scenario to see how state and local debt can be paid as public budgets are thrown into limbo by the virus pandemic.

The Fiscal Squeeze Forces Governments to Privatize Public Services and Assets

Since 1945, the normal Keynesian response to an economic slowdown has been for governments to run budget deficits to revive the economy and employment. But that can’t happen in the wake of the 2020 pandemic. For one thing, tax revenue is falling. Governments can create domestic money, of course, but the U.S. government quickly ran up a $2 trillion deficit by June 2020 simply to support Wall Street’s financial and corporate markets, leaving a fiscal squeeze when it came to public spending into the real economy. Many U.S. states and cities have laws obliging them to balance their budgets. So public spending into the real economy (instead of just into the financial and corporate markets) had to be cut back.

Sales taxes from restaurants and hotels, income taxes, and property taxes from landlords not receiving rents. U.S. states and localities are having a huge tax shortfall that is forcing them to cut back basic social services and infrastructure. New York City mayor de Blasio has warned that schools, the police and public transportation may have to be cut back unless the city is given $7 billion. The CARES act passed by the Democratic Party in control of the House of Representatives made no attempt to allocate a single dollar to make up the widening fiscal gap. As for the Trump administration, it was unwilling to give money to states voting Democratic in the presidential or governorship elections.

The irony is that just at the time when a pandemic calls for public health care, political pressure for that abruptly stopped. Logically, it might have been expected the virus to have become a major catalyst for single-payer public health care, not least to prevent a wave of personal bankruptcy resulting from high medical bills. But hopes were dashed when the leading torch bearer for socialized medicine, Senator Bernie Sanders, threw his support behind Joe Biden and other opponents for the presidential nomination instead of focusing the primary elections on what the future of the Democratic Party would be. It decided to focus the 2020 U.S. election merely on the personality of which candidate would impose neoliberal policy: Republican Donald Trump, or his opponent running simply on a platform of “I am not Trump.”

Both candidates – and indeed, both parties behind them –sought to downsize government and privatize as much of the public sector as possible, leaving administration to financial managers. Past government policy would have restored prosperity by public spending programs to to rebuild the roads and bridges, trains and subways that have fallen apart. But the fiscal squeeze caused by the economic shutdown has created pressure to Thatcherize America’s crumbling transportation and urban infrastructure – and also to sell off land and public enterprises, basic urban health, schools – and at the national level, the post office. Fiscal budgets are to be balanced by selling off this infrastructure, in lucrative Public-Private Partnerships (PPPs) with financial firms.

The neoliberal rent-extractive plan is for private capital to buy monopoly rights to repair the nation’s bridges by turning them into toll bridges, to repair the nation’s roads and highways by making the toll roads, to repair sewer systems by privatizing them. Schools, prisons, hospitals and other traditionally public functions. Even the police are to be privately owned security-guard agencies and managed for profit – on terms that will provide interest and capital gains for the financial sector. It is a New Enclosures movement seeking monopoly rent much as landlords extract land rent.

Having given $10 trillion dollars to support financial and mortgage markets, neoliberals in both the Republican and Democratic parties announced that the government had created so large a budget deficit as a result of bailing out the banking and landlord class that it lacked any more room for money creation for actual social spending programs. Republican Senate leader Mitch McConnell advised states to solve their budget squeeze by raiding their pension funds to pay their bondholders.

For many decades, public employees accepted low wage growth in exchange for pensions. Their patient choice was to defer demands for wage increases in order to secure good pensions for their retirement. But now that they have worked at stagnant wages for many years, the money ostensibly saved for their pensions is to be given to bondholders. Likewise at the federal level, pressure was renewed by both parties to cut back Social Security, Medicare and Medicaid, with Obama’s 2010 Simpson-Bowles Commission on Fiscal Responsibility and Reform to reduce the deficit at the expense of retirees and the poor.

In sum, money is being created to fuel the financial sector and its stock and bond markets, not to increase the economy’s solvency, employment and living standards. The coronavirus pandemic did not create this shift, but it catalyzed and accelerated the power grab, not least by pushing public-sector budgets into crisis.

It Doesn’t Have To Be This Way

Every successful economy has been a mixed public/private economy with checks on the financial sector’s power to indebt society in ways that impoverish it. Always at issue, however, is who will control the government. As American and European industry becomes more debt ridden, will they be oligarchic or democratic?

A socialist government such as China’s can keep its industry going simply by simply writing down debts when they can’t be paid without forcing a closedown and bankruptcy and loss of assets and employment. The world thus has two options: a basically productive public financial system in China, or a predatory financial system in the United States.

China can recover financially and fiscally from the virus disruption because most debts ultimately are owned to the government-based banking system. Money can be created to finance the material economy, labor and industry, construction and agriculture. When a company is unable to pay its bills and rent, the government doesn’t stand by and let it be closed down and sold at a distressed price to a vulture investor.

China has an option that Western economies do not: It is in a position to do what Hammurabi and other ancient Near Eastern palatial economies did for thousands of years: write down debts so as to keep the economy resilient and functioning. It can suspend scheduled debt service, taxes, rents and public fees from having to be paid by troubled areas of its economy, because China’s government is the ultimate creditor. It need not contend with politically powerful bankers who insist that the economy at large must lose, not themselves. The government can write down the debt to keep companies in business, and also their employees. That’s what socialist governments do.

The underlying problem is finance capitalism. Its roots lie at the heart of Western civilization itself, rejecting the “circular time” permitting economic renewal by Clean Slates in favor of “linear time” in which debts are permanent and irreversible, without public oversight to manage finance and credit in the economy’s overall long-term interest.

It often is easier to get rich in such times of disaster and need than in times of normal prosperity. While the U.S. economy polarizes between creditors and debtors, the stock market anticipates fortunes being made quickly from the insolvency of business with assets and property to be grabbed. Coupled with the Federal Reserve’s credit creation to support the financial and real estate markets, asset prices are soaring (as of June 2020) for companies that expect to get even richer from the widespread distress to come in autumn 2020 when evictions and foreclosures ae scheduled to begin again.

In that respect, the coronavirus’ effect has been to help defeat the financial sector’s enemy, governments strong enough to regulate it. The fiscal squeeze resulting from widespread unemployment, business closedowns, rent and tax arrears is being seized upon as a means of dismantling and privatizing government at the federal, state and local levels, at the expense of the citizenry at large.''',


"32":'''Don’t “Trust the Science,” Trust Science While You Hone Your Critical Thinking Skills
Posted on August 31,
                2020 by Lambert Strether
By Lambert Strether

I have a quarrel with the phrase “trust the science” (and in so quarreling, I don’t mean to reinforce culture war-ish talking points; I straight up disagree with the plain meaning of the words, for reasons I am about to explain). Here is a typical usage example, from the Tallahassee Democrat:

The kids join the drumbeat of public sentiment of frustration with leaders that continue to stall instead of addressing the climate crisis. After years of feeling like climate science and environmental warnings were falling on deaf ears,
                2019 feels different. Perhaps 2018 served as a wake-up call and Americans are finally ready to connect the dots and trust the science.

(Because who but a yahoo wouldn’t “trust the science”? We’ll get to Thomas Frank below.) Here is an example of signage:



Here’s a headline; here’s ironic mockery; search turns up numerous examples and variations (“believe science“). Here’s Joe Biden:

I would listen to the scientists.

(“-ists” will become important later.) A Republican spokesperson:

We have never ignored the science in making the very tough policy decisions required of the agency

I believe Greta Thunberg was Patient Zero. Time:

When Greta Thunberg, the youthful climate activist, testified in Congress last month, submitting as her testimony the IPCC 1.5° report, she was asked by one member why should we trust the science. She replied, incredulously, “because it’s science!”

So many people vehemently disagreeing with each other, all the while trusting science; and so many people not trusting science at all. Perhaps “trust the science” is not all that meaningful? My concern, as I said, is with the plain meaning of the phrase: There is no “the science” (with definite article) because because progress in science is based on conflict, and you have to pick a side (and there may be more than two). Similarly with “the scientists,” as Biden would have it. Which ones?

So how is science done, and how is progress in science achieved? I may be showing my age here, but I believe that Thomas Kuhn, in the Structure of Scientific Revolutions, gave a very good account. Excerpting from Kuhn’s entry in The Stanford Encyclopedia of Philosophy:

In The Structure of Scientific Revolutions Kuhn paints a picture of the development of science quite unlike any that had gone before … [Kuhn
                ] claims that normal science can succeed in making progress only if there is a strong commitment by the relevant scientific community to their shared theoretical beliefs, values, instruments and techniques, and even metaphysics. This constellation of shared commitments Kuhn at one point calls a ‘disciplinary matrix’ (1970a,
                182) although elsewhere he often uses the term ‘paradigm’. Because commitment to the disciplinary matrix is a pre-requisite for successful normal science, an inculcation of that commitment is a key element in scientific training and in the formation of the mind-set of a successful scientist. … A mature science, according to Kuhn, experiences alternating phases of normal science and revolutions. In normal science the key theories, instruments, values and metaphysical assumptions that comprise the disciplinary matrix are kept fixed, permitting the cumulative generation of puzzle-solutions….

Here is an example of “normal science,” from Quebec’s The Suburban, “Trust the science on COVID-19, but much is still not known,” from chemist Dr. Joe Schwarcz, Director of the McGill Office for Science and Society:

In the long run, we have to trust the science, but unfortunately, science does not progress by giant leaps and bounds — only the quacks can do that. Science progresses by a series of small, careful steps, but eventually it will put us on the right track.

Back to Kuhn:

….whereas in a scientific revolution the disciplinary matrix undergoes revision, in order to permit the solution of the more serious anomalous puzzles that disturbed the preceding period of normal science. A particularly important part of Kuhn’s thesis in The Structure of Scientific Revolutions focuses upon one specific component of the disciplinary matrix. This is the consensus on exemplary instances of scientific research. These exemplars of good science are what Kuhn refers to when he uses the term ‘paradigm’in a narrower sense. He cites Aristotle’s analysis of motion, Ptolemy’s computations of plantery positions, Lavoisier’s application of the balance, and Maxwell’s mathematization of the electromagnetic field as paradigms (1962/1970a,
                23). Exemplary instances of science are typically to be found in books and papers, and so Kuhn often also describes great texts as paradigms—Ptolemy’s Almagest, Lavoisier’s Traité élémentaire de chimie, and Newton’s Principia Mathematica and Opticks (1962/1970a,
                12). Such texts contain not only the key theories and laws, but also—and this is what makes them paradigms—the applications of those theories in the solution of important problems

(For awhile, one was seeing “paradigm shift” in every book in every airport bookstore business section, when we were going to airports; what most of these books didn’t understand was that a paradigm applies across a discipline, and not simply within a firm. Nor is it possible to induce a paradigm shift simply by proclaiming it, sadly for motivational speakers.)

Interestingly, we’re seeing an example of such a paradigm shift, and the resistance to it, in the COVID-19 crisis, in the droplet vs. aerosol transmission controversy. Vox explains: [In a 1932 paper, William Wells
                ] outlined a clear distinction between droplets and aerosols according to their size. Big drops fall, and little aerosolized drops float.

That is the paradigm. Here comes the paradigm shift:

It’s now appreciated that the actual picture is a lot more complicated.

“We’re always exhaling, in fact, a gas cloud that contains within it a continuum spectrum of droplet sizes,” says Lydia Bourouiba, an MIT researcher who studies the fluid dynamics of infections. And, as she explained in a March paper in JAMA, the conditions of the cloud itself can affect the range of some of the droplets. If propelled by a cough or sneeze, Bourouiba finds, droplets can travel upward of 20 feet. “The cloud mixture, not the drop sizes, determines the initial range of the drops and their fate in indoor environments.”….

There’s growing theoretical evidence for the airborne spread of the coronavirus. Lab studies, in idealized conditions, also show that the virus can live in an aerosolized form for up to 16 hours (the scientists in this case intentionally created aerosolized droplets with a machine).

Multiple studies have found evidence of the virus’s RNA in the air of hospital rooms. But the WHO notes “no studies have found viable virus in air samples,” [no longer true
                ] meaning the virus was either incapable of infecting others [no longer true
                ] or was in very small quantities unlikely to infect others.

“What we are trying to say is, well, let’s not worry about whether you call it aerosol or whether you call it a droplet,” Morawska, the co-author of the recent commentary imploring….

“Imploring” because “the key theories, instruments, values and metaphysical assumptions that comprise the disciplinary matrix are kept fixed.”

… the WHO and others to address airborne transmission of Covid-19, says. “It is in the air,” she says, “and you inhale it. It’s coming from our nose from our mouths. It’s lingering in the air and others can inhale it.”

That the WHO updated its language is a sign that it’s starting to appreciate [“kept fixed”
                ] this perspective. (That said: The WHO still defines [“kept fixed”
                ] a droplet as a particle larger than than 5-to-10 microns, and an aerosol as something smaller, despite many scientists arguing the cutoff is meaningless.)

So, when we say “trust the science” in this context, what can we mean? Which paradigm — “a science” — do we select? (I exercised what I consider to be my critical thinking skills, and went with the aerosol transmission paradigm, and adjusted my personal practice accordingly.[
                        1
                ])

A second difficulty with “trust the science” is that it shifts over very easily to “trust the scientists” (as it did with Biden) and then, in our partisan era, to “trust this scientist.” For example:


Another example:


A final example:


This last example, of “Fauci” screen-printed onto masks, is especially ironic. As I wrote back in June:

About masks:


Lambert here: To my shame, I bought into — and worse, propagated, told readers and friends — the original LIE propagated by Fauci and WHO, that masks were not necessary. Fortunately, I continued to do my homework and watch the news flow, and changed my mind (and my practice). Fauci and WHO perpetrated what Plato called a “noble lie,” [UPDATE See also contemporary philosopher Leo Strauss
                ] believing that the best way to make sure that medical personnel — and they, too, personally — had masks was to make sure the public they duped didn’t buy them up, and so they used their authority to lie about whether masks worked (they do). In an election season where the liberal Democrat pitch seems to be “Let The Professionals Take Charge Again”™, having top PMC and global agencies get caught out in a Noble Lie might not have been the greatest idea. And as we few, we happy few in the Blue States make fun of the fat stupid loud people in the Red States who don’t trust the experts that lied to them, we might consider whether our Noble Lies have unexpected effects, not merely politically, but in the destruction of the very concept of public health. Sorry about that.

Sometimes, critical thinking can be painful. But, sadly, there’s no particular reason to lend one’s trust to scientists while surrendering it. Thomas Frank writes:

These days, right-thinking Americans are tearfully declaring their eternal and unswerving faith in science. Democratic leaders are urging our disease-stricken country to heed the findings of medical experts as though they were the word of God….

Unfortunately, it’s all a mistake. Donald Trump’s prodigious stupidity is not the sole cause of our crushing national failure to beat the coronavirus. Plenty of blame must also go to our screwed-up healthcare system, which scorns the very idea of public health and treats access to medical care as a private luxury that is rightfully available only to some. It is the healthcare system, not Trump, that routinely denies people treatment if they lack insurance; that bankrupts people for ordinary therapies; that strips people of their coverage when they lose their jobs — and millions of people are losing their jobs in this pandemic. It is the healthcare system that, when a Covid treatment finally arrives, will almost certainly charge Americans a hefty price to receive it (3).

And that system is the way it is because organised medicine has for almost a century used the prestige of expertise to keep it that way.

Bowing down before expertise is precisely what has made public health an impossible dream.

Is there a way to respectfully leverage the expertise of scientists — some of whom are truly in it “for the love of the game,” let us not forget that — without bowing down? I would, again, urge that critical thinking skills are the anwer.

Sadly, we as a society and policy do not seem to inculcate critical thinking skills very well. How to do better? I would like to see, well, a paradigm shift from “Trust the science” to “Do the science,” because I think that is an operational capacity that an informed citizenry should have. (We see this all the time when ordinary working people become subject matter experts to fight pipelines or landfills, or save lakes, or become involved in long legal battles with corporations that have poisoned them and their environs). We should encourage this capacity. One easy way would be to remove all paywalls from scientific publications, and have the Federal Government pay the rapacious publishers a reasonable sum. Those same publishers should include, besides Abstracts, a “Plain Langauge Summary” in their editorial designs. We should also fund a great deal more citizen science, ideally under the aegis of a Jobs Guarantee. With climate change barreling down upon us, there are innumerable observational studies that should be performed.

NOTES

[
                        1
                ] There is also a paper which I could not retrieve, which argues in summary that hospital personnel are triggered by the word “airborne,” because to them it means a germ that’s wildly contagious, like measles or worse (which COVID is not), and they have to take a lot of measures accordingly, like moon suits or whatever. This is another example of a disciplinary matrix or paradigm.''',



"33":'''Global Warming Is Accelerating. (In Other News, Democrats Reverse Platform, Won’t End Fossil Fuel Subsidies)
Posted on August 21,
                2020 by Yves Smith
Yves here. As  global warming keeps passing all sorts of tipping points, the Democrats refuse to make even minimal steps to Do Something.

By Thomas Neuburger. Originally published at DownWithTyranny!



The three colors in the chart represent odds that a season will be perceived as cool (blue), normal (white) or hot (red). In 1950 to 1980, if represented on a six-sided dice, there were two blue sides, two red sides and two white sides. “The dice are now loaded, really loaded. … Four sides of the die are now red (hot) and one side is deep red for extreme heat, more than three standard deviations warmer than in 1951-1980. Dark red (22%) is creeping onto another side” (James Hansen et. al.)
As we contemplate the political events of the week — the Republican takeover of the Democratic Party and convention; Democratic media adjunct MSNBC lying about AOC’s Party-approved nomination of Bernie Sanders (before changing their headline); Bill Clinton daring to show his face in public, and post-MeToo leadership letting him — it’s nevertheless impossible not to be overwhelmed by this.

 • “Good morning. The Greenland ice sheet has past the melting point of no return“

“[I
                ]ce that’s discharging into the ocean is far surpassing the snow that’s accumulating on the surface of the ice sheet” — Michalea King, lead author of the study and a researcher at The Ohio State University’s Byrd Polar and Climate Research Center.

“[S
                ]tarting in 2000, you start superimposing that seasonal melt on a higher baseline—so you’re going to get even more losses,” meaning the melt-rate has permanently accelerated while the snowfall has not.

But there’s a bright side: “It’s always a positive thing to learn more about glacier environments, because we can only improve our predictions for how rapidly things will change in the future … The more we know, the better we can prepare.”

We’re learning how to learn sooner how wrong we are, “so we can better prepare.” That’s the bright side.

• “Record Arctic blazes may herald new ‘fire regime’ decades sooner than anticipated”

“Something’s changed in the environment there” — Mark Parrington, senior scientist and wildfire expert at the EU’s Copernicus Atmosphere Monitoring Service.

“This is the type of fire event that would be described by these worst-case modeling scenarios that were supposed to occur mid-century” — Jessica McCarty, a wildfire expert at Miami University of Ohio.

Mid-century (2050) Arctic fires now occur regularly.

• “Global warming is accelerating. 12-month mean peaked just below prior maximum”

“[G
                ]lobal temperature is clearly running well above the linear trend that existed for decades” — climate scientist James Hansen


“1) That jump off the linear trend ought to scare the crap out of you. 2) Who but the careful public managers of your emotions say that being batcrap-scared is a useless response to the climate?” — Yours truly

Nonetheless, not everyone is scared.

• “Democrats Drop Demand To End Fossil Fuel Subsidies From Party Platform”

“Roughly half of all U.S. oil reserves required subsidies to generate a profit, according to a study published in the journal Nature Energy in 2017, and that was before the price of crude plunged far below $50 a barrel.” — Huffington Post writer Alexander Kaufman.

“This platform is a step backwards” — Charlie Jiang, Greenpeace.

• “DNC’s Flip-Flop on Fossil Fuel Subsidies Follows Deep Ties the Industry”

“In August 2018, the DNC approved a resolution from Chair Tom Perez that reversed a DNC policy prohibiting it from accepting contributions from fossil fuel PACs. … Shortly thereafter, donations from fossil fuel executives began flowing into DNC coffers.” — Donald Shaw, money-in-politics editor and co-founder, Sludge

• “A-a-and we’re done…” — Yours truly

If the question is climate, who with any power is the answer? Certainly not Joe Biden.

The real answer, of course, is the people, but only if they know it.'''
        },
        "target": {
                "0": "Lester data science",
                "1": "Lester data science",
                "2": "Lester data science",
                "3": "Lester data science",
                "4": "Lester data science",
                "5": "Lester self help",
                "6": "Lester history/society",
                "7": "Lester data science",
                "8": "Lester data science",
                "9": "Lester science",
                "10": "Lester economics",
                "11": "Lester politics",
                "12": "Lester politics/economics",
                "13": "Lester finance/economics",
                "14": "Lester history/space",
                "15": "Lester data science",
                "16": "Lester finance",
                "17": "Lester economics/politics",
                "18": "Lester history/politics",
                "19": "Lester finance/economics",
                "20": "Lester economics/climate change",
                "21": "Lester finance/economics",
                "22": "Lester finance/economics",
                "23": "Lester finance/economics",
                "24": "Lester finance/economics",
                "25": "Lester finance/economics",
                "26": "Lester finance/economics",
                "27": "Lester finance/economics",
                "28": "Lester finance/economics",
                "29": "Lester finance/economics",
                "30": "Lester finance/economics",
                "31": "Lester finance/economics",
                "32": "Lester politics/science",
                "33": "Lester politics/climate change"
        },
        "url": {
                "0": "https://medium.com/@jayshah_84248/deepsign-a-deep-learning-pipeline-for-sign-language-recognition-a51a8f116dfc?source=bookmarks---------0------------------",
                "1": "https://towardsdatascience.com/boost-your-cnn-image-classifier-performance-with-progressive-resizing-in-keras-a7d96da06e20?source=bookmarks---------1------------------",
                "2": "https://towardsdatascience.com/5-professional-projects-every-data-scientist-should-know-e89bf4e7e8e1?source=bookmarks---------3------------------",
                "3": "https://towardsdatascience.com/analytics-is-not-storytelling-a1fe61b1ab6c?source=bookmarks---------6------------------",
                "4": "https://medium.com/the-ascent/9-skills-you-can-get-from-extraordinary-learners-8839d7f253eb?source=bookmarks---------7------------------",
                "5": "https://medium.com/@chrisrackliffe/13-books-that-changed-my-life-a657e4c9efd4?source=bookmarks---------9------------------",
                "6": "https://medium.com/@djonesvi/the-mutually-exclusive-society-e2ac82863926?source=bookmarks---------10------------------",
                "7": "https://towardsdatascience.com/introduction-to-decision-intelligence-5d147ddab767?source=bookmarks---------13------------------",
                "8": "https://medium.com/@jasoncbenn/everything-you-need-to-become-a-self-taught-machine-learning-engineer-d09bbcdfa631?source=bookmarks---------24------------------",
                "9": "https://elemental.medium.com/a-supercomputer-analyzed-covid-19-and-an-interesting-new-theory-has-emerged-31cb8eba9d63?source=topic_page---------------------------20",
                "10": "https://marker.medium.com/remote-work-is-killing-the-hidden-trillion-dollar-office-economy-5800af06b007?source=topic_page---------7------------------1",
                "11": "https://eand.co/we-dont-know-how-to-warn-you-any-harder-america-is-dying-26ff80912391?source=topic_page---------15------------------1",
                "12": "https://onezero.medium.com/how-to-destroy-surveillance-capitalism-8135e6744d59?source=topic_page---------17------------------1",
                "13": "https://medium.com/the-ascent/warren-buffetts-recent-explanation-of-how-money-now-works-is-the-most-important-in-history-2e45461a5969?source=topic_page---------20------------------1",
                "14": "https://medium.com/history-of-yesterday/the-only-humans-to-die-in-space-2d7dc49ba6e5?source=topic_page---------22------------------1",
                "15": "https://towardsdatascience.com/amazon-wants-to-make-you-an-ml-practitioner-for-free-552c46cea9ba?source=topic_page---------38------------------1",
                "16": "https://medium.com/refinery29/10-bizarre-money-habits-making-millennials-richer-f699c95f01cb?source=topic_page---------58------------------1",
                "17": "https://level.medium.com/the-third-crisis-of-2020-is-almost-here-d9cff8720fc5?source=topic_page---------94------------------1",
                "18": "https://gen.medium.com/the-future-alexander-hamilton-warned-about-has-arrived-d1e0e48a8a72?source=topic_page---------116------------------1",
                "19": "https://medium.com/concoda/when-the-u-s-dollar-collapses-the-elites-will-try-to-steal-your-money-8e41a42f684c?source=topic_page---------122------------------1",
                "20": "https://onezero.medium.com/why-2020-to-2050-will-be-the-most-transformative-decades-in-human-history-ba282dcd83c7?source=topic_page---------136------------------1",
                "21": "https://www.oftwominds.com/blogsept20/four-Ds9-20.html",
                "22": "https://www.oftwominds.com/blogsept20/austerity-inflation9-20.html",
                "23": "https://www.oftwominds.com/blogaug20/trends-accelerating8-20.html",
                "24": "https://www.oftwominds.com/blogaug20/disunity8-20.html",
                "25": "https://www.oftwominds.com/blogmay20/system-collapse5-20.html",
                "26": "https://www.oftwominds.com/blogmay20/fragility5-20.html",
                "27": "https://www.oftwominds.com/blogmay20/assets-crash5-20.html",
                "28": "https://www.oftwominds.com/blogapr20/globalization-insanity4-20.html",
                "29": "https://www.nakedcapitalism.com/2020/09/climate-crisis-and-population-growth-will-displace-1-billion-over-next-30-years.html",
                "30": "https://www.nakedcapitalism.com/2020/09/how-us-consumers-use-their-stimulus-payments.html",
                "31": "https://www.nakedcapitalism.com/2020/09/michael-hudson-how-an-act-of-god-pandemic-is-destroying-the-west-the-u-s-is-saving-the-financial-sector-not-the-economy.html",
                "32": "https://www.nakedcapitalism.com/2020/08/dont-trust-the-science-trust-science-while-you-hone-your-critical-thinking-skills.html",
                "33": "https://www.nakedcapitalism.com/2020/08/global-warming-is-accelerating-in-other-news-democrats-reverse-platform-wont-end-fossil-fuel-subsidies.html"
        }
}

import pandas as pd 
df = pd.DataFrame.from_dict(dictionary)
df.head()