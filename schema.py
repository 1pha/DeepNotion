def get_schema(opt=None):


    if opt is None:
        return {
            "title": {"name": "Epochs", "type": "text"},

            "Train Loss": {"name": "Train Loss", "type": "number"},
            "Train Acc": {"name": "Train Acc", "type": "number"},

            "Test Loss": {"name": "Test Loss", "type": "number"},
            "Test Acc": {"name": "Test Acc", "type": "number"},
        }

    elif opt is 'fold':
        return {
            "title" : {"name" : "Epoch/Config", "type" : "text"},

            'Train MAE' : {'name': 'Train MAE', "type": "number"},
            'Train LOSS': {'name': 'Train LOSS', "type": "number"},
            'Train RMSE': {'name': 'Train RMSE', "type": "number"},
            'Train CORR': {'name': 'Train CORR', "type": "number"},

            'Valid MAE' : {'name': 'Valid MAE', "type": "number"},
            'Valid LOSS': {'name': 'Valid LOSS', "type": "number"},
            'Valid RMSE': {'name': 'Valid RMSE', "type": "number"},
            'Valid CORR': {'name': 'Valid CORR', "type": "number"},

            'Aug MAE' : {'name': 'Aug MAE', "type": "number"},
            'Aug LOSS': {'name': 'Aug LOSS', "type": "number"},
            'Aug RMSE': {'name': 'Aug RMSE', "type": "number"},
            'Aug CORR': {'name': 'Aug CORR', "type": "number"},

            'Learning Rate': {'name': 'Learning Rate', "type": "number"},
            'Elapsed Time': {'name': 'Elapsed Time', "type": "number"},
        }

    elif opt is 'test':
        return {
            'Fold': {'name': 'Fold', "type": "text"},

            'Test MAE' : {'name': 'Test MAE', "type": "number"},
            'Test LOSS': {'name': 'Test LOSS', "type": "number"},
            'Test RMSE': {'name': 'Test RMSE', "type": "number"},           
            'Test CORR': {'name': 'Test CORR', "type": "number"},   
        }

    elif opt is 'debug':
        return {
            'title': {'name': 'Epoch', "type": "text"},
            'call' : {'name': 'real', 'type': 'number'}
        }
