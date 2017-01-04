import pandas as pd
import pickle

class C1:
    def def1(self):
        data = pd.read_csv('d1_test.csv', header=None, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
        print('\n')

        with open('test3_model.pkl', 'rb') as f:
            classifier = pickle.load(f)

        del data['col1']

        predicted_set = classifier.predict(data)
        prob_predicted = classifier.predict_proba(data)

        data = pd.DataFrame(data, columns=["col1", "col2", "col3", "col4", "col5", "col6"])
        pred = pd.DataFrame(predicted_set, columns=["col7"])
        df_prob = pd.DataFrame(prob_predicted, columns=["col8", "col9"])

        frame1 = [data,pred]
        df1 = pd.concat(frame1,axis=1, join_axes=[data.index])
        frame2 = [df1,df_prob]
        df2 = pd.concat(frame2,axis=1, join_axes=[data.index])


        df2['col10'] = df2['col9'].map(lambda x: 'Low' if x < 0.5 else 'Medium' if x < 0.75 else 'High')
        del df2['col1']
        return df2
