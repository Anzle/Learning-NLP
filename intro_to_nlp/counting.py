from __future__ import division
import nltk

print(nltk.corpus.gutenberg.fileids())

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
print(md[:8])

# count number of words
print(md.count("whale"))
print(md.count("boat"))
print(md.count("laptop"))

# total words in book
print(len(md))

# unique set of all words
md_set = set(md)
print(len(md_set))
print(len(md)/(len(md_set)))

# list of sentences
md_senta = nltk.corpus.gutenberg.sents("Melville-moby_dick.txt")
# avg words per sentences
print(len(md)/len(md_senta))
