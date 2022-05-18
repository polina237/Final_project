# Final_project


#**Model predict last_price_log(rent) by using rooms, area, renovation, amount**


#**First step: Information about source data and some statistics **


Dataset (155391 rows)

<img width="547" alt="image" src="https://user-images.githubusercontent.com/91419407/169150769-bc1bf823-877f-4791-b29c-67cdb2c0583b.png">


#**Second step: Information about model**

*Rooms = total amount of rooms*

*Area = total area*

*Renovation = number of years remaining before renovation* 

*Amount = difference between last day and first day*


I have used **RandomForestRegressor** and **CatBoostRegressor**

*train_df = rent_df_cleaned[(rent_df_cleaned.first_day_exposition >= '2015-01-01') & (rent_df_cleaned.first_day_exposition < '2017-02-01')]*


*test_df = rent_df_cleaned[(rent_df_cleaned.first_day_exposition >= '2017-02-01') & (rent_df_cleaned.first_day_exposition < '2018-01-01')]*


*holdout_df = rent_df_cleaned[rent_df_cleaned.first_day_exposition >= '2018-01-01']*


*Random forest regressors*

<img width="662" alt="image" src="https://user-images.githubusercontent.com/91419407/169151297-95436890-4eab-42b4-8c8d-c51f2f9f4bfe.png">

MAE: 0.580286469383839
MSE: 0.5287821515002182
RMSE: 0.7271740861033335

*CatBoost regressors*

<img width="662" alt="image" src="https://user-images.githubusercontent.com/91419407/169151471-79e9b52f-e065-4714-9c65-c73ad7531639.png">

MAE: 0.5925005350172596
MSE: 0.5486212726848376
RMSE: 0.7406897276760611


#**Third step: How to install instructions and run your app with virtual environment **

*Run your VM*

virtualenv .env -p python3.7

source .env/bin/activate

pip install -r requirements.txt

python app.py

