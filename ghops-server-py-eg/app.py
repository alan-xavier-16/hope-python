'''
Grasshopper Hops python servers example
This python module helps you create python (specifically CPython) functions and use them inside your Grasshopper scripts using the new Hops components
'''

# import flask, ghhops_server, and rhino3dm (automatically installed with ghhops_server)
from flask import Flask
import ghhops_server as hs
import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

'''
Creates a Hops Python component that takes a curve and number as input and returns coordinates of a point at given parameter on the curve.
- @hops.component decorator to decorate the function pointat(curve, t) as a Hops component, where the first argument ("/pointat") is the URL of this component on our server and the rest are information that Grasshopper needs to visualize the component on its canvas, show the input and outputs, icon, description, and the rest.
- Note: Uses Hops predefined parameter types (e.g. HopsCurve) to define the inputs and outputs which is necessary so Hops knows which exact Grasshopper data type we want to use.
'''


@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along curve",
    icon="assets/bmw.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate"),
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point on curve at t")
    ]
)
def pointat(curve, t):
    return curve.PointAt(t)


if __name__ == "__main__":
    app.run()
