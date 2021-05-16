# Homework №1

## Prerequisites

* Python >= 3.8
* pip >= 20.1.1
* [Heart Disease UCI Dataset](https://www.kaggle.com/ronitf/heart-disease-uci) (put the dataset in data/raw folder)

## Installation

### For development

```bash
git clone https://github.com/made-ml-in-prod-2021/iseman1993.git
git checkout homework1
cd ml_project
python -m venv .venv
source .venv/bin/activate (.venv\Scripts\activate for windows)
pip install -r requirements.txt
```


## Project structure

------------

    ├── config                        <- Configuration files for project modules.
    │   ├── logging_config.yaml
    │   ├── lr_train_config.yaml
    │   ├── lr_predict_config.yaml
    │   ├── rf_train_config.yaml
    │   └── rf_predict_config.yaml
    │
    ├── data
    │   └── raw                        <- The original, immutable data dump.
    │
    ├── models                         <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks                      <- Jupyter notebooks.
    │
    ├── src                            <- Source code for use in this project.
    │   ├── __init__.py                <- Makes src a Python module.
    │   │
    │   ├── data                       <- Scripts to download or generate data.
    │   │   └── make_dataset.py
    │   │
    │   ├── entities                   <- Parameters for different project modules.
    │   │   ├── feature_params.py
    │   │   ├── model_params.py
    │   │   ├── predict_pipeline_params.py
    │   │   ├── split_params.py
    │   │   └── train_pipeline_params.py    
    │   │
    │   ├── features                   <- Scripts to turn raw data into features for modeling.
    │   │   ├── build_features.py
    │   │   └── custom_transformer.py  
    │   │
    │   └── models                     <- Scripts to train models and then use trained models to make
    │       │                             predictions.
    │       └── classifier.py
    │
    ├── LICENSE
    │
    ├── log_info.log                   <- Training and prediction log file.
    │
    ├── README.md                      <- The top-level README for developers using this project.
    │
    ├── requirements.txt               <- The requirements file for reproducing the analysis environment, e.g.
    │                                     generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                       <- Makes project pip installable (pip install -e .) so src can be imported.
    │
    ├── train_pipeline.py              <- Train script.
    │
    └── predict_pipeline.py            <- Predict script.




## Usage


### Train model

```bash
python3 src/train_pipeline.py configs/lr_train_config.yaml
```

### Predict with model

```bash
python3 src/predict_pipeline.py configs/lr_predict_config.yaml
```



------------

## Самоанализ


| # |  | Description | Score |
| --- | --- | --- | --- |
| -2 | :ballot_box_with_check: | Назовите ветку homework1 | 1 |
| -1 | :ballot_box_with_check: | Положите код в папку heart_disease | - |
| 0 | :ballot_box_with_check: | В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код | 2 |
| 1 | :ballot_box_with_check:| Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов) Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы) Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл) | 3 |
| 2 | :ballot_box_with_check: | Проект имеет модульную структуру(не все в одном файле =) ) (2 баллов) | 2 |
| 3 | :ballot_box_with_check: | Использованы логгеры (2 балла) | 3 |
| 4 | :black_square_button: | Написаны тесты на ные к реальнотдельные модули и на прогон всего пайплайна(3 баллов) | 0 |
| 5 | :black_square_button: | Для тестов генерируются синтетические данные, приближеным (3 баллов) | 0 |
| 6 | :ballot_box_with_check: | Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла) | 3 | 
| 7 | :ballot_box_with_check: | Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) | 3 |
| 8 | :ballot_box_with_check: | Используйте кастомный трансформер(написанный своими руками) и протестируйте его(3 балла) | 3 |
| 9 | :ballot_box_with_check: | Обучите модель, запишите в readme как это предлагается (3 балла) | 3 |
| 10 | :ballot_box_with_check: |Напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3 балла) | 0 |
| 11 | :black_square_button: | Используется hydra  (https://hydra.cc/docs/intro/) (3 балла - доп баллы) | 3 |
| 12 | :black_square_button: | Настроен CI(прогон тестов, линтера) на основе github actions  (3 балла - доп баллы (будем проходить дальше в курсе, но если есть желание поразбираться - welcome) | 0 | 
| 13 | :ballot_box_with_check: | Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1 балл доп баллы) | 1 |

------------

### Итоговый балл 27 * 0.65  = 17.55
