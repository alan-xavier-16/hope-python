'''
Grasshopper Hops - Addition example
'''

# import flask, ghhops_server, and rhino3dm (automatically installed with ghhops_server)
from unicodedata import category
from flask import Flask
import ghhops_server as hs
import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

'''
Creates a Hops Python component that takes two numbers as input and returns the sum.
- @hops.component decorator to decorate the function pointat(curve, t) as a Hops component, where the first argument ("/pointat") is the URL of this component on our server and the rest are information that Grasshopper needs to visualize the component on its canvas, show the input and outputs, icon, description, and the rest.
- Note: Uses Hops predefined parameter types (e.g. HopsCurve) to define the inputs and outputs which is necessary so Hops knows which exact Grasshopper data type we want to use.
'''


@hops.component(
    "/add",
    name="Add",
    description="Add numbers",
    category="Math",
    icon="assets/bmw.png",
    inputs=[
        hs.HopsNumber("a", "a", "Curve to evaluate"),
        hs.HopsNumber("b", "b", "Parameter on Curve to evaluate"),
    ],
    outputs=[
        hs.HopsNumber("Sum", "s", "a+b")
    ]
)
def add(a, b):
    print(a+b)
    return a+b


if __name__ == "__main__":
    app.run()
