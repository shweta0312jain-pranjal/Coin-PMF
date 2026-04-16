import scipy.stats as stats

x = 3
n = 10

prob_1 = stats.binom.pmf(x, n, 0.5)
print("The probability of getting exactly 3 heads in 10 coin flips is: ")
print(prob_1)

prob_2 = 1-stats.binom.pmf(0, n = 10, p = 0.5)-stats.binom.pmf(1, n = 10, p = 0.5)-stats.binom.pmf(2, n = 10, p = 0.5)
print("The probability of getting at least 3 heads in 10 coin flips is: ")
print(prob_2)