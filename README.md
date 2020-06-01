# mass_function_fitting

This is the Git location that I will be using for my work trying to fit the Mass function for Star Clusters in M33.

I will be utilizing MCMC simulations to fit both a Schechtar function and power law distributions to the data to see which provides a better fit. 

The Analysis will follow that of Johnson et. al 2017 http://adsabs.harvard.edu/abs/2017ApJ...839...78J

The M31_MF_replication folder is proof of concept where I am testing the code I wrote against the results from M31.
The data from this analysis is provided in apendix A of Johnson et. al 2016 https://doi.org/10.3847%2F0004-637x%2F827%2F1%2F33

There will be a series of different codes that I be using, each building in complexty of the previous. 
The first: Schectar_Fuction_wo_cpn is the simplist form of the Schectar Function, (insert function here)
Then second: incporating the observational completeness function while still not dealing with the normalization (Schectar_Function_wc_nn).
Finally: incorperating both the observational completeness and the normalization (Schectar_Function_w/every)

I will then push the final working code to the main repository to use on M33 data.
