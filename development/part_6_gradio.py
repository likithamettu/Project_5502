
import pickle
import pandas as pd

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


def predict_subscribe(watch, duration, ctr, interest):
    data = [{"watch_time": watch, "avg_view_duration": duration, "click_through_rate": ctr, "interest": interest}]
    sample = pd.DataFrame(data)
    pred = model.predict_proba(sample.values)[0]
    return {'Misses Out': pred[0], 'Subscribes': pred[1]}

# print(predict_subscribe(-8.1, 1.4, -0.7, 0))

# # def predict_subscribe(watch, duration, ctr, interest):
# import gradio as gr

# watch = gr.Slider(minimum=-9, maximum=12, label="Watch")
# duration = gr.Slider(minimum=-4, maximum=4, label="Duration")
# ctr = gr.Slider(minimum=-5, maximum=5, label="Click Through Rate")
# interest = gr.Radio([0, 1], label="Interest")

# gr.Interface(predict_subscribe, [watch, duration, ctr, interest], "label", live=False).launch();!