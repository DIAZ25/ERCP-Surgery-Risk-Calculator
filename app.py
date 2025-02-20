import tensorflow as tf
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2b872d1b219327b71ad7737e1ede3f50974a69f6ab046d5'


@app.route('/', methods=['GET'])
def index():
	print("index function called")
	print(request.method)
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	#requesting variable from front end
	print("result function called")
	print(request.method)
	firstName = request.form['first']
	lastName = request.form['last']
	age = float(request.form['age'])
	gender = float(request.form['gender'])
	htncomplicn = float(request.form['htncomplicn'])
	thyroidcncr = float(request.form['thyroidcncr'])
	hr_min_day1 = float(request.form['hr_min_day1'])
	hr_max_day1 = float(request.form['hr_max_day1'])
	sys_bp_min_day1 = float(request.form['sys_bp_min_day1'])
	sys_bp_max_day1 = float(request.form['sys_bp_max_day1'])

	#print all the variables in the console once to debug
	print([gender,age,hr_min_day1,hr_max_day1,sys_bp_min_day1,sys_bp_max_day1,thyroidcncr,htncomplicn])

	#load model and predict
	dnn_model = tf.keras.models.load_model(r'C:\Users\zaidj\OneDrive\Documents\NHS Calculator\mortality_prediction_model_epoch_480.h5')
	
	#pass the variables in a nested list format inside the model to predict the outputs 
	pred = dnn_model.predict([[gender,age,hr_min_day1,hr_max_day1,sys_bp_min_day1,sys_bp_max_day1,thyroidcncr,htncomplicn]])
	
	#printing prediction in logs
	print(pred)
	mr = pred[0][0]
	mortality_rate = round((100-(mr*100)),2) #to calculate the success rate because 0=alive and 1=death
	#return "Surgery Success Rate: "+str(mortality_rate) + "%"
	mortality_rate = str(mortality_rate) + "%"
	return render_template('result.html', mortality_rate=mortality_rate)
	
if __name__ == '__main__':
    app.run(debug=True)


