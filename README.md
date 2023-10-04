
# ConvolutionNeuralNetwork With Deployment
This project utilises Flask to serve a webpage that interacts with saved tensorflow model for image classification of digits in SVHN dataset. 

This is the codebase that was created as part of this tutorial here:

[![Youtube video link](https://i9.ytimg.com/vi_webp/kbLSJIWFLQA/mq1.webp?sqp=CKSV86gG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEggWChlMA8=&rs=AOn4CLCJA3nBVL4PABo_EuwEP98DX-4DBg)](https://youtu.be/kbLSJIWFLQA)

I performed model training, tuning and testing in Google Colab using GPU runtime.

Then saved the tuned model as .h5 file.

Loaded the saved model in app.py.

Submitted pictures of digits via the form submission in the webapp.

Model showed satisfactory results.

## Dependencies
Install the dependencies 
``` bash
pip install -r requirements.txt
```

> **Please Note** This project used Python 3.11 or higher 

## Usage
1. To run locally either run from the IDE(I used VScode) or use the following command:
```bash
python app.py
```

2. Open your web browser and visit `http://localhost:3000`
3. Select an image of a digit,  click on the `Predict Image` button to submit.


