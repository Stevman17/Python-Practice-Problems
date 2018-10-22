# Python-Problems

#This code uses fetchmaker, numpy, and scipy tools to perform a number of statistical analyses on a categorical dataset including: a Chi Squared Test, a Binomial Test, and a Tukey's Range Test

import numpy as np
import fetchmaker


#Determine's mean and tail length of Rottweiler's
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print np.mean(rottweiler_tl)
print np.std(rottweiler_tl)

#Tests whether whippets are significantly more or less likely to be a rescue than the average dog breed.
whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
from scipy.stats import binom_test
pval = binom_test(num_whippet_rescues, n=num_whippets, p=0.08)
print pval, num_whippet_rescues, num_whippets

from scipy.stats import f_oneway
a = fetchmaker.get_weight("whippet")
b = fetchmaker.get_weight("terrier")
c = fetchmaker.get_weight("pitbull")
fstat, pval2 = f_oneway(a, b, c)
print pval2

from statsmodels.stats.multicomp import pairwise_tukeyhsd
values = np.concatenate([a, b, c])
labels = ['whippet'] * len(a) + ['terrier'] * len(b) + ['pitbull'] * len(c)

print pairwise_tukeyhsd(values, labels, .05)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

from scipy.stats import chi2_contingency

color_table = [
  [np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")],
  [np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")],
  [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")],
  [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")],[np.count_nonzero(poodle_colors == "white"),   np.count_nonzero(shihtzu_colors == "white")]]
#Tests whether poodles and shihtzus have significantly different color breakdowns.
chi2, pval3, dof, expected = chi2_contingency(color_table)
print color_table
print pval3

#Tests whether chiuaua's and greyhounds have significantly different color breakdowns.

chihuahua_colors = fetchmaker.get_color("chihuahua")
greyhound_colors = fetchmaker.get_color("greyhound")

color_table2 = [
  [np.count_nonzero(chihuahua_colors == "black"), np.count_nonzero(greyhound_colors == "black")],
  [np.count_nonzero(chihuahua_colors == "brown"), np.count_nonzero(greyhound_colors == "brown")],
  [np.count_nonzero(chihuahua_colors == "gold"), np.count_nonzero(greyhound_colors == "gold")],
  [np.count_nonzero(chihuahua_colors == "grey"), np.count_nonzero(greyhound_colors == "grey")],[np.count_nonzero(chihuahua_colors == "white"),   np.count_nonzero(greyhound_colors == "white")]]

chi2, pval4, dof, expected = chi2_contingency(color_table2)
print color_table
print pval4
