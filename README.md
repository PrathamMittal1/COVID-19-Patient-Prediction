# COVID-19-Patient-Prediction

The main feature of Covid-19 Patient Prediction project is that, the dataset used is not any built-in one nor it is taken from any internet resource.

The dataset has been created by visiting around 20 recent patients who applied for RTPCR and antigen testing.
Features like cough, running nose, breathing difficulty, fever, body pain, redness of skin, blood pressure,
and weakness were recorded of each patient then corresponding result of their Covid-19 tests were recorded as target label.
Then all data recorded was saved in a excel sheet.

The application is created without a console terminal window.
Its interface contains a series of checkboxes to be selected as the patient’s symptoms.
After selecting the symptoms, we have to hit the submit button to predict whether patient is corona positive or negative.

The logic behind this prediction is K Neighbours Classifier.
