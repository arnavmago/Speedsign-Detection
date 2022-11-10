Developed a web app that takes a photo of the road as input, recognizes if the photo has any road signs and if the photo has a speed sign it extrapolates the speed limit given on the speed sign. It can also tell you if your car is going over the speed limit by giving a pop-up on the HUD of the car.

Front end - Streamlit + HTML + CSS

Back end - Python, Tensorflow library, Faster R-CNN neural network

Instructions - 
1. In model/faster_rcnn_resnet50 unzip the inference-graph.7z file using the 7-zip extension (or anything else) 
2. After extraction ensure that the structure is of the form model/faster_rcnn_resnet50/inference_graph where -
  Inference_graph has onlt 1 file called frozen_inference_graph.pb.
  (thus, path of frozen_inference_graph.pb is - model/faster_rcnn_resnet50/inference_graph/frozen_inference_graph.pb)
