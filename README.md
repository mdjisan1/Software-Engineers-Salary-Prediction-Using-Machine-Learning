Abstract

Modern technology has contributed to modern society,
and software developers play a significant part in developing
and maintaining this technological world. But in this complex
field, accurate salary prediction is crucial for job seekers and
recruiters. But by the machine learning approach for predicting
software engineering salaries effectively. By leveraging a dataset
of historical salary information and various relevant features
such as years of experience, education level, and geographical
location, we employ a regression model to estimate software engineers’
future salary or current possible salary. The methodology
integrates data prepossessing, feature selection, model training,
and evaluation to construct a robust prediction web framework.
We consider several machine learning algorithms, including
linear regression, decision trees, random forest, Support vectors,
XGB, Save Model, and methods with extensive performance
comparisons.

Our research demonstrate the effectiveness of machine learning
models in accurately forecasting software engineers’ salaries
by getting an highest accuracy of 76% and lowest Root mean
squared error of 9.59 %. Also, this model empowers job seekers
and employers to make more informed decisions regarding salary
expectations. This research contributes to the field of software
engineering by offering a valuable tool for salary negotiation
and career planning, enhancing transparency and efficiency in
the software job market.
Index Terms—Software engineer, Salary prediction, Machine
Learning, Predictive modeling, Feature engineering, Model evaluation,
Data preprocessing, Regression, Decision trees, Random
forests,XGB.

I. INTRODUCTION

The demand for software engineers is growing day by day
with the improvement of technology. Currently, the software
engineering field is the most challenging for a recruiter and
a job seeker to predict salary. In most cases, a recruiter can
offer a salary, and the job seeker thinks that it is not perfect
for them; they feel that they deserve more. Also, the recruiter
might offer more salary than a job seeker deserves. Because
sometimes salary can vary by geographical location.In this
article, we look into this problem and present a machinelearning
approach to forecast the salary of software engineers
Identify applicable funding agency here. If none, delete this.
by geographical location. The model described in this article
will aid a prospective job seeker and recruiter in making
a more informed decision while predicting the salary of a
software engineer.

A. Software engineers salary in different top leading countries
The USA is the leading country in demand for software
engineers, and this country tends to be higher than the demand
for skilled software engineers in the technology sector. The
median annual income for software developers, which includes
software engineers, was $110,140 in May 2020, as reported by
the US Labor Statistics. Also, the lowest 10% earned less than
$63,250, while the wealthiest 10% made more than $164,590.
[1] Also, it can vary by the different state. If we see that
in San Francisco, software engineers get 31% higher salaries
than the national average, whereas in Austin, it was only 14%.
[2] Through the research, we also found that salary can vary
based on economic conditions and skill base, like entry-level,
mid-level, and senior-level [3], [4]. Also, we research in terms
of India, [5] the Southeast Asian leading software engineers’
labor market. Their entry-level software gets around $8000 to
$10000 in terms of the USA, which is 90% less, where both
have the same qualifications and skills. [6]

B. Applicability of Machine Learning in Predicting the salary
of Software Engineers

A software engineer’s salary is determined by some criteria,
including their educational background, work experience, talents,
and place of employment [7].It is not easy to effectively
estimate their salaries using rule-based algorithms due to
the complexity of these affecting variables. Using inductive
machine learning techniques to extract salary predictions from
the data-set is a more practical strategy. [8] For this reason,
using a machine learning approach is a good fit for this specific
application.

C. Research Goal

This research outlines several key objectives and contributions
related to predicting the salary of software engineers
using machine learning approaches. Here’s a summarized
version:
1) Collect a large data-set of software engineer salaries and
discover the most important features that can be utilized
for predicting salary.
2) Using machine learning algorithms, predicted the
salaries of software engineers with high accuracy.
3) To deploy the model as a web application on a local
machine for ultimate deployment to end users.
The primary contributions of this research article include:
1) Collecting and carefully collecting a real-world dataset
of software engineer salaries, which will be a great
resource for the research.
2) Building an accurate predictive model for estimating
salary, utilizing the collected data-set.
3) Evaluating the model’s performance by comparing its
predictions against unseen data, ensuring its reliability.
4) Deploying the model as a web application, making it
accessible to end users for future use.

METHODOLOGY

The approach adopted in this work is outlined in Figure 1:
![Screenshot 2025-02-19 142826](https://github.com/user-attachments/assets/8a72f7b0-0a1d-46b5-87f4-396ad587574f)

A. Data Acquisition

We have collected our dataset from stack overflow official
website. Stack Overflow is a professional community for
developers. Every year since 2011, they conduct a developer
survey and release the collected data open-source on the
web. Developers from almost 180 countries participate in this
survey [17]. Stack overflow then collects all the data and then
publish them as a csv file in their official website every year
at once. The participants are mostly from the US, India, UK
and EMEA regions. The majority of the survey respondents
had a background of developer/ coding experience. For our
project, we have selected the 2020 Stack overflow survey
dataset. Almost 65000 developers from all over the world
have participated in this survey [18]. The initial dataset has
64461 instances and 61 features. But we have selected total
five attribute including the target class. The dataset that we
have used to generate results can be found in [19] description
of selected attributes from data set in given in table 1.
