# # #gradio app
# # import gradio as gr

# # def greet(name, intensity):
# #      return "Hello, " + name + "!" * int(intensity)

# # demo = gr.Interface(
# #      fn=greet,
# #      inputs=["text", "slider"],
# #      outputs=["text"],
# #  )

# # demo.launch() 
# import gradio as gr
# import joblib
# import pandas as pd
# from model import predict  # Import your prediction function

# # Load the trained model
# model = joblib.load('models/model.pkl')

# # Define the Gradio interface (adapt inputs/outputs to your needs)
# iface = gr.Interface(
#     fn=predict,
#     inputs=gr.inputs.Dataframe(headers=["Feature 1", "Feature 2", ...]),
#     outputs="text",
#     title="Random Forest Model",
#     description="Enter input values to get a prediction."
# )

# iface.launch()
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()