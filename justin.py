dictionary = { 'content': {
                '0': '''One key observation that helped launch the field of behavioral economics into stardom is called probability weighting: a human cognitive bias to assign higher probabilities to extreme events than … well, than what? Than what someone else thinks the probabilities should be. Below, I will present a very simple mechanistic explanation, most of all for the iconic probability weighting figure in (Tversky and Kahneman, 1992). The result is a now familiar theme: (behavioral) economics expresses a more or less robust observation in psychological terms, as a persistent cognitive error. Ergodicity economics explains the same observation mechanistically, and as perfectly rational behavior.


1 Definitions and key observation
I won’t go into how probability weighting is established empirically. Instead, I’ll jump into its definition and then mention some caveats.

Probability weighting: People tend to treat extreme events as though they had higher probabilities than they actually do, and (necessarily because of normalization) common events as if they had lower probabilities than they actually do.

Before going any further: what probabilities are, and even whether they have any actual physical meaning at all, is disputed. They are certainly not directly observable, we can’t touch, taste, smell, see, or hear them. Maybe it’s uncontroversial to say they are parameters in models of ignorance. Consequently, when we make statements about weighting, or misperceiving, probabilities we will always be on shaky ground.

To keep the discussion as concrete as possible, let’s use a specific notion of probability.

Temporal frequentist probability: The probability of an event is the relative amount of time in which the event occurs, in a long time series.

For example, we could say “the probability of a traffic light being green is 40%.” Of course we don’t have to describe traffic lights probabilistically if we know or control their algorithms. But you can imagine situations where we have no such knowledge or control. If we were to say “the probability of rain falling somewhere in London between 3pm and 4pm on a given day in May is 10%” — we would mean that we’d looked at a long time series of days in Mays from the past and found that in 10% of the periods from 3pm to 4pm it had rained somewhere in London.

I’ve said what I mean by probability weighting, and what I mean by probability. Two more bits of nomenclature.

 I will refer to an experimenter, or scientist, or observer, as a Disinterested Observer (DO); and to a test subject, or observed person as a Decision Maker (DM). The DO is not directly affected by the DM’s decisions, but the DM is, of course.
I will refer to the probability the DO uses (and possibly controls) in his model by the word “probability,” expressed as a probability density function (PDF), p(x); and to the probabilities that best describe the DM’s decisions by the term “decision weights,” expressed as a PDF, w(x).
 

Probability weighting, neatly summarized by Barberis (2013) can be expressed as a mapping of probabilities p into decision weights w, a simple function w(p). We could look at these functions directly, but in the literature it’s more common to look at cumulative density functions (CDFs) instead. So we’ll look at the CDF for p(x), which is F_p(x)=\int_{-\infty}^{x} p(s) ds and the CDF for w(x), which is F_w(x)=\int_{-\infty}^{x} w(s) ds.

Fig. 1 is copied from Tversky and Kahneman (1992): an inverse-S curve describes the mapping between the cumulatives.

TK1992
Fig.1 copied from Tversky and Kahneman (1992). A graphical summary of many studies in behavioral economics showing typically observed cumulative decision weights versus cumulative probabilities. Tversky and Kahneman chose the smooth function because it resembles the data. It is not derived from a mechanistic model. Large uncertainties (notice the absence of error bars) clearly exist. However, qualitatively, it is generally believed that the inverse-S shape is reasonably robust. The asymmetry of the S is to an extent artificial: the function the authors chose to fit always, by mathematical necessity, becomes asymmetric when it deviates from a straight line.
2 Mechanistic models that generate these observations
Let’s list some mechanistic models that predict this behavior. The key common feature is that the DM’s model will have extra uncertainty, beyond what the DO accounts for in his model. Behavioral economics assumes that the DO knows “the truth,” and the DM is cognitively biased and cannot see this truth. We will be agnostic: the DO and DM have different models. Whether one, both, or neither is “correct” is irrelevant for explaining the observation in Fig.1 We’re just looking for good reasons for the difference.

2.1 DM estimates probabilities
How can a DM know the probability of anything? In the real world, the only way to find the probability as we have defined it — relative frequency in time — is to look at time series and count: how often was the traffic light green? How often did it rain between 3pm and 4pm in London in May etc.

The result is a count: in n=68 out of N=680 observations the event occurred. The best estimate for the probability of the event is then 68/680=10\%. But we know a little more than that: counts of events are usually modeled as Poisson processes — it’s the null model that assumes no correlation between events, a common baseline. In this null model, the uncertainty in a count goes as \sqrt{n}.

A DO faced with these statistics is quite likely to put into his model the most likely value, 10\%. A DM, on the other hand, is likely to take into account the uncertainty in the count in a conservative way. It’s not good to be caught off guard, so let’s assume the DM adds to all probabilities one standard error, so that

Eq. 1 w(x)=\frac{1}{c}\left[p(x)+\sqrt{p(x)}\right],

where c ensures normalization, c=\int_{-\infty}^{+\infty} \left[ p(x) + \sqrt{p(x)}\right] dx.

From here it’s just handle-cranking.

specify the DO’s model, p(x)
specify the DM’s model, w(x)
integrate to find F_p(x) and F_w(x)
plot F_w vs. F_p
Fig.2 shows what happens for a Gaussian distribution and for a fat-tailed Student-t.

Gauss_Student_Poisson_error
Fig.2 A DM estimates probabilities from frequencies in a time series in the simplest (Poissonian) way and conservatively uses probabilities one standard error greater than the most likely value, Eq.1. A DO, on the other hand, uses most likely probabilities. This results in an inverse-S-shape map between cumulative probabilities and cumulative decision weights. Blue: standard Gaussian. Green: fat-tailed Student-t with shape parameter 2.5.
Generally, probability weighting is a mismatch between the models of the DO and the DM. The canonical inverse-S shape represents the precautionary principle: it’s best for the DM to err on the side of caution, whereas the DO will often use most likely probabilities.

2.2 DO confuses ensemble-average and time-average growth
Incidentally, neglecting the detrimental effects of fluctuations (i.e. neglecting the precautionary principle) is one direct consequence of the ergodicity problem in economics: a DO who models people as expectation-value optimizers rather than time-average growth optimizers will find the same type of “probability weighting,” which should really just be seen as an empirical falsification of the DO’s model. The prevalence of these curves could therefore be interpreted as evidence for the importance of adopting ergodicity economics. See also this blog post by Ihor Kendiukhov.

2.3 DM assumes a broader range of outcomes
Recognizing probability weighting as a simple mismatch between the model of the DO and the model of the DM predicts all sorts of probability weighting curves. Now we know what they mean, we can make predictions and test them. Fig.3 is the result of the DO using a Gaussian distribution, and the DM also using a Gaussian distribution, but one with a higher mean and a higher variance. It looks strikingly similar to the observations of Tverskey and Kahneman (1992).

The inverse-S shape arises whenever a DM (cautiously) assumes a larger range of plausible outcomes than the DO. This happens whenever the DM has additional sources of uncertainty — did he understand the experiment? Does he trust the DO? Taleb (2019) calls the assumption by the DO that the DM will use probabilities as specified in an experiment the “ludic fallacy:” what may seem sensible to the designer of a game-like experiment may seem less so to a test subject.

 

Gauss_scale_location_both_KT
Fig.3 Probability weighting curves for a Gaussian distribution. It is assumed that the DM uses a larger mean (location) in his model (top left); a larger standard deviation (scale, top right), and a larger mean and standard deviation (location and scale, bottom left); for comparison the curve estimated by Tversky and Kahneman (1992) (bottom right). Tversky and Kahneman’s estimated relationship is indistinguishable from a DM using different estimates for location and scale of a Gaussian distribution. The reader is encouraged to try out other distributions — the inverse-S result is robust for unimodal distribtions.
3 Conclusion
Ergodicity economics carefully considers the situation of the DM as living along a time line. Probability weighting then appears not as a cognitive bias but as an aspect of sensible behavior across time. Unlike the vague postulate of a bias, it can make specific predictions: it’s often sensible for the DM to assume a larger variance than the DO, but not always. Also, a DO may be aware of the true situation of the DM, and both may use the same model, in which case there won’t be a systematic effect. In other words, the ergodicity-economics conceptualization adds clarity to ongoing research.

Ergodicity economics urges us to consider how real actors have to operate within time, not across an ensemble where probabilities make no reference to time. The precautionary principle is one consequence (because fluctuations are harmful over time); having to estimate probabilities from time series is another. Assuming a perfectly informed, perfectly rational DM, ergodicity economics predicts the observations that in behavioral economics are usually presented as a misperception of the world. Ergodicity economics thus suggests once again that economics jumps to psychological explanations too soon and without need.

What are we to make of probability weighting, then? Just like in the case of utility, I don’t recommend using the concept at all. “Probability weighting” is an extremely complicated way of expressing a rule known by all living things. A bit of surfing wisdom: if in doubt, don’t go out.

 

p.s. Alex Adamou, Mark Kirstein, Yonatan Berman and I are in the process of writing this up, which you can follow live with the latest PDF and the python code to generate the figures online. ''',

                '1': '''Book Recommendations from Nassim Taleb
READING TIME: 39 MINUTES
(Jan 2017) Perilous Interventions: The Security Council and the Politics of Chaos

Solid Book on Interventionism, Should be Mandatory Reading in Foreign Affairs. This is an outstanding book on the side effects of interventionism, written in extremely elegant prose and with maximal clarity. It documents how people find arguments couched in moralistic terms to intervene in complex systems they don’t understand. These interventions trigger endless chains of unintended consequences –consequences for the victims, but none for the interventionistas, allowing them to repeat the mistake again and again. Puri, as an insider, outlines the principles and legal mechanisms, then runs through the events of the past few years since the Iraq invasion; each one of his chapters are models of concision, presenting the story of Ukraine, Syria, Lybia, and Yemen, among others, as standalone briefings to the uninitiated. It was high time that somebody in international affairs has approached the problem of “iatrogenics”, i.e. harm done by the healer. This book should be mandatory reading to every student and practitioner of foreign affairs.

(July 2016) Idea Makers: Personal Perspectives on the Lives & Ideas of Some Notable People

The general public is usually supplied by books on mathematical scientists written by “science communicators” and other outside observers–the worst by far being the academic historians of science. Their books are like reviews of comparative squid ink recipes written by anorexics, or descriptions of the Loire Valley by visually impaired travel writers. They are well written, which masks the BS. The descriptions focus on “interesting” traits of the personalities; scientists are discussed as if they were partaking of spectator sports. This fellow “was the best…”, this fellow “was the first to…”, “Einstein made a big blunder”, etc. This book, “Idea Makers”, is written from an insider. It is the real thing on several accounts. Primo, Wolfram deserves to be in the book as an “idea maker”, in his own right. Secondo, Wolfram is the developer of a new way to do (useful) mathematics, an entirely new method, which allows us to tinker with mathematics, something that is an anathema to purists. Thus he depicts Ramanujan, not with the usual mathematical prism of the theorem crowds, but as someone who, starting with intuitions, does experiments till a mathematical identity feels right. As an eyewitness, I spent almost all my career in quant finance and probability toying with Mathematica (Stephen Wolfram’s invention), and saw it accumulate special functions and tools. Mathematica allowed me to be a car mechanic who looked under the hood; such experience makes us look at the pompous theoretician as a cook would a nerdy chemist. The book is about this refreshing perspective: theorems were to Ramanujan a thing used by European mathematicians to convince other European mathematicians. Terso, Wolfram is fair. He shows a fair –even adulatory– portrait of Mandelbrot, in spite of attacks by the latter. Indeed, if Mandelbrot hated someone, the person has to be good and threatening. Otherwise he would not bother mentioning him. Finally, many of the people involved are actually known either personally (Feynman, Mandelbrot, Minsky), or like Boole, Ramanujan, Godel, and Lebnitz, “connect” to the author.

(April 2016) The Secret of Fatima (5 Stars)

Masterly! This is the page turner par excellence; every new page brings some surprise and it was impossible for me to put the book down. I even read some of it during elevator rides, not being able to resist. And truly sophisticated: Nobody but Peter Tanous would have imagined to cross James Bond with a Catholic priest.”

(May 2015) Birth of a Theorem: A Mathematical Adventure (5 stars)

A gem: how to go from the abstract to the abstract in a playful way. There is no book like it.

This book takes us through the formulation of the theorems in “On Landau damping” by Clément Mouhot and Cédric Villani. Villani is playful in real life, his research is playful, and the book is playful.

This is a gem for a singular reason. One sees exactly how Villani (or a pure mathematician) goes from abstract to abstract without ever exiting the world of pure and symbolic mathematics, even though the subject concerns a very concrete real-world topic. I kept waiting for him to use simulations or even plots to see how the equations worked. But he did not … he and Mouhot had recourse to outside help (a student or an assistant) for the graphs and he camly noted that they “looked” great. Later in the book he relied on others to do the numerical work… as an afterthought. Most physicists, quants, and applied mathematicians would have played with a computer to get the intuition; Villani just worked with mathematical objects, abstract mathematical objects, and very abstract at that. And this is a big deal for the subject because it belongs to a certain class of problems that do not have analytic solutions, usually requiring numerical approaches.

Landau damping is about something many people are indirectly familiar with. Some history: Fokker–Planck equation, itself the Kolmogorov forward equation, is used commonly as the law of motion of particles (hence diffusions in finance). We quants use it in the main partial stochastic differential equation. In plasma physics it is related to the Boltzman equation, which, by using mean-interraction in place of every interration (mean-field), leads to the Vlasov equation. Landau damping is (sort of) about how things don’t blow up because of some exponential decay. Proving it outside the linear version remained elusive. Villani and Mouhot set to prove it. They eventually do.
One note. I read it in the English translation (because I was in a hurry to get the book), but noticed an oddity that may confuse the reader. “Calcul” in French does not mean “calculation” (in the sense of numerical calculation) but “derivation”, so the reader might be confused about calculations thinking they were numerical when Villani stayed at the abstract/symbolic level.

I would have read the book in one sitting. It grips you like a detective novel.

PS- Some UK BS operator, the type of journalist with an attempt at some PhD in something related to physics who thinks he knows it all and is the representative of the general public trashed the book in the Spectator. Ignore him: the fellow is clueless. Look at reviews by PRACTICING quants and mathematicians. I do not think there is another book like this one.

(November 2014) Modern Aramaic-English/English-Modern Aramaic Dictionary & Phrasebook: Assyrian/Syriac (5 Stars)

There is no way we Levantines can learn the language of our ancestors in an organic way except via nerds insisting on 1) grammar, 2) writing in one of the unwieldy Syriac scripts that one cannot even read on a computer screen without dowloading strange fonts. But Aramaic is still spoken, let us take advantage of it, and figure out how to say “I want to eat mjaddara” rather than memorize poetry by some dead author. Aramaic isn’t a dead language and it is the shame Levantines study Arabic instead of our own heritage.

This book in the Latin alphabet makes both Swadaya and Turoyo alive and easy to read, with all manner of real-world expressions. One can use it to supplement scholarly studies, or just to figure out how modern people speak our ancient language. There are Arabic influences, but the distance between the spoken language and, say, Bar Hebraeus is quite narrow.
I would suggest the authors expand the dictionary. It would be the only one in the latin script.

Most excellent, except for very few and small mistakes. “Debo” in Turoyo is not wolf, but bear.

(April 2014) The Tyranny of Experts: Economists, Dictators, and the Forgotten Rights of the Poor (5 Stars)

The point that top-down development methods are great on paper but have not produced benefits (“so far”) is a point Easterly has made before, heavily influencing yours truly in the formation his own argument against naive interventionism and the collection of “humanitarians” fulfilling their personal growth and shielding themselves from their conscience… This is more powerful: the West has been putting development ahead of moral issues, patronizingly setting aside the right of the people to decide their own fate, including whether they want these “improvements”, hence compounding failure and turning much of development into an agenda that benefits the careers (and angst) of “humanitarians”, imperial policies, and, not least, local autocrats *without* any moral contribution. Talking about a sucker problem.

***

To put it in an aphorism, they didn’t ask the people if they would rather get respect and no aid rather than aid and no respect.

(Jan 2014) Modelling Extremal Events: for Insurance and Finance (Stochastic Modelling and Applied Probability) (5 stars “Indispensable”)

The mathematics of extreme events, or the remote parts of the probability distributions, is a discipline on its own, more important than any other with respect to risk and decisions since some domains are dominated by the extremes: for the class of subexponential (and of course for the subclass of power laws) the tails ARE the story.

Now this book is the bible for the field. It has been diligently updated. It is complete, in the sense that there is nothing of relevance that is not mentioned, treated, or referred to in the text. My business is hidden risk which starts where this book stops, and I need the most complete text for that.

In spite of the momentous importance of the field, there is a very small number of mathematicians who deal with tail events; of these there is a smaller group who go both inside and outside the “Cramer conditions” (intuitively, thin-tailed or exponential decline).

It is also a book that grows on you. I would have given it a 5 stars when I started using it; today I give it 6 stars, and certainly 7 next year.

I am buying a second copy for the office. If I had to go on a desert island with 2 probability books, I would take Feller’s two volumes (written >40 years ago) and this one.

One housecleaning detail: buy the hardcover, not the paperback as the ink quality is weaker for the latter.

(Dec 1/2013) The Kelly Capital Growth Investment Criterion: Theory and Practice (5 Stars)

There are two methods to consider in a risky strategy.

1) The first is to know all parameters about the future and engage in optimized portfolio construction, a lunacy unless one has a god-like knowledge of the future. Let us call it Markowitz-style. In order to implement a full Markowitz- style optimization, one needs to know the entire joint probability distribution of all assets for the entire future, plus the exact utility function for wealth at all future times. And without errors! (I have shown that estimation errors make the system explode.)

2) Kelly’s method (or, rather, Kelly-Thorpe), developed around the same period, which requires no joint distribution or utility function. It is very robust. In practice one needs to estimate the ratio of expected profit to worst- case return– dynamically adjusted to avoid ruin. In the case of barbell transformations, the worst case is guaranteed (leave 80% or so of your money in reserves). And model error is much, much milder under Kelly criterion. So, assuming one has the edge (as a sole central piece of information), engage in a dynamic strategy of variable betting, getting more conservative after losses (“cut your losses”) and more aggressive “with the house’s money”. The entire focus is the avoidance of gambler’s ruin.

The first strategy was only embraced by academic financial economists –empty suits without skin in the game — because you can make an academic career writing BS papers with method 1 much better than with method 2. On the other hand EVERY SURVIVING speculator uses explicitly or implicitly method 2 (evidence: Ray Dalio, Paul Tudor Jones, Renaissance, even Goldman Sachs!) For the first method, think of LTCM and the banking failure.

Let me repeat. Method 2 is much, much, much more scientific in the true sense of the word, that is rigorous and applicable. Method 1 is good for “job market papers” . Now this book presents all the major papers for the second line of thinking. It is almost exhaustive; many great thinkers in Information theory and probability (Ed Thorpe, Leo Breiman, T M Cover, Bill Ziemba) are represented… even the original paper by Bernouilli.

Buy 2 copies, just in case you lose one. This book has more meat than any other book in decision theory, economics, finance, etc…

(Sept 5/2013) A Few Lessons from Sherlock Holmes (5 Stars)

We Sherlock Holmes fans, readers, and secret imitators need a map. Here it is. Peter Bevelin is one of the wisest people on the planet. He went through the books and pulled out sections from Conan Doyle’s stories that are relevant to us moderns, a guide to both wisdom and Sherlock Holmes. It makes you both wiser and eager to reread Sherlock Holmes.

(Ed. I posted on Peter’s Book)

(Aug 31/2013) The Science of Conjecture: Evidence and Probability before Pascal (5 Stars)

Indispensable. As a practitioner of probability, I’ve read many book on the subject. More are linear combinations of other books and ideas rehashed without real understanding that the idea of probability harks back the Greek pisteuo (credibility) and pervaded classical thought. Almost all of these writers made the mistake to think that the ancients were not into probability. And most books such “Against the Gods” are not even wrong about the notion of probability: odds on coin flips are a mere footnote. If the ancients were not into computable probabilities, it was not because of theology, but because they were not into games. They dealt with complex decisions, not merely probability. And they were very sophisticated at it.

This book stands above, way above the rest: I’ve never seen a deeper exposition of the subject, as this text covers, in addition to the mathematical bases, the true philosophical origin of the notion of probability. In addition Franklin covers matters related to ethics and contract law, such as the works of the medieval thinker Pierre de Jean Olivi, that very few people discuss today.

Probability, Random Variables and Stochastic Processes (5 Stars)

When readers and students ask to me for a useable book for nonmathematicians to get into probability (or a probabilistic approach to statistics), before embarking into deeper problems, I suggest this book by the Late A. Papoulis. I even recommend it to mathematicians as their training often tends to make them spend too much time on limit theorems and very little on the actual “plumbing”.

The treatment has no measure theory, cuts to the chase, and can be used as a desk reference. If you want measure theory, go spend some time reading Billingsley. A deep understanding of measure theory is not necessary for scientific and engineering applications; it is not necessary for those who do not want to work on theorems and technical proofs.

I’ve notice a few complaints in the comments section by people who felt frustrated by the treatment: do not pay attention to them. Ignore them. It the subject itself that is difficult, not this book. The book, in fact, is admirable and comprehensive given the current state of the art.

I am using this book as a benchmark while writing my own, but more advanced, textbook (on errors in use of statistical models). Anything derived and presented in Papoulis, I can skip. And when students ask me what they need as pre-requisite to attend my class or read my book, my answer is: Papoulis if you are a scientist, Varadhan if you are more abstract.

Mathematics: Its Content, Methods and Meaning (5 Stars)

There is something admirable about the school of the Russians: they are thinkers doing math, with remarkable clarity, minimal formalism, and total absence of unnecessary pedantry one finds in more modern texts (in the post Bourbaki era). This is of course surprising as one would have expected the exact opposite from the products of the communist era. Mathematicians should be using this book as a model for their own composition. You can read it and reread it. Professors should assign this in addition to modern texts, as readers can get intutions, something alas absent from modern texts.

Probability Theory (Courant Lecture Notes) (5 Stars)

I know which books I value when I end up buying a second copy after losing the first one. This book gives a complete overview of the basis of probability theory with some grounding in measure theory, and presents the main proofs. It is remarkable because of its concision and completeness: visibly prof Varadhan lectured from these notes and kept improving on them until we got this gem. There is not a single sentence too many, yet nothing is missing.

For those who don’t know who he is, Varadhan stands as one of the greatest probabilists of all time. Learning probability from him is like learning from Aristotle.

Varadhan has two other similar volumes one covering stochastic processes the other into the theory of large deviations (though older than this current text). The book on Stochastic Processes should be paired with this one.

Models.Behaving.Badly.: Why Confusing Illusion with Reality Can Lead to Disaster, on Wall Street and in Life (5 Stars)

Here is what I wrote in my endorsement: Emanuel Derman has written my kind of a book, an elegant combination of memoir, confession, and essay on ethics, philosophy of science and professional practice. He convincingly establishes the difference between model and theory and shows why attempts to model financial markets can never be genuinely scientific. It vindicates those of us who hold that financial modeling is neither practical nor scientific. Exceedingly readable.

From the remarks here, people seem to be blaming Derman for not having written the type of books they usually read… They are blaming him for being original! This is very philistinic. This book is a personal essay; if you don’t like it, don’t read it, there is no need to blame the author for not delivering your regular science reporting. Why don’t you go blame Montaigne for discussing his personal habits in the middle of a meditation on war inspired by Plutarch?

Body by Science: A Research Based Program to Get the Results You Want in 12 Minutes a Week (5 Stars)

I feel guilty for not having posted a review earlier: I owe a lot to this book. I figured out the value of intensity training and maximizing recovery. I use the ideas but with minor modifications (my own personal workout is entirely based on free weights and barbells, but I incur –and accept –a risk of injury). I have been applying the ideas for more than three years. Just get over the inhibitions (and illusions of control) and accept the idea of training less.
Gratitude.

The Hour Between Dog and Wolf: Risk Taking, Gut Feelings and the Biology of Boom and Bust (5 Stars)

I read this book after completing my exposition of overcompensation, how a stressor or a random event causes an increase in strength, in excess of what is needed, like a redundancy. I was also looking for evidence of convex reaction to stressor, or the effect of a mathematical property called Jensen’s inequality in domains and found it exposed here (in other words, why a combination low dose (most of the time) and high dose (rarely) beats medium dose all the time. The authors presents the evidence for the phenomenon in the following: 1) acute stressors cum recovery beat both absence of stressors and chronic ones; 2) stressors make one stronger (post traumatic growth); 3) risk management is mediated by the deep structures in us, not rational decision-making; 4) winning causes an increase in strength (the latter are more complicated effects of convexity/Jensen’s Inequality).

Great book. I ignored the connection to financial markets while reading it. But I learned that when under stress, one should seek the familiar. Bravo!

The Opposing Shore (5 Stars)

Until I read this book, Buzzati’s “Il deserto dei tartari” was my favorite novel, perhaps my only novel, the only one I cared to keep re-reading through life. This is, remarkably a very similar story about the antichamber of anticipation (rather than “the antichamber of hope” as I called Buzzati’s book), but written in a much finer language, by a real writer (Buzzati was a journalist, which made his prose more functional) ; the style is lapidary with remarkable precision; it has texture, wealth of details, and creates a mesmerizing athmosphere. Once you enter it, you are stuck there. I kept telling myself while reading it: “this is the book”. It suddenly replaced the “deserto”.

A few caveats/comments. First, I read it in the original French Le Rivage des Syrtes (French Edition), not in this English translation, but I doubt that the translator can mess up such a fine style and the imagery. Second, the blurb says Gracq received the Goncourt prize for it. Julien Gracq REFUSED the Goncourt, he despised the Parisian literary circles and by 1951 decided to stay in the margin. He stuck to his publisher José Corti rather than switch to the fancy Gallimard after his success (as Proust did) (or other publishing houses for the fakes and the selfpromoters). Third, this book came out a few years after Buzzati’s “deserto”, but before Buzzati was translated into French. I wonder if Gracq had heard of the “deserto”; the coincidence is too strong to be ignored.

Bull by the Horns: Fighting to Save Main Street from Wall Street and Wall Street from Itself (5 Stars)

I don’t have time for a full review for now; all I have to say is that we have the account of a person who says it the way it was, revealing the types of truths that don’t fit the New York Times and others pawns. When history is written, this will be used, not the spin by the bankers’ slaves and soldiers (Geithner, Rubin et al.) Bravo Sheila!

Information: The New Language of Science (5 stars)

If you want an introduction to information theory, and, in a way, probability theory from the real front door, this is it. A clearly written book, very intuitive, explains things, such as the Monty Hall problem in a few lines. I will make it a prerequisite before more technical great books, such as Cover and Thompson.

Free The Animal: Lose Weight & Fat With The Paleo Diet (5 stars)

A charming primer on the paleo idea, with an illustration through the authors own life. I read it in one sitting.

Why Everyone (Else) Is a Hypocrite: Evolution and the Modular Mind (5 stars)

This is a great synthesis of the modularity approach to cognitive science. It covers the entire field and has the right footnotes for the patches.

The style is readable, & the author has an attitude (with is a very good thing, but his jokes are often bland, not aggressive enough). While I strongly disagree with his treatment of morality (I am deontic), I can safely say, so far, that this is not just one of the best books in cognitive science, but certainly one of the most readable.

Explaining Social Behavior: More Nuts and Bolts for the Social Sciences (5 stars)

I read this book twice. The first time, I thought that it was excellent, the best compendium of ideas of social science by arguably the best thinker in the field. I took copious notes, etc. I agreed with its patchwork-style approach to rational decision making. I knew that it had huge insights applicable to my refusal of general theories [they don’t work], rather limit ourselves to nuts and bolts [they work].

Then I started reading it again, as the book tends to locate itself by my bedside and sneaks itself in my suitcase when I go on a trip. It is as if the book wanted me to read it. It is what literature does to you when it is at its best. So I realized why: it had another layer of depth –and the author distilled ideas from the works of Proust, La Rochefoucault, Tocqueville, Montaigne, people with the kind of insights that extend beyond the ideas, and that makes you feel that a reductionist academic treatment of the subject will necessary distort it [& somehow Elster managed to combine Montaigne and Kahneman-Tversky]. So as an anti-Platonist I finally found a rigorous treatment of human nature that is not Platonistic –not academic (in the bad sense of the word).

The Discovery of France: A Historical Geography from the Revolution to the First World War (5 stars)

This book has wonderful qualities that I am certain will be picked up by other reviewers. But I would like to add the following. This is the most profound examination of how nationality is enforced on a group of people, with the internal colonization process and the stamping out of idiosyncratic traits. As someone suspicious of government and state control, I was wondering how France did so well in spite of having a big government. This book gave me the answer: it took a long time for the government and the “nation” to penetrate the depth of deep France, “la France profonde”. It was not until recently that French was spoken by the majority of the citizens. Schools taught French but it was just like Greek or Latin: people forgot it right after they finished their (short) school life. For a long time France’s villages were unreachable.

A great book, a great investigation.

Good Calories, Bad Calories: Challenging the Conventional Wisdom on Diet, Weight Control, and Disease (5 stars)

Gary Taubes is a true empiricist. I can’t believe people hold on to the Platonicity of the thermodynamic theory of diet (calorie in = calorie out).

Read it twice, once for the diet, once a a rich document in the history of science.

Plato and a Platypus Walk into a Bar: Understanding Philosophy Through Jokes (4 stars)

I read Plato and the Platypus by Umberto Eco, which I found brilliant and was sucked into buying this book thinking it was about the same problem of categories. But Philosophy this is not, or if it is, it is not deep enough to give satisfaction. This is like a brief drink in an airplane lounge with someone funny, smart, witty, but not too funny. So I would give it my lowest rating: 4 stars (as an author I can’t give below that –I just would not review).

Would I buy it again? Perhaps, but only for a plane ride. It left me very very hungry for both jokes and philosophy.

Seeking Wisdom: From Darwin to Munger, 3rd Edition (5 Stars)

A wonderful book on wisdom and decision-making written by a wise decision-maker. This is the kind of book you read first, then leave by your bedside and re-read a bit every day, so you can slowly soak up the wisdom. It is sort of Montaigne but applied to business, with a great investigation of the psychological dimension of decision-making.

I like the book for many reasons –the main one is that it was written by a practitioner who knows what he wants, not by an academic.

Enjoy it.

The Doctrine of Deification in the Greek Patristic Tradition (5 stars)

I initially bought this book as I was curious about the differences between Eastern & Western traditions, particularly with the notion of theosis –the deification of man. This book goes far deeper, and covers pre-Christian practices (like Stoic thoughts, the deifications of Kings, Roman Emperors, that of private citizens who committed symbolic acts –such as Antinous, Hadrian’s obsession, who drowned to “save” mankind and other sotirologies).

The book was initially Russell’s doctoral thesis, which, as far as I can guess from the dates, had to have been completed when he was in late middle age. But he made it very readable, free of the theophilosophical jargon of similar texts. He still has quotes in the original language and it is a true piece of scholarship.

Statistical Models: Theory and Practice (5 stars)

I spent my life focusing on the errors of statistics and how they sometimes fail us in real life, because of the misinterpretation of what the techniques can do for you. This book is outstanding in the following two aspects: 1) It is of immense clarity, embedding everything in real situations, 2) It uses the real-life situation to critique the statistical model and show you the limit of statistic. For instance, he shows a few anecdotes here and there to illustrate how correlation between two variables might not mean anything causal, or how asymptotic properties may not be relevant in real life.

This is the first statistics book I’ve seen that cares about presenting statistics as a tool to GET TO THE TRUTH.
Please buy it.

Happy Accidents: Serendipity in Modern Medical Breakthroughs (5 stars)

The Birth Stochastic Science: Rewriting the History of Medicine

Controlled experiment can easily show absence of design in medical research: you compare the results of top-down directed research to randomly generated discoveries. Well, the U.S. government provides us with the perfect experiment for that: the National Cancer Institute that came out of the Nixon “war on cancer” in the early 1970s.

“Despite the Herculean effort and enormous expense, only a few drugs for the treatment of cancer were found through NCI’s centrally directed, targeted program. Over a twenty-year period of screening more than 144,000 plant extracts, representing about 15,000 species, not a single plant-based anticancer drug reached approved status. This failure stands in stark contrast to the discovery in the late 1950s of a major group of plant-derived cancer drugs, the Vinca Alcaloids -a discovery that came about by chance, not through directed research.”

From Happy Accidents: Serendipity in Modern Medical Breakthroughs, by Morton Meyers, a book that just came out. It is a MUST read. Please go buy it. Read it twice, not once. Although the author does not take my drastic “stochastic tinkering” approach, he provides all kind of empirical evidence for the role of design. He does not directly discuss the narrative fallacy(q.v.) and the retrospective distortion (q.v.) but he certainly allows us to rewrite the history of medicine.

We did not realize that cures for cancer had been coming from other brands of research. You search for noncancer drugs and find something you were not looking for (and vice versa). But the interesting constant:
a- The discoverer is almost always treated like an idiot by his colleagues. Meyers describes the vicious side effect of “peer reviewing”.
b- Often people see the result but cannot connect the dots (researchers are autistic in their own way).
c- The members of the guild gives the researcher a hard time for not coming from their union. Pasteur was a chemist not a doctor/biologist. The establishment kept asking him “where is your M.D., monsieur”. Luckily Pasteur had too much confidence to be deterred.
d- Many of the results are initially discovered by an academic researchers who neglects the consequences because it is not his job –he has a script to follow. Or he cannot connect the dots because he is a nerd. Meyers uses Darwin as the ultimate model: the independent gentleman scholar who does not need anyone and can follow a lead when he sees it.
e- It seems to me that discoverers are nonnerds.
Now it is depressing to see the works of the late Roy Porter, a man with remarkable curiosity and a refined intellect, who wrote many charming books on the history of medicine. Does the narrative fallacy cancels everything he did? I hope not. We urgently need to rewrite the history of medicine without the ex post explanations. Meyers started the process: he provides data for modern medicine since, say, Pasteur. I am more interested in the genesis of the field before the Galenic nerdification.

Financial Derivatives: Pricing, Applications, and Mathematics (5 stars)

One of the author, Baz, gave me a copy of this book when it came out and it went to sleep in my library as I was not in a finance mood. I forgot about it until this week as I was stuck on a problem related to risk-neutral pricing and the Girsanov theorem concerning changes in probability measure. I looked at every passage on the the subject until I hit on it. Then I realized that I should have read it before: it is a condensed, but extremely deep , and complete exposition of the subject of theoretical finance.

No financial book has the clarity of this text.

Other quant books do not have such notions as “pricing kernel” and economic theoretical matters. I would recommend it as a necessary piece of the “quant” toolkit. Every quant should have it as a background tool as the usual quant literature is standalone and devoid of these concepts.

Thinking and Deciding (5 stars)

People vote with their wallet –particularly when they do it a second time, when they REpurchase. Those who believe in the “revelation of preferences” should note that there are books one buys again when a copy is lost –particularly when they are read cover to cover.

I am buying another copy of this book as mine was lost or misplaced. That should speak volumes.

Critical Phenomena in Natural Sciences: Chaos, Fractals, Selforganization and Disorder: Concepts and Tools (Springer Series in Synergetics) (5 stars)

As I am teaching the statistical mechanics part of a graduate class in mathematics,I was looking for a textbook on complex systems & statistical physics with derivations, intuitions, and some physical examples. I did not realize that I was looking too far –Sornette, with hom I correspond regularly, is well known for his contributions and his prolific output (actually some physicists make fun of the quantity of papers he writes). So his book did not come to mind. I once stumbled on a problem with the derivation of preferential attachments;he recommended his book, which I took with a grain a salt. After spending some time working the derivations on scalable laws, extreme value theory, renormalization groups in this book, I elected to use it as my textbook. There is no equivalent. I have a dozen such yellow manuals; this one is complete and ultimately clearest.

I do not know of a better textbook.

The Wisdom Paradox: How Your Mind Can Grow Stronger As Your Brain Grows Older (5 stars)

If you like the thinker’s prose, the so-called “romantic science”,a style attributed to the Russian neuroscientist A. R. Luria,which consists in publishing original research in literary form, you would love this book. Clearly intellectual scientists are vanishing under the weight of the commoditization of the discipline. But once in a while someone emerges to reverse such setbacks.

Goldberg, who was the great Luria’s student and collaborator, is even more colorful and fun to read than the master. He is egocentric, abrasive, opinionated, and colorful. He is also disdainful of the conventional beliefs in neurosciences –for instance he is suspicious of the assignment of specific functions, such as language, to anatomical regions. He is also skeptical of the journalistic “triune” brain. His theory is that the hemispheric specialization is principally along pattern matching and information processing lines:the left side stores patterns, while the right one processes novel tasks. It is convincing to see that children suffer more from a right brain injury, while adults have the opposite effect.

There is a little bit of open plugging of Goldberg’s for-profit institute;he would have gotten better results by being subtle. A fre minor points. I did not understand why Goldberg discusses “modularity”, of which he is critical, as if it were the same thing in both neurobiology and in cognitive science. In neurobiology, modularity implies regional localization, while cognitive scientists (Marr, Fodor, etc.) make no such assumption: for them it is entirely functional and they would be in great agreement with Goldberg. Also I did not understand why he attributes the language instinct to Pinker, not Chomsky, and why he makes snide remarks about behavioral scientists like Kahneman and Tversky. But these are very minor details that do not weaken the message (I still gave the book 5 stars). I am now spoiled; I need more essays by opinionated, original,and intellectual, contemporary scientists.

The Sunday Philosophy Club : An Isabel Dalhousie Mystery (5 stars)

If your interests are limited to mystery books, nothing else, this book is not for you.

I initially bought this book because of the title, thinking that we would have a female version of Her Professor Dr Dr (Hon.) Moritz-Maria von Igenfeld, the Pninish uberscholar philologist who wrote the seminal Portugese Irregular Verbs (“after which there was nothing left to discuss about the subject, Nothing.”). I was curious to see how he would present a female version of such scholar.

He did not. Nor was it a detective story, although there is an element of suspense. This book is about Applied Ethics, a subject about which the author seems to know a bit. It also makes you feel like leading a quite thinking life in Edinburgh.

I don’t want to spoil the story but I felt that I was reading a detective story until I realized what it was…

How Nature Works: The Science of Self-organized Criticality (5 stars)

This book is a great attempt at finding some universality based on systems in a “critical” state, with departures from such state taking place in a manner that follows power laws. The sandpile is a great baby model for that.

Some people are critical of Bak’s approach, some even suggesting that we may not get power laws in these “sandpile” effects, but something less scalable in the tails. The point is :so what? The man has vision.

I looked at the reviews of this book. Clearly a few narrow-minded scientists do not seem to like it (many did not like Per Bak’s ego). But the book is remarkably intuitive and the presentation is so clear that he takes you by the hand. It is even entertaining. If you are looking to find flaws in his argument his pedagogy allows it (it is immediately obvious to us who dabble with simulations of these processes that you need an infinite sandpile to get a pure power law).

Another problem. I have been ordering the book on Amazon for ages. Copernicus books does not respond to emails. I got my copy at the NYU library. Bak passed away 2 years ago and nobody seems to be pushing for his interest and that of us his readers (for used books to sell for 99 implies some demand). This convinces me NEVER to publish with Springer.

Social Cognition: Making Sense of People (5 stars)

I spent some time looking for a simple bedside aggregation of the various topics associated with the psychology of decision making and the various perceptual biases, without finding much. Most of the books are excellent; but, aside from this one (and Jon Baron’s) they are usually compilation of original research. I like to have a readable consolidation of the material not far from my figertips. I was lucky to have found this book, which provides a wonderful and comprehensive coverage of the topics.

It is limpid, precise, illustrative, showing a wonderful clarity of mind.

Now the bad news. The author passed away recently at the age of 48.

The (Mis)behavior of Markets (5 stars)

I have been involved in the professional practice of uncertainty for almost all of my adult life. I’ve seen and read books and papers on the subject of deviations, with “this is interesting” here and there. I closed this book feeling that it was the first book in economics that spoke directly to me. Not only that, but this astonishing simplicity, realism, and relevance of the subject makes it the only work in finance I’ve read that seemed to make sense.

I cannot make justice to the book other than say 1) MAKES SENSE, 2) EASY TO UNDERSTAND, 3) PRESENT SUCH EMPIRICAL VALIDY that it will make financial economists (charlatans) have to hide deeper from the common man with their complicated “mathematics”.

Mandelbrot brought fractals into mathematics by going to the general public. He is doing the same here: pleading to the regular man unburnded with knowledge of economics.

The Status Syndrome: How Social Standing Affects Our Health and Longevity (5 stars)

You are a hot shot in a company, though not the boss. You are paid extremely well, but, again you have plenty of bosses above you (say the partners of an investment firm). Is it better than deriving a modest income being your own boss? The counterintuive answer is NO. You will live longer in the second situation, even controlling for diet, lifestyle, and genetic predispositions.

Marmot spent years poring over data; he left no stone unturned and is well read in the general literature on human nature. This idea of people living longer when they exert control over their lives has not spread yet. That people lead longer lives when they trust their neighbors and feel part of a community is far reaching. Just think of the implications on social justice etc. Also think that everything you learn on human preferences and well-being in both economics and medicine is either incomplete (medicine) or bogus (economics).

The book is well written, humorous at times, and rigorous –it reads like a well-translated scientific paper. But it feels that it is just the introduction to a topic. Please, write the continuation.

The Paradox of Choice: Why More Is Less (5 stars)

I find it clear in its exposition of the problems of modern psychology. In addition to the ideas of “satisficing”, it displays the major ideas in the psychology of happiness (hedonic treadmill), along with the theories of choice & decision making.

Clearly this is not for scholars as it is extremely diluted and slow at times; this is a popular science book. Still, I could not put it down.

The Dream of Reason: A History of Philosophy from the Greeks to the Renaissance (5 stars)

I could not put it down. It hit me at some point that I was at the intersection of readability and scholarship. Clearly the value of this book lies beyond its readability: Gottlieb is both a philosopher and a journalist (in the good sense), not a journalist who writes about philosophy. He investigates and provides a fresh look at the material: For instance what we bemoan as the flaws of Aristotelianism during the scholastic period came 2000 years after his work. Aristotle had an empirical bent –his followers are the ones to blame.

I liked his constant questioning of the labels put on philosophers and philosophies by the second hand readers.

Clearly he missed a few authors who deserve real coverage like Algazali, but I take what I can get.

The only other readable history of philosophy is Russell’s. This one was less hurriedly put together.

Someone should bug the author to hurry with the sequel on Locke, Hume, etc.

Intellectuals in the Middle Ages (5 stars)

Excellent, be it only for the presentation of the difference between the pompous scholastic thinker laboring in the academy and the other nonacademic humanist laboring in the the “luxe calme et volupte” of his study.

Another of the attributes is the readability of the work Le Goff is a gifted writer.

Kant and the Platypus: Essays on Language and Cognition (5 stars)

I read the review of Simon Blackburn trashing the book: Eco made a few mistakes concerning the two dogmas of empiricism (he confused Davidson’s work with Quine’s first dogma). So I am sure many readers hesitated after a review by such a rigorous big gun thinker as Blackburn.

When I started reading the book I was taken aback by the combination of depth and the vividness of the style. Eco is sprightly and alive, something that cannot be said of many philosophers dealing with the subject of categories.

The notion of categories is not trivial: you need a simple conditional prior to identify an object; it is a simple mathematical fact. You need to know what a table is to see it in the background separated from its surroundings. You need to know what a face is so when it rotates you know it is still the same face. Computers have had a hard time with such pattern recognition. A PRIOR category is a necessity. This was Kant’s intuition (the so-called “rationalism”). This is also the field of semiotics as initially conceived. Eco took it to greater levels with his notion of what I would call in scientific language a compression, a “simplifation”. This leads to the major problem we face today: what if the act of compressing is arbitrary?

Not just very deep but it is a breath of fresh air to see such a philosophical discussion nondull, nondry, alive!

Confessions of a Philosopher: A Personal Journey Through Western Philosophy from Plato to Popper (5 stars)

This is not a polularization /adult-education style presentation. Magee sees things form the inside; it is his own formation of philosophical ideas & techniques that we witness.

Magee was close enough to Popper to present us with his ideas first-hand (nobody reads Popper; people read about him). He also debunks a few idiotic myths about Wittgenstein as an atomist (Magee read W and realized that people read commentary on him rarely the original).

Magee writes with the remarkable clarity of the English philosophers/thinkers.

Invariances: The Structure of the Objective World (5 stars)

Philosophy has been under severe challenge from science, literally eating up its provinces: philosophy of mind went to neuroscience; philosophy of language to Artificial Intelligence and Computer Science,etc. This book shows that there is a need for someone to just specialize in the TRUTH, its scructure, its accessibility, its INVARIANCE.

Aside from the purely philosophical answers that scientists were grappling with, the book is like a manual for a new regimen in philosophy. It reviews everything from epistemology to the logic of contingency, with insights here and there about such topics as the observer biases (about computing probabilities when our existence has been linked to a particular realization of the process).

I am not a philosopher but a probabilist; I found that this book just spoke to me. It certainly rid me of my prejudice against modern philosophers.

A History of the Mind: Evolution and the Birth of Consciousness (5 stars)

Humphreys is the only person I know of who can work on nonhuman primates, write philosophy, and edit a literary magazine.

The latter shows in this writing: I read this book in a single sitting. You may not agree with the ideas on consciousness (I don’t) but you get a clear exposition of all the work from Descartes to McGinn. Also if you want to figure out what Dennett is saying it helps to read this book first.

Bull! : A History of the Boom, 1982-1999: What drove the Breakneck Market–and What Every Investor Needs to Know About Financial Cycles (5 stars)

Maggie Mahar had the courage to take a look at what was behind all of this religious belief in markets. Clearly I do not understand how she was able to work as a journalist when she has the attitude and mindset of a truth-seeker. I spent some time looking at the difference between her book and Lowenstein’s: not even possible to start comparing. One needs to be a trader to value her work.

Read this book now; wait a while then read it again.

I Think, Therefore I Laugh (5 stars)

I found this copy last week at Waterstone in London . It made me feel the plane ride was very short! I should have bought a couple. This is a great book for a refresher in analytical philosophy: pleasant, clear. Great training for people who tend to forget elementary relationships.

I did not know that JAP was a logician. Go buy this book!

The only competition is “Think” by Blackburn (rather boring).

The Making of a Philosopher: My Journey Through Twentieth-Century Philosophy (4 stars)

This is a great book but I felt something cold inside of me while reading it. I don’t know if it is cultural (the modern English philosopher’s fear of displaying passion) but I had the feeling to talk to a plumber who developed expertise in abstract concepts and their relationships just as if they were small plumbing problems fitting together under a generalized plumbing theory. Perhaps philosophy needs to be treated like that, just like engineering –but not for me. At least I give myself the illusion of doing something more…literary.

Colin McGINN teaches us that we need nevertheless to master the art of clarity of both thought and exposition. He write with perfect clarity: a clear, unburdened, unaffected, UnFrench UnGerman philosophical prose.

The book has a presentation of the Kripke idea of naming as necessity of such clarity that I felt actually smart reading it.

Other than that there is the feeling of drabness in part of the book of the type I got once at a conference in an industrial city West of London.

Straw Dogs: Thoughts on Humans and Other Animals (4 stars)

I became interested in this book while reading a review panning it in The Nation by one Danny Postell (thanks to Arts & Letters Daily). Clearly it was visible that John Gray was after a definition of humans that integrates our discoveries from cognitive science, that we are just animals who are curse with intelligence, sufficient intelligence to figure out things but insufficient to control our actions –what I call the ability to rationalize (“much of the difference between us and other primates lies in our being considerably better than them at explaining our behavior”). Postel (I have no clue who he is and what kind of training he has in modern scientific thought but I am sure that he is sufficiently burdened with a knowledge of humanities verbiage to get the book wrong); Postel was panning Gray exactly for the reasons that would make this book insightful. So I BOUGHT THIS BOOK BECAUSE OF A BAD REVIEW!

What struck me with this book is that Gray converges in opinion to the discoveries of the New Science of Man –without quoting from neurobiology, cognitive science, evolutionary psychology, the Kahneman-Tversky Heuristics & Biases Tradition. It is remarkable that he identified the ills of the so-called humanist tradition without assistance from the works on rationality posited by Kahneman and his peers.

This book is worth 4 stars because here we have a literary intellectual who manages to break through the mud in his knowledge. It would have been worth 5 stars had Gray read a few more works in scientific thought beyond Darwin. Anyway I am very impressed with a literary intellectual capable of this empirical and realistic view of man.

Mapping the Mind (5 stars)

I started my interest in neurobiology in December 1998 after reading a discussion by Rita Carter in the FT showing that rational behavior under uncertainty and rational decision making can come from a defect in the amygdala. Since then I’ve had five years of reading more technical material (Gazzaniga et al is perhaps the most complete reference on cognitive neuroscience) and thought that I transcended this book.

But it was not so. I picked up this book again last weekend and was both astonished at a) the ease of reading , b) the clarity of the text and c) the breadth of the approach! I was looking for a refresher as I am trying to capture a general idea of the functioning of that black box and found exactly what I needed without the excess burden of prominent textbooks.

Very pedagogical.

I read here and there comments by neuroscientists dissing the book over small details perhaps invisible even to experts. I just realize that Carter should keep updating it, as it is invaluable in my suitcase when I travel! I do not conceal my suspicion of “science writers” and journalists more trained in communicating than understanding and usually shallow babblers but Carter is an exception. Perhaps the science of the mind requires breadth of knowledge that she has. She is a thinker in her own right not just a “medical journalist”.

The Mind Doesn’t Work That Way (5 stars)

This critique of the computational theory of mind and the pan-adaptionist tradition is clearly so honest that it goes after the ideas promoted by Fodor’s own 1983 watershed book “The Modularity of Mind”. In brief the essay is an attack on massive modularity by saying that there are things after all that escape the programming (encapsulation and opacity are key: how can we talk about something OPAQUE? We know nothing about a few critical things…).

Granted the book is horribly written (that is Fodor’s charm after all) but his argumentation is so ferocious that he ends up loud & clear.

The man is critical of his own ideas, and of the current in thought that he he helped create –one may use Fodor-1 against Fodor-2. Perhaps persons I hold in highest respect are those who go after their own ideas!

Bravo Fodor. Even if I do not agree I can’t help admiring the man.

Consciousness: An Introduction (5 stars)

I am glad to find a complete book dealing with all aspects of consciousness in CLEARLY written format, with graphs and tables to facilitate comprehension. The book covers everything I had seen before from Artificial Intelligence to Philosophy to Neurology to Evolutionary Biology.

Say one wants to get an idea of Dan Dennett’s theory of consciousness (without having to get through Dennett’s circuitous, unfocused and evasive prose) or Searle’s Chinese room argument or Turing’s test or Chalmer’s position or Churchland’s neurophilosophy or a presentation of research on the neural correlates of consciousness…Everything I could think about is there.

Mean Genes: From Sex to Money to Food: Taming Our Primal Instincts (5 stars)

I read the book once when it came out. Since then I’ve had the chance to reread it a few times, discovering more and more layers as my interests take me in new directions(for instance the discussion on the happiness treadmill goes to the core of the current discussions in the economics of happiness). I now carry a copy on my trips as I can kill time in airports by perusing random sections.

The book is so readable as to perhaps set a standard. Yet it is complete in the sense that it covers more of the evolutionary thinking than meets the eye. I didn’t realize it until I went to the site www.meangenes.org and got into the more technical research material.
Reread it.

Why Stock Markets Crash: Critical Events in Complex Financial Systems (5 stars)

The author aside from the problem of crashes presents an insightful exposition of tipping points. I don’t know why his approach makes it clearer and deeper than those of Watts and Barabasi –is it due to his using financial markets as a base? or his being an expert at fat-tailed dynamics?

His work builds on the “abyssus abyssum invocat” (panic begets panics) and the dynamics of compounding disequilibria. In addition the notion of “CRITICAL POINT” is made very clear.

Honestly I don’t care for the idea of crashes; the same concepts can apply to sudden and unexpected euphorias.

I learned more from this book than any other on disequilibrium.

The New Financial Order: Risk in the 21st Century (5 stars)

Robert Shiller has the remarkable ability to think independently and the courage to propose ideas that to middlebrow thinkers may sound speculative.

Think of what your reaction would have been had someone discussed risk sharing (insurance) before it became popular. A lunacy people would have thought. Most risk management is like that: we think backwards with the benefit of past history and find these ideas obvious. They were not at the time.

Throughout his career Shiller stood for unpopular ideas and was proven right (his 1981 paper on volatility, his 2000 discussion of the bubble). I would read and re-read this book.

Strangers to Ourselves: Discovering the Adaptive Unconscious (5 stars)

The book that carried the most influence on my thinking this year (I went back to it half a dozen times).
This is a clearly written presentation of our inability to forecast our own behavior and to predict our emotional reactions to positive and negative events. One would think that the repetition of experiences with consistent forecasting biases would lead to some correction but this is not the case.

We are more resilient than we think (“immune neglect”). The book also discusses the reversion to baseline happiness after what we thought would bring a permanent improvement in our moods (yet we never learn from it).

The most important part covers the “hindsight bias” how we see past misfortunes as deterministic –and how we can confront negative emotions by making them even more so (by creating a narrative that make the events appear unavoidable).

The Blank Slate: The Modern Denial of Human Nature (4 stars)

The book is a great exposition of modern scientific thinking and understanding of the nature of man–but it spends some time on topics that are entirely obvious outside of the humanities academia. Indeed Pinker gives them too much respect by honoring them with such a lengthy reply.

His other two books are much better.

No Bull: My Life In and Out of Markets (5 stars)

As a speculator I learned to take the best from books and ideas without arguments (many readers seem to be training to be shallow critics)–good insights are hard to come by. One does not find these in the writings of a journalist. There are some things personal to the author that might be uninteresting to some, but I take the package. The man is one of the greatest traders in history. There are a few jewels in there.

The man did it. I’d rather listen to him than read better written but hollow prose from some journalist-writer.

The Statistical Mechanics of Financial Markets (5 stars)

Very useful book, particularly in what concerns alternative L-Stable distributions. True, not too versed in financial theory but I’d rather see the author erring on the side of more physics than mathematical economics. As an author I don’t ask much from books, just to deliver what they indend. This one does.

Clear historical description of Einstein/Bachelier. Hopefully one day we will call derivatives pricing the Bachelier valuation.

The book in short provides an excellent perspective on the statistical approach to asset price dynamics. Very clear and to the point.

Tartar Steppe (Verba Mundi) (5 stars)

I never understood why the book never made it in the Anglo-Saxon world. Il deserto is one of the 20th century’s masterpieces.

A Guide to Econometrics – 4th Edition (5 stars)

The best intuition builder in both statitics and econometrics. I have been reading the various editions throught my career. Please, keep updating it, Peter Kennedy! ''',

                '2': '''Mental Models: The Best Way to Make Intelligent Decisions (109 Models Explained)
The Great Mental Models Volumes One and Two are out.
Learn more about the project here.

This guide explores everything you need to know about mental models. By the time you’re done, you’ll think better, make fewer mistakes, and get better results.

Let’s explore the following:

What Are Mental Models?
Learning to Think Better
Building a Latticework of Mental Models
Mental Models
General Thinking Concepts
Physics and Chemistry
Biology
Systems
Numeracy
Microeconomics
Military and War
Human Nature and Judgment


What Are Mental Models?
Mental models are how we understand the world. Not only do they shape what we think and how we understand but they shape the connections and opportunities that we see. Mental models are how we simplify complexity, why we consider some things more relevant than others, and how we reason.

A mental model is simply a representation of how something works. We cannot keep all of the details of the world in our brains, so we use models to simplify the complex into understandable and organizable chunks.

Learning to Think Better
The quality of our thinking is proportional to the models in our head and their usefulness in the situation at hand. The more models you have—the bigger your toolbox—the more likely you are to have the right models to see reality. It turns out that when it comes to improving your ability to make decisions variety matters.

Most of us, however, are specialists. Instead of a latticework of mental models, we have a few from our discipline. Each specialist sees something different. By default, a typical Engineer will think in systems. A psychologist will think in terms of incentives. A biologist will think in terms of evolution. By putting these disciplines together in our head, we can walk around a problem in a three dimensional way. If we’re only looking at the problem one way, we’ve got a blind spot. And blind spots can kill you.

Here’s another way to think about it. When a botanist looks at a forest they may focus on the ecosystem, an environmentalist sees the impact of climate change, a forestry engineer the state of the tree growth, a business person the value of the land. None are wrong, but neither are any of them able to describe the full scope of the forest. Sharing knowledge, or learning the basics of the other disciplines, would lead to a more well-rounded understanding that would allow for better initial decisions about managing the forest.

In a famous speech in the 1990s, Charlie Munger summed up the approach to practical wisdom through understanding mental models by saying: “Well, the first rule is that you can’t really know anything if you just remember isolated facts and try and bang ’em back. If the facts don’t hang together on a latticework of theory, you don’t have them in a usable form. You’ve got to have models in your head. And you’ve got to array your experience both vicarious and direct on this latticework of models. You may have noticed students who just try to remember and pound back what is remembered. Well, they fail in school and in life. You’ve got to hang experience on a latticework of models in your head.”

Mental Model Toolbox

A Latticework of Mental Models
To help you build your latticework of mental models so you can make better decisions, we’ve collected and summarized the ones we’ve found the most useful.

And remember: Building your latticework is a lifelong project. Stick with it, and you’ll find that your ability to understand reality, make consistently good decisions, and help those you love will always be improving.

General Thinking Concepts
1. The Map is not the Territory
The map of reality is not reality. Even the best maps are imperfect. That’s because they are reductions of what they represent. If a map were to represent the territory with perfect fidelity, it would no longer be a reduction and thus would no longer be useful to us. A map can also be a snapshot of a point in time, representing something that no longer exists. This is important to keep in mind as we think through problems and make better decisions.

2. Circle of Competence
When ego and not competence drives what we undertake, we have blind spots. If you know what you understand, you know where you have an edge over others. When you are honest about where your knowledge is lacking you know where you are vulnerable and where you can improve. Understanding your circle of competence improves decision making and outcomes.

3. First Principles Thinking
First principles thinking is one of the best ways to reverse-engineer complicated situations and unleash creative possibility. Sometimes called reasoning from first principles, it’s a tool to help clarify complicated problems by separating the underlying ideas or facts from any assumptions based on them. What remains are the essentials. If you know the first principles of something, you can build the rest of your knowledge around them to produce something new.

4. Thought Experiment
Thought experiments can be defined as “devices of the imagination used to investigate the nature of things.” Many disciplines, such as philosophy and physics, make use of thought experiments to examine what can be known. In doing so, they can open up new avenues for inquiry and exploration. Thought experiments are powerful because they help us learn from our mistakes and avoid future ones. They let us take on the impossible, evaluate the potential consequences of our actions, and re-examine history to make better decisions. They can help us both figure out what we really want, and the best way to get there.

5. Second-Order Thinking
Almost everyone can anticipate the immediate results of their actions. This type of first-order thinking is easy and safe but it’s also a way to ensure you get the same results that everyone else gets. Second-order thinking is thinking farther ahead and thinking holistically. It requires us to not only consider our actions and their immediate consequences, but the subsequent effects of those actions as well. Failing to consider the second and third order effects can unleash disaster.

6. Probabilistic Thinking
Probabilistic thinking is essentially trying to estimate, using some tools of math and logic, the likelihood of any specific outcome coming to pass. It is one of the best tools we have to improve the accuracy of our decisions. In a world where each moment is determined by an infinitely complex set of factors, probabilistic thinking helps us identify the most likely outcomes. When we know these our decisions can be more precise and effective.

This includes Fat-Tailed Processes

A process can often look like a normal distribution but have a large “tail” – meaning that seemingly outlier events are far more likely than they are in an actual normal distribution. A strategy or process may be far more risky than a normal distribution is capable of describing if the fat tail is on the negative side, or far more profitable if the fat tail is on the positive side. Much of the human social world is said to be fat-tailed rather than normally distributed.

and Bayesian Updating

The Bayesian method is a method of thought (named for Thomas Bayes) whereby one takes into account all prior relevant probabilities and then incrementally updates them as newer information arrives. This method is especially productive given the fundamentally non-deterministic world we experience: We must use prior odds and new information in combination to arrive at our best decisions. This is not necessarily our intuitive decision-making engine.

7. Inversion
Inversion is a powerful tool to improve your thinking because it helps you identify and remove obstacles to success. The root of inversion is “invert,” which means to upend or turn upside down. As a thinking tool it means approaching a situation from the opposite end of the natural starting point. Most of us tend to think one way about a problem: forward. Inversion allows us to flip the problem around and think backward. Sometimes it’s good to start at the beginning, but it can be more useful to start at the end.

8. Occam’s Razor
Simpler explanations are more likely to be true than complicated ones. This is the essence of Occam’s Razor, a classic principle of logic and problem-solving. Instead of wasting your time trying to disprove complex scenarios, you can make decisions more confidently by basing them on the explanation that has the fewest moving parts.

9. Hanlon’s Razor
Hard to trace in its origin, Hanlon’s Razor states that we should not attribute to malice that which is more easily explained by stupidity. In a complex world, using this model helps us avoid paranoia and ideology. By not generally assuming that bad results are the fault of a bad actor, we look for options instead of missing opportunities. This model reminds us that people do make mistakes. It demands that we ask if there is another reasonable explanation for the events that have occurred. The explanation most likely to be right is the one that contains the least amount of intent. ''',

                '3': '''How to Make Smart Decisions Without Getting Lucky
Few things will change your trajectory in life or business as much as learning to make effective decisions.

The decision-making principles in this article aren’t pulled out of thin air. They’re the result of many years of experience and experimentation. They draw upon the combined expertise of some of history’s deepest thinkers. They summarize the core insights and skills from influential books on decision-making.

In this guide, we’ll cover:

No One Taught you How to Decide
Your Mind is a Pattern Matching Machine
Decision Making
Smart People Make Terrible Decisions
Sources of Stupidy
Intelligent Preparation: The World Is Multidisciplinary
How We Make Decisions
General Thinking Concepts
Add To Your Decision Making Skills
Books to Improve Decisions
Ready? Ok, Let’s dig in.

(c) 2018 Farnam Street Media Inc. All rights reserved. May not be used without written permission.

No one Taught you How to Decide
I started working at an intelligence agency on August 28, 2001. Two weeks later, the world would never be the same.

My computer science degree lost its value after a few promotions. I came from a world of 1s and 0s, not people, families, and interpersonal dynamics.

Just out of school, I found that my decisions affected not only my employees but their families. Not only my country but other countries. However, there was one small problem. I had no idea how to make smart decisions. I had no idea how to reduce errors. I only knew I had an obligation to make the best decisions I could. But where do you start?

There is no class called “decision making.” Making better decisions isn’t one skill but rather a series of tools and frameworks. What distinguishes consistently good decision makers from poor ones is a series of diverse mental frameworks and tools (as well as relevant specific information).

Most of us operate like a carpenter with only a hammer. To a man with a hammer, every problem looks like a nail. No matter the job, we pull out our hammer and attempt to make it work. While a hammer can often get the job done eventually, it comes with a cost. In my world a poor decision could cost lives, impact my country, or even start a war. A hammer wasn’t enough, I wanted more tools.

To fill my mental toolbox, I looked around my organization and found some mentors. I watched them, asked them annoying questions, and tried to learn as much as I could from them. I went back to school to get an MBA. I read everything I could about making decisions and the tools I needed to develop.

Thanks to the internet, I was no longer limited to the best teachers in my organization or university. The entire world was available. I could find the best teachers in the world, learn their tools and frameworks, and add them to my mental toolbox.

“The older I get the more I realize how many kinds of smart there are. There are a lot of kinds of smart. There are a lot of kinds of stupid, too.”
— Jeff Bezos

Your Mind is a Pattern Matching Machine
You probably don’t know it but you already think in mental models. Mental models are mental chunks of knowledge that represent a concept. Gravity is a model. So is probabilistic thinking, inversion, and entropy.

Mental models shape how you think, how you approach problems, and how you identify the information that matters and ignore what doesn’t. The mental models in your head are your cognitive skillset.

Decision Making
Think about the state of your life, your career, your business, your major relationships — anything consequential to you.

How many important decisions have you already had to make? With the benefit of hindsight, how well did you make them?

How many decisions did you make today? How did you make these decisions? Is there a better way?



Not all decisions matter. Most decisions, like where to grab a sandwich, are unimportant. The consequences of these decisions don’t matter.

Yet some decisions are critical — they change our lives. Whether its who to trust, where to live, or whom to marry, these decisions reverberate for years.

Yet most of us don’t have the right skills to think through these problems. As a result, we often fall back to the pro-con list, where you list all the positive things that happen on one side and the negative things on the other trading them off.

While useful when deciding what to have for lunch, the pro-con list comes with a lot of blind spots.

“I regard it as a criminal waste of time to go through the slow and painful ordeal of ascertaining things for one’s self if these same things have already been ascertained and made available by others.”
—Thomas Edison

SMART People Make Terrible Decisions
Otherwise smart people can make terrible decisions. Think about decisions like these:

Napoleon deciding to invade Russia (and Hitler doing it again 130 years later)
An editor deciding to publish O.J Simpson’s If I Did It
Chris Webber choosing the timeout he didn’t have in the 1993 Final Four
NASA’s decision to ignore the O-ring issues on the Challenger
President Kennedy’s famous blunder to continue the Bay of Pigs operation inherited from the previous administration (a mistake he quickly learned from)
Margaret Thatcher deciding to get behind a “poll tax” that led to her ouster by her own party
Juergen Schrempp, the CEO of Daimler-Benz, deciding to merge with Chrysler despite massive internal opposition and a general history of big M&A deals working very poorly
Jim Cramer looking at Bear Stearns in 2007 and calling it a “BUY”
…and a hundred thousand more…
These were catastrophic decisions made by people who were, in some sense, professional decision-makers. They had impeccable credentials and judgment, and yet they made poor decisions due to poor judgment, a too-limited mental representations of the world, or just plain stupidity.

Sources of Stupidity
There are a lot of reasons we fail to make effective decisions.

Let’s take a look at five of the biggest ones:

1. We’re unintentionally stupid. I like to think that I’m rational and capable of interpreting all information in a non-biased way but that’s a dream. Cognitive biases are great at explaining how our evolutionary programming leads us astray. Knowledge of these biases in advance rarely helps us make better decisions. There are, however, many easily recognizable situations that increase the odds we’re about to do something stupid. Whether we’re tired, overly focused on a goal, rushing, distracted, operating in a group, or under the influence of a group, we’re more prone to stupidity.2

2. We have the wrong information. Making decisions with the wrong assumptions or facts is likely to lead to disaster.

3. We use the wrong model. We use mental models to make decisions. The quality of those models determines the quality of our thinking. There are a variety of reasons that we use false, incomplete, or incorrect models. Novices are prone to using models that the expert knows are incomplete or irrelevant. The odds of employing the wrong models increase as the pace of environmental change increases.

4. We fail to learn. We all know the person that has 20 years of experience but it’s really the same year over and over. Well, that person is sometimes us. If we don’t understand how we learn, we’re likely to make the same mistakes over and over.

5. Looking over doing good. Our evolutionary programming conditions us to do what’s easy over what’s right. After all it’s often easier to signal being virtuous than actually being virtuous. We unconsciously make choices based on optics, politics, and defendability. We hate criticism and seek the validation of our peers and superiors. We often want to feel good about ourselves first and have the outcome we desire second.

Luckily, we can take steps to reduce the odds of stupidity and increase the odds of good decisions in each of these categories.

“The frog in the well knows nothing of the mighty ocean.”
—Japanese Proverb

Intelligent Preparation: The World Is Multidisciplinary
We live in a society that demands specialization. Being the best means being an expert in something. Letters after your name and decades in the trenches of experience are required before you can claim to know anything. In one sense there is nothing wrong with this — specialized knowledge is required to solve problems and advance our global potential. But a byproduct of this niche focus is that it narrows the ways we think we can apply our knowledge without being called a fraud.

So we think physicists can’t teach us about love; mathematicians can’t instruct us on how to run a business; poets don’t know squat about “my life.” And bloggers can’t contribute to philosophy.

I don’t believe this is true.

Knowledge is hard to come by.

It takes work and commitment, and I think we owe it to ourselves to take it out of the box it comes in and experiment with it. We should blow past conformity and apply all the knowledge at our disposal to the problems and challenges we face every day.

Think about it. Over time you’ve picked up a lot of fundamentals about how the world works. You may have read a book about the Manhattan Project and the building of the nuclear bomb that was launched at Hiroshima. This story conveys the awesome power of self-sustaining nuclear reactions. Have you ever thought about applying those ideas to your life? You should.

How We Make Decisions
When was the last time you thought about how you make decisions?

If you’re like most people, you’ve never been explicitly taught how to make effective decisions. You make decisions like a golfer who never took any lessons: miserable with the state of your game and yet not seeking to learn a better swing, and instead hoping for the best every time you lift the club. Hoping that this time your choice will finally work out.

In the early 1980s, Charlie Munger and his partner Warren Buffett realized that a Savings & Loan operation they owned, as with the rest of the industry, was doomed to fail miserably due to forces outside of their control. At a time when almost none of their peers were taking action, they changed course dramatically, massively reducing the effect of the bank’s failure on the rest of their business holdings. These two men knew they had to act much differently than their peers.

It worked: The S&L industry collapsed, yet Munger and Buffett escaped with barely a scratch. They saved themselves a great deal of stress and financial pain by applying a uniquely effective system of organized common sense. In hindsight, it seems like an obvious good decision; at the time, it seemed odd and unusual.

The lesson for us is that the people making consistently good decisions take advantage of how the world works. That’s wisdom.

Real knowledge of the art of decision making, which remains true across time and circumstances, eras and epochs, can help increase the odds that we get what we want and reduce costly mistakes.

While everyone else is guessing, falling into old patterns, blindly following cognitive biases, we can be clear-headed and laser-focused.

That’s what Farnam Street is all about.

Here are some examples of applying — or failing to apply — knowledge about how the world really works.

It doesn’t matter how smart you are if you don’t realize where things are additive and where they are multiplicative. Nikola Tesla failed to understand Multiplication by Zero when he failed to realize that poor relations with others affected his life. While the Serbian-American was a brilliant inventor, he had difficulty relating to others, which made him difficult to work with. This problem cost him a Nobel Prize and a fortune that today would likely have made him the richest man in the world.
While we all rely on maps, which are reductions of complexity, to make decisions, they are not always accurate. General George S. Patton Jr. understood that the map is not the territory. When he visited the troops near Coutances, he found them sitting on the side of the road, studying a map. Responding to Patton’s inquiry as to why they had not crossed the Seine, the troops informed him that they were studying the map and could not find a safe place to wade across. Patton informed them that he had just waded across it and it was not more than two feet deep.
While we all like to be in the sexy industries, that desire shows an under-appreciation for the laws of thermodynamics. Smart companies like Berkshire Hathaway, guided by legendary investor Warren Buffett, understand that contrast is important. Sexy internet businesses are rarely effective, no matter how good they are, because the others are nearly just as good. What you want is contrast — to be the big fish in a small pond. And when you analyze the types of investments he’s made over the years, that’s what you find. If you’re going to compete with people, you want to compete with people who are way less sophisticated than you.
Understanding and applying the mental model of relativity helped Michael Abrashoff take the worst-performing ship in the US Pacific Fleet and turn it into the best. In his book, It’s Your Ship, he wrote: “The most important skill a skipper can have is the ability to see through the eyes of the crew.”
This website is about understanding and applying these time-tested mental models. Knowing how the world works means that you can stop fighting reality — and yourself along with it.

General Thinking Concepts
Combining intelligent preparation — learning about the big time-tested ideas from multiple disciplines — with general thinking frameworks will dramatically improve your decision-making skills.

These thinking frameworks help you look at problems through different lenses.

Inversion — Otherwise known as thinking something through in reverse or thinking “backwards,” inversion is a problem-solving technique.
Second-Order Thinking — Ask yourself, “And then what?”
The Map Is Not the Territory —The map of reality is not reality itself. If any map were to represent its actual territory with perfect fidelity, it would be the size of the territory itself.
All of these concepts (and six others) can be found in The Great Mental Models Volume 1: General Thinking Concepts.

Add to your Decision-Making Skills
How Not to Be Stupid — Stupidity is overlooking or dismissing conspicuously crucial information. Here are seven situational factors that compromise your cognitive ability and result in increased odds of stupidity.
The Decision Matrix: How to Prioritize What Matters — The decision matrix is a powerful tool to help you prioritize which decisions deserve your attention as a leader, and which should be delegated. Here’s how you can start using it today.
How to Learn How To Think — An argument to spend more time thinking.
The Anatomy of a Decision: An Introduction to Decision Making — A structured process to walk through decisions.
Use a Decision Journal (Example Template) — One reason we struggle to get better at making decisions is that we rarely receive feedback on the quality of our decisions.
A Two-Step Process to Improve Your Thinking — How the smartest people decide.
The Science of Hitting — Ted Williams, one of the best hitters in baseball, knew a lot about making effective decisions.
An Ancient Lesson on Taking Responsibility for Decisions — “A decision is responsible,” wrote Charles Frankel, “when the man or group that makes it has to answer for it to those who are directly or indirectly affected by it.”
When someone says “this time is different,” think very carefully.
If you don’t have deep fluency, you’re in trouble. It’s hard to make decisions based on shallow knowledge.
The Three Filters Needed to Think About Problems — Three filters that help us interpret reality.
How People Make Big Decisions — We all go through psychological steps when we make big decisions.
Make sure you can answer the next question.
Avoiding Stupidity Is Easier than Seeking Brilliance — If you’re an amateur, your focus should be on avoiding stupidity.
Keeping Things Simple and Tuning Out Folly — William James said, “The art of being wise is the art of knowing what to overlook.” No truer words have been spoken.
Your Environment Matters If You Want to Make Better Decisions — It’s hard to make rational decisions the way most of us work.
What Matters More in Decisions: Analysis or Process? — “Our research indicates that, contrary to what one might assume, good analysis in the hands of managers who have good judgment won’t naturally yield good decisions.”
What happens when decisions go wrong? — “When a decision goes awry, we tend to focus on the people who made it, rather than on the decision itself. Our assumption, which is really unwarranted, is that good people make good decisions, and vice versa.”
Books to Improve Decisions
We compiled a list of 39 of the most helpful books on decision making. Here are some of my go-to recommendations:

Judgment and Managerial Decision Making — An academic book that effectively covers heuristics and biases (i.e., how we fool ourselves.) For a non-academic book on the same subject, see Thinking, Fast and Slow by Daniel Kahneman.
Poor Charlies Almanack and Seeking Wisdom — These books cover most of the ways we fool ourselves but add a layer of applied multidisciplinary education.
The Great Mental Models Volume 1: General Thinking Concepts — This volume details nine of the most versatile, all-purpose mental models you can use right away to improve your decision making, productivity, and how clearly you see the world.
 

Endnotes:

1 paraphrased from my friend Peter Kaufmann.
2 See the work of Adam Robinson. ''',

                '4': '''Naval Ravikant: The Angel Philosopher [The Knowledge Project Ep. #18]
In our most popular episode to date, AngelList CEO Naval Ravikant and Shane Parrish break down reading, happiness, decision making, habits, and mental models.


Listen and Learn with The Knowledge Project on iTunes | Youtube | Spotify | Android | Google Play

Naval Ravikant (@naval) is the CEO and co-founder of AngelList. He’s invested in more than 100 companies, including Uber, Twitter, Yammer, and many others.

It’s difficult to nail down exactly what we discuss in our conversation because I had so many questions to ask him. Naval is an incredibly deep thinker who challenges the status quo on so many things. This is an interview you’ll want to listen to, think a bit, and then listen to again.

Here are just a few of the many things we cover in this episode:

What a “typical day” looks like (not the answer I expected, and not one you’ve likely heard before)
How Naval developed his legendary reading habits and how he finds time to read no matter how busy life gets
How the internet has impacted book reading (both good and bad) and how to make sure you’re getting the best information from the most reliable sources
What popular habit advice Naval thinks is BS and why
Naval’s habit stacking technique that helped him overcome a desire for alcohol and other potentially destructive habits
How Naval’s core values give direction to his life and how those values developed over time
Naval’s thoughts on the current education system and what we can do to facilitate better learning for our children
Naval’s favorite mental models for making critical high-stakes decisions
His brilliant two-factor calendar authentication concept to keep him focused on only the most important projects
Naval’s definition for the meaning of life (buckle up for this one)
His amazing response to the investor who wanted to be just like Steve Jobs
And so, so much more.

Just a heads up, this is the longest podcast I’ve ever done. While it felt like only thirty minutes, our conversation lasted over two hours!

And although it is the longest, it’s also our most downloaded episode on the Knowledge Project, so make sure you have a pen and paper handy. There’s a lot of wisdom up for grabs here.

Enjoy this amazing conversation.

Listen
Listen to this episode on Apple Podcasts | YouTube | Spotify
Stream by clicking here
Download as MP3 by right-clicking here and choosing “save as”
Books mentioned
Seven Brief Lessons On Physics
Sapiens: A Brief History of Humankind
The Book of Life
René Girard’s Mimetic Theory
Tools of Titans
Stories of Your Life and Others
Thermoinfocomplexity: A New Theory: Origin of Life and Evolution of Complex Adaptive Systems
Pre-Suasion: A Revolutionary Way to Influence and Persuade
The Lessons of History
The Story of Philosophy
God’s Debris: A Thought Experiment
The Undercover Economist
Feynman, Perfectly Reasonable Deviations
Genius: The Life and Science of Richard Feynman
The Evolution of Everything
The Three-Body Problem
Man’s Search for Meaning
Sex at Dawn: How We Mate, Why We Stray, and What It Means for Modern Relationships
Superintelligence: Paths, Dangers, Strategies
The Art of Manipulation
Thing Explainer
Transcript
Would you like your own hand-edited transcript of this and every other Knowledge Project episode?

If so, consider becoming a Knowledge Project Premium Member. You’ll get exclusive benefits like podcast transcripts to highlight and revisit your favorite insights, behind the scenes commentary, and member-only AMAs with host Shane Parrish.

Your support also allows us to continue to produce high quality shows in the future. Learn more about it here.

Want even more Naval? He’s been chatting on Periscope, and we have edited transcripts [First, Second]. ''',

                '5': '''100 Things I Learned in 10 Years and 100 Reads of Marcus Aurelius’s Meditations
meditations-flat

Almost exactly ten years ago, I bought the Meditations of Marcus Aurelius on Amazon. Amazon Prime didn’t exist then and to qualify for free shipping, I had to purchase a few other books at the same time. Two or three days later they all arrived.



It’s a medium sized paperback, mostly white with a golden spine. On the cover Marcus is shown in relief, pardoning the barbarians. “Here, for our age, is Marcus’s great work,” says Robert Fagles in his blurb. I was 19 years old. I didn’t know who Marcus Aurelius was (besides the old guy in Gladiator) and I certainly didn’t know who Robert Fagles or Gregory Hays, the translator, was. But something drew me to this book almost immediately. I suppose it was luck that brought me to the specific translation I’d chosen (Modern Library Edition)—though the Stoics would call it fated—but what arrived would change my life.

It would be for me, what Tyler Cowen would call a “a quake book,” shaking everything I thought I knew about the world (however little that actually was). I would also become what Stephen Marche has referred to as a “centireader,” reading Marcus Aurelius well over 100 times across multiple editions and copies.

In the course of those readings and my study of Stoicism, a lot has changed. Marcus Aurelius has guided me through breakups and getting married, through being relatively young and poor and relatively older and well-off. His wisdom has helped me with getting fired and with quitting, with success and with struggles. I’ve carried him to close to a dozen countries and moved him to multiple houses. I’ve turned to him for articles and books and casual dinner conversation. The one pristine white cover is now its own shade of tan, but with every read, every time I’ve touched the book, I’ve gotten something new or been reminded of something timeless and important.

Now with the release of my own translation and compendium, The Daily Stoic (and a daily email newsletter at DailyStoic.com), I wanted to take the time to reflect on what I’ve learned in ten years with one of the greatest and most unique pieces of literature ever created.

(And to learn more about Marcus Aurelius and Stoicism, sign up for the Daily Stoic’s free 7-day course on Stoicism packed with exclusive resources, Stoic exercises, interviews and much more!)

meditations-marcus-aurelius

-It was the opening passage of Book 5—about our reluctance to get out of bed and get moving in the morning—that struck me most on my first read. As you can see, I wrote “FUCK” with a highlighter and you can see how important that passage was to me at the time in a 2007 blog post. Later, I would print out this passage and put it next to my desk and bed. I think it was that as a college student I needed that extra motivation. I was a little lazy and entitled. I needed to seize life and take advantage of it—and Marcus served me well in that regard for a long time.

fuck

-Though I will say that today, I think less about the passage that motivates me to do more and be more active. If I was to put a different one on my desk, I’d choose from Book Ten, “If you seek tranquility, do less.”

-In my first read of Meditations, I highlighted the line “It can ruin your life only if it ruins your character.” In a later read I added brackets around that line, just for more emphasis. And I underlined in pen what came after, “Otherwise, it cannot harm you—inside or out.”

-Pages XXVI and XXV of Hays’s introduction is where I was first introduced to the distillation of Stoicism into three distinct disciplines (perception, action, will). It was this order that eventually shaped both The Obstacle is the Way and The Daily Stoic. When I get asked to explain the three disciplines, this is usually my short answer: See things for what they are. Do what we can. Endure and bear what we must.

-Hays’s introduction also lists Alexander Pope, Goethe and William Alexander Percy as students and fans of Marcus Aurelius. Reading works by all of these individuals—especially Percy (and his adopted son, Walker Percy)—sent me down a rabbit hole that would be one of the most enjoyable of my reading life. I encourage everyone to read Percy’s Lanterns on the Levee.

-In Book Four, Marcus reminds himself to think about all the doctors who “died, after furrowing their brows over how many deathbeds, how many astrologers, after pompous forecasts about other’s ends.” In black pen—somewhat recently it looks like—I added “or plotters, schemers and strategists, outsmarted, outmaneuvered and destroyed.” I suppose that was a dig at myself and other smart people. None of what we do lasts, no matter how clever or brilliant. It’s good to remember that.

plotters

-“So we throw out other people’s recognition. What’s left for us to prize?” I answer in blue pen in one read, “To embrace and to resist our nature.” What do I—what did Marcus—mean by that? I think it’s encouraging what is good about us and to fight against what is bad. To encourage the parts of ourselves that are moral, helpful, honest and aware and to fight against what is selfish, petty, shortsighted and wrong. It’s to live by what Warren Buffett calls the “inner scorecard” and ignore the outer one (other people’s recognition).

-In that same passage, Marcus also writes “If you can’t stop prizing a lot of other things? Then you’ll never be free—free, independent, imperturbable.” I have in my copy a jotted note from Fight Club, “Only when you’ve lost everything, you are free to do anything.”

fight-club

-When I first read Meditations, I was in the middle of some ridiculous drama with my college roommates. I won’t bore you with the details, but at the time, I was frustrated, disappointed and miserable about where I was living. I think this was the reason that I latched on the the meditation in Book Six, about how if you were sparring with someone and they hurt you, you wouldn’t yell at them or whine or hold it against them—you’d just make a mental note about it and act accordingly in the future. I can see where I actually wrote the name of my roommates down to explicitly make this connection. “Do not hate them,” I wrote to myself, “remain aloof.”

-I said earlier that all I’d originally known of Marcus Aurelius was that he was the “old guy in Gladiator.” Future research taught me that depiction was even more interesting than the movie presented. First off, Maximus (Russell Crowe’s character) was based on a real Roman story—the general Cincinnatus, who saved Rome but wanted simply to return to his farm. Second, Marcus’s son Commodus (Joaquin Phoenix) was real too—and probably even more horrible in real life. He was in fact, killed by a gladiator and he did enjoy torturing and hurting people. It makes you think: How could such a great man have had such an awful son? What does that say about his teachings?

-Marcus writes “Mastery of reading and writing requires a master. Still, more so life.” I wrote “Tucker, R.G” in the margins next to that passage. R.G stands for Robert Greene—who was and is my master in writing and, more, in life. Tucker refers to Tucker Max, who was a mentor of mine in writing and business. It occurs to me now that I understood this passage only partway—I was focused on the first half, when really the “more so life” line is the most important. Understanding this could have saved me a lot of trouble.

tucker-rg

-In Book Twelve, as Meditations is wrapping up, Marcus writes “It never ceases to amaze me: we all love ourselves more than other people, but care more about their opinion than our own.” This passage struck me early on, I can tell. But it struck me hardest in 2014, when I was re-reading the passage. I know this because I wrote an article with that line as the title, as I was dealing with the fact that my book had just been snubbed by the New York Times Bestseller list and I was dealing with the fallout. It was helpful to ask: Why do I care what these people think again? Why does their opinion matter to me? Understanding the words is not always enough, sometimes we have to really feel them—to have their meaning forced upon us. This was one of those events.

-Going back through my copy to write this post, I found a white notecard with some bullet points written on it. At first I couldn’t figure out what these were about. Then I realized they were notes I’d written down before my conversation with Greg Bishop, a reporter for Sports Illustrated, when he interviewed me for a story he was doing on stoicism and the NFL. One bullet is a line from Arnold Schwarzenegger, “always stronger that we think we know.”

arnold-si

-On what I would guess is my third or fourth read, I marked this passage: “You could leave life right now. Let that determine what you do and say and think.” There are not many reminders of your own mortality at 20. This was one of my first.


-There’s no question that for every first time reader of Meditations, it’s the opening line of Book Two is one of the most striking: “When you wake up in the morning, tell yourself: The people I deal with today will be meddling, ungrateful, arrogant, dishonest, jealous and surly.”

-And then the passage which follows is great—if not a bit contradictory: “Throw away your books; stop letting yourself be distracted.” Did he mean the very book I was reading?

-One of my favorite lines: “To accept without arrogance, to let it go with indifference.” Another translation of the same: “Receive without pride, let go without attachment.”

-In one passage, Marcus justifies his love of art. He points out that tragedies (plays) help remind us of what can happen in life. He also makes an interesting point—“If something gives you pleasure on that stage, it shouldn’t cause you anger on this one.” If you can appreciate it in fiction, you can appreciate it in life—and learn from both.

-In Book Five, I learned what philosophy really was. It’s not an “instructor,” as Marcus put it. It’s not the courses I was taking in school. It is medicine. It’s “a soothing ointment, a warm lotion.” It’s designed to help us deal with the difficulties of life—to heal, as Epicurus said, the suffering of man.

-It wasn’t until last week, re-reading Marcus that I noticed the word “stillness” as it appears in Book Six, 7: “To move from one unselfish action to another with God in mind. Only there, delight and stillness.” Stillness was something I had been thinking about a lot—how to find it, how to get it, why it’s superior to activity. I was looking for it in Eastern texts and here it has been in Stoicism the entire time.

-Book Nine, 6 I found not only a potential epigraph for my book The Obstacle is the Way (which I noted in blue pen in 2013) but the best possible summation of Stoicism there is:

“Objective judgement, now, at this very moment.

Unselfish action, now, at this very moment.

Willing acceptance—now, at this very moment—of all external events.

That’s all you need.”

-At some point after I read the Hays translation, I picked up another translation of Marcus—probably one by George Long or A. S. L. Farquharson, that was free online. I was immediately struck by how the beautiful, lyrical book I loved had become dense and unreadable. It struck me that if I had cheaped out and tried to get for free what I’d bought instead, my entire life might have turned out differently. Books are investments. Be glad to put in your money.

-Marcus has a wonderful phrase for the approval and cheering of other people. He calls it “the clacking of tongues”—that’s all public appraise is, he says. Anyone that works in the public eye, who puts their work or their life out there for consumption, could use to remember this phrase.

–“Often injustice lies in what you aren’t doing, not only in what you are doing.” Or, as we say more modernly, ‘The only thing required for the triumph of evil is for good men to do nothing…’

-Don’t try to get even with other people, Marcus says at one point. Just don’t be like that.

-“The student as a boxer, not a fencer.” Why? Because the fencer has a weapon they must pick up. A boxer’s weapons are a part of him, he and the weapon are one. Same goes for knowledge, philosophy and wisdom.

meditations-flat

-Marcus commands himself to winnow his thoughts. He has a great standard. If someone were to ask you right now, “What are you thinking about?” could you give a concise answer? If not, you’re daydreaming and wandering too much.

-“It stares you right in the face,” Marcus writes. “No role is so well suited to philosophy as the one you happen to be in right now.” Was he referring specifically to the role of emperor? Did he mean that any and every role is the perfect one for philosophy? I prefer to think it is the latter.

-I’ve been lucky enough that some generous fans have sent me rare old copies of Meditations. They’re falling apart, worn with age. It strikes me what a Stoic would have thought if given a book that was then a couple hundred years old. They’d think about the person who owned it and what became of them (dead), they’d think about all the things the person did other than study philosophy (mostly pointless stuff), and they’d also think of the difficult times that the wisdom contained within may have helped them (which is what I think now). And then they’d consider how we are all subject to the rhythm of events and that someone may pick up this book after them and have the same thoughts.

meditations-old-editions

-Going through one copy of the Hays translation a few years ago, I found a receipt. It said January 2007 and it was from a Borders in Riverside, California. I’d bought mine on Amazon, so I knew it wasn’t mine. Then I realized, this was my wife’s copy. She’d bought the book shortly after we’d met, on my recommendation. That she’d read it after I mentioned it in passing, made me think our feelings might be mutual. It was one of the first things we’d connected over. Ten years later we are still together.

-In Gregory Hays’s intro he says that “an American president” claims to re-read Marcus Aurelius every year. Some research turned up that Bill Clinton was that president. Was that where I got the idea to keep reading and re-reading the book? To use it as a reminder of all the lessons that success would bring?

-Absolute power corrupts absolutely is what we say. But Marcus had absolute power. To me, his writing and his life are proof that the right principles and the right discipline—if followed rigorously—can help buck this timeless trend.

-Marcus reminded himself: “Don’t await the perfection of Plato’s Republic.” He wasn’t expecting the world to be exactly the way he wanted it to be, but Marcus knew instinctively, as the Catholic philosopher Josef Pieper would later write, that “he alone can do good who knows what things are like and what their situation is.”

-It’s funny to think that his writings may be as special as they are because they were never intended for us to be read. Almost every other piece of literature is a kind of performance—it’s made for the audience. Meditations isn’t. In fact, their original title (Ta eis heauton) roughly translates as To Himself.

-It’s also interesting to think that we have no idea if the meditations were once ordered differently. All we have now are translations of translations—no original writing from his hand survives. It all could have been arranged in an entirely different format originally (Did all the books have titles originally—as the first two do? Are those titles made up? Were they all numbered originally? Or were even the breaks between thoughts added in by a later translator?)

-Who hasn’t used the expressions “I’ll be honest with you” or “With all due respect” or “I’ll be straight with you.” It wasn’t until I read Marcus’s specific condemnation of these phrases that I really thought about what they were saying—honesty, respect, straightforwardness should be the default. If you have to specifically preface your remarks with it, that’s a sign something is wrong with your normal speech and your normal habits.

-“But if you accept the obstacle and work with what you’re given, an alternative will present itself—another piece of what you’re trying to assemble. Action by action.” There’s no question that we’re going to be stopped from what we’d like to do, or even desperately need to do from time to time. Money will be lost. Plans will be frustrated. Long held dreams will be broken. People (including us) will be hurt. And yet, as bad as these situations are and will be, I think you’ll have to admit, they don’t prevent everything. You can still practice honesty, forgiveness, friendship, patience, humility, good spirit, resilience, creativity, and on and on.

-It must have been many reads in before I came to understand that many of the admonishments—Don’t waste time, Don’t lose your temper, Stop getting caught up in things that don’t matter—must be there because Marcus had recently done the exact opposite. Remember, this was essentially his journal, the meditations are reflections written after a long hard day. They are not abstractions, they are notes on what he can do better next time.

meditations-lake-2

-There is a line in Joseph Brodsky’s essay about the famous equestrian statue of Marcus Aurelius (which I went to Rome a few years ago to see). “If Meditations is antiquity,” he says, “then it is we who are the ruins.” What I think he means by that is that when you compare the strength and power and rigorous self-honesty of Marcus’s writings to now, all you can feel is a sense of decay. It feels like we have regressed instead of progressed.

-A great rhetorical exercise from Marcus goes essentially like this: “Is a world without shameless people possible? No. So this person you’ve just met is one of them. Get over it.” It’s a good thing to remember every time you meet someone who frustrates or bothers you.

-One of the benefits of reading a book so many times is that it starts to feel like it’s following you everywhere. It’s like when you get a new car and all of a sudden you start seeing that car everywhere—it’s like you and those drivers are suddenly on the same time. I remember reading East of Eden shortly after Meditations, and guess who is quoted everywhere? Then I read John Stuart Mill, and Marcus appeared again. Then on a trip to New York City I was walking up 41 St and there’s a plaque with a quote from Marcus. It’s one of the most amazing feelings, you find the thread of the work everywhere and it’s like you’re both on the same team, with the same message to propagate.

-One of the most practical things I’ve learned from the Stoics is an exercise I’ve come to call “contemptuous expressions.” I love how Marcus would take fancy things and describe them in almost cynical, dismissive language—roasted meat is a dead animal and vintage wine is old, fermented grapes. He even describes the Emperor’s purple cloak as just a piece of fabric dyed with shellfish blood. The aim was to see these things as they really are, to “strip away the legend that encrusts them.” I try to use this exercise every day.

-The short lines are the best:

 

“Discard your misperceptions.

Stop being jerked like a puppet.

Limit yourself to the present.”

 

-Imagine the emperor of Rome, with his captive audience and unlimited power, telling himself not to be a person of “too many words and too many deeds.” How great is that? How inspiring?

-It wasn’t until working with Steve Hanselman on the translations in The Daily Stoic that I was made aware of just how malleable translation was. I assumed that Hays was capturing the inherent beauty in Marcus. In some sense he was, but he was also choosing to write beautifully—someone could just as easily decide to be blunt and literal. It gave me a new appreciation for the art of translation—and how much room for interpretation there is in all of it.

-If there was one translation I would love to read it would be the late Pierre Hadot’s. In his excellent book The Inner Citadel about Marcus Aurelius and Stoicism, Hadot did original translations for the passages he quotes—but sadly he died without publishing a full translation of Marcus for wider consumption.

-It was in reading Hadot that I first got an explicit explanation of what he calls “turning obstacles upside down.” I’d obviously read the original passage he quotes several times in Hays, but Hadot’s translation was different, it made it clearer. The original title of my book was “Turning Obstacles Upside Down.” It was only in reading The Dictionary of Modern Proverbs that I found the Zen saying, “The obstacle is the path” that I was able to combine it all and come up with the book.

-“Everything lasts for a day, the one who remembers and the remembered.” That means something special coming from a guy whose face you can still see on Roman coins you can buy on Etsy.

-From Marcus I learned who Heraclitus was (Marcus quotes him a lot). “No man steps in the same river twice,” is one of the line he quotes. What a beautiful idea. I loved it so much that when I was in college I added a special “Quote of the Week” section to the student newspaper—just so I could use it.

-After I read Marcus, I immediately read Epictetus (Lebell’s The Art of Living translation), then Seneca’s Letters from a Stoic, then back to the Penguin translation of Epictetus, then Seneca’s On The Shortness of Life. It’s been a ten year journey now, and I still feel like I am at the very beginning of it. Or at least, there is so much further left to go.

-How crazy is it that not only does Marcus’s “journal” survive to us, so do the letters between him and his rhetoric teacher, Cornelius Fronto? The Stoics might say that such an event was “fated” but I’d say we are incredibly lucky that chance did not destroy these documents and deprive humanity of them.

–Marcus talks about the logos—essentially the force of the universe—repeatedly. That word seemed familiar to me when I first read it. Then I made the connection, Viktor Frankl, the psychologist and Holocaust survivor named his school of psychology logotherapy.

-Still, I was a bit confused as to what the logos was. Hays—and many writers—have used the analogy of a dog tied to a cart to explain our connection to the logos. The cart (the logos) is moving and we are pulled behind it. We have a little slack to move here and there, but not much.

-I think instinctively at 19 years old, I rejected this idea. Predetermination? No free will? Please. That sounded religious. College kids are often attracted to atheism for precisely the freedom and empowerment it implies. But as I have gotten older, I’ve started to understand how much we are shaped by chance and forces beyond our control. It strikes me, then, that the debate is not whether we are in fact the dog tied to the moving cart but rather, just how long the rope is? How much room to we have to explore and determine our own pace? A lot? A little?

logos

-Marcus’s Meditations are filled with self-criticism. It’s important to remember, however, that that’s as far as it goes. There was no self-flagellation, no paying penance, no self-esteem issues from guilt or self-loathing. This self-criticism is constructive.

-There is a passage is Marcus where he talks about sitting next to a smelly, rude person. It must have been just a couple months after I first read that that I was on a flight from Long Beach to New York. I was stuck in the middle seat. The person next to me was horrible. They were imposing in my space. They were being obnoxious. I was stewing. Then this hit me: Either I say something or I let it go. All the anger left me. I went back to what I was doing. I probably think of that line every other time I get on a plane now.

-As a reminder of the man and the principles in the book, I ended up buying a marble bust of Marcus carved in 1840 that sits on my desk where I can see it daily. It’s probably the most expensive piece of “art” I own—it cost $900. But for the reminders it’s given me and the calming presence it has had, it’s worth every penny. To think that 3 or 4 generations of people may have owned this thing. That someone will own it after I die.

-Years later, one of my readers created and sent me two 3D printed busts of both Marcus and Seneca which sit in my library. They’re a lot cheaper and they weigh a lot less but they have the same impact.

-I set out to learn everything I could about Marcus Aurelius. At one point, I found an old academic paper that suggested Marcus’s writing was shaped by an addiction to opium—why else would have written down extended, cerebral reflections about spinning away from the earth and looking at things from far above? The answer is because this is a Stoic exercise that goes back thousands of years (and in fact, has also been observed by astronauts thousands of years later). All the things that people do hallucinogens to explore, you can also do while sober as a judge. It just takes work.

-Explicitly setting standards for himself in Book 10, Marcus extolls himself to be: “Upright. Modest. Straightforward. Sane. Cooperative. Disinterested.” In a blog post in 2007, I added the following for myself: Empathetic. Open. Diligent. Ambitious.

-I wrote a piece about Peter Thiel’s long campaign for revenge against Gawker earlier this year. As I was writing it, a line from Marcus came rushing back from the recesses of my memory: “The best way to avenge yourself is to not be like that.”

-In writing The Daily Stoic, I got to parse the words of Marcus Aurelius (and his translators) in ways I otherwise never would have done. I’ve always liked the line, “How trivial the things we want so passionately are.” In my initial readings, I’d always thought it was beautiful the way he was saying “passionately are.” Upon later reflection, I realized Hays/Aurelius were saying “the things are want so passionately, are” which has its own beauty.

-You also come to realize and understand the deeper historical references. For instance, in one passage, Marcus writes “To escape imperialization, that indelible stain.” I know, obviously, what “imperialism” and “imperial” mean but it wasn’t until many reads later that I came to understand he meant to escape the trappings of his office. He was saying: I must avoid being changed and corrupted by my office. Not all of us hold executive power, but we all can use that advice.

-When translating for The Daily Stoic, our editor asked about a line where Marcus says “enough of this whiny, miserable life. Stop monkeying around!” Would Marcus have ever seen a monkey, she asked? Or is this a modern line? Of course he would have! In fact, his psychopathic son probably killed a bunch of them in the coliseum. Marcus supposedly hated the gladiatorial games but he definitely would have been familiar with a shocking amount of African wildlife.

-Another interesting factoid about Marcus—proof, I think that he lived his philosophy. He was selected for the throne by Hadrian who set in line a succession plan that involved Hadrian adopting the elderly Antoninus Pius who in turn adopted Marcus Aurelius. When Marcus eventually ascended to the throne, what was his first decision? He appointed his step-brother Lucius Verus co-emperor. He was given unlimited, executive power and the first thing he did was share it with someone he was not even technically related to? That’s magnanimity.

-His advice on change is amazing. We’re like rocks—we gain nothing by going up and lose nothing by coming back down.

-“Don’t allow yourself to be heard any longer griping about public life, not even with your own ears!” You chose this life, he is telling himself, and that means you don’t get to complain about it.

-I was lucky enough to interview Gregory Hays in 2007. I asked him what his favorite passage was. He quoted: “Keep in mind how fast things pass by and are gone–those that are now and those to come. Existence flows past us like a river: the ‘what’ is in constant flux, the ‘why’ has a thousand variations. Nothing is stable, not even what’s right here. The infinity of past and future gapes before us—a chasm whose depths we cannot see.” I have to admit I missed the brilliance of that one the first time, but it’s stuck with me ever since.

-Did you know that Ambrose Bierce, the amazing Civil War-era writer and Mark Twain contemporary, was a big fan of the Stoics? Clearly his grandparents were too since his father was named Marcus Aurelius Bierce and his uncle, Lucius Verus Bierce (Marcus’s step brother and co-emperor).

-When I interviewed Robert Greene for The Daily Stoic’s companion website, I was surprised to hear he also loved the passage about “seeing roasted meat and other dishes in front of you and suddenly realizing: This is a dead fish. A dead bird. A dead pig.” As he explained to me: “I’ve tried to bring that across in my writing. For instance, to deconstruct things like power and seduction and to see the actual elements in play instead of the legends surrounding them.”

-During our interview he actually showed me his own copy of the Meditations and could remember the camping trip when he had written all the notes on the pages. On several of them he had marked AF in the marginalia, a shorthand for amor fati—a love of one’s fate. As he explained the idea, “Stop wishing for something else to happen, for a different fate. That is to live a false life.”

-The best way to learn and to lead is by example. I think that’s why I liked Marcus’s book so much—he was showing me (us) what is possible. As he put it “Nothing is as encouraging as when virtues are visibly embodied in the people around us, when we’re practically showered with them.”

-In my own education I’ve always followed Marcus’s dictum to “go straight to the seat of intelligence—your own, the world’s, your neighbors.” He also writes that learning to read and write requires a master—and so does the art of life. To me, people like Robert Greene were that master and so were people like Marcus. You have to go straight to the sources of knowledge and absorb what you can from them.

-During one of his most dangerous and threatening adventures, the journey down the “River of Doubt,” Teddy Roosevelt carried with him a copy of Meditations. I would kill to flip through his copy! Did he sit down at night and read few pages? Are there interesting notes in the margins? What were his favorite passages? A more Stoic question: How many other famous or important men and women have sat down with a copy of Marcus? And where are they now? Gone and mostly forgotten.

-In my work with bestselling authors and creatives there is one line from Marcus that I am often tempted to quote: “Ambition,” he reminded himself, “means tying your well-being to what other people say or do…Sanity means tying it to your own actions.” Doing good work is what matters. Recognition and rewards—those are just extra. To be too attached to results you don’t control? That’s a recipe for misery.

-Despite his privileges, Marcus Aurelius had a difficult life. The Roman historian Cassius Dio mused that Marcus “did not meet with the good fortune that he deserved, for he was not strong in body and was involved in a multitude of troubles throughout practically his entire reign.” But throughout these struggles he never gave up. It’s an inspiring example for us to think about today if we get tired, frustrated, or have to deal with some crisis.

-From the Stoics, I learned about the concept of the Inner Citadel. It is this fortress, they believed, that protects our soul. Though we might be physically vulnerable, though we might be at the mercy of fate in many ways, our inner domain is impenetrable. As Marcus put it (repeatedly, in fact), “stuff cannot touch the soul.”

-Right after the 2008 presidential elections, I remember connecting Obama’s “teachable moment” about the Reverend Wright scandal and how it illustrated Marcus’s principle of turning the obstacle upside down. As Obama put it, turning the negative situation into the perfect platform for his landmark speech about race, he would be “missing an important opportunity for leadership.” It’s something I try to think about in my own life as a boss and as a soon-to-be-father.

-Bill Belichick tells his players: “Do your job.” Marcus makes it clear what that job is: “What is your vocation? To be a good person.”

-Marcus is a beautiful writer, capable of finding beauty in strange places. In one passage, he praises the “charm and allure” of nature’s process, the “stalks of ripe grain bending low, the frowning brow of the lion, the foam dripping from the boar’s mouth.” As a writer, I’ve learned a lot from this skill of his. As a person, I’ve learned more. It’s about looking for majesty everywhere and anywhere.

-At one point Marcus tells himself to “Avoid false friendship at all costs.” I think he’s right, but we can take it a step further: What if, instead, we ask about the times that we have been false to our friends?

-Marcus constantly points out how the emperors who came before him were barely remembered just a few years later. To him, this was a reminder that no matter how much he conquered, no matter how much he inflicted his will on the world, it would be like building a castle in the sand—soon to be erased by the winds of time. The same is true for us.

-It’s interesting how much of Meditations is made up of short quotes and passages from other writers. In a way, it’s really Marcus’s commonplace book (and he’s inspired me to keep my own). One of my favorites is Marcus quoting a lost line from Euripides: “You shouldn’t give circumstances the power to rouse anger, for they don’t care at all.”

-I’ve talked a little bit about my tendency to overwork and to compulsively do. Marcus has a good reminder: “In your actions, don’t procrastinate. In your conversations, don’t confuse. In your thoughts, don’t wander. In your soul, don’t be passive or aggressive. In your life, don’t be all about business.”

-Marcus was one of the first writers to articulate the notion of cosmopolitanism—saying that he was a citizen of the world, not just of Rome. Which is an interesting and impressive thought…considering his job was as the first citizen of Rome.

-Marcus had many responsibilities, as those who hold executive power do. He judged cases, heard appeals, sent troops into battle, appointed administrators, approved budgets. A lot rode on his choices and actions. He wrote this reminder to himself which beautifully illustrates the kind of man he was: “Never shirk the proper dispatch of your duty, no matter if you are freezing or hot, groggy or well-rested, vilified or praised, not even if dying or pressed by other demands.”

-In the first book of Meditations, Marcus thanks Rusticus for teaching him “to read carefully and not be satisfied with a rough understanding of the whole, and not to agree too quickly with those who have a lot to say about something.” It’s a reminder for us in this busy media world of liars and bullshit artists. Don’t be satisfied with the superficial impression. Don’t be reactive. Know.

-How was Marcus introduced to the Stoics? We’re not quite sure but we do know that he got his copy of Epictetus from Rusticus (and in fact, Rusticus may have provided him his own notes from attending Epictetus’s lectures). A number of my favorite books came to me from my teachers. In fact, I was introduced to the Stoics by asking Dr. Drew for a book recommendation. Who did he recommend? Epictetus.

-Marcus writes, “Don’t lament this and don’t get agitated.” It calls to mind the motto of another statesman, the British prime minister Benjamin Disraeli: “Never complain, never explain.”

-Long before modern discussions of self-talk, Marcus understood the notion: “Your mind will take the shape of what you frequently hold in thought.”

-At one point, Marcus essentially says to not ever do anything that we would be worried might remain ‘behind closed doors.’ It’s easy to say, but hard to do. Who wouldn’t be embarrassed if their email account was leaked or if a fight with their spouse was made public? We all do things in private that we would never do in front of other people. Which is a good thought/test to evaluate our behavior before we embark on something.

-In Book Six we find one of the strongest encouragements that Marcus gives himself. He says, basically: If someone else has done it—then it is humanly possible. If it’s humanly possible, then of course you can do it too.

-I’ve found over the years that jealousy is a toxic emotion. We want so desperately what others have that we lose the pleasure of the things we already have. Marcus provides a solution: “Don’t set your mind on things you don’t possess…, but count the blessings you actually possess and think how much you would desire them if they weren’t already yours.”

-Repeatedly Marcus warns himself that anger and grief only serve to make bad situations worse. Being pissed off that someone was rude to you isn’t soothing—it’s agitating. Being sad that you’ve lost something doesn’t bring it back, it exaggerates your sense of loss. It’s like the first rule of holes: When you’re in one, stop digging.

-When I was on the Tim Ferriss podcast this summer I learned that he had one of my favorite quotes from Marcus taped to his fridge: “When jarred, unavoidably, by circumstance, revert at once to yourself, and don’t lose the rhythm more than you can help. You’ll have a better grasp of the harmony if you keep going back to it.”

-What is tragic about Marcus, as one scholar wrote, is how his “philosophy—which is about self-restraint, duty, and respect for others—was so abjectly abandoned by the imperial line he anointed on his death.” As I said, Marcus’s terrible son, is an important reminder that it doesn’t matter how good you are at your job, if you neglect your duties at home…

-“We are what we repeatedly do,” Aristotle said, “therefore, excellence is not an act but a habit.” The Stoics add to that that we are a product of our thoughts (“Such as are your habitual thoughts, such also will be the character of your mind,” is how Marcus put it).

-Marcus consistently admonishes himself to return to the present moment and focus on what’s in front of him. This idea of being “present” seems very Eastern but of course it’s central to Stoicism too. “Stick with the situation at hand,” he tells himself, “and ask, “Why is this so unbearable? Why can’t I endure it?” You’ll be embarrassed to answer.” Yup.

-In Meditations we find one of the most helpful exercises when seeking perspective: “Run down the list of those who felt intense anger at something: the most famous, the most unfortunate, the most hated, the most whatever: Where is all that now? Smoke, dust, legend…or not even a legend.” Eventually, all of us will pass away and slowly be forgotten. We should enjoy this brief time we have on earth—not be enslaved to emotions that make us miserable and dissatisfied.

**

I’ll leave you with one final lesson, in fact, it’s the lesson we chose to close The Daily Stoic with. Marcus was clearly a big reader, he clearly took copious notes and studied philosophy deeply. Yet he took the unusual step of reminding himself to put all that aside.

“Stop wandering about!” he wrote. “You aren’t likely to read your own notebooks, or ancient histories, or the anthologies you’ve collected to enjoy in your old age. Get busy with life’s purpose, toss aside empty hopes, get active in your own rescue—if you care for yourself at all—and do it while you can.”

At some point, we must stop our reading, put all the advice from Marcus and the other stoics aside and take action. So that, as Seneca put it, the “words become works.”

That’s what I have tried to do over the last ten years. To alternate between the reading and the doing. I’m not perfect at it. I’m not even as far along as I’d like to be. But I am making progress.

I hope you are too. ''',

                '6': '''What Makes You You?
 December 12, 2014 By Tim Urban

Note: If you want to print this post or read it offline, the PDF is probably the way to go. You can buy it here.
When you say the word “me,” you probably feel pretty clear about what that means. It’s one of the things you’re clearest on in the whole world—something you’ve understood since you were a year old. You might be working on the question, “Who am I?” but what you’re figuring out is the who am part of the question—the I part is obvious. It’s just you. Easy.

But when you stop and actually think about it for a minute—about what “me” really boils down to at its core—things start to get pretty weird. Let’s give it a try.

The Body Theory

We’ll start with the first thing most people equate with what a person is—the physical body itself. The Body Theory says that that’s what makes you you. And that would make sense. It doesn’t matter what’s happening in your life—if your body stops working, you die. If Mark goes through something traumatic and his family says, CH“It really changed him—he’s just not the same person anymore,” they don’t literally mean Mark isn’t the same person—he’s changed, but he’s still Mark, because Mark’s body is Mark, no matter what he’s acting like. Humans believe they’re so much more than a hunk of flesh and bone, but in the end, a physical ant is the ant, a squirrel’s body is the squirrel, and a human is its body. This is the Body Theory—let’s test it:

So what happens when you cut your fingernails? You’re changing your body, severing some of its atoms from the whole. Does that mean you’re not you anymore? Definitely not—you’re still you.

How about if you get a liver transplant? Bigger deal, but definitely still you, right?

What if you get a terrible disease and need to replace your liver, kidney, heart, lungs, blood, and facial tissue with synthetic parts, but after all the surgery, you’re fine and can live your life normally. Would your family say that you had died because most of your physical body was gone? No, they wouldn’t. You’d still be you. None of that is needed for you to be you.

Well maybe it’s your DNA? Maybe that’s the core thing that makes you you, and none of these organ transplants matter because your remaining cells all still contain your DNA, and they’re what maintains “you.” One major problem—identical twins have identical DNA, and they’re not the same person. You are you, and your identical twin is most certainly not you. DNA isn’t the answer.

So far, the Body Theory isn’t looking too good. We keep changing major parts of the body, and you keep being you.

But how about your brain?

The Brain Theory

Let’s say a mad scientist captures both you and Bill Clinton and locks the two of you up in a room.

CH

The scientist then performs an operation on both of you, whereby he safely removes each of your brains and switches them into the other’s head. Then he seals up your skulls and wakes you both up. You look down and you’re in a totally different body—Bill Clinton’s body. And across the room, you see your body—with Bill Clinton’s personality.

CFO

Now, are you still you? Well, my intuition says that you’re you—you still have your exact personality and all your memories—you’re just in Bill Clinton’s body now. You’d go find your family to explain what happened:

CF1

CF2

So unlike your other organs, which could be transplanted without changing your identity, when you swapped brains, it wasn’t a brain transplant—it was a body transplant. You’d still feel like you, just with a different body. Meanwhile, your old body would not be you—it would be Bill Clinton. So what makes you you must be your brain. The Brain Theory says that wherever the brain goes, you go—even if it goes into someone else’s skull.

The Data Theory

Consider this—

What if the mad scientist, after capturing you and Bill Clinton, instead of swapping your physical brains, just hooks up a computer to each of your brains, copies every single bit of data in each one, then wipes both of your brains completely clean, and then copies each of your brain data onto the other person’s physical brain? So you both wake up, both with your own physical brains in your head, but you’re not in your body—you’re in Bill Clinton’s body. After all, Bill Clinton’s brain now has all of your thoughts, memories, fears, hopes, dreams, emotions, and personality. The body and brain of Bill Clinton would still run out and go freak out about this to your family. And again, after a significant amount of convincing, they would indeed accept that you were alive, just in Bill Clinton’s body.

Philosopher John Locke’s memory theory of personal identity suggests that what makes you you is your memory of your experiences. Under Locke’s definition of you, the new Bill Clinton in this latest example is you, despite not containing any part of your physical body, not even your brain. 

This suggests a new theory we’ll call The Data Theory, which says that you’re not your physical body at all. Maybe what makes you you is your brain’s data—your memories and your personality.

We seem to be homing in on something, but the best way to get to concrete answers is by testing these theories in hypothetical scenarios. Here’s an interesting one, conceived by British philosopher Bernard Williams:

The Torture Test

Situation 1: The mad scientist kidnaps you and Clinton, switches your brain data with Clinton’s, as in the latest example, wakes you both up, and then walks over to the body of Clinton, where you supposedly reside, and says, “I’m now going to horribly torture one of you—which one should I torture?”

What’s your instinct? Mine is to point at my old body, where I no longer reside, and say, “Him.” And if I believe in the Data Theory, then I’ve made a good choice. My brain data is in Clinton’s body, so I’m now in Clinton’s body, so who cares about my body anymore? Sure, it sucks for anyone to be tortured, but if it’s between me and Bill Clinton, I’m choosing him.

Situation 2: The mad scientist captures you and Clinton, except he doesn’t do anything to your brains yet. He comes over to you—normal you with your normal brain and body—and asks you a series of questions. Here’s how I think it would play out:

Mad Scientist: Okay so here’s what’s happening. I’m gonna torture one of you. Who should I torture?

You: [pointing at Clinton] Him.

MS: Okay but there’s something else—before I torture whoever I torture, I’m going to wipe both of your brains of all memories, so when the torture is happening, neither of you will remember who you were before this. Does that change your choice?

You: Nope. Torture him.

MS: One more thing—before the torture happens, not only am I going to wipe your brains clean, I’m going to build new circuitry into your brain that will convince you that you’re Bill Clinton. By the time I’m done, you’ll think you’re Bill Clinton and you’ll have all of his memories and his full personality and anything else that he thinks or feels or knows. I’ll do the same thing to him, convincing him he’s you. Does that change your choice?

You: Um, no. Regardless of any delusion I’m going through and no matter who I think I am, I don’t want to go through the horrible pain of being tortured. Insane people still feel pain. Torture him.

So in the first situation, I think you’d choose to have your own body tortured. But in the second, I think you’d choose Bill Clinton’s body—at least I would. But the thing is—they’re the exact same example. In both cases, before any torture happens, Clinton’s brain ends up with all of your data and your brain has his—the difference is just at which point in the process you were asked to decide. In both cases, your goal is for you to not be tortured, but in the first situation, you felt that after the brain data swap, you were in Clinton’s body, with all of your personality and memories there with you—while in the second situation, if you’re like me, you didn’t care what was going to happen with the two brains’ data, you believed that you would remain with your physical brain, and body, either way.

Choosing your body to be the one tortured in the first situation is an argument for the Data Theory—you believe that where your data goes, you go. Choosing Clinton’s body to be tortured in the second situation is an argument for the Brain Theory, because you believe that regardless of what he does with your brain’s data, you will continue to be in your own body, because that’s where your physical brain is. Some might even take it a step further, and if the mad scientist told you he was even going to switch your physical brains, you’d still choose Clinton’s body, with your brain in it, to be tortured. Those that would torture a body with their own brain in it over torturing their own body believe in the Body Theory.

Not sure about you, but I’m finishing this experiment still divided. Let’s try another. Here’s my version of modern philosopher Derek Parfit’s teletransporter thought experiment, which he first described in his book Reasons and Persons—

The Teletransporter Thought Experiment

It’s the year 2700. The human race has invented all kinds of technology unimaginable in today’s world. One of these technologies is teleportation—the ability to transport yourself to distant places at the speed of light. Here’s how it works—

You go into a Departure Chamber—a little room the size of a small cubicle.

cube stand

You set your location—let’s say you’re in Boston and your destination is London—and when you’re ready to go, you press the button on the wall. The chamber walls then scan your entire body, uploading the exact molecular makeup of your body—every atom that makes up every part of you and its precise location—and as it scans, it destroys, so every cell in your body is destroyed by the scanner as it goes.

cube beam

When it’s finished (the Departure Chamber is now empty after destroying all of your cells), it beams your body’s information to an Arrival Chamber in London, which has all the necessary atoms waiting there ready to go. The Arrival Chamber uses the data to re-form your entire body with its storage of atoms, and when it’s finished you walk out of the chamber in London looking and feeling exactly how you did back in Boston—you’re in the same mood, you’re hungry just like you were before, you even have the same paper cut on your thumb you got that morning.

The whole process, from the time you hit the button in the Departure Chamber to when you walk out of the Arrival Chamber in London, takes five minutes—but to you it feels instantaneous. You hit the button, things go black for a blink, and now you’re standing in London. Cool, right?

In 2700, this is common technology. Everyone you know travels by teleportation. In addition to the convenience of speed, it’s incredibly safe—no one has ever gotten hurt doing it.

But then one day, you head into the Departure Chamber in Boston for your normal morning commute to your job in London, you press the big button on the wall, and you hear the scanner turn on, but it doesn’t work.

cubicle broken

The normal split-second blackout never happens, and when you walk out of the chamber, sure enough, you’re still in Boston. You head to the check-in counter and tell the woman working there that the Departure Chamber is broken, and you ask her if there’s another one you can use, since you have an early meeting and don’t want to be late.

She looks down at her records and says, “Hm—it looks like the scanner worked and collected its data just fine, but the cell destroyer that usually works in conjunction with the scanner has malfunctioned.”

“No,” you explain, “it couldn’t have worked, because I’m still here. And I’m late for this meeting—can you please set me up with a new Departure Chamber?”

She pulls up a video screen and says, “No, it did work—see? There you are in London—it looks like you’re gonna be right on time for your meeting.” She shows you the screen, and you see yourself walking on the street in London.

“But that can’t be me,” you say, “because I’m still here.”

At that point, her supervisor comes into the room and explains that she’s correct—the scanner worked as normal and you’re in London as planned. The only thing that didn’t work was the cell destroyer in the Departure Chamber here in Boston. “It’s not a problem, though,” he tells you, “we can just set you up in another chamber and activate its cell destroyer and finish the job.”

And even though this isn’t anything that wasn’t going to happen before—in fact, you have your cells destroyed twice every day—suddenly, you’re horrified at the prospect.

“Wait—no—I don’t want to do that—I’ll die.”

The supervisor explains, “You won’t die sir. You just saw yourself in London—you’re alive and well.”

“But that’s not me. That’s a replica of me—an imposter. I’m the real me—you can’t destroy my cells!”

The supervisor and the woman glance awkwardly at each other. “I’m really sorry sir—but we’re obligated by law to destroy your cells. We’re not allowed to form the body of a person in an Arrival Chamber without destroying the body’s cells in a Departure Chamber.”

You stare at them in disbelief and then run for the door. Two security guards come out and grab you. They drag you toward a chamber that will destroy your cells, as you kick and scream…

__________

If you’re like me, in the first part of that story, you were pretty into the idea of teletransportation, and by the end, you were not.

The question the story poses is, “Is teletransportation, as described in this experiment, a form of traveling? Or a form of dying?

This question might have been ambiguous when I first described it—it might have even felt like a perfectly safe way of traveling—but by the end, it felt much more like a form of dying. Which means that every day when you commute to work from Boston to London, you’re killed by the cell destroyer, and a replica of you is created.1 To the people who know you, you survive teletransportation just fine, the same way your wife seems just fine when she arrives home to you after her own teletransportation, talking about her day and discussing plans for next week. But is it possible that your wife was actually killed that day, and the person you’re kissing now was just created a few minutes ago?

Well again, it depends on what you are. Someone who believes in the Data Theory would posit that London you is you as much as Boston you, and that teletransportation is perfectly survivable. But we all related to Boston you’s terror at the end there—could anyone really believe that he should be fine with being obliterated just because his data is safe and alive over in London? Further, if the teletransporter could beam your data to London for reassembly, couldn’t it also beam it to 50 other cities and create 50 new versions of you? You’d be hard-pressed to argue that those were all you. To me, the teletransporter experiment is a big strike against the Data Theory.

Similarly, if there were an Ego Theory that suggests that you are simply your ego, the teletransporter does away nicely with that. Thinking about London Tim, I realize that “Tim Urban” surviving means nothing to me. The fact that my replica in London will stay friends with my friends, keep Wait But Why going with his Tuesday-ish posts, and live out the whole life I was planning for myself—the fact that no one will miss me or even realize that I’m dead, the same way in the story you never felt like you lost your wife—does almost nothing for me. I don’t care about Tim Urban surviving. I care about me surviving.

All of this seems like very good news for Body Theory and Brain Theory. But let’s not judge things yet. Here’s another experiment:

The Split Brain Experiment

A cool fact about the human brain is that the left and right hemispheres function as their own little worlds, each with their own things to worry about, but if you remove one half of someone’s brain, they can sometimes not only survive, but their remaining brain half can learn to do many of the other half’s previous jobs, allowing the person to live a normal life. That’s right—you could lose half of your brain and potentially function normally.

So say you have an identical twin sibling named Bob who develops a fatal brain defect. You decide to save him by giving him half of your brain. Doctors operate on both of you, discarding his brain and replacing it with half of yours. When you wake up, you feel normal and like yourself. Your twin (who already has your identical DNA because you’re twins) wakes up with your exact personality and memories.

twins

When you realize this, you panic for a minute that your twin now knows all of your innermost thoughts and feelings on absolutely everything, and you’re about to make him promise not to tell anyone, when it hits you that you of course don’t have to tell him. He’s not your twin—he’s you. He’s just as intent on your privacy as you are, because it’s his privacy too.

As you look over at the guy who used to be Bob and watch him freak out that he’s in Bob’s body now instead of his own, you wonder, “Why did I stay in my body and not wake up in Bob’s? Both brain halves are me, so why am I distinctly in my body and not seeing and thinking in dual split-screen right now, from both of our points of view? And whatever part of me is in Bob’s head, why did I lose touch with it? Who is the me in Bob’s head, and how did he end up over there while I stayed here?”

Brain Theory is shitting his pants right now—it makes no sense. If people are supposed to go wherever their brains go, what happens when a brain is in two places at once? Data Theory, who was badly embarrassed by the teletransporter experiment, is doing no better in this one.

But Body Theory—who was shot down at the very beginning of the post—is suddenly all smug and thrilled with himself. Body Theory says “Of course you woke up in your own body—your body is what makes you you. Your brain is just the tool your body uses to think. Bob isn’t you—he’s Bob. He’s just now a Bob who has your thoughts and personality. There’s nothing Bob’s body can ever do to not be Bob.” This would help explain why you stayed in your body.

So a nice boost for Body Theory, but let’s take a look at a couple more things—

What we learned in the teletransporter experiment is that if your brain data is transferred to someone else’s brain, even if that person is molecularly identical to you, all it does is create a replica of you—a total stranger who happens to be just like you. There’s something distinct about Boston you that was important. When you were recreated out of different atoms in London, something critical was lost—something that made you you.

Body Theory (and Brain Theory) would point out that the only difference between Boston you and London you was that London you was made out of different atoms. London you’s body was like your body, but it was still made of different material. So is that it? Could Body Theory explain this too?

Let’s put it through two tests:

The Cell Replacement Test

Imagine I replace a cell in your arm with an identical, but foreign, replica cell. Are you not you anymore? Of course you are. But how about if, one at a time, I replace 1% of your cells with replicas? How about 10%? 30%? 60%? The London you was composed of 100% replacement cells, and we decided that that was not you—so when does the “crossover” happen? How many of your cells do we need to swap out for replicas before you “die” and what’s remaining becomes your replica?

Something feels off with this, right? Considering that the cells we’re replacing are molecularly identical to those we’re removing, and someone watching this all happen wouldn’t even notice anything change about you, it seems implausible that you’d ever die during this process, even if we eventually replaced 100% of your cells with replicas. But if your cells are eventually all replicas, how are you any different from London you?

The Body Scattering Test 

Imagine going into an Atom Scattering Chamber that completely disassembles your body’s atoms so that all that’s left in the room is a light gas of floating atoms—and then a few minutes later, it perfectly reassembles the atoms into you, and you walk out feeling totally normal.

disassemble

Is that still you? Or did you die when you were disassembled and what has been reassembled is a replica of you? It doesn’t really make sense that this reassembled you would be the real you and London you would be a replica, when the only difference between the two cases is that the scattering room preserves your exact atoms and the London chamber assembles you out of different atoms. At their most basic level, atoms are identical—a hydrogen atom from your body is identical in every way to a hydrogen atom in London. Given that, I’d say that if we’re deciding London you is not you, then reassembled you is probably not you either.

The first thing these two tests illustrate is that the key distinction between Boston you and London you isn’t about the presence or absence of your actual, physical cells. The Cell Replacement Test suggests that you can gradually replace much or all of your body with replica material and still be you, and the Body Scattering Test suggests that you can go through a scatter and a reassembly, even with all of your original physical material, and be no more you than the you in London. Not looking great for Body Theory anymore.

The second thing these tests reveal is that the difference between Boston and London you might not be the nature of the particular atoms or cells involved, but about continuity. The Cell Replacement Test might have left you intact because it changed you gradually, one cell at a time. And if the Body Scattering Test were the end of you, maybe it’s because it happened all at the same time, breaking the continuity of you. This could also explain why the teletransporter might be a murder machine—London you has no continuity with your previous life.

So could it be that we’ve been off the whole time pitting the brain, the body, and the personality and memories against each other? Could it be that anytime you relocate your brain, or disassemble your atoms all at once, transfer your brain data onto a new brain, etc., you lose you because maybe, you’re not defined by any of these things on their own, but rather by a long and unbroken string of continuous existence?

Continuity

A few years ago, my late grandfather, in his 90s and suffering from dementia, pointed at a picture on the wall of himself as a six-year-old. “That’s me!” he explained.

He was right. But come on. It seems ridiculous that the six-year-old in the picture and the extremely old man standing next to me could be the same person. Those two people had nothing in common. Physically, they were vastly different—almost every cell in the six-year-old’s body died decades ago. As far as their personalities—we can agree that they wouldn’t have been friends. And they shared almost no common brain data at all. Any 90-year-old man on the street is much more similar to my grandfather than that six-year-old.

But remember—maybe it’s not about similarity, but about continuity. If similarity were enough to define you, Boston you and London you, who are identical, would be the same person. The thing that my grandfather shared with the six-year-old in the picture is something he shared with no one else on Earth—they were connected to each other by a long, unbroken string of continuous existence. As an old man, he may not know anything about that six-year-old boy, but he knows something about himself as an 89-year-old, and that 89-year-old might know a bunch about himself as an 85-year-old. As a 50-year-old, he knew a ton about him as a 43-year-old, and when he was seven, he was a pro on himself as a 6-year-old. It’s a long chain of overlapping memories, personality traits, and physical characteristics.

It’s like having an old wooden boat. You may have repaired it hundreds of times over the years, replacing wood chip after wood chip, until one day, you realize that not one piece of material from the original boat is still part of it. So is that still your boat? If you named your boat Polly the day you bought it, would you change the name now? It would still be Polly, right?

In this way, what you are is not really a thing as much as a story, or a progression, or one particular theme of person. You’re a bit like a room with a bunch of things in it—some old, some new, some you’re aware of, some you aren’t—but the room is always changing, never exactly the same from week to week.

Likewise, you’re not a set of brain data, you’re a particular database whose contents are constantly changing, growing, and being updated. And you’re not a physical body of atoms, you’re a set of instructions on how to deal with and organize the atoms that bump into you.

People always say the word soul and I never really know what they’re talking about. To me, the word soul has always seemed like a poetic euphemism for a part of the brain that feels very inner to us; or an attempt to give humans more dignity than just being primal biological organisms; or a way to declare that we’re eternal. But maybe when people say the word soul what they’re talking about is whatever it is that connects my 90-year-old grandfather to the boy in the picture. As his cells and memories come and go, as every wood chip in his canoe changes again and again, maybe the single common thread that ties it all together is his soul. After examining a human from every physical and mental angle throughout the post, maybe the answer this whole time has been the much less tangible Soul Theory.

______

It would have been pleasant to end the post there, but I just can’t do it, because I can’t quite believe in souls.

The way I actually feel right now is completely off-balance. Spending a week thinking about clones of yourself, imagining sharing your brain or merging yours with someone else’s, and wondering whether you secretly die every time you sleep and wake up as a replica will do that to you. If you’re looking for a satisfying conclusion, I’ll direct you to the sources below since I don’t even know who I am right now.

The only thing I’ll say is that I told someone about the topic I was posting on for this week, and their question was, “That’s cool, but what’s the point of trying to figure this out?” While researching, I came across this quote by Parfit: “The early Buddhist view is that much or most of the misery of human life resulted from the false view of self.” I think that’s probably very true, and that’s the point of thinking about this topic.

___________

If you’re into Wait But Why, sign up for the Wait But Why email list and we’ll send you the new posts right when they come out. That’s the only thing we use the list for—and since my posting schedule isn’t exactly…regular…this is the best way to stay up-to-date with WBW posts.

If you’d like to support Wait But Why, here’s our Patreon.

You can buy this post as a PDF for printing and offline reading here.

___________

Related Wait But Why Posts
– Here’s how I’m working on this false view of self thing.
– And things could get even more confusing soon when we have to figure out if Artificial Superintelligence is conscious or not.

Sources
Very few of the ideas or thought experiments in this post are my original thinking. I read and listened to a bunch of personal identity philosophy this week and gathered my favorite parts together for the post. The two sources I drew from the most were philosopher Derek Parfit’s book Reasons and Persons and Yale professor Shelly Kagan’s fascinating philosophy course on death—the lectures are all watchable online for free.

Other Sources:
David Hume: Hume on Identity Over Time and Persons
Derek Parfit: We Are Not Human Beings
Peter Van Inwagen: Materialism and the Psychological-Continuity Account of Personal Identity
Bernard Williams: The Self and the Future
John Locke: An Essay Concerning Human Understanding (Chapter: Of Identity and Diversity)
Douglas Hofstadter: Gödel, Escher, Bach
Patrick Bailey: Concerning Theories of Personal Identity

And a fascinating and related video
For a while now, my favorite YouTube channel has been Kurzgesagt. They make one amazing five-minute animated video a month on the exact kinds of topics I love to write about. I highly recommend subscribing. Anyway, I’ve spoken to them and we liked the idea of tag-teaming a similar topic at the same time, and since this one was on both of our lists, we did that this week. I focused on what the self is, they explored what life itself is. Check it out: ''',

                '7': '''The essential guide to predictive college football rankings

rank_guide_mainfigHow do you determine the best team in college football? Which four teams should make the playoffs?

College football rankings can help you answer these questions, but only if you find the right ones. With a good ranking, a higher ranked teams should more often than not beat a lower ranked team.

This article looks at the rankings you should take seriously in making predictions on college football games, whether you’re in a weekly pool, bet on games or just need to feel smart in front of your friends. Analytics also shows which rankings you can safely ignore.

The results on the predictive power of rankings are often surprising and counter intuitive. If you believe most of the conventional wisdom you hear on ESPN, you might want to stop reading right now.

The results below ask you to open your mind to new possibilities. For example, the preseason AP poll is not only useful during the season but makes good predictions on bowl games. This might seem crazy, but I’ll back it up with data below.

For the curious fans with the open mind, let’s get started.

List of trusted college football rankings
For quick reference:

College Football Playoff rankings. A committee of 13 people with backgrounds in college athletics.
Preseason AP and Coaches Poll. The collective opinion of sports writers and coaches before the season begins.
The Power Rank. My computer rankings based on margin of victory adjusted for strength of schedule.
Sagarin Ratings. A combination of three different points based computer rankings.
ESPN Football Power Index. Computer rankings based on expected points added.
Massey-Peabody. Computer rankings that combine points and yards based metrics.
S&P+. Bill Connelly’s calculations that use college football’s four factors.
Fremeau Efficiency Index. Points per possession based computer rankings.
College Football Playoff committee rankings
This committee of 13 people with backgrounds in college athletics has clear importance. Their rankings not only determine the four teams for the College Football Playoff but also influence the match ups for the New Years Six bowl games.

With only a few years of data, it’s not possible to say anything of significance about how often a higher ranked team wins a playoff or bowl game. However, there is data to suggest these ranking have predictive power.

The NCAA men’s basketball tournament has used a selection committee similar to the College Football Playoff committee to select the field and assign a seed to each team. From 2002 through 2017, the team with the higher seed has won 72% of tournament games (716 wins, 279 losses, with no prediction 50 games in which both teams had the same seed).

Let’s stop to appreciate this predictive accuracy. The selection committee consists of athletic directors and conference commissioners. There’s no requirement for coaching experience or a background in analytics. Yet over a huge sample of games, the higher seed wins more than 7 of every 10 games.

Will the College Football Playoff committee do this well with their rankings? Some factors point in their favor. This committee meets every week starting in late October until the season ends in early December. They need to rank 25 teams, not the sixty some teams of the NCAA tournament.

However, there are other factors working against the playoff committee. College football provides only 12 or 13 games each season to evaluate a team. With this small sample size, teams can look much better by their record than they deserve.

As an example, consider Florida State in 2014. The Seminoles won the BCS title the previous year and returned Heisman winning QB Jameis Winston.

However, the defense declined in 2014, and Florida State no longer dominated opponents. They had close calls against Notre Dame, Miami and Georgia Tech. “All they do is win,” said their supporters.

Florida State went 13-0 and won their conference championship. The committee ranked them third behind two one loss teams (Alabama, Oregon). The Seminoles fell apart in the playoff semifinal against Oregon, losing 59-20.

Only time will tell whether the College Football Playoff committee can be as good as the selection committee for March Madness.

The Preseason AP and Coaches polls
The preseason polls might seem worthless for making predictions. The humans of AP and Coaches have no games upon which to base their ballots. It seems more reasonable to wait until later in the season to look at these polls.

However, this is a mistake. The preseason AP and Coaches poll have remarkable predictive power, even during Bowl season. Human polls from later in the season do not.

To show this, we ask how often the higher ranked team in the poll beat a lower ranked team in a bowl game. In this study, I rank teams beyond the top 25 based on points earned from pollsters, and ranked teams are predicted to beat unranked teams.

Over the past 10 years, a sample of 339 bowl games, the preseason Coaches poll predicted 59.9% of bowl game winners (163-109 with no prediction in 67 games with two unranked teams). The AP poll didn’t do much worse at 58.8% of winners (154-108 with no prediction in 77 games).

To put this in perspective, the team favored by the closing line in the gambling markets won 61.5% of games according to The Prediction Tracker (208-130 with no prediction in one game). The visual shows these results.

preseason_poll_accuracy_2014

Note the prediction accuracy of the polls before the bowls is less than the accuracy of preseason polls.

The remarkable predictive power of preseason human polls most likely comes from the wisdom of crowds. No one sports writer or coach can create a perfect ranking. However, combining the ballots of many humans cancels out the small errors made by each one.

Don’t forget about preseason expectations. To see the preseason AP and Coaches poll for 2015, click here.

Points based computer rankings
There are so many college football computer rankings. Ken Massey compiles over a hundred of them on his site. How do you distinguish the rankings that make good predictions from those that do not?

There’s a simple trick for sorting the good from the bad rankings, and it comes from consider two ideas: strength of schedule and margin of victory.

The college football playoff committee has made strength of schedule a buzzword. How does one evaluate a team in the context of which teams they have played? Computer rankings are a numerical approach to answering this question.

Margin of victory doesn’t get discussed as much as strength of schedule. This lack of attention may have resulted from the old Bowl Championship Series. To deter teams from running up the score in the name of sportsmanship, they didn’t allow their computer polls to consider margin of victory.

Which idea matters more: strength of schedule or margin of victory?

To test this with data, we can construct rankings that consider neither, one or two of these factors. Consider the following metrics for rankings teams.

Win percentage. Fraction of games won. Considers neither strength of schedule nor margin of victory.
Colley Matrix. A computer poll that takes wins and losses and adjusts for strength of schedule.
Raw margin of victory. Points scored minus points allowed divided by number of games, a raw number that makes no adjustment for schedule.
Simple Rating System. A least squares ranking system that takes margin of victory and adjusts for strength of schedule.
The Power Rank. An algorithm I developed that takes margin of victory and adjusts for strength of schedule.
The visual shows how often each of these rankings predicted the winner in 339 bowl games from 2005 through 2014.

rank_accuracy_2014

Win percentage is hardly better than flipping a coin for each bowl game. The Colley Matrix does better than win percentage but not nearly as good as raw margin of victory. Strength of schedule without margin of victory results in poor rankings for making predictions, and you should avoid these rankings.

The two algorithms that take margin of victory and adjust for strength of schedule perform the best and almost as well as the closing spread from the markets (61.5%).

Let’s look at two recommended points based computer rankings that make good predictions.

The Power Rank. A method I developed based on research in statistical physics. For more details, click here.
Sagarin Ratings. Combines three different types of points based computer rankings for his college football rankings.
Play by play based computer rankings
Modern college football rankings go beyond the final score and use the play by play data from each game. I recommend the following rankings.

ESPN’s Football Power Index
ESPN’s analytics group has developed college football rankings based the idea of expected points added (EPA), or the notion that each play of a game has a point value.

To understand EPA, suppose a team has a 1st and 10 at their own 20 yard line. They could drive the length of the field for a touchdown for +7 points or kick a field goal for +3 points. In the worst case, an interception gets returned for a touchdown, netting -7 points for the offense.

Given a down, distance and field position, the offense’s expected points is an average of the net points of the next score. For example, Brian Burke of ESPN has used NFL play by play data to determine that 1st and 10 from a team’s 20 yard line gives +0.3 expected points.

Expected points added (EPA) is the points gained or lost from a play. For example, suppose the offense gains 20 yards from that 1st and 10 from their own 20 yard line. Burke calculates 1.3 expected points for a 1st and 10 from their own 40. Since the offense started in a situation with +0.3 expected points, they had +1.0 EPA for this play.

ESPN uses EPA in college football for their FPI rankings, numbers meant to make predictions looking forward. They use the Simple Ratings System, a least squares method for ranking teams, to adjust EPA for strength of schedule.

To check out ESPN’s FPI, click here.

Bill Connelly’s S&P+
Bill Connelly, SB Nation’s college football analytics guru, writes a preview for each and every FBS team, even New Mexico State. These treasures have become the only team previews I read each season.

Connelly’s numbers inform his writing as he ranks college football teams based on four factors.

Explosiveness – Measured by equivalent points per play, a metric similar to the expected points added used by ESPN’s FPI.
Efficiency – Measured by success rate, or 50% of the necessary yards on 1st down, 70% on 2nd down, and 100% on 3rd and 4th down.
Finishing drives – Measured by points per trip inside the opponent’s 40 yard line.
Field Position – Measured by average starting field position, a number affected by special teams.
His methods takes each of these factors and adjusts for strength of schedule. These four factors are combined to make the final rankings. Connelly provides a sense for the importance of each factor in his original article on football’s five factors.

Before the 2015 season, Connelly’s rankings depended on only success rate and points per play, which gives the term S&P. He has kept the same name despite adding two addition factors to the calculation.

To check out S&P+, click here.

Massey-Peabody
Cade Massey, a professor at the Wharton School of Business and Rufus Peabody, a professional sports gambler, have developed football rankings based on a simple idea.

We use only four statistics – one each for rushing, passing, scoring and play success. Rather than creating esoteric new stats (not that we aren’t occasionally impressed with those), we focus on “cleaning up” these relatively basic stats and then finding the appropriate weight for them in our model.

Most likely, they use yards per play for the rushing and passing numbers. The scoring component is similar to the points based rankings mentioned earlier. Last, the play success is either like Bill Connelly’s success rate or expected points used by ESPN.

Combining these metrics lead to powerful rankings. I use a similar ensemble method in the college football rankings and predictions for members of The Power Rank, and I most often check my results with those of Massey-Peabody.

To see the top 35 college football teams in Massey-Peabody, click here. They also publish NFL rankings.

Fremeau Efficiency Index
Brian Fremeau uses points per possession to evaluate teams in football. It starts by comparing the points earned on a drive with the expected number of points based on starting field position.

Accounting for starting field position is important. For example, if the offense gets the ball only a yard from the end zone, they should not get full credit for scoring the touchdown. Instead, the offense get 7 minus the expected 6.4 points teams usually score from the opponent’s one yard line.

Fremeau publishes his drive based numbers both on his own site and Football Outsiders. The latter site also combines FEI with S&P+ to obtain the F/+ rankings, an aggregate picture of team, offense and defense in college football.

Feedback
Have a question or know of other rankings that should be included? Send me an email here. ''',

                '8': '''How You Should Read Research Papers According To Andrew Ng (Stanford Deep Learning Lectures)
Instructions on how to approach knowledge acquisition through published research papers by a recognized figure within the world of machine learning and education
Richmond Alake
Richmond Alake
Follow
Jul 1 · 8 min read



Image for post
Photo by Annie Spratt on Unsplash
“Wisdom is not a product of schooling but of the lifelong attempt to acquire it.”
— Albert Einstein
Introduction
The ability to understand information produced by the individuals at the cutting edge of research within Artificial Intelligence and the Machine learning domain is a skill that every serious machine learning practitioner should acquire.
To stay relevant and increase your knowledge, machine learning practitioners need to have an academic mindset and habit. AI, ML and DL are evolving at a fast pace, and we have to equip ourselves with the knowledge to keep up with the field, knowledge that is only attainable through research papers.
This article will provide you within instructions on how to go through a research paper effectively, and also provide the following:
A systematic approach to reading a collection of papers to gain knowledge within a domain
How to properly read a research paper
Useful online resources that can aid you in searching for papers and key information
For those who would like to get to the key content within this article, scroll down to the section titled “Reading Research Papers”.
First, Who is Andrew Ng?
The information I provide in this article was derived from a Stanford lecture taught by Andrew Ng. I’ve also supplemented the information contained in this article with personal tips and information from resources on the internet.
But first, a brief introduction on Andrew Ng.
Andrew Ng is probably the most known(and watched) machine learning teacher on the internet. He is also the co-founder of both Deeplearning.ai and Coursera.
Apart from his ongoing work within online education, he’s also a professor at Stanford University.
More information on Andrew Ng is just a google search away.
It’s natural for a person to pick up skills and habits demonstrated by individuals around their environment; this is why most PhD students will acquire the skill of effectively digesting the content of a research paper appropriately. This is somewhat a fact, and Andrew mentions it very early in the video referenced earlier.
But we are not PhD students, well some might be, but how do we normal individuals gain the required skills to read a research paper and understand its content wholeheartedly.
Reading Research Papers
Image for post
Photo by Christa Dodoo on Unsplash
Specialization within the machine learning domain is favourable if you are talented. For example, having a generalist knowledge on the field of Computer vision is commendable, but having specialized knowledge and expertise within key techniques such as Pose estimation will be more appealing to companies and organization looking for practitioners within that domain.
So let’s use Pose Estimation as a guide to how we would approach reading research papers related to the subject matter: pose estimation.
1. Assemble collections of resources that focus on the subject matter. Resources can come in the form of research papers, Medium articles, blog posts, videos, GitHub repository etc.
A quick google search on the phrase “pose estimation” will provide you with top resources that contain information in regards to the subject matter. At this initial step, the aim is to collate all resources that are relevant, such as YouTube videos, implementation documentations and of course research papers. Ideally, at this stage, there is no limit to the number of resources you consider important, but be sure to create a shortlist of papers, videos and articles that are useful.
2. In this next step, you will conduct a deep dive of any resource you deem relevant to the subject matter. It is crucial that there’s a method to track the understanding of each shortlisted resources. Andrew Ng, suggests a table of resource plotted against your understanding level that looks similar to the table below.
Image for post
Understanding level table of resources By Richmond Alake
It is advisable to ensure you go through at least 10–20% of the content of each paper you have added to the list; this will ensure that you have been exposed to enough of the introductory content within an identified resource and are able to gauge its relevancy accurately.
For the more relevant papers/resources identified, it is expected that you progress to a higher level of understanding. Eventually, you will have identified some appropriate resources with content that you understand fully.
You are probably asking yourself, “what number of papers/resource is sufficient”.
Well, I don’t have the answer, but Andrew does.
According to Andrew, an understanding of 5–20 papers will showcase a basic understanding within the subject matter, perhaps enough understanding to progress to implementation of techniques.
50–100 papers will primarily provide you with a very good understanding of the domain.
After going through the resources and extraction of vital information, your table might look something similar to what’s shown below.
Image for post
Updated Understanding level table of resources By Richmond Alake
3. The third step is a quick tip from what I’ve observed works for me when trying to understand research papers. The third step is to take structured notes that summarises the key discoveries, findings and techniques within a paper, in your own words.
The following steps will now be focused on how to read a single research paper.
Reading A Single Research Paper
Image for post
Photo by Alfons Morales on Unsplash
Reading for the purpose of understanding is not done through one pass of the contents within the paper. According to Andrew, reading a paper from the first word to the last word in one sitting might not be the best way to form an understanding.
Be prepared to go through a paper at least three times to have a good understanding of its content
4. In your first pass, start with reading the following sections within the paper: title, abstract and figures.
5. The second pass entails you reading the following sections: introduction, conclusion, another pass through figures and scan through the rest of the content.
The introduction and conclusion section of a paper contains clear and concise information on the content of the paper and a summary of any findings. The information presented in this section usually dismisses any supplementary information and only key information are included. This is beneficial to you as a reader as you get the vital information required to proceed to the other sections within the paper.
6. The third pass of the paper involves reading the whole sections within the paper but skipping any complicated maths or technique formulations that might be alien to you. During this pass, you can also skip any terms and terminologies that you do not understand or aren’t familiar.
7. Those conducting in-depth research into a domain can take a few more passes. These additional passes will mainly be focused on an understanding of the maths, techniques and unknown terminologies presented within the paper.
For those who are generally reading research papers for informational and engineering purposes, then in-depth research might be very time consuming, especially if you have 20 more papers to get through.
I went through the process presented in this article with the original paper introducing the LeNet convolutional neural network, and I summarised the key content in notes which I later then converted to a series of Medium articles.
Understanding and Implementing LeNet-5 CNN Architecture (Deep Learning)
In this article, we perform image classification on the MNIST dataset with custom implemented LeNet-5 neural network…
towardsdatascience.com
(You Should) Understand Sub-Sampling Layers Within Deep Learning
Average pooling, max-pooling, sub-sampling, downsampling, are all phrases that you’ll come across within Deep Learning…
towardsdatascience.com
Understanding Parameter Sharing (or weights replication) Within Convolutional Neural Networks
Parameter sharing or weights replication is a topic area that can be easily overlooked within deep learning studies…
towardsdatascience.com
Understand Local Receptive Fields In Convolutional Neural Networks
Ever wondered why all the neurons in a convolutional neural network aren’t connected?
towardsdatascience.com
Questions To Ask Yourself
Andrew provides a set of questions that you should ask yourself as you read a paper. These questions generally will show you understand the critical information presented in a paper. I use the questions below as beacons to ensure I don’t stray from the aim of understanding vital information.
They are as follow:
Describe what the authors of the paper aim to accomplish, or perhaps did achieve.
If a new approach/technique/method was introduced in a paper, what are the key elements of the newly proposed approach?
What content within the paper is useful to you?
What other references do you want to follow?
Additional Resources To Assist Research
Several online resources have made the discovery and retrieval of relevant information relatively easy. Below are examples of resources that will assist you in your search for pertinent information.
The Machine Learning Subreddit
The Deep Learning Subreddit
PapersWithCode
Top conferences such as NIPS, ICML, ICLR
Research Gate
Conclusion
“Learn steadily rather than short burst for longevity.“
— Andrew Ng
I’m still relatively new to the field of Machine Learning and Computer Vision, there is a lot that I do not know (that’s an understatement). Still, I believe that if an individual is consistent in their search for knowledge, regardless of the domain, they’ll be rewarded with an understanding and expertise that surpasses the norm.
From the techniques introduced by Andrew Ng, I’ll be reading at least four research papers a month, reading to the point of understanding. I’ll be honest and say that the LeNet paper took me about a week and a half to complete wholeheartedly. But you get better and faster at reading and understanding research papers the more times you do it.
Andrew states in his video that he carries a batch of research papers around with him, intending to read them. Andrew is a prominent figure within the field of machine learning, and I believe emulating his habits and learning techniques can be advantageous to your learning journey. ''',

                '9': '''The Narrative Fallacy
When I first moved to LA, I didn’t have enough money to buy a bed. I borrowed an IKEA futon and slept on the floor for almost two months. Now I know that you can get some really comfortable futons these days, especially if you look on somewhere like ReviewingThis, but this thing I was sleeping on was definitely not that. I was so stressed and scared that I would wake up in the middle of the night just soaked in sweat. My parents practically disowned me.

Here’s the thing, I could make that all into some dramatic story – like it was this harrowing experience that stays with me – but to be frank, I have almost no recollection of that time. Not because I blocked it out or anything, but because it didn’t seem worth remembering. I worked through it and now I’ve got things back where I like them.

The more painful the initiation, the more likely we are to want to stick with the program. The more inspiring and metaphoric we make our stories, the less they seem to resemble the dull and comfortably literal world that the rest of us live in. We start to think that we’re different, that the laws don’t apply to us – that all we have to do is let manifest destiny take its course. This denies the fundamental role of hard work and sacrifice and luck in everything. Narration conveniently ignores the day we laid around and watched tv and the week where we were sure we were going to quit but didn’t. It’s just not honest.

I guess I could slowly trick myself into thinking that my first few real months in LA will end up molding who I am. “Oh to be be young and driven…” But then I’m more attached to the path I’ve embarked on, those become hard, sunk costs. I’ll start to think that that was the “right way” as opposed to a way and my judgment will be clouded and off.

The fact of the matter is this: I’m 20. I have a cool job that was not without its tradeoffs. I wake up and sometimes I’m super motivated, sometimes I’m not. I’ve been doing it for a while. I’ve had days where I thought to myself that it was over and others where I leaped way ahead. That sounds a lot different than the 200 word biography I could type up for myself if I wanted to impress someone.

There is this Stoic exercise where you break apart something sacred into its most basic parts. When you see how unromantic it really is, the object loses all power over you – you maintain the sovereignty of self. Marcus does this throughout Meditations: sex is rubbing and semen, the cloak of the Emperor differs only in color, death is but the end of feeling.

Shit like prodigy or lucky or “destined for big things” and whatever other superlatives I hear are stories. Just stories. And stories are worthless because they’re mental creations – they are not reality. In ten years, you tell me what bank is going to cash a protégé label. Yours are different but the same.

No question, the use of story is a persuasive tactic. But why? Because they please and pleasure the senses. When stories are applied to self-perception, they are called delusions.

I don’t think the idea is to strip the meaning and specialness out of life. There is still very much a purpose and uniqueness in us. That is innate. But humbleness, clarity, and restraint – those are learned and practiced forms of excellence. They are the extension of honesty. This doesn’t mean you’re unappreciative or pessimistic. Or good food turns to ash in your mouth. That you have to hate the things you want to like. It doesn’t change so much how you live life, as much as it does how you talk about it.

Still, that is not easy either. We are wired to think a certain way – linearly, towards purpose, in terms of justification. Ambivalence, in the jungle, was death. The mind strives for congruency and lashes out violently when there isn’t any. It’s also why people wake up one day and have no idea how the world works anymore. That’s why people say things like “Do you have any idea who I am?” with a straight face.

Resisting the urge to tell yourself stories is difficult. It’s depressing. You fuck up and do it all the time. And occasionally, with little things, that’s OK. Mixed with my self-loathing, I’m often overwhelmed. And tired. And feel like quitting. I have trouble really putting to words how much I struggle with whether its worth it – but if I didn’t say that, I wouldn’t be being honest. It works for me because I work at it but just barely.

I don’t think it’s a fight you can win on your own – it takes people on both sides, cynical and optimistic to keep you centered. Living in delusion is a short-term strategy – simply unsustainable. My philosophy, and it’s one that’s working pretty well is this: There are more than enough people willing to tell your story for you if its good enough. In the meantime, I’ve too much other stuff I need to work on. ''',

                '10': '''How to understand college football analytics – the ultimate guide
By Dr. Ed Feng 7 Comments


What can analytics tell us about college football? Can numbers help us determine the four best teams for the new playoff?

College football seems behind other sports in the analytics revolution. Bill James started using baseball data to answer the sport’s important questions in the late 70’s. His methods hit mainstream in 2003 when Michael Lewis published Moneyball, a book on how the Oakland A’s used analytics to compete with higher payroll teams.

Now, baseball will soon track the motion of every player on every play of every game. The NBA has also evolved beyond box score statistics like points per possession and installed player tracking cameras in every arena.

However, we’re not completely in the dark with college football analytics. Here, we discuss the most important concepts you should take away from college football analytics. Keep this primer handy as you argue which teams should make the playoff.

Strength of Schedule and Margin of Victory
With the upcoming playoff, strength of schedule has become a buzzword in college football because it’s a key criteria for the selection committee that will pick the best four teams. It’s an immense improvement from the BCS era in which a team’s record played a much greater role in making the championship game.

However, a less discussed but also important concept is margin of victory. The data shows that teams with a larger average margin of victory tend to win more. This holds in every sport from college football to international soccer.

The BCS made margin of victory a political issue. Since they didn’t want teams to run up the score, they banned margin of victory from the computer polls in their formulas. This resulted in the insanity of using Jeff Sagarin’s Elo rankings, a model with less predictive power than his predictor rankings. (With the end of the BCS, Sagarin now uses margin of victory in his Elo rankings.)

Let’s use data to determine the importance of strength of schedule and margin of victory in predicting football games. We will calculate a set of rankings based on games prior to bowl season and ask how often the higher ranked team won a bowl game. The test set includes 339 bowl games from the 2005 through 2014 seasons. The visual contains results for a number of rankings.

rank_accuracy_2014

The rankings by win percentage considers neither strength of schedule nor margin of victory. The team with the better record by win percentage is predicted to win a bowl game. It doesn’t matter that Rice’s 10 wins came in Conference USA while Mississippi State won 6 games in the SEC.

The Colley matrix, one of the computer polls of the deceased BCS, adjusts wins and losses for strength of schedule. This method has a weird quirk but is otherwise based on the sound mathematics of linear algebra.

Raw margin of victory is calculated by taking points scored minus points allowed and dividing by the number of games, an extraordinarily simple metric.

The last two rankings depend on algorithms that take raw margin of victory and adjust for strength of schedule.

The Simple Rating System (SRS) appears on all the Sports Reference sites. If you dig into the math, you’ll find that SRS is a least squares rating system. Just compare the matrix equation on page 38 of Ken Massey’s thesis with the equations in this article on Sports Reference. We’ll encounter this method again later in discussing efficiency metrics.

I developed The Power Rank from my research in statistical physics. While the details are not public, the algorithm is based on the mathematics of Markov chains and tends to strongly diminish the effect of blowouts.

The visual shows the importance of margin of victory. While Colley’s method increases the predictive performance of a team’s record, it can’t match the predictive power of raw margin of victory. The BCS brought knives to a gun fight. With a 339 game sample, the uncertainty in these win percentages is about 3%, which shows the significant improvement of raw margin of victory over Colley.

The strength of schedule adjustments from the Simple Rating System and The Power Rank improve the prediction accuracy of raw margin of victory.

Randomness of turnovers
Turnovers have an enormous impact in football. A lost fumble at the goal line negates a scoring opportunity, or a tipped pass falls into the hands of a defender who scores a touchdown. It’s enough to make any fan go looking for Prozac.

It’s easy to assign blame or credit for these plays. The running back didn’t hold on to the ball, or the linebacker smacked the crown of his helmet right onto the ball, jarring it loose. Newton’s second law supports these arguments.

However, data tells a different story about turnovers. First, consider fumbles. Can a defense force fumbles, meaning both knocking the ball loose and recovering it? If they can, then teams that force more fumbles in the first six games of the season should also force more fumbles the next six games.

In 2013, nine teams forced nine or more fumbles in their first six games. These defenses (and possibly special teams) averaged 1.77 fumbles per game in this early part of the season. In their next six games, these teams averaged 0.89 forced fumbles per game, close to the 0.78 average. This doesn’t support the idea of a big play defense.

How about holding onto the ball, either by not fumbling or recovering any such fumbles on offense? That must be a skill, right? In 2013, eight teams had one or fewer fumbles lost in their first six games. In their next six games, these same teams lost 0.63 fumbles per game, much closer to the 0.78 average.

Fumble rates on offense and defense strongly regress to the mean from early to late season. For the 246 FBS and FCS teams that played at least 9 games in 2013, the forced fumble rate for a defense in the first 6 games of the season had no correlation with forced fumble rate later in the season (explains less than 1% of the variance). Bill Barnwell found the same result in the NFL. This lack of correlation also holds for lost fumbles on offense.

Fumbles rates do depend on where the fumble occurs on the field. Brett Thiessen, who writes as the Mathalete on MGoBlog, found that a defense forces fumbles on almost 6% of sacks, a much higher rate than any other kind of play. While the defense doesn’t recover as many of these sack fumbles as those on positive plays, sacks still have the highest net rate of recovered fumbles by the defense.

How about interceptions? For a college football defense, their interception rate (interceptions divided by pass attempts) in the first 6 games explains 1.3% of the interception rate the rest of the season. As the visual shows, you’re essentially looking at randomness when your defense picks off the other team.

How early season interception rate predicts later in the season

On offense, interception rate still shows the same randomness from early to late season. However, offenses that complete a higher number of passes tend to throw few interceptions. In 2013, a team’s completion percentage explains 28.5% of the variance in interception rate. This correlation gets stronger when looking at the statistics for individual quarterbacks in the NFL.

I understand the difficulty in accepting the randomness of turnovers. Your eyes see the linebacker put his helmet on the ball while making a hit, which jars the ball loose from the running back. However, the data implies that the linebacker cannot consistently hit the back with enough force to cause the fumble. Don’t let your eyes deceive you.

Turnovers can have a large impact on margin of victory. A tipped pass near the goal line that the defense returns for a touchdown could be a 14 point swing. Since turnovers introduce randomness into the margin of victory that most computer rankings use, we need other metrics to evaluate a team. The next section discusses these efficiency metrics.

Efficiency metrics
To define an efficiency metric in football, you take a meaningful number like yards gained by an offense and divide it by an appropriate quantity. Unfortunately, most talking heads pick number of games as the denominator and use yards per game to rank offenses.

Yards per game statistics have serious problems in evaluating offense and defense. College football teams play at variety of paces, from the 87.3 plays per game that Texas Tech ran in 2013 to the 59.3 of South Florida. Moreover, yards per game is a particularly bad metric for the defense of an uptempo offense like Oregon or Oklahoma State. These defenses face a large number of plays since their offenses play so fast.

Tempo matters more in the college game than the NFL. In 2013, the standard deviation in plays per game was 5.7 in college, so 2 out of 3 teams averaged within 5.7 plays of 70 play average. The NFL had a standard deviation of 3.2 plays per game.

More problems with yards per game appear when evaluating passing and rushing. Teams tend to run the ball when they’re ahead since these plays keep the clock running. Hence, good teams tend to have better rush yards per game due to play selection.

To get better insight, the football analytics community has developed a number of efficiency metrics for offense and defense.

Yards per play
The most simple metric is yards per play. Take total yards and divide by the number of plays. It does not account for the situation of any play like some of the metrics discussed later. However, yards per play is mostly immune from the randomness of turnovers, one reason it has great predictive power.

Bob Stoll, a college football handicapper that has a 54.9% win rate against the spread from 2001 through 2013, uses yards per play as his primary metric in evaluating offense and defense. You can read more about his methods in this essay and his free analysis of games every week.

Yards per play gets tricky in college football when breaking an offense or defense into passing and rushing. In college football, negative yards from sacks count against rushing totals. However, sacks started as an attempt to the throw the ball and should count against pass totals.

No matter, every major media site counts sacks as rushes in both yards per game and per play statistics. To see yards per play with sacks as pass plays, check out my numbers at The Power Rank.

The NFL does not count sacks as rush plays. However, sacks do not count as pass attempts either. Then the total number of plays includes passes, rushes and sacks. It’s important to include sacks in total plays to calculate the correct yards per play.

At The Power Rank, I take yards per play and adjust for strength of schedule with my ranking algorithm I developed from my Ph.D. research in statistical physics. These efficiency rankings for both college football and the NFL are available to members. Bob Stoll also adjusts for schedule strength in his yards per play numbers.

Expected points added
Suppose a team has a 1st and 10 at their own 20 yard line. They could drive the length of the field for a touchdown, gaining +7 points for the offense. Their drive could also stall at the opponent’s 17 yard line, which results in a field goal for +3 points. In the worst case, a tipped pass could fall into the hands of a cornerback who scores a touchdown, netting -7 points for the offense on the next score of the game.

Given a down, distance and field position, the offense’s expected points is an average of the net points of the next score, a calculation which requires historical play by play data. Brian Burke of Advanced Football Analytics has performed this calculation for the NFL and found that a 1st and 10 from a team’s 20 yard line gives +0.3 expected points.

With this baseline knowledge, the expected points added (EPA) is the points gained or lost from a play. For example, suppose the offense gains 20 yards from that 1st and 10 from their own 20 yard line. Burke calculates 1.3 expected points for a 1st and 10 from their own 40. Since the offense started in a situation with +0.3 expected points, they had +1.0 EPA for this play.

This metric accounts for the situation of a play. There’s more value in gaining 2 yards on 3rd and 1 than gaining 2 yards on 1st and 10.

EPA forms the basis of ESPN’s Football Power Index (FPI) for college football. They use the Simple Rating System, the least squares ranking system discussed previously, to adjust this statistic for strength of schedule. Bill Connelly of SB Nation also uses this concept in his Equivalent Points Per Play, a component of his S&P ratings for college football. For the NFL, Burke uses EPA to evaluate players.

Success rate
Success rate is the number of successful plays divided by the total number of plays. In college football, Bill Connelly defines success as 50% of the necessary yards on 1st down and 70% on 2nd down. Success requires all the necessary yards on 3rd and 4th down.

Connelly’s S&P metric multiples his success rate with the Equivalent Points per Play mentioned earlier. He then adjusts for strength of schedule by looking both at a team’s opponents and opponents of opponents. This results in S&P+, which appears on Football Outsiders.

This idea of success rate also forms the basis of Football Outsider’s DVOA (Defense adjusted value over average) for the NFL. Aaron Schatz and coworkers expanded success beyond assigning a 0 or 1 to each play. They give a real value such as 1.3 or -4.0 to each play based on down and distance. This leads to their team rankings as well as player metrics.

The Football Outsiders also talks about large negative values of DVOA on turnovers. Hence, this success rate statistic is affected by the randomness of turnovers just like margin of victory. Turnovers impact Connelly’s success rate much less since it only counts as a failure.

Points per drive
Instead of looking at football on each play, it also makes sense to evaluate offense and defense on each drive. Brian Fremeau does this with his Fremeau Efficiency Index. It compares the points earned on a drive with the expected number of points based on starting field position.

Accounting for starting field position is important. For example, if the offense gets the ball only a yard from the end zone, they should not get full credit for scoring the touchdown. Instead, the offense get 7 minus the expected 6.4 points teams usually score from the opponent’s one yard line.

Fremeau publishes his drive based numbers both on his own site and Football Outsiders. The latter site also combines FEI with S&P+ to obtain the F/+ rankings, an aggregate picture of team, offense and defense in college football.

Football Outsiders also publishes drive stats for the NFL. Unlike FEI, these stats neither consider starting field position nor adjust for schedule strength.

Will the selection committee use analytics?
No one knows whether the 13 people responsible for picking the 4 teams for the college football playoff will care about numbers. However, it’s encouraging that the selection committee has publicly talked about strength of schedule. That’s a huge step.

However, they need to apply it correctly. They could also consider strength of schedule by wins and losses and not margin of victory. In 2012, Notre Dame went 12-0 with 3 wins over top 25 teams. A ranking system like the Colley Matrix, which adjusts wins and losses for strength of schedule, ranked the Fighting Irish first heading into Bowl season.

But this article shows the importance of margin of victory in rating teams. Notre Dame had an average margin of victory of 16.4 points compared to the 27.8 of Alabama, the team they faced in the BCS title game. Alabama stomped Notre Dame 41-14 in that game. The Colley matrix had Notre Dame ranked over Alabama after the title game, showing the fallacy in systems that don’t use margin of victory.

There’s even less hope the committee grasps the randomness of turnovers. They will be watching games, but turnovers are an area in which your eyes will fool you. Forcing a fumble by a big hit looks impressive and can change a game. However, high forced turnover rates are not sustainable.

Just ask Oregon about the randomness of turnovers. In 2013, they forced 9 fumbles in their first 6 games as they raced towards a spot in the BCS title game. Oregon only forced 2 fumbles in their next 6 games. Losses to Stanford and Arizona killed their championship dreams.

And there’s no chance the committee gets into efficiency metrics. The college football establishment is just not sophisticated enough for that. Maybe in a few years.

But we can all hope they grasp the basics of using margin of victory in their deliberations. It’s the only way to determine the 4 best teams, the goal of the selection committee. ''',

                '11': '''Python Sports Analytics Made Simple (Part 2)
Robert Clark
Robert Clark
Follow
Mar 2, 2019 · 10 min read



Image for post
Photo by Timur Saglambilek from Pexels
Python Sports Analytics Made Simple (Part 1) — Creating a public sports API
Python Sports Analytics Made Simple (Part 2) — Pull any sports metric in 10 lines of Python
Welcome to this two-part series where I demonstrate how to pull thousands of sports metrics with just a few lines of Python.
In the first part, I detailed the steps I took to create a public API called sportsreference. In this second article, I dive into the installation and usage of the API and demonstrate how easy it can be to pull various sports statistics.
Image for post
Try to avoid dependency hell at all costs. Photo by icon0.com from Pexels
Setup
Prerequisites
Prior to installing sportsreference, the following prerequisites are required for your development environment:
Python 2.7 or Python ≥ 3.5
PIP ≥ 8.1.2
Recommendations
In addition to the requirements above, it is also highly recommended to use a virtualenv for development work to avoid what is affectionately known as “dependency hell”.
Dependency hell is a colloquial term for the frustration of some software users who have installed software packages which have dependencies on specific versions of other software packages. The dependency issue arises around shared packages/libraries on which several other packages have dependencies but where they depend on different and incompatible versions of the shared packages.
Source: Wikipedia
For more information on virtualenv, I recommend reading the official documentation.
Installation
The easiest way to get started with sportsreference is to use PIP to download and install the latest binary:
pip install sportsreference
If using a virtualenv, this will install sportsreference and all necessary dependencies in the active virtual environment. If not using virtualenv, the package and its dependencies will be installed globally and made available system-wide.
Usage
Now that sportsreference is installed, let’s write our first program using the package we downloaded. In all of the following examples, you will notice a theme where a specific class or module is imported from sportsreference, the imported class is instantiated, and that instantiated class is used to query metrics.
Image for post
Teamwork makes the dream work! Photo by rawpixel.com from Pexels
Teams
The first module, teams, is the core module of all six sports and exposes metrics on a team-by-team basis, such as current records, total points, shooting percentages, stolen bases, interceptions, and more. While the various sports expose different statistical categories, they all follow the same method of returning metrics for each team.
For our first example, we are going to request every NCAA Men’s Division-I Basketball team for the current season and print their name, wins, and losses:

Printing team names and records using sportsreference
In the sample code above, we are only printing three categories for each team, but the Teams class alone contains nearly 100 different statistical and informational categories that can be called just by specifying the respective property name. For example, if you wanted to print each team’s turnover percentage, you would change the fourth line above to:
    print(team.turnover_percentage)
Et voilà! In just four lines of code, you can now read nearly any team-based metric for all teams in all supported sports for the current or most recent season.
Vigilant readers will notice that I mentioned this only works for the current or most recent seasons for the given sport. By default, sportsreference will attempt to pull stats for a season that is in-progress, or for the season that most recently concluded during the off-season. Previous seasons can be requested, however, by simply passing the desired year as a string while instantiating the Teams class:

Print the number of wins and losses for all NCAAB teams for a previous year
This example likely looks identical to the previous snippet, but there is a subtle difference in the argument to Teams. This time, we included the year to pull data from, so we will be printing the names and final records of all teams during the 2018 NCAAB season only.
sportsreference also integrates with the pandas library to provide a DataFrame of all statistical values in a single object:

Create a Pandas DataFrame of all statistical categories for all teams in the current NCAAB season
Image for post
Photo by Craig Adderley from Pexels
Schedules
Overall team-based metrics aren’t the only categories that sportsreference supplies — each team’s schedule can also be queried on a game-by-game basis. There are two main ways to get a team’s schedule; either by requesting the schedule from the Team class, or by using the schedule module to specifically request a particular team’s schedule.
For the next few examples, I switched to the NFL to demonstrate the similarities of using sportsreference to retrieve data regardless of the sport. Though the NFL is very different from NCAA Basketball in terms of how the games are played and who can participate, when it comes to sportsreference, we only need to change the first line in our code where the package is imported.
We can run the following code to get the schedule for every NFL team using the first method listed above by requesting the schedule for each Team instance:

Print the date and score of every game for each team in the NFL
As with the NCAAB examples in the previous section, we iterate through all of the teams that participated in the most recent NFL season and print their names. This time, however, after printing the team name, we request their schedule and iterate through every game played during the season and print the date the game was played on as well as the amount of points the team scored followed by the amount of points the opponent scored.
If the schedule for just a single team is desired, the Schedule class can be called directly with an argument specifying the team to pull:

Print the date and score of every game for each team in the NFL using schedule module
This sample prints out the exact same information as with the previous snippet, but instead of generating the output for each team in the NFL, it only does so for the Houston Texans. When calling the Schedule class, the 3-letter abbreviation of the desired team needs to be passed as a string. Each team’s abbreviation can be found on sports-reference.com by checking any links to a team page. There’s just one minor caveat for college football and basketball: due to the comparatively large number of college teams compared to professional, it is impossible to succinctly identify colleges using just three letters, so sports-reference differentiates various schools by using their hyphenated name in place of the abbreviation in lower-case letters, such as “purdue” or “michigan-state”. When requesting metrics for college sports, this hyphenated name should be used instead of the 3-letter abbreviation shown above.
Back to the examples, we can generate a pandas DataFrame containing game-by-game stats for a given team:

Print a pandas DataFrame for a team’s schedule
This time, instead of iterating over every game in the schedule, we can request a DataFrame directly from the class instance. The code above will generate a DataFrame where each row correlates to a different game in the team’s schedule and the categories are different statistical fields for each particular game.
Image for post
Photo by Jason Weingardt on Unsplash
Boxscores
A sports API project wouldn’t be complete without including detailed stats for individual games. With the boxscores module, all games can be queried for a deep analysis into the score, game trends, team-based percentages and totals, as well as individual player contributions.
To pull results and analysis from a specific MLB game, we just need to grab the URI straight from sports-reference.com and use it while instantiating the Boxscore class:

Print the score and a DataFrame for a specific MLB game
For this example, I simply print the final number of runs scored by both the away and home teams, as well as a DataFrame featuring in-depth stats for the game.
I retrieved the URI of BOS/BOS20180808020 by navigating to sports-reference.com and selecting a game played on August 2, 2018 between the Boston Red Sox and the New York Yankees. The URL for this specific game is the following: https://www.baseball-reference.com/boxes/BOS/BOS201808020.shtml. As you can probably tell, the URI I need is everything between "boxes/" and ".shtml".
While this is a simple method of getting information on a specific game, it isn’t the most natural when attempting to parse multiple boxscores in a script, or when you don’t know the URL for a particular game. As an alternative to the above, you can use the schedule module to grab the boxscore URI, or call the Boxscore class directly without worrying about links and URIs:

Get a boxscore link for each game in a team’s schedule
The above example iterates through every game in the Houston Astro’s schedule for the most recent season and both prints the boxscore index (like the BOS/BOS20180808020 example we saw above) as well as creates a boxscore object representing the specific game in the iteration which can be used in the same way as the previous example.
Image for post
Photo by Alturas Homes from Pexels
Players
The final module I will discuss here is dedicated to all of the athletes out there. Teamwork is paramount to success in sports, but a team can’t exist without individual contributions.
sportsreference enables us to dive into a player’s career and identify record performances, career totals, and yearly trends. To get started, we must first find a player’s ID. In general, the player ID is a string in the format lllllffnn where lllll is the first five letters of the player’s last name, ff is the first two letters of the player’s first name, and nn is a number starting at 01 for the first time that player ID has been used and increments by 1 for every successive player. For example, the player ID for the former Detroit Red Wings star Henrik Zetterberg is zettehe01. The ID can also be grabbed by navigating to the player’s individual stats page and capturing the string between the last "/" and ".html". Similar to the boxscore module, however, a list of player names and IDs can be retrieved from the Player class which I will dive into shortly.
To print the career stats for Henrik Zetterberg, we just need the player ID using any method above, and apply it to the Player class:

Print name, points, and games played for an individual NHL player
This sample prints Henrik Zetterberg’s full name, plus the total number of points he obtained, and the total number of games he played over his NHL career. It also prints a DataFrame of all relevant statistical categories he has achieved. Not only does the DataFrame contain his career stats, but it also prints his stats on a year-by-year basis where each row in the frame represents a different season.
If just a single season is desired, a string specifier can be used in a call to the class instance so only that season is returned:

Print name, points, and games played for a single season for an NHL player
The above will print Zetterberg’s full name, his points, and the number of games he played just liked before, but this time, only for the 2017–2018 season. To resume querying career stats, simply call the class instance again but instead of passing a season, specify 'career'.
Lastly, as mentioned at the beginning of this section, a team’s entire roster can be requested at once and individual players iterated upon from there. Instead of calling the Player class, we will instead use the Roster class:

Print the name and career games total for every player on an NHL team
This snippet grabs every player on the current Detroit Red Wings roster and iteratively prints their name and the number of games they’ve played in their career.
Image for post
Photo by Luke Ellis-Craven on Unsplash
Extending sportsreference
As you can hopefully see by this point, sportsreference enables you to collect a wide range of stats, many of which I didn’t cover here, in just a few lines of Python code, enabling you to focus on doing something with data instead of finding data. While the examples above are a simple overview of how to use sportsreference, I feel it is only fair to show a few ways that you can connect various modules and create analyses of your own.
This first sample iterates through every game for every NCAAB team in the current or most recent season and prints several advanced metrics for each game. Notice that though I use functionality from the teams, schedule, and boxscore modules, I only import and directly instantiate a single class. sportsreference takes care of the interconnections between classes so I don’t have to worry about that in my code.

Print several advanced metrics for every NCAAB game for each team in the current season
This second example combs through every NBA team and finds and displays the tallest player on each squad. A great advantage of using sportsreference is that you can find information like this without needing to store data in a database and making unique queries on said database. So long as you have the latest version of sportsreference and an internet connection, you can pull information exactly like this without setting up any other hardware or software.

Find the tallest player on the current roster for all NBA teams
For my last example, I simply run from the 2000 season until the 2018 season (remember that the range function in Python has a soft upper-bound so the year 2019 will not be tested here) and check the number of wins each MLB team gained each year and print the team with the most victories.

Find and print the name and number of wins for the MLB team with the most victories by year
Image for post
Off to the races!
Off to the races!
Now that you know the basic usage of sportsreference, you should hopefully now be able to write programs of your own that rely on sports statistics. Note that while all of the samples above demonstrate how easy it is to use sportsreference, I only showed a very small subset of stats that can be pulled from the package. I documented the approximately 1,000 supported unique metrics at readthedocs.org for those interested.
Thanks for the read — now Go! Fight! Win! and create an awesome sports project of your own! Already have a project that uses sportsreference? Comment below as I would love to hear more! ''',

                '12': '''The Mathematics of Machine Learning
Wale Akinfaderin
Wale Akinfaderin
Follow
Mar 23, 2017 · 4 min read



In the last few months, I have had several people contact me about their enthusiasm for venturing into the world of data science and using Machine Learning (ML) techniques to probe statistical regularities and build impeccable data-driven products. However, I have observed that some actually lack the necessary mathematical intuition and framework to get useful results. This is the main reason I decided to write this blog post. Recently, there has been an upsurge in the availability of many easy-to-use machine and deep learning packages such as scikit-learn, Weka, Tensorflow, R-caret etc. Machine Learning theory is a field that intersects statistical, probabilistic, computer science and algorithmic aspects arising from learning iteratively from data and finding hidden insights which can be used to build intelligent applications. Despite the immense possibilities of Machine and Deep Learning, a thorough mathematical understanding of many of these techniques is necessary for a good grasp of the inner workings of the algorithms and getting good results.
Why Worry About The Maths?
There are many reasons why the mathematics of Machine Learning is important and I will highlight some of them below:
Selecting the right algorithm which includes giving considerations to accuracy, training time, model complexity, number of parameters and number of features.
Choosing parameter settings and validation strategies.
Identifying underfitting and overfitting by understanding the Bias-Variance tradeoff.
Estimating the right confidence interval and uncertainty.
What Level of Maths Do You Need?
The main question when trying to understand an interdisciplinary field such as Machine Learning is the amount of maths necessary and the level of maths needed to understand these techniques. The answer to this question is multidimensional and depends on the level and interest of the individual. Research in mathematical formulations and theoretical advancement of Machine Learning is ongoing and some researchers are working on more advance techniques. I will state what I believe to be the minimum level of mathematics needed to be a Machine Learning Scientist/Engineer and the importance of each mathematical concept.
Image for post
Linear Algebra: A colleague, Skyler Speakman, recently said that “Linear Algebra is the mathematics of the 21st century” and I totally agree with the statement. In ML, Linear Algebra comes up everywhere. Topics such as Principal Component Analysis (PCA), Singular Value Decomposition (SVD), Eigendecomposition of a matrix, LU Decomposition, QR Decomposition/Factorization, Symmetric Matrices, Orthogonalization & Orthonormalization, Matrix Operations, Projections, Eigenvalues & Eigenvectors, Vector Spaces and Norms are needed for understanding the optimization methods used for machine learning. The amazing thing about Linear Algebra is that there are so many online resources. I have always said that the traditional classroom is dying because of the vast amount of resources available on the internet. My favorite Linear Algebra course is the one offered by MIT Courseware (Prof. Gilbert Strang).
Probability Theory and Statistics: Machine Learning and Statistics aren’t very different fields. Actually, someone recently defined Machine Learning as ‘doing statistics on a Mac’. Some of the fundamental Statistical and Probability Theory needed for ML are Combinatorics, Probability Rules & Axioms, Bayes’ Theorem, Random Variables, Variance and Expectation, Conditional and Joint Distributions, Standard Distributions (Bernoulli, Binomial, Multinomial, Uniform and Gaussian), Moment Generating Functions, Maximum Likelihood Estimation (MLE), Prior and Posterior, Maximum a Posteriori Estimation (MAP) and Sampling Methods.
Multivariate Calculus: Some of the necessary topics include Differential and Integral Calculus, Partial Derivatives, Vector-Values Functions, Directional Gradient, Hessian, Jacobian, Laplacian and Lagragian Distribution.
Algorithms and Complex Optimizations: This is important for understanding the computational efficiency and scalability of our Machine Learning Algorithm and for exploiting sparsity in our datasets. Knowledge of data structures (Binary Trees, Hashing, Heap, Stack etc), Dynamic Programming, Randomized & Sublinear Algorithm, Graphs, Gradient/Stochastic Descents and Primal-Dual methods are needed.
Others: This comprises of other Math topics not covered in the four major areas described above. They include Real and Complex Analysis (Sets and Sequences, Topology, Metric Spaces, Single-Valued and Continuous Functions, Limits, Cauchy Kernel, Fourier Transforms), Information Theory (Entropy, Information Gain), Function Spaces and Manifolds.
Some online MOOCs and materials for studying some of the Mathematics topics needed for Machine Learning are:
Khan Academy’s Linear Algebra, Probability & Statistics, Multivariable Calculus and Optimization.
Coding the Matrix: Linear Algebra through Computer Science Applications by Philip Klein, Brown University.
Linear Algebra — Foundations to Frontiers by Robert van de Geijn, University of Texas.
Applications of Linear Algebra, Part 1 and Part 2. A newer course by Tim Chartier, Davidson College.
Joseph Blitzstein — Harvard Stat 110 lectures.
Larry Wasserman’s book — All of statistics: A Concise Course in Statistical Inference.
Boyd and Vandenberghe’s course on Convex optimization from Stanford.
Linear Algebra — Foundations to Frontiers on edX.
Udacity’s Introduction to Statistics.
Finally, the main aim of this blog post is to give a well-intentioned advice about the importance of Mathematics in Machine Learning and the necessary topics and useful resources for a mastery of these topics. However, some Machine Learning enthusiasts are novice in Maths and will probably find this post disheartening (seriously, this is not my aim). For beginners, you don’t need a lot of Mathematics to start doing Machine Learning. The fundamental prerequisite is data analysis as described in this blog post and you can learn the maths on the go as you master more techniques and algorithms. ''',

                '13': '''Peeking under the S&P+ hood: Second-order wins
23
Which teams have been particularly fortunate (Florida State, Arizona, Bowling Green) or unfortunate (Pitt, Indiana) this season? Let's use second-order wins to explore.

By Bill C.@SBN_BillC  Dec 16, 2014, 9:00am EST
Share this story
Share this on Facebook (opens in new window)
Share this on Twitter (opens in new window)
SHARE
All sharing options

Jeremy Brevard-USA TODAY Sports
The ratings redesign process is going well, thanks for asking! I discussed it a bit last week, and as I continue to tinker, I'm coming up with numbers that look pretty good from a retrodictive perspective (the end-of-season rating seems to be getting between 80-81 percent of past results correct) and phenomenal from a predictive perspective.

There's still some tweaking to do to make sure I'm not overfitting, but I've simulated the 2013 and 2014 seasons, week by week, and right now the new measure is hitting about 54.5 percent against the spread and about 76 straight up. Going by the results here, that's about as good as you're going to find over a two-year period. And I'm tinkering with the idea of presenting the ratings in terms of point values, which would allow anybody to quickly look at teams' ratings, apply a home-field advantage where appropriate, and come up with a general "Team A would likely beat Team B by 6.6 points" estimation.

Right after I posted my Under the Hood piece last Thursday, it hit me that I was thinking way too hard about the whole "where's the balance between predictive and retrodictive?" thing, and the responses to that post certainly solidified that. It seems the best way to approach ratings is to make them as predictive as possible, period. But in looking back at past results, it is useful to still provide clues regarding which teams have been overachieving, underachieving, lucky, unlucky, et cetera.

That's where things like Pythagorean records can come in handy. It is a popular approach for many sports -- in this instance, the Wikipedia entry basically tells you everything you need to know (the short version: look at points/runs scored and allowed, apply an exponent, and produce a team's most likely win percentage) -- and it is good at telling you which teams are likely punching above their weight and are due some regression.

There are exponents available for turning college football points into a Pythagorean win percentage, but I'm more interested in another concept: second-order wins. That basically takes the same idea but uses advanced stats of some sort to determine not simply what you did score and allow, but what you should have scored and allowed.

My new ratings are based on margins in categories related to my Five Factors: efficiency, explosiveness, field position, finishing drives, turnovers/luck. As I flesh the system out with previous years of data, I'm able to basically use these margins to determine both what was your most likely scoring margin in a given game and, based on the plays that took place, your likelihood of winning a given game.

To further explain the second part of that last sentence, it basically says "If you took all the plays in this game, tossed them up in the air, and had them land in a random order, you'd win this game XX% of the time." It is a single-game win likelihood concept, and with it, we can look at wins and losses not as zeroes and ones, but as percentages. And if you're winning a lot of "You'd have won this game 60 percent of the time" games, you're probably getting a little bit lucky. And as with everything else, that luck is likely to change over time.

So who's been particularly fortunate or unfortunate in 2014? Let's take a look.

Team	Games	Wins	Second-order Wins	Diff	Rank
Florida State	13	13	9.6	-3.4	128
Arizona	13	10	7.5	-2.5	127
Bowling Green	12	7	4.9	-2.1	126
Utah	12	8	6.1	-1.9	125
Northern Illinois	13	11	9.2	-1.8	124
Missouri	13	10	8.2	-1.8	123
Rutgers	12	7	5.3	-1.7	122
Ohio	12	6	4.5	-1.5	121
Clemson	12	9	7.6	-1.4	120
North Carolina	12	6	4.7	-1.3	119
UCLA	12	9	7.7	-1.3	118
Duke	12	9	7.9	-1.1	117
Colorado State	12	10	9.0	-1.0	116
UTEP	12	7	6.0	-1.0	115
Hawaii	13	4	3.0	-1.0	114
Illinois	12	6	5.0	-1.0	113
Michigan State	12	10	9.0	-1.0	112
Central Florida	12	9	8.0	-1.0	111
Boise State	13	11	10.0	-1.0	110
Nevada	12	7	6.1	-0.9	109
Cincinnati	12	9	8.1	-0.9	108
Baylor	12	11	10.1	-0.9	107
West Virginia	12	7	6.2	-0.8	106
LSU	12	8	7.3	-0.7	105
Old Dominion	12	6	5.3	-0.7	104
Mississippi State	12	10	9.3	-0.7	103
Marshall	13	12	11.3	-0.7	102
USC	12	8	7.4	-0.6	101
Team	Games	Wins	Second-order Wins	Diff	Rank
Alabama	13	12	11.4	-0.6	100
South Florida	12	4	3.4	-0.6	99
TCU	12	11	10.4	-0.6	98
Toledo	12	8	7.5	-0.5	97
Wake Forest	11	2	1.5	-0.5	96
Ohio State	13	12	11.5	-0.5	95
Wyoming	12	4	3.5	-0.5	94
Texas State	12	7	6.6	-0.4	93
Minnesota	12	8	7.6	-0.4	92
Oklahoma State	12	6	5.6	-0.4	91
Texas A&M	12	7	6.6	-0.4	90
South Carolina	12	6	5.6	-0.4	89
NC State	12	7	6.6	-0.4	88
Kansas State	12	9	8.7	-0.3	87
South Alabama	12	6	5.7	-0.3	86
Washington	13	8	7.7	-0.3	85
Georgia Tech	13	10	9.7	-0.3	84
Fresno State	13	6	5.7	-0.3	83
Nebraska	12	9	8.7	-0.3	82
Vanderbilt	12	3	2.7	-0.3	81
Air Force	12	9	8.8	-0.2	80
Western Kentucky	12	7	6.8	-0.2	79
UL-Lafayette	12	8	7.8	-0.2	78
Tulsa	12	2	1.8	-0.2	77
Arizona State	12	9	8.8	-0.2	76
Team	Games	Wins	Second-order Wins	Diff	Rank
Southern Miss	12	3	2.9	-0.1	75
Rice	12	7	6.9	-0.1	74
Tennessee	12	6	5.9	-0.1	73
Penn State	12	6	5.9	-0.1	72
Middle Tennessee	12	6	5.9	-0.1	71
Eastern Michigan	12	2	1.9	-0.1	70
Appalachian State	12	7	7.0	0.0	69
California	12	5	5.0	0.0	68
Wisconsin	13	10	10.0	0.0	67
Ball State	12	5	5.0	0.0	66
Buffalo	11	5	5.0	0.0	65
Memphis	12	9	9.0	0.0	64
Oregon	13	12	12.0	0.0	63
Akron	11	5	5.0	0.0	62
Northwestern	12	5	5.1	0.1	61
Auburn	12	8	8.1	0.1	60
Iowa State	12	2	2.1	0.1	59
UAB	12	6	6.1	0.1	58
Virginia Tech	12	6	6.1	0.1	57
New Mexico State	12	2	2.1	0.1	56
Houston	12	7	7.1	0.1	55
UL-Monroe	12	4	4.2	0.2	54
Arkansas State	12	7	7.2	0.2	53
BYU	12	8	8.2	0.2	52
Georgia Southern	12	9	9.2	0.2	51
Team	Games	Wins	Second-order Wins	Diff	Rank
Purdue	12	3	3.2	0.2	50
SMU	12	1	1.3	0.3	49
Kentucky	12	5	5.3	0.3	48
Syracuse	12	3	3.3	0.3	47
Maryland	12	7	7.3	0.3	46
Oregon State	12	5	5.4	0.4	45
Tulane	12	3	3.4	0.4	44
New Mexico	12	4	4.4	0.4	43
Florida International	12	4	4.4	0.4	42
Oklahoma	12	8	8.4	0.4	41
Ole Miss	12	9	9.4	0.4	40
Iowa	12	7	7.4	0.4	39
North Texas	12	4	4.4	0.4	38
Texas Tech	12	4	4.5	0.5	37
Navy	11	6	6.5	0.5	36
UTSA	12	4	4.6	0.6	35
Florida Atlantic	12	3	3.6	0.6	34
Michigan	12	5	5.6	0.6	33
Troy	12	3	3.6	0.6	32
Temple	12	6	6.6	0.6	31
Western Michigan	12	8	8.6	0.6	30
Virginia	12	5	5.6	0.6	29
Louisville	12	9	9.7	0.7	28
Georgia	12	9	9.7	0.7	27
UNLV	13	2	2.8	0.8	26
Team	Games	Wins	Second-order Wins	Diff	Rank
Army	11	4	4.8	0.8	25
Notre Dame	12	7	7.8	0.8	24
Texas	12	6	6.8	0.8	23
Connecticut	12	2	2.8	0.8	22
Miami	12	6	6.9	0.9	21
Utah State	13	9	9.9	0.9	20
San Diego State	12	7	7.9	0.9	19
Georgia State	12	1	2.0	1.0	18
San Jose State	12	3	4.0	1.0	17
Arkansas	12	6	7.0	1.0	16
Idaho	11	1	2.0	1.0	15
Central Michigan	12	7	8.1	1.1	14
Kansas	12	3	4.1	1.1	13
East Carolina	12	8	9.1	1.1	12
Boston College	12	7	8.1	1.1	11
Washington State	12	3	4.1	1.1	10
Louisiana Tech	13	8	9.1	1.1	9
Florida	11	6	7.2	1.2	8
Stanford	12	7	8.4	1.4	7
Massachusetts	12	3	4.5	1.5	6
Colorado	12	2	3.5	1.5	5
Indiana	12	4	5.6	1.6	4
Miami (Ohio)	12	2	3.8	1.8	3
Kent State	10	1	3.0	2.0	2
Pittsburgh	12	6	8.2	2.2	1
So basically, Florida State, Arizona, and BGSU, not to mention Utah, NIU, Mizzou, Rutgers, and others, have been getting by on smoke and mirrors to some degree. Meanwhile, Pitt has been figuring out ways to lose games it had no business losing.

So what does this mean? It's hard to conclude anything too drastic before I have data set up for all previous years, but here's something worth noting: your second-order win totals, or at least the difference between your wins and second-order wins, were a pretty good predictor of progression or regression last year.

The four schools with a difference (second-order wins vs. wins) of minus-2 or lower in 2013 (Oklahoma, Nebraska, UCF, ULM) saw their win percentage decrease by about 0.130 in 2014. Nebraska improved slightly (from 9-4 to 9-3), and Oklahoma (11-2 to 8-4), UCF (12-1 to 9-3), and ULM (6-6 to 4-8) all fell by a solid margin. Oklahoma (minus-3.08), by the way, was far and away the most fortunate team in the country last year in terms of second-order wins.
The 18 schools with a difference between minus-1 and minus-2 saw their win percentage decrease by an average of 0.102 in 2014.
The 44 schools with a difference between zero and minus-1 saw their win percentage decrease by an average of 0.044.
The 43 schools with a difference between zero and plus-1 saw their win percentage increase by an average of 0.075.
The 13 schools with a difference between plus-1 and plus-2 saw their win percentage increase by an average of 0.094.
The three schools with a difference of plus-2 or higher (Georgia State, Temple, TCU) saw their win percentage increase by an average of 0.333. All three improved, and TCU improved significantly.
However I end up laying out my new ratings and data, I figure this is a concept worth sharing from week to week. Right now, it appears these ratings are pretty damn good, and this second-order win total might be a pretty good predictor of future good or bad fortune.

More soon. ''',

                '14': '''Possession Efficiency Notes

I'm frequently asked questions about the origins of my work with college football data. After witnessing a 2002 victory by Boston College over Notre Dame, a game in which the Eagles failed to advance a single offensive drive across midfield, I had questions that traditional box scores were unable to sufficiently answer. I began collecting possession data soon thereafter; to define the fluid value of field position, quantify the impact of turnovers and special teams, evaluate offensive and defensive team strengths, and develop new measures of success. The Fremeau Efficiency Index (FEI) and other possession statistics found on this site are the results of those initial inquiries, and many more since.

These notes, detailing my approach to evaluating possession efficiency and providing additional context to the numbers, are intended especially to prompt new questions and inspire more contributions to the college football analytics community.

Contact me via email at bcfremeau at gmail.com and follow me on Twitter @bcfremeau. 

 

Game Results

FBS (Football Bowl Subdivision) college football teams generally schedule 12 regular season opponents, and sometimes play additional post-season games in conference championships, bowl matchups, and in the four-team College Football Playoff to conclude the season. The vast majority of games played are against fellow FBS opponents, but many teams also schedule one (or more) games against FCS (Football Championship Subdivision) opponents. The results of those FBS vs FCS games are not included in the data sets used in my analysis.

Why? FEI team and unit ratings published here are opponent-adjusted, and I'm not comfortable making such adjustments without confidence in the relative strength of each opponent. I have not yet developed FCS team or unit ratings I can trust. Further, FBS vs FCS games are frequently mismatched, and possession results from these games can skew a team's unadjusted possession efficiency data. I prefer to maintain a closed FBS vs FBS data set.

 

Possession Types

College football games are contested as a series of alternating possessions between two teams. A possession typically consists of a scrimmage play or series of plays in which the team in control of the ball attempts to advance the ball in order to score while its opponent attempts to deny that effort. I define possession types as follows:

Offensive Drives (96.7 percent of all possessions) consist of at least one scrimmage play run by an offense in possession against the opposing team defense. Drives conclude in one of eight ways: touchdown, field goal attempt, punt, turnover on downs, fumble, interception, safety, or time expiring at the end of the half.
Field Goal Attempt Possessions (only 0.02 percent of all possessions) are situations in which, due to limited time remaining at the end of the half, no offensive scrimmage plays are run and only a field goal is attempted.
Defensive Possessions (1.1 percent of all possessions) are initiated as a result of an opponent interception or fumble and, with the defense in control of the ball, conclude on the same play in one of three ways: touchdown, fumble recovered by the offense, or safety.
Special Teams Possessions (1.7 percent of all possessions) are kickoff or punt return events that conclude in one of four ways: touchdown, fumble recovered by the kickoff or punt team, onside kick recovered by the kickoff team, or safety.
Overtime Possessions (0.5 percent of all possessions) include overtime offensive drives (teams alternate drives begun at the opponent's 25-yard line), overtime field goal attempt possessions, overtime defensive possessions, and (as of a rule change in 2019) overtime conversion possessions in which beginning with the 5th overtime, teams alternate two-point conversion scoring attempts from the opponent's 3-yard line.
From 2007 to 2019, FBS games have averaged 26.5 total game possessions.


 

Garbage vs Non-Garbage Possessions

Unless otherwise noted, all ratings and supporting data are calculated only after first filtering out garbage possessions, defined as of February 2020, as follows:

An offensive possession of two plays or fewer that runs out the clock to conclude the first half and does not result in a turnover, score, or field goal attempt.
An offensive possession of two plays or fewer that runs out the clock to conclude the second half with the score tied and does not result in a turnover, score, or field goal attempt.
A possession in the second half of a game in which eight times the number of the losing team's remaining possessions plus one is less than the losing team's scoring deficit at the start of the possession.
An offensive possession of two plays or fewer by the losing team with a score deficit greater than eight points that runs out the clock to conclude the game.
An offensive possession or non-offensive scoring possession by the winning team leading by eight points or fewer at the start of the possession that runs out the clock to conclude the game.
From 2007 to 2019, 10.5 percent of all possessions have been classified as garbage possessions according to these criteria. FBS games have averaged 23.7 non-garbage possessions per game in that span. ''',

                '15': '''To Be Truly Effective in Life . . .
Neurohacker Collective
Neurohacker Collective
Follow
Jan 10, 2017 · 3 min read



Forrest Landry has a wide-ranging output of brilliance to offer the world, from large scale software systems design employed by various agencies of government, to engineering and master woodworking. But perhaps his most compelling contribution is his insights in metaphysics, with works such as An Immanent Metaphysics and Tiny Book Of Essential Wisdom. In this piece, Forrest examines the topic of effectiveness. Allow yourself a clean mental slate with regards to what effectiveness means to you, and allow Forrest to define the word in a perhaps more thoughtful framework than you’ve considered before.
Image for post
To be truly effective in life, one needs to be able:
To desire clarity, rather than just simplicity.
To value diversity, rather than just to value solidarity.
To desire choice, rather than just comfort or security.
To focus on the future and the moment,
rather than just on the past.
To have vision, rather than to have only sight.
To hear as well as to see.
To deeply feel, as well as to quickly think.
To synthesize, rather than to merely analyze.
To focus awareness on one’s loves,
rather than on one’s fears and anger.
To focus on spirit, rather than on just matter.
To focus on mind, rather than on just body.
To focus on quality (qualia),
rather than on just quantity (quanta).
To focus on similarity, rather than on just difference.
To focus on context, rather than on just content.
To focus on that which is organic,
rather than that which is mechanistic.
To focus on meaning (inner values)
rather than on just purpose or just (monetary) value.
To focus on possibility, rather than on just actuality.
To focus on creation,
rather than on just that which already exists.
To focus on expression, rather than on just perception.
To focus on communication, rather than on just information.
To focus on the spiritual, rather than on just the physical.
To focus on the infinite, rather than on just the measurable.
To focus on the small, rather than on just the large.
To focus on depth, rather than on just speed.
To focus on creativity, rather than on just control.
To focus on continuity, rather than on just symmetry.
To focus on the beautiful and inspirational,
rather than that which is just practical.
To focus on that which is within,
rather than on that which is without.
To focus on inner strength, rather than on external power.
To focus on how one already has freedoms,
rather than on what are one’s (seeming) limitations.
To focus on the ways something is true,
rather than on just the ways something is false.
To focus on cooperation (peace),
rather than on just competition (war).
To focus on the sacred, rather than on just the mundane.
To focus on what is already right,
rather than on what could go wrong.
To focus on the subjective, rather than on just the objective.
To focus on the myths, rather than on just the facts.
To focus on the unknowable, rather than on just the known.
To focus on soundness, rather than on just validity.
To focus on environment, rather than on just self.
To focus on desire, rather than on just want or need.
To focus on health, rather than on just wealth.
To focus on attaining joy, rather than on just avoiding pain. ''',

                '16': '''Evaluating gambles using dynamics
Chaos 26, 023103 (2016); https://doi.org/10.1063/1.4940236
 O. Peters1, a) and M. Gell-Mann2, b)
View Affiliations
 PDF	 
TOPICS
Hamiltonian mechanics
Ecology
Mathematical modeling
Dimensional analysis
Stochastic processes
Statistical thermodynamics
Game theory
Decision theory
Entropy
Growth factors
ABSTRACT
Gambles are random variables that model possible changes in wealth. Classic decision theory transforms money into utility through a utility function and defines the value of a gamble as the expectation value of utility changes. Utility functions aim to capture individual psychological characteristics, but their generality limits predictive power. Expectation value maximizers are defined as rational in economics, 
but expectation values are only meaningful in the presence of ensembles or in systems with ergodic properties, whereas decision-makers have no access to ensembles, and the variables representing wealth in the usual growth models do not have the relevant ergodic properties. Simultaneously addressing the shortcomings of utility and those of expectations, we propose to evaluate gambles by averaging wealth growth over time. 
No utility function is needed, but a dynamic must be specified to compute time averages. Linear and logarithmic “utility functions” appear as transformations that generate ergodic observables for purely additive and purely multiplicative dynamics, respectively. We highlight inconsistencies throughout the development of decision theory, whose correction clarifies that our perspective is legitimate. 
These invalidate a commonly cited argument for bounded utility functions.
Over the past few years, we have explored a conceptually deep, simple, change of perspective that leads to a novel approach to economics. Much of current economic theory is based on early work in probability theory, performed specifically between the 1650s and the 1730s. This foundational work predates the development of the notion of ergodicity, and it assumes that expectation values reflect what happens over time. 
This is not the case for stochastic growth processes, but such processes constitute the essential models of economics. As a consequence, nowadays expectation values are often used to evaluate situations where time averages would be appropriate instead, and the result is a “paradox,” “puzzle,” or “anomaly.” This class of problems, including the St. Petersburg paradox and the equity-premium puzzle, 
can be resolved by ensuring the following: the stochastic growth process involved in the problem needs to be made explicit; the process needs to be transformed to find an appropriate ergodic observable. The expectation value of the new observable will then indeed reflect long-time behavior, and the puzzling essence of the problem will go away. Here we spell out the general recipe, which we phrase as the solution to the general gamble problem that stood at the beginning of the debate in the 17th century. We hope that this recipe will resolve puzzles in many different areas. ''',

                '17': '''On Sovereignty
Jordan Hall
Jordan Hall
Follow
Feb 19, 2018 · 9 min read



It might very well be the case that 2018 will be known as the “Year of Jordan Peterson”.
If you happen to have read anything that I’ve written, you will have noticed that I come from a very different place than Dr. Peterson. I spend most of my time in high abstraction, thinking about global systems and long term dynamics. Not about how important it is to clean your room. Accordingly, if you are thinking, you might be puzzled. Just what could I mean by proposing that Peterson is not merely popular nor controversial. But that he is important and precisely of the moment.
In this essay, I will endeavor to explain. Naturally, I will be using my own personal approach to making sense of things. So if you are a Dr. Peterson aficionado, this might be a bit of an odd journey. Perhaps you might consider this an invitation down a particular rabbit hole. I wouldn’t be spending the time to write this if I didn’t think it worth your time. But, of course, the choice is entirely yours.
I would like to begin with a concept that I think is both deeply powerful and not broadly used. In this case, I’m going to be treading the dangerous waters of trying to articulate something that is similar to, and therefore might be mistaken for, a bunch of other concepts that are kind of in the same space.
I’m going to take the bold path and challenge you to really think. I’m going to intentionally use a word that typically comes loaded with a whole lot of “understanding.” And I’m going to re-load that word with a meaning that I believe is much more clear and true and useful.
That word is “sovereignty.”
By sovereignty, I do not mean the notion that nation-states have the right to self-determination on the geopolitical stage. I also don’t mean that human individuals are magically able to separate themselves from the rest of the human world and make up their own rules. I mean something very specific, very central to being in the world and, if properly understood, very empowering.
Sovereignty is the capacity to take responsibility. It is the ability to be present to the world and to respond to the world — rather than to be overwhelmed or merely reactive. Sovereignty is to be a conscious agent.
As it turns out, sovereignty can be understood as consisting of three distinguishable capacities.
Your ability to relate to the world. This includes things like your ability to perceive the world. Reality. To be sensitive to what is going on in all sorts of different ways. To be able to listen and see. And feel. To “tune in” to what is going on without preemptively closing off the world with your own frames or judgements. Or to be overwhelmed by what the world is sending at you.
Your ability to make sense of the world. This includes your ability to skillfully select frames and concepts that are appropriate to what is really going on. And to create new ones when the old ones won’t do. It is a measure of both speed and precision. Move too slowly and the world has passed you by. Move too haphazardly and you will confuse sense with error.
Your ability to make and effect choice in the world. This includes both the ability to actually move the world with your actions (your ability to deploy a force on the world) and your capacity to do so with both wisdom and elegance. That is, your ability to move from sense to action with sound judgement (to make good choices) and your ability to do just and only what you intend. No more, no less. And with as little effort as necessary.
Of course, these capacities overlap and mingle with each-other. This distinction is merely a way of looking at things that might prove helpful in your own practices of sovereignty.
Consider, for example, that a major challenge to sovereignty is an imbalance of these capacities. If you have much more ability to perceive the world than you have ability to act in the world, you might feel powerless and non-responsive. If you have much more ability to act than you have the ability to make sense, you might find yourself doing more harm than good.
Then of course, you have the relationship between your own sovereignty and the world that you are trying to navigate. As an infant, your sovereignty is minuscule and you are entirely dependent on other people to help you survive and, hopefully, to increase your own sovereignty.
As you develop, if you are lucky, you learn something. You increase your ability to relate to the world and to make sense of it. And, ultimately to make good choices. This is a virtuous cycle. The more good choices you make, the better positioned you are to make good choices in the future.
The opposite is also true. If and as you get off track, your sovereignty gets overwhelmed and you get out of balance. Like a boxer who has been stunned by a blow, you might find yourself no longer able to skillfully respond to the world. Not in a good position to make good choices; and all too likely to get yourself into trouble.
Sovereignty is the center. If you are anchored in sovereignty and able to fully respond to the world, you are able to do the best you can do. It might not be enough, but it is the best you can do. If you are out of sovereignty, try as you might, you will not be giving your best. And, in the process, you might likely find yourself making things (and yourself) worse off in the process.
Thus it is that growing your sovereignty, improving your ability to fully respond to the world, is a singularly useful pursuit.
In this pursuit, perhaps you will discover the value of developing two specific capabilities. The first: awareness. Are you equal to the circumstances you find yourself in, or are you in over your head? Are you swimming effortlessly, or are you starting to struggle? Is your sovereignty increasing or is it beginning to falter? Or has it gone altogether and you have plunged into reaction?
This is an omnipresent challenge. You never know what is going to happen. The world is a crazy place and we are all deeply vulnerable. One moment you might be the rock of Gibraltar, able to face the world with equanimity and competence. The next, something has happened and you are a seething teenager, barely able to avoid slamming the door and stomping away. You can get better and better at responding to the world, more resilient in your sovereignty. But you never know what is going to happen and being aware of where you really are is a useful thing.
And then you might also be well served by building a repertoire of skills and practices for regaining your sovereignty when you have stumbled. The world is rich with such things, and many of them work. I have found breathing to be enormously useful. Specifically, I have worked on a habit of taking deep breaths throughout the day. When I feel like I’m moving out of sovereignty, I can use this habit to slow things down with a few breaths and then to recenter myself.
There are a lot of good practices out there and many good teachers. But getting good at regaining your sovereignty when you have been knocked out of balance is no joke. This is a something that takes time and effort. Moreover, it is not something that you can be taught. You can be invited to the work, but you must undertake it yourself.
And then there is the issue of maintaining your sovereignty. This is also an art. You must become sensitive to things like nutrition and sleep, to the kind of media you consume and the relationships you maintain. You are an enormously complex creature and every aspect of your total environment plays a role in your sovereignty.
Sadly, for all of its wealth and power, our contemporary environment does a rather poor job at helping us in this work. Our media deceives and manipulates us. Much of our food is only a simulation of nutrition. Our ideologies are often confused and self-destructive — leading us away from rather than towards a position of sovereignty and responsibility.
Of course it could be worse. Our ancestors had to deal with cholera and the killing cold of winter. As they say, “it is what it is.” You are here, now, and this is the world you must navigate. And this is the life for which you are responsible.
Hence the deep wisdom of Dr. Peterson’s injunction: “clean your room”. Sort yourself out. First. When it comes to relating to the world, remember, the world starts with you. Before you can begin to extend yourself into the complex dance of the larger universe, you need to get a handle on yourself. You need to achieve balance, to improve your sovereignty. And then a mastery of maintaining that balance and regaining it when lost. Only then can you proceed into the problems of the outside world.
These days that might seem like a bit of a burden. In the past it was merely called “being an adult.”
It seems odd that in this moment of so much consequence, when it is possible that everything is at stake and that we are at the threshold of unspeakable power that the most wise and most intelligent thing that can be urged is “grow the hell up.”
But consider Stewart Brand. In 1968, he opened the Whole Earth Catalog: “we are as gods and might as well get good at it.” At that quintessential moment of the Boomers coming of age, he sensed a choice.
In the 20th Century, humanity had crossed a Rubicon. The powers unlocked by science and technology had put us onto a path of exponentially growing power.
For the totality of human existence until 1945, we could do terrible things, but we couldn’t put the entire species at risk. Then, suddenly, in the Atomic Age we found ourselves faced with the real possibility of ending everything as a result of an excess of power and a lack of wisdom.
So far, we’ve managed not to end the story. But history hasn’t even slowed down. Every day we increase our ability to deploy force in the world. Increasingly, we are bulls in a china shop. And so, in 2009 an older (and perhaps wiser) Brand revised his maxim. “We are as gods and we must get good at it.”
In other words, we need to grow the hell up and take the responsibility that is ours to take.
This is no easy task. In fact, it appears to be excruciating. We seem to have become enthralled with increasing our power without appropriate regard to increasing the sovereignty necessary to wisely deploy that power. Does Mark Zuckerberg have the sovereignty to be controlling something as forceful as Facebook? Do the folks at Google have the sovereignty to be choosing how our collective intelligence perceives the world? Does anyone? Could anyone?
Hmm. And what of nanotechnology and AI?
I’m not pointing fingers here. We are, all of us, faced with the same basic set of choices. Are we taking full responsibility? Are we being careful to grow our sovereignty in alignment with our power? Are we able to take complete responsibility for what we find ourselves capable of doing?
Here is the final thing. No one is going to come close to being able to do this on their own. And no one is coming to save us. We are it.
If this seems overwhelming, return to Jordan Peterson. Yes, the world is in trouble. And yes, we are going to need to do incredible things to make it through this transition. But until you have achieved your own sovereignty, you are as likely to make it worse as you are to make it better. Thus the task is simple. Whether you are seated at the throne of Empire or are struggling to just make ends meet, the right, best and only path begins at the center of you. Clean your room. Get yourself sorted out. Build yourself into a rock upon which profound things can be set. Then, and only then, is it time to begin taking care of the rest of the world.
Slowly and deliberately become a master of your own sovereignty. And then, find the load that is yours to carry and carry it. ''',

                '18': '''PETER THIEL'S RELIGION
Peter Thiel's Religion
"I am the Lord your God.” — 1st Commandment

Human culture began with a murder. That culture was fueled by rage and rivalry, which led to violence. Managing that violence is the secret reason for all religious and political institutions. 

In The Bible, The Cain and Abel story is the first act of life after the Garden of Eden. Cain is a farmer and the older brother to Abel, who is a shepherd. Initially, Cain admires Abel. But eventually, when Cain turns envious of his younger and more successful brother, he kills him. The two brothers represent two halves of the human psyche: Abel represents the part that looks up towards the transcendent, where Cain represents the other that looks down towards death and destruction.

Depending on who you ask, the significance of the Cain and Abel story ranges from nothing to everything. For some, the Christian cross is too strange to be taken seriously. It’s archaic and stuck inside a biblical world that can no longer speak to the challenges of life with iPhones, Tinder, and $12 avocado toast. But to others, religion is the foundation of human culture. Without it, peace cannot be maintained and violence will erupt like an angry volcano. 

What does Peter Thiel think? Is religion a superfluous add-on or the origin of everything?

In this essay, we’ll explore the significance of religion and the Cain and Abel story. We’ll learn why the story is an archetype for human relationships, even in the Western world where people stiff-arm religion like it’s the Heisman trophy.

We’ll study religion through the lens of Peter Thiel. He’s an investor who found wealth in PayPal, a student who found wisdom in Libertarian ideals, and a philosopher who found faith in the resurrection of Jesus Christ. Thiel was raised as an Evangelical and inherited the Christianity of his parents. But his beliefs are “somewhat heterodox.” In a profile in the New Yorker, Thiel said: “I believe Christianity to be true. I don’t feel a compelling need to convince other people of that.”

Three simple statements will lead us towards our ultimate answer about the importance of religion: 

Don’t copy your neighbors

Time moves forward

The future will be different from the present

Rather than focusing on Thiel’s actions, I’ve chosen to focus on his ideas. First, we’ll explore the principles of Peter Thiel’s worldview. We’ll begin by explaining Thiel’s connection to a French philosopher named Rene Girard. We’ll return to old books like The Bible, old ideas like sacrifice, and old writers like Shakespeare, and see why this ancient wisdom holds clues for modern life. Then, we’ll return to the tenets of the Christian story. We’ll cover the shift from cyclical time to linear time, which was spurred by technological development and human progress. We’ll see why the last book in The Bible,The Book of Revelation, is a core pillar of Thiel’s philosophy. Then, we’ll close with Thiel’s advice and wisdom almost as old as Cain and Abel: the Ten Commandments.

IMG_DB41477003EB-2.jpeg
Some disclaimers: I’ve never met Peter Thiel. The contents of this essay are based on public information and my own intuition. Hopefully, some of it is interesting. Inevitably, some of it is wrong. I am not a Christian and only have a basic understanding of Christian theology. If you agree with everything in this essay, I haven’t challenged you enough. I’ve also chosen an interpretation of the Bible, and especially The Book of Revelation that aligns with Thiel’s philosophy. Thiel fanatics will say I’ve only scratched the surface. Others will say I’ve gone too deep. And both might complain I’ve focused too much on his relationship with Christianity. 

I don’t agree with all of Thiel’s conclusions, but I admire his rigorous and independent thought. By the time you finish reading this essay, you will too. 

I wrote this essay because I’m fascinated by Christianity and impressed with Thiel. I’ve spent the past decade as an agnostic, just like everybody around me. But after a recent change of heart, I’m on a quest to develop my own conclusions about religion. 

This essay is an introduction to his ideas, but it’s not just about Thiel. It’s about modern society, human behavior, and the philosophy of religion. 

Let’s begin.

THIEL’S INTELLECTUAL BACKGROUND
To understand Thiel’s ideas, we need to begin with the person who influenced Peter Thiel more than any other writer: Rene Girard. 

Rene Girard was a French historian and literary critic. He’s famous for Mimetic Theory, which forms the bedrock of Thiel’s worldview. Thiel studied under Girard as an undergraduate at Stanford in the late 1980s. Their relationship stretched beyond the walls of Palo Alto classrooms and became a lifelong friendship. When Girard died, Thiel spoke at the memorial service. 

Mimetic Theory rests on the assumption that all our cultural behaviors, beginning with the acquisition of language by children are imitative. He sees the world as a theatre of envy, where, like mimes, we imitate other people’s desires. His theory builds upon the kinds of books and people that modern people tend to ignore: The Bible, classic fiction writers such as Marcel Proust, and playwrights like Shakespeare.  

Mimetic conflict emerges when two people desire the same, scarce resource. Like lions in a cage, we mirror our enemies, fight because of our sameness, and ascend status hierarchies instead of providing value for society. Only by observing others do we learn how and what to desire. Our Mimetic nature is simultaneously our biggest strength and biggest weakness. When it goes right, imitation is a shortcut to learning. But when it spirals out of control, Mimetic imitation leads to envy, violence, and bitter, ever-escalating violence. 

Mimesis is the Greek word for imitation. Imitation is not the childish, low-level form of behavior that many people think it is. Since humanity would not exist without it, humans aren’t as independent as they think they are. Early psychologists like Sigmund Freud didn’t take imitation seriously enough. In one essay, Thiel described human brains as “gigantic imitation machines.” 

Our capacity for imitation is unconscious. This drive towards imitation separates us from other animals, and historically, it enabled our evolution from earlier primates to humans. Imitation is linked to forms of intelligence that are unique to humans, especially culture and language. 

We’ve known this for centuries. In the time of Shakespeare, the word ape meant both “primate” and “imitate.” Learning and human behavior is learned through imitation. Without it, all forms of culture would vanish. As any dancer will tell you, the heart beats fastest when two people agree to imitate each other and move in perfect sync. These are the moments when time disappears; when years of trust are built in seconds of synchronicity. 

Thiel speaks with a religious reverence for Girard’s theory: 

“[Girard’s ideas are] a portal onto the past, onto human origins, and our history. It’s a portal onto the present and onto the interpersonal dynamics of psychology. It’s a portal onto the future in terms of where we are going to let these Mimetic desires run amok and head towards apocalyptic violence... It has a sense of both danger and hope for the future as well. So it is this panoramic theory... [It’s] super powerful and extraordinarily different from what one would normally hear. There was almost a cult-like element where you have these people who were followers of Girard and it was a sense that we had figured out the truth about the world in a way that nobody else did.”

Thiel credits Girard with inspiring him to switch careers. Before he internalized Girard’s ideas, Thiel was on track to become a lawyer. He worked as an associate for Sullivan & Cromwell in New York City, where the hours were long and the competition was cutthroat. As Thiel recounts, all the lawyers competed for the same shared goals. They ranked themselves not by absolute progress towards a transcendent end goal, but by progress within their peer group. 

As Peter Thiel recounted:

“When I left after seven months and three days, one of the lawyers down the hall from me said, ‘You know, I had no idea it was possible to escape from Alcatraz.’ Of course that was not literally true, since all you had to do was go out the front door and not come back. But psychologically this was not what people were capable of. Because their identity was defined by competing so intensely with other people, they could not imagine leaving… On the outside, everybody wanted to get in. On the inside, everybody wanted to get out.”

Competition distracts us from things that are more important, meaningful, or valuable. We buy things we don’t need with money we don’t have to impress people we don’t like. Trapped in a never-ending rat race, lawyers climbed the corporate ladder by winning favor with partners at the top. Others engaged in small acts of sabotage against their coworkers. 

Law school was worse. Like lobsters in a bucket, wannabe lawyers battled for law school placement and law firm employment. Each goal led to the next. Rather than focusing their attention on the end goal of developing a legal expertise, transforming the Constitution, or rescuing the powerless from tyrannical injustice, they elbowed their peers so they could score higher than their classmates on standardized tests. The competition was zero-sum. The better one student did, the worse their peers scored.

HOW GIRARD INFLUENCED THIEL IN BUSINESS
Thiel sees the world at a strange angle. His contrarian streak runs through everything he does. But until now, nobody has explained the roots of his singular philosophy. 

His verbal tendencies double as a mirror into his mind. Listen to a Thiel interview and you’ll notice how often he reframes the question before answering. When he speaks, he skips between perspectives faster than a game of hopscotch. He says things like “One version of this is…” or “You could say that…” He has an uncanny ability to consider cultural trends and investment trades from a diversity of perspectives. Sometimes, I wonder if he sees life as a game of chess, where he plays against himself and simultaneously switches from black, to white, and back again. Listen carefully and you’ll see how often he hides answers inside of questions. By playing both sides of the board with the rigor of a Dostoyevsky novel, he sees what others miss with crystal clarity. 

In the words of one of his friends: 

“Peter is of two minds on everything. If you were able to open his skull, you would see a number of Mexican standoffs between powerful antagonistic ideas you wouldn’t think could be safely housed in the same brain.”

Before playing a game, you have to know the rules. Breakthrough businesses are so innovative that people don’t have the words to describe them. He focuses on questions as much as answers, so he can identify the difference that makes the difference. For example, people still talk about Google as a search engine and Facebook as a social networking site. Both descriptions miss the point. Google succeeded because it’s a machine-powered search engine. Until Facebook, social networks mostly helped people become virtual cats and dogs. Facebook succeeded because it helped people create real identities online. 15 years after its founding, people incorrectly frame the history of social networks. He doesn’t just focus on the brushstrokes. He looks at how the painting is framed. 

Thiel’s companies are governed by Girard’s wisdom. Girard observed that all desires come from other people. When two people want the same scarce object, they fight. In response, as CEO of PayPal, Thiel set up the company structure to eliminate competition between employees. PayPal overhauled the organization chart every three months. By repositioning people, the company avoided most conflicts before they even started. Employees were evaluated on one single criterion, and no two employees had the same one. They were responsible for one job, one metric, and one part of the business. 

Thiel provided the first outside money into Facebook and still serves on the company board. His $500,000 investment was partially informed by Mimetic Theory because he saw Girard’s ideas validated by social media. As Thiel said: “Facebook first spread by word of mouth, and it’s about word of mouth, so it’s doubly Mimetic. Social media proved to be more important than it looked, because it’s about our natures.” 

To be sure, not all of Thiel’s investments have been successful. Thiel’s hedge fund, Clarium Capital, was unsuccessful. The fund fell 13 percent in August 2008, 18 percent in October 2008, and lost money for the third year in a row in 2009. By September 2009, the total assets under management had fallen from a peak of $7.8 billion to a mere $850 million, most of which was Thiel’s personal capital.

People who work with Thiel are told to look for heterodox ideas and people with clear visions of the future. Thiel doesn’t like to be an operator because it’s a low-leverage activity. Instead of banging the keyboard himself, Thiel installs strong CEOs and leaders whose judgements are similar to his own. Time and again, these skilled operators have the agency to act without Thiel’s approval, and are encouraged to pursue bold visions of the future. They have freedom to pursue bizarre ideas and people who don’t fit the standard mold. 

In an epic exchange between two billionaires, Jeff Bezos said: 

“Peter Thiel is a contrarian, first and foremost. You just have to remember that contrarians are usually wrong.”

In an email to Ryan Holiday, Peter responded as such: 

“Contrarians may be mostly wrong, but when they get it right, they get it really right.”

Across PayPal and Facebook, Peter Thiel’s philosophy can be summarized in a single sentence: Don’t copy your neighbors. It’s like a search for keys. Instead of looking in the light, Thiel and his employees look in the dark, where nobody else is looking. 

SECTION 1: DON’T COPY YOUR NEIGHBORS
“Do not love the world or the things in the world. If anyone loves the world, the love of the Father is not in him. For all that is in the world—the lust of the flesh, the lust of the eyes, and the pride of life—is not of the Father but is of the world. And the world is passing away, and the lust of it; but he who does the will of God abides forever.” — 1 John 2: 15–17

Everybody imitates. We cannot resist Mimetic contagion, and that will never change. But there are bad ways to copy and good ways to copy. Bad imitators follow the crowd and mirror false idols, while good imitators copy a transcendent goal or figure. 

Imitation draws people together. Then, it pulls them apart like an ocean riptide. 

At first, two people who share the same desire will be united by it. But if they cannot share what they both desire, their relationship will transform. They’ll turn from the best of friends to the worst of enemies. Conventional wisdom says that we loathe people who are nothing like us. But when it comes to envy, jealousy, and resentment Girard takes a different perspective. Since small disagreements loom large in the imagination, Girard wrote that social differences and rigid hierarchies maintain peace. When those differences collapse, the infectious spread of violence accelerates. The fiercest rivalries emerge not between people who are different, but people who are the same. The more two people share the same desires, the greater the risk of Mimetic competition. 

Consider the famous opening words of Shakespeare’s Romeo and Juliet: “Two houses, both alike in dignity…” Through bloody battles between the Montagues and the Capulets, Shakespeare reminds us that people fight not because they’re so different, but because they’re so alike. Similar people are most prone to Mimetic envy because we tend to compete for status with the people who are closest to us. When two people are different and far away from each other, the tension will stay calm. Thus, the more we resemble our peers, the more Mimetic conflict will arise. 

Shakespeare wasn’t the only writer to identify the vicious Mimetic impulse. Sigmund Freud called the tendency for conflict between two similar people “The Narcissism of Small Differences.” We reserve tooth-grinding envy for people most like ourselves. Thomas Hobbes wrote that “if any two men desire the same thing, which nevertheless they cannot both enjoy, they become enemies; and in the way to their End... endeavor to destroy, or subdue one another.“

True to the observations of Shakespeare, Freud, and Hobbes, academics are famous for institutional elbow-knocking. 

Prestige-oriented environments can create nasty feuds over little prizes. A family friend named Julia tells a head-spinning story about her time at Columbia University. She couldn’t leave her books in the library. When she did, competing students often stole them. Not because they needed money or material goods, but because they felt surges of envy. Rather than absorbing the course material and preparing themselves for a life after college, students sabotaged their peers and shared false study guides. Relationships were shattered by sour resentment. Classmates could not be trusted, especially those who wanted to help. 

As Julia’s story demonstrates, academic rivalries are vicious because they focus on hierarchies over knowledge. They bicker over trivial details and compete for a limited set of status-based titles. In each department, there can only be one chairman. In each university, one president. Speaking about the faculty relationships at Harvard, Henry Kissinger once said: “The battles were so ferocious because the stakes were so small.” By obsessing over their competitors, the faculty lost sight over the big picture and fought over the small scraps of superficial status games. The more they strived to be different, the more their actions mirrored each other. 

Choose your enemies well. Like two children who fight for a toy, the more you fight somebody, the more you resemble your enemy. 

26B2A8CC-076C-41F2-822D-569AFBF71C3A.jpg
TOYS: LESSONS FROM RENE GIRARD    
I’ll be honest. When I first read about Mimetic Theory, I was skeptical. Girard’s ideas seemed trivial and I couldn’t find any evidence to support them. Then, I started seeing his ideas everywhere. Once I saw empirical evidence of Girard’s ideas, I started taking them seriously.  

Mimetic Theory shines brightest in trivial everyday moments, such as watching children play with toys. First, you have to understand Mimetic Theory at an intellectual level. Then, you have to understand it at an emotional one. Until then, Girard’s ideas might feel like ancient and irrelevant ideas. Once you watch these ideas impact your family, your friends, and your coworkers, you will have the same revelation Peter Thiel had as a student in Girard’s class at Stanford. 

Girard observed that even when you put a group of kids together in a room full of toys, they’ll inevitably desire the same toy instead of finding their own toy to play with. A rivalry will emerge. Human see, human want. 

Our capacity for imitation leads to envy. Babies’ interest in a particular toy has less to do with the toy itself and more to do with the fact that the other babies desire the toy. As soon as one child desires the toy, so do the others. Eventually, even though there are many toys available to play with, all the children want the same toy.

TOYS: LESSONS FROM JOSEPH HENRICH
Harvard anthropologist Joseph Henrich found empirical evidence for Girard’s observations about children and toys. In his book, The Secret of Our Success, he shows that humans are cultural learners. Mimetic desire is innate, not learned. We copy other people spontaneously, automatically, and unconsciously. And we are especially likely to copy people who are more successful than us, especially in moments of difficulty or uncertainty. 

Henrich illustrates our Mimetic nature by studying children and how they desire toys. Even at a young age, and especially in moments of confusion, they emulate people around them. In one study, Henrich found that babies engaged in social referencing four times more often when an ambiguous toy was placed in front of them. When faced with an ambiguous toy, babies altered their behavior based on adults’ emotional reactions. In their early years, babies depend on elders to navigate the world and outsource their decisions to them. 

I can relate. Nothing piques a child’s desire like watching their friends receive a new toy. Throughout my childhood, I remember coming home to my parents to ask for new toys. Back when I needed a car seat to ride in a vehicle, I asked for Thomas the Tank Engine train sets. Once I could read and write, I asked for the same LeBron James jersey my friends had. And in my first month of college in North Carolina, I demanded the same “Nantucket Red” Vineyard Vines pants as my fraternity brothers. 

None of these desires were my own. Looking back, these desires came from my peers. I wasn’t the only one. My friends’ desires moved in perfect synchronicity. Once one kid received a cool new toy, so did the rest of the group. When my parents wouldn’t buy me a toy, I shot back with Mimetic-fueled social proof: “But my friend Jeremy just got a new baseball glove and now I need one.” 

Turns out, I’m not crazy. 

Through toys, Girard and Henrich show how our tendency to desire the same scarce resources as our peers leads to envy and competition. 

Mimetic competition is visible in every aspect of social life. People shift their attention from the object of desire to the other person, and the drive to beat them. From bored students, to ambitious graduate school students, to empire-building business professionals, the objects we fight about change, but human nature doesn’t. 

COMPETITIVE STRATEGY IN BUSINESS
Thiel’s Christianity-inspired worldview lines up with Michael Porter’s philosophy of business strategy. Porter is a Harvard Business School professor known for his theories on economics and business strategy. He believed that strong businesses aim to be unique, not the best. Trying to outcompete rivals leads to mediocre performance, so companies should avoid competition and seek to create value instead of beating rivals. 

As Thiel once wrote: 

“Once you have many people doing something, you have lots of competition and little differentiation. You, generally, never want to be part of a popular trend… So I think trends are often things to avoid. What I prefer over trends is a sense of mission. That you are working on a unique problem that people are not solving elsewhere.”

After the 2008 financial crisis, when the new General Motors went public in 2010, CEO Dan Akerson announced that his company was free of legacy costs and ready to compete again. As he shouted to reporters: “May the best car win!” This phrase reflects an assumption that competition is the best way to grow shareholder value. It implies that if you want to win, you should try to be the best. But this is the wrong way to think about competition. 

We analogize business to war. In war, victory requires that the enemy is crippled or destroyed. Rivals who pursue the “one best way” to compete will converge on a collision course, where everybody listens to the same advice and pursues the same strategies, leading to zero-sum outcomes where total industry profits fall towards nothing. 

When you compete to be the best, you imitate. When you compete to be unique, you innovate. In business, multiple winners can thrive and coexist. You don’t have to annihilate your competition. While imitation creates a race to the bottom, innovation promotes healthy competition and economic growth. In that way, business is like the performing arts, not war. In the performing arts there are many entertaining singers and actors, each with a distinct style. The more talented and differentiated performers there are, the more the arts flourish. This is the essence of positive-sum competition. 

To drive the point home, let’s turn back to Peter Thiel. The third chapter of his book, Zero to One is called “All Happy Companies Are Different.” 

Thiel’s book applies Girard’s ideas to business. Like Girard himself, he says companies should avoid competition and walk the path of differentiation. He explains that many businesses create a lot of value, but don’t capture a lot of the value they create. As a result, even very big businesses can be unprofitable. 

According to Thiel, monopoly is the end state of every successful business. If you want to create and capture lasting economic value, don’t compete. The more unique companies are, the more the business world can flourish. Consider Thiel’s favorite example: the airline industry. 

As I type these words, I’m sitting in the United Airlines lounge at Denver International Airport. I’m writing during a five-hour layover on my way from New York to Los Angeles. In front of me, I see a lemon yellow Spirit Airlines jet preparing for takeoff. To advertise its affordable prices, the engine on the right wing says “Home of the Bare Fare.” Like the Southwest Airlines Boeing 737 to its left, the rise of low-cost airline carriers reflects the price sensitivity of flyers. I’m part of the bargain-hungry tribe too. This morning, I woke up at 3:50am so I could take a dirt-cheap 6:10am flight from La Guardia. As part of the journey, I also swallowed a five-hour layover in Denver so I could pay with frequent flyer points. My body screams for sleep, my mind shouts for productivity, and thankfully, due to the triple-shot cappuccino on the table in front of me, I’ll meet my writing quota today. 

Let’s wrap my morning in economic language. Air travel is an “elastic good.” Small changes in price lead to big changes in demand for a flight. Behavior differs between leisure travelers and business travelers. Leisure travelers are particularly sensitive to price fluctuations, so they fly much less when prices are high than when they are low. In contrast, business travelers don’t have as much flexibility. Since there’s money at stake, their decision to travel isn’t as influenced by shifts in price. 

public.jpeg
The airline industry suffers from near-perfect competition. Each year, U.S airlines serve millions of passengers and create hundreds of billions of dollars in consumer value. But in 2012, when the average airfare each way was $178, the airlines made only 37 cents per passenger trip. Whenever one airline makes a move such as lowering prices or adding an extra inch of leg room, its rivals match it. Since all the airlines chase the same price sensitive customers, they compete for every sale. That’s why, compared to the major tech companies, the major airlines in America are starving for profit. 

As a contrast to the hyper-competitive airline business, consider Google. Here’s Peter Thiel: 

“Compare [the airlines] to Google, which creates less value but captures far more. Google brought in $50 billion in 2012 (versus $160 billion for the airlines), but it kept 21% of those revenues as profits—more than 100 times the airline industry’s profit margin that year. 

Google makes so much money that it’s now worth three times more than every U.S. airline combined. The airlines compete with each other, but Google stands alone.”

Perfect competition is the default state in Economics 101. In a perfectly competitive market, undifferentiated companies sell homogenous and substitutable products. Firms don’t have market power, so their prices are determined by the iron laws of supply and demand. 

High profits attract competition. According to economic theory, if outside entrepreneurs hear about profits, they’ll start a new firm and enter the industry. Increased supply will drive prices down, which will decrease total industry profits. If too many firms enter the market, the entire industry will suffer losses. If companies start to lose money, they’ll go out of business until industry prices rise back to sustainable levels. Most importantly, in a world of perfect competition, no company will make an economic profit in the long run. Just like the airline industry.

Thiel offers an alternative to perfect competition: monopoly. Without competition, they can produce at the quantity and price combination that maximizes their profits. Successful strategies attract imitators, so the best businesses are difficult to copy. Firms in a competitive industry who sell a commodity product cannot turn a profit.  But companies who have a monopoly can set their own prices since they offer an in-demand product that cannot be replicated. Monopoly firms are big fish in a small pond. 

Don’t copy your neighbors.

SECTION 2: TIME MOVES FORWARD
“The twentieth century was great and terrible, and the twenty-first century promises to be far greater and more terrible.” — Peter Thiel

In this section of the essay, we will depart from a focus on Thiel. Instead, we’ll explore Christianity and the history of time. By doing so, we will have the necessary context to frame Thiel’s worldview in the next section. 

The Christian story begins with: “In the beginning, God created the heavens and the earth.” At its root, the story is about how the world went bad and how we can fix it. The world is broken because humans are broken. Human sin is responsible for the world’s evil, and our relationship with God is broken because it was ruined by human rebellion. God is the central character in the story. That’s why instead of worshiping things, Christians are instructed to worship their creator. God’s purposes are central, not theirs. Humans need to be ruled, and man must glorify its king. Only under God’s rule can man discover his deepest satisfaction and forever enjoy the Kingdom of Heaven. 

The Resurrection is a symbol that someday, all wrongs will be made right. Christians do not take it as a symbol, but as a concrete fact. Christians say that if you believe in Jesus — that he was raised from the dead and is the Son of God — he will restore your life until every pain and heartache becomes untrue. 

Linear conceptions of time, and especially the idea of progress, emerged with Christianity. In a cyclical conception of time, the circle of time closes where it opened. There is no beginning or end. For example, the Hindu Vedas teach that the world spins along an endless cycle: creation, rise, decline, destruction, and rebirth. Even if the cycle repeats for millions of years, it will continue to spin forever. 

IMG_0287.jpg
With a linear perspective, time moves from the past to the future. It begins with the Garden of Eden at the beginning of The Bible and ends with the Kingdom of Heaven. 

With Jesus as its savior, Christianity is the only religion that sees a human as the Son of God. When Jesus died on the cross, he paid for the sins of humanity so he could end evil and suffering. Jesus speaks of his return to earth in Matthew 19:28. He says: “I tell you the truth, at the renewal of all things, the Son of Man will sit on his glorious throne.” Instead of relying on a cyclical re-birth, Jesus’ return will fix the material world by destroying all decay and brokenness. 

FROM CYCLICAL TO LINEAR TIME
Religious or not, it’s worth studying Jesus Christ. He’s had more influence than anybody in human history. For example, Western Civilization divides time into two periods: before and after Jesus Christ. He’s a universal icon. 

In a letter called One Solitary Life, James Allen Francis wrote: 

“Twenty centuries have come and gone, and today he is the central figure of the human race. I am well within the mark when I say that all the armies that ever marched, all the navies that ever sailed, all the parliaments that ever sat, all the kings that ever reigned—put together—have not affected the life of man on this earth as much as that one, solitary life.”

Earlier this year, I attended a series of Questioning Christianity lectures in New York City. Every Thursday, Tim Keller spoke about the core tenets of Christianity: faith, meaning, satisfaction, identity, morality, justice, and hope. In one of his talks, he spoke about the human transition from hope to optimism. From praying for a better world to working hard to ensure a better future. In the sermon, Keller argued that humans are future-oriented beings. If we don’t have a positive vision for our future, we become slaves to the desires of the present day and crumble under the suffering of daily life. That’s why we need to believe that our lives are marching towards an end that’s worth striving for. Otherwise, we will become adrift like a log in the ocean. 

In his final lecture, Keller quoted Robert Nisbet, the author of The History of the Idea of Progress. In it, Nisbet argues that ancient people saw time as cyclical, and no idea has been more important to Western Civilization than the idea of progress. 

The Ancients assumed that humanity was doomed to cycles of pessimism. Even if they held ideas of moral, spiritual, and material improvement, the idea that humanity can improve itself, step-by-step and stage-by-stage into an earthly paradise is uniquely Western. Christian theology sees time as linear. It moves away from the Garden of Eden, and toward a day of judgement, justice, and the establishment of a divine, peace-filled kingdom. 

The linear perspective on time was born out of Greek philosophy. Controversial at the time, writers like Seneca wrote that mankind had advanced in the past, and will continue to advance in the future. But the idea of progress did not crystallize until St. Augustine. His book, The City of God, was the first full-blown philosophy of world history. By fusing the Greek idea of growth with the Jewish idea of sacred history, St. Augustine introduced a Christianity-inspired linear theory of humanity. He believed in the unity of mankind, a succession of fixed stages of human development, the assumption that all that has happened and will happen is necessary, and the vision of a future condition of heaven on earth. 

Through a belief in Redemption, Christians turned their minds to the supernatural and adopted a belief in an eternal heaven. Nisbet writes: 

“Of all the contributions to the idea of progress by Christian thought, none is greater than this Augustinian suggestion of a final period on earth, utopian in character, and historically inevitable.”

Christian ideals of progress are sprinkled throughout The City of God. At the end of his book, St. Augustine refers to the seven stages of early history. The last, still-yet-to-come stage will consist of peace and happiness on earth. He wrote that as a result of the inevitable historical development from the primitive world of the Garden of Eden, those who put their faith in Christ will experience an earthly paradise. ¹ 

Beginning with the Greeks and accelerated by the Christian writers such as St. Augustine, Western philosophy is defined by the march towards heavenly perfection. People in the West see progress, evolution, and innovation as synonyms. We assume that increased freedom and knowledge is limited only by the passage of time and an active commitment to creating a better future. Like a law of nature, progress was as inevitable as cherry blossoms in the spring.

If time is cyclical, the future will look like the present. The arrow of time points back towards its origin and ends where it began. Taken to the extreme, cyclical perspectives on time implicitly remove human agency. No matter what you do, the world will return to its original state. 

IMG_AEC1FBA9C6F6-1.jpeg
GIRARDIAN SACRIFICE: HOW VIOLENCE STOPS VIOLENCE
Once Tim Keller’s lectures were over and I understood Nisbet’s philosophy of progress, I turned to a series of Rene Girard interviews. As I started reading, I was shocked to see Nisbet’s idea of progress fit Girard’s theory of Mimetics like a pair of puzzle pieces. 

The similarities are stunning. Girard saw sacrifice and the scapegoat mechanism as the reason for Christianity and the center of human culture. The Christian story is the ultimate Girardian ritual because Jesus is a classic scapegoat, but with an all-important twist. Where previous myths were told from the perspective of the community, the Christian story is told from the perspective of the victim. And according to Girard, this is the essence of biblical revelation. The Gospels classify Jesus as a scapegoat. True to the scapegoat phenomenon, Jesus is not killed by the Romans, the Jewish priests, or by the crowd alone, but by everybody. The death of Jesus, like a scapegoat ritual, is a collective and community murder. 

Like all scapegoat victims, Jesus is killed despite his innocence. Christianity reveals the radical injustice of the scapegoat phenomenon. All scapegoats are both insiders and outsiders. At once, they must be insider enough to be part of the community, but outsider enough to blame for the community’s problems. As the Gospel of John says: “It is better for one man to die for the people, than for the whole nation to be destroyed... They hated me for no reason.”

Sacrifice is a social event. Without sacrifice, human beings wouldn’t have a culture. All human societies are built around religion because it’s the only way to peacefully work with the scapegoat mechanism. When humans engage in a Mimetic crisis, the violence can only be fixed by murdering the scapegoat. This process of killing the victim again and again is the main peace pill in an archaic society. People perform ritual sacrifices together, and when a priest is appointed to kill a victim, he kills the victim in the name of the whole community. After all, a community can’t scapegoat somebody unless it thinks the scapegoat is guilty. That’s why scapegoating has to be unconscious. Once the group ritual is performed, violence is repelled and peace is restored for the community. 

Ritual protects communities from the great violence of Mimetic disorder thanks to the real and symbolic violence of sacrifice. Girard said “sacrificial systems contain violence.” His message has two meanings. Violence is the disease and the cure for the disease. Sacrificial ritual is always violent. And yet, since the real and symbolic violence of sacrifice restores peace in the community, it prevents the escalation of runaway Mimetic violence. In that way, humanity contains violence with violence because sacrifice saves the community from its own violence. 

IMG_140381BF3BD0-1.jpeg
HOW TIME RELATES TO GIRARDIAN SACRIFICE
It’s hard to gauge the impact of various philosophies of time. Even as I argue for it, I’m skeptical that a linear perspective on time is a meaningful driver of innovation and technological progress. And yet, my skepticism is balanced by my own relationship with my future self. 

Creating explicit images of my future has made me healthier, happier, and much more productive. I re-write my 25-year vision multiple times per year. Then, twice a month, I meet with a personal coach to make sure my short-term actions sync up with my long-term goals. By treating my future self with the same respect as my current self, I’m better able to ignore the nagging impulses of the moment and work towards a better future for myself and humanity. 

Fueled by a healthy skepticism, I’d love to see two studies. The first one would track the relationship between technological progress and conceptions of time. Scientists would ask proxy questions for determining a culture’s time horizon, and use it to evaluate its impact on productivity growth. The second study would measure the relationship between urban life and farm life. In my recent podcast conversation with Jason Zweig, he shared his experience growing up on a farm in upstate New York. Farm life encourages cyclical thinking in a way city life doesn’t. On a farm, you’re mesmerized by simple pleasures: the movement of the sun, the turn of the seasons, and the emotions of the turbulent skies. Aside from violent rainstorms and purple-painted sunsets, synthetic city environments take us away from nature. I suspect that people in cities are more likely to see time as linear, while people who grow up in nature see its cyclical traits, such as the rise of the sun, the seasonal thunderstorms, and the changing of the seasons. 

Likewise, ancient cultures saw time like an endless wheel. They believed that every so often, the universe would wind down and burn up, and after this re-birth, history would begin again. And everything, from our bodies to our souls, would be purified. Relative to the Christian tradition, this philosophy assumes the futility of long-term progress. 

Girard offers a historical perspective for the transition from cyclical time to linear time. He identified a cyclical loop: First, when a scapegoat is sacrificed, peace is restored in the community. Then, the culture lives peacefully for a short time. But eventually, tensions flare and violence returns to the community. To restore the peace, a new scapegoat must be named and sacrificed, which re-starts the sacrificial loop. 

IMG_008CF1AC84F7-1.jpeg
HOW LINEAR TIME DRIVES PROGRESS AND LONG-TERM THINKING
To Peter Thiel, short-term thinking is the essence of sin. Like The Bible, he advises us to make plans and sacrifice the present for the future. Greatness is like chess. To win, you must study the end game and work towards the one you want to see. Thiel’s favorite chess player was José Raúl Capablanca who said: “To begin you must study the end. You don’t want to be the first to act, you want to be the last man standing.” 

Thiel says a bad plan is better than no plan at all. Having no plan is chaotic. He supports people who trade the shiny mirage of short-termism for the calm, controlled grace of a long time horizon. Like Capablanca, they are the kinds of people who study the end-game and work backwards from there. 

In a thought-provoking essay called Peter Thiel and the Cathedral, Pascal-Emmanuel Gobry argues that Cathedrals were the equivalent of the Apollo project in the High Middle Ages. Like America’s Apollo program, each Cathedral required a specific and ambitious plan for building it. Medieval cathedrals were the first man-made structures to soar higher than the Egyptian Pyramids, which were monuments to death. But cathedrals are dedicated to the triumph over death. Moreover, cathedrals can only be built with scientific knowledge and communal support. They require scientists, mathematicians, engineers, craftsmen, and artists. And all of them need a long time horizon.  

Long time horizons aren’t just psychological. They’re cultural. Modern society suffers from temporal exhaustion. Or as, sociologist Elise Boulding once said: “If one is mentally out of breath all the time from dealing with the present, there is no energy left for imagining the future.” 

As I’ve written before, the speed of technology and the hyperconnectivity of society have placed us in a “never-ending now.” Like hamsters running on a wheel, we live in an endless cycle of ephemeral content consumption — a merry-go-round that spins faster and faster but never goes anywhere. Even the virtues of information consumption have changed. Most people I know care more about being informed than being well read. By focusing on the desperate screams of moody news anchors and not the books you’ll find in libraries, they let the culture’s moods dictate their own. The news has swept us into a dizzying chaos. When we whirl in its vortex, we become overwhelmed by the slightest breeze of chaos and lose sight of our place in history. 

For the opposite perspective, consider the Japanese. Some of its citizens recently witnessed the 66th cycle of a ritual that began more than 13 centuries ago. In a city called Ise, people have been rebuilding the grand Jingu shrine with wood and thatch since the 7th century. This Shinto ritual does more than keep the structure intact. It helps the master temple builder train the next generation and injects participants with a long-time horizon. This Japanese commitment to maintenance allows it to sustain structures and rituals for millennia. We shouldn’t be surprised that Japan is home to most of the oldest companies in the world. 

With that said, I don’t endorse the Japanese perspective in all its forms. The country is not as innovative as it once was. When I speak with friends who do business there, they complain about the rigid hierarchies and the inability to take risks. Instead of copying the Japanese commitment to long-term thinking, we should learn from it and use Christian-theology to build upon it. 

Thiel concludes that time is linear, not cyclical. The future won’t look like the present. It will either be much worse or much better. Or more explicitly, “stagnation leads straight to apocalypse.” If we don’t, we’ll suffer from limitless Mimetic violence; and if things go well, we might find our place in God’s peaceful kingdom. 

Informed by its linear conception of time and the Christian image of heaven, Thiel applauds the grand visions of yesterday’s leaders. Modern presidents no longer inspire Americans with positive visions of the future. The visions of the past weren’t just ambitious. They were clear and specific. Unfortunately, there is no modern equivalent of the Manhattan Project, the Apollo Project, or Nixon’s 1974 plan to defeat cancer by the end of the decade. 

Christians were the first group to reject cyclical time. They shouted that the future could be meaningfully better than the past. By doing so, they initiated a positive feedback loop, where progress led to progress, which led to more progress. 

Guided by this belief in the possibility of progress, Christians follow a high-resolution painting of a perfect future. It’s as if humanity is on a mission. They believe humans are here to reflect God’s light onto the world. Instead of returning to the Garden of Eden, humanity will march forward, from the past to the future, and create “a new heaven and a new earth.”

SECTION 3: THE FUTURE WILL BE DIFFERENT FROM THE PRESENT
“And I saw a new heaven and a new earth: for the first heaven and the first earth were passed away; and there was no more sea.” -- Revelation 21:1

"The cliche goes like this; live each day as if it were your last. The best way to take this advice is to do exactly the opposite: live each day as if you would live forever.” — Peter Thiel

A NEW HEAVEN AND A NEW EARTH
The Book of Revelation is the last chapter in the New Testament. In this section, I interpret it in a way that supports the rest of Thiel’s conclusions. Inevitably, I have misspoken here. If I met Thiel, this is the section I would focus on. It’s foundational to Thiel’s worldview and I’ve never heard him speak about this section of The Bible in public. 

Here’s what I do know: Thiel is trying to save the world from apocalypse. 

The Book of Revelation paints two outcomes for the future of humanity: catastrophic apocalypse or a new heaven and a new earth. Some of the Christians I know believe that humans aren’t literally taken out of this world and transported into heaven. Instead, as explained in Revelations 21, heaven comes down to earth. According to this vision, humanity will be cleansed, renewed and perfected. The horrors of the world will be undone. People will receive the lives they’ve always wanted. All evils will be repaired, and the pain of existence will vanish like evaporating water after a thunderstorm. Better yet, the joy and glory of a world after redemption will be greater because humans have suffered to reach it.

I suspect Thiel holds this philosophy. To Thiel, The Book of Revelation is more than a metaphor. It’s a playbook for guiding humanity from the garden of the past to the city of the future.

As Thiel once wrote:

“For Girard, this combination of mimesis and the unraveling of archaic culture implies that the modern world contains a powerfully apocalyptic dimension.”

The probability of a civilization-ending apocalypse is increasing. Just because we no longer believe that Zeus can strike humans with sky-lighting thunderbolts, doesn’t mean that existential risk isn’t possible. Like Girard, he worries that the world is becoming more Mimetic. Worse, globalization is raising the threat of runaway mimesis and an apocalyptic world with cold corpses, dead horses, and splintered guns. 

In an essay called The Optimistic Thought Experiment, Thiel advises us to build the modern equivalent of Noah’s ark, so we can survive the floods of Girardian evil. Thiel fears that due to technologies like nuclear weapons, humans are already capable of destroying the world. With modern technology, a tiny number of people are capable of inflicting unprecedented levels of damage and death with the push of a single button. That though, doesn’t mean we should stop innovating. A lack of progress leads straight to a bleak, ravaged, and apocalyptic world. He writes: 

"The entire human order could unravel in a relentless escalation of violence — famine, disease, war, and death. The final book of the Bible, the Book of Revelation, even gives a name and a place: The Battle of Armageddon in the Middle East is the great conflagration that would end the world. Against this future, it is far better to save one’s immortal soul and accumulate treasures in heaven, in the eternal City of God, than it is to amass a fleeting fortune in the transient and passing City of Man.”

Here, Thiel encourages us to be specific about the long-term future we want to create. Here, he counters the secular and Eastern philosophy. Under the secular mindset, there is no transcendent future after death. This is it. You have one life. Similarly, according to Eastern religions, we lose our individuality and lose our material lives so we can become part of the whole again. But Christianity offers a different perspective: work for the fruits of eternity instead of chasing the fleeting pleasures of the day. Don’t place too much weight on the present moment. Instead of focusing on meaningless scandals, endless political dramas, or the limitless accumulation of wealth, we should focus on the impending catastrophe at the end of the road. Work to prevent runaway Girardian violence. That way, when the Day of Judgement comes, we’ll lean towards the side of the good. 

If there was ever a silver bullet, Thiel believes living with a long time horizon is it. 

Whether the future is better or worse will depend on our actions. Like Girard, Thiel, believes that Western political philosophy cannot cope with global violence. In 2004, three years after 9/11, Thiel sponsored a philosophical conference called “On Politics and Apocalypse.” Thiel contributed an essay called The Straussian Moment. In it, he tried to find common ground between Girard’s Mimetic theory and the work of two right-wing political philosophers: Leo Strauss and Carl Schmitt. He argued that the issue of violence and existential risk has not been taken seriously enough since the Enlightenment. 

Here are Thiel’s words: 

“The Christian statesman or stateswoman knows that the modern age will not be permanent, and ultimately will give way to something very different. One must never forget that one day all will be revealed, that all injustices will be exposed, and that those who perpetrated them will be held to account.

The postmodern world would differ from the modern world in a way that is much worse or much better — the limitless violence of runaway mimesis or the peace of the kingdom of God… One must never forget that one day all will be revealed, that all injustices will be exposed, and that those who perpetrated them will be held to account.”

As a libertarian who holds the New Testament as a seminal text, Thiel seeks to increase individual freedoms while preventing runaway Mimetic violence. As promised, here’s where Girard’s observations of the past can shape our understanding of the present. Everybody condemns hate-fueled online speech. If Girard’s theories are accurate, online fighting might be the preventative medicine we need, even if it tastes disgusting and comes with painful side-effects. The forces of globalization and technology may have abolished the boundaries of violence. 

If so, the cure is nested inside the disease. Online, social-media based arguments might repel an apocalyptic scenario. Perhaps Thiel sees Facebook as a place to contain unbounded Mimetic violence. It simultaneously perpetuates violence and prevents it from happening. After all, if people fight on social media, they won’t fight on the streets. Like a boiling kettle, we have to let out steam somewhere. Better to cool the pot on social media than in the streets. In the words of Thiel, “social media proved to be more important than it looked.”

FOUR WAYS OF THINKING ABOUT THE FUTURE
The pull towards Girardian conflict stems from pessimism and short-term thinking. In Zero to One, Peter Thiel describes four ways of thinking about the future: definite optimism, indefinite optimism, definite pessimism, and indefinite pessimism. In a definite world, the future is knowable. There is a predetermined plan for what the future will look like. An indefinite world is more of a random walk. Like a lottery, the future is out of our control. It’s governed solely by probabilities and chance events, which makes it impossible to act with any agency. 

Thiel defines the four quadrants as such:

Definite Optimism: The future will be better and we know how.

Indefinite Optimism: The future will be better and we don’t know how.

Definite Pessimism: The future will be worse and we know how.

Indefinite Pessimism: The future will be worse and we don’t know how. 

IMG_ADBE7063D097-1.jpeg
BACKGROUND TO DEFINITE OPTIMISM
Innovation begins with inspiration. Positive visions of the future inject people with imagination, which pulls the future forward. 

A quick browse through the history books shows that Americans, and especially the government, used to make big plans and live with Definite Optimism. To illustrate the idea, let’s turn to my favorite example: The Reber Plan. 

REBER PLAN
The Reber Plan is my favorite example of Definite Optimism. In the 1940s a San Francisco-based teacher and amateur theater producer devised a plan to reconstruct the San Francisco Bay Area. People took the plan seriously. Newspaper boards across California endorsed it. 

Reber proposed two large earth and rock dams, one between San Francisco and Oakland, and another between Marin County and Richmond. Dams would drain water from north to south and convert the Bay from saltwater to freshwater. Congress explored the project. Engineers planned to construct a 32-lane highway and scatter high-rise buildings throughout the reconstructed city. To test the plan, the Army Corps of Engineers built a 1.5-acre scale model of the proposed design. 

Ultimately, the Reber Plan didn’t work. The freshwater lakes would have evaporated too quickly. Nevertheless, due to the spirit of the post World War II age, people gave the Reber Plan the respect it deserved. 

IMG_4393427F321B-1.jpeg
FORD MOTORS AIRPLANES DURING WORLD WAR II
As Americans geared up for World War II in the early 1940s, President Franklin D. Roosevelt (FDR) called upon the nation to increase its production of airplanes. But in a 1940 speech to Congress, FDR said: “I should like to see this Nation geared up to the ability to turn out at least 50,000 planes a year.” At the time, nobody thought FDR’s goal was possible. 

Americans were still plagued by the Great Depression. Roosevelt spoke to 132 million Americans. Only 48,000 of them earned more than $2,500 per year, the modern equivalent of $40,000 in today’s dollars. Nearly one-third had no running water. And none of them had antibiotics or unemployment insurance. 

At the time, Americans were producing fewer than 1,000 planes per year. The Nazis had 7 million soldiers, but America had less than 200,000. American industry responded with passionate intensity. Ford Motors had never built an airplane, but America sought to produce more airplanes at Willow Run than Hitler produced in all of Germany. To build the plant, builders moved 650,000 cubic yards of dirt and laid 58 miles of grain tile underground. Production exceeded expectations. Ford Liberator bombers took flight in the spring of 1942, ahead of schedule. Within five years, Ford produced tens of thousands of airplanes per year. War production board chief Donald Nelson captured the ambition of the moment: “When we are talking about America’s war production job we are discussing the biggest job in all of history.”

IMG_1BC8A6CEC9A5-1.jpeg
Today, these bold visions would be ignored and dismissed as lunacy. Definite Optimism is withering. Big dreams are now seen as childish illusions. We no longer trust amateurs with vast imaginations, and we no longer challenge people to imagine futures that look radically different from the present. Instead, we defer only to experts with mainstream opinions. 

The Reber model has been demoted from a grand vision of the future to a meager Sausalito tourist attraction. “Let’s dam the San Francisco Bay” is too grand and too specific. Instead, we say “Let’s improve the economy” or “promote information.” We doubt the potential of grand plans. Instead, we put our faith in small tweaks and A/B tests, implying that millions of small actions are a better way of improving the world and creating a desired future. 

We’ve moved from an atmosphere of utopian promises to one of dystopian threats. Definite Optimism has disappeared.

THE END OF THE FUTURE
Since the Financial Crisis, tens of thousands of Americans have moved into the Indefinite Optimism and Definite Pessimism quadrants. 

According to Thiel, this shift has been worse than acknowledged. A 2011 essay called The End of the Future, which lives on the homepage of the website of his venture capital firm, argues that progress has stagnated. We’ve shifted away from funding transformational companies and toward companies that solve incremental problems, and sometimes even fake ones. To be sure, he doesn’t only invest in companies with little competition like Palantir and DeepMind. His firm also invested in Airbnb, Stripe, and Postmates.

Today, we’ve narrowed the definition of technology to Angry Birds and goofy SnapChat filters. That’s why Thiel longs for the days when technology alluded to space, airplanes, and rockets that generated more energy than a small atomic bomb. 

NASA’s star spangled splendor transformed consciousness. Astronauts with stomachs of steel traveled the impossible distances of space. The Apollo 8 mission required superhuman precision, equivalent in scale to throwing a dart at a peach from a distance of 28 feet, and grazing the top of the fuzz without touching the fruit’s skin. To reach the moon, America’s pioneers traveled across 240,000 miles, about fifty-eight times the distance Columbus sailed when he discovered the Western world. As the Apollo rockets pierced through the stratosphere, and navigated the pin-drop silence of outer space, they inspired people back on earth to expand their horizons. 

Literally. 

America’s imagination peaked in 1969, when Neil Armstrong stepped foot on the moon. He stepped on moon-dust less than a decade after Alan Shepard became the first American in space, and only 8 years after President John F. Kennedy’s speech at Rice University where he said: “We choose to go to the moon, not because it’s easy, but because it’s hard.”  

As the American people watched their comrades explore the distant skies and travel to the moon, they thought they’d witnessed the opening of a new frontier. Humans were no longer trapped on the pale blue dot. Soon, all of humanity would traverse the stratosphere and soar through space. Science fiction writers such as Arthur C. Clarke predicted imminent commercial space travel, interstellar exploration, and genuine artificial intelligences. The Apollo Project didn’t just shake the Florida launchpads. It shook the entire world. 

To echo the point, Thiel likes to quote a 1967 best-selling book called The American Challenge. The book predicted that America would be a post-industrial society by the year 2000. Americans would work four days per week and seven hours per day. The year would be comprised of 39 work weeks and 13 weeks of vacation. 

Unfortunately, this dream never arrived. Transportation machines soared higher and faster for 200 years. In the span of a single lifetime, people went from traveling by horse and buggy to walking on the moon. Depending on who you ask, it seemed like humanity was guided by the invisible hand or an all-powerful God. Interstellar travel and vacations on the moon were the future, and everybody knew it. 

In an unexpected twist, the physics stagnated. Transportation stopped improving. And today, we’re no longer pushing the limits of height and speed. 

IMG_D47E8ED52D66-1.jpeg
Just ask Pan American World Airways, the iconic airline of the Post World War II era. After Americans stepped foot on the moon, the airline’s customer center was inundated with phone calls from around the country. First the astronauts. Then, the people. Customers wanted to reserve seats on the first trips to the moon. Between 1968 and 1971, Pan Am accepted 93,005 reservations for planned commercial flights to the moon. Fast forward five decades and only 12 men have ever walked on the moon. No American, let alone any ordinary human being, has stepped foot on the moon since 1972. 

The rate of technological progress is slowing. The only major exceptions are semiconductors, DNA sequencing, and communications technology. Side effects of slow growth plague the economy. Real median wages haven’t risen since 1973. Meanwhile, the costs of housing, healthcare, and education are rising faster than inflation. More than 40 million Americans are collectively liable for more than $1.5 trillion in student loans. 

In response, we’ve lowered our efficiency standards. The Golden Gate Bridge was built in less than four years in the 1930s. The recently completed Golden Gate Bridge access road, Doyle Drive, took seven years to build and cost more in real dollars than the original bridge. Buildings, too. The Empire State Building was built in 15 months from 1931-1932. 80 years later, The Freedom Tower took more than 12 years to build. We’ve masked our lack of progress with government money printing, rising debt levels, and distractions of digital technology. 

America is not as dynamic as it once was. We see it in the statistics and feel it in our politics. And yet, ask the average person, and they’ll tell you that we’re living in a world of exponential technological growth. 

Don’t believe Thiel? 

Follow the money. Warren Buffett, the richest investor in America bets against change. The less the world changes, the more Buffett succeeds. BNSF Railway, where Buffett recently invested $44 billion is the largest non-financial company in the Berkshire Hathaway portfolio. Thiel proclaims that 40 percent of railroads involve the transport of coal, so Buffett’s investment will do especially well if the travel and energy consumption patterns of the 21st century look like the past. 

After digging through the 2018 Berkshire Hathaway Annual Report, I’d like to add context to Thiel’s thesis. Buffett’s firm has poured millions of dollars into renewable energy. In addition to coal and natural gas, Berkshire Hathaway Energy (90% owned by Berkshire Hathaway) has made meaningful investments in solar, nuclear, hydro-electric, geo-thermal, and in particular, wind.

IMG_0256 2.jpg
From a distance, we see a mirage of progress. From up-close, once we remove the smartphone screens in front of us, we feel the reality of struggle and stagnation. According to a recent survey, 80% of Americans think the next generation will be worse off than the current generation. As Tim Keller wrote in Making Sense of God: 

“Younger Americans today are perhaps the first generation to be certain that they are and will be “worse off” than their parents. The interconnected nature of the world makes nightmare scenarios—pandemics, global economic collapse, climate-change disaster, cyberattacks, terrorism—all seem like genuine possibilities, even probabilities… Today hope has narrowed to the vanishing point of the self alone. In our current phase of American history we have lost belief in God and salvation, or in any shared sense of national greatness and destiny.”

This intuition is supported by data. Millennials are less well off than members of earlier generations were when they were young. They have lower earnings, fewer assets, and less wealth. Children born in 1940 had a 90% chance of earning more than their parents. But children born in the 1980s have only a 50% chance. Christoper Kurz, an economist at the Federal Reserve has shown that millennial households had an average net worth of about $92,000 in 2016, nearly 40% less than Gen X households in 2001, adjusted for inflation, and about 20% less than baby boomer households in 1989. Wages tell a similar story. In short, millennials have it tough and it isn’t their fault. With the rise of dystopian films, Hollywood creates and reflects these dark predictions about the future. 

Unable to pay for college or afford an apartment in a job-filled city, many Millennials have lost hope. 

One friend doesn’t want to have kids because “the entire state of California is going to be underwater by 2050.” Or, in the words of a comedian on Twitter: “The fun part about living right now is we get to see how it ends.”


MILLENNIALS: YOUNG AND YEARNING
When I speak with friends and travel the 50 states, I’m struck by how numb many people are to the world. Besides immigrants and their children, both of whom inspire me with their ambition and passionate work ethic, I see fear, complacency, and extreme risk-aversion everywhere. 

Benjamin Franklin once said: “If everyone is thinking alike, then no one is thinking.” 

The most talented people follow the same narrow tracks. People are afraid to dream big or stand out. Without a positive vision for their future, these young Americans are stuck playing vicious, zero-sum status games. Instead of constructing our own desires, they mirror the goals of people around them. Patrick Collison, the CEO of Stripe, shared a similar observation: 

“If you're in the US and go to a good school, there are a lot of forces that will push you towards following train tracks laid by others rather than charting a course yourself. Make sure that the things you're pursuing are weird things that you want to pursue, not whatever the standard path is. Heuristic: do your friends at school think your path is a bit strange? If not, maybe it's too normal.”

There’s a lack of differentiation. As Thiel observed: 

“There is something very odd about a society where the most talented people get all tracked toward the same elite colleges, where they end up studying the same small number of subjects and going into the same small number of careers… It’s very limiting for our society as well as for those students.”

The top colleges have become vocational schools for investment banking and management consulting. In 2007, for example, half of Harvard seniors took jobs in finance or consulting. This mirrors my own experience. My college jobs department steered us towards high-status jobs instead of high-impact ones. Students, professors, and advisors cared more about perception than reality. It felt as if the goal of life wasn’t to improve the world, but to win awards and build an impressive resume. Instead, my smartest friends were pushed towards a handful of fields: law, management consulting, and investment banking. Other options were peripheral and besides the point. 

Young Americans are trapped by student loans, crippled by path dependence, and constrained by runaway housing costs. They’re raised in institutional environments where conformity is praised and originality is punished. Like Pavlov’s rats, they’ve responded with authoritarian obedience. To no fault of their own, they’re sleepwalking through life as if their best years are already behind them. 

I recently had dinner with a fraternity brother in Manhattan. Let’s call him Jim. Right after the bacon cheeseburgers arrived and just as we splattered ketchup on our crispy French Fries, I asked him how he liked his job. First, he paused for time. Then, he wiggled his eyes left and right, and said “Good. I’m learning a lot.”

Immediately, I smirked and questioned his answer. It reeked like Orwellian doublespeak. In my experience, “learning a lot” is code for “boring, but I’m putting up with it.” 

Jim told me he liked his job because it taught him how to “collaborate” and “work with people.” His words sounded like they were parroted from the company’s Human Resources department. I poked and poked. And after 10 minutes, we reached the truth. 

He explained how the school system taught him to follow rules, mimic his peers, and listen to teachers. That’s how Jim was taught to succeed, so that’s his strategy for climbing the corporate ladder. It’s as if the age-based fraternity hierarchy never left his mind. Pledge first. Succeed later. All the while, he’s spent years marching along the institutional track, obeying orders and doing exactly what others told him to do, without questioning why he should listen to them in the first place.

Spoiler alert: Jim is wasting his time.

He knows how to get things done, but never asks if it’s worth doing in the first place. Instead of working on important problems, he’s building “options” for the future. Like so many other college graduates, he’s been pushed into a mundane and uncreative profession. His dream-filled heart is crushed by the cold logic of investment banking. His words echo those of another friend, who said: “I’m just trying to get through the next 25 years as fast as possible.” 

Sparkling dreams have become minor annoyances, like a buzzing fly in a lakeside cabin. Student loans keep him stuck on the institutional treadmill. He paid too steep a price for college, and now he’s unable to question the system and forced to accept the institutional doctrine as gospel. As I listened, I wondered what would happen if a high-voltage defibrillator shocked him and he woke up from his intellectual slumber. 

Until then, he’ll stagger along the soul-crushing stepping stones of life: work hard in middle school so you can do well in high school; work hard in high school so you can do well in college; work hard in college so you can get a respected job; and get a respected job so one day, towards the end of your career, you can finally do what you want to do. All the while you “build skills” and “accumulate options,” as if the next corner will provide the happiness you’ve been seeking all along. 

In an essay called The Trouble with Optionality, Harvard professor Mihir Desai worries that the language of finance has polluted life. He condemns the modern, finance-fueled affair with optionality. Rather than taking risks or working on important projects, students acquire options. In finance, when you hold an option and the world moves with you, you enjoy the benefits; when the world moves against you, your downside risk is protected and you don’t have to do anything. The more optionality, the better. Picking a path reduces optionality, so people stay in limbo and don’t make commitments. This language doesn’t only apply to career planning. Some students talk about marriage as the death of optionality. But life is not like options trading. 

Optionality is a means to an end, not the end itself. Our obsession with optionality can backfire. In theory, these safety nets give them freedom. Bolstered by the confidence of security, they can jump head-first into ambitious projects. In practice, they become habitual acquirers of safety nets and never work on anything of substance. The longer they spend acquiring options, the harder it is to stop.

Desai advises:

“The shortest distance between two points is reliably a straight line. If your dreams are apparent to you, pursue them. Creating optionality and buying lottery tickets are not weigh stations on the road to pursuing your dreamy outcomes. They are dangerous diversions that will change you.”

When we pursue optionality, we avoid bold decisions. Like anything meaningful, venturing into the unknown is an act of faith. It demands responsibility. You‘ll have to take a stand, trust your decision, and ignore the taunts of outside dissent. But a life without conviction is a life controlled by the futile winds of fashion. Or worse, the hollow echoes of the crowd.

By brainwashing us into thinking that prosperity is inevitable, privilege can have a numbing effect. Among my friends in the upper echelons of society — the ones with the means to pursue transcendent dreams — I wonder if they’re too comfortable. Nobody believes in destiny. Social events revolve around binge drinking and conversations so superficial a robot could automate them. They’re dozing off in an intellectual slumber. Rather than rising to the level of their dreams, they fall to the average of their environment. In my college classes, where the annual education costs $40,000 per year, the vast majority of students wasted the time away on Facebook. Office hours were an afterthought. “Try hards” were mocked and made-fun-of, and nobody had a vision for their future.

We lack courage, not genius. We’re swimming in money, but starving for ambition. Every venture capitalist I meet says there’s too much money and not enough good ideas. As Peter Thiel reminds us:

"Progress is neither automatic nor mechanistic; it is rare. Indeed, the unique history of the West proves the exception to the rule that most human beings through the millennia have existed in a naturally brutal, unchanging, and impoverished state. But there is no law that the exceptional rise of the West must continue."

We increasingly believe that progress is inevitable. Progress, though, is not guaranteed. We must work for it. Otherwise, our living standards will not improve, and may get worse. 

THE PROMISE OF CHRISTIANITY 
To offer solutions, Thiel turns to the Christian value of hope. He has a heterodox view of Christianity. In his reading of history, the non-violence of Jesus is the antidote to Mimetic conflict. 

When I speak with Christians, they always return to the importance of hope. They have a point. Our beliefs about the future impact our thoughts about the present. The more we can turn our attention away from the ephemeral present and towards the eternal future, the more we can pursue grand visions and persist through the challenges of the day. The present cannot be divorced from the future. They are codependent. 

One of my friends works for a California-based investment firm which manages $6 billion in investment assets. For the first three years, during the initial fundraising process, investors turned their cheeks. The firm struggled to raise capital. And yet, in the face of rejection, the fund’s Christian founder maintained faith in the face of struggle. As my friend observed: “She succeeded because her Christianity gave her hope.” 

Our spirits rise when hopes are high. That’s why the day before Christmas is as exhilarating as Christmas Day. Big, bright gifts sit under the tree. Smaller ones hang in firetruck-red socks over the living room fireplace. Children play. Parents cook. Grandparents tell stories. And the rush of anticipation releases everybody’s serotonin.

Likewise, everybody knows that a team with belief is hard to beat. But a team that doesn’t believe they can win is hopeless. The importance of belief and momentum is evident to any shouting fan in any arena across the country. And yet, few consider its importance at the societal level. 

Christianity promises a Living Hope that enables believers to endure unimaginable suffering. A hope so resilient that like a Captain America’s shield, it can survive any evil, any sickness, or any torture. No matter the obstacles, certainty about the future gives you the confidence to act in the present. 

Thiel’s idea of Definite Optimism is Christian theology cloaked in secular language. By raising our spirits, a positive vision for the future unites society and raises our spirits. And that’s what the Western world needs right now.

Technological growth is the best way to reduce suffering in the world. Technological progress has stagnated since the 1970s, which contributes to the vile political atmosphere and the pessimism of modern Westerners. Thiel says we should acknowledge our lack of progress, dream up a vision of Definite Optimism, and guided by Christian theology, work to make it a reality.

SECTION 4: PETER THIEL’S ADVICE
“Enter through the narrow gate. For wide is the gate and broad is the road that leads to destruction, and many enter through it. But small is the gate and narrow the road that leads to life, and only a few find it.” (Matthew 7:13)

Now that we’ve outlined the Christianity-inspired foundations of Peter Thiel’s worldview, we’ll close with Peter Thiel’s advice for how to live. I’ll conclude with three actionable, Thiel-inspired principles: (1) create a positive vision for the future, (2) be careful who you copy, and (3) follow the Ten Commandments. 

SEARCH FOR SECRETS
“It is the glory of God to conceal a matter; to search out a matter is the glory of kings.” — Proverbs 25:2

Thiel opposes the idea that luck is all-powerful. He encourages human agency and believes in the power of a single individual to bend the future to their will. Thiel believes we attribute too much to luck, which stops us from actually doing things. As he proclaimed, “you are not a lottery ticket… you can either dispassionately accept the universe for what it is, or put your dent in it, but not both.”

For example, if you treat startup investments like a series of lottery tickets, you won’t think hard about them, and as a result, you will fail. Thiel asks: “Is this a business that I have enough confidence in that I would consider joining it myself?” If yes, he’ll consider an investment. If the answer is no, he won’t. He doesn’t see the world as a mere distribution of luck-based outcomes. Instead, he praises conviction, bets on transcendent founders, and invests in the kind of companies he’d want to work for. 

God is an all-encompassing term for things we don’t understand. Under that definition, luck is the secular God. Naturally, Thiel speaks about luck in the context of startup investing. “It’s just a matter of luck” is a statement of the deep nature of the universe. Deferring to luck is counter-productive. Treating people and events like lottery tickets makes us doubt our agency. 

Look for secrets instead of luck. Thiel recommends one book: Things Hidden Since the Foundation of the World by Rene Girard. The title is as revealing as the contents of the book. It comes from Matthew 13:35, which reads: “I will proclaim what has been hidden [since] the foundation of the world.” 

In job interviews, Thiel famously asks: “What very important truth do very few people agree with you on?” With it, Thiel can identify heterodox thinkers who aren’t blinded by Mimetic dogmas or intellectual fashions. He insists that there are still secrets left to uncover. Some are small and incremental. But the most valuable secrets are big enough to shake the world. Like Easter eggs, these broad and unconventional truths are hidden in places where nobody looks. You can find them, but you have to dig in obscure places. Other secrets are hidden in plain sight. They’re so obvious that nobody thinks about them. And once you learn about them, you’ll pinch yourself for not seeing them before. 

Writing in Zero to One, Thiel says: 

“The big secret is that there are many secrets left to uncover. There are still many large white spaces on the map of human knowledge. You can go discover them. So do it. Get out there and fill in the blank spaces. Every single moment is a possibility to go to these new places and explore them.”

Thiel’s attraction to secrets comes from a conservative writer named Leo Strauss. His writing was obscure because he hid truths behind a curtain of mystery. That way, they would only be shared with a small, select group of people. Make no mistake. Even today, forbidden truths are exchanged in closed forums, private conferences, and corner offices on the 72nd floor. They’re shared in whispers, not shouts. 

Strauss did not believe in transparency. He believed that even in the most open-minded societies, many truths were too problematic to be shouted. His contemporary disciples, like Thiel, conceal their words. They hide controversial ideas in esoteric language, and Strauss described the benefits as such:

"It has all the advantages of private communication without having its greatest disadvantage—that it reaches only the writer’s acquaintances. It has all the advantages of public communication without having its greatest disadvantage—capital punishment for the author… Their literature is addressed, not to all readers, but to trustworthy and intelligent readers only.” 

Sometimes, Straussians hide truths in plain sight. When they do, they’re concealed in unpopular characters, such as devils, beggars, and buffoons. Pseudonymous Twitter accounts are the new Straussian philosophers, but with one important twist. Instead of sharing their names and hiding the truth, today’s Straussians hide their names, but share the truth.  

BE CAREFUL WHO YOU COPY
“Then I saw that all toil and all skill in work come from a man’s envy of his neighbor. This also is vanity and a striving after wind.” — Ecclesiastes 4:4

Even if imitation is inevitable, we can reduce the negative effects of it. We can avoid the kinds of competition that lead to violence. If Girard is right, we are not as individualistic as we think we are. If we must copy others, we should be careful who we copy. 

Thiel encourages people to ask themselves: “How do I become less competitive in order that I can become more successful?”

Ask a Christian and they’ll say that you should only imitate Jesus. That’s why, in Revelations, humanity receives a warning: “In the future, an Antichrist will come who brings a promise: we can all be Gods and models for one another, and we can all live in harmony together.” In a world where everybody is a model, anybody can become a scapegoat. This is a recipe for evil. Rather than turning to each other for answers, the Bible tells us to imitate Jesus, and nobody else. Or as Christ says: “Imitate me as I imitate the father.”

I’m not sure that works for me. I feel an intellectual pull towards Christianity, but not an emotional one. Many of my secular friends feel the same way. Telling them to only follow Jesus’ teachings wouldn’t be productive. To a Christian, Jesus’ words carry the weight of the world. To me, they’re like a brick: heavy enough to make me careful, but light enough to add other ones to my mental backpack.  

According to Girard, the more differentiated a society, the more stable it is. But on the internet, everybody feels like an undifferentiated peer. Social media decreases the distance between people and their role models, so the pull to idolize false gods is greater than ever. Pair that with the blank slate theory that anybody can do whatever they want, and you have a recipe for runaway Girardian conflict. YouTube celebrities and Instagram influencers sell the exact kinds of behaviors that the Bible warns us about. By manufacturing envy, they tell fans that if they look like them, dress like them, and act like them, they can become them. 

We all form our identity by looking towards others. Since everybody copies, we can improve society by encouraging people to copy the right people. As a kid, back when I was 100% sure I was going to be a professional baseball player, I looked up to J.T. Snow, the first basemen for the San Francisco Giants. I was obsessed. I scavenged the kids’ section for his jerseys and waited patiently for autographs at the annual Giants meet-and-greet. I copied his mannerisms, his jersey number, and his position on the baseball field. And in 4th grade, I brought a chocolate ice cream cake to school to celebrate his birthday. 

Here’s how Thiel would respond to my imitative instincts: Be careful who you copy. If you’re going to follow a role model, find one who you won’t compete with. Don’t look to your peers for answers. Find somebody in a different stage of life who you admire and respect. They should be somebody who defied the status quo and took an independent path. In life, you have two options: (1) you can dispassionately accept the universe for what it is, or (2) you can put your dent in it. But you can’t do both. 

Win the decade, not the day. For example, if you’re a writer, your goals should transcend the New York Times Bestseller List. Think bigger than that. If you’re going to model a famous writer, pick a dead one such as Tolstoy or Hemingway. They are real enough to model. Since they’re dead, you won’t compete with them directly. Better yet, you can copy more than their writing. If you want to stretch your imagination, you can live where they lived and read what they read. That way, you can ignore superficial status competitions and think beyond the day-to-day stress of writing a book.

I suspect this is why Thiel admires Elon Musk so much. Since the first day of SpaceX, Elon has been on a mission to go to Mars. Since the entire company was aligned around the mission, the employees were motivated and paddling the boat in the same inspiring direction.

Great people trade the temptations of today for the trophies of tomorrow. Think like you’re immortal. Place the eternal before the perishable. Treat people like you’ll know them for the next ten thousand years and work on the kinds of projects you’ll be proud to tell your grandchildren about. Live like you’ll be alive forever. When in doubt, follow the Ten Commandments.

FOLLOW THE TEN COMMANDMENTS
“Thou shalt not covet your neighbor’s goods.” — 10th Commandment

To return to our initial question about the significance of the Cain and Abel story, we return to Rene Girard. From history, Girard learned that human relations are built on the primacy of violence. That’s why the Cain and Abel story is the archetypal example of Mimetic conflict, and Thiel sees Christianity as the optimal solution to apocalyptic violence. 

As Girard once said: “There are fundamentally only two ways of looking at religion: as superfluous, added on—or as the origin of everything.” If there can be no in-between, I suspect that like Girard, Thiel sees religion as the origin of everything.

public.jpeg
Thiel closed his Dave Rubin interview with practical career advice, inspired by the Ten Commandments. 

The first commandment says that we should only look to God. There is only one God and you should worship him. Look up, not around. Follow The Bible, which says there is no salvation in anyone other than Jesus. You won’t figure out what to do by looking at your peers, so don’t copy the people around you. Instead, we’ll end up in copycat rivalries where we claw and fight with each other like crabs in a bucket. 

The last commandment says you shouldn’t covet your neighbor’s goods. Inspired by the 10th commandment, Thiel encourages listeners to avoid competition. True to Mimetic Theory, the last commandment focuses on the neighbor instead of the object of desire because all objects are desirable when they belong to your neighbor. Society will push you towards competition, but you shouldn’t compete with your peers or depend on them for guidance. Competition is for losers. Instead of looking to the people around you for answers, find models that you cannot compete with. If you’re Christian, follow Jesus, and if you’re not, follow an intellectual hero who is way ahead of you. Rather than using your peers as a reference point, find your own transcendent orientation. 

Let the flame of Definite Optimism burn away the Mimetic virus. Use the Internet to curate your environment, so you can be hyper-mimetic towards the rare few who are anti-mimetic. Copy the people who don’t copy people. Take risks. Build a differentiated skillset. Pursue timeless wisdom, not intellectual fashions. Be skeptical of convention, and don’t let it double as a shortcut to the truth. Work on problems that nobody else is working on, especially if you’re uniquely capable of solving them. And ultimately, ask the questions you’re not supposed to ask, so you can find the answers you’re not supposed to find. 

Guided by the Cain and Abel story, remember the danger of imitating the wrong person. At first, it can inspire cooperation. But over time, it leads to envy, violence, and the apocalypse. 

FOOTNOTES
¹ In addition to St. Augustine, writers such as Adam Smith, Thomas Jefferson, and Benjamin Franklin supported Christian ideals of progress. Adam Smith’s book, The Wealth of Nations is regarded as economics’ foundational text. Smith declares that there’s a natural order to the progress of nations. His “invisible hand” doesn’t just speak to the stability of the economic system, but also to the natural progress of wealth, labor, skill, rent, and profits. Western civilization is built on these ideals. Two of America’s founding fathers, Thomas Jefferson and Benjamin Franklin operated with a similar progress-inspired philosophy. 

Writing two years before his death in 1824, Thomas Jefferson marveled at all the progress he had witnessed in his life: “And where this progress. No one can say. Barbarism has, in the meantime, been receding before the steady step of amelioration, and will in time, I trust, disappear from the earth.”

Likewise, in a letter to a friend, Benjamin Franklin wrote: “It is impossible to imagine the height to which may be carried, in a thousand years, the power of Man over Matter.”

ACKNOWLEDGEMENTS
Thank you to Kevin Harrington for the conversations that led to this post. Your wisdom and feedback is invaluable to me, and I’m grateful for our friendship. This essay is for you. 

Thank you to the other people who contributed to this essay through feedback and conversation: Brent Beshore, Lyn Cook, Nick Maggiulli, Sid Jha, Bushra Farooqui, Jeremy Giffon, James Patterson, Manan Hora, Ben Colley, and Michael Naka. ''',

                '19': '''Matt Ridley: How Innovation Works, Part 1
Innovation is the child of freedom
29:49
Get podcast 
Naval interviews Matt Ridley, the author of The Red Queen and, recently, How Innovation Works.

Transcript
Naval: I don’t have heroes, but there are people who I look up to and have learned a lot from, and Matt Ridley, who is on the line, has got to be near the top of that list. Growing up, I was a voracious reader, especially of science. Matt had a bigger influence on pulling me into science, and a love of science, than almost any other author. His first book that I read was called Genome. I must have six or seven dog-eared copies of it lying around in various boxes. It helped me define what life is, how it works, why it’s important, and placed evolution as a binding principle in the center of my worldview. That’s a common theme that runs across Matt’s books. 

After that, I read his book The Red Queen, which laid out the age-old competition between bacteria, viruses and humans—a topic that’s extremely relevant today. I also read his book The Rational Optimist, which helped me realize that it was rational to be optimistic, because of the technological and scientific advancement that we’ve had as human species since we first came across the stone ax and basic tools.

His book The Origins of Virtue helped me take a game-theoretical framework towards virtues and ethics. His book The Evolution of Everything continued that theme towards everything evolving. I’m sad to say I’ve missed one or two of your books in there, Matt. The Agile Gene, I have to go back and read that one. And most recently, 

Matt wrote a great book called How Innovation Works, which will be out by the time this podcast is out there. I had the pleasure of reading an advance copy over the last week.

Welcome, Matt. I’m honored to have you here. Do you want to give us a little bit of your background and how you got into writing about science?

Matt’s Background
Matt: Naval, it’s great to meet you and interesting to hear that story of how you’ve read so many of my books and got the point of them. It’s wonderful. I’m someone who’s enjoyed writing all my life. I became a professional journalist after a brief career as a scientist. I only got as far as doing a PhD in biology and then decided that I wanted to be a writer instead. So I became a journalist. I was a science editor at The Economist for a number of years and also served as a political reporter and correspondent there as well.

I then became a freelance writer. That was when I wrote The Red Queen, which was a book close to the topic I’d been studying as a biologist, that is to say, the evolution of sex. From there on, I’ve been incredibly lucky because people have given me contracts to write books about things that interest me. At the moment it’s about every five years that I do a book. But I don’t do a book until I’m interested enough in a topic. It’s a very difficult decision, plunging into writing a book on one topic and thereby not doing all the other topics you want to write books about.

The New Book
Naval: I read this book in preparation for this conversation, so it’s suffered from becoming a chore. Because normally one reads purely for enjoyment at their leisure and this time it became more about hitting a deadline. That said, this has been your most impactful book for me since Genome. It was very revealing. There are two things about this book that put it in a different class than your previous books, for me.

One is that it corrected a long-standing misconception I had about how Silicon Valley works. I am steeped in Silicon Valley. I’ve been here since 1996, I’m an investor in hundreds of companies. I’ve started close to a dozen companies. I thought I knew this game as well as anybody, and your book corrected a serious error that I had in my mind of the framework of how Silicon Valley works. And we can get into that.

The second thing about this book is that it was actionable. The first half was this collection of incredible stories about inventors and innovators that would be fun, historical reading in its own right. But then the second half explains  how innovation works, what helps it works and what stops it from working, what creates the conditions for it to work and not work.

So I recommend this book for two classes of people. One is innovators and would-be innovators themselves. If you’re an entrepreneur in Silicon Valley, Shanghai or Bangalore and you’re thinking about creating products—whether it’s social media, launching rockets, building airplanes or genetic engineering—you need to read this book because it will give you a better view of the history of innovation as well as the future of innovation than any other book that I know of. That context will be incredibly important when you’re trying to figure out things like: “Do I file patents? How important is the role of science? How important is the role of government? How long will it take for my innovation to be adopted? How much can I expect to sink into legal battles, vs. explaining things to people, vs. building the product?” So it’s a must-read for that category of people.

The other category that it’s very relevant for is government officials. Because to the extent that many of them pay lip service to the idea of building “the next Silicon Valley” or attracting entrepreneurship, they don’t know how. People ask me this all the time, and I give them basic, vague things like, “Yeah, you need to have some freedom, you need to have nice weather, you need to have a university system.” But this book has an actionable playbook near the end  for how to foster that environment.

Matt: I’m very encouraged that you think it’s practical and actionable because that’s one thing I wanted to do in this book. Most of my books are, on the whole, thinking about the world, rather than changing the world. But in this case, I wanted to try and zero in on the practicalities of what innovation does involve.

Naval: There’s one line that I pulled out from near the end of the book which is this idea that “innovation is the child of freedom and the parent of prosperity.” I love that line. That’s a great tweet right there. Child of freedom, as to how do you create innovation? You have a very expansive definition of freedom in there. And the parents of prosperity, why it’s important. We can get into both of those, but I thought that was a good summary. I don’t know if you meant that to be the summary, but that is the one that stuck out to me.

Matt: Yes, indeed. Your ideas are often triggered by other people’s ideas. You almost need someone else to tell you what you’re saying. This freedom theme, which ended up on the cover of the book, was pointed out to me by the first reader of the book, a very intelligent friend of mine, John Constable, who thinks about things very deeply.

He came back and he said, “Well, the basic theme is freedom. Have you realized that?” And I said, “I don’t think I have realized that, no.” I then rewrote some sections, and that’s probably where that soundbite came from. It was one of the last rewrites.

Naval: Another theme that is very obvious and profound is that there’s this conversation that goes on over and over about almost everything in history: Is history the product of a few great men and women, a few great accomplishments, a few great moments, a few great battles, a few great inventions that happen to come along, or is it an inevitable, inexorable and evolved process? You conclusively lay out, with lots of evidence, that innovation is an evolutionary process, rather than an invention process. And you call it innovation rather than invention. That seems a deliberate choice. Tell me about that choice.

Invention vs. Innovation
Matt: I try to draw a distinction between invention and innovation. It’s not a distinction that is cast in iron, but I think this is the best way to think about it. Invention is the coming up with a prototype of a new device or a new social practice innovation. Innovation is the business of turning a new device into something practical, affordable and reliable that people will want to use and acquire. It’s the process of driving down the price; it’s the process of driving up the reliability and the efficiency of the device; and it’s the process of persuading other people to adopt it, too. Thomas Edison captures this point very well. I don’t think he used the word “innovation” much—he used the word “invention”—but he is mainly an innovator because he’s not necessarily coming up with original ideas. He’s taking other people’s ideas and turning them into practical propositions.

Edison said this is a process of 1% inspiration and 99% perspiration. What I’m trying to do in this book is rescue the perspirators from obscurity and slightly relegate the inspirators, who will always think they deserve the most credit, and who sometimes complain about not getting enough reward because it’s their original idea. I like to tell the story that Charles Towns, the inventor of the laser, used to tell, of a rabbit and a beaver looking at the Hoover Dam, and the beaver says to the rabbit, “No, I didn’t build it, but it’s based on an idea of mine.” That is how inventors quite often think about innovations: “Come on, I had the idea!” But it’s a huge amount of work and talent to turn an idea into something practical.

Naval: This is something that you learn in Silicon Valley very early on, that ideas are a dime a dozen. Every idea has been floating around. Even a lot of the old ideas that failed weren’t necessarily bad ideas; they were just the wrong time.

In 1999, for example, we had the dot-com bubble. We had things like Webvan and Kozmo failed back then, but now we have Instacart, Postmates and DoorDash, which work. We had Pets.com, which crashed, and now we’ve had a big dog food company bought by Amazon for over half a billion dollars. So these things do work—they just need that right structure of previous innovations to build on top of. And sometimes you’re jumping too far ahead. The previous innovations stack or the shoulders that you want to stand on, the giants don’t yet exist, so you’re trying to bootstrap too much.

Matt: One of the things I’m doing in this book is slightly downplaying the importance of disruption. Most of the time innovation is an incremental process. It looks disruptive when you’re looking backwards. but at the time it’s surprisingly gradual. The first version of a new technology looks surprisingly like the last version of an old technology.

Naval: This is the misconception about Silicon Valley that you fixed for me. I grew up reading science and scientists, and I originally wanted to be a scientist. But I was never very good. I knew I wasn’t going to be a world-class physicist, and I wanted to make money, so I pivoted into the technology business, which I thought was commercializing science and bringing it to the masses. I came to Silicon Valley thinking that invention was a thing that I’d read about, where a genius inventor comes up with a new invention and it changes the world.

Oliver and Wilbur Wright created the airplane; Samuel Morse created the telegraph; Alexander Graham Bell created the telephone; Newton and Leibniz discovered calculus—without them we would have been stuck in the Dark Ages for god knows how long. That was my view of how the world worked.

“There’s an old quip in Silicon Valley that the reason we do well is because we operate in the last unregulated domains.”

When I came to Silicon Valley, I looked around and I didn’t see that happening. I didn’t see a single genius inventor creating a single thing that suddenly changed the world. I saw, instead, lots of people doing lots of tinkering.

Somewhere in the back of my head, I adopted this mentality that, even though I am in Silicon Valley and even though it is the engine of innovation for the world today—or seems like it—we’re not as innovative as we used to be. We’ve lost the great people; we’ve lost the audacious goals; and we don’t invent new things. The lone inventor has gone away.

Your book showed me that that was a myth. That lone inventor never existed. Innovation is going on all around us right now, especially in the unregulated domains. There’s an old quip in Silicon Valley that the reason we do well is because we operate in the last unregulated domains. But it didn’t seem to me like there was innovation going on. Now I realize it’s an evolutionary process with lots of people looking at it from different views. Perhaps I am in an innovative industry, but I just can’t see it because I see the evolutionary process eternally, as opposed to the breakthrough process.

Individuals vs. Teams
Matt: I’m delighted to hear that that is what you’re experiencing because I very much set out to make that point. It’s not a case that there was a Golden Age when individuals invented things and nowadays it’s teams that do it. It was always teams, in the sense of collaborators. They weren’t necessarily working for the same institution. Our habit of giving the Nobel Prize or that patent to one individual has tended to pull out the great man of history and put him on a pedestal where he doesn’t necessarily deserve to be. He’s very important, but he’s putting the last stone in the arch and other people built the rest of the arch.

In the book I describe one of my heroes, Norman Borlaug, who developed short-strawed, high-yielding varieties of wheat in Mexico and then persuaded India and Pakistan to take them up, and effectively kicked off the Green Revolution, which drove famine largely extinct on the Indian sub-continent and led to India becoming an exporter of food rather than a chronically starving country.

But where did he get the idea of these dwarf varieties of wheat which could handle higher applications of fertilizer and therefore produce greater yields? He got it in a bar in Buenos Aires at a conference from Burton Bales, a fairly obscure agronomist who happened to be at this conference but had seen Orville Vogel growing this stuff in Oregon and crossing different varieties.

Orville Vogel had gotten these varieties from Cecil Salmon, who’d been on Douglas MacArthur’s staff in Tokyo at the end of the war and had visited agricultural stations in Japan and found these dwarf varieties growing. And they had been developed, crossed, hybridized and bred by Gonjiro Inazuka, and he had got them from somewhere in the Korean Peninsula. And at this point the trail goes cold.

If you then jump back to Norman Borlaug and say, “Yes, but he didn’t persuade India single-handedly. He talked to M.S. Swaminathan, an Indian geneticist who picked the ball up and did a huge amount of work to persuade his countrymen to take up this technology.” So there’s a nice example of what looks like a linear chain of people, but, in a sense, it’s also a team, a collaborative enterprise and a much more gradual story than it would be in the normal way of telling it.

Geographic Concentration of Innovation
Naval: This also helps explain why it tends to be geographically concentrated. If it was a breakthrough by lone individuals, you would expect innovation to be highly geographically distributed. But it tends to be very geographically concentrated where you’re surrounded by other inventors, tinkerers and thinkers, because you’re always building on little bits and pieces. We see that in Silicon Valley, where it’s geographically dense and concentrated almost to a level that seems unfair to the rest of the world. One person’s idea at a cocktail party goes to the next person at a coffee shop, goes into a prototype, which goes to a VC, who talks about it with the portfolio company, who then mentions it to another entrepreneur, and so on.

Matt: I’m amazed by how geographically concentrated innovation is at any one point in history. In the last 50 years it’s been California, but there was a period when it was Victorian Britain. There was a period when it was the low countries. There was a period when it was Renaissance Italy. At some point it was ancient Greece. It was Fujian China for a while. It was probably the Ganges Valley at a different point. Why is the bushfire only burning in one place at one time? The key to this is understanding the ecosystem in which these innovative people operate. Because they’re not only getting ideas from each other, daring each other on to be innovators and experiencing unique aspects of freedom that allow them to do it. They’re also directly borrowing technologies. It became clear to me when I was writing about the harbor process, which fixes nitrogen from the air—a very important process for good and evil in terms of making explosives, but also in terms of making fertilizer—that it couldn’t have happened without all the other industries around it in Germany that were producing the high-quality metals and chemicals that were necessary for this process. The same will be true in Silicon Valley: One idea won;t work without the neighboring company producing devices and programs that are necessary in developing your idea.

Naval: Now it’s gotten to another level where, when you first create an innovation and launch a new product, you need customers. The early-adopter customers tend to be other innovative companies. In Silicon Valley we have a critical mass of thousands of innovative companies that will adopt products from each other, so you not only find your innovator base and your talent base in one place, but you also find your customer base in one place. That network effect ends up being very tight and, of course, the local politicians exploit it with high taxes and low services, constantly attacking and blaming technology for all evils, but it works for them because this has turned into the golden goose. It’s the oil reservoir that will always be gushing, so they can get away with a lot.

Matt: Until it no longer is gushing. One of the patterns of innovators is that they move. They move from uncongenial regimes to congenial ones. The secret of Europe when it was at its most innovative was that it was fragmented politically. It’s very hard to unify Europe because of all the mountain ranges and peninsulas. So, you end up with lots of different countries. A lot of the innovative people like Gutenberg, the pioneer of printing, had to move from his hometown to another town to find a regime that would allow him. The same is true, I reckon, of China during the Song dynasty, which is the period when it was most innovative. It was a surprisingly decentralized empire at the time. And it was possible for people to move around and escape from local rule that wasn’t promising.

America is the exception that seems to prove this rule. Although it looks like an empire from the outside—a great, big unified country—once you get inside it you find that California has a quite different regime from other parts. Even this week, Elon Musk was talking about leaving California and moving to Texas because he’s so upset with the way they’re treating the end of lockdown. It’s like a 15th Century European innovator threatening to leave one part of Germany for another part of Germany.

Crypto
Naval: For a long time I had thought, despite the poor political governance, California was impregnable. It had too much of a network effect; the lock was too strong. But now I can see the cracks.

This pandemic, of course, is accelerating things, forcing people to work remotely. Twitter recently announced they’re going fully remote. Many of the companies that I’ve been involved with are wondering, “Should we even go back to having an office?” I wouldn’t be surprised if the next Silicon Valley moves to the cloud. That would be an incredibly good thing for all of humanity, because then we could distribute it. Obviously, some things can’t move to the cloud. You can’t have a semiconductor manufacturing plant in the cloud, but a lot of the initial coordination, invention, social networking, conversation, design work can happen in the cloud.

There is recent precedent for this. I don’t know how much you’ve been tracking the crypto revolution, but crypto obviously went through its big hype cycle a few years ago. At this point there’s a lot of innovation going on in crypto. We’re now in that silent under-the-radar phase where great entrepreneurs are building great products that will be more widely deployed in the next 5 to 10 years. What’s interesting about crypto is that it’s truly geographically distributed. Some of the biggest innovators in crypto are scattered all around the world. More than half of my crypto investments are outside of the Bay area, which is not true of any other class of investment that I do. Many of the top crypto innovators are anonymous, like Satoshi Nakamoto famously.

“I wouldn’t be surprised if the next Silicon Valley moves to the cloud.”

Crypto companies raise money in public, in plain sight, by issuing tokens so they’re not locked into the Sand Hill Road venture capital model. The crypto system is starting with finance but is laying the foundation for future companies to be built completely distributed with potentially anonymous contributors, anonymous funding, anonymous cash and anonymous developers. There’s even a Holy Grail of crypto called autonomous organization, which are these companies that are smart contracts living in the block chain completely extra-sovereign outside of the state, able to engage in contract laws, contract enforcement, payments, dividends, investment, equity, debt, payouts, reputations and reconstructing the corporation—but modernizing it from the Magna Carta days to a modern code-based system living on a mathematical, reputation-based, anonymous blockchain.

I wouldn’t be surprised if 10 years from now that the rest of the tech industry is just as distributed as the crypto industry is today. California and the Bay area will still do fine. They will still be a hub. I don’t believe that innovators will get priced out of the Bay area, because innovators are the highest earners in history; they’re the most leveraged people. They’re leveraged through code, capital, media, labor, intelligence—they can create more than everybody else on a per capita basis. So they can always afford to live wherever they want to live. They won’t be forced out by prices, but they may be forced out by regulations. They may be forced out by not being able to go to work because the government forbids them. They may be forced out because the place is no longer attractive to live 

If they are forced out, it would be amazing for everybody if they moved the cloud rather than to another physical location from which we may be displaced. In the examples that you gave, they’re punctuated. In between each one of them, there’s 50, 100, 200 years that pass where there is no place to innovate. Therefore, the rate of innovation collapses. So if innovation is the flower of a well-tended garden, if you have to uproot those flowers and shift them, there is a huge deadweight loss to society when, for decades or perhaps even centuries, we have to wait for another garden to emerge and for people to coalesce there for this right magic soup of deregulation combined with innovators, good weather and a rich society— all of that has to assemble.

Matt: Thank you very much for that, because that has filled in a gap in my understanding in one go. I’ve always been interested in the fact that these innovation bush fires eventually are extinguished by some combination of chiefs, priests and thieves, if you like. 

Naval: I like that: chiefs, priests and thieves. Or, as a wag might say, “Chiefs, priests and thieves—what’s the difference?”

Political Fragmentation and Innovation
Matt: Right, exactly. So, in Ming China it’s a very, restrictive authoritarian and interfering political regime that kills the goose that’s laying the golden eggs. In Abbasid Arabia, not hugely different in the time period—we’re talking about 1100s—a great, flowering of knowledge and innovation is crushed by a religious fundamentalist revival when Islam goes from being a very open-minded to a very closed-minded structure. Something similar is happening in Paris around the same time. Bernard of Clairvaux was burning books. I singled that out in a previous book as a period when it’s possible the world could’ve lost this habit all together. It could’ve given up on innovation everywhere. The flame would’ve been extinguished.

“What if America does lose its mojo and we have to rely on China for the world’s innovation engine?”

Fortunately, the Italian city-states kept the flame burning. I write about Fibonacci, the Italian merchant who brings Indian numerals from North Africa back to Italy, and they spread around the world. It’s lucky that somewhere keeps the show on the road at each stage in history, but it’s not accidental. These are people escaping the other regime and starting it again. But I did worry that, in the old days, there was always somewhere else to go and in this global world. You could imagine a sufficiently benighted cult taking over the entire world and saying, “No, we don’t want learning, innovation and technology. We want to stop everything.”

It’s very unlikely, but what if America does lose its mojo and we have to rely on China for the world’s innovation engine? China is not a free place. It’s a politically dictatorial regime, albeit there’s a certain amount of freedom for entrepreneurs below the level of politics. If that’s our only hope, it’s not a great prospect. Maybe India can pick up the pattern. Europes not great at picking up the pattern at the moment; it’s not a very innovative continent. It’s trying to centralize all its decision making through the European Union.

But India has done this before. It was probably the first place to start all this going. A place of free thought and a lot of spontaneous order— a lot of spontaneous disorder, too. Maybe that’s the place. But you’ve given me another prospect, which is this escape from the chiefs, priests and thieves into the cloud where it can be out of their reach for at least long enough until they work out how to reach it.

Naval: I think the digital innovation can escape into the cloud. Obviously, physical innovation requires physical infrastructure, and that would depend on the enlightened city state, a Switzerland type place or Hong Kong. A Singapore or a New Zealand. But then you have the small-market problem. You don’t have many early adopters of the technology. Although you can build a prototype, you can’t deploy it in volume. I do think physical innovation is in trouble, and you talk about this in the book. The speed of innovation has been very low in some places. For example, we can’t travel any faster than we used to. Why is that? It’s mostly for regulatory reasons.

One underlying theme running this whole book is innovation is a process of evolution. Like any process of evolution, it requires trial and error. Innovation happens by taking the body of innovators that surround you one step further, engaging in lots of trials and then having error and feedback from customers and the economy. All of those pieces are necessary. You need to have a body of innovators around you, which means there has to be a place where they can all gather, whether it’s online or offline.

There has to be the ability to take lots of tries. You need venture capital. You need start-ups. You need a friendly environment to start a business. We don’t like people making errors anymore, so we try to cover the downside risk. But by doing that we’ve also cut off the upside. Finally, you need the feedback loop from the environment, and part of that involves a large customer base.

“California doesn’t create entrepreneurs. California attracts entrepreneurs.”

So I’m optimistic that we can do this in the digital domain. I can see that happening in crypto, for example. But I’m a little pessimistic in the physical domain, which is unfortunate because a lot of the big problems of humanity that we have to solve—like the energy problem, getting nuclear fusion working at large scale or the transportation problem, moving people around quickly with hypersonic jets, or even some of the biotech problems—these require physical infrastructure and large markets that are relatively deregulated. So I think you’re right that we’re down to India and China—and neither of those is ideal. China is not going to be a place where the next Jew fleeing the Nazis is going to go because China is not an integration destination. It doesn’t attract the best and brightest.

California doesn’t create entrepreneurs. California attracts entrepreneurs. China is not going to be an attractor, and it will always be limited because of that. Even though India has a lot of the other elements, it doesn’t have the basic infrastructure to make it an attractive place to go. Because of its poverty level, India also has a very anti-innovation culture. Innovators in India often survive by keeping their heads down. You can see this in how India banned crypto. Hopefully that’ll get overturned, but they can do things like that. Early on something got listed on eBay India that wasn’t supposed to be listed, so they just rounded up the local eBay managers and threw them in jail.

The history of India fostering innovation recently has not been great. That said, there is a flowering going on right now in places like Bangalore, Mumbai and Delhi. Hopefully, as India gets richer and is run by a more competent government, we’re going to see them step out of the way and allow India to become an innovation hub. The market there is large enough; they’re poor enough that they could welcome it; they speak English; they’re very well educated; there’s a deep respect for STEM—so India could be one of these hubs. But they would also need immigration and clean, beautiful places where people want to live. Innovators are going to go live where they want to live because they’re so productive.

You said something else very interesting: What about people who may create a global movement to stop innovation? That is very scary and very possible. Take environmentalism for example. It runs on two tracks today. There’s local environmentalism that everybody can get behind—clean up my rivers, save the species, I want trees, forests and parks. Everybody likes that. Then it gets mixed into this global command and control environmentalism, which says, “You must stop progress. you must stop innovation, you must stop everything because you’re destroying the environment.” One of the things that you talk about in your book is how the world is refreshing, how innovation allows us to do more with less, and how we’ve become much more efficient as a society.

We’re not going to be able to stop India and China from growing. We’re not going to be able to stop them from innovating. We’re not going to be able to stop them from modernizing. We can do what Elon Musk does: He says let me give them solar-powered electric cars and rockets as quickly as possible so they can jump through the wasteful phase of innovation, where there’s a lot of environmental destruction, and get to the part where we can all afford clean rivers beautiful forests, nice parks and other species in our environment. By the way, I credit this to Genome. The book paints a picture of utopia.

Not in the sense of a top-down, human-enforced, platonic sense of this is how the world should be run, but in how the natural world is designed and operates, and our role in it. Genome paints a picture of paradise being a garden. This is in our deeply embedded myths: The paradise that Adam and Eve live in is a garden. They fall from grace, and they fall out of the garden. 

Today in Covid-19 land, where do you want to be living? In your little apartment in New York city or a little flat in London? Or do you want to be sitting in a beautiful garden out in the sunshine? Humans inherently want a clean and beautiful environment, but that movement gets hacked by top-down command-and-control mechanisms by chiefs, priests and thieves who can then squander our existing resources as well as squash innovation, which prevents us from moving forward. ''',

                '20': '''Who Is Robert Cialdini? Meet the Master of Influence and Persuasion
Dr. Robert Cialdini is the mind behind Influence: The Psychology of Persuasion, one of the great and enduring works of social psychology, along with a number of other books, including Pre-Suasion: A Revolutionary Way to Influence and Persuade. Cialdini’s work is among the world’s best resources on how we persuade others and how we are persuaded.

“There is no expedient to which a man will not resort to avoid the real labor of thinking.”
Robert Beno Cialdini grew up in the 1950s and 1960s, a time when psychology’s influence on the public was large and growing. Dr. Spock told us how to raise kids. Freudian and Jungian psychotherapy was a growing practice, Abraham Maslow proposed his hierarchy of needs, B.F. Skinner proposed behavioral therapy, Alfred Kinsey was showing us our sexuality, and Stanley Milgram conducted his famous experiment on authority.

After attending the University of Wisconsin, the University of North Carolina (where he earned his Ph.D.), and Columbia University (for post-doctoral training), Cialdini eventually went on to make his own contributions to the field of psychology, as important as any of those he grew up with. His work on influence would be summarized in his legendary book on social psychology Influence, as well as a number of later books.

Human beings are automatically, unavoidably influenced, in definite and predictable ways, by the actions of those around us. By pointing out six principles of influence and associating them with a number of clever, well-designed experiments and real-life experiences to prove them, Cialdini synthesized a theory of what he called a “click-whirr” reaction in the mind: an automatic reaction reminiscent of Daniel Kahneman’s description of the brain’s “System 1” thinking.

Cialdini believes that if we are not careful, we can be manipulated into parting ways with our money, our time, our lives, and ourselves. The only way to protect against that is to be aware of all the tricks people can use to persuade us. For that, Cialdini deserves his reputation as a Master of Influence.

Robert Cialdini Quotes
“We seem to assume that if a lot of people are doing the same thing, they must know something we don’t.”

“Since 95 percent of the people are imitators and only 5 percent initiators, people are persuaded more by the actions of others than by any proof we can offer.”

“In part, the answer involves an essential but poorly appreciated tenet of all communication: what we present first changes the way people experience what we present to them next.”

“We will use the actions of others to decide on proper behavior for ourselves, especially when we view those others as similar to ourselves.”

“In general, when we are unsure of ourselves, when the situation is unclear or ambiguous, when uncertainty reigns, we are most likely to look to and accept the actions of others as correct.”

“There is an obligation to give, an obligation to receive, and an obligation to repay.”

“Freedoms once granted will not be relinquished without a fight.”

“Advertisers love to inform us when a product is the ‘fastest-growing’ or ‘largest-selling’ because they don’t have to convince us directly that the product is good; they need only say that many others think so, which seems proof enough.”

“As the stimuli saturating our lives continue to grow more intricate and variable, we will have to depend increasingly on our shortcuts to handle them all.”

Suggested Readings on Robert Cialdini
Robert Cialdini on the Best Persuasion Technique for Job-Seekers – Cialdini talks about the best way job-seekers can use persuasion to help them land a job.

The Principles of Influence – A short video of Cialdini introducing the universal principles of influence.

The Psychology of Persuasion – More discussion of the six principles of persuasion.

Secrets from the Science of Persuasion – An animated look at the psychology of persuasion.

Yes! 50 Scientifically Proven Ways to Be Persuasive – Here are the 50 ways you can become more persuasive, from Cialdini’s book of that name.

Mental Model: Commitment and Consistency Bias – Cialdini uncovered one of the great useful psychology principles: our preference for commitment and consistency.

Social Proof: Why We Look to Others For What We Should Think and Do – Why do we do what we do? Because other people are doing it.

How Raising Prices Can Increase Sales – Cialdini suggests that in some cases, businesses can actually increase their sales by raising prices.

What Lovers Tell Us About Persuasion – As Cialdini concludes, “We’d be fools to think that a force as primitive and powerful as human connection can direct change only within romantic relationships.”

The Most Effective Way to Retain What You Read – Cialdini offers a great method of helping to hang on to what you read.

Videos
The Big Think: How to Use Pre-suasive Tactics on Others – and Yourself
Six Ways to Get People to Say “Yes”
Articles
The Uses (and Abuses) of Influence
Robert Cialdini: How To Master The Art Of ‘Pre-Suasion’
Robert Cialdini’s Blog
Books
Influence: The Psychology of Persuasion

Yes: 50 Scientifically Proven Ways to Be Persuasive

Pre-Suasion: A Revolutionary Way to Influence and Persuade

Book Recommendations
5 Book Recommendations from Robert Cialdini ''',

                '21': '''Yes, My Son (A Story Of Non-Attachment)


Once long ago, a man had a young son.

He did everything for the boy.

He taught him everything he knew.

He gave him all that he had.

When the boy turned 20, he turned to his father and said, “Father, I have decided to leave home. I will now go my own way.”

The father said, “Yes, my son.”

After six months of living on his own, he asked his father for money.

The father said, “Yes, my son.”

A few more years passed. The son wrote a letter to his father from a faraway land.

The letter said, “Father, I realize you did your best. But your ideas about early to bed and early to rise I find to be rather foolish. I have found some friends. They live carefree. We are not beholden to this and that. I will live my life as I choose. And make rules as I see fit.”

The father penned a reply. He wrote, “Yes, my son.”

The son married. And his wife did not approve of his father.

She convinced him not to invite his father to the wedding.

The son wrote a letter to his father. Apologizing for not having invited him. And that he would one day come and visit.

The father penned a reply. He wrote, “Yes, my son.”

It had been years since the boy had come to see his father.

The seasons had not been kind to the aging man.

The boy and his wife had fallen on hard times.

He wrote a letter to his father, asking him for financial assistance.

The father sent him money, accompanied by a letter that said, “Yes, my son.”

The father grew old. His time had come.

He wrote a letter to his son, requesting to see him before he passed on.

The son came to see him.

He sat next to his father on the edge of the bed.

And he began to cry.

“Father,” he said. “I have not been good to you. Why did you not correct me? Why did you not lead me away from my own ignorance?”

The father did not reply.

The boy asked again, “Father, tell me. I am beside myself with guilt. Why did you not teach me the proper way of things?”

The father broke his silence.

“Son, when you were small, I had so much to teach you. I was overjoyed by the times I tried to guide you and instruct you. But all my efforts failed. And the reason I failed is because the things that I had to teach you were not born of wisdom. They were born of my own limited experiences. They were born of my own biased views. Truth be told, I do not know what is right and what is wrong. For there are so many things that I once swore were right. But in the end, they turned out to be wrong.”

The son replied, “But Father, surely what I have done cannot be right.”

The father said, “If it is not right, this is a conclusion that only you can make. And as I see the tears in your eyes, I must attest to the fact that it is right. For you speak with true sincerity. Son, in the end a man has very little to teach another. For his knowledge is born of his own sense of ego and need.”

The son said, “Father, do you not need anything from me?”

The father replied, “I stopped needing from you long ago, my son.”

“But why?” said the son.

The father said, “Because this need became a noose around my neck. And a weight upon your back.”

The son replied, “Father, do you love me?”

The father said, “I love the very sight of you, and the very shadow by your side. But I have abandoned all need. From you and from anyone and anything in this world. Understand, my son. That it is this, and this alone, that allows me to truly love you.”

Namaste. ''',

                '22': '''The Difference Between Amateurs and Professionals
READING TIME: 2 MINUTES
Why is it that some people seem to be hugely successful and do so much, while the vast majority of us struggle to tread water?

The answer is complicated and likely multifaceted.

One aspect is mindset—specifically, the difference between amateurs and professionals.

Most of us are just amateurs.

What’s the difference? Actually, there are many differences:

Amateurs stop when they achieve something. Professionals understand that the initial achievement is just the beginning.
Amateurs have a goal. Professionals have a process.
Amateurs think they are good at everything. Professionals understand their circles of competence.
Amateurs see feedback and coaching as someone criticizing them as a person. Professionals know they have weak spots and seek out thoughtful criticism.
Amateurs value isolated performance. Think about the receiver who catches the ball once on a difficult throw. Professionals value consistency. Can I catch the ball in the same situation 9 times out of 10?
Amateurs give up at the first sign of trouble and assume they’re failures. Professionals see failure as part of the path to growth and mastery.
Amateurs don’t have any idea what improves the odds of achieving good outcomes. Professionals do.
Amateurs show up to practice to have fun. Professionals realize that what happens in practice happens in games.
Amateurs focus on identifying their weaknesses and improving them. Professionals focus on their strengths and on finding people who are strong where they are weak.
Amateurs think knowledge is power. Professionals pass on wisdom and advice.
Amateurs focus on being right. Professionals focus on getting the best outcome.
Amateurs focus on first-level thinking. Professionals focus on second-order thinking.
Amateurs think good outcomes are the result of their brilliance. Professionals understand when good outcomes are the result of luck.
Amateurs focus on the short term. Professionals focus on the long term.
Amateurs focus on tearing other people down. Professionals focus on making everyone better.
Amateurs make decisions in committees so there is no one person responsible if things go wrong. Professionals make decisions as individuals and accept responsibility.
Amateurs blame others. Professionals accept responsibility.
Amateurs show up inconsistently. Professionals show up every day.
Amateurs go faster. Professionals go further.
Amateurs go with the first idea that comes into their head. Professionals realize the first idea is rarely the best idea.
Amateurs think in ways that can’t be invalidated. Professionals don’t.
Amateurs think in absolutes. Professionals think in probabilities.
Amateurs think the probability of them having the best idea is high. Professionals know the probability of that is low.
Amateurs think reality is what they want to see. Professionals know reality is what’s true.
Amateurs think disagreements are threats. Professionals see them as an opportunity to learn.
There are a host of other differences, but they can effectively be boiled down to two things: fear and reality.

Amateurs believe that the world should work the way they want it to. Professionals realize that they have to work with the world as they find it. Amateurs are scared — scared to be vulnerable and honest with themselves. Professionals feel like they are capable of handling almost anything.

Luck aside, which approach do you think is going to yield better results?

Food for Thought:
In what circumstances do you find yourself behaving like an amateur instead of as a professional?
What’s holding you back? Are you hanging around people who are amateurs when you should be hanging around professionals? ''',

                '23': '''Meet Silq- The First Intuitive High-Level Language for Quantum Computers

Jul 29, 2020
Sometime in the 1970s, the computing world hit its first major breakthrough - Dennis Ritchie and Ken Thompson at AT&T Bell Laboratories founded the Holy Grail of C programming. It took another 50 years for programmers to achieve a milestone of similar force - a language that brought a comparable level of simplicity and functions to quantum computing.

Introducing Silq - “A new high-level programming language for quantum computing with a strong static type system”- the first and only one of its kind!

A Look at the 21st Century’s Big Bang
Martin Vechev, associate professor of computer science at ETH Switzerland, says it all began when his team of researchers wanted to “solve a core problem in quantum computing.” Expressing his predicament, he said:

“We looked at various problems in quantum computing but what kept coming up as a fundamental issue is that we looked at the programs and how they are expressed — and you see that this is not ideal, this is not optimal.”

The existing languages, including Microsoft’s Q# and IBM’s Qiskit, were failing to meet the high-level properties criteria required for the project. So while they did not begin with a programming end-result in their minds, necessity paved their way to it.

"Silq is the first quantum programming language that is not designed primarily around the construction and functionality of the hardware, but on the mindset of the programmers when they want to solve a problem — without requiring them to understand every detail of the computer architecture and implementation." – Benjamin Bichsel

Before we begin to analyze the programming goldmine Silq, let’s tap on a few basics:

Quantum Computing
Classical computers have been working on a series of zeros and ones. Known as the future of computing, quantum computing works in qubits, which could be ones, zeros, or both.



High-level Languages
Computer languages that detach themselves from the technical details of the distinct type of computer are called high-level programming languages.

Compatible with different computer architectures, these languages are more expressive and they can explain even complex algorithms and tasks with less code. Programmers find these languages easier to understand and use.

Limitations of Current Quantum Programming Languages
James Wootton, a quantum computing researcher at IBM, says the current frameworks of quantum computing are “much like the classical logic circuits that I used to assemble in my shed as a kid, so it is more intuitive than some might assume. But it is certainly not the method that all the quantum programmers of the future will want to use.”

Several others in the fraternity echo these sentiments, including Benjamin Bichsel, Silq co-creator who said: “Existing quantum languages are [really] more low-level than assembly languages in some aspects: They typically describe operations on individual quantum bits, which is more in line with low-level hardware description languages like VHDL or Verilog.”

How Silq Improves Upon These Limitations
Speaking about the existing approaches to quantum computing, Wootton says: “Currently, the main approach to quantum computation is at the machine code level, or by using and adapting tools that others have already built.”

Silq facilitates a C-level abstraction and supports subexpressions, a trait unavailable in existing quantum languages.

Present quantum computing languages are closely linked with the hardware. These languages are error-prone, cumbersome, and need detailed instructions.

Bichsel says that because Silq programs are less concerned about low-level details, analyzing them is easier. It is an excellent option for those who want to create their own quantum algorithms and not depend on the existing frameworks. It bridges the conceptual gap between the classical and quantum languages.

Other Features
According to Bischel, “The key benefit of Silq is that it automatically handles uncomputation of temporary values. Unlike in the classical setting, where we can simply forget about temporary values that are produced during a computation, discarding temporary values in the quantum setting requires explicit operations to remove these values from consideration.”



Aside from this, Silq:

Can automatically remove garbage or superfluous values that can result in quantum entanglement*

Is more compact, quicker, and more intuitive

Has a compiler type-checker that restricts programmers from making common errors

Has much shorter programs than those written in Q# and Quipper

Incorporates the latest developments in classical languages

Needs significantly less code and fewer built-in functions, gates, and annotations, as compared to Q#

“In our case, because we are more high-level, we envision the compilation as a two-step process, where first you express your high-level intent and then it’s the job of the compiler to decide which architecture will this run on and how to optimize for a particular architecture.” – Bischel

Looking at the impact and applicability of the language, we expect many more benefits to emerge in the near future. The future of quantum computing sure looks promising!

Trivia:
Silq is written in the D programming language.

To install Silq via vscode, see: https://silq.ethz.ch/install.

A timeline of major developments in quantum computing: ''',

                '24': '''Claude Shannon: Tinkerer, Prankster, and Father of Information Theory
Shannon, who died in 2001, is regarded as one of the greatest electrical engineering heroes of all time. This profile, originally published in 1992, reveals the many facets of his life and work
By John Horgan

Advertisement
Editor's Picks
photo of Shannon
Meet the Authors of A Mind at Play: How Claude Shannon Invented the Information Age
null
Bell Labs Looks at Claude Shannon’s Legacy and the Future of Information Age
Photo of Claude Shannon at Bell Labs during World War II
A Man in a Hurry: Claude Shannon’s New York Years
Shannon profile opener
Editor’s note: This month marks the centennial of the birth of Claude Shannon, the American mathematician and electrical engineer whose groundbreaking work laid out the theoretical foundation for modern digital communications. To celebrate the occasion, we’re republishing online a memorable profile of Shannon that IEEE Spectrum ran in its April 1992 issue.

Written by former Spectrum editor John Horgan, who interviewed Shannon at his home in Winchester, Mass., the profile reveals the many facets of Shannon’s character: While best known as the father of information theory, Shannon was also an inventor, tinkerer, puzzle solver, and prankster. The 1992 profile included a portrait of Shannon taken by Boston-area photographer Stanley Rowin. On this page we’re reproducing that portrait along with other Shannon photos by Rowin that Spectrum has never published.

Shannon died in 2001 at age 84 after a long battle with Alzheimer’s disease. He is regarded as one of the greatest electrical engineering heroes of all time.

Who is the real Claude Shannon? A visitor to Entropy House, the stuccoed mansion outside Boston where Shannon and his wife Betty have lived for more than 30 years, might reach different conclusions in different rooms. One room, prim and tidy, is lined with plaques that solemnly testify to Shannon’s numerous honors, including the National Medal of Science, which he received in 1966; the Kyoto Prize, Japan’s equivalent of the Nobel; and the IEEE Medal of Honor.

That room enshrines the Shannon whose work Robert W. Lucky, the executive director of research for AT&T Bell Laboratories, has called the greatest “in the annals of technological thought,” and whose “pioneering insight” IBM Fellow Rolf W. Landauer has equated with Einstein’s. That Shannon is the one who, as a young engineer at Bell Laboratories in 1948, defined the field of information theory. With a brilliant paper in the Bell System Technical Journal, he established the intellectual framework for the efficient packaging and transmission of electronic data. The paper, entitled “A Mathematical Theory of Communication,” still stands as the Magna Carta of the communications age. [Editor’s note: Read the paper on IEEE Xplore: Parts I and II; Part III.]

But showing a recent visitor his awards, Shannon, who at 75 has a shock of snowy hair and an elfish grin, seemed almost embarrassed. After a fidgety minute, he bolted into the room next door. This room has framed certificates, too, including one certifying Shannon as a “doctor of juggling.” But it is also lined with tables heaped with all kinds of gadgets.

photo of Claude Shannon
Some of these treasures—such as the talking chess-playing machine, the hundred-blade jackknife, the motorized pogo stick, and the countless musical instruments—Shannon has collected through the years. Others he has built himself: a miniature stage with three juggling clowns,  a mechanical mouse that finds its way out of a maze, a juggling manikin of the comedian W.C. Fields, and a computer called Throbac (Thrifty Roman Numeral Backward Computer) that calculates in Roman numerals. Shannon tried to get the manikin W.C. Fields to demonstrate his prowess, but in vain. “I love building machines, but it’s hard keeping them in repair,” he said a bit wistfully.

This roomful of gadgets reveals the other Shannon, the one who rode through the halls of Bell Laboratories on a unicycle while simultaneously juggling four balls, invented a rocket-powered Frisbee, and designed a “mind-reading” machine.

This room typifies the Shannon who—seeking insights that could lead to a chess-playing machine—began playing so much chess at work that “at least one supervisor became somewhat worried,” according to a former colleague.

Suggested Wiley-IEEE Reading
Understanding Information Transmission
Multimedia Information Extraction: Advances in Video, Audio, and Imagery Analysis for Search, Data Mining, Surveillance and AuthoringMultimedia Information Extraction: Advances in Video, Audio, and Imagery Analysis for Search, Data Mining, Surveillance and Authoring
Shannon makes no apologies. “I’ve always pursued my interests without much regard for final value or value to the world,” he said cheerfully. “I’ve spent lots of time on totally useless things.”

The Gold Bug Influence
Shannon’s delight in both mathematical abstractions and gadgetry emerged early on. Growing up in Gaylord, Mich., near where he was born in 1916, Shannon played with radio kits and erector sets supplied by his father, a probate judge. He also enjoyed solving mathematical puzzles given to him by his sister, Catherine, who eventually became a professor of mathematics.

“I was always interested, even as a boy, in cryptography and things of that sort,” Shannon said. One of his favorite stories was “The Gold Bug,” an Edgar Allan Poe mystery with a rare happy ending: By decoding a mysterious map, the hero finds a buried treasure.

As an undergraduate at the University of Michigan, in Ann Arbor, Shannon majored in both mathematics and electrical engineering. His familiarity with the two fields helped him notch his first big success as a graduate student at the Massachusetts Institute of Technology (MIT), in Cambridge. Following a discussion of complex telephone switching circuits with Amos Joel, famed Bell Laboratories expert in the topic, in his master’s thesis Shannon showed how an algebra invented by the British mathematician George Boole in the mid-1800s—which deals with such concepts as “if X or Y happens but not Z, then Q results”—could represent the workings of switches and relays in electronic circuits. 

Claude Elwood Shannon
Date of birth: 30 April 1916

Birthplace: Petosky, Mich.

Height: 178 centimeters

Weight: 68 kilograms

Childhood hero: Thomas Alva Edison

First job: Western Union messenger boy

Family: Married to Mary Elizabeth (Betty) Moore; three children: Robert J., computer engineer; Andrew M., musician; and Margarita C., geologist

Education: B.S., 1936, University of Michigan; M.S., 1940, Ph.D., 1940, Massachusetts Institute of Technology

Hobbies: Building gadgets, juggling, unicycling

Favorite invention: A juggling W.C. Fields robot

Favorite author: T. S. Eliot

Favorite music: Dixieland jazz

Favorite food: Vanilla ice cream with chocolate sauce

Memberships and awards: Fellow, IEEE; member, National Academy of Sciences, American Academy of Arts and Sciences; 1966 IEEE Medal of Honor; 1966 National Medal of Science; 1972 Harvey Prize; 1985 Kyoto Prize

Favorite award: 1940 American Institute of Electrical Engineers award for master’s thesis

The implications of the paper by the 22-year-old student were profound: Circuit designs could be tested mathematically, before they were built, rather than through tedious trial and error. Engineers now routinely design computer hardware and software, telephone networks, and other complex systems with the aid of Boolean algebra.

Shannon’s paper has been called “possibly the most important master’s thesis in the century,” but Shannon, typically, downplays it. “It just happened that no one else was familiar with both those fields at the same time,” he said. After a moment’s reflection, he added, “I’ve always loved that word, ‘Boolean.’”

Receiving his doctorate from MIT in 1940 (his Ph.D. thesis addressed the mathematics of genetic transmission), Shannon then spent a year at the Institute for Advanced Study, in Princeton, N.J. Lowering his voice dramatically, Shannon recalled how he was giving a talk at the institute when suddenly the legendary Einstein entered a door at the rear of the room. Einstein looked at Shannon, whispered something to another scientist, and departed. After his talk, Shannon rushed over to the scientist and asked him what Einstein had said. The scientist gravely told him that the great physicist had “wanted to know where the tea was,” Shannon said, and burst into laughter.

How Do You Spell “Eureka”?
Shannon went to Bell Laboratories in 1941 and remained there for 15 years. During World War II, he was part of a group that developed digital encryption systems, including one that Churchill and Roosevelt used for transoceanic conferences.

It was this work, Shannon said, that led him to develop his theory of communication. He realized that, just as digital codes could protect information from prying eyes, so could they shield it from the ravages of static or other forms of interference. The codes could also be used to package information more efficiently, so that more of it could be carried over a given channel.

“My first thinking about [information theory],” Shannon said, “was how you best improve information transmission over a noisy channel. This was a specific problem, where you’re thinking about a telegraph system or a telephone system. But when you get to thinking about that, you begin to generalize in your head about all these broader applications.” Asked whether at any point he had a “Eureka!”-style flash of insight, Shannon deflected the simplistic question with, “I would have, but I didn’t know how to spell the word.”

The definition of information set forth in Shannon’s 1948 paper is crucial to his theory of communication. Sidestepping questions about meaning (which he has stressed that his theory “can’t and wasn’t intended to address”), Shannon demonstrated that information is a measurable commodity. The amount of information in a given message, he showed, is determined by the probability that—out of all the messages that could be sent—that particular message would be selected.

He defined the overall potential for information in a system as its “entropy,” which in thermodynamics denotes the randomness—or “shuffledness,” as one physicist has put it—of a system. (The great mathematician and computer theoretician John von Neumann persuaded Shannon to use the word entropy. The fact that no one knows what entropy really is, von Neumann argued, would give Shannon an edge in debates over information theory.)

Shannon defined the basic unit of information, which John Tukey of Bell Laboratories dubbed a binary unit and then a bit, as a message representing one of two states. One could encode a great deal of information in relatively few bits, just as in the old game “Twenty Questions” one could quickly zero in on the correct answer through deft questioning.

Building on this mathematical foundation, Shannon then showed that any given communications channel has a maximum capacity for reliably transmitting information. Actually, he showed that although one can approach this maximum through clever coding, one can never quite reach it. The maximum has come to be known as the Shannon limit.

Shannon’s 1948 paper showed how to calculate the Shannon limit—but not how to approach it. Shannon and others took up that challenge later. The first step was to eliminate redundancy from the message. Just as a laconic Romeo can get his message across with a mere “i lv u,” a good code first compresses information to its most efficient form.

A so-called error-correction code then adds just enough redundancy to ensure that the stripped-down message is not obscured by noise. For example, an error-correction code processing a stream of numbers might add a polynomial equation on whose graph the numbers all fall. The decoder on the receiving end knows that any numbers diverging from the graph have been altered in transmission.

Aaron D. Wyner, the head of the Communications Analysis Research Department at the AT&T Bell Laboratories, in Murray Hill, N.J., noted that some scientific discoveries seem in retrospect to be inevitably products of their times—but not Shannon’s.

In fact Shannon’s ideas were almost too prescient to have an immediate impact. “A lot of practical people around the labs thought it was an interesting theory but not very useful,” said Edgar Gilbert, who went to Bell Labs in 1948—in part to work alongside Shannon. Vacuum-tube circuits simply could not handle the complex codes needed to approach the Shannon limit, Gilbert explained. Shannon’s paper even received a negative review from J. L. Doob, a prominent mathematician at the University of Illinois, in Urbana-Champaign. Historian William Aspray also noted that in any event the conceptual framework was not in place to permit the application of information theory at the time.

Not until the early 1970s—with the advent of high-speed integrated circuits—did engineers begin fully to exploit information theory. Today Shannon’s insights help shape virtually all systems that store, process, or transmit information in digital form—from compact discs to supercomputers, from facsimile machines to deep-space probes such as Voyager.

Solomon W. Golomb, an electrical engineer at the University of Southern California, Los Angeles, and a former president of the IEEE Information Theory Society, thinks Shannon’s influence cannot be overstated. “It’s like saying how much influence the inventor of the alphabet has had on literature,” Golomb remarked.

photo of Claude Shannon
Information Theory and Religion
Especially early on, however, information theory captivated an audience much larger than the one for which it was intended. People in linguistics, psychology, economics, biology, even music and the arts sought to fuse information theory to their disciplines.

John R. Pierce, a former coworker of Shannon who is now a professor emeritus at California’s Stanford University, has compared the “widespread abuse” of information theory to that inflicted on two other profound and much misunderstood scientific ideas: Heisenberg’s uncertainty principle and Einstein’s theory of relativity.

Some physicists went to extraordinary lengths to prove that the entropy of information theory was mathematically equivalent to the entropy in thermodynamics. That turned out to be true but of little consequence, according to Bell Labs veteran David Slepian, a former colleague of Shannon at the laboratories who was also a seminal figure in information coding. Many engineers, too, “jumped on the bandwagon without really understanding” the theory, Slepian said. Shannon’s work inspired the formation of the IEEE Information Theory Society in 1956, and subgroups dedicated to economics, biological systems, and other applications soon formed. In the early 1970s, the IEEE Transactions on Information Theory published an editorial, titled “Information Theory, Photosynthesis, and Religion,” deploring the overextension of Shannon’s theory. [Editor’s note: In fact, the editorial, by Peter Elias, was titled “Two Famous Papers” and was published in September 1958.]

Shannon, while also skeptical of some of the uses of his theory, was rather free-ranging in his own investigations. In the 1950s, he did living-room experiments on the redundancy of language with his wife, Betty, who was a Bell computer scientist; Bernard Oliver, another Bell scientist (and a former IEEE president); and Oliver’s wife. One person would offer the first few letters of a word, or words in a sentence, and the others would try to guess what came next. Shannon also directed an experiment at Bell Labs in which workers counted the number of times various letters appeared in a written text, and their order of appearance.

Moreover, Shannon has suggested that applying information theory to biological systems, at least, may not be so far-fetched. “The nervous system is a complex communication system, and it processes information in complicated ways,” he said. When asked whether he thought machines could “think,” he replied: “You bet. I’m a machine and you’re a machine, and we both think, don’t we?”

Indeed, Shannon’s work on information theory and his love of gadgets led to a precocious fascination with intelligent machines. Shannon was one of the first scientists to propose that a computer could compete with humans in chess; in 1950 he wrote an article for Scientific American explaining how that task might be accomplished.

Shannon did not restrict himself to chess. He built a “mind-reading” machine that played the game of penny-matching, in which one person tries to guess whether the other has chosen heads or tails. A colleague at Bell Laboratories, David W. Hagelbarger, built the prototype; the machine recorded and analyzed its opponents’ past choices, looking for patterns that would foretell the next choice. Because humans almost invariably fall into such patterns, the machine won more than 50 percent of the time. Shannon then built his own version of the machine and challenged Hagelbarger to a now legendary duel.

He also constructed a machine that could beat any human player at a board game called Hex, which was popular among the mathematically inclined a few decades back. Actually, Shannon had customized the board so that the human player’s side had more hexes than the other; all the machine had to do to win was take the center hex and then match its opponent’s moves thereafter.

The machine could have moved instantly, but to convey the impression that it was pondering its next move, Shannon added a delay switch to its circuit. Andrew Gleason, a brilliant mathematician from Harvard, challenged the machine to a game, vowing that no machine could beat him. Only when Gleason, after being soundly thrashed, demanded a rematch did Shannon finally reveal the machine’s secret.

In 1950 Shannon created a mechanical mouse that could learn how to find its way through a maze to a chunk of brass cheese, seemingly unassisted. Shannon named the mouse Theseus, after the mythical Greek hero who slew the Minotaur and found his way out of the dreaded labyrinth. Actually, the “brains” of the mouse were contained in a bulky set of vacuum-tube circuitry under the floor of the maze; the circuits controlled the movement of a magnet which in turn controlled the mouse.

When in 1977 the editor of IEEE Spectrum challenged readers to create a “micromouse” whose “brains” were self-contained, who could through trial and error solve a maze, and who could then learn through its mistakes and get through the maze in a repeat attempt without error, a former colleague of Shannon called Spectrum and insisted that Shannon had built such a micromouse two decades earlier.

Knowing the technology of the ’50s would not have permitted it, the editor nevertheless called Shannon, who laughed, saying he had fooled a lot of people as he took his “smart” mouse around the country. The drapes around the table that hid the vacuum tubes and lead-screw machinery were vital, he chuckled. When Spectrum ceremoniously presented its Amazing Micromouse Maze Contest awards in 1979, Shannon got Theseus down from his attic, loaded him into his station wagon, and put him on display alongside the lineup of contending micromice.

Asked about prospects for artificial intelligence, Shannon noted that current computers, in spite of their extraordinary power, are still “not up to the human level yet” in terms of raw information processing. Simply replicating human vision in a machine, he points out, remains a formidable task. But he added that “it is certainly plausible to me that in a few decades machines will be beyond humans.”

Unified Field Theory of Juggling
In 1956 Shannon left his permanent position at Bell Labs (he remained affiliated for more than a decade) to become a professor of communications science at MIT. In recent years, his great obsession has been juggling. He has built several juggling machines and devised what may be the unified field theory of juggling: If B equals the number of balls, H the number of hands, D the time each ball spends in a hand, F the time of flight of each ball, and E the time each hand is empty, then B/H = (D + F)/(D + E).

(Unfortunately, the theory could not help Shannon juggle more than four balls at once. He has claimed his hands are too small.)

Shannon has also developed various mathematical models to predict stock performance and has tested them—successfully, he said—on his own portfolio.

He has even dabbled in poetry. Among his works is a homage to the Rubik’s Cube, a popular puzzle during the late 1970s. The poem, “A Rubric on Rubik’s Cubics,” is set to the tune “Ta-Ra-Ra-Boom-De-Aye.” One verse goes: “Respect your cube and keep it clean./Lube your cube with Vaseline./Beware the dreaded cubist’s thumb,/The callused hand and fingers numb./No borrower nor lender be./Rude folk might switch two tabs on thee,/The most unkindest switch of all,/Into insolubility. [Chorus] In-sol-u-bility./The strangest place to be./However you persist/Solutions don’t exist.”

Shannon himself had a genius for avoiding that “strangest place,” according to Elwyn Berlekamp, who studied under him at MIT and cowrote several papers with him. “There are doable problems that are trivial, and profound problems that are not doable,” Berlekamp explained. Shannon had a “fantastic intuition and ability to formulate profound problems that were doable.”

However, after the late 1950s, Shannon published little on information theory. Some former Bell colleagues suggested that by the time he went to MIT Shannon had “burned out” and tired of the field he had created.

But Shannon denied that claim. He said he continued to work on various problems in information theory through the 1960s, and even published a few papers, though he did not consider most of his investigations then important enough to publish. “Most great mathematicians have done their finest work when they were young,” he observed.

In the 1960s Shannon also stopped attending meetings dedicated to the field he had created. Berlekamp offered one possible explanation. In 1973, he recalled, he persuaded Shannon to give the first annual Shannon lecture at the International Information Theory Symposium, but Shannon almost backed out at the last minute. “I never saw a guy with so much stage fright,” Berlekamp said. “In this crowd, he was viewed as a godlike figure, and I guess he was worried he wouldn’t live up to his reputation.”

Berlekamp said Shannon eventually gave an inspiring speech, which anticipated ideas on the universality of feedback and self-referentiality in nature.

Shannon nevertheless fell out of sight once again. But in recent years, encouraged by his wife, he has begun to drop in on small meetings and to visit various laboratories where his work is carried on.

In 1985 he made an unexpected appearance at the International Information Theory Symposium in Brighton, England. The meeting was proceeding smoothly, if uneventfully, when news raced through the halls and lecture rooms that the snowy-haired man with the shy grin who was wandering in and out of the sessions was none other than Claude Shannon. Some of those at the conference had not even known he was still alive.

At the banquet, the meeting’s organizers somehow persuaded Shannon to address the audience. He spoke for a few minutes and then—fearing that he was boring his audience, he recalled later—pulled three balls out of his pockets and began juggling. The audience cheered and lined up for autographs. Said Robert J. McEliece, a professor of electrical engineering at the California Institute of Technology and chairman of the symposium: “It was as if Newton had showed up at a physics conference.”

A correction to this article was made on 29 April 2016. ''',

                '25': '''This Is Not Capitalism
allen
allen
Follow
Mar 22 · 30 min read



this is your brain on central banking, regulatory capture, and financialization.
Allen Farrington & Sacha Meyers
Image for post
photo by Roberto Júnior, via Unsplash
The everything bubble has popped. In the end it wasn’t PE ratios that imploded under their own stupendous highs, nor the conceptual insanity of negative rates triggering bank runs. The Euro didn’t fall apart (yet) and there was no hyperinflation (yet). It was an “exogenous shock” wot done it. We encourage readers to read this phrase with maximal eye-rolling sass, and to recall when we discuss the kind of macroeconomic macrobullshit that got us into this mess, which works perfectly well in every conceivable circumstance other than contact with the real world.
This puts us in a tragicomic position. In order to deal with this horrifically dangerous “exogeny”, we seemingly need to go into overdrive on the exact same measures that made us vulnerable in the first place: we need to print money like there is no tomorrow and throw it at everything that moves. That is literally the plan. That’s how we deal with emergencies now.
Money printer go BRRR
Print it, baby!
brrr.money
This essay is about the bizarre reaction we have noticed from a solid majority of the professional commentariat to the effect that this is the inevitable result of capitalism run wild. We are not sure what these people mean, or even think they mean, by “capitalism”. If they mean, “the regime of political economy dominant in the West since 1971 and particularly acute since 2009”, then they are correct on a technicality, but they are abusing the word. If “capitalism” means anything, that meaning ought to at least include the notion of preserving and growing capital. It can include other nasty bits and bobs, for sure, but it must at least include this.
The preservation and growth of capital is not happening, nor has it happened since before the dominance of the regime now misleadingly bearing this name. And so, it is somewhat concerning that people are lining up to both defend and attack “capitalism”, when the object of discussion could hardly be further from any worthwhile meaning of the word but is rather better described as: boosting aimless consumption, primarily with uncollateralised debt, by destroying the price signals for capital and depleting its stock. This may well be necessary for the sake of public health — we are not doctors, nor experts in biology, epidemiology, virology, or any similar field, and so we do not deny the merits of such an approach nor offer any views on their likely effectiveness. We just beg for the proper economic analysis of why we are in this position, and do our best to provide it.
This is your brain on central banking, regulatory capture, and financialization. This is not capitalism.
Money Is A Story
Image for post
photo by Josh Appel, via Unsplash
There is a vast literature on the question of ‘what is money?’ We present a simplified version for the purpose of establishing enough key points to keep the discussion moving along. Our account is by no means exhaustively wide nor exhaustively deep, but it is correct enough within the realms of what we cover. Readers looking for a more thorough treatment are encouraged to bookmark Shelling Out by Nick Szabo, Andreas Antonopoulos’s talk The Stories We Tell About Money, or for a longer, more academic read, The Theory of Money and Credit by Ludwig von Mises, and The Ethics of Money Production by Jörg Guido Hülsmann. But for the time being …
Money is a story. It is a story of what work has been done on credit that is yet to be redeemed. It is the Schelling point for universal credit. It is an IOU that everybody is willing to redeem (primarily because everybody is willing to redeem it) and hence that at every instance of its transfer is re-ordained with the ascription of economic value to work actually performed. Note that money is not a social construct, a collective delusion, or any other such denigration that snidely implies that nothing about money really matters and we could reinvent it all tomorrow if we wanted to. Money may be a story, but the qualities of the story matter a great deal. The truer the story, the better.
By ‘true’, we ought to mean that the process of transferring money has, and is trusted to have always had, the characteristics of censorship resistance and integrity assurance. We can think of this in cryptographic terms, as there is a ready analogy to be made to ensuring the security and validity of network communications. Transferring money is sending a message through the network of economic exchange. It is ‘censorship resistant’ if Alice knows her message is to Bob and only Bob; it is not diverted to Charlie, nor is it destroyed. It is ‘integrity assured’ if Bob knows the message is from Alice and only Alice; it is not really from Charlie, nor also to Dorothy, nor really from nobody at all.
When money is printed — whether this be bank notes or lines in a database — this is violating integrity assurance. It is equivalent to the printer extending themselves credit on the unwilling, and mostly unknowing, behalf of everybody. No work has been done that anybody is willing to redeem. No economic value has been created, or contracted to be created, to match the token now in circulation. Bob does not know his message of value transfer is from Alice and only Alice; it is not from anybody. The issuer has executed a man-in-the-middle attack on the structure of economic exchange.
And note this isn’t an old man yells at cloud rant against money creation in general in which we insist all economic activity must be conducted with gold. The money created by credit extension can be perfectly legitimate if the risk of the maturity transformation is priced freely by interest, borne by the equity holders of the lending institution, and mitigated with collateral they understand. But it is not if the risk is priced by political expediency, borne by nobody, and collateralised by everybody. It also doesn’t hurt to have the lenders know and consent to what is happening with their deposits, rather than suffering from the collective delusion that their funds are ‘in the bank’.
We will return below to the implications of taking the latter course of action. For now, bear in mind as we continue that money is universal credit and that its supply in a free market is a reflection of the reality of how much valuable work has been done. As Oliver Wendell Holmes put it,
“We must think things not words, or at least we must constantly translate our words into the facts for which they stand, if we are to keep the real and the true.”
There may be valid social or political reasons to compromise the censorship resistance or integrity assurance of money. Fighting a deadly virus might well be one of them. But there will be consequences; people will believe a story that simply isn’t true, but will act as if it is. We are currently living through the mother of all such consequences.
Stocks And Flows
Image for post
photo by Anders Ipsen, via Unsplash
Another decent definition of money is the most liquid form of capital. Although this is rather a circular definition, as ‘liquidity’ is traditionally conceived of as a measure of how quickly and easily an asset can be converted to ‘money’. It still tautologically works, as money can be converted to money in zero time and with zero difficulty, but it deserves to be padded out. We can say that money is the most salable asset: the asset that emerges with the property of being the most widely accepted in exchange for other assets, not to be consumed, but to retain value for later exchange. Note that, in a barter economy of only consumable goods, money adds little value beyond the administrative: it becomes easier to calculate exchange rates. Where money adds immense social value is in calibrating the exchange rates of goods that cannot be consumed, but rather are used to create consumable goods, or are used to create goods that are used to create consumable goods, and so on.
This all points to a higher analysis; money itself is not the most important aspect of capitalism. Nor is trade, nor markets, nor profits, nor even assets, but capital. ‘goods that are used to create consumable goods’ are a form of capital, but really, we mean something less tangible than any of the former; a kind of economic potential energy stored in the transformation of materials into higher and higher forms of complex good, but always ready to be rereleased to work again the same process of transformation. Seen this way, capital is not any particular thing or even behaviour — it can exist only as an emergent property of a social system in which the exchange of shares of ownership of private assets is seamless.
Capital is a stock. Its dimension is currency. It exists (and in theory could be measured) at any instantaneous point in time. Money and assets are also stocks, meaning they too can be measured at any point in time. But the numbers alone cannot have any independent meaning because they are dependent on the unit chosen to measure the dimension: Dollars. The number will be different in Euros, Yen, or Bitcoin.
Such measures as ‘revenue’, ‘profits’, and with a little leeway even ‘trade’ are flows. Their dimensions are currency over time. There is no such thing as instantaneous profit. Profit happens over time. This means that the numbers representing profit, and all flows, are sensitive to changing the unit measuring the currency, and the unit measuring the time. To avoid confusion on this account, we will assume Dollars per year as a default, but will at various points toy with this concept to make different points clear.
This might seem like semantics, but the distinction is key as follows: you need stocks to create flows, and you need flows to replenish stocks. Our entire analysis of how bankrupt (morally as well as factually) our financial system is can more or less be derived from the appreciation that this simple maxim is not widely understood. What does it mean more practically?
“The economy” is an aggregation of businesses, which are helpfully split into financial and nonfinancial (we hate the expression “the economy” and will endeavour not to use it unless avoiding it would be unbearably clumsy. It is a noun when it should really be a verb, because the way it is used refers to a flow, not a stock). Financial businesses oversee the allocation of liquid capital by matching the preferences of contributors of capital with regards to perceived risk, timeframe, and so on, with nonfinancial business projects with appropriate characteristics. Nonfinancial businesses turn liquid capital into illiquid capital — higher and higher forms of complex good — in an attempt to satisfy a perceived customer demand. If they make revenue, they are correct in a demand existing for such a good or service. If they make a profit, they have satisfied this demand efficiently; they have produced more than they have consumed. Profit is both payment to the providers of capital, and the opportunity to reinvest without requiring further external financing.
Nonfinancial businesses cannot create either revenues or profits without first being provided with capital. This might be as simple as saying that you can’t sell goods without first buying them or making them, and you can’t pay for the raw materials before you have made a profit unless you first have financing. Or it might be more complicated, but also more obviously linked to wealth creation, in that you need to buy a machine (a higher order capital good) that takes raw materials as an input and churns out something more complicated and more valuable. Clearly you don’t want the machine for its own sake; you want it for what it will produce. The machine has to be purchased with liquid capital, and then exists as illiquid capital. It can be liquidated if desired (i.e. sold for cash), but its primary value is as a form of economic potential energy. It is a stock that creates flows.
You need stocks to create flows, and you need flows to replenish stocks. You need financing to start a business, and you need profits to maintain one. Profits are required to pay back the financing, and will eventually give the business owner the ability to eschew financing entirely and maintain the business’s capital requirements sustainably and internally. This is as true for a single business as when aggregated to “the economy”.
The health of a single business, and the health of the aggregation of all businesses, should not be measured by ‘growth’ in revenue, or in profits, or even in capital, but in the ratio of profits to capital. The rate of return. And ideally, it should be (geometrically) averaged over a very long time — not only can no meaningful investment take place over a single year (accruals-based accounting exists in the first place to give at least some useful information over shorter time periods) but the length of credit cycles will obscure what is really happening over as long as ten or twenty years. A high rate of return is a high flow to stock ratio. If all the flow is reinvested, it will be the rate of increase of the stock, and reflect the meaningful growth of “the economy”.
Recall once more the ‘dimensionality’ argument: the ratio of profit one year to profit the year before is not even ‘growth’. It is an ‘increase’. Return on capital is a growth rate. Its units are one over time. Economic wellbeing and sustainability can only be sensibly measured with aggregated return on capital. Unsurprisingly, this is not at all how anybody does so …
‘GDP Growth’, And Other Useless Metrics
Image for post
photo by Fleur, via Unsplash
Widespread misunderstandings of money and capital, and of stocks and flows, come together to form a dangerous cocktail with GDP growth. In understanding how GDP is commonly discussed, and why that discussion betrays a stunning ignorance of money and capital, we will be in a position to evaluate the crisis we now face. This section marks the middle of the essay: the turning point between theory and practical analysis.
As we see it, there are (at least) three problems with ‘GDP growth’, all of which have some bearing on the crisis we now face, and which we will discuss in turn: i) the ‘economic wellbeing’ it claims to measure is in fact unmeasurable, ii) the ‘economic wellbeing’ it claims to measure is politically and socially irrelevant, and iii) it is not a ‘growth rate’ at all.
i) the ‘economic wellbeing’ it claims to measure is in fact unmeasurable: GDP is the total monetary value of goods and services produced in a region over a period. If somebody says “the economy” grew by 2%, they likely mean that the quantity of goods and services produced increased by that amount. Of course, not every quantity grew by exactly that amount. Some might even be shrinking. What matters is the total monetary value. When there is one fewer unit of A, costing $1, but one more unit of B, costing $2, GDP still increases by $1.
So far so good. This certainly seems ‘measurable’, so what’s the problem? Over time, human ingenuity comes up with new or improved goods and services. When that happens, there isn’t merely one more of A or B. There is something else entirely: C. GDP, which so far tracked how much the production of A and B increased, now also tracks C. Given enough time, demand for A, B, and C might disappear, so that GDP only consists of X, Y, and Z — none of which existed when records started. How can we then say that ‘the economy’ grew when it doesn’t make more of what it used to?
The unsatisfactory answer is that when C was invented, it had a market price which could be compared to those of A and B. In that way, the comparison stands. But this exchange rate between A and C only came into existence after C was invented. Beforehand, no amount of money could buy C. Innovation expanded our opportunity set so that capital could be allocated to the production of something new. The price of C only reflects the opportunity cost of its production and consumption after its discovery, not the value embedded in the discovery itself. There are no exchange rates to the future.
The value of discoveries compounds over time. A practical illustration of long-term ‘GDP growth’ makes its nonsensical nature plain. According to GDP, individual Vietnamese on average earn as much today as Americans did in the 1880s. Yet the Vietnamese have the same life expectancy as Americans did in the 1980s. Today’s Vietnamese live in a world of smartphones and penicillin, whereas 1880s Americans lived in an age of candlelight and often-fatal bacterial infections. The monetary value of their income might be considered comparable by economists, but that is because they do not, and cannot, measure the constant improvements brought upon by human ingenuity.
Economies do not ‘grow’, they ‘change’. And you can’t measure counterfactuals in Dollars.
ii) the ‘economic wellbeing’ it claims to measure is politically and socially irrelevant: we encourage readers to look into the blog post Democratic Domestic Product by Ole Peters, and the wider Ergodicity Economics research programme of which he is a part. But we will summarise the salient points here.
GDP growth is the growth in wealth of the average person, rather than the average growth in wealth of a person (the latter is Peters’ proposal for ‘DDP’). GDP growth is a plutocratic measure, that is indifferent to the higher moments of the distribution from which it is drawn. It is entirely possible for the wealth of every single person bar one to go down, while GDP growth goes up. In fact, something not too dissimilar to this seems to have happened in Europe and the US since the financial crisis. GDP keeps on climbing while median measures of income, disposable income, assets, net financial wealth, and more, have gone sideways or even down. The gains have increasingly been concentrated in higher and higher brackets of existing wealth, to the point where, at certain cut-offs, more than 100% of the gains have gone to some upper bracket. In other words, some groups are in fact getting poorer, but other groups are getting richer at a faster rate, such that GDP still grows.
While there is reason to believe that technological changes and geopolitics have contributed to this phenomenon, we will explain below why we think this can largely be explained by state enforcement of the dominant regime of political economy, and its abject ignorance of the principles of money, capital, and returns.
iii) it is not a ‘growth rate’ at all: as above, it is an ‘increase’. It is a difference between two flows. A growth rate is a return; a flow over a stock. Moreover, GDP isn’t even the correct flow one would need to compute a relevant return, because it is the aggregation of revenue, not of profit. By religiously focusing on this entirely irrelevant metric, it is almost trivially easy to end up doing both of the following:
· encouraging profitless revenue, which indicates a real demand, but an inefficient use of resources in satisfying that demand. Capital is one such resource — possibly the most important — hence:
· encouraging destruction or consumption of capital; or, a short-term high of consumption at the expense of the long-term ability to produce what we might like to consume. Think of a farmer eating seed rather than planting it. His consumption increases, but eventually he loses the ability to consume at all.
Equally useless without the proper context is stock market capitalisation. Obviously, it is more or less a good thing for stocks to go up, because it means that lenders of capital are getting a return, and companies that are proving the viability of their economic proposition can raise capital more cheaply. But there must be underlying economic success for this to be justified. Individual companies can always see their valuations grow out of line with their fundamentals, either on hype or entirely on merit as their prospects for the future are seen to be improving. But if valuations across the board are marching upwards vastly out of line with rates of return on capital, never mind with increases in cash flows or book value of equity, something is wrong.
There are two obvious contenders for what might be wrong, and which have the potential to reinforce one another in a deadly spiral: inflation and speculation.
By inflation, we mean to ignore such bullshit euphemisms as ‘quantitative easing’ and ‘market support’ and to direct the reader’s attention to the simple fact of artificial money being pumped into financial markets to increase prices beyond what reality is doing its best to get them to show. When prices go up because a currency is being debased, that is inflation. It might make a social and political difference if the price increases are in milk and bread, or housing and healthcare, rather than in financial assets, but economically it is irrelevant. It reflects only what the artificial money was first used to buy. Eventually it will dissipate to all goods and services. We will return below to the broader consequences of artificial money being directed specifically to financial assets, but for the time being, we simply mean to point out that the prices are fake. They do not reflect reality.
By ‘speculation’ we should be clear that we do not mean anything intrinsically negative. Speculation is usually rolled out by financially illiterate opportunistic rabble-rousers as a culprit for the consequences of intervention-induced market collapses, when in fact it is more than likely that speculation was trying to direct prices to reflect reality while artificial money was pushing in the other direction. We mean simply that financial market inflation can induce a certain kind of speculation that is unhealthy. If it becomes clear enough to market participants that the artificial money firehose will not be turned off, this actually reduces the incentive to speculate against the fake signals being provided by inflation and start contributing to inflation instead. In reviewing an early draft of this essay, Nic Carter kindly drew our attention to the large numbers of so-called ‘permabears’ who flipped long around 2016 when they realised this thing wasn’t going to stop.
Say you are a pension fund that needs an 8% return to meet its liabilities without difficulty. And say that stocks have been inflated to the point that you can in all honesty expect only a 2% return over the long run from here given reasonable assumptions about valuation metrics returning to something sensible at some point. You might be tempted to look for other asset classes that are not so corrupted. But if you are reasonably sure that artificial money will keep pushing prices up for longer than the time horizon over which you would otherwise expect a reversion, then it might actually be sensible to stay invested and get your 8% from inflation alone. This way, those who might otherwise be incentivised to contribute to correcting the effect of price manipulation are actually incentivised to contribute to reinforcing it, if the manipulation is strong enough in the first place.
When this vicious cycle gets into full gear, the idea of measuring ‘economic wellbeing’ solely by the increase (not growth) in stock market valuations, may be even more misguided than by that of GDP ‘growth’. It is not a returns metric. It says nothing about sustainability and in this specific scenario (the one we have been in for at least ten years) it is virtually guaranteed to be concealing highly unsustainable misdirection of capital, if not its outright destruction.
What Would Happen In An Economically Healthy Capitalist Society
Image for post
photo by Brooke Larke, via Unsplash
Lots of things. We will go through some of them relatively quickly as they are more or less common sense and fall out naturally from the above discussion.
· You would be able to preserve wealth in money. Money is the stored and accepted value of work done in the past, redeemable for goods and services in the present or future. Money should not constantly decline in value. There are considerations regarding the conditions of credit extension and systemic leverage that make the issue more complicated and that we do not want to get into — but, all else equal, over a long enough period of time you would expect the purchasing power of money to increase roughly in line with aggregate return on capital, because the same past work done now has access to a greater amount of goods and services.
· This means you would only lend capital to risky enterprises because you want to, not because you have to in order to have any hope of preserving your wealth. This in turn means capital would be priced so as to accurately reflect society’s preferences for saving and consumption, and investment projects would be coordinated accordingly.
· Governments would either run surpluses or it would be acknowledged and accepted that they could institute emergency taxes. Printing money is a stealth tax on wealth that disincentivises holding money, as above. It has the same first-order effect on wealth transfers, but has hidden second-order effects of misdirecting capital due to political expediency and cowardice.
· Relatedly, governments would (or should) therefore be incentivised to act in the public interest at all times. They should not be beholden to stoking financial market inflation at all costs. They should not be ‘bought’ by Wall Street, nor have their banking laws written by bankers and their airline safety regulations written by unsafe airlines. If that means instituting economically disastrous short-term measures for the sake of public health (and to avert even more disastrous long-term economic results) there should be no wavering and no discussion. It should be done, and prices should be allowed to adjust to reflect the new reality without political consequence.
· Investment decisions could legitimately include greater social and environmental considerations without risking fiduciary liability. If you are constantly incentivised to increase short term profits, you will consider firing everybody and moving production to China. If you are incentivised to increase long term returns, you can double down on investment in your existing workforce and stomach the costs of more environmentally friendly inputs to production. The latter is clearly a broader social good, but is still easy enough to motivate and justify given the effects would otherwise be worst felt in the local communities where the workforce is based.
· Individuals and businesses would buy a lot more insurance. Preservation of wealth would be more important than the desperate need to grow it to stay ahead of inflation, and so the prudence of insurance against any and every “exogenous” disaster would be incentivised. Or, rather, it is obviously sensible in the first place, and so it wouldn’t be incentivised against.
· There would be no bailouts. Nothing would be “systemically important” because disasters — even “exogenous” ones — would be adequately insured against. When a business fails, its (willing) contributors of equity would be wiped out, its (willing) contributors of debt would not make whole, and its remaining liabilities would be covered by insurance. Government could even take a far more expansive role in protecting consumers in such cases given, i) it can afford it, and ii) there is no competing incentive to side with business, nor a moral hazard to side with both but encourage recklessness nonetheless.
· Company executives would be incentivised by long-term measures of growth in real value, not short-term measures of increases in per-share value. To be clear, buybacks are, in theory, a valuable tool to price capital properly. We do not argue against them in general, but we acknowledge that, in practice, they are often used as a means to enhance the latter rather than the former. We argue below this behaviour is entirely a pathology of the dominant regime of political economy of which this essay is a critique.
What Has Happened In Real Life
Image for post
photo by Hermes Rivera, via Unsplash
We have spent the past ten years working on the assumption that the supply and price of money is unimportant, that maximising the increase in GDP and stock market valuations is best for “the economy”, that it doesn’t matter that these numbers do not represent rates of return, and that ‘the average person’ is a meaningful concept whose economic wellbeing we can measure. This is your brain on central banking, regulatory capture and financialization. There is far too much to cover so we will stick to what you might have seen in the news lately.
Everybody Gets Levered Up The Wazoo: if you can’t save because money does not retain value, then you have to be fully invested. If capital has all been misallocated such that price signals are unreliable and losses are artificially sustained, then any minor advantage has to be levered to achieve a satisfactory return. And if interest rates are artificially low, this might even seem like it makes good business sense.
If all your competitors are levered to the hilt and you aren’t, even though you can optically afford it, you will be outcompeted. So you have to do it too. You can’t compete prudently in the long run if your competitors spend you to death on cheap capital in the short run. Even if there are no competitive pressures, there will be pressures from shareholders. As with speculation and buybacks above, there are perfectly sensible ways for businesses to use leverage to beneficially affect capital allocation, for themselves and for the market at large. But usually, this is because the company has visibility on likely variations in cashflows and slack to absorb shocks — not despite having no visibility and no slack.
There are forms of leverage other than debt. You can think of leverage more abstractly as an induced vulnerability to shocks — “exogenous” or otherwise — in exchange for a magnified gain in their absence. The more debt you have, the more vulnerable you are to shocks to cash flow, because you have no choice but to pay the interest. But in many ways, other vulnerabilities to shocks can be even more dangerous. At least debt is relatively transparent: you can infer from the financial statements how much of a shock you can afford. Other vulnerabilities are less inherently knowable. Supply chain decisions can be a form of leverage: to get the absolute lowest costs that can be sweated out your setup, you could choose a single supplier (say, in China) and instruct them to deliver right on time to drive your carried inventory to effectively zero.

Of course, this means that any shock to this setup whatsoever will break it entirely. There is no slack. It is exceedingly fragile. Which is more or less what we are seeing now, as Preston Byrne points out above. Not only are entire sectors grinding to a halt because they are operationally levered to the eyeballs towards one specific task and cannot adjust to even mildly different circumstances, never mind a quarantine, but this setup is precisely why we are in these circumstances in the first place. If we could have cut all contact with China in January there would be no crisis whatsoever. For some (cough cough US and UK) this would have been meant a reduction in imported tat. For others (cough cough Italy and Iran) this would rather more seriously have meant risking forfeiting strategic assets financed with Chinese debt under the Belt and Road Initiative. And so, obviously, tragically, the borders stayed wide open:

Swap out ‘freedom and democracy’ for ‘public health’ and you get the idea.
Declining to hold a cash balance is a form of leverage by omission. As is declining to purchase insurance it would really be prudent to hold. If the need to be levered gets desperate enough, many will even consider selling insurance as a way to top up returns, clearly indifferent to the long-term implications of this insanity, because the short-term pressures are too intense to care. The behavioural pull here should not be underestimated. If absolutely everybody is selling insurance, you might want to consider buying some, and yet this takes a special resolve.
Universa Investments exists more or less exclusively to run this trade. Do you think you could mimic them? Really? You are willing to lose a little bit more every day for ten years, waiting for the everything bubble to maybe, one day, pop? Or will you cave after 2 or 3? Will you get up and dance to the song that never ends? We haven’t seen any numbers but we imagine the past two months have been quite spectacular for Universa. Rumour has it 1,000% in February and 3,000% and counting in March. Not to detract from their genuinely brilliant analysis and essential work for their clients, but we can’t help but feel it is somewhat sad that, bet against absolutely everybody’s desperation, ignorance, and stupidity, is a viable strategy for a hedge fund. That said, it may be sad, but it is true, and we should not downplay or envy the valuable public service of those who pursue such a strategy successfully.
The Cantillon Effect Is Justified As A Public Good: The Cantillon Effect refers to the phenomenon that debased money is not distributed equally throughout society all at once, but is introduced in a specific place, giving its initial holders illegitimate purchasing power at everybody else’s expense. By the time the inflation washes through “the economy”, those who receive the artificial money last have had reduced purchasing power for as long as it takes them to at best catch up with everybody else. Also, as this is done sneakily, the new money isn’t priced in properly either, giving the Cantillon insiders an additional advantage. This is all rather amusing when you consider the likely hyperbolic response of financial elites and economists to the idea of ‘helicopter money’. For all its flaws, helicopter money is a substantially better and fairer idea than quantitative easing.
As per the dominant regime of political economy, the artificial money is introduced to the financial sector by means of ‘open market operations’ in which central banks add assets to their balance sheets in order either to boost the prices of financial assets, lower the borrowing costs of corporations, or both at once. This is justified because ‘growing GDP’ and ‘supporting the stock market’ are thought to be legitimate political goals — price signals, capital allocation, and rates of return be damned.
This means that everybody whose income derives from the face value of financial instruments benefits at everybody else’s expense. There is a decent argument to be made that, actually, the pensions of at least every past and present government employee are entirely dependent on these valuations, which justifies the social and political goal in the first place. But this obscures a crucial point: there is an extremely important difference between benefitting from increases in valuation because your wealth is tied up in those assets, and because your income derives from periodically skimming the value of those assets. Those in the latter position are actually in charge of all of this financialised, regulatorily-captured mess, and yet when challenged will wax lyrical about the savings of all those hard-working men and women in the former camp, pulling on your heartstrings until they snap.
Those in the latter camp tend to be exceedingly well-off already: bankers, market makers, hedge funds, mutual fund managers; the derivative professional services of each of the above: lawyers, accountants, corporate managers; corporate executives incentivised by options, hence in turn incentivised to buy back stock — not because the stock is undervalued and capital pricing in aggregate will benefit from this decision, but because valuation is not considered at all, and the intention is to temporarily boost the stock price in time for the options to mature and be cashed in. Each of the above makes out like bandits while little old retired schoolteacher grandmas are left holding the bag when markets inevitably collapse and their pensions evaporate.
And of course, when that happens, who can we expect to go on CNBC and beg Congress for bailouts but precisely the corporate executives, bankers, and the like, whose maintaining of this regime of political economy caused it all in the first place. In dire enough straits, some executive teams will have even have the stone cold cojones to buy back $3bn of stock with more or less the entirety of their company’s free cash flow, take combined options packages worth over $10m marked-to-market in one fiscal year, no doubt boosted higher in time for payday by all these buybacks, and then hold their employees’ jobs hostage in their negotiations for government bailouts:

These people’s wealth is determined almost exclusively by how high they can push flows — stocks and rates of return be damned. Everybody else is left with low or negative real returns and depleted stocks of capital and wealth. This is why GDP growth can be positive while almost everybody feels poorer. Almost everybody is poorer. Objectively so. Their savings have been stealthily taxed and handed to the already rich, while their everyday costs have gone up to reflect the dissipation of this inflation. Democratic Domestic Product growth (or lack thereof) would capture this, but nobody cares about DDP. GDP all the way, baby! Look at that S&P go!
Hey, wait, what happened? …
Financialization
Image for post
from The New Yorker
In a world with only apples and oranges, bananas are new. But so are securities backed by mortgages on the properties of apple and orange farmers. Leading up to the last financial crisis, banks selling MBSs were contributing to GDP growth. They were incentivised to do so because their income came from skimming flows rather than growing stocks, and were allowed to flagrantly lie about the risks of doing so by captured regulators. Of course, the products themselves were largely highly toxic — not only did they not create any real wealth, they encouraged the staking of real wealth against synthetic versions of the same underlying toxic assets. Capital was depleted, but only in the very long run, long after the banks had taken their cut and passed on the hot potato (well, most banks).
But that cut was growth! GDP went up! Bank stocks went up! Bonuses went up! Everything went up until suddenly it went down to lower than where it started. This might seem hopelessly irrational, and in one sense it is. But that is not the sense in which anybody is incentivised to behave in a world in which returns must chase inflation, insurance must be sold rather than bought, and you know full well you will be bailed out if (or when) you blow up. And not this is not just banks: United Airlines is in an arguably conceptually identical position. It financialised its balance sheet (woo hoo growth!) for little reason other than to enrich its executives, blew up (but but but exogenous!), and now wants a bailout.
Nor is it all banks. It is perfectly possible to run a bank responsibly amidst such insanity. It just takes ethics and guts. Legendary BB&T CEO John Allison wrote an entire book about how flagrantly unethical banking and regulatory practices caused the previous crisis while he ran his bank well, including being subject to a Treasury shakedown to take TARP funds it didn’t need in order to help the likes of Citigroup and Merrill Lynch look less like dangerous lunatics. Readers might see the unfortunately suggestive title of this book and think Allison is solely proposing greater privatisation of gains. It is far more accurate to say he is proposing less socialisation of losses. Amen to that.
Ever eager to prevent the last crisis (or to be seen to have retroactively and heroically prevented the last crisis) much of the pre-GFC financialization has since been made illegal. And yet financialization continues apace. Imagine what grifting, off-balance sheet, 2010s shenanigans are on the cusp of seeing the light of day!
Image for post
Source: US Bureau of Economic Analysis
Consider the chart above of finance as a proportion of US GDP. Something is wrong here. Finance certainly ought to grow: if done properly it contributes enormously to societal wellbeing by allocating capital efficiently. This is all well and good. But it should not grow faster than everything else, because it typically charges a percentage fee of the face value of the assets or securities that pass through its allocating hands. For finance to consistently grow as a proportion of GDP, either it is simply upping its take — which might be reasonable within bounds, but raises questions of adequate competition in the sector and of possible regulatory capture — or it is making more and more MBS-like time bombs. It is spinning off flows of toxic financial exposure, of whose values it is taking a cut but not a stake, that don’t actually contribute to real economic returns, and hence to the aggregate growth in the stock of capital.
Once again, it isn’t just banks. In recent years this attitude seems to have firmly entrenched itself in just about every industry. Credit card income represents 40% of Macy’s profit. Patreon is now basically a payday lender. These aren’t extraordinary cases. They are exactly what you would expect when interest rates are artificially low for long enough: any business with enough customers and enough data on their customers’ purchasing behaviour can very likely borrow at low (fake) rates and effectively lend to customers at higher ones.
Image for post
You had a little typo there, Apple, but we fixed it for you
This arbitrage can even give them the leeway to make a loss on their actual good or service, furthering the widespread misallocation of capital away from things that can be sustainably profitable and towards facilitating indebted consumption of garbage:

The obsession with GDP growth that fuels financialization also leads us to forget that inventing new things to produce tomorrow is as important, if not more so, than increasing what is produced today. So-called capitalists in such a regime can resemble the Soviet Union apparatchiks (hardy flattering, we admit) who focused exclusively on increasing output at the expense of managing the inputs or improving the quality of anything produced. Since the value of genuine innovation can’t be measured, it tends to be discarded in a world focused exclusively on forever increasing such meaningless statistics as GDP and stock market capitalisations with no understanding of why these numbers ought to go up. In many ways it is like a cargo cult: when good things happen, stocks go up — so stocks going up must be a good thing! Official government policy from now on is for stocks to go up.
Image for post
Official government policy in meme form
The effect of all this is that we make more of A, B, and C, and then move on to securitisations of A, B, and C, and synthetic securitisations of A, B, and C, and so on, until it all collapses. We never get to see X, Y, or Z. We never even think about what they might have been.
Conclusion
The dominant regime of political economy in the West since 1971, and particularly acute since 2009, has been built on a set of related economic fallacies: that there are no adverse consequences to manipulating the price and supply of money; that economic wellbeing can be measured by increases in flows of revenue rather than the growth rate of profit over capital; that such measures as GDP growth and stock market capitalisation ought to be maximised at all costs; and that the growth rate of the average matters, but not the average growth rate.
Had we built a capitalistic society on the principles of sound money and long-term returns, a great many institutions and incentives would likely be radically different to what we see today. The structure of economic production would be far more robust to shocks, far more inclusive in its creation and distribution of wealth, and far less corrupting in its rewarding of political cronyism.
That we have not has led to dire consequences that the coronavirus outbreak has exposed and exacerbated, but which existed nonetheless and, given enough time, would have found another way to explode. The factors we falsely deem to cause economic wellbeing are in fact fine-tuned to accelerate our inevitable descent into ever greater fragility, inequality, extraction, and financialization, and, ultimately, to the total depletion of capital.
This is your brain on central banking, regulatory capture, and financialization. This is not capitalism. ''',

                '26': '''Goals vs. Systems
Posted November 18, 2013 in: #General Nonsense

In my new book, How to Fail at Almost Everything and Still Win Big: Kind of the Story of My Life, I talk about using systems instead of goals. For example, losing ten pounds is a goal (that most people can’t maintain), whereas learning to eat right is a system that substitutes knowledge for willpower.

Expanding on that point, let’s say you have a choice between pasta and a white potato. Assume you enjoy both foods equally and you want to choose the best one for your waistline. Which do you pick?

I recently posed that question to a crowd of ninety senior managers at a huge tech company. About 88 of them chose the potato. That’s the wrong answer because pasta is only half as high on the glycemic index. The two people out of ninety who knew pasta was the better choice wouldn’t need to use as much willpower later in the day to stay within a good diet range. Studies have shown that if you use your willpower resisting one temptation you have less in reserve for the next. The systems approach to weight management is to gradually replace willpower with knowledge, e.g. knowing pasta is better than a potato. (The book describes more ways to replace willpower with knowledge in the diet realm.)

Here’s another example. Going to the gym 3-4 times a week is a goal. And it can be a hard one to accomplish for people who don’t enjoy exercise. Exercising 3-4 times a week can feel like punishment – especially if you overdo it because you’re impatient to get results.  When you associate discomfort with exercise you inadvertently train yourself to stop doing it. Eventually you will find yourself “too busy” to keep up your 3-4 days of exercise. The real reason will be because it just hurts and you don’t want to do it anymore. And if you do manage to stay with your goal, you use up your limited supply of willpower.

Compare the goal of exercising 3-4 times a week with a system of being active every day at a level that feels good, while continuously learning about the best methods of exercise. Before long your body will be trained, like Pavlov’s dogs, to crave the psychological lift you get from being active every day. It will soon become easier to exercise than to skip it – no willpower required. And your natural inclination for challenge and variety will gently nudge you toward higher levels of daily activity while at the same time you are learning in your spare time how to exercise in the most effective way. That’s a system.

By the way, it is only in the past few years that you could replace willpower with knowledge about diet and exercise and get a good result. That’s because much of what science told us in those realms was wrong. When I was a kid, science told us to eat plenty of Wonder Bread. I think we have finally crossed the tipping point where following the recommendations of science will get you a good result.

One of the systems I use but didn’t mention in the book is what I’m doing right now: blogging.

When I first started blogging, my future wife often asked about what my goal was. The blogging seemed to double my workload while promising a 5% higher income that didn’t make any real difference in my life. It seemed a silly use of time. I tried explaining that blogging was a system, not a goal. But I never did a good job of it. I’ll try again here.

Writing is a skill that requires practice. So the first part of my system involves practicing on a regular basis. I didn’t know what I was practicing for, exactly, and that’s what makes it a system and not a goal. I was moving from a place with low odds (being an out-of-practice writer) to a place of good odds (a well-practiced writer with higher visibility).

The second part of my blogging system is a sort of R&D for writing. I write on a variety of topics and see which ones get the best response. I also write in different “voices”. I have my humorously self-deprecating voice, my angry voice, my thoughtful voice, my analytical voice, my half-crazy voice, my offensive voice, and so on. You readers do a good job of telling me what works and what doesn’t.

When the Wall Street Journal took notice of my blog posts, they asked me to write some guest features. Thanks to all of my writing practice here, and my knowledge of which topics got the best response, the guest articles were highly popular. Those articles weren’t big money-makers either, but it all fit within my system of public practice.

My writing for the Wall Street Journal, along with my public practice on this blog, attracted the attention of book publishers, and that attention turned into a book deal. And the book deal generated speaking requests that are embarrassingly lucrative. So the payday for blogging eventually arrived, but I didn’t know in advance what path it would take. My blogging has kicked up dozens of business opportunities over the past years, so it could have taken any direction.

My problem with goals is that they are limiting. Granted, if you focus on one particular goal, your odds of achieving it are better than if you have no goal. But you also miss out on opportunities that might have been far better than your goal. Systems, however, simply move you from a game with low odds to a game with better odds. With a system you are less likely to miss one opportunity because you were too focused on another. With a system, you are always scanning for any opportunity.

There are obviously some special cases in which goals are useful. If you plan to become a doctor, for example, and you have the natural ability, then by all means focus. But for most of us, we have no idea where we’ll be in five years, what opportunities will arise, or what we’ll want or need by then. So our best bet is to move from a place of low odds to a place of better odds. That means living someplace that has opportunities, paying attention to your health, continuously upgrading your skills, networking, and perhaps dabbling in lots of different areas.

The systems vs. goals idea is only one through-thread of my new book, but readers and reviewers are consistently mentioning it as the thing they found most useful, saying it is both fresh and obvious at the same time. That’s a rare combination.

I’m curious if any of you have systems you’d like to share? ''',

                '27': '''Who Is Cato? Roman Senator. Mortal Enemy of Julius Caesar.

For George Washington and the entire revolutionary generation, Cato was Liberty—the last man standing when Rome’s Republic fell. For centuries of philosophers and theologians, Cato was the Good Suicide—the most principled, most persuasive exception to the rule against self-slaughter. For Julius Caesar, the dictator who famously pardoned every opponent, Cato was the only man he could never forgive.

George Washington and his peers studied Cato’s life in the form of the most popular play of that era: Cato: A Tragedy in Five Acts, by Joseph Addison. The great men of the day quoted this play about Cato in public statements and in private correspondence. When Benjamin Franklin opened his private diary, he was greeted with lines from the play that he had chosen as a motto. John and Abigail Adams quoted Cato to one another in their love letters. When Patrick Henry dared King George to give him liberty or death, he was cribbing from Cato. When Nathan Hale regretted that he had only one life to give for his country—seconds before the British army hanged him for high treason—he was poaching words straight from Cato.

George Washington, John Adams, and Samuel Adams were all honored in their time as “the American Cato”—and in revolutionary America, there was little higher praise. And when Washington wrote to a pre-turncoat Benedict Arnold that “it is not in the power of any man to command success; but you have done more—you have deserved it,” he, too, lifted the words from Addison’s Cato.

Through two millennia, Cato was mimicked, studied, despised, feared, revered. In his own day, he was a soldier and an aristocrat, a senator and a Stoic. The last in a family line of prominent statesmen, Cato spent a lifetime in the public eye as the standard-bearer of Rome’s optimates, traditionalists who saw themselves as the defenders of Rome’s ancient constitution, the preservers of the centuries-old system of government that propelled Rome’s growth from muddy city to mighty empire.

Cato made a career out of purity, out of his refusal to give an inch in the face of pressure to compromise and deal. His was a powerful and lasting political type: the man who achieves and wields power by disdaining power, the politician above politics. It was an approach designed to elicit one of two things from his enemies: either total surrender or (in Cato’s eyes) a kind of moral capitulation. This strategy of all-or-nothing ended in crushing defeat. No one did more than Cato to rage against his Republic’s fall. Yet few did more, in the last accounting, to bring that fall to pass.

History remembers Cato as Julius Caesar’s most formidable, infuriating enemy—at times the leader of the opposition, at times an opposition party unto himself, but always Caesar’s equal in eloquence, in conviction, and in force of character, a man equally capable of a full-volume dawn-to-dusk speech before Rome’s Senate and of a 30-day trek through North Africa’s sands, on foot.

Cato’s name has faded in our time in a way that Caesar’s has not. Perhaps that is the cost of his political defeat; perhaps his virtues are out of style. More likely, he is forgotten because he left behind very little that was concrete. He reached the heights of Roman politics, but he didn’t pen epics celebrating his own accomplishments, as Cicero did. He was a brave, self-sacrificing, successful military commander, but he didn’t send home gripping third-person histories of his exploits, as Caesar did. His name was proverbial in his own time, but he didn’t engrave that name on monuments. He studied and practiced philosophy with focused intensity, turning himself into the model of the unflinching Stoic ideal, but he preferred that his philosophy be lived, not written. In fact, the only writing of Cato’s that survives is a single, short letter.

Cato was certainly a self-promoter, but the only form of promotion he valued was example, the conspicuous conduct of his life—righteous in his friends’ eyes, self-righteous in his enemies’. Cato’s Rome teemed with imported wealth; Cato chose to wear the simple, outmoded clothing of Rome’s mythical founders and to go barefoot in sun and cold. Powerful men gifted themselves villas and vineyards; Cato preferred a life of monkish frugality. Roman politics was well-oiled with bribes, strategic marriages, and under-the-table favors; Cato’s vote famously had no price. These gestures were all, in their own way, a deliberate message to his fellow citizens, a warning that they had gone fatally soft. It is the kind of message that is remembered, but rarely heeded.

NOTABLE WORKS & SUGGESTED READINGS
Cato did not pen an autobiography, nor leave behind an extensive set of essays or journals. While Cato the Younger was an evergreen subject for a wide range of historians, biographers, and moralists in the Roman world, the most detailed classical treatment of his life comes from Plutarch. Plutarch was a Greek biographer, magistrate, and priest of Apollo, who took the Roman name Lucius Mestrius Plutarchus. He flourished during the reign of the Emperor Trajan and is best known today for his Parallel Lives of eminent Greeks and Romans, a collection that includes his life of Cato.

There is good reason to believe that Plutarch’s biography is founded on eyewitness accounts of Cato’s life. Joseph Michael Conant (The Younger Cato: A Critical Life with Special Reference to Plutarch’s Biography) makes a strong case that Plutarch worked largely from two sources, now lost. One of these was likely Cicero’s Cato, which dealt with some of the most important events in Cato’s political life, from the perspective of man who saw many of them first-hand. The other was a life of Cato by Thrasea Paetus, the Stoic senator condemned by Nero; this work, in turn, was based on the memoirs of Munatius Rufus, Cato’s Stoic companion. The two most important sources for Plutarch’s biography, then, appear to have been written by men who knew Cato intimately: a political ally and a close personal friend. Because Plutarch’s life seems to originate in first-hand accounts, and because it contains such a wealth of detail, it is fair to agree with the classicist Robert J. Goar’s judgment: Plutarch “brings us as close to the historical Cato as it is possible for us to come.”

For more than 2,000 years, there was no full-length biography of Cato outside of Plutarch’s work. In 2011, Jimmy Soni and Rob Goodman endeavored to write one. The result, Rome’s Last Citizen: The Life and Legacy of Cato, Mortal Enemy of Cesar, is the best volume, to date, that covers the end-to-end life of Cato.

They were inspired by numerous book in which Cato is a central figure, including Rubicon by Tom Holland. If you have even a passing interest in the history of Rome—or you think you might—pick up Rubicon. It is gripping and thoughtful; you’ll never for a minute believe that you’re reading ancient history.

3 Stoic exercises from Cato
1) Use pain as a teacher

Cato walked around ancient Rome in unusual clothing—with a goal of getting people to laugh at him. He learned to eat a poor man’s bread and live without luxuries—even though he was a Roman aristocrat. He would walk bareheaded in the rain, shoe-less in the cold.

Cato was training himself. Small difficulties, endured with forbearance and patience, could shape his character. All of Cato’s practice paid off. Seneca, the great imperial Stoic, relates a telling story. Visiting the public baths one day, Cato was shoved and struck. Once the fight was broken up, he simply refused to accept an apology from the offender: “I don’t even remember being hit.”

2) Embrace high standards

The Stoics taught Cato that there were no shades of gray. There was no more-or-less good, no more-or-less bad. Whether you were a foot underwater or a fathom, you were still drowning. All virtues were one and the same virtue, all vices the same vice.

It is the kind of austere scheme that seems unreasonable to live by and almost entirely impossible for the flux of war and politics. But Cato made it work. He refused political compromise in every form, to the point that bribe-takers turned his name into an aphorism: “What do you expect of us? We can’t all be Catos.”

He demanded the same of his friends, his family, and his soldiers. He was infuriating to his enemies, and he could seem crazy to his allies. And yes, sometimes he took his adherence to principle down absurd, blind alleys. But he also built an impossible, almost inhuman standard that brought him unshakable authority. By default, he became Rome’s arbiter of right and wrong. When Cato spoke, people sat up straighter. When he was carted off to jail by Julius Caesar, the entire Senate joined him in sympathy, forcing Caesar to let Cato go.

Many in Cato’s day spent their fortunes and slaughtered armies in pursuit of that kind of authority. But it can’t be bought or fought for—it’s the charisma of character. His countrymen couldn’t all be Catos, but they could join whichever uncompromising side of the argument Cato was on.

3) Put fear in its proper place

On election day during a consequential race, Cato and his brother-in-law were ambushed while walking to the polls. The torchbearer at the head of Cato’s party collapsed with a groan—stabbed to death. They were surrounded by shadows swinging swords. The assailants wounded each member of the party until all had fled but Cato and his brother-in-law. They held their ground, Cato gripping a wound that poured blood from his arm.

For Cato, the ambush was a reminder that if the front-runners were willing to perpetrate such crimes on the way to power, then one could only imagine what they would do once they arrived. It was all the more important that he stand in front of the Roman people, show off his wounds, and announce that he would stand for liberty as long as he had life in him. But his brother-in-law didn’t have the stomach for it. He apologized, left, and barricaded himself inside his home.

Cato, meanwhile, walked unguarded and alone to the polls.

Fear can only enter the mind with our consent, Cato had been taught. Choose not to be afraid, and fear simply vanishes. To the untrained observer, Cato’s physical courage was reckless. But in fact, it was among the most practiced aspects of Cato’s self-presentation. And it was this long meditation on the absurdity of fear—on its near-total insignificance but for our own belief in it—that enabled him to press forward where others gave in.

Cato Quotes
Bitter are the roots of study, but how sweet their fruit. – Cato

 

A honest man is seldom a vagrant. – Cato

 

Consider in silence whatever any one says: speech both conceals and reveals the inner soul of man. – Cato

Flee sloth; for the indolence of the soul is the decay of the body. – Cato

I will begin to speak, when I have that to say which had not better be unsaid. – Cato

In doing nothing men learn to do evil. – Cato ''',

                '28': '''The Complex Markets Hypothesis
allen
allen
Follow
Feb 15 · 56 min read



in which I hypothesise that markets are subjective, uncertain, complex, stochastic, adaptive, fractal, reflexive … — really any clever sounding adjective you like — just not efficient.
(available as pdf here, if desired)
Image for post
photo by skeeze, via Pixabay
Around a month ago, Nic Carter asked me to have a look at a final draft of his article on the basics of the Efficient Markets Hypothesis. Dancing around the edges of Bitcoin Twitter as I am prone to do, I immediately grasped both the need for and the point of such an article; the question of whether the upcoming ‘halving’ is ‘priced in’ or not had “become a source of great rancor and debate,” as Nic wrote. For the uninitiated, ‘the halving’ is the reduction of the Bitcoin block reward from 12.5 bitcoin to 6.25, expected around May 2020. Nic set himself the task of explaining the EMH more or less from scratch, in such a way that the explanation would naturally lend itself towards insight on questions of Bitcoin’s market behaviour.
An Introduction to the Efficient Market Hypothesis for Bitcoiners
What the EMH does and does not say
medium.com
I think he did a great job and the article is well worth reading. But I couldn’t help thinking as I went through it that, basically, I didn’t believe this stuff the first time around, and it all seemed strangely incongruous in a setting explicitly involving Bitcoin, what with the tendency of serious thinkers in this space to treat highly mathematised mainstream / neoclassical financial economics with something between suspicion and disdain.
To be completely clear, this is in no way a ‘rebuttal’ to Nic. He articulated the EMH very well, but didn’t defend it. That wasn’t the point of his article at all. He watered down the presentation at several points by saying (quite helpful) things like:
“I do not believe in the ‘strong form’ of the EMH. No finance professional I know does. It is generally a straw man,”
and,
“Interestingly, by caveating the EMH, we have stumbled on an alternative conception entirely. The model I have described here somewhat resembles Andrew Lo’s adaptive market hypothesis. Indeed, while I am very happy to maintain that most (liquid) markets are efficient, most of the time, the adaptive market model far more closely captures my views on the markets than any of the generic EMH formulations.”
One passage in particular stuck out to me:
“Referring to it as a model makes it very clear that it’s just an abstraction of the world, a description of the way markets should (and generally do) work, but by no means an iron law. It’s just a useful way to think about markets.”
This is where I’m not so sure. Yes, it’s an abstraction, and no, it’s not an iron law. But I don’t think it’s a terribly good abstraction, and I think the reason is that it subtly contradicts and elides what are, in fact, iron laws, or as close to iron laws as can be found in economics. It’s a useful way to think about markets, to a point, but I want to explore what I think is a more useful way.
My argument will go through the following propositions, which serve as headings for their own sub-sections of discussion: value is subjective; uncertainty is not risk; economic complexity resists equilibria; markets aggregate prices, not information; and, markets tend to leverage efficiency.
I will conclude with some additional commentary on Andrew Lo’s Adaptive Markets Hypothesis and Benoit Mandelbrot’s interpretation of fractal geometry in financial markets, simply because, of all the reading around this topic that was thrown up by Nic’s article, these two were by far the most intriguing. I didn’t want to do either an injustice by bending their arguments too far to make them fit my own, but I think that they can be very fruitfully analysed with the conceptual tools we will have developed by the conclusion of the essay. I will also occasionally invoke the concepts of ‘reflexivity’, as articulated by George Soros in The Alchemy of Finance, and several concepts popularised and articulated by Nassim Taleb, such as ‘skin in the game’, ‘black swans’, and ‘robustness’.
This might seem like an excessive coverage list just to offer a counter to the claim that markets are ‘efficient’ — which seems pretty reasonable in and of itself. If it is at all reassuring to the reader before diving in, I don’t think my thesis has five intimidating-sounding propositions, so much as one quite simple idea, from which many related propositions can be shown to follow. I think that, fundamentally, the efficient markets hypothesis is contradicted by the implications of value being subjective, and that some basic elements of complex systems are helpful, in places, to nudge the reasoning along. This essay is an attempt to tease these implications out.
Value is Subjective
You shouldn’t compare apples and oranges, except that sometimes you have to, like when you are hungry. If apples and oranges are the same price, you need to make a decision that simply cannot be mathematised. You either like apples more than oranges, or vice versa. And actually, even this may not be true. Maybe you know full well you like oranges, but you just feel like an apple today, or you need apples for a pie recipe for which oranges would be très gauche. This reasoning is readily extended in all directions; which is objectively better, a novel by Dickens or Austen? A hardback or an ebook by either, or anybody? And what about the higher order capital goods that go into producing apples, oranges, novels, Kindles, and the like? Clearly they are ‘worth’ only whatever their buyer subjectively assesses as likely to be a worthwhile investment given the (again) subjective valuations of others as to the worth of apples, oranges, novels, and whatnot …
This is all fine and dandy; readily understood since the marginal revolution of Menger, Jevons, and Walras in the 1870s rigorously refuted cost and labour theories of value. As Menger put it in his magisterial Principles of Economics,
“Value is thus nothing inherent in goods, no property of them, nor an independent thing existing by itself. It is a judgment economizing men make about the importance of the goods at their disposal for the maintenance of their lives and well-being. Hence value does not exist outside the consciousness of men.”
Fair enough. But the first seductive trappings of the EMH come from the rarely articulated assumption that such essential subjectivity is erased in financial markets because the goods in the market are defined only in terms of cash flows. There may not be a scientific answer as to whether apples are better than oranges, but surely $10 is better than $5? And surely $10 now is better than $10 in the future? But what about $5 now or $10 in the future?
There are (at least) two reasons this reductionism is misleading. The first comes from the mainstream neoclassical treatment of temporal discounting, which is to assume that only exponential discounting can possibly be “optimal”. The widespread prevalence of alternative approaches — hyperbolic discounting, for example — is then usually treated via behavioural economics, as a deviation from optimality that is evidence of irrational cognitive biases.
This has been challenged by a recently published preprint paper by Alex Adamou, Yonatan Berman, Diomides Mavroyiannis, and Ole Peters, entitled The Microfoundations of Discounting (arXiv link here) arguing that the single assumption of an individual aiming to optimise the growth rate of her wealth can generate different discounting regimes that are optimal relative to the conditions by which her wealth grows in the first place. This in turn rests on the relationship between her current wealth and the payments that may be received. Sometimes the discounting that pops out is exponential, sometimes hyperbolic, sometimes something else entirely. It depends on her circumstances.
I would editorialise here that an underlying cause of confusion is that people value time itself, and, naturally, do so subjectively. It may be fair enough to say that they typically want to use their time as efficiently as possible — or grow their wealth the fastest — but this is rather vacuous in isolation. Padding it out with circumstantial information immediately runs into the fact that everybody’s circumstances are different. As Adamou said on Twitter shortly after the paper’s first release, not many 90-year olds play the stock market. It’s funny because it’s true.
And it is easy to see how this result can be used as a wedge to pry open a conceptual can of worms. In financial markets, there are far more variables to compare than just the discount rate — and if we can’t even assess an objective discount rate, we really are in trouble! In choosing between financial assets we are choosing between non-deterministic streams of future cash flows, as well as (maybe — who knows?) desiring to preserve some initial capital value.
Assume these cash flows are ‘risky’, in the sense that we can assign probabilities to their space of outcomes. In the following section, we will see that really the cash flows are not ‘risky’, but ‘uncertain’, which makes this problem even worse — but we can stick with ‘risky’ for now as it works well enough to make the point. There can be no objective answer because different market participants could easily have different risk preferences, exposure preferences, liquidity needs, timeframes, and so on.
Timeframes are worth dwelling on for a second longer (there’s ‘time’ again) because this points to an ill-definition in my hasty setup of the problem: to what space of outcomes are we assigning probabilities, exactly? Financial markets do not have an end-point, so this makes no sense on the face of it. If we amend it by suggesting (obviously ludicrously) that the probabilities are well-defined for every interval’s end-point, forever, then we invite the obvious criticism that different participants may care about different sequences of intervals. Particularly if their different discount rates (which we admitted they must have) have a different effect on how far in the future cash flows have to come to be discounted back to a value that is negligible in the present. Once again, people value time itself subjectively.
In the readily understood language employed just above, market participants almost certainly have different circumstances to one another, from which different subjective valuations will naturally emerge. What seems to you like a stupidly low price at which to sell an asset might be ideal for the seller because they are facing a margin call elsewhere in their portfolio (see Nic’s cited example of what blew up LTCM despite it being a ‘rational bet’), or because they hold too much of this asset for their liking and want to rebalance their exposure. Or perhaps some price might seem stupidly high to buy, but the buyer has a funding gap so large that they need to invest in something that has a non-zero probability of appreciating by that much. If you need to double your money, then the ‘risk-free asset’ is infinitely risky. There is no right answer, because value is subjective.
Uncertainty is not Risk
‘Risk’ characterises a nondeterministic system for which the space of possible outcomes can be assigned probabilities. Expected values are meaningful and hence prices, if they exist in such a system, lend themselves to effective hedging. ‘Uncertainty’ characterises a nondeterministic system for which probabilities cannot be assigned to the space of outcomes. Uncertain outcomes cannot be hedged. This distinction in economics is usually credited to Frank Knight and his wonderful 1921 book, Risk, Uncertainty, and Profit. In the introduction, Knight writes,
“It will appear that a measurable uncertainty, or “risk” proper, as we shall use the term, is so far different from an unmeasurable one that it is not in effect an uncertainty at all. We shall accordingly restrict the term “uncertainty” to cases of the non-quantitive type. It is this “true” uncertainty, and not risk, as has been argued, which forms the basis of a valid theory of profit and accounts for the divergence between actual and theoretical competition.”
Keynes is often also credited an excellent exposition,
“By “uncertain” knowledge, let me explain, I do not mean merely to distinguish what is known for certain from what is only probable. The game of roulette is not subject, in this sense, to uncertainty… Or, again, the expectation of life is only slightly uncertain. Even the weather is only moderately uncertain. The sense in which I am using the term is that in which the prospect of a European war is uncertain, or the price of copper and the rate of interest twenty years hence, or the obsolescence of a new invention, or the position of private wealth owners in the social system in 1970. About these matters there is no scientific basis on which to form any calculable probability whatever. We simply do not know. Nevertheless, the necessity for action and for decision compels us as practical men to do our best to overlook this awkward fact and to behave exactly as we should if we had behind us a good Benthamite calculation of a series of prospective advantages and disadvantages, each multiplied by its appropriate probability, waiting to be summed.”
The conclusion of the Keynes passage is particularly insightful as it gets at why it is so important to be clear on the difference, which otherwise might seem like little more than semantics: people need to act. They will strive for a basis to treat uncertainty as if it were risk so as to tackle it more easily, but however successful they are or are not, they must act nonetheless.
The Knight extract hints at the direction of the book’s argument, which I will summarise here: that profit is the essence of competitive uncertainty. Were there no uncertainty, but merely quantifiable risk in patterns of production and consumption, competition would drive all prices to a stable and commoditised equilibrium. In financial vocabulary, we would say there would be no such thing as a sustainable competitive advantage. The cost of capital would be the risk-free rate, as would all returns on capital, meaning profit is minimised. In aggregate, profit would function merely as a kind of force pulling all economic activity to this precise point of strong attraction.
But of course, uncertainty is very real, as Keynes’ quote makes delightfully clear. I would argue, in fact, that in the economic realm it is a direct consequence of subjective value; in engaging in pursuing profit, you are guessing what others will value. As Knight later writes,
“With uncertainty present, doing things, the actual execution of activity, becomes in a real sense a secondary part of life; the primary problem or function is deciding what to do and how to do it.”
So far I have danced around the key word and concept here, so as to try to let the reader arrive at it herself, but this ‘deciding what to do and how to do it’, and ‘pursuing profit’, we call entrepreneurship. In a world with uncertainty, the role of the entrepreneur is to shoulder the uncertainty of untried combinations of capital, the success of which will ultimately be dependent on the subjective valuations of others. This is not something that can be calculated or mathematised, as any entrepreneur (or VC) will tell you. As Ross Emmett noted in his centennial review of Risk, Uncertainty, and Profit, it is no coincidence that the word ‘judgment’ appears on average every two pages in the book.
There are two points about the process of entrepreneurship that I believe ought to be explored further, and which lead us to Soros and Taleb: you can’t just imagine starting a business; you have to actually do it in order to learn anything. And, in order to do it, you have to expose yourself to your own successes and failures. Your experiment changes the system in which you are experimenting, and you will inevitably have a stake in the experiment’s result.
This is fertile ground in which to plant Soros’ theory of reflexivity. As briefly as possible, and certainly not doing it justice, Soros believes that financial markets are fundamentally resistant to truly scientific analysis because they can only be fully understood in such a way that acknowledges the fact that thinking about the system influences the system. He writes that the scientific method:
“is clearly not applicable to reflexive situations because even if all the observable facts are identical, the prevailing views of the participants are liable to be different when an experiment is repeated. The very fact that an experiment has been conducted is liable to change the perceptions of the participants. Yet, without testing, generalisations cannot be falsified.”
All potential entrepreneurial activity is uncertain (by definition) but the fact of engaging in it crystallises the knowledge of its success or failure. The subjective valuations on which its success depends are revealed by the experiment, and you can’t repeat the experiment pretending you don’t now know this information. Alternatively, this can be conceived of in terms of the difference between thinking and acting, or talking and doing. In a reflexive environment, you can’t say what would have happened had you done something, because, had you done it, you would have changed the circumstances that lead to you now claiming you would have done it. As Yogi Berra (allegedly) said, “in theory there is no difference between theory and practice, but in practice, there is,” and as Amy Adams vigorously proclaims in Talladega Nights, quite the treatise on risk and uncertainty by the way, and with a criminally underrated soundtrack, “Ricky Bobby is not a thinker. Ricky Bobby is a driver.”

We can also now invoke ‘skin in the game’, a phrase of dubious origin, but nowadays associated primarily with Nassim Taleb, and expounded in his 2017 book of the same name. Again, not doing it justice (he did write a whole book about this) Taleb believes that people ought to have equal exposure to the potential upsides and downsides of their decisions; ‘ought to’ in both a moral sense of deserving the outcome, but also in the sense of optimal system design, in that such an arrangement encourages people to behave the most prudently out of all possible incentive schemes. It readily applies here in that braving the wild uncertainties of entrepreneurship requires capital — it requires a stake on which the entrepreneur might get the upside of profit, but might get the downside of loss. I say ‘might’ because you cannot possibly know the odds of such a wager. It relies not on risk, but on uncertainty. As Taleb writes, “entrepreneurs are heroes in our society. They fail for the rest of us.”
The combined appreciation of ‘judgment’ and ‘skin in the game’ is key to understanding what entrepreneurs are actually doing. They do not merely throw capital into a combinatorial vacuum; they are intuiting the wants and needs of potential customers. And as I simply cannot resist the opportunity to employ, possibly my favourite quote from any economist, ever: as Alex Tabarrok says, a bet is a tax on bullshit. Or, don’t talk; do.
Image for post
my desk at work. It’s good to keep these things in mind.
That same Emmett review of Knight’s book noted that the very concept of Knightian uncertainty re-emerged in the public consciousness around a decade ago due to two events: the role ironically played by financial risk instruments in the financial crisis, which neoclassical economists had up until that point insisted would reduce uncertainty in markets (search for “Raghuram Rajan Jackson Hole” if unfamiliar); and Taleb publishing the bestseller The Black Swan.
( Although, naturally, Taleb deplores the concept of ‘Knightian Uncertainty’. What I believe Taleb truly objects to, however, is how the concept has come to be used, rather than anything Knight himself believed. Economists often invoke ‘Knightian Uncertainty’ as a sleight of hand to demarcate some corner of reality, and imply that everywhere else is merely ‘risky’ and can be modelled. This is nonsense. In real life, everything is uncertain, or, as Joseph Walker succinctly put, “Taleb’s problem with Knightian uncertainty is that there’s no such thing as non-Knightian uncertainty.” I think Knight would almost certainly agree, as would anybody who has actually read Knight, instead of employing his name in the course of macro-bullshitting, as Taleb would put it.)
Writes Emmett,
“Taleb did not suggest that uncertainty could be handled by risk markets. Instead, he made a very Knightian argument: since you cannot protect yourself entirely against uncertainty, you should build robustness into your personal life, your company, your economic theory, and even the institutions of your society, to withstand uncertainty and avoid tragic results. These actions imply costs that may limit other aspects of your business, and even your openness to new opportunity.”
But enough about entrepreneurship, what about financial markets? Well, financial markets are readily understood as one degree removed from entrepreneurship. With adequate mental flexibility, you can think of them as markets for fractions of entrepreneurial activity. Entrepreneurship-by-proxy, we might say. If you want, you can use them to mimic the uncertainty profile of an entrepreneur: your ‘portfolio’ could be 100% the equity of the company you wish you founded. Or 200%, with leverage, if you are really gung-ho! But most people think precisely the opposite way: markets present the opportunity to tame the rabid uncertainty of entrepreneurship in isolation, and skim some portion of its aggregate benefit.
There is an additional complication. The fact of such markets usually being liquid enough to enable widespread ownership creates the incentive to think not about the underlying entrepreneurship at all, but only about the expectations of other market participants — to ignore the fundamentals and consider only the valuation. There are shades of Soros’ reflexivity here. The market depends to some extent on the thinking of those participating in the market about the market. This is sometimes called a Keynesian beauty contest, after Keynes’ analogy of judging a beauty contest not on the basis of who you think is most beautiful, but on the basis of who you think others will think is the most beautiful. But if everybody is doing that, then you really need to judge on the basis of who you think others will think others will think is the most beautiful, and so on. Unlike the entrepreneur, who must only worry about the subjective valuation of his potential customers, participants in financial markets must worry, in addition, about the subjective valuation of this subjective valuation by other market participants. There is often grumbling at this point that this represents ‘speculation’ as opposed to ‘investment’, and I certainly buy the idea that over time periods long enough to reflect real economic activity allowed for by the investments, such concerns will make less and less of a difference. As Benjamin Graham famously said, “in the short run, the market is a voting machine, but in the long run, it is a weighing machine”. But the voting still happens. It is clearly real and needs to be accounted for. Risk is once again useless. Uncertainty abounds.
This range of possibilities is intriguing and points to a deeper understanding of what financial markets really are: the aim of a great deal of finance is to grapple with the totality of uncertainty inherent in entrepreneurial activity — equally well understood as ‘investment of capital’, given the need for a ‘stake’ — by partitioning it into different exposures that can sensibly be described as relatively more or less ‘risky’. The aim of doing so is generally to minimise the cost of capital going towards real investment by tailoring the packaging of uncertainty to the ‘risk profiles’ of those willing to invest, as balanced by escalating transaction costs if this process becomes too fine-grained.
This is the essence of a capital structure: the more senior the capital claim, the better defined the probability space of outcomes for that instrument. Uncertainty in aggregate cannot be altered, nor can its influence be completely removed from individual instruments, but exposure to uncertainty can be unevenly parcelled out amongst instruments.
This suggests a far more sophisticated understanding of ‘the risk/reward trade-off’ and ‘the equity premium’ than is generally accepted in the realm of modern portfolio theory, and, by extension, the EMH: bonds are likely to get a lower return than stocks not because they are less ‘risky’ (which in that context is even more questionably interpreted as ‘less volatile’) but because they are engineered to be less uncertain. The burden of uncertainty is deliberately shifted from debt to equity. You don’t get a ‘higher reward’ for taking on the ‘risk/volatility’ of equities; you deliberately expose yourself to the uncertain possibility of a greater reward in exchange for accepting an uncertain possibility of a greater loss.
It is worth pondering for a second that this is arguably why the ‘equity risk premium’ even exists (and why neoclassical economists are so confused about it, while financial professionals are not in the slightest) — if there really were no uncertainty in investment and every enterprise — and hence every financial instrument linked to it — had a calculable risk profile, then price discrepancies derivable from expectation values could be arbitraged away. There would be no equity risk premium — nor a risk premium of any kind on any asset. Everything would be priced correctly and volatility would be zero. That volatility is never zero clearly invalidates this idea. I suggest that the distinction between risk and uncertainty provides at least part of the explanation: unless, by remarkable coincidence, every market participant’s opportunity costs (of exposure, liquidity, time, etc.) and perception of uncertainty (of fundamentals, other’ perceptions of fundamentals, others’ perception of others’ perceptions, etc.) is all identical, and remains so over a period of time, price-altering trading will occur.
(I will note in passing that this commentary is merely intended to provide the intuition that something is amiss with the ‘equity premium puzzle’. It is incomplete as an explanation. In the later section on leverage efficiency, I will cover Peters’ and Adamou’s more formal proof of the puzzle’s non-puzzliness.)
An important concept to appreciate in the context of uncertainty is that of ‘heuristics’. This is an important loose-end to tie up before moving on from uncertainty, along with one more, ‘randomness and unpredictability’, which I cover shortly. This is quite a simple idea that originates with Herbert Simon and has been taken up with force more recently by Gerd Gigerenzer of the Max Planck Institute for Human Development, and more obliquely by Taleb. Simon’s framing began by assuming that individuals do not in fact have perfect information, nor the resources to compute perfectly optimal decisions. Given these constraints, Simon proposed that individuals demonstrate bounded rationality; they will be as rational as they can given the information and resources they actually have. This probably sounds straightforward enough — perhaps tautological — but notice it flies in the face of behavioural economics, which tends to cover for neoclassical economics by saying, effectively, that since information and competition are perfect, risk is always defined and the optimal decision can always be calculated, but the reason people don’t do so is that they are hopelessly irrational. I have always thought this is quite silly on the face of it, but it is clearly also seductive. Anybody reading the likes of Thinking, Fast and Slow immediately gets the intellectual rush of thinking everybody is stupid except him.
Bounded rationality encourages the development of ‘heuristics’, which the reader may recall behavioural economists railing against. A heuristic is effectively a rule of thumb for dealing with an uncertain environment that you are pretty sure will work even if you can’t explain why, precisely. The classic example is that of a dog and a frisbee, or an outfielder in baseball catching a flyball: the outfielder could solve enough differential equations to calculate the spot the ball will land, but the dog certainly can’t. And it turns out that neither do: in real life, they adjust their running speed and direction such that the angle at which they see the frisbee or ball stays constant. And it works. No equations required. Yippee.
(Farrington’s Heuristic is another good example, which I made up while editing a later version of this essay— if a writer is discussing risk, uncertainty, knowledge, and the like, if he refers to Gödel’s Incompleteness Theorems, and if he is not obviously joking, then everything else he says can immediately be dismissed because he is a bullshitting charlatan enamoured by cargo cult math. This heuristic has only one binary parameter — ‘is he joking?’ — and so is highly robust. In case anybody cares, the theorems are NOT about ‘knowledge’: they are about provability within first order formal logical theories strong enough to model the arithmetic of the natural numbers. This is quite a specific mathematical thing that bears no relation whatsoever to epistemology or metaphysics. Also, there are two of them, which turns out to be important if you understand what the first one says.)
The implied simplicity of heuristics has subtle mathematical importance, also. A more technical way of specifying this is to say that they have very few parameters — discrete, independent information inputs to the decision procedure — ideally they could even have zero. In a purely risky environment (if such a thing exists, which, in real life, it almost certainly does not) a decision procedure ought to have as many parameters as are needed to capture the underlying probability distribution. But the more uncertainty you add to such an environment, the more dangerous this becomes, essentially because what you are doing is fine-tuning your model to an environment that simply no longer exists. Eventually you will get an unforeseen fluctuation so large that your overfitted model gives you a truly awful suggestion. Heuristics are robust to such circumstances in light of having very few parameters to begin with. Think back to the outfielder: imagine he solves all the necessary fluid dynamical equations, taking account of the fly ball’s mass, velocity, and rotation, the air’s viscosity, the turbulence generated, and so on. If there is then a gust of wind, he’s screwed. His calculation will be completely wrong. But if he embraces the heuristic of just looking at the damn ball this won’t matter!
Interested readers are encouraged to peruse Gigerenzer’s recent(ish) work on the use of heuristics in finance, and their abuse in behavioural economics, which recently got a shout out in Bloomberg, or this video which is a great introduction to Gigerenzer’s ideas, as well as their connection to Taleb’s more informal thinking on the same topic. (also, note the number of times Gigerenzer uses the word ‘complex’. It is no coincidence that this is a lot, as we shall shortly see):
The video linked to is around an hour and a half, so the reader need not take such a detour now, but I would encourage it at some point, as both Gigerenzer and Taleb are excellent. My favourite excerpt comes around the 19-minute mark, when Gigerenzer recalls that Harry Markowitz — considered the founder of modern portfolio theory — didn’t actually use any Nobel-prize winning modern portfolio theory for his own retirement portfolio; he used the zero-parameter 1/n approach. If one were being especially mean-spirited, one might say that he didn’t want his own bullshit to be taxed. And as it turns out, in order for the Markowitz many-many-many parameter approach to investing to consistently outperform 1/n, you would need around 500 years of data to finetune the parameters. Of course, you also need the market to not change at all in that time. Good luck with that.
Since markets feature multitudes of interrelated uncertainties, it is reasonable to expect participants to interact with them not with the perfect rationality of provably optimal behaviour, but with the bounded rationality of heuristics, which are selected on the basis of judgment, intuition, creativity, etc. Basically, people mostly are not stupid. And if they are, they have skin in the game, so they get punished, and possibly wiped out.
A kind of nice, conceptual corollary to ‘risk is not uncertainty’ is, ‘unpredictability is not randomness’. There can be unpredictable events that are not random, and randomness that is not unpredictable. The difference essentially comes down to ‘causation’. Think of Keynes’ example of the obsolescence of a new invention. This is ‘unpredictable’ not because it is subject to an extremely complicated probability density function, but because the path of causation that would lead to such a situation involves too much uncertainty to coherently grasp. Or think of the Bitcoin mining process. The time series of the first non-zero character in the hash of every block is certifiably random, but it is not unpredictably random. It is the result of a highly coordinated and purposeful effort. It doesn’t spring forth from beta decay. Because we understand the causal process by which this time series emerges, we can predict this randomness very effectively.
A key building block of the EMH is the ‘random walk hypothesis’: the idea that you can ‘prove’ using statistical methods that stock prices follow ‘random walks’ — a kind of well-defined and genuinely random mathematical behaviour. But you can do no such thing. You can prove that they are indistinguishable from random walks, but that is really just saying you can use a statistical test to prove that some data can pass a statistical test. If you understand what causes price movements, you will arrive at no such nonsense as claiming that the moves are, themselves, random. They very probably look random because they are fundamentally unpredictable from the data. And they are fundamentally unpredictable from the data because they derive from the incalculable interplay of millions of market participants’ subjective assessments of the at-root uncertain process of entrepreneurship.
None of this is based on randomness, nor ‘risk’, nor ‘luck’. It is based on the unknown and unknowable profit that derives from intuiting the results of untried and unrepeatable experiments and backing one’s intuition with skin in the game.
Before moving on, I think it is worth tying all of this to where it is more tangibly sensible, lest the reader not quite know what to do with it all. A big deal was made recently about Netflix being by far the best performing US mid-to-large-cap stock of the 2010s. Netflix is useful as an example because of the scale of its success, but note the following argument does not depend on scale at all. While you could craft an explanation as complicated as you like, I think saying, streaming is better than cable, pretty much does it, once added to all the circumstantial factors to do with the competitive and technological environment. Now imagine an investor in 2010 whose thesis was that streaming is better than cable and would likely win in the long run, who surveyed the competitive environment, and decided Netflix would be a good investment. Is their outperformance over the next 10 years ‘luck’? Was all the ‘information’ ‘in the price’ in 2010? Would the CAPM tell you what the price should have been? Did the stock go for a nice little random walk to the moon?
This is clearly an insane interpretation. Consider the alternative: The investor better intuited the subjective values of future consumers than did the average market participant. Very likely she justified this on the basis of a heuristic or two. She staked capital on this bet — which was not risky and random, but uncertain and unpredictable — and exposed herself to a payoff that turned out to be huge, because she was right! To the peddlers of the EMH, rational expectations, perfect information, and the like, this obviously sensible interpretation is utterly heretical.
Economic Complexity Resists Equilibria
The link between profit and entrepreneurship can be tugged at ever-so-slightly further, and invites a brief detour into the basics of complex systems. The argument goes more or less as follows: the discussion on uncertainty needn’t be interpreted as a call to abandon mathematical analysis altogether — just the sloppy mathematics of risk and randomness that has effectively no connection to the real world. There is an alternative mathematical approach, however, which directly addresses and contradicts the standard neoclassical formalism.
The starting point is Israel Kirzner, widely considered one of the foremost scholars of entrepreneurship, and his book, Competition and Entrepreneurship. One of Kirzner’s theses is a positive argument that has roughly two parts, as follows: first, entrepreneurship is by its nature non-exclusionary. It is a price discrepancy between the costs of available factors of production and the revenues to be gained by employing them in a particular way — or, profit. In other words, it is perfectly competitive. It does not rely on any privileged position with respect to access to assets; The assets are presumed to be available on the market. They are just not yet employed in that way, but could be, with capital that is presumably homogeneous. Anybody could do so. The only barrier is that of the willingness to judge and stake on uncertainty. He writes,
“The entrepreneur’s activity is essentially competitive. And thus competition is inherent in the nature of the entrepreneurial market process. Or, to put it the other way around, entrepreneurship is inherent in the competitive market process.”
This notion of what ‘competition’ really means is highly antithetical to the neoclassical usage. In fact, it is more or less the exact opposite. Rather than meaning something like, tending towards abnormal profit and hence away from equilibrium, the neoclassicals mean, tending towards equilibrium and hence away from abnormal profit. Kirzner bemoans this,
“Clearly, if a state of affairs is to be labelled competitive, and if this label is to bear any relation to the layman’s use of the term, the term must mean either a state of affairs from which competitive activity (in the layman’s sense) is to be expected or a state of affairs that is the consequence of competitive activity … [Yet] competition, to the equilibrium price theorist, turned out to refer to a state of affairs into which so many competing participants have already entered that no room remains for additional entry (or other modification of existing market conditions). The most unfortunate aspect of this use of the term ‘competition’ is of course that, by referring to the situation in which no room remains for further steps in the competitive market process, the word has come to be understood as the very opposite of the kind of activity of which that process consists. Thus, as we shall discover, any real-world departure from equilibrium conditions came to be stamped as the opposite of ‘competitive’ and hence, by simple extension, as actually ‘monopolistic’.”
I’d note in passing the delightful similarity in the concluding thought of this extract to the argument of Peter Thiel’s Zero to One, considered by many a kind of spiritual bible for — you guessed it — entrepreneurship. Anyway …
Kirzner’s second positive argument is that correcting this conceptual blunder leads one to realise that a realistic description of competitive markets would not be as constantly at equilibrium, but rather as constantly out of equilibrium. And that’s really all we need to move on to complex systems.
Complex systems are commonly associated with the Santa Fe Institute, and popularised by W. Mitchell Waldrop’s fantastic popular science book, Complexity. Waldrop focuses, for the most part, on one of the SFI’s first ever workshops, held between a group of physicists and economists in 1987. The proceedings of the workshop are fantastic, have aged very well, and seem to your author cheap relative to his subjective valuation of them at ~$70 in paperback or ~$140 in hardback. My thinking here comes from the very first paper of the workshop, W. Brian Arthur’s now somewhat infamous work on increasing returns. To get a sense of what I mean by ‘infamous’, consider the following from Waldrop:
“Arthur had convinced himself that increasing returns pointed the way to the future for economics, a future in which he and his colleagues would work alongside the physicists and the biologists to understand the messiness, the upheaval, and the spontaneous self-organisation of the world. He’d convinced himself that increasing returns could be the foundation for a new and very different kind of economic science.
Unfortunately, however, he hadn’t much luck convincing anybody else. Outside of his immediate circle at Stanford, most economists thought his ideas were — strange. Journal editors were telling him that this increasing-returns stuff ‘wasn’t economics.’ In seminars, a good fraction of the audience reacted with outrage: how dare he suggest that the economy was not in equilibrium! ”
Readers can probably sense where this is going.
Arthur’s paper at the workshop, Self-Reinforcing Mechanisms in Economics, is a breath of fresh air if you have ever slogged through the incessant cargo cult math of neoclassical financial economics (as I had to in researching this essay — thanks a lot, Nic!) It is frankly just all so sensible! Okay, so there are a few differential equations, but only after ten pages of things that are obviously true, and only to frame the obviously true observations in the absurd formalism of the mainstream.
To begin with, “conventional economic theory is built largely on the assumption of diminishing returns on the margin (local negative feedbacks); and so it may seem that positive feedback, increasing-returns-on-the-margin mechanisms ought to be rare.” Standard neoclassical theory assumes competition pushes all into equilibrium, from which a deviation is punished by the negative feedback of reduced profits. So far, so good.
“Self-reinforcement goes under different labels in these different parts of economics: increasing returns; cumulative causation; deviation-amplifying mutual causal processes; virtuous and vicious circles; threshold effects; and non-convexity. The sources vary. But usually self-reinforcing mechanisms are variants of or derive from four generic sources: large set-up or fixed costs (which give the advantage of falling unit costs to increased output); learning effects (which act to improve products or lower their cost as their prevalence increases); coordination effects (which confer advantages to ‘going along’ with other economics agents taking similar action); and adaptive expectations (where increased prevalence on the market enhances beliefs of further prevalence).”
Now we are getting into the meat of it. An example or two wouldn’t hurt before applying this to entrepreneurship and markets.
Arthur likes Betamax versus VHS — which is a particularly good example in hindsight because we know that VHS won despite being mildly technologically inferior. Point number 1: If a manufacturer of VHS tapes spends an enormous amount on the biggest VHS (or Betamax) factory in the world, then the marginal costs of producing VHS will be lower from that point on. Even if the factory as a whole is loss making, the costs are sunk, and so the incentive is to pump out VHS by the gallon. The fact that this can be done so cheaply makes consumers more likely to choose VHS over Betamax, which will in turn justify the initial expense and contribute positive feedback (via profit).
Point number 2: doing so may give the owner of the factory the experience to learn how to do so even more efficiently in the future. By the same eventual mechanism as above, this contributes positive feedback via lower prices. (interested readers are encouraged to look into ‘Wright’s Law’, in particular a recent paper by Béla Nagy, Doyne Famer, Quan Bui, and Jessika Trancik, which basically says that Moore’s Law happens for everything, just slower; or, we learn by doing)
Points number 3 and 4: if more people seem to be buying VHS tapes than Betamax, then producers of Betamax players are incentivised to shift production towards VHS players instead. Cheaper VHS players incentivise consumers to buy more VHS tapes. The appearance of VHS winning this battle causes economic agents to adapt their behaviour in such a way that makes VHS more likely to actually win. In glancing over an early draft of this essay, Nic kindly pointed out to me that this represents the dominant philosophy behind growth VC from 2015 until WeWorkGate, as if a bunch of zealous, born-again Arthurians were playing a game of non-iterated prisoner’s dilemma with other people’s money. Anyway …
Arthur writes, “if Betamax and its rival VHS compete, a small lead in market share gained by one of the technologies may enhance its competitive position and help it further increase its lead. There is positive feedback. If both systems start out at the same time, market shares may fluctuate at the outset, as external circumstances and ‘luck’ change, and as backers manoeuvre for advantage. And if the self-reinforcing mechanism is strong enough, eventually one of the two technologies may accumulate enough advantage to take 100% of the market. Notice however we cannot say in advance which one this will be.”
While Arthur mostly considers realistic examples in economics which have discrete end-states that are then ‘locked into’, such as settling on VHS over Betamax, or Silicon Valley over Massachusetts Route 128, my contention would be that every one of these features describes a part of the process of entrepreneurial competition. The fact of staking capital at all towards an uncertain end represents a fixed cost which must be matched by competitors, and after which unit costs fall. As we have mentioned several times, entrepreneurs learn from the result of their experiments and improve their own processes. There is a clear coordination effect for customers in the default assumption of doing whatever other customers are doing. And adaptive expectations are likewise fairly straightforwardly applied: we tend to assume that businesses will continue to exist and that we can continue to act as their customers. Businesses tend to assume the same of their customers within reasonable bounds of caution. The specific positive feedback as a result of each individual effect is that of ‘profit’ — it is positive in the sense that it can be reinvested in the enterprise and allow it to grow.
Of course, it is possible that these effects would diminish and the marginal feedback become negative. But what we are more tangibly proposing here is that any once-existing competitive advantage has been completely eroded away. This only happens when the product itself becomes either obsolete in light of a superior competitor, or completely commoditised. The former is simply more of the same at the macro level, but the latter we can in turn explain by uncertainty becoming so minimal that we can more or less safely assume it is merely risk. Such circumstances are few and far between. Uncertainty is prevalent in all aspects of economic life, as we have discussed. My argument here is that, so, therefore, are increasing returns and positive feedback loops.
To bring in Arthur one last time:
“if self-reinforcement is not offset by countervailing forces, local positive feedbacks are present. In turn, these imply that deviations from certain states are amplified. These states are therefore unstable. If the vector-field associated with the system is smooth and if its critical points — its ‘equilibria’ — lie in the interior of some manifold, standard Poincaré-index topological arguments imply the existence of other critical points or cycles that are stable, or attractors. In this case multiple equilibria must occur. Of course, there is no reason that the number of these should be small. Schelling gives the practical example of people seating themselves in an auditorium, each with the desire to sit beside others. Here the number of steady-states or ‘equilibria’ would be combinatorial.”
Recall there is no way to know from the starting point which steady-state will be settled into. And of course, Arthur is only talking about specific economic circumstances, not the aggregate of all economic behaviour. The aggregate will likely have shades of evolution in a competitive environment (another concept we will soon encounter in more detail): many, many such interdependent sub-systems, always moving towards their own steady state, but almost all never getting there. And so, in summary, there is a solid mathematical basis to saying that economic behaviour in aggregate is wildly uncertain.
Before moving on, I just want to mention that Arthur should almost certainly be better known and respected in Bitcoin circles. Readers uninterested in the connection I am proposing between Bitcoin and complex systems (or unimpressed by my amateur passion for both) can skip ahead without missing anything. Arthur’s 2013 paper, Complexity Economics, is an excellent place to start. Likewise, a good argument can be made that complex systems researchers should be a lot more interested in Bitcoin. Readers may well have picked up on the essence of Arthur’s analysis consisting of ‘network effects’. I avoided using the term because Arthur himself doesn’t use it. But he is considered the pioneer of their analysis in economics, and when you think about it, the concept of ‘increasing returns’ makes perfect sense in the context of a network. What greater competitive advantage can you have than everybody needing to use your product simply because enough people already use it? And what product do people need to use solely because others are using it more than ‘money’?
Although I have eschewed the idea of ‘lock-in’ as helpful for the analysis above, Bitcoin surely has amongst the strongest interdependent network effects of any economic phenomenon in history? Is it not a naturally interdisciplinary complex adaptive system par excellence? Is it not a form of artificial life, coevolved with economising humans in the ecology of the Internet? I mean, for goodness’ sake, Andreas Antonopoulos claims to have put ants on the cover of Mastering Bitcoin because,
“the highly intelligent and sophisticated behaviour exhibited by a multimillion-member ant colony is an emergent property form the interaction of the individuals in a social network. Nature demonstrates that decentralised systems can be resilient and can produce emergent complexity and incredible sophistication without the need for a central authority, hierarchy, or complex parts.”
Back in the SFI workshop, Arthur writes,
“When a nonlinear physical system finds itself occupying a local minimum of a potential function, ‘exit’ to a neighbouring minimum requires sufficient influx of energy to overcome the ‘potential barrier’ that separates the minima. There are parallels to such phase-locking, and to the difficulties of exit, in self-reinforcing economic systems. Self-reinforcement, almost by definition, means that a particular equilibrium is locked in to a degree measurable by the minimum cost to effect changeover to an alternative equilibrium.”
I’m not sure anybody can sensibly describe what such a ‘minimum cost’ would be. Particularly because Bitcoin is set up in such a way that any move away from lock-in by one metric causes a disproportionate pull back to lock-in by another. It’s Schelling points all the way down.
Markets Aggregate Prices, Not Information
The most frustrating thing about the EMH for me is that even the framing is nonsensical. You don’t really need to get into subjective value, uncertainty, complex systems, and so on, to realise that in reading the proposition, prices reflect all available information, you have already been hoodwinked (hoodwunk?). What does ‘reflect’ mean?
Nic dramatically improved upon this by saying that markets aggregate information. I noticed this is typical of many more enlightened critiques of EMH, and it serves as a far better starting point, in at least suggesting a mechanism by which the mysterious link between information and price might be instantiated. Unfortunately, I think the mechanism suggested is simply invalid. It is not realistic at all and it implicitly encourages a dramatic misunderstanding of what prices really are and where they come from.
In making sense of this we have to assume some kind of ‘function’ from the space of information to price. I think it’s acceptable to mean this metaphorically, without implying the quasi-metaphysical existence of some such force. We might really mean something like, the market behaves as if operating according to such and such a function. Adam Smith’s ‘invisible hand’ is an instructive comparison. For the time being, I will talk as if some such function ‘exists’.
We can maybe imagine information as existing as a vector in an incredibly high-dimensional space, at least as compared to price, which is clearly one-dimensional. We could even account for the multitudes of uncertainty we have already learned to accept by suggesting that each individual’s subjective understanding of all the relevant factors and/or ignorance of many of them constitutes a unique mapping of this space to itself, such that the ‘true information vector’ is transformed into something more personal for each market participant. Perhaps individuals then bring this personal information vector to the market, and what the market does is aggregate all the vectors by finding the average. Finally, the market projects this n-dimensional average vector onto the single dimension of price. If you accept the metaphorical nature of all these functions, I can admit this model has some intuitive appeal, in the vein of James Surowiecki’s The Wisdom of Crowds.
The problem is that this is clearly not how anybody actually interacts with markets. You don’t submit your n-dimensional information/intention-vector; you submit your one-dimensional price. That’s it. The market aggregates these one-dimensional price submissions in real time by matching the flow of marginal bids and asks.
This understanding gets two birds stoned at once. First, it captures the mechanics of how we know price discovery in markets actually works. There is no mysterious, market-wide canonical projection function — no inexplicable ‘prices reflect information’ — there are just prices, volumes, and the continuous move towards clearing.
Second, it implies a perfectly satisfactory and not at all mysterious source of the projection of information into price: individuals who make judgments and act. Any supposedly relevant ‘information’ is subject both to opportunity cost and uncertainty. Individuals alone know the importance of their opportunity costs, and individuals alone engage with uncertainty with heuristics, judgment, and staking. If individuals are wrong, they learn. If they are very wrong, they are wiped out. Effective heuristics live to fight another day.
I am genuinely surprised that this confusion continues to exist in the realm of the EMH, given that, as far as I am concerned, Hayek cleared it up in its entirety in The Use of Knowledge in Society. A superficial reading of Hayek’s ingenious essay might lead one to believe something like prices reflect information. But, to anachronistically borrow our function metaphor once more, Hayek points out that the projection from the n-dimensions of information to the one dimension of price destroys an enormous amount of information. Which is the whole point! Individuals are incapable of understanding the entirety of information in the world. Even the entirety of individuals is incapable of this. Thanks to the existence of markets, nobody has to. They need only know about prices. ‘Perfect information’ is once again shown to be an absurdity. Of the ‘man on the spot’, whom we might hope would make a sensible decision about resource allocation,
“There is hardly anything that happens anywhere in the world that might not have an effect on the decision he ought to make. But he need not know of these events as such, nor of all their effects. It does not matter for him why at the particular moment more screws of one size than of another are wanted, why paper bags are more readily available than canvas bags, or why skilled labor, or particular machine tools, have for the moment become more difficult to obtain. All that is significant for him is how much more or less difficult to procure they have become compared with other things with which he is also concerned, or how much more or less urgently wanted are the alternative things he produces or uses. It is always a question of the relative importance of the particular things with which he is concerned, and the causes which alter their relative importance are of no interest to him beyond the effect on those concrete things of his own environment.”
Hayek proposes this be resolved by the price mechanism:
“Fundamentally, in a system in which the knowledge of the relevant facts is dispersed among many people, prices can act to coordinate the separate actions of different people in the same way as subjective values help the individual to coordinate the parts of his plan.”
Perhaps ironically, this points to the only sensible way in which markets can be called ‘efficient’. They are efficient with respect to the information they manipulate and convey: as a one-dimensional price, it is the absolute minimum required for participants to interpret and sensibly respond. Markets have excellent social scalability; they are the original distributed systems, around long before anybody thought to coin that expression.
Interestingly, this meshes very nicely with the complex systems approach to economics associated with Arthur at SFI, and perhaps more specifically with John Holland. His paper at the aforementioned inaugural economics workshop, The Global Economy as an Adaptive Process, at seven pages and zero equations, is well worth a read. Holland recounts many, now familiar, difficulties in mathematical analysis of economics that assume linearity, exclusively negative feedback loops, equilibria, and so on, before proposing that ‘the economy’ is best thought of as a type of ‘adaptive nonlinear network’ he calls a ‘classifier system’. Its features are worth exploring, even if they require some translation:
“Each rule in a classifier system is assigned a strength that reflects its usefulness in the context of other active rules. When a rule’s conditions are satisfied, it competes with other satisfied rules for activation. The stronger the rule, the more likely it is to be activated. This procedure assures that a rule’s influence is affected by both its relevance (the satisfied condition) and its confirmation (the strength). Usually many, but not all, of the rules satisfied will be activated. It is in this sense that a rule serves as a hypothesis competing with alternative hypotheses. Because of the competition there are no internal consistency requirements on the system; the system can tolerate a multitude of models with contradictory implications.”
We could easily translate ‘rule’ as ‘entrepreneurial plan’ or something similar. Entrepreneurial plans can contradict one another, clearly — if they are bidding on the same resources for a novel combination — and can and do compete with one another. Clearly, such plans are hypotheses about the result of an experiment that hasn’t been run yet. Holland then says,
“A rule’s strength is supposed to reflect the extent to which it has been confirmed as a hypothesis. This, of course, it’s a matter of experience, and subject to revision. In classifier systems, this revision of strength is carried out by the bucket-brigade credit assignment algorithm. Under the bucket-brigade algorithm, a rule actually bids a part of its strength in competing for activation. If the rule wins the competition, it must pay this bid to the rules sending the messages that satisfied its condition (its suppliers). It thus pays for the right to post its message. The rule will regain what it has paid only if there are other rules that in turn bid and pay for its message (its consumers). In effect, each rule is a middleman in a complex economy, and it will only increase its strength if it turns a profit.”
Much of this does not need translating at all: we see Menger’s higher orders of capital goods, and value of intermediate goods resting ultimately with the subjective value of consumers, who pass information up the chain of production. We see agents that learn from their experience. We see skin-in-the-game of staked capital in ‘bidding part of its strength’ and we see uncertain gain or reward ultimately realised by profit or loss. But most importantly — most Hayekily — we see agents who have no such fiction as ‘perfect information’, but rather responding solely to prices in their immediate environment, and whose reactions affect prices that are passed to other environments. In Complexity, Waldrop quotes Holland’s frustration with the neoclassical obsession with well-defined mathematical problems:
“‘Evolution doesn’t care whether problems are well-defined or not.’ Adaptative agents are just responding to a reward, he pointed out. They don’t have to make assumptions about where the reward is coming from. In fact, that was the whole point of his classifier systems. Algorithmically speaking, these systems were defined with all the rigor you could ask for. And yet they could operate in an environment that was not well defined at all. Since the classifier rules were only hypotheses about the world, not ‘facts’ they could be mutually contradictory. Moreover, because the system was always testing those hypotheses to find out which ones were useful and led to rewards, it could continue to learn even in the face of crummy, incomplete information — and even while the environment was changing in unexpected ways.
‘But its behaviour isn’t optimal!’ the economists complain, having convinced themselves that a rational agent is one who optimises his ‘utility function’.
‘Optimal relative to what?’ Holland replied. Talk about your ill-defined criterion: in any real environment, the space of possibilities is so huge that there is no way an agent can find the optimum — or even recognise it. And that’s before you take into account the fact that the environment might be changing in unforeseen ways.”
Hayek gives us the intuition of prices conveying only what market participants deem to be the most important information and actually destroying the rest, and Holland shows how this can be represented with the formalism of complex systems. But note that the EMH forces us to imagine that the information is somehow in the market itself. It is honestly unclear to me whether the EMH even allows for honest or ‘rational’ disagreement given it implies that the price is ‘correct’, and all other trading is allegedly ‘noise’. By my account (and Hayek’s) people can clearly disagree. That’s why they trade in the first place; they value the same thing differently. This is not at all mysterious if we realise that engaging with markets requires individuals to ‘project’ the n-dimensions of their information, heuristics, judgments, and stakes onto the single dimension of price, and that markets do not project the aggregates; they aggregate the projections.
Markets Tend to Leverage Efficiency
So we know that entrepreneurial efforts will tend towards positive feedback loops if successful, which is a fancy way of saying, they will ‘grow’. And we know that the diversity of compounding uncertainty in markets for securities linked to these efforts will likely generate substantial volatility. But can we say anything more? Can we expect anything more precise?
It turns out that we can, and here we finally get to Alex Adamou, Ole Peters, and the ergodicity economics research program. It’s about time! The goal of the program is to trace the repercussions of a conceptual and algebraic error regarding the proper treatment of ‘time’ in calculations of ‘expectation value’ that pervaded mainstream economics over the course of the twentieth century. Interested readers are encouraged to visit the program’s website, check out this recent primer in Nature Physics, or just follow Ole and Alex on Twitter, which is where most of the action seems to happen anyway!
First, a down to earth example. Imagine you want a pair of shoes. You can either go to the same shoe store every day for a month, or you can go to every shoe store in town all in one trip. If it turns out there is no difference between these approaches, this system is ‘ergodic’. If, as seems more likely, there is a difference, the system is ‘non-ergodic’.
Now with more technical detail, the conceptual and algebraic error is as follows: imagine some variable that changes over time, subject to some well-defined randomness. Now imagine a system of many such variables, whose ‘value’ is just the sum of all the values of the variables. Now imagine you want to find the ‘average’ value of a variable in this system in some pure, undefined sense.
How do you make sense of an ‘average’ of a system that will be different every time you run it? Well, you could fix the period of time the system runs for, and take the limit of where individual variables get to attained by running the system over and over and over to infinity. Or, you could fix the number of systems (preferably at ‘one’ for minimal confusion) and take the limit of where individual variables get to attained by running the system further and further into the future, to infinity.
These are called, respectively, the ‘ensemble average’ and the ‘time average’, and are easily remembered as the average achieved by taking x to infinity. ‘Ensemble average’ is commonly known as ‘the expectation’ but Peters and Adamou resist this terminology because it has nothing whatsoever to do with the English word ‘expectation’. You shouldn’t necessarily expect the expectation.
Now these values might be the same. This means you can measure one of these even if what you really want is the other. If so, your system is called ‘ergodic’. The concept first developed within nineteenth century physics when Ludwig Boltzmann wanted to justify using ensemble averages to model macroscopic quantities such as pressure and temperature in fluids, which are strictly speaking better understood as time averages over bajillions of classically mechanical collisions. If any regular readers of mine exist, they will remember me going through much of this in Cargo Cult Math:
Cargo Cult Math
blog.goodaudience.com
My point that time around was to go on to say that a great deal of financial modelling uses techniques — most notably expectation values — which would only be appropriate if the corresponding observables were ergodic. But they are not. Almost none of them are, to a degree that is both obvious and scary once you grasp it in its totality: clearly the numbers in finance are causally dependent on one another and take place in a world in which time has a direction.
My point this time around is more cheerful. I want to direct the reader’s attention to another of Peters’ and Adamou’s papers on the topic: Leverage Efficiency (arXiv link here). This subsection is a whistle-stop tour of what that paper says. The usual disclaimer about not doing it justice absolutely applies. The reader is heartily encouraged to read the paper too.
Imagine a toy model of the price of a stock that obeys geometric Brownian motion with constant drift and with volatility that varies by random draws from a normal distribution. It turns out that the growth rate of the ensemble average price — i.e. the price averaged over all possible parallel systems — is not the same as the time average growth rate of the price — i.e. the growth rate in a single system taken in the long time limit. Clearly what we care about is the time average, as we don’t tend to hold stocks across multiple alternate universes, but rather across time in the actual universe. In particular, in turns out that the ensemble average growth rate is equal to the drift, while the time average growth rate is equal to the drift minus a correction term: the variance over 2.
This becomes very important when we introduce leverage via a riskless asset an investor can hold short. Let’s call the model drift of the stock minus the stipulated drift of the non-volatile riskless asset ‘the excess growth rate’. Then we can say that the ensemble average growth rate in situations with variable leverage is the growth rate of the riskless asset, plus the leverage multiplied by the excess growth rate. However, the time average has a linked correction, as above. As it is difficult at this point to continue the exposition in English, compare the formulae below:
Image for post
The relevance of the difference is that the latter formula is not monotonic in l. In other words, you don’t increase your growth rate unboundedly by leveraging up more and more. This might seem intuitively obvious, and, in fact, the intuition likely strikes in exactly the right spot: in reality there is volatility. The more and more levered you are, the more susceptible you are to total wipeout for smaller and smaller swings. In fact, we can go further and observe that we can therefore maximise the growth rate as a function of leverage, implying an objectively optimal leverage for this toy stock:
Image for post
What might this optimal leverage be in practice? Well, Peters and Adamoupropose the tantalising alternative to the EMH: the stochastic markets hypothesis. As opposed to the EMH’s price efficiency, they propose leverage efficiency: it is impossible for a market participant without privileged information to beat the market by applying leverage. In other words, real markets self-organise such that the optimal leverage of 1 is an attractive point for their stochastic properties.
The paper continues in two directions: firstly, Peters and Adamou propose a theoretical argument for feedback systems that ought to be triggered over long enough periods of the theoretical value of optimal leverage in fact deviating from 1, which all ought to pull it back to 1. I will skip this as it is tangential to the point I am building towards, although obviously very interesting in its own right. Secondly, Peters and Adamou gather data from real markets to establish what the optimal leverage would, in fact, have been. I include some screenshots that strongly suggest this approach is quite fruitful:
Image for post
Image for post
This chart probably deserves some explanation, but is very satisfying once grasped: as opposed to just the S&P500, above, both the German equity market (DAX) and Bitcoin show pretty much identical behaviours to the S&P500, which Peters and Adamou term “satisfying leverage efficiency”. That the Madoff curve is so different, and seems to have no clear maximum, indicates it is likely too good to be true. This is a nice result given that we know Madoff’s returns to be fraudulent!
However, what I really want to get to in all of this is a specific interpretation of the SMH; that markets self-organise such that optimal leverage tends to 1 in the long run. If we assume that the excess return of the stock price is generated by real economic activity (ultimately, the consistency of the stock’s return on equity) in the long enough run, this would seem to suggest that a certain amount of volatility is actually natural. Were a stock to consistently generate an excess return above that of the riskless asset, investors would lever up to purchase it. This mass act would (reflexively!) cause its volatility to shoot up as the price shoots up, and in the inevitable case of a margin call on these levered investors, volatility would increase further as the stock price comes back down.
This is a somewhat naïve explanation, but the gist is that the lack of volatility in the short run will tend to generate excess volatility in the medium run, such that a natural level is tended to in the long run. Or, markets are stochastically efficient. Readers familiar with the unsuspecting role that ‘portfolio insurance’ turned out to have played in 1987’s Black Monday — the single biggest daily stock market drop in modern history that seemed to follow no negative news whatsoever — will find all this eerily familiar. Taleb calls Black Monday a prototypical Black Swan that shaped his formative years as a Wall Street trader. Mandelbrot cites it as sure-fire evidence of power laws and wild randomness in financial markets. It ties together many themes of this essay because, evidently, the information was not in any of the prices. Not in the slightest. I leave it to the reader to mull over what all this implies if interventions in financial markets are targeted solely at reducing volatility as a worthwhile end in itself, the rationale of which makes no mention of growth or leverage. Once again, search for “Raghuram Rajan Jackson Hole” or read about the so-called Great Moderation if unsure where to start. Volatility signals stability, in financial markets and likely well beyond …
All this has a final interesting implication that I teased earlier: the resolution of the so-called ‘equity premium puzzle’; that, according to such-and-such behavioural models from the psychological literature, the excess return of equities ‘should be’ much lower than it really is. Cue the behavioural economists claims of irrational risk aversion, blah blah blah. Peters and Adamou provide an alternative with no reference to human behaviour at all. The difference between the growth rates of the risky (l=1) and riskless (l=0) assets is the excess return minus the volatility correction. If markets are attracted to the point at which leverage efficiency equals 1, then it follows by substituting the definition of the equity risk premium in terms of risky and riskless assets into the equation defining optimal leverage, that the equity premium ought to be attracted to the excess return over 2. Peters and Adamou delightfully write, “our analysis reveals this to be a very accurate prediction … we regard the consistency of the observed equity premium with the leverage efficiency hypothesis to be a resolution of the equity premium puzzle.” QED.
I’ll note before wrapping up this sub-section that any readers triggered by such terms as geometric Brownian motion and normal distributions needn’t be. Peters and Adamou acknowledge that GBM is not realistically either necessary or sufficient as a mechanism for stock price movements. But their argument really only depends on the characteristics of an upward drift and random volatility, both of which are reasonable to expect. They choose GBM because it is simple to handle, well understood, and prevalent in the literature they criticise, but they also write that,
“for any time-window that includes both positive and negative daily excess returns, regardless of their distribution, a well-defined optimal constant leverage exists in our computations …
Stability arguments, which do not depend on the specific distribution of returns and go beyond the model of geometric Brownian motion, led us to the quantitative prediction that on sufficiently long time scales real optimal leverage is attracted to 0 ≤ lopt ≤ 1 (or, in the strong form of our hypothesis, to l-opt =1).”
We knew from previous sections that volatility is likely. It will exist to some extent due to the teased-out implications of subjective values and omnipresent uncertainty. But now we know that it is necessary. It is not noise, irrationality, panic, etc, around a correct price. It is, at least in part, inevitable reflexive rebalancing of leverage around whatever the price happens to be.
Incompleteness
You can’t write ten thousand words on mathematical formalisms outlining the limits of human knowledge without mentioning Gödel’s Incompleteness Theorems.
Adaptation and Fractals
As mentioned in the introduction, of all the dissenting work on the EMH, I most recommend, by far, Andrew Lo’s Adaptive Markets Hypothesis — the original paper and the follow-up book- and the various thoughts of Benoit Mandelbrot on fractals in financial markets — strewn across numerous academic papers, but lucidly conveyed in the popular book, The (Mis)behaviour of Markets. I assume familiarity with these works to avoid explaining everything from scratch, so if the reader is unfamiliar, I encourage jumping ahead to the next section.
My main critique of Lo is that he doesn’t take uncertainty seriously enough. In covering the academic history surrounding the EMH, he only gives Simon a page or so, and Gigerenzer a paragraph. The key point of failure, in my view, is his treatment of the Ellsberg paradox. Or rather, the fact that he stops his rigorous discussion of uncertainty at this point.
The problem here is that the uncertainty in the Ellsberg paradox is confined to the odds, whereas we know from the previous discussion that the uncertainty in economics exists in the outcomes. This means that the odds aren’t just uncertain, they are non-existent. By stopping here, Lo passes off the results of running the experiment that gives rise to the so-called paradox as simply indicating ambiguity aversion, which he presents as a kind of irrational bias — then a segue to behavioural economics. This prevents Lo from exploring the implications of Knightian uncertainty on entrepreneurship and competition, and ultimately gives him little ammunition to take on the EMH directly. In fact, he acknowledges that he never really does — he just proposes something he thinks is better.
That said, I agree that his model is better. Far better! Adaptation is a fascinating concept to employ here. As noted several times, it comes through very naturally in the complex systems approach. I won’t comment on it too much as its roots in evolutionary biology are outside my academic pedigree. But the basic intuition of changing circumstances and responding agents I find rather compelling. As do, it would seem, several thinkers I have already cited. Consider this passage from Kirzner,
“it is necessary to introduce the insight that men learn from their experiences in the market. It is necessary to postulate that out of the mistakes which led market participants to choose less-than-optimal courses of action yesterday, there can be expected to develop systematic changes in expectations concerning ends and means that can generate corresponding alterations in plans.”
Also, there is a tradition of referring to heuristics as ecologically rational, and the biological analogy is no coincidence. This passage from Waldrop’s Complexity on John Holland’s conversion to complex systems thinking in his study of genetics is striking in the almost simple obviousness of the comparison drawn to economics (again, not at all a coincidence):
“it bothered Holland that [R.A.] Fisher kept talking about evolution achieving a stable equilibrium — that state in which a given species has attained its optimum size, its optimum sharpness of tooth, its optimum fitness to survive and reproduce. Fisher’s argument was essentially the same one that economist use to define economic equilibrium: once a species’ fitness is at a maximum, he said, any mutation will lower the fitness … but that did not sound like evolution to me.
… to Holland, evolution and learning seemed much more like — well, a game. In both cases, trying to win enough of what it needed to keep going. In evolution that payoff is literally survival, and a chance for the agent to pass its genes on to the next generation. In learning, the payoff is a reward of some kind, such as food, a pleasant sensation, or emotional fulfilment, but either way, the payoff (or lack of it) gives agents the feedback they need to improve their performance: if they’re going to be ‘adaptive’ at all, they somehow have to keep the strategies that pay off well, and let the others die out.”
One thing I especially like about Lo’s approach is his idea of ‘evolution at the speed of thought’, often rhetorical as much as anything else. I think this provides a useful conceptual tool to deal with what I deemed to be the only consistent deficiency in the material I covered on complex systems: Arthur, Holland, et al, seem to me so focused on the comparison to biological evolution, and on shifting the comparative conceptual framework from physics to biology as a whole, that they forget the role of purposeful human beings in all of this. Economic ‘mutation’ is not random, it is creative, intuitive, judgmental. It happens at the speed of thought because humans think on purpose. They do not cycle through the space of every thought that can possibly be had until they hit on one that happens to be a business plan.
To put this in a wider context and loop back to previously cited thinkers, I think Arthur is best read alongside Kirzner, and indeed Kirzner is best read alongside Arthur. Particularly in The Nature of Technology, which is otherwise an excellent book, Arthur perfectly grasps how change happens, but not why. In Competition and Entrepreneurship, Kirzner perfectly grasps why change happens, but not how. Both the why and the how rely, in part, on understanding economic evolution as an essentially human phenomenon, because genes mutate, but humans think.
Mandelbrot’s ideas on fractals in finance are iconoclastic, to say the least. Unlike Lo, I see nothing to disagree with, and much that probably went over my head. But given Mandelbrot sets himself the task of demolishing the EMH out of left field, and seemingly succeeds, it is definitely worth grappling with.
The mildly boring part of The (Mis)behaviour of Markets is Mandelbrot showing that, empirically, financial data does not seem to fit the Brownian motion of the random walk hypothesis, and hence the EMH. The really juicy part is his explanation of why. To avoid getting into any really tricky mathematics and essentially rewriting his book, I will summarise his argument, again not doing it justice, as, this isn’t random enough. More suggestively, it is too predictably random.
Mandelbrot thinks that prices in financial markets are, up to a certain granularity, fractals. If true, this has many fascinating implications, but the most relevant here is that the self-similarity this implies means that any randomness in their fluctuation must be irregular. It should not be possible to ascertain any regularity just by changing the timespan because they look the same on every timespan (look! there’s ‘time’ again!) The randomness must itself be pretty random. And that randomness must be random, and so on. There are no genuinely normal distributions in finance, Mandelbrot believes, but rather they all tend towards Cauchy. We could be less hand-wavy about all this and point out instead that while a statistical test on some financial data might suggest the tail of a lognormal distribution, we are really looking at a power law. If parameterized to induce fat enough tails, such a distribution may not have a variance, and if fat enough, not even a mean. (And no, it doesn’t have an ‘infinite variance’ or ‘infinite mean’ because that is meaningless, but nice try). As Taleb and Mandelbrot both wrote in Fortune,
“In bell-curve finance, the chance of big drops is vanishingly small and is thus ignored. The 1987 stock market crash was, according to such models, something that could happen only once in several billion billion years.”
Black swans, amiright?
What does this have to do with ‘complex’ markets? Mandelbrot doesn’t explore this idea, and I may be going out on a limb here, but I think this is almost exactly what you would expect if you thought markets were maximally uncertain, so to speak. If risk were predictable, then it could be hedged against. If it were unpredictable in and of itself, but were distributed predictably, then that could be hedged against. And so on and so forth. This all lends itself to a hand-wavy inductive proof by contradiction. We know that nothing can be perfectly hedged because it derives from uncertainty, and uncertainty on uncertainty, and uncertainty on that uncertainty, and so on. Financial markets can shift uncertainty around, and selectively parcel it into more and less risky instruments, but uncertainty itself cannot be removed.
Bitcoin
Oh goodness, I guess I have to say something about Bitcoin now, lest I be accused of rickrolling an angry twitter mob into a sermon on armchair economics. Is the halving priced in?
I have no idea. Which is sort of the moral of all of this. You can’t predict the uncertain future, but you can bet on it. I’m not sure how you would bet on this exact hypothesis: perhaps a combination of options that pay off if and only if the price goes up (or doesn’t go up) by whatever the stock-to-flow model predicts, within some bounds, when it predicts it, within some bounds? Obviously, you could just be long Bitcoin, but then you aren’t isolating the essence of this claim, and you can benefit for all sorts of other reasons. If you do either, you’ll move the price towards the outcome you are hoping for. But only by having put skin in the game. Also, you could believe something very specific about the halving, but have no way of testing it as you don’t believe in stock-to-flow models, or any other valuation model, for that matter. That’s the essence of my noncommittal answer above: I shouldn’t tell you what I think, I should show you my portfolio, right? Well, I have no ‘halving bet’ in my portfolio, so I guess I think nothing. Which is what I said :)
Even so, we can still make a few interesting observations that draw on the above discussion. Clearly, the question relies on reflexivity, which is interesting in and of itself. It’s only derivatively a question about the fundamentals, and more about the extent to which the market is a well-oiled beauty contest. I don’t think I know enough about the actual workings of the Bitcoin market to comment on this. It strikes me that, relative to global equities markets, at least, the range of heuristics that market participants in Bitcoin are using vary wildly from one another. If it makes any sense to say so, they likely have pretty dramatic variance. At the same time, the market itself is probably highly illiquid, relative to what we might be used to. This might suggest the halving isn’t priced in, in the sense that the change in marginal bids and asks at which the market clears that we know is going to happen dwarfs the capital that is already deployed, including towards solely this essentially reflexive bet. But then again, maybe it doesn’t.
Honestly, I just don’t know. And if somebody does claim to know, tell them to show you their portfolio.
Conclusion
Value is subjective, which means uncertainty governs all economic phenomena. This creates a complexity that resists equilibria and is constantly changing besides. Within such a system, prices convey the minimal possible information necessary for economic agents to purposefully react. They do so with judgment and heuristics, not ‘perfect information’, which is nonsensical, as is ‘perfect competition’ and ‘rational expectations’. Prices may pass statistical tests for randomness, but they are not themselves random (although it is plausible that their randomness is random, and that randomness is random, and so on) but rather are unpredictable on the basis of market data alone. They are, however, predictable to the extent that the predictor accurately assesses the future subjective valuations both of economic agents and fellow market participants, and backs up this prediction with staked capital. This act of staking changes the uncertainties at play, rendering any attempt at genuinely scientific analysis futile. You can beat the market, it’s just really hard, and it depends on understanding people, not data. And it’s meaningless if you do it in theory but not practice.
Markets have many characteristics. I suggest they are subjective, uncertain, complex, stochastic, adaptive, fractal, reflexive … — really any clever sounding adjective you like — just not efficient.
Thanks to Nic Carter, Robert Natzler, Alex Adamou, and Sacha Meyers, for edits and contributions. ''',

                '29': '''Ways to think about machine learning
We're now four or five years into the current explosion of machine learning, and pretty much everyone has heard of it. It's not just that startups are forming every day or that the big tech platform companies are rebuilding themselves around it - everyone outside tech has read the Economist or BusinessWeek cover story, and many big companies have some projects underway. We know this is a Next Big Thing.

Going a step further, we mostly understand what neural networks might be, in theory, and we get that this might be about patterns and data. Machine learning lets us find patterns or structures in data that are implicit and probabilistic (hence ‘inferred’) rather than explicit, that previously only people and not computers could find. They address a class of questions that were previously ‘hard for computers and easy for people’, or, perhaps more usefully, ‘hard for people to describe to computers’. And we’ve seen some cool (or worrying, depending on your perspective) speech and vision demos. 

I don't think, though, that we yet have a settled sense of quite what machine learning means - what it will mean for tech companies or for companies in the broader economy, how to think structurally about what new things it could enable, or what machine learning means for all the rest of us, and what important problems it might actually be able to solve. 

This isn't helped by the term 'artificial intelligence', which tends to end any conversation as soon as it's begun. As soon as we say 'AI', it's as though the black monolith from the beginning of 2001 has appeared, and we all become apes screaming at it and shaking our fists. You can’t analyze ‘AI’. 

maxresdefault.jpg
Indeed, I think one could propose a whole list of unhelpful ways of talking about current developments in machine learning. For example:

Data is the new oil

Google and China (or Facebook, or Amazon, or BAT) have all the data

AI will take all the jobs

And, of course, saying AI itself.

More useful things to talk about, perhaps, might be: 

Automation

Enabling technology layers

Relational databases.

Why relational databases? They were a new fundamental enabling layer that changed what computing could do. Before relational databases appeared in the late 1970s, if you wanted your database to show you, say, 'all customers who bought this product and live in this city', that would generally need a custom engineering project. Databases were not built with structure such that any arbitrary cross-referenced query was an easy, routine thing to do. If you wanted to ask a question, someone would have to build it. Databases were record-keeping systems; relational databases turned them into business intelligence systems. 

This changed what databases could be used for in important ways, and so created new use cases and new billion dollar companies. Relational databases gave us Oracle, but they also gave us SAP, and SAP and its peers gave us global just-in-time supply chains - they gave us Apple and Starbucks. By the 1990s, pretty much all enterprise software was a relational database - PeopleSoft and CRM and SuccessFactors and dozens more all ran on relational databases. No-one looked at SuccessFactors or Salesforce and said "that will never work because Oracle has all the database" - rather, this technology became an enabling layer that was part of everything.

So, this is a good grounding way to think about ML today - it’s a step change in what we can do with computers, and that will be part of many different products for many different companies. Eventually, pretty much everything will have ML somewhere inside and no-one will care. 

An important parallel here is that though relational databases had economy of scale effects, there were limited network or ‘winner takes all’ effects. The database being used by company A doesn't get better if company B buys the same database software from the same vendor: Safeway's database doesn't get better if Caterpillar buys the same one. Much the same actually applies to machine learning: machine learning is all about data, but data is highly specific to particular applications. More handwriting data will make a handwriting recognizer better, and more gas turbine data will make a system that predicts failures in gas turbines better, but the one doesn't help with the other. Data isn’t fungible. 

This gets to the heart of the most common misconception that comes up in talking about machine learning - that it is in some way a single, general purpose thing, on a path to HAL 9000, and that Google or Microsoft have each built *one*, or that Google 'has all the data', or that IBM has an actual thing called ‘Watson’. Really, this is always the mistake in looking at automation: with each wave of automation, we imagine we're creating something anthropomorphic or something with general intelligence. In the 1920s and 30s we imagined steel men walking around factories holding hammers, and in the 1950s we imagined humanoid robots walking around the kitchen doing the housework. We didn't get robot servants - we got washing machines.

Screen Shot 2017-11-02 at 4.44.52 PM.png
Washing machines are robots, but they're not ‘intelligent’. They don't know what water or clothes are. Moreover, they're not general purpose even in the narrow domain of washing - you can't put dishes in a washing machine, nor clothes in a dishwasher (or rather, you can, but you won’t get the result you want). They're just another kind of automation, no different conceptually to a conveyor belt or a pick-and-place machine. Equally, machine learning lets us solve classes of problem that computers could not usefully address before, but each of those problems will require a different implementation, and different data, a different route to market, and often a different company. Each of them is a piece of automation. Each of them is a washing machine. 

Hence, one of the challenges in talking about machine learning is to find the middle ground between a mechanistic explanation of the mathematics on one hand and fantasies about general AI on the other. Machine learning is not going to create HAL 9000 (at least, very few people in the field think that it will do so any time soon), but it’s also not useful to call it ‘just statistics’. Returning to the parallels with relational databases, this might be rather like talking about SQL in 1980 - how do you get from explaining table joins to thinking about Salesforce.com? It's all very well to say 'this lets you ask these new kinds of questions', but it isn't always very obvious what questions. You can do impressive demos of voice recognition and image recognition, but again, what would a normal company do with that? As a team at a major US media company said to me a while ago: 'well, we know we can use ML to index ten years of video of our talent interviewing athletes - but what do we look for?’ 

What, then, are the washing machines of machine learning, for real companies? I think there are two sets of tools for thinking about this. The first is to think in terms of a procession of types of data and types of question:  

Machine learning may well deliver better results for questions you're already asking about data you already have, simply as an analytic or optimization technique. For example, our portfolio company Instacart built a system to optimize the routing of its personal shoppers through grocery stores that delivered a 50% improvement (this was built by just three engineers, using Google's open-source tools Keras and Tensorflow).

Machine learning lets you ask new questions of the data you already have. For example, a lawyer doing discovery might search for 'angry’ emails, or 'anxious’ or anomalous threads or clusters of documents, as well as doing keyword searches,

Third, machine learning opens up new data types to analysis - computers could not really read audio, images or video before and now, increasingly, that will be possible.

Within this, I find imaging much the most exciting. Computers have been able to process text and numbers for as long as we’ve had computers, but images (and video) have been mostly opaque. Now they’ll be able to ‘see’ in the same sense as they can ‘read’. This means that image sensors (and microphones) become a whole new input mechanism - less a ‘camera’ than a new, powerful and flexible sensor that generates a stream of (potentially) machine-readable data.  All sorts of things will turn out to be computer vision problems that don’t look like computer vision problems today. 

This isn’t about recognizing cat pictures. I met a company recently that supplies seats to the car industry, which has put a neural network on a cheap DSP chip with a cheap smartphone image sensor, to detect whether there’s a wrinkle in the fabric (we should expect all sorts of similar uses for machine learning in very small, cheap widgets, doing just one thing, as described here). It’s not useful to describe this as ‘artificial intelligence’: it’s automation of a task that could not previously be automated. A person had to look.  

This sense of automation is the second tool for thinking about machine learning. Spotting whether there’s a wrinkle in fabric doesn't need 20 years of experience - it really just needs a mammal brain. Indeed, one of my colleagues suggested that machine learning will be able to do anything you could train a dog to do, which is also a useful way to think about AI bias (What exactly has the dog learnt? What was in the training data? Are you sure? How do you ask?), but also limited because dogs do have general intelligence and common sense, unlike any neural network we know how to build. Andrew Ng has suggested that ML will be able to do anything you could do in less than one second. Talking about ML does tend to be a hunt for metaphors, but I prefer the metaphor that this gives you infinite interns, or, perhaps, infinite ten year olds. 

Five years ago, if you gave a computer a pile of photos, it couldn’t do much more than sort them by size. A ten year old could sort them into men and women, a fifteen year old into cool and uncool and an intern could say ‘this one’s really interesting’. Today, with ML, the computer will match the ten year old and perhaps the fifteen year old. It might never get to the intern. But what would you do if you had a million fifteen year olds to look at your data? What calls would you listen to, what images would you look at, and what file transfers or credit card payments would you inspect?

That is, machine learning doesn't have to match experts or decades of experience or judgement. We’re not automating experts. Rather, we’re asking ‘listen to all the phone calls and find the angry ones’. ‘Read all the emails and find the anxious ones’. ‘Look at a hundred thousand photos and find the cool (or at least weird) people’. 

In a sense, this is what automation always does; Excel didn't give us artificial accountants, Photoshop and Indesign didn’t give us artificial graphic designers and indeed steam engines didn’t give us artificial horses. (In an earlier wave of ‘AI’, chess computers didn’t give us a grumpy middle-aged Russian in a box.) Rather, we automated one discrete task, at massive scale. 

Where this metaphor breaks down (as all metaphors do) is in the sense that in some fields, machine learning can not just find things we can already recognize, but find things that humans can’t recognize, or find levels of pattern, inference or implication that no ten year old (or 50 year old) would recognize. This is best seen Deepmind’s AlphaGo. AlphaGo doesn’t play Go the way the chess computers played chess - by analysing every possible tree of moves in sequence. Rather, it was given the rules and a board and left to try to work out strategies by itself, playing more games against itself than a human could do in many lifetimes. That is, this not so much a thousand interns as one intern that’s very very fast, and you give your intern 10 million images and they come back and say ‘it’s a funny thing, but when I looked at the third million images, this pattern really started coming out’. So, what fields are narrow enough that we can tell an ML system the rules (or give it a score), but deep enough that looking at all of the data, as no human could ever do, might bring out new results? 

I spend quite a lot of time meeting big companies and talking about their technology needs, and they generally have some pretty clear low hanging fruit for machine learning. There are lots of obvious analysis and optimisation problems, and plenty of things that are clearly image recognition problems or audio analysis questions. Equally, the only reason we’re talking about autonomous cars and mixed reality is because machine learning (probably) enables them - ML offers a path for cars to work out what’s around them and what human drivers might be going to do, and offers mixed reality a way to work out what I should be seeing, if I’m looking though a pair of glasses that could show anything. But after we’ve talked about wrinkles in fabric or sentiment analysis in the call center, these companies tend to sit back and ask, ‘well, what else?’ What are the other things that this will enable, and what are the unknown unknowns that it will find? We’ve probably got ten to fifteen years before that starts getting boring.  ''',

                '30': '''Money, Banking, Bitcoin, Libra
allen
allen
Follow
Jun 22, 2019 · 24 min read



there are no necessary or sufficient criteria for ‘money’. Anything that enhances the ability to create universal credit will do.
Image for post
Photo by Fabian Blank, via Unsplash
Money
There is a common misunderstanding of Bitcoin as a ‘payment mechanism’, and hence that it somehow ought to capture all payments. I am not really sure, but I suspect this comes from a dogmatic application of the three essential characteristics of money as typically taught in macroeconomics 101: unit of account, store of value, and medium of exchange. I think this is rather silly and that, really, money is just universal credit. How it works or what extra characteristics it has is beside the point. The former attitude leads one to say things like: it’s too volatile, and, it’s too hard to trade with, and then immediately jump to, it can’t be money, while conveniently ignoring the multitude of other amazing and entirely novel things it can do: for example, it has a guaranteed inflation schedule that cannot be manipulated, transaction fees are either non-existent or regressive, it is totally agnostic to geography or identity, settlement time is rarely over one hour, it is completely transparent, it is a network that is never down and cannot be hacked, it is programmable (to a small degree — more on this later), and more. Better even than the abstraction of ‘money’, a less common but more intelligent approach is to treat Bitcoin as a better version of gold. After a century or so of relentless devaluation of previously gold backed fiat currency we are not used to thinking of the relevance of gold to money or finance. But its legacy is still imprinted on the banking system, and so it is with banks I will begin.
Before getting to the more exciting possibilities it is worth tackling head on why Bitcoin almost certainly can’t be used for payments all on its own. Bitcoin cannot handle the necessary throughput, by design: amending the block size or block confirmation time would be a trivial exercise and could solve this ‘problem’ instantly, but would make the blockchain itself unacceptably large as a data structure such that very few parties could run full nodes and authenticate the chain, reintroducing the centralisation that is essential to the social core of the enterprise to begin with. ‘Fixing’ Bitcoin by making it ‘scale’ would really break it altogether (which is why most copycats are entirely pointless)
How to scale Bitcoin (without changing a thing)
Why Bitcoin banks need to prove their solvency
medium.com
The implicit trade-off of foregoing practical payment applications may be overcome by second-layer protocols such as Lightning, further abstractions and generalisations as in the Polkadot network, or Bitcoin-backed assets, all of which I will discuss below, but not with Bitcoin itself. The constant furore over Bitcoin ‘failing to scale’ obscures a point that has been really been understood in the core Bitcoin community for almost its entire existence. Hal Finney, the legendary cryptographer and cypherpunk who was the second ever miner of Bitcoin and received its first transaction from Satoshi, gave what really ought to have been the final word on this in the Bitcoin forum in 2010:
“Actually there is a very good reason for Bitcoin-backed banks to exist, issuing their own digital currency, redeemable for Bitcoins. Bitcoin itself cannot scale to have every single financial transaction in the world be broadcast to everyone and included in the block chain. There needs to be a secondary level of payment systems which is lighter weight and more efficient. Likewise, the time needed for Bitcoin transactions to finalize will be impractical for medium to large value purchases.
Bitcoin backed banks will solve these problems. They can work like banks did before nationalisation of currency. Different banks can have different policies, some more aggressive, some more conservative. Some would be fractional reserve while others may be 100% Bitcoin backed. Interest rates may vary. Cash from some banks may trade at a discount to that from others.
George Selgin has worked out the theory of competitive free banking in detail, and he argues that such a system would be stable, inflation resistant and self-regulating.
I believe this will be the ultimate fate of Bitcoin, to be the “high-powered money” that serves as a reserve currency for banks that issue their own digital cash. Most Bitcoin transactions will occur between banks, to settle net transfers. Bitcoin transactions by private individuals will be as rare as … well, as Bitcoin based purchases are today.”
While I think Finney was mostly directionally correct, the picture will likely become far more complicated than what he imagined here, due to a combination of both higher ‘layers’ of Bitcoin and interoperability with other protocols, which I discuss below, and the possibility of integrating Bitcoin into FX markets to serve a range of business needs.
FX is a gigantic industry that isn’t necessarily cheap. Common pairs such as Dollar to Pound have very liquid markets and very tight spreads (for trade participants, but not even necessarily for consumers) but to consider an extreme example, moving Indonesian Rupiah into Peruvian Sol will likely be very expensive and may invalidate the business case behind the desired move. The more contrived the example, the longer it will take, also. Were both Bitcoin and a range of local fiat exchanges to be liquid enough, this would be far preferable for almost every FX transaction imaginable, possibly only excluding the interchange of Dollars, Pounds, Euros, and Yen. The reason is simple: it rarely takes more than one hour to transact Bitcoin, and is often more like 10–15 minutes. Also, the cost is utterly negligible compared to FX, and is actually regressive: miner fees (if they exist at all) are determined by how congested each block is with the data of individual transactions, which is unrelated to transaction value. And notice that volatility doesn’t matter either: only market liquidity does. Even Bitcoin is not volatile enough to create an exposure risk over the space of 15 minutes, and it will become less so the more it is used as a kind of meta-currency or settlement-commodity (or however else it helps to conceptualise it) rather than a speculative asset. What matters far more is that there are adequately liquid exchanges in the relevant currencies. If there are several markets between Bitcoin and the Dollar, and several more between Bitcoin and the Rupiah and the Sol, that are deep and liquid enough to prevent any arbitrage triangles emerging, then the problem should be solved. What would stymie this would be dramatically different exchange rates for Bitcoin in different exchanges such that value couldn’t really be transferred in the first place — but volatility is largely irrelevant.
This isn’t necessarily an argument in favour of Bitcoin appreciating, since the holding period I am stipulating is only as long as it takes to receive a transaction and flip it back to fiat. However, what would be really interesting is if an equally deep and liquid industry in Bitcoin futures developed, with the notional posted in fiat. What this would mean is that there would then be a use case to hold Bitcoin on the balance sheet of a company that expects to have to do a lot of FX trading or cross-border fiat settlement, especially that cannot be predicted with any precision. The likely volatility absent any futures would make this an extremely risky idea, but with a futures market, a company could maintain a float of Bitcoin that is fully hedged to their preferred fiat, so that the process of engaging in FX and settlement is sped up and cheapened even further. You would never need to rely on fiat exchanges potentially being inaccessible when you need them most; you tap directly into the Bitcoin network, and only return to the fiat exchange when convenient. Most excitingly of all, this market would probably make a lot more sense as part of a prediction market, itself based on another smart-contract platform blockchain, than it would if run out of an investment bank’s prop trading desk. We then come back to familiar questions of which system is more trustworthy, and how valuable it is to have a counterparty for legal reasons, etc.
On Prediction Markets and Blockchains
Why are prediction markets so accurate, why do they lend themselves to blockchain, and what does blockchain do for…
medium.com
Image for post
photo by Tim Evans, via Unsplash
Banking
The final tumble down the rabbit hole gets us to Bitcoin backed banks. (but if the rabbit hole is a fractal, is there ever a final tumble? anyway …) If you have a global settlement layer with highly liquid markets, then why not hold this asset in reserve and issue digital cash against it? Such digital cash might not even need to be blockchain-based, since you get the trust benefits from the Bitcoin the bank holds in reserve; you should be able to know the bank has adequate capital because you can check the blockchain, and you can redeem it whenever you like. Or maybe you can’t because you don’t have a demand deposit, but you can enter some kind of smart contract as to what exactly you can do with your savings and how you are rewarded for lending your capital. We get the blooming of a thousand flowers in banking experiments contrary to fractional reserve: entrepreneurs can actually try something different and see how the market reacts rather than just the occasional academic whining about it. Again, not predicting this will happen, just that it will be possible.
Bitcoin backed banks are worth pondering for a little longer, as both their risks and potential strike me as being widely misunderstood. Starting from first principles, there are two separate risks in running a bank, and most cryptonerds only seem to be concerned with one. A bank, as opposed to just a depository institution, is necessarily an asset manager that succeeds on the basis of directing capital towards profitable enterprise (this direction may be extremely indirect, but even mortgages rely on this happening somewhere in the monetary ecosystem) The risk managed by the reserve ratio is simply that the bank screws up the promises regarding liquidity made to the loaners of funds in the process of maturity transformation — in other words that they misjudge the true maturity of liabilities. The reserve is a buffer against that happening, but is a distinct concern from the risk of making bad loans — in other words that they misjudge the true quality of assets. Another conceptualisation of the difference is the risk of badly managing working capital as opposed to invested capital, or liquidity as opposed to solvency. You can take your pick.
The liability maturity risk is presumably greatly improved upon by Bitcoin due to its auditability. This seems to be well understood and has been interestingly explored. But the asset quality problem seems more pertinent to the concept of an entirely new kind of money and bank, whereas a lot of hardcore Bitcoiners seem to mistake the second risk for the first and misunderstand both risks in the brave new world. In a sense a wallet is a depository institution, so if you want to avoid illiquidity from the liability maturity risk, you can, which you can’t really do with regular money unless you hide it under your mattress. That’s one of the serious problems of being forced to live within an opaque and corrupt financial system; you are forced to shoulder that risk whether you want to or not, and of course the existence of ‘lenders of last resort’ makes it even worse.
In cryptoland, this problem is naturally avoided because the ‘money under the mattress’ situation is not weird at all. If anything, it is the natural state. But the fallacy here is assuming that the removal of the liability maturity risk via auditability immediately translates to the removal of the asset quality risk too, which it does not. If the bank makes enough bad loans (interestingly this quantum is determined by what it would take to wipe out the reserves, so the risks are related, just in a subtler way than is commonly understood) then it doesn’t matter how auditable everything is — the depositor is not getting anything back. It won’t matter whether it’s gold or Dollars or Bitcoin or magic internet money backed by gold or Dollars or Bitcoin or whatever. If it’s really a bank and not just a depository institution, and enough loans go bad, then the money is gone.
So that’s the risk, but there are opportunities too. To the best of my (admittedly limited) knowledge, the furthest this idea really gained traction was with the distinction between a checking and savings account, but even that difference is mostly trivialised by having money that is basically exclusively digital anyway. Regardless, you could have a structure whereby there are different classes of deposits, or perhaps the nature of the deposits depends on some parameter (the auditable reserve ratio being an obvious contender) It could also be the performance of the loans; you could get transparency on where exactly your funds have gone (or it’s a choice as a depositor as to what class of savings product you take) and both your access to the funds and your interest is somehow programmatic, or dynamic. Really, it could be whatever conceived of reason makes the bank function better, or more appealingly given different customer profiles. This seems to me to be the really intriguing part of Bitcoin backed banks.
For Bitcoin maximalists, this line of thought can even be framed in a way that implicitly mocks the more delusional CS types who have promised us the world with their ‘Bitcoin + X’ contrivances. What many of these amount to is just financial engineering via software engineering. More advanced, transparent, and democratic financial engineering than any investment bank ever provided, but financial engineering nonetheless. Whereas you need actual economic productivity for this to ever matter, for which sound money certainly helps. Keynes had a line that reflected this well,
“Of the maxims of orthodox finance, none, surely, is more anti-social than the fetish of liquidity, the doctrine that it is a positive virtue on the part of the investment institutions to concentrate their resources on the holding of ‘liquid’ securities. It forgets that there is no such thing as liquidity of investment for the community as a whole.”
Despite being highly questionable on economics, Keynes had a remarkable intuition for finance. Liquidity means nothing if the liquid asset doesn’t contribute to economic productivity over at least the term of the debt that financed it, and preferably much longer, which is something a system of Bitcoin-based banking might materially enhance …
Image for post
Photo by Rafael Cerquiera, via Unsplash
Bitcoin
The core thesis behind these speculative ideas is that there are no necessary or sufficient criteria for ‘money’. As I alluded to above, anything that enhances the ability to create and circulate universal credit will do. There is no need for maximalism when we can observe what seems to work following countless independent experiments. If you wanted a slogan for this, how about, ‘unbundling money’, or ‘decentralising capital’? If the functions I suggest, or any others, come into existence, it will not be precisely because, Bitcoin is better money, but because Bitcoin introduces desirable and entirely novel features into the process of storing and transferring value, which can then be used to create credit. Bitcoin cannot transact instantly, cannot support more than around 7 transactions per second (averaged over the settlement period), cannot be reclaimed in cases of fraud, and can’t really be used to buy much stuff at all, at least currently. Fiat currency on existing payment rails can. But fiat currency (over any payments rails) cannot be sound money, cannot be guaranteed to always be online, cannot be transferred for free, cannot be programmed, cannot be audited, and if online cannot be permissionless. Bitcoin can.
With all this in mind, I will briefly cover two blockchain projects that have the potential to extend the capabilities of Bitcoin and, implicitly, any other robust public blockchain: The Lightning Network and The Polkadot Network. Bitcoin has almost certainly won the race to be sound money. Nothing truly ‘competes’ with it. But it also need not exist entirely on its own. Just as nobody gets excited bouncing packets around the network layer of the Internet, but really enjoys watching Netflix, Bitcoin will have truly succeeded when you have no idea you are using it. And so, the most important thing to take from this discussion is not an endorsement of Polkadot or Lightning specifically or exclusively, but to get the reader thinking about the broader concept of layered and interoperable protocols, of which there are - and will be - many. I only mention Lightning and Polkadot because I know the bare minimum about each to say something sensible. Apologies if it’s still questionable …
The Lightning Network is what has come to be known as a ‘layer 2’ protocol, in that it sits ‘on top of’ Bitcoin in a more or less metaphorical sense. I won’t go too far into the technical details here but what this means is that Lightning is a peer-to-peer network of Bitcoin transactors, whose transactions are not being recorded in the Bitcoin blockchain but which are subject to a cryptographic system enforcing eventual settlement in the blockchain. The goal of the project is to get around Bitcoin’s ‘scaling problems’ without corrupting the Bitcoin protocol itself. It is early days, but transactions on the Lightning network appear to be instant, basically free, and scale well with the size of the network. The networks runs on a rather ingenious incentive system that allows honest and cooperative parties to continue to transact off the blockchain indefinitely, but for dishonest parties to be punished by a financial loss that is settled on the blockchain immediately. Counterparty risk is completely removed by all parties staking collateral that they will programatically lose if they lie.
This may sound too good to be true, and in a sense, it is. There are two enormous caveats relating to any real-world application. The first is that the service is clearly only as useful as Bitcoin itself. In addition to the technical issues with scaling, another obvious reason people don’t regularly transact in Bitcoin (although some do) is the volatility of the price relative to fiat. Lightning solves the key technical problem with transacting in Bitcoin, but not the key financial problem. If anything, it might make it worse, as the second caveat is that involvement in the network requires placing some amount of Bitcoin in a kind of cryptographic custody — ideally slightly larger than the maximum expected net negative balance of the participant at any single moment during the period of participation. This both increases the exchange rate risk — which, recall from above, didn’t originally exist for many uses cases of Bitcoin as a currency proxy — and creates a potentially enormous working capital drain on any business wanting to implement this payments channel. Perhaps weirdly, it is not a zero-sum working capital drain across the economy; one participant’s accounts receivables are not another’s accounts payable. Everybody has accounts receivable from having sunk collateral into the Bitcoin blockchain to enable the incentive mechanism that prevents them from interacting with the network dishonestly. In summary then, nearly free and instant payments, but for a different kind of price.
Consider, however, that this price may very well be worth paying if it enables behaviour not previously possible. Who would want to transact for free? We don’t really know because it has never been possible to send less than around $10 without the fee being an exorbitant portion of the transaction. In mimicking tipping at the very least, online micropayment ecosystems could enable fairly large markets, or expand already large ones. Who would want to transact instantly? Visa allows between 40 and 60 thousand transactions per second. Bitcoin allows 7. Lightning allows billions. To ask a better question, then, who would want to transact billions of times per second? Machines. This is a whole other (probably fractal) rabbit hole that I will leave it to the reader to go down on their own if they so desire. But as Andrew Miller of the ZCash foundation put it,

Image for post
The Fractal Rabbit Hole of Bitcoin. Great idea by Miles Suter. Not so great graphic design by me.
Who wants to transact instantly and for free? Well, the W3 Consortium abandoned an effort in the mid-90s to extend HTTP to enable Internet native payments — I wouldn’t be at all surprised if this is revived if or when Lightning proves it can scale.
Polkadot is an interchain protocol, among other things enabling interoperability between blockchains. They refer to this as a ‘heterogeneous multi-chain framework’, which intriguingly ought to work for blockchains of all kinds: public, private, whatever Libra is, or some new thing not yet invented. The obvious analogy is between intranets and the Internet, with Polkadot providing a kind of universal data transfer API (I’m not sure how wedded I am to this analogy, but for those familiar with it, Polkadot strikes me as very similar to Mulesoft, but open and public, rather than within an organisation, and for all manner of blockchains) The functioning of this communications layer abstracts away from the conceptualisation I put forward here of the transferable data on a blockchain constituting a balance exchanged for a computational service, to the idea of a ‘message’, which is a data transfer of any kind between blockchain nodes. This may or may not be a token transfer. Furthermore, the transfer may be between wallets (or contracts, or however they are stylised) on different blockchains. In fact, Polkadot encourages this. I mentioned above that Bitcoin is ‘programmable to a small degree’. It is not worth explaining exactly why or how this is the case — although actually the small degree to which it is the case is what lets Lightning work — but an exciting implication of Polkadot is that it really needn’t be at all; the programmability can exist somewhere else, on some other blockchain, and tied to Bitcoin via Polkadot.
The implication is that novel ideas around the utility of markets for scarce data need not come in the shape of endless fully formed decentralised computers that really only exist for one specific task. They can be far lighter, but if they require a store of value, they can tie in Bitcoin; if they need free and instant payments, they can tie in Lightning; if they need smart contract execution, they can tie in Ethereum, Tezos, EOS, etc. An analogy to cloud computing is apt. If you have an idea for an app, you may choose to let AWS deal with the infrastructure of storage and compute, within which you can run Kubernetes and Docker; you can let Stripe deal with payments, which you can implement directly, or perhaps go through Wix, in which case Stripe and AWS may well be working in the background; you can build your front-end store on Shopify, or maybe the whole thing, in which case Shopify will do all of the above for you, and so on and so forth, up and up the interlocking layers. The situation in cryptoland is not quite as generous, in that the services you need are not guaranteed to exist, or if they do exist, they are not guaranteed to be effective or robust. But Polkadot will hopefully at least let you utilise them extremely easily.
I find this particularly exciting for Bitcoin — and the idea of money and banking in general — because of what money means: universal credit. Almost any activity can be designed to have a monetary component, which is really only to say that people value the time devoted to their labour, while others value the product of that labour, very probably in the form of capital that will multiply their labour, and so on and so forth, up and up the interlocking layers. Therefore, Bitcoin — the most secure form of value settlement ever invented — and Lightning — which builds on top of this layer to provide free and instant transfer of that value — can potentially be used in combination with Polkadot to provide either a value-storage or payments functionality to any kind of wonderful, free and open source, new kind of computer, decentralised corporation that can be imagined:
The Conceptual Blockchain
blockchains are combinations of three concepts: a new kind of computer, an open source software project, and a…
medium.com
Image for post
Photo by Con Karampelas, via Unsplash
Libra
Of course, this all brings us to Libra. I have three main points to make in order to adequately compare Libra to money, banking, and Bitcoin. We might call them the good, the bad, and the ugly, although unfortunately I won’t treat them in that order. The bad is that the Libra data structure is a database, not a blockchain, and the Libra consortium is a hedge fund, not a network of nodes. The good is that Libra will acclimatise billions of people to digital bearer assets, and may be a force for great social good in the short run. The ugly is that it will be a force for great social evil in the long run.
That Libra is not a blockchain is really just a technicality, but it is worth disabusing anybody who has been fooled by clueless journalists. Libra is a distributed ledger that is an attempt to mashup the most palatable parts of Bitcoin, Ethereum, and Ripple, but none of the parts that make them truly revolutionary. It is very technically interesting, and if it works, it will be an incredible technical achievement, but it is not a blockchain. This matters for more than linguistic reasons; the Libra data structure may be open and may be private, but will definitely not be neutral or permissionless, and the tokens will not be sound. This wouldn’t be worth stressing so much if both the official and technical white papers didn’t constantly misuse the words ‘blockchain’ and ‘cryptocurrency’. After each of the following extracts, I provide a translation,
Image for post
“Libra is a permissioned database. We will think really hard about how to transition it to a permissionless database but unfortunately we don’t really like the only known way to do that.”
And,
Image for post
“There are some really difficult unsolved problems in the theoretical underpinnings of scaling open blockchains. We also don’t know how to solve them.”
And,
Image for post
“Just to be extra clear: the Libra blockchain is a database of validator-signed ledger states with a Merkle tree of the historical states - not a blockchain.”
Given Libra the data structure is not a blockchain, we must then wonder what the Libra consortium is, given it is clearly not a network of nodes. A collection of transaction validators is accurate enough, but a little dry. It is a lot more revealing to describe it as a hedge fund.
The way it looks like the Libra ‘token’ will come into existence will be in exchange for deposits from users. You will send the consortium fiat over existing payment rails, and they will mint some ‘Libra’ and give it to you, and you can cash in your Libra for fiat and they will ‘burn’ the fake money and return your fiat (the feature of having different names for the data structure and the tokens is not one of the better parts of other blockchains implemented here). The ‘nodes’ are really processing centres, in that they need to contribute a minimum of computing power to handle the transactions being submitted. It all sounds very communitarian until you realise that what is in it for them is interest on the deposits of real assets ‘backing’ the digital assets issued. In order to maintain price stability, these deposits will be invested in the government bonds of the fiat currencies against which Libra is desired to be stable.

“How about a corporate haggis that is pretending to be an open haggis?” — Andreas Antonopoulos in Edinburgh, 19/6/19, the day after the release of the Libra white paper.
This is worth pondering as it is really quite incredible. Libra is going to have zero cost of capital on funds it will lend at the risk-free rate. Despite strictly speaking being total nonsense, the ‘risk-free rate’ ought to be the lowest rate it is possible to borrow at, hence governments borrowing at this rate and not an even lower one. Because Libra has an even lower borrowing cost (none), it can lend at the risk-free rate and earn an arbitrage profit on what will almost certainly be the largest pool of capital ever collected by a corporation. In the above vein of banking theory, it is worth considering that Libra will only need petty cash / liquidity / working capital / however you want to conceptualise it, of the most extreme net negative redemption of Libra to fiat, multiplied by the settlement period of government debt, which in most cases is one or two days. This will almost certainly be utterly trivial compared to the market valuation of minted Libra at most times, and given the intention to charge transaction fees, may actually be completely irrelevant since fees can be dynamically matched to real time outflows even while remaining miniscule. So Libra will be an almost artificially highly leveraged hedge fund. What’s more, it will be a perfectly safely leveraged one, because the assets will be both the highest quality in existence and perfectly liquid. Neither banking risk will exist. This is astonishing.
How it achieves this hedge fund like status is worth exploring because it is the source of both the great social good and great social evil that will likely follow — assuming it works, or is allowed to work. My hunch is it won’t be allowed to work at all, so I would take much of the juxtaposed utopianism and dystopianism below with a pinch of salt.
Every Libra bought will either represent a Dollar/Pound/Euro/Yen given to Libra and invested in government debt denominated in those currencies, in which case who cares, or it will be something else, in which case things get very interesting. A WhatsApp user will transfer their Indian Rupee, let’s say, to Libra in exchange for digital money. Libra will then sell Rupee for Dollar on the FX market to gain the fiat to back the Libra. This will cause the Rupee to depreciate relative to the Dollar/Pound/Euro/Yen, making it more difficult to raise capital in Rupee and easier in Dollars, making Libra even more viable as a medium of exchange, on top of the worldwide networked marketplace in which it is already exclusively accepted by fiat. The role Libra will be playing is the FX broker-dealer that ‘dollarizes’ emerging markets and immediately provides an economy in which the the hybrid Dollar/Pound/Euro/Yen can be spent.
This could initially be a great social good, for three reasons. Firstly, we should not underestimate the dramatic difference this could really make to the billions of unbanked around the world who can afford a phone but not a bank account — and the hundreds of millions more who have bank accounts that achieve nothing given their monetary wealth is consistently inflated away. Additionally, the smart contract elements of Libra could allow for programming of cross border business logic that would previously have been impossible due to combinations of illiquidity, inflation, and capital controls. Facebook’s rhetoric around empowerment, while suspicious to the point of hilarious given its coming from Facebook, is probably entirely accurate in this case. This could be tremendously beneficial to those living in monetary regimes that are inept, corrupt, or both.
Secondly, Libra is arguably a necessary experiment in the development of the banking of digital assets. It is a simple and natural step to first trial a digital asset backed by fiat that, however philosophically flawed, is actually used as money currently. There are fewer degrees of freedom than a bank of a novel digital money backed by Bitcoin, and yet the lessons learned will obviously be relevant, be they technical, economic, or social. This will be truer the more genuinely open Libra turns out to be, since the experiment will not be of the viability of Libra and banking of digital assets alone, but of every other open system that connects to it to incorporate Internet-native money, contracts, and so on. Libra will be psychologically safer to build on to begin with, but via the likes of Polkadot will open the door to Bitcoin, Ethereum, and more.
But the third and most important reason is that in addition to developers and entrepreneurs, Libra will acclimatise billions of regular people to digital bearer assets. Minds.com founder Bill Ottman put it well in a recent interview, “it’s not Bitcoin, it’s not Ethereum, but maybe it’s a weird bridge? It’s a weird bridge which you don’t necessarily know whether or not it will collapse as you are walking over it.” The acclimatisation will be particularly important when the dream of dollarized digital money collapses into the nightmare of corporate neo-feudalism. Some readers may have winced at my positive invocation of ‘dollarization’, given its connotations of monetary imperialism. They would have been right to do so had they thought my enthusiasm was unequivocal. But notice I only ever said ‘could’, not ‘will’. This could be a great social good, but it will likely devolve into a great social evil. If you think the monetary imperialism of the United States of America is bad, wait until you see the monetary imperialism of a corporation that actually makes a profit.
If you believe that Facebook will never use your activity with Libra to better serve you ads, you are delusional. They won’t do it right away, for sure. They said so in the white paper. But there is absolutely nothing about this technology that enforces this promise. It’s a promise from this man:
Image for post
n.b. this is real, not a joke or a fake. see here for more.
What is particularly perverse is that Facebook has a legal obligation to its shareholders to follow this path. The board of directors will be failing in their fiduciary responsibility if they do not encourage Mark Zuckerberg to direct Libra to behave in this way. Which, of course, he can. Libra is not an open, permissionless, neutral, private, sound money like Bitcoin. It is corporate money. It will work better than government money but it will turn out to be even more insidious. If you are actually adding value with your service relative to a useless competitor your customers previously had no choice but to use, you generate an enormous amount of goodwill you can later rapaciously exploit.
Which means there will be mass surveillance and data leaks. Even without leaks there will be deanonymization of the transactional graph. There will be purges, and censorship, and confiscations of wealth. Facebook will control enough economic activity to dictate monetary policy to economically weaker nations. This won’t be in the form of direct confrontation — it will be a system upgrade that optimises something or other that within a few days sees yet more value sucked into lowering the cost of funding the governments of the largest economies in the world — those that have meaningful power over Facebook, the corporation — and a few days after that the power of every other government to affect the economic goings on within their own borders. Shades of this may sound ideal and romantic, but this is not a stripping of the power to interfere with the activity of willing individuals — it is a transfer of that power to Silicon Valley.
Much of the above few paragraphs consist of the worst possible dystopian outcome. I seriously doubt anything like all of this will happen in its entirety, but there will come a point when it becomes obvious that it could happen. The steps to roll back Libra’s power to ensure that it doesn’t happen will not be pretty. And the fallout will see a great many disillusioned people turning to money that is open, permissionless, neutral, private, and sound.
Which is what we wanted all along. ''',

                '31': '''This is Water
April 17, 2019 | Ben Hunt | 16 Comments | Note

58+
PDF Download (Paid Subscription Required):  This Is Water


There are these two young fish swimming along and they happen to meet an older fish swimming the other way, who nods at them and says “Morning, boys. How’s the water?” And the two young fish swim on for a bit, and then eventually one of them looks over at the other and goes “What the hell is water?”

David Foster Wallace (2005)
It’s the perfect description of a Zeitgeist … the water in which we swim.

We can’t see it. We can’t hear it. We can kinda sorta feel it, if we focus really hard, but only kinda sorta. All the same, because it’s part of a social system and not a physical system, WE create it. Not in a conscious fashion. We can’t set out to create a Zeitgeist.

But we can be nudged.


It’s like a stadium crowd holding up cards for the TV audience. They can’t see the picture they’re making … they have no idea what it looks like or what their role in its making might be. But they’re told/asked to do it. So they do.

THIS is a Zeitgeist.

What’s the matter, Ben? You got a problem holding this card up over your head? It’s for the troops. You support the troops, don’t you? Don’t you?

Yes, I support the troops. And yes, I have a problem with this.

Why? Because I don’t trust the State and the Oligarchy to use the common knowledge of “support for the troops” – the crowd watching the crowd express a public act of allegiance to the military, so that everyone knows that everyone knows that yes, it is right and proper to support the troops – for the right reasons.

Instead, I suspect that they will use my voluntary “support” (hey, no one forced you to hold up that card) to justify things like … oh, I dunno, a trillion dollars wasted and 2,000 kids dead to fight a war in freakin’ Afghanistan. Because, you know, otherwise “the terrorists win”. Otherwise we lose “credibility”. JFC.

It’s exactly the same thing with capitalism.
In exactly the same way that all of us sit in our citizenship stadium and get nudged to hold up a card creating a common knowledge display of “Yay, military!”, so do all of us sit in our investor stadium and get nudged to hold up a card creating a common knowledge display of “Yay, capitalism!”.

What’s the matter, Ben? You got a problem holding this card up over your head? It’s for capitalism. You support capitalism, don’t you? Don’t you?

Yes, I support capitalism.

AND I have a problem with holding up this card.

You should, too.

Because we can’t trust the State and the Oligarchy to use our support for the right reasons.

In You Are Here, I wrote that the investment Zeitgeist is changing in three ways.

Deflationary expectations, now 40+ years old, are becoming inflationary expectations.
Cooperative and multi-play games in both international politics and domestic politics, now 70+ years old, are becoming competitive and single-play games.
Modern capital markets, now 150+ years old, are becoming political utilities.
Time to add a fourth.

Capitalist productivity, now 200+ years old, is becoming capitalist financialization.
What is financialization?

Financialization is profit margin growth without labor productivity growth.

That sounds like a small thing, but I tell you it is EVERYTHING.

Financialization is squeezing more earnings from a dollar of sales without squeezing at all, but through tax arbitrage or balance sheet arbitrage.

Financialization is the zero-sum game aspect of capitalism, where profit margin growth is both pulled forward from future real growth and pulled away from current economic risk-taking.

Financialization is the smiley-face perversion of Smith’s invisible hand and Schumpeter’s creative destruction. It is a profoundly repressive political equilibrium that masks itself in the common knowledge of “Yay, capitalism!”.

Financialization is a global phenomenon. In China, it’s transmitted through the real estate market. In the US, it’s transmitted through the stock market.

Financialization is the zombiefication of an economy and the oligarchification of a society.

Here’s the foundational chart for these strong words.


source: Bloomberg
This is a 30-year chart of total S&P 500 earnings divided by total S&P 500 sales. It’s how many pennies of earnings S&P 500 companies get from a dollar of sales … earnings margin, essentially, at a high level of aggregation. So at the lows of 1991, $1 in sales generated a bit more than $0.03 in earnings for the S&P 500. Today in 2019, we are at an all-time high of a bit more than $0.11 in earnings from $1 in sales.

It’s a marvelously steady progression up and to the right, temporarily marred by a recession here and there, but really quite awe-inspiring in its consistency. Yay, capitalism!

It’s a foundational chart for this note because I believe that the WHY of earnings margin growth in the 1990s and early 2000s is fundamentally different than the WHY of earnings margin growth since then.

WHY do we get three times as much in earnings out of a dollar of sales today than we did 30 years ago, and twice as much than we did 10 years ago?

The common knowledge answer is technology!.

By which I mean that the common knowledge answer is the meme! of technology as opposed to any actual technology. By which I mean that we can’t exactly say why technology would improve earnings margins and efficiency over the past decade, but we believe it MUST be technology. Somehow. Of course it’s technology. Everyone knows that everyone knows that it’s technology that makes anything in the world more efficient. So we mumble something-something-technology whenever anyone asks a question like this. And yes, This Is Why We Can’t Have Nice Things.

Here, hold this card up over your head. It’s for technology and progress. You support technology and progress, don’t you? Don’t you?

I used to believe this, too. I used to believe that corporate management was getting better and smarter over time, that they were making constant process improvements and technology-based productivity enhancements to squeeze more and more profits out of the same sales dollar.

And I think this used to be true. I think that during the 1990s and early 2000s – the so-called Great Moderation of the Fed’s Golden Age – when we actually had significant advancements in labor productivity year after year after year, corporate management was, in fact, able to drive earnings margins higher for the right reasons. I think the driver of profit margin growth over this period was actual technology, as opposed to the meme of technology!.

But I don’t believe this is true anymore. I don’t believe that technology and productivity advancements have been responsible for earnings margin improvements for the past decade … for some years before the Great Financial Crisis, in fact.

Here, take a look for yourself.

See, the Fed was convinced that an easy money policy would lead to corporate management investing more in technology and plant and equipment … you know, all of those things you need to drive productivity. All of those things you need to drive a 1990s style recovery, with earnings margin accretion for the right reasons.

Instead, corporate management followed the Zeitgeist.

They always do. It’s the smart move.


This is a chart of Labor Productivity growth in the US for the past 30 years. It’s how much more stuff we make or services we provide from a unit of labor. It’s how much we’re growing for the right reasons, by applying capital investment in plant and equipment and technology to work smarter and more efficiently. It’s how we generated earnings efficiency and margin growth for the right reasons in the 1990s and early 2000s. It’s how we’ve been reduced to squeezing tax policy and ZIRP-supported balance sheets for earnings efficiency ever since.

This chart IS the failure of monetary policy for the past decade.

This chart IS the zombiefication and oligarchification of the US economy.

Why do I rail at the Fed? THIS.

Trillions of dollars in QE, and all we got for it was this lousy t-shirt. Yes, I’m going to get this productivity chart put on a t-shirt.

The reason companies aren’t investing more aggressively in plant and equipment and technology is BECAUSE we have the most accommodative monetary policy in the history of the world, with the easiest money to borrow that corporations have ever seen. Why in the world would management take the risk — and it’s definitely a risk — of investing for real growth when they are so awash in easy money that they can beat their earnings guidance with a risk-free stock buyback? Why in the world would management take the risk — and it’s definitely a risk — of investing for GAAP earnings when they are so awash in easy money that they can hit their pro forma narrative guidance by simply buying profitless revenue? Why in the world would companies take any risk at all when the Fed has eliminated any and all negative consequences for playing it safe?

That’s from Gradually and Then Suddenly, written in July 2017. It’s worth your time.

What’s changed since I wrote that note is that the barge of monetary policy, both in the US and everywhere else in the world, has done a 180 and is now chugging back down the easing river. No central bank in the developed world is looking to tighten today, and if anything we’re on the cusp of fiscal policies like MMT, or at least trillion dollar deficits forever and ever amen, to accelerate the shift in the modern Zeitgeist towards fiat EVERYTHING.

This is not a mean-reverting phenomenon.

This doesn’t get better going forward. It gets worse.

But wait, there’s more …


source: Bloomberg
This is a chart of the S&P 500 price-to-earnings ratio in yellow, the belle of the narrative ball, together with its forgotten cousin, the price-to-sales ratio in blue.

When we grow profits through productivity growth – when our “supply” of earnings is directly connected to the same operations that generate sales – P/E and P/Sales multiples go up and down together. When we extract excess earnings through financialization – when our “supply” of earnings increases for no operational reason connected with sales – the P/E multiple becomes depressed relative to the P/Sales multiple. As the kids say, it’s just math.

Why is this important? Because a P/E multiple deflated by financialization doesn’t mean what you think it means.

How many times in the past ten years have you heard that the market is not expensive on a valuation basis? And what you’ve heard is right, as far as it goes.

Because the market narrative of valuation is completely dominated by the vocabulary of earnings, not the vocabulary of sales.

Sure, the S&P 500 P/Sales ratio is near an all-time high, but who cares about that? The S&P 500 P/E ratio today is right at 19 … neither crazy low nor crazy high … and we ALL care about that. But here’s the thing:

Without financialization, my guess is that the S&P 500 P/E ratio today would be 28.

Good luck selling that to a value investor, Wall Street.

Here, hold this card up over your head. It’s for value and a reasonable earnings multiple. You support value and a reasonable earnings multiple, don’t you? Don’t you?

But wait, still more …


source: Bloomberg
This is a chart of S&P 500 buybacks per share (in blue) imposed over the ratio of S&P 500 earnings-to-sales in green. You’ll see that share buybacks spike after profit margins spike. You’ll see that share buybacks spike before and during recessions.

When do stock buybacks accelerate dramatically?

In 2006 and 2007, when management is rolling in record profits and profit margins, despite meager productivity growth.

In 2018 and 2019, when management is rolling in record profits and profit margins, despite meager productivity growth.

This is not an accident.

Here’s the past five years so you can see the temporal relationship more clearly.


source: Bloomberg
Stock buybacks are what you DO with the excess earnings you’ve made from financialization.

Why? Because stock buybacks are part and parcel of the financialization Zeitgeist. They’re part and parcel of the tax-advantaged issuance of stock to management, which is then converted into tax-advantaged income for management through stock buybacks.

Here, hold this card up over your head. It’s for alignment of interests between management and investors. You support alignment of interests between management and investors, don’t you? Don’t you?

What does Wall Street get out of financialization? A valuation story to sell.

What does management get out of financialization? Stock-based compensation.

What does the Fed get out of financialization? A (very) grateful Wall Street.

What does the White House get out of financialization? Re-election.

What do YOU get out of financialization?

You get to hold up a card that says “Yay, capitalism!”.

So what do we DO about this?

I’ve got three answers, one for your life as an investor, one for your life as a citizen, and one for your life as a human being.

As an investor, my answer is this: Adapt.
How? First read this.


And then take this to heart.

What are the Narratives I am being told?
What are the Abstractions presented to me?
What are the Metagames I am playing?
What are the Estimations shaping my outcomes?
Am I acting to promote Reciprocity?
Am I acting in a way that reflects my Identity?
Why? Because Clear Eyes, Full Hearts, Can’t Lose.
As a citizen, my answer is this: Resist.
How? First read this.


And then take this to heart.

Take back your vote.
Take back your distance.
Take back your data.
As a human being, my answer is this: Find your pack.
We’re all little fish.

We’re all swimming in the same smiley-face authoritarian waters of “Yay, military!” and “Yay, capitalism!”.

I tell you, brothers and sisters, we’re all we’ve got.

But I also tell you, we are all we need.

Yours in service to the pack. – Ben ''',

                '32': '''Understanding the Blue Church
Jordan Hall
Jordan Hall
Follow
Mar 30, 2017 · 20 min read



In my Situational Assessment: 2017, I quoted a post from Reddit:
“The Blue Church is panicking because they’ve just witnessed the birth of a new Red Religion. Not the tired old Christian cliches they defeated back in the ’60s, but a new faith based on cultural identity and outright rejection of the Blue Faith.” — /u/notjfao
A number of folks noted that they were not familiar with the concept of the Blue Church and wondered what was meant by it. The Democratic Party? Liberalism? Progressivism? As I mentioned in SA:2017, I had originally lifted the idea wholesale from that Reddit post with only an intuitive sense that it (and its juxtaposition with a Red Religion) was useful and pointed at something real.
In this essay, I dive into the concept. Below I endeavor to provide an answer that is adequate to Deep Code. I believe that the results are well worth the effort, but this is not a simple journey. Few things of importance these days are. If we want to get to the bottom of the contemporary situation, we are going to have to get comfortable going deep.
The abstract is this: the Blue Church is a kind of narrative / ideology control structure that is a natural result of mass media. It is an evolved (rather than designed) function that has come over the past half-century to be deeply connected with the Democratic political “Establishment” and lightly connected with the “Deep State” to form an effective political and dominant cultural force in the United States.
We can trace its roots at least as far back as the beginning of the 20th Century where it emerged in response to the new capabilities of mass media for social control. By mid-century it began to play an increasingly meaningful role in forming and shaping American culture-producing institutions; became pervasive through the last half of the 20th and seems to have peaked in its influence somewhere in the first decade of the 21st Century.
It is now beginning to unravel.
In part it is unravelling because of developing schisms within its master narrative, the Blue Faith. These are important, but they are not the subject of this essay. In this essay, I am focusing on what I think is both much more fundamental and much less obvious: deep shifts in technology and society that are undermining the very foundations of the Church. Shifts that render the Church itself obsolete.
If you are ready for a deep dive, come on in. The water is warm.
Image for post
Complexity and Control
Yaneer Bar-Yam’s book Making Things Work, does an excellent job explaining the relationship between complexity and the kinds of control structures that we humans build to try and manage that complexity. For those who want to go deeper, I recommend the whole book. The basic idea is actually pretty simple.
Imagine a boat. We are going to row that boat, starting with but one paddle. If you’ve ever learned to canoe, you know that this isn’t simple. There is an art to it. You have to hold the paddle correctly, you have to learn how to put it into the water, how to stroke, how to return. The difference between doing it well and doing it poorly is significant. But, with a little practice, almost everyone can get at least reasonably capable of rowing their canoe.
This is a “management of complexity” problem. The relationship between oar, water, boat and person is complex. All of these systems are feeding back on each other in subtle and hard to predict ways. But the “control capacity” of a standard-issue human is up to the task. The human body, adapted to things like walking upright on two legs and throwing rocks has enough control capacity to manage this level of complexity.
Now add another oar. Generally, even someone experienced with a single paddle takes a little while to get it figured out. In particular, you have to learn how to simplify the problem by constraining some of the degrees of freedom of the paddles. Perhaps you fix the oars to the boat so that they can only traverse a single path. Certainly, you are going to have to make sure that you are paddling both oars in the same rhythm. By getting the oars into “coherence,” you can get the complexity of the problem inside your control capacity.
Coherence is one of the most important concepts in the management of complexity. When you take two systems (two paddles) and synchronize them, you radically simplify the complexity of the overall system. By getting two paddles into coherence, you are able to turn two paddles that you can’t manage into one big paddle that you can manage.
Now add another person to the mix. Side by side — each with one oar. This kicks the complexity up a lot. We are now dealing not only with two oars, we are dealing with two different control structures. And, of course, the only way to get things moving is for the control structures to get into coherence. Fortunately, humans are pretty good at this too. Like dancers or musicians playing together, we have a lot of bandwidth for small group synchrony. Getting into flow together takes some doing, but with a little practice we can manage this complexity.
Now add another ten people into the boat. This is a real problem. The complexity of this overall system exceeds the natural control capacity of “group flow”. Try as you might, it is darn near impossible for a group of twelve people to “self organize” into an effective rowing team.
Unless you put someone in charge.
Add someone to the front of the boat whose job is nothing but synchronizing the whole team (“stroke!”) and reduce everyone else’s job to responding to the signal coming from that leader (“stroke!”) and suddenly the system comes back into control. In effect, you’ve replaced thirteen individuals with one “group of people” and one “leader” in a control hierarchy. This is a radical simplification. As the Greeks and Romans of old discovered, it scales. As long as the people rowing the boat stay inside their box and focus only on doing their job, and as long as the coxswain says in a simple rhythm, you can stack dozens of rowers and get the job done.
Notice what happens here. In particular, notice what has to happen up and down the control hierarchy. The bandwidth (the amount of signal) going up and down the hierarchy has to be extremely simple. (“Stroke!”) Imagine if the rowers had to paddle and converse about where the boat should go. It couldn’t be done. Imagine if the coxswain had to try and control two boats simultaneously. Except in the very rare circumstance that the two boats could be consistently and precisely coherent, it couldn’t be done.
These are the core concepts to understand the Blue Church. The complexity of the system. Our ability to simplify the system. The control bandwidth available to manage the simplified system.
Image for post
The Complexity of Modern Life
In 1860, the population of the United States was 30 million people. Six short generations later, the population had increased tenfold to over 300 million people.
Consider this. For the first millennium A.D., the human population was relatively constant. Over the next six hundred years, it only barely doubled. Then, suddenly, with the beginnings of the industrial revolution it began to take off. By the 20th Century, the rate of growth in the United States (and the world) absolutely skyrocketed. The past 150 years have witnessed an unprecedented explosion of population, and along with that population, an explosion of social complexity.
By any measure of social complexity, the transition from the 19th to the 20th Century was extraordinary. For the first time in human history, the population shifted from a rural to an urban majority bringing the increased pace of life and social interaction that comes with big cities. Horses gave way to railroads which were replaced by automobiles and then airplanes — shrinking the world into a single connected meta-community. We went from Darwin first postulating evolution in 1859 all the way to Crick and Watson’s DNA in 1953. We went from the first theory of electromagnetism in 1864 to the actual deployment of the Atomic Bomb in 1945. This was a hell of a century.
And just like in our example of adding a dozen people to our boat, this expansion of complexity created a problem. The forms of social control that had been used to get us to the 19th Century were inadequate to the levels of novelty and complexity of the 20th Century. Society cannot function without a regulatory structure adequate to its level of complexity.
The Blue Church was the emergent solution to this problem.
Image for post
Understanding Media
Technology is not neutral. As Marshall McLuhan wrote, when we innovate technology, “we become what we behold. We shape our tools and then our tools shape us.”
McLuhan’s theories are subtle and powerful. In fact, it is hard for me to imagine anyone being able to navigate the contemporary environment without at least a good grasp of his principles. If you’ve never read his stuff, I recommend Understanding Media: the Extensions of Man.
I’m not going to try and recapitulate McLuhan’s work here. Instead, I’m going to steal some portions of it and recast it in a very different form to make it accessible for our present purposes.
Imagine a landscape of rolling hills. Now imagine rain falling evenly on this uneven ground. What is going to happen? Well, eventually, the water is going to run downhill, gather in the valleys and, depending on the actual shape of the terrain, either form into a flowing river or gather into a lake or pond.
Once you know the “shape” of a particular space and the nature of the forces acting in it, you can make some neat predictions about how it is going to play out. Of course, the future is never locked down. The lake might overflow and transform into a waterfall. A meteor might fly out of the sky and change the shape of the whole space. But, subject to certain constraints, you can predict the future.
Media is like a landscape. The kind of human social dynamics and psychologies that form around an oral tradition are quite different than those that can (and do) form around a literate media.
The 20th Century brought a number of technological advancements. One of the most important was the emergence and development of “mass media.” While the various kinds of mass media (newspaper, radio, television) are different, as “mass” (or “broadcast”) media they share a basic shape: they are asymmetric. One to many. Author to audience. Coxswain to rowers.
Not everyone can get access to the printing press, the radio station or the television broadcast booth. Those few that can are the ones to get to create the narrative. Everyone else is the audience. We read, listen, watch. But not much else. (Actually, we do one very important thing else, but I’ll get to that in a moment.)
The key insight for this post is that as an audience we are coherent. As a mass, we transform from millions of diverse individuals into one, relatively simple, group. So long as we can be maintained in this coherence, we present something that can be managed.
This is the formal core of the Blue Church: it solves the problem of 20th Century social complexity through the use of mass media to generate manageable social coherence.
Image for post
The Formation of Good Opinion
Once you grasp the basic shape of the Blue Church control structure, you begin to see it everywhere. There is a basic bi-directional flow. In the upwards direction there is the flow of “credentialed authority.” The “experts” who are authorized through some legitimizing process to be permitted to form and express their opinions through some form of broadcast media. In the downwards direction, these “good opinions” which anchor and place boundaries around our collective social coherence.
Consider academia. The students are the audience. Their job is to pay attention to the credentialed authority. To listen and watch closely and to learn from the professor the nature of “good opinion” in this particular domain. If they do a good job in this, that is, if they can answer questions correctly according to the authorities’ evaluation process, then they pass. If not, they fail.
While the content matters, the form is crucial. Regardless of the specific subject matter, every class is a lesson in how to play the Blue Church game.
The professors, in their turn, are authorities largely because they did a good job being students and were invited into the authority hierarchy. Here they learned the nuance and boundary of good opinion, the social pecking order (Harvard is at the top thank you) and the ins and outs of being a good expert.
Don’t get me wrong. I’m not saying that the academy is propaganda or bullshit. In fact, in many ways, the opposite. It works. This process of academic credentialization has proven to be a powerful engine for filtering out nonsense and searching for truth. While there have been a lot of digressions (string theory) and inappropriate authorizations (economics), in the main, the 20th Century expertise machine has been the crown jewel of civilization.
What I am pointing to here is the formal structure. Broadcast. Asymmetry. An architecture that enables a scalable division of labor for social sensemaking and decision making. No one could possibly try and understand even a small fraction of what is going on in the world. So we break the problem up into bits, hand the smaller problems up the expertise hierarchy where they are processed and reduced to simple shared “good opinion” which is then broadcast down and out to the whole population.
This gets us good answers to hard problems and, more importantly, gets us all more or less on the same page. And *this* enables us to run a modern society.
For example, imagine what street traffic would look like if everyone had their own opinions about what should happen. Disaster. But as long as we all agree, implicitly and without much consideration, that a red light means “stop” then suddenly millions of people flinging tons of steel about at sixty five miles per hour is manageable.
Similarly, as long as we all agree that “free trade is a good idea”, or that “borders should be protected,” or that “healthcare is a human right,” or that “people should be treated equally,” or that “carbon emissions lead to global warming” then the still enormously difficult job of designing and implementing policies based upon these assumptions and frameworks can be managed and the ship of state moved forward. (“Stroke!”)
Life in the Blue Church
Going deeper, the actual playing out of the Blue Church control structure is influenced by three characteristics of human beings:
We are a pack animal constantly trying to make sure we have high status within the pack;
We have a really hard time distinguishing between “having attention” and “deserving attention;”
We principally learn by doing and emulation (not by thinking).
Image for post
The first characteristic leads to one of the most important reinforcement functions that maintains the Blue Church: social signaling. In Blue Church society, to hold and express good opinion means that you are part of the pack, in the tribe, on the team. Holding and expressing good opinion brings social benefit. More importantly, failing to hold and express good opinion can be ruinous.
This social dynamic means that good opinion is self-reinforcing. There is no need for a top-down thought police or such. Once enough people are coherent around good opinion, natural human social dynamics will kick-in to maintain that coherence.
This one is easy to test for yourself. If you live in any big city in the United States, go to a social gathering and simply express an opinion that is out of line with Blue Church orthodoxy. Then watch closely. Particularly watch the reactions of members of the opposite sex. Pretend that you believe, for example, that climate change isn’t real. Or that Islam or Feminism are dangerous ideologies. What will quite likely happen is that you will be “out grouped.” At a physical level, way below conscious consideration, you will be assessed and found wanting. Not a good mating prospect. Not a good social ally.
Interestingly, this is true largely regardless of where you live in the social hierarchy. Regardless of whether you are a twenty-something just learning how to play the game or a senior expert trading on your good standing, social pressure will provide a strong signal on how to stay in coherence.
After all, if you have worked for decades to achieve a high level of social standing, this is a lot to risk for having bad opinions. Ask Sam Harris and Jordan Peterson and Steven Pinker — all of whom are high experts who have recently begun to find themselves on the wrong side of good opinion.
The downside result of this social reinforcement, of course, is the echo chamber where opinions that violate good opinion are removed from discourse — even when they are valuable and important. And the contemporary Blue Church has definitely developed into an echo chamber. There is always room to play *within* good opinion, of course. In fact, the Church offers a broad menu of good opinions to try on and play with. As long as you play within the coherence of good opinion, you are free to roam. You have the freedom to be Lady Gaga or Taylor Swift. But mind the gap. Social reinforcement has gotten very sensitive in the wake of the Trumpocalypse. If you step on the third rail, you are in for a shock.
Image for post
The Blue Church and Culture
The habit of seeking authority is not merely a product of Blue Church training. It is, in fact, one of the more hard wired aspects of being human. We are a social animal and we are constantly on the lookout for people to watch and learn from. In many ways, this capacity is the “secret of our success” and the foundation of culture itself. However, when we look at our hardwired “attention allocation” functions, we discover that human beings use a pretty simple model: pay attention to the people who other people are paying attention to.
As a society, we are obsessed with who has attention, and conspicuously less interested in whether it is deserved.
Among many things, this deficit leads to the cultural consequence of “celebrity”. Since having attention is hard to separate from deserving attention, simply having the camera pointing at you implicitly confers upon you some of the power and credentials of authority. This is why we find ourselves in the situation where Hollywood entertainers and professional athletes are empowered to steward good opinion far beyond their actual expertise.
In a broadcast world, merely being “on camera” is to be credentialed. Regardless of your actual capabilities, insight, or character, if you can somehow manage to get on camera you are granted actual audience *and* social authority (Kim Kardashian). By contrast, if (for some reason), access to the camera is prevented, withheld or otherwise not achieved, your lack of access results in both lack of practical audience *and* questionable authority — regardless of your actual capabilities, insight or character (Bernie Sanders during the primaries).
As it turns out, this fact played an important role in precisely how the Blue Church came to be, why it ended up allied with the Democratic Establishment and why it chose the particular content of the Faith. More on that in the next post perhaps.
Image for post
Here is the kicker. Being on camera gives you authority even if you aren’t real. This is why pop culture plays such an important role for the Blue Church. Carroll O’Connor was somewhat influential as a celebrity. But his character Archie Bunker lives high in the cannon of the Blue Church. Every week for years, millions of people gave their attention to the Archie Bunker family and tuned in to the social signaling of good (and bad) opinion. At a human level, the signaling was very clear. Even as a young child I could read the signs (and monitor the laugh track). Archie was an archetype of a fading good opinion, rapidly moving out of favor; while the rest of the family represented an emerging good opinion in the process of establishing its position in the social field.
Yes, we humans can discern between real people and fictional characters. But the importance of pop culture in the operations of the Blue Church shouldn’t be underestimated. Broadcast is powerful. When tens of millions of people are consistently entrained to narratives honed to a sharp edge by market forces to be hyper-capable of grabbing and holding attention, it is going to have an effect. This is particularly true when the entire culture has been trained for generations to learn, think and act within the authority framework of the Church.
Image for post
Do as I say, not as I do
The contents of popular culture and the good opinion of authorities are important aspects of the Church, but the most central and subtle lesson taught by the Blue Church is the Blue Church itself.
Whether you are learning algebra, or reading about history, or watching a basketball game or listening to your favorite musician, the commonality among all of these is the asymmetric relationship of broadcast. Pay attention, watch and listen closely, learn and express “good opinion” and act accordingly. The content is important, but far more important is the form. The content varies. The form is consistent.
Just like the rowers entrained to the cadence of the coxswain, we have all of us trained for the vast majority of our lives to find, adopt and execute on some kind of master narrative. Some story that is complicated enough to respond to life but simple enough to be managed. Some framework of assumptions, axioms, truths, truth making and authority that takes the absolutely overwhelming complexity of the modern world and allows us poor apes some easy way to move forward in a coordinated fashion.
This fact explains a whole lot about what is going on in America (and most of the West) today. Perhaps it helps explain why the left is always trying to find a narrative to simplify and make the world manageable. It might even explain the mania on the left for psychoanalysis. After all when your principal social responsibility is to respond correctly to authority and deftly read where you are in the field of good opinion, being able to peek behind the psychological curtain is an advantageous skill. (And if you really want to go deep, the ability to dismiss bad opinion as psychopathology is one of the most subtle, and surprisingly common, techniques of the Church.)
In any event, the near monopoly of the Church on our ability to make sense and meaning of the world certainly helps to explain why the ongoing collapse of the Blue Church is creating so much anxiety.
Image for post
The End is Nigh
There are many reasons why the Blue Church is crumbling. Some of it has to do with an increasing friction among the diverse sub-narratives that have gathered under Blue, particularly where the fundamental incoherence of “identity politics” is reaching a tipping point (and is being pushed into what feels to me like a nihilist endgame by the alt-right). However, while this tension is important, I don’t think it is fundamental. Instead, to identify the real existential threat to the Blue Church, I return to our our two core concepts: technology and complexity.
One primary driver behind the collapse of the Blue Church is the swift replacement of the very mass media it is premised upon with a new symmetric kind of media — the Internet. This new media presents a niche for coherence that is very different from the one that gave rise to the Blue Church. It is a fundamentally different landscape. Like polar bears condemned to extinction by a thawing ice cap, the Blue Church’s days are numbered by the relentless erosion of broadcast mindshare to the new much more symmetrical media of the Internet.
As I discussed in Situational Assessment: 2017, I assign a significant portion of the surprising victory of the Trump Insurgency to the fact that the transfer of power from broadcast to digital has crossed the tipping point.
It is this technological transition that leads me to the conclusion that while the Blue Church (and its allies in the Deep State and the Establishment) can certainly struggle and hold for a while, their day is done. The climate is changing and they must adapt or die.
And then there is the question of complexity. The Blue Church emerged in response to the explosion of complexity of the 20th Century and the capacity of mass media to form a control structure that was adequate to that complexity.
It worked. But the 20th Century didn’t stand still. In fact, it accelerated. In the face of this ongoing acceleration, the Blue Church control structure is no longer adequate. The level of complexity of the 21st Century is simply outside of the control capacity that is possible within the form of the Blue Church. Unless we abandon the Church and move to a new approach, our race into the future will be increasingly out of control.
However, and this is a profoundly important point, we currently know of no form of control structure that is adequate — even in principle.
The fundamental problem is at least threefold:
Our entire approach to managing complex systems like our environment is flawed. Until the late 20th Century we could get away with this flaw because we weren’t powerful enough to matter. This has changed and as Joe Brewer has been writing about beautifully, we need to level up quickly. We need to switch from trying to manage complex systems with complicated control structures and invent entirely new techniques for intrinsically up regulating the complex systems that make up our natural world. We don’t yet know how to do this.
Complex systems that include human beings are different. Unlike atmospheres and nitrogen cycles, people can forecast, strategize and adapt hyper-rapidly to our environment. Dave Snowden calls this anthro-complexity. We have to innovate an entirely new approach to governance that is adequate to the challenging set of problems posed by anthro-complexity. We really don’t know how to do this.
Finally, we have to come to terms with the real nature of technology, the difficult to predict feedback loops of how we affect technology and how it affects us. And then we have to figure out how to navigate the actual consequences of exponential technology — on ourselves and on our lived world. Most people aren’t even prepared to think about how to do this.
In the context of these challenges, the Blue Church is simply in way over its head. The world is just too big and moving too fast for this kind of control hierarchy to keep up — even when it is trying to do its best, it is going to get in the way. Addressing these challenges is going to require the innovation of an entirely new approach to how we collectively make sense of and act in the world.
I have been referring to the solution with the term “collective intelligence” and have discussed some of the issues in a short video here and in an older Medium post focused on blockchain efforts in the space here.
The brief on collective intelligences is that we really know very little about them. Perhaps the most robust version of a highly decentralized collective intelligence that has so far emerged is the Red Religion / Trump Insurgency that I discuss in Situational Assessment: 2017. As I mention in that post, for a number of reasons, I do not believe that this particular kind of “dCI” will get us where we need to go. But it presents a very useful case study. For those who want to dig deeper, I recommend taking a look at the work posted by Gustavo in Rally Point Journal.
If you know of other people who are doing good work here, please mention them in the comments. If you feel like you are in a position to help the small group of people who are gathering around trying to at least begin to ask the right questions, drop me a line.
In Conclusion
Well, that ran a bit long. I hope some of you found it worth sticking it out to the end. I had intended to spend some time on the actual content of the Blue Faith, but that had to be cut. If you are interested, let me know in the comments. If enough people care, I’ll take a swing at it and perhaps at the Establishment and the Deep State to boot.
[Author’s note, I have never read “Yarvin” or his articulation of “the Cathedral.” This material could have inspired the original use of the concept by the Reddit author. If what I have written here is close to Yarvin’s analysis, that is interesting. If not, well, that is interesting too.] ''',

                '33': '''The Rise and Fall of Networks
Jordan Hall
Jordan Hall
Follow
Jul 1 · 3 min read



The following has long struck me as obvious, but it occurred to me yesterday that it might not be. So I share it herein.
We are aware of the phenomenon called “Metcalfe’s Law.” Roughly that the value of a network is proportional to the square of the number of users connected to the system. This “network effect” is perhaps the most important value driver in the world today. Because the value of the network increases with the number of people on the network, there is a self fulfilling prophecy. Past a critical point the biggest network is more attractive than any other competing network. Which means that it gets more users. Which means that it gets more valuable. Which means that it is more attractive.
It can be a pretty quick ride to monopolistic vastness. Just ask Facebook, YouTube and Twitter.
OK. Lets call this feedback loop the “network attractor.” Once you have achieved some critical point, your platform is like a black hole that sucks in everything and makes escape increasingly impossible.
Now I would like to introduce a new concept. Perhaps even a new law.
“Any for-profit entity that is founded on the value of network effects must maximally extract that value to the limit of the network attractor. This produces an ‘extractive repulsor’ force. As the limit is approached, the network becomes poised at fragility.
Note that the extraction of value does not necessarily come in the form of “optimizing for profit.” To be sure, much of it does — things like increasing the number and intrusiveness of ads often shows up — but a lot of the ‘extraction’ comes in other forms. Things like reduced customer service. Or increasing use of the platform to accomplish goals that are anti-valued by the users. Of particular note is the increasing intrusiveness of the platform itself — sucking value out of the whole of the user’s life and into the platform.
The specific form of the extraction is up to the specific platform. But the rule is general: the camel will be loaded with straw until the last.
And then we have the final piece of this new law: Metcalfe’s law cuts both ways. If the value of a network increases exponentially as you add new users to the system, it also *decreases* exponentially as users leave the system.
But on this side of the ride the network has a problem: it is now burdened with the ‘extractive repulsor.’ So unless the folks in charge of the platform can figure out a way to reduce the extraction at an exponential rate, even a small number of people leaving the network will quickly lead to a torrent.
Through the relentless carelessness of value extraction, the system has become “hollowed out.” All surface area, no volume.
As quickly as systems built by Metcalfe’s law can grow, by Halls’ law, they can even more quickly collapse. ''',
}, 

                'target': {
                '0': "Justin Economics",
                '1': "Justin Reading/ Book Recommendations",
                '2': "Justin Mental Models",
                '3': "Justin Decision Making",
                '4': "Justin Naval FS Podcast Notes",
                '5': "Justin Philosophy",
                '6': "Justin Philosophy/ Psychology",
                '7': "Justin Sports",
                '8': "Justin Learning/ Reading",
                '9': "Justin Learning/Reading",
                '10': "Justin Sports",
                '11': "Justin Sports/Data Science",
                '12': "Justin Data Science",
                '13': "Justin Sports",
                '14': "Justin Sports",
                '15': "Justin Philosophy/ Life Advice",
                '16': "Justin Economics/Gambling",
                '17': "Justin Philosophy/ Life Advice",
                '18': "Justin Business/ Philosophy",
                '19': "Justin Innovation/ Philosophy",
                '20': "Justin Psychology/ Persuasion",
                '21': "Justin Philosophy/ Life Advice",
                '22': "Justin Life Advice/ Productivity",
                '23': "Justin Computer Science/ Quantum",
                '24': "Justin Computer Science/ Information Theory",
                '25': "Justin Economics",
                '26': "Justin Life Advice/ Productivity",
                '27': "Justin Philosophy",
                '28': "Justin Economics",
                '29': "Justin Data Science",
                '30': "Justin Economics",
                '31': "Justin Business/Economics",
                '32': "Justin Politics/ Philosophy",
                '33': "Justin Systems/Complexity",
                },

                'url':{
                '0': "https://ergodicityeconomics.com/2020/03/06/probability-weighting-and-ergodicity-economics/",
                '1': "https://fs.blog/2012/02/book-recommendations-from-nassim-taleb/",
                '2': "https://fs.blog/mental-models/",
                '3': "https://fs.blog/smart-decisions/",
                '4': "https://fs.blog/knowledge-project/naval-ravikant/",
                '5': "https://ryanholiday.net/100-things-learned-10-years-100-reads-marcus-aureliuss-meditations/",
                '6': "https://waitbutwhy.com/2014/12/what-makes-you-you.html",
                '7': "https://thepowerrank.com/guide-cfb-rankings/",
                '8': "https://towardsdatascience.com/how-you-should-read-research-papers-according-to-andrew-ng-stanford-deep-learning-lectures-98ecbd3ccfb3",
                '9': "https://ryanholiday.net/the-narrative-fallacy/",
                '10': "https://thepowerrank.com/2014/11/24/how-to-understand-college-football-analytics-the-ultimate-guide/",
                '11': "https://medium.com/clarktech-sports/python-sports-analytics-made-simple-part-2-40e591a7f3db",
                '12': "https://towardsdatascience.com/the-mathematics-of-machine-learning-894f046c568",
                '13': "https://www.footballstudyhall.com/2014/12/16/7398531/college-football-ratings-second-order-wins",
                '14': "https://www.bcftoys.com/notes/",
                '15': "https://medium.com/@theneurohacker/to-be-truly-effective-in-life-25b01a04ad51",
                '16': "https://aip.scitation.org/doi/10.1063/1.4940236",
                '17': "https://medium.com/deep-code/on-jordan-peterson-and-the-future-51402a370d79",
                '18': "https://www.perell.com/blog/peter-thiel",
                '19': "https://nav.al/matt-ridley",
                '20': "https://fs.blog/intellectual-giants/robert-cialdini/",
                '21': "https://www.kapilguptamd.com/2018/11/20/yes-my-son-a-story-of-non-attachment/",
                '22': "https://fs.blog/2017/08/amateurs-professionals/",
                '23': "https://www.artiba.org/blog/meet-silq-the-first-intuitive-high-level-language-for-quantum-computers",
                '24': "https://spectrum.ieee.org/tech-history/cyberspace/claude-shannon-tinkerer-prankster-and-father-of-information-theory",
                '25': "https://medium.com/@allenfarrington/this-is-not-capitalism-5ed0a9d5dfa9",
                '26': "https://www.scottadamssays.com/2013/11/18/goals-vs-systems/",
                '27': "https://dailystoic.com/cato/",
                '28': "https://medium.com/@allenfarrington/the-complex-markets-hypothesis-44c2b2b191d2",
                '29': "https://www.ben-evans.com/benedictevans/2018/06/22/ways-to-think-about-machine-learning-8nefy",
                '30': "https://medium.com/@allenfarrington/money-banking-bitcoin-libra-191183d5e825",
                '31': "https://www.epsilontheory.com/this-is-water/",
                '32': "https://medium.com/deep-code/understanding-the-blue-church-e4781b2bd9b5",
                '33': "https://medium.com/deep-code/the-rise-and-fall-of-networks-be504049927",
                }

}