# ArtificialVisionForPartsInspection

### Colaboradores: 
-Ricardo Ruiz Almanza A01383658
-Cuauhtemoc Maldonado A01067820
-Luis Carlos Ramos Zazueta A00839010
-Marilu Flores Turon Ramirez A00836898

### Abstract
Inteligencia artificial Computacional

Para generar modelos de inteligencia artificial precisos se necesitan grandes cantidades de información, esta es procesada por el propio modelo para así dar una salida de información acertada al objetivo. Los modelos que detectan objetos de manera visual requieren de una gran cantidad de imágenes y clasificaciones. You Only Look Once, es un algoritmo de visión por computadora utilizado para la detección de objetos en tiempo real creando cuadros delimitadores. Uno de los mayores problemas en la generación de modelos para detección de objetos es la recopilación de datos ya sean imágenes o video. Esto debido a la cantidad de fotos, etiquetas y organización de las clasificaciones que los modelos necesitan para su continuo entrenamiento, haciendo más laboriosa la recopilación de información que el generar el modelo. Nuestro objetivo es generar un modelo eficiente de inteligencia artificial de clasificación utilizando modelos 3D renderizados para una recolección de datos rápida, esto aplicado al proyecto FrED Factory y los más de 100 componentes mecánicos utilizados durante la construcción de uno de los extrusores. Durante la investigación y trabajo de este proyecto utilizando Blender hemos desarrollado un código utilizando el API integrado del programa para poder automatizar el proceso de aleatoriedad de diferentes factores ambientales y de posición con el objetivo de mejorar la calidad y diversidad de los datos. Así mismo este automatiza el etiquetado de las imágenes al inferir las coordenadas de los polígonos dentro del render. Estos datos son transferidos a un código de python que utiliza el programa de You Only Look Once que procesa la imagen completa en tiempo real utilizando una webcam. Utilizando un raspberry pi 4 los datos de entrenamiento se procesan para que teniendo en mano uno de los componentes de FrED se identifique en tiempo real el nombre y número de la pieza con precisión.

Development of an efficient artificial intelligence classification model using computer-generated rendered 3D models for fast data collection, applied to the FrED Factory project mechanical components used during the building of one of its extruders.

Large amounts of information are needed to generate accurate artificial intelligence models. The model itself processes this information to output accurate information to the target. Models that detect objects visually require a large number of images and classifications. 

During the research and work on this project using Blender we have developed a code using the program's integrated API to automate the randomization process of different environmental and position factors to improve the quality and diversity of the data. It also automates the labeling of the images by inferring the coordinates of the polygons within the render. This data is transferred to a Python code that uses the You Only Look Once program that processes the complete image in real-time using a webcam. The training data is processed so that when having one of the FrED components in hand, the name and number of the part can be accurately identified in real-time by the AI model.

The accuracy of the computer-generated images based on the rendered 3D models and the speed of data delivery give a range of success rates for the real-life application of the AI model.

As a deliverable, we will conduct research on which configurations for the blender model are the most accurate when entering them into the AI program.

Our goal and impact are to reduce the amount of time needed in the collection of visual data for the development of Artificial Intelligence models. 
