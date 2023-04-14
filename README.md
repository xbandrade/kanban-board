# Kanban Board
A simple implementation of a Kanban Board using CustomTkinter

## Setup
* Install the requirements using `pip install -r requirements.txt`
* Run `python -m main` to start the app

<img src="https://raw.githubusercontent.com/xbandrade/kanban-board/main/img/board.png" width=90% height=90%>

### With a Kanban Board you can manage the workflow of a project you are working on.

The options available in the sidebar of the app are:
* `Add Column` Add a new column to the current board
* `Add Card` Add a new card to the current board
* `Save Board` Save the current board to a JSON file
* `Load Board` Load a board that was previously saved
* `Create New Board` Clear the current board and create a new one
* `Dark Mode` Switch between light and dark mode

Both columns and cards are implemented using serializable Python classes, and the boards are saved in JSON format in the `json/` folder.

The card content can be edited by clicking on the text box, and each card in the board also have three buttons by them:
* `Move Card` Move the card to the next column
* `Pop-up Card` Create a pop-up with the contents of the card. These card pop-ups can be locked to be always on top of all other apps
* `Delete Card` Remove the card from the column

### Card Pop-ups
<img src="https://raw.githubusercontent.com/xbandrade/kanban-board/main/img/cards.png" width=35% height=35%>
