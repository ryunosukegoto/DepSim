# DepSim: Health Insurance Coverage Simulator
## Description:
DepSim is an interactive simulator that predicts how much a low-income individual is expected to benefit from insurance coverage. Based on <a href="https://academic.oup.com/aje/article/193/7/951/7612960" target="_blank">Machine learning for detection of heterogeneous effects of Medicaid coverage on depression</a> published in <i>American Journal of Epidemiology</i>, DepSim estimates the treatment effect of insurance coverage on depression using the generalized random forest, developed by Wager and Athey (<a href="https://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1319839?journalCode=uasa20"><i>Journal of the American Statistical Association</i>, 2018</a>). For more information on our study, please see [study details](#study-details) below or refer to the <a href="https://academic.oup.com/aje/article/193/7/951/7612960" target="_blank">original publication</a>.

The user can enter their demographic information as well as past medical history, with which the model will estimate the effects of health insurance coverage on depression. Note that the external validity of the model has not been tested and the model may not necessarily be generalizable to individuals other than low-income adults in Oregon, where the original study (<a href="https://www.nejm.org/doi/full/10.1056/NEJMsa1212321">Baicker et al., <i>New England Journal of Medicine</i>, 2013</a>) was based.

The app was created for demonstrative purposes, but illustrates how a healthcare provider might personalize treatment decisions based on an individual’s characteristics. The approach we took in this research article can be applied to any treatment, as long as data are available.


## Run locally:
After cloning to project with ```git clone```, go to the project directory and install the required Python packages by using the following ```pip``` command:
```
pip install -r requirements_python.txt
```

As the model used in this app was created in R, you will also need to have installed R. <a href="model.R">```model.R```</a> will check whether the required R packages are downloaded, and if not, it will automatically download the packages.

To run the app, use the following command:
```
flask run
```

## Study details:
In 2008, a group of researchers ran the <a href="https://www.nejm.org/doi/full/10.1056/NEJMsa1212321">Oregon Health Insurance Experiment (OHIE)</a>, which evaluated the health effects of Medicaid, a health insurance program for low-income households. The researchers took advantage of the randomized allocation of insurance enrollment through a lottery, and evaluated the effects of Medicaid coverage using a randomized controlled design. The OHIE received significant attention, as public health insurance programs for low-income households have been implemented in many countries, but its health effects had rarely been explored. The investigators found that Medicaid coverage significantly decreased the probability of a positive screening result for depression.

However, the average benefits of Medicaid expansion in treating depression seen in the OHIE may mask substantial heterogeneity, with some people benefitting much more than others. In this post hoc analysis of the OHIE, we assessed the degree of response heterogeneity and the extent to which it is predictable ex ante. By applying a novel machine learning method recently introduced in the econometrics literature, the <a href="https://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1319839?journalCode=uasa20">causal forest</a>, we delineated the characteristics of individuals with high or low predicted benefit and evaluate both the health benefits and efficiency of an approach for targeting health insurance coverage on those most likely to benefit. Thus, in the original OHIE, investigators evaluated the average treatment effect (ATE) of Medicaid coverage, but in the present study, we evaluated the conditional average treatment effects (CATEs; alternatively, individual treatment effects) of Medicaid coverage. With this approach, we were able to evaluate the causal effects of Medicaid coverage at the individual level, conditional on individual level characteristics such as gender, age, educational level, race and ethnicity, whether the interview was conducted in English or not, diagnoses before the lottery, and previous histories of emergency department visits. To screen for depression an average of 25 months post-treatment, we used the Patient Health Questionnaire-8 (PHQ-8). Treatment effects were expressed as percentage point reduction in positive depression screening. A total of 10,068 low-income individuals were eligible for analysis.

We found that individuals with high predicted benefit were older and had more physical or mental health conditions at baseline, and there was substantial heterogeneity in the effects of Medicaid coverage on depression. Considering a scenario where Medicaid coverage cannot be expanded to the full population due to e.g., budget constraints, we evaluated the “high-benefit approach,” where Medicaid coverage is expanded to only those with high predicted benefit. The cutoff for high benefit was defined as the median of the estimated CATEs. We found that compared to expanding coverage to the full sample of 10,068 low-income individuals (“population approach”), expanding coverage to 5,034 individuals with high predicted benefit (“high benefit approach”) generated greater reduction in the proportion of individuals screening positive for depression (21.5 vs. 8.8 percentage point reduction; adjusted difference [95% confidence interval (CI)], +12.7 [+4.6, +20.8]; P=0.003), at substantially lower cost per case prevented ($16,627 vs. $36,048; adjusted difference [95%CI], -$18,598 [-$156,953, -$3,120]; P=0.04).

In this post hoc analysis of the OHIE using the machine learning causal forest, we found substantial – and predictable – heterogeneity in the effect of Medicaid coverage on depression. Those who experienced large improvements in depression were older and had more baseline physical or mental health conditions. We found that providing Medicaid coverage to individuals with high likelihood of benefit as predicted using ex ante information reduced depression by a three-fold greater margin than providing coverage to all low-income individuals. This approach was not only effective in reducing depression cases, but also more cost-effective than broader expansions as captured by the healthcare spending per case of depression averted. Taken together, our findings suggest that it is possible to use baseline information to prioritize coverage expansion to those who are likely to benefit the most, and demonstrate the promises of a novel machine learning-based approach to precision health and policy.