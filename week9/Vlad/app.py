from flask import Flask, render_template ,request,jsonify
from logic import save_user,search_user
import os
app = Flask(__name__)
thisfolder = os.path.dirname(os.path.abspath(__file__))
 
@app.route('/', methods=['POST', 'GET'])
@app.route('/home' , methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        person = {
            'name':request.form.get('user_first_name'),
            'surname':request.form.get('user_last_name'),
            'age':request.form.get('user_age'),
            'gender':request.form.get('user_gender')
        }
        save_user(person,f'{thisfolder}/data.json')
    return render_template('feedback.html')

@app.route('/search', methods=['GET'])
def search():
    data = request.args.get('user_search')
    search_result =  search_user(data,f'{thisfolder}/data.json')
    if search_result :
        return render_template('user_info.html',result=search_result)
    return render_template('search.html')

 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True,port=8000)