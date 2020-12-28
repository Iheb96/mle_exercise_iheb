# mle_exercise_iheb

 Work on posos exercise.
 For now i am using TD-IDF encoder and a basic svm as decoder.
 
*trainer.py is the training file.
-Running this file will generate two files that save the encoder and decoder data. You can see the training and validation score.

*ML_API.py is the api.
-Running this file will load the saved files in a new model.

To run this part. Use the following command in cmd.
$ uvicorn ML_API:app --reload
You should be able to test the prediction function in this adress in browser: http://127.0.0.1:8000/docs#/default/predict_items__item_id__get

There you can write a question/test for the prediction function and execute it to see the resulting predicted class.

By : Iheb BEN SALEM