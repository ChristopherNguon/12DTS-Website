from flask import Flask,render_template
import sqlite3
from sqlite3 import Error
app = Flask(__name__)
DATABASE = 'Character.db'
def create_connection(db_file):
   try:
       connection = sqlite3.connect(db_file)
       return connection
   except Error as e:
       print(e)
   return None

@app.route('/')
def render_home():  # put application's code here
    return render_template('index.html')

@app.route('/characters')
def render_characters():
    query = "SELECT Character,Path,Element,Version,Home_Planet,First_Met,HP,ATK,DEF,SPD FROM Character"
    con = create_connection(DATABASE)  # runs the function create_connection and passes the bd stared in DATABASE for it to use.
    cur = con.cursor()  # Applies and stores the cursor system to the data.
    cur.execute(query)  # runs the query
    character_list = cur.fetchall()  # stores all the info from the query into the tag list.
    con.close()
    print(character_list)


@app.route('/styles')
def render_styles():
   return render_template("styles.html")



if __name__ == '__main__':
    app.run()
