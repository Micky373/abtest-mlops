import scipy.stats as sc_s

# calculate the sample size needed for the specified power and confidence level

def min_sample_size(bcr, mde, power=0.8, sig_level=0.05):
    standard_norm = sc_s.norm(0, 1)
    beta = standard_norm.ppf(power)
    alpha = standard_norm.ppf(1-sig_level/2)
    pooled_prob = (bcr + bcr+mde) / 2
    min_N = (2 * pooled_prob * (1 - pooled_prob) * (beta + alpha)**2/ mde**2)
    return min_N