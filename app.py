import pymysql
from flask import *


app = Flask(__name__)
# creating connection to the database
# connection = pymysql.connect(host="localhost", user="root", password="", database="recruitement_portal")

# @app.route("/")
# def main():
#     return render_template("index.html")

@app.route("/apply", methods=['POST'])
def apply():

    # creating connection to the database
    connection = pymysql.connect(host="localhost", user="root", password="", database="recruitement_portal")

    # create cursor
    cursor = connection.cursor()

    # get data from the form
    serialno =request.form['serialno']
    name = request.form['name']
    qualifications = request.form['qualifications']
    qualificationevidence =request.form['qualificationevidence']
    specialization = request.form['specialization']
    institutionoflearning =request.form['institutionoflearning']
    yearofuniversitystarting = request.form['yearofunversitystarting']
    yearofuniversitycompletion = request.form['yearofuniversitycompletion']
    totalyearsofworkexperience =request.form['totalyearsofworkexperience']
    state = request.form['state']
    county = request.form['county']
    constituency = request.form['constituency']
    phonenumber = request.form['phonenummber']
    email = request.form['email']
    nationalid = request.form['nationalid']
    cv = request.form['cv']
    previousworkexperience = request.form['previousworkexperience']

     # insert data into the database
    sql = "insert into applicants (serialno,name,qualfications,qualificationevidence,specialization,institutionoflearning,yearofuniversitystarting,yearofuniversitycompletion,totalyearsofworkexperience,state,county,constituency,phonenumber,email,nationalid,cv,previousworkexperience) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    # execute the sql 
    cursor.execute(sql, (serialno,name,qualifications,qualificationevidence,specialization,institutionoflearning,yearofuniversitystarting,yearofuniversitycompletion,totalyearsofworkexperience,state,county,constituency,phonenumber,email,nationalid,cv,previousworkexperience))

    # commit
    connection.commit( )

    # close the cursor and connection
    cursor.close()
    connection.close()

    return "Submitted successfully"


        



