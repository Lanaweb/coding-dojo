from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
    
@app.route('/dojo')
def success():
  return 'Dojo'

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(name):
    #print(name)
    return 'Hi, ' + name

@app.route('/repeat/<int:times>/<string>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat_string_times(times, string):
#    if type(times) != int:
#        return "Sorry! No response. Try again."
#
#    else:
    return string * times

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
