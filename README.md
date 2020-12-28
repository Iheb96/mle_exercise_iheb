# mle_exercise_iheb <br />

 Work on posos exercise. <br />
 For now i am using TD-IDF encoder and a basic svm as decoder. <br />

*trainer.py is the training file.
-Running this file will generate two files that save the encoder and decoder data. You can see the training and validation score.<br />

*ML_API.py is the api.<br />
-Running this file will load the saved files in a new model.

To run this part. Use the following command in cmd.<br />
$ uvicorn ML_API:app --reload<br />
You should be able to test the prediction function in this adress in browser: http://127.0.0.1:8000/docs#/default/predict_items__item_id__get<br />

There you can write a question/test for the prediction function and execute it to see the resulting predicted class.<br />

By : Iheb BEN SALEM