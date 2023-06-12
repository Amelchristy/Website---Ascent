from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot_route')
def plot_route():
    return render_template('plot.html')

if __name__ == '__main__':
    app.run(debug=True)
