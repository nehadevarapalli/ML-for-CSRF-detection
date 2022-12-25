from sklearn.model_selection import train_test_split
class MLConcepts:
    def startPOSTProcess(self,df):
        print(df.head())
        df = df[['numOfParams', 'numOfBools', 'numOfIds','numOfBlobs','reqLen','isPOST']]
        #df_get = df[['numOfParams', 'numOfBools', 'numOfIds', 'numOfBlobs', 'reqLen', 'isGET']]
        X = df[['numOfParams', 'numOfBools', 'numOfIds','numOfBlobs','reqLen']]
        y = df[['isPOST']]
        X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=0)
        from sklearn.ensemble import RandomForestClassifier
        regressor = RandomForestClassifier()
        regressor.fit(X_train, y_train)
        # Predecting The test Result
        y_pred = regressor.predict(X_test)
        # Need to implement Accuracy, Precession and recall
        from sklearn.metrics import accuracy_score
        accuracy = accuracy_score(y_pred.round(), y_test)
        print('POST Accuracy=', accuracy)
        from sklearn.metrics import precision_score
        precision = precision_score(y_pred.round(), y_test)
        print("POST Precession=", precision)
        from sklearn.metrics import recall_score
        recall = recall_score(y_pred.round(), y_test)
        print("POST Recall=", recall)
        post_dict = {"post_accuracy":accuracy,"post_precision":precision,"post_recall":recall}
        return post_dict

    def startGETProcess(self,df):
        print(df.head())
        df = df[['numOfParams', 'numOfBools', 'numOfIds','numOfBlobs','reqLen','isGET']]
        X = df[['numOfParams', 'numOfBools', 'numOfIds','numOfBlobs','reqLen']]
        y = df[['isGET']]
        X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=0)
        from sklearn.ensemble import RandomForestClassifier
        regressor = RandomForestClassifier()
        regressor.fit(X_train, y_train)
        # Predecting The test Result
        y_pred = regressor.predict(X_test)
        # Need to implement Accuracy, Precession and recall
        from sklearn.metrics import accuracy_score
        accuracy = accuracy_score(y_pred.round(), y_test)
        print('GET Accuracy=', accuracy)
        from sklearn.metrics import precision_score
        precision = precision_score(y_pred.round(), y_test)
        print("GET Precession=", precision)
        from sklearn.metrics import recall_score
        recall = recall_score(y_pred.round(), y_test)
        print("GET Recall=", recall)
        get_dict = {"get_accuracy": accuracy, "get_precision":precision, "get_recall": recall}
        return get_dict

    def startOPTIONProcess(self,df):
        print(df.head())
        df = df[['numOfParams', 'numOfBools', 'numOfIds','numOfBlobs','reqLen','isOPTIONS']]
        X = df[['numOfParams', 'numOfBools', 'numOfIds','numOfBlobs','reqLen']]
        y = df[['isOPTIONS']]
        X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=0)
        from sklearn.ensemble import RandomForestClassifier
        regressor = RandomForestClassifier()
        regressor.fit(X_train, y_train)
        # Predecting The test Result
        y_pred = regressor.predict(X_test)
        # Need to implement Accuracy, Precession and recall
        from sklearn.metrics import accuracy_score
        accuracy = accuracy_score(y_pred.round(), y_test)
        print('OPTION Accuracy=', accuracy)
        from sklearn.metrics import precision_score
        precision = precision_score(y_pred.round(), y_test)
        print("OPTION Precession=", precision)
        from sklearn.metrics import recall_score
        recall = recall_score(y_pred.round(), y_test)
        print("OPTION Recall=", recall)
        ooption_dict = {"option_accuracy": accuracy, "option_precision":precision, "option_recall": recall}
        return ooption_dict

