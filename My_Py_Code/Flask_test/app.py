import MySQLdb
from flask import Flask, render_template


app = Flask(__name__, static_folder='./templates', static_url_path='')


@app.route('/')
def home():
    db = MySQLdb.connect(unix_socket="/var/run/mysqld/mysqld.sock",db="sisdb",read_default_file="~/.my.cnf")
    db.autocommit(True)
    cur = db.cursor()
    
    sql_query = """SELECT * FROM students ORDER BY id ASC"""
    cur.execute(sql_query)
    final_res = cur.fetchall()
    
    db.close()
    
    students_list = []
    for i in final_res:
        students_list.append((str(i[1]), i[2], i[0]))
        
    return render_template('index.html', students_list=students_list)

@app.route('/add/<name>/<age>')
def add(name,age):
    db = MySQLdb.connect(unix_socket="/var/run/mysqld/mysqld.sock",db="sisdb",read_default_file="~/.my.cnf")
    db.autocommit(True)
    cur = db.cursor()
    
    sql_query = """SELECT * FROM students ORDER BY id ASC"""
    cur.execute(sql_query)
    final_res = cur.fetchall()
    db_user_id = final_res[-1:][0][0]+1
      
    data_to_insert = {'id': db_user_id, 'name': name, 'age': age}
    sql_query = "INSERT INTO `students` VALUES (%(id)s, %(name)s, %(age)s)"
    cur.execute(sql_query, data_to_insert)
    
    cur.close()
    db.close()
    
    link = """ inserted. Return to main page: <a href="http://195.64.154.204:5000/" />http://195.64.154.204:5000/</a>"""
    
    return 'OK, ' + name + link


@app.route('/del/<user_id>')
def delete(user_id):
    db = MySQLdb.connect(unix_socket="/var/run/mysqld/mysqld.sock",db="sisdb",read_default_file="~/.my.cnf")
    db.autocommit(True)
    cur = db.cursor()
    
    sql_query = ("""DELETE FROM students WHERE id="""+str(user_id))
    cur.execute(sql_query)
    
    cur.close()
    db.close()
    
    link = """ has been removed. Return to main page: <a href="http://195.64.154.204:5000/" />http://195.64.154.204:5000/</a>"""
    
    return 'OK, user with ID ' + user_id + link
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    