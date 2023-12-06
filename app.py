"""
* Name : FreeTime Tracker Project - application program
* Author: Amber Miller
* Created : 12/5/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: MAC OS Ventura 13.5.1
* IDE: PyCharm 2023.2.1 (Professional Edition) Version
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : App file that controls the flask routing, html page behavior,
* and starts the website program using flask framework
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
from flask import Flask, render_template, request, redirect
import crochetSQ
import gameMap

# Initializing empty stack and map for flask program to work with
crochet = crochetSQ.Stack()
games = gameMap.Map()

# initializing flask so python code can run server
app = Flask(__name__)
app.secret_key = "secret key"


# default index page when the program starts
@app.route('/')
def index():
    return render_template('index.html')


# games home page
@app.route('/gameHome')
def gameHome():
    return render_template('gamesHome.html')


# crochet home page
@app.route('/crochetHome')
def crochetHome():
    return render_template('crochetHome.html')


# add crochet project screen that has form data
@app.route('/crochetAdd', methods=["GET", "POST"])
def crochetAdd():
    # pulling size of the list, so we can display to the user
    current_size = crochet.size()
    # if the user posts (aka submits the form, the following occurs)
    if request.method == "POST":
        # pull user data from the project name field
        project_name = request.form.get("cname")
        # push project name to the top of the stack
        crochet.push(project_name)
        # redirect user to the crochet list page to see their changes
        return redirect('/crochetList')
    # if user is accessing page, the page is rendered without adjusting the stack
    return render_template('crochetAdd.html', current_size=current_size)


# retrieve and/or remove project from the top of the stack
@app.route('/crochetNext', methods=["GET", "POST"])
def crochetNext():
    # setting error message to None
    error = None
    # if the size of the stack is 0, user is routed to crochet home page where error message is displayed
    if crochet.size() == 0:
        error = "No crochet projects available! Add projects first!"
        return render_template('crochetHome.html', error=error)
    # retrieving top of the stack to display to user
    top_stack = crochet.peek()
    # if the user posts (aka submits the form, the following occurs)
    if request.method == "POST":
        # project on top of the stack is removed
        crochet.pop()
        # project that was popped is added to user message to confirm pop
        error = top_stack + " has been removed from the stack."
        # project that is now on top of the stack is displayed to user
        top_stack = crochet.peek()
        return render_template('crochetNext.html', error=error, top_stack=top_stack)
    # if user is accessing page, top of the stack is revealed with form data available
    return render_template('crochetNext.html', top_stack=top_stack)


# page that displays all items in the crochet stack
@app.route('/crochetList')
def crochetList():
    # saving stack to variable to send to html page
    cList = crochet.print_stack_up()
    return render_template('crochetList.html', cList=cList)


# add game and ranking to map and displays entry form
@app.route('/gameAdd', methods=["GET", "POST"])
def gameAdd():
    # if the user posts (aka submits the form, the following occurs)
    if request.method == "POST":
        # setting error message to None
        error = None
        # retrieving form data and converting priority string value to int
        game_name = request.form.get("gname")
        game_priority = request.form.get("gpriority", type=int)
        # if insert is successful, user is redirected to the game list page
        if games.insert_pair(game_name, game_priority):
            return redirect('/gameList')
        # if insert is unsuccessful (key already exists), error is displayed and form is cleared of data
        else:
            error = 'Game already in list!'
            return render_template('gameAdd.html', error=error)
    return render_template('gameAdd.html')


# page that prints current list of games and allows user to remove it from the map
@app.route('/gameRemove', methods=["GET", "POST"])
def gameRemove():
    # setting error message to None
    error = None
    # retrieving list of key, value pairs from map to variable for html to display
    g_list = games.print_map()
    # if there is no data in the map, error message is created and user is directed to games home page
    if len(g_list) == 0:
        error = "No games available! Add games first!"
        return render_template('gamesHome.html', error=error)
    # if the user posts (aka submits the form, the following occurs)
    if request.method == "POST":
        # form data is collected and stored into a variable
        game_selected = request.form.get("gameSelect")
        # if game removal is successful, user is sent to game list to view revised map list
        if games.remove_pair(game_selected):
            return redirect('/gameList')
        # if game removal is unsuccessful, error message is created and displayed on a new blank removal page
        else:
            error = 'Game does not exist or is misspelled. Try again!'
            return render_template('gameRemove.html', error=error, g_list=g_list)
    return render_template('gameRemove.html', g_list=g_list)


@app.route('/gameList')
def gameList():
    # retrieving and storing map key, value pairs in variable
    g_list = games.print_map()
    # sorting map and turning into a list with 1 being the first in the list
    sorted_g_list = sorted(g_list.items(), key=lambda x: x[1])
    # displaying sorted map to user in correct order
    return render_template('gameList.html', g_list=dict(sorted_g_list))


# main to run the flask app
if __name__ == '__main__':
    app.run()
