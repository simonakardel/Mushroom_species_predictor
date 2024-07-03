from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

model = load_model('mushrooms_model.h5') 

class_map = {
    0: 'Agaricus',
    1: 'Amanita',
    2: 'Boletus',
    3: 'Cortinarius',
    4: 'Entoloma',
    5: 'Hygrocybe',
    6: 'Lactarius',
    7: 'Russula',
    8: 'Suillus'
}

mushroom_descriptions = {
    'Agaricus': 'Agaricus is a genus of mushrooms containing both edible and poisonous species, with possibly over 300 members worldwide. They are characterized by having a cap that is flat when mature, gills beneath the cap, and a partial veil that often forms a ring around the stem.',
    'Amanita': 'The Amanita genus contains some of the most iconic and deadly fungi in the world, like the death cap (Amanita phalloides) and the fly agaric (Amanita muscaria). It´s important to note that while some Amanita species are edible, accurate identification is crucial as some members are deadly poisonous.',
    'Boletus': 'The Boletus genus includes the widely recognized and sought-after porcini mushroom (Boletus edulis). Mushrooms in this genus have a characteristic sponge-like surface beneath their cap instead of gills.',
    'Cortinarius': 'The Cortinarius genus is the largest genus of mushrooms in the world. Species in this genus can be identified by their rusty brown spore print and the cobweb-like cortina (veil) that covers the gills when young.',
    'Entoloma': 'Entoloma is a large genus of pink-spored gilled mushrooms, many of which are not well-documented due to their difficulty in identification. While some species are edible, others are poisonous and can cause gastrointestinal distress.',
    'Hygrocybe': 'Hygrocybe is a genus of typically small to medium-sized gilled mushrooms, widely distributed worldwide. They are known for their bright colors and waxy appearance.',
    'Lactarius': 'Known as the milk-caps, members of the Lactarius genus release a milky fluid (latex) if the mushroom tissue is damaged. This genus includes both edible and poisonous species.',
    'Russula': 'he Russula genus includes approximately 750 species of mushrooms characterized by their brittle flesh, and typically brightly colored caps. Many are edible, but care must be taken as some can cause mild to severe gastrointestinal upset.',
    'Suillus': 'Suillus is a genus of boletes closely associated with coniferous trees. They are known for their slimy caps and the presence of a ring or veil remnants on the stem. Most Suillus species are edible.'
}



@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            image = request.files['image']
            temp_path = "temp.jpg"
            image.save(temp_path)
            img = load_img(temp_path, target_size=(224, 224))
            x = img_to_array(img) / 255.0
            x = np.expand_dims(x, axis=0)
            print(x.shape) 
            
            predictions = model.predict(x)
            predicted_class = np.argmax(predictions[0])
            predicted_class_name = class_map[predicted_class]

            # Mapping the class name to its description
            class_description = mushroom_descriptions[predicted_class_name]

            os.remove(temp_path)

            # Returns the prediction and the description as a JSON response
            return jsonify({'prediction': predicted_class_name, 'description': class_description})
  
        except Exception as e:
            return jsonify({'error': str(e)})

    else:  # GET request
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)  
