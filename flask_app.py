from flask import Flask, render_template, request
import pickle
ml_model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def house():
    if request.method == 'GET':
        return render_template('HOUSE.html')
    elif request.method == 'POST':
        print("Post Request received")
        size=float(request.form.get('size'))
        bedrooms=int(request.form.get('bedrooms'))
        bathrooms=float(request.form.get('bathrooms'))
        age=int(request.form.get('age'))
        distance=int(request.form.get('distance'))
        Pred_Price_arr = ml_model.predict([[size,bedrooms,bathrooms,age,distance]])
        Pred_Price = Pred_Price_arr[0]
        total = round(Pred_Price, 2)
        return render_template('pp.html',  total=total)


if __name__ == '__main__':
    app.run(debug=True)