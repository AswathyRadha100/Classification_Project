--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                                                                      #
# **Investigating Drivers For Telco customer churn - A project on Machine Learning Classification Models**(Level1)                                                
#                                                                                                                                                                      # 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Project Description** (Level 2)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Project Goal** (Level 2)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Initial Thoughts** (Level 2)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **The Plan** (Level 2) 

- **Acquire data from SQL**
- **Prepare data that's acquired**
  - &#9733; Create Engineered columns from existing data
    - &#9642; Sub-item A
    - &#9642; Sub-sub-item 1
    - &#9642; Sub-sub-item 2
  - &#9733; Explore data in search of drivers of churn
      - Answer the following initial questions
        - &#9642; Are customers with DSL more or less likely to churn?
        - &#9642; What month are customers most likely to churn and does that depend on their contract type?
        - &#9642; Is there a service that is associated with more churn than expected?  
        - &#9642; Is there a service that is associated with more churn than expected?  
        - &#9642; Do customers who churn have a higher average monthly spend than those who don't?

    



- &#9733; Explore data in search of drivers of upsets
  - &#9733; Explore data in search of drivers of upsets

  - &#9642; Sub-item B
- Main Item 2
  - &#9642; Sub-item C
    - &#9642; Sub-sub-item 3



 Explore data in search of drivers of
Aquire data from Kaggle

Prepare data

Create Engineered columns from existing data
upset
rating_difference
game_rating
lower_rated_white
time_control_group
Explore data in search of drivers of upsets

Answer the following initial questions
How often do upsets occur?
Does first move advantage affect upsets?
Does a game being rated affect upsets?
Does the average rating of both players have an effect on upsets?
Does time block affect upsets?
Does a player's choice of opening affect upsets?
Develop a Model to predict if a chess game will end in an upset

Use drivers identified in explore to build predictive models of different types
Evaluate models on train and validate data
Select the best model based on highest accuracy
Evaluate the best model on test data
Draw conclusions

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Data Dictionary** (Level 2) 

| Name      | Age | Occupation |
| --------- | --- | ---------- |
| John      | 30  | Developer  |
| Emily     | 25  | Designer   |
| Michael   | 28  | Engineer   |
     

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Steps to Reproduce** (Level 2) 

Ordered List:
1. Clone this repo.
2. Acquire the data from SQL DB.
3. Put the Data in the Cloned Repo Directory.
4. Run the Jupyter Notebook
5. Run the Notebook.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Takeaways and Conclusions** (Level 2) 



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Recommendations**(Level2)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### **Sub-subheader** (Level 3)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Chess Upsets
Project Description
Chess is widely renowned as one of the most skill intensive games ever invented. Both sides begin the game with identical pieces in an identical position, there are no random elements (aside from assigning the first move), and the movement of those pieces during a game can result in over 121 million possible combinations in just the fist three moves. Because of this, the player with the most skill is likely to win the grand majority of chess games. I have decided to look into the different elements of a chess game to determine if any of them increase or decrease the chance of a player with lower skill defeating a player with greater skill.

Project Goal
Discover drivers of upsets in chess games played on Lichess.org
Use drivers to develop a machine learning model to classify games as ending in upset or not ending in upset
An upset is defined as a lower rated player defeating a higher rated player.
This information could be used to further our understanding of which game elements contribute to or detract from a game’s skill intensity.
Initial Thoughts
My initial hypothesis is that drivers of upsets will be elements that either grant an outright advantage to one player or increase the likelihood of players making mistakes.

The Plan

README
Your README should contain all of the following elements:

Title Gives the name of your project
Project Description Describes what your project is and why it is important
Project Goal Clearly states what your project sets out to do and how the information gained can be applied to the real world
Initial Hypotheses Initial questions used to focus your project
Project Plan Guides the reader through the different stages of the pipeline as they relate to your project
Data Dictionary Gives a definition for each of the features used in your report and the units they are measured in, if applicable
Steps to Reproduce Gives instructions for reproducing your work. i.e. Running your notebook on someone else's computer.