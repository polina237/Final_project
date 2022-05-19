# Final_project


## Model predict last_price_log(rent) by using rooms, area, renovation, amount


## First step: Information about source data and some statistics


Dataset (155391 rows)

 *  Correlation
 
<img width="318" alt="image" src="https://user-images.githubusercontent.com/91419407/169224496-2f5cc602-f74e-48f1-885b-432c2f8e2342.png">


<img width="547" alt="image" src="https://user-images.githubusercontent.com/91419407/169150769-bc1bf823-877f-4791-b29c-67cdb2c0583b.png">


## Second step: Information about model
*Modeltype = 1 (RandomForest) or 2 (CatBoost)

* Rooms = total amount of rooms

* Area = total area

* Renovation = number of years remaining before renovation 

* Amount = difference between last day and first day


I have used **RandomForestRegressor** and **CatBoostRegressor**

* train_df = rent_df_cleaned[(rent_df_cleaned.first_day_exposition >= '2015-01-01') & (rent_df_cleaned.first_day_exposition < '2017-02-01')]


<img width="232" alt="image" src="https://user-images.githubusercontent.com/91419407/169220322-ab9b6cf1-37b0-4561-92cb-c6f52b5e0523.png">


* test_df = rent_df_cleaned[(rent_df_cleaned.first_day_exposition >= '2017-02-01') & (rent_df_cleaned.first_day_exposition < '2018-01-01')]


* holdout_df = rent_df_cleaned[rent_df_cleaned.first_day_exposition >= '2018-01-01']


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


## Third step: How to install instructions and run your app with virtual environment 

**Run your VM**

    virtualenv .env -p python3.7
    source .env/bin/activate
    pip install -r requirements.txt
    python app.py


## Fourth step: Information about Dockerfile and describe it’s content

**Dockerfile**

    from ubuntu:20.04
    MAINTAINER Polina Golubeva
    RUN apt-get update -y
    COPY . /opt/Final_project
    WORKDIR /opt/Final_project
    RUN apt install -y python3-pip
    RUN pip3 install -r requirements.txt
    CMD python3 app.py

## Fifth step: How to open the port in your remote VM

**Use Postman**

http://--.---.--.---:5444/predict_price?modeltype=1&rooms=2&area=40&renovation=2&amount=50

<img width="647" alt="image" src="https://user-images.githubusercontent.com/91419407/169163628-f92afca6-70f0-447a-86b9-b0d4881eddfd.png">
<img width="640" alt="image" src="https://user-images.githubusercontent.com/91419407/169163678-37648819-a0f8-4198-a186-a5e3f61b5339.png">



##  Sixth step: How to run app using docker and which port it uses

**Build containers and run them**

We build container by using

    docker build -t your_name/docker_folder:v.0.something .

We launch the container
  
    docker run --network host -it your_name/docker_folder:v.0.something . /bin/bash
    docker run --network host -d your_name/docker_folder:v.0.something .
    
We check running container

    docker ps
    
We stop the container

    docker stop <container name>
