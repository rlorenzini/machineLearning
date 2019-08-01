# Python Machine Learning Basics

Built using Python 3.7.4 on a MacBook Pro.

## Requirements:
1. Python3 or greater (go to Python's website and download latest version)
2. mlxtend          ```pip3 install mlxtend```
3. pandas           ```pip3 install pandas```
4. matplotlib       ```pip3 install matplotlib```
5. scikit_learn     ```pip3 install scikit_learn```
6. numpy            ```pip3 install numpy```
7. scipy            ```pip3 install scipy```

Optionally, run ```pip install --upgrade pip``` if needed.

```pip3 install mlxtend && pip3 install pandas && pip3 install matplotlib && pip3 install scikit_learn && pip3 install numpy && pip3 install scipy```

## Why Learn Machine Learning?

Without knowing it, you have used a website, application, or another piece of technology which utilizes machine learning. Do you play Chess against an AI? Do you have a spam folder for your emails? Machine learning is everywhere, and as a programmer it is the future of the industry. Machine learning can be used to improve websites, games, technologies, and so on, but also provide a custom user experience based on the actions taken by the user. Whether you are creating a suggestion list on a shopping website or having a robot traverse a maze, machine learning is the best way to improve such features. 

## Three machine learning Types:
1. Unsupervised
2. Supervised
3. Reinforcement

**Unsupervised learning** is where no information on the data is known; unlabeled data. Think of registering emails as spam. When you mark an email as spam, the email server checks your incoming emails for likeness to previously spammed emails. If the email fits enough criteria, the incoming email is sent to spam. The incoming emails are unlabeled data and the algorithm uses pre-existing data to determine what to do with said email. Unsupervised learning clusters the data into groups based on likeness.

**Supervised learning** takes the data and, instead of clustering the data, tries to establish a linear relation between the data. On one side of the line are emails which are acceptable and the other side of the line are spam emails. This is called linear regression. There is also logistic regression, which draws a nonlinear line. This allows for more flexibility but also greater errors and issues depending on the incoming data. Which supervised learning regression is best is determined by the data being looked at by your algorithm.

**Reinforcement learning** works differently than the previous two. The Agent looks at the Environment and tries to learn the best possible actions. The Agent is the algorithm, or AI, the Environment is the data, which can be a game like chess, and the action is what the Agent does based on the information given. In Chess, the Agent will look at the board, the pieces it has versus you, previous data and strategies, win/losses based on movesets, and so forth. The Agent will then move the piece and register if the move was positive or negative. The positive and negative feedback is the reward the Agent receives. The Agent uses the rewards to better itself the next time it plays the game.
