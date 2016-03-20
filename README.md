# GCB 535 Challenge

We ([Casey Greene](http://www.greenelab.com/lab-members/) , [Ben Voight](http://coruscant.itmat.upenn.edu/people.html)) teach [GCB 535](http://www.med.upenn.edu/bgs/documents/GCB535.pdf) at Penn. The class as a whole is computational biology for biologists. This portion of the class aims to give students an introduction to machine learning, as well as hands on practice with machine learning methods. 

In this game, we try to build and accurately assess a predictor. This repository hosts the challenge for individuals outside of our class. Feel free to play along with us.

## Structure

We'll provide two different datasets. Within each dataset (D1 and D2), we have 5000 examples. We've randomly partitioned these into sets of 2000, 1000, 1000, and 1000. These are respectively numbered S1, S2, S3, and S4 for each dataset. Thus D1_S1.csv is a comma separated set of 2000 samples for the first dataset. The data have 200 features. The final column is the class label that we expect you to predict.

The initial repository contains the first sets of 2000 (S1) and 1000 (S2) examples for each dataset. Each sample (S1, S2, S3, S4) within a dataset (e.g. D1) should be comparable. We'll provide an S3 that contains an additional 1000 samples for each dataset on Wednesday, April 6th. We'll also provide an S4 at that time in a predict subfolder. This one will have the labels stripped. You may use these samples however you wish (e.g. combine and cross validate, etc). The final metrics that we're interested in are prediction accuracy on the final subset (S4) as well as your ability to predict your accuracy on the held out data.

```
gcb535challenge
│   README.md
│
└───data
    │   D1_S1.csv
    │   D1_S2.csv
    │   D1_S3.csv
    │   D2_S1.csv
    │   D2_S2.csv
    │   D2_S3.csv
└───predict
    │   D1_S4.csv
    │   D1_S4.csv

```

We'll release the third set of data at the time of our class on Wednesday, April 6. At this time, we'll also release the final prediction sets with labels stripped. If you participate, we'd love to hear what you expect your accuracy to be (for binary class labels) once we release the final labels. We'll make these available just before or just after class on April 8th at 10AM EST.

If you want to make predictions, fork this repository. Make sure your predictions are committed and pushed by April 8th at 10AM EST. Alongside your predictions, provide an estimate for the performance that you expect to see on the independent validation data.

----

Please ask clarifying questions, and we'll try to update this README to address the questions.
