# ERCP-Surgery-Risk-Calculator

## Surgery Risk Calculator Prototype Instructions:

The prototype includes a few main files attached along, for example: app.py, index.html, results.html, mortality_prediction_model_epoch_480.h5

Install python (latest version) on your pc

I used Visual Studio Code (VS Code) to run the code files and setup the flask server.

In VS Code terminal create a python virtual environment by typing python3 -m venv venv

Type venv\scripts\activate after the previous command to activate the virtual environment. A (venv) would appear before the directory after that.  


The app.py file uses only 2 packages for now: Flask and Tensorflow

So, install the packages by typing in pip install flask  and   pip install tensorflow   one after another. This would install the packages on your python virtual environment.


Then in app.py change the code a little to put the right directory for the model .h5 file to be loaded.


Then open in terminal the directory for NHS Calculator folder and run app.py by typing python app.py

The model’s Google Colab notebook can be found here https://colab.research.google.com/drive/1NeTMuOtv72X0FOmfCKHBrydRYjQfook6?usp=sharing
