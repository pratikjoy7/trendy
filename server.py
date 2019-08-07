import os

from flask import Flask, render_template, request
from werkzeug import secure_filename
import pandas
import matplotlib.pyplot as plt

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = set(['xlsx'])
SEMESTERS = {
    'Spring': 1,
    'Summer': 2,
    'Autumn': 3
}

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_FOLDER


def generate_chart(filename):
    df = pandas.read_excel(filename, sheet_name='Sheet1')

    autumn_2019_data = df.loc[(df['year'] == 2019) & (df['Semester'] == 3)]
    schools = autumn_2019_data.groupby(['School'])['no. of Student'].sum()
    for school in schools:
        print school
    # plt.plot(autumn_2019_data['School'], autumn_2019_data['no. of Student'])
    # plt.show()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['dataFile']
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = os.path.join(app.config['UPLOAD_DIR'], secure_filename(uploaded_file.filename))
            uploaded_file.save(filename)
            generate_chart(filename)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=9999)
