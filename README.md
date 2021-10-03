# MAIS HACK 2021 Project 

**Team members:**
* **[Angela Fan](https://github.com/Angelalalula)**
* **[Zichuan Guan](https://github.com/zcguan)**
* **[Amanda Boatswain Jacques](https://github.com/AmandaBoatswain)**
* **[Hanying Shao](https://github.com/42694647426)**

![alt text](https://github.com/42694647426/MAISHACK2021/blob/main/official_website/static/uploads/Picture1.png)


## Inspiration & What it does
Have you ever seen a beautiful flower and wondered what kind of flower it is? Have you ever stepped on a pretty leaf and questioned which tree did it possibly fall of? Well, you're not the first In this website, you can get the answer to all your questions by simply uploading a picture!

## How we built it
To build the website, we used Flask, along with Python. Users can upload a picture of any format; an alert will pop-up if it is the wrong format, say a pdf. To train the model, we used to dataset by Maria-Elena Nilsback and Andrew Zisserman and trained the model using different methods in order to get the most accurate results.

## Challenges we ran into
We did not get good accuracies at first, therefore we had to train the model using more precise data. Linking the website's back-end to the training model code was time-consuming too, as we were not very familiar in that field.

## Accomplishments that we're proud of
We finished the project 10min before the deadline, everything working, the website looks nice at the end, and we solved each issue as a team; teamwork energy to the max :) We successfully got an accuracy of more than 67%

## What we learned
We learnt Flask on spot and created a website from scratch. We were able to communicate efficiently even if it was purely virtual.

## What's next for Biodiversity Tracker
We are trying to do a basemap in the future too, where when the user uploads the picture, it will be shown on a map where the flower or the leaf was discovered, so that the user will have an idea of the different species present in the world. Would be nice if one day, I travel abroad, see a pretty flower, upload to the website, and have my tracker keeping the info for me.

## How to run the APP
1. Clone the repository
```
git clone https://github.com/42694647426/MAISHACK2021.git
```
2. Install dependencies 
```
pip install -r requirements.txt
```
3. Run flask
```
set FLASK_APP='official_website/websiteTrial.py'

flask run
```





