<!-- ABOUT THE PROJECT -->
## About The Project

This project illustrates my knowledge about the basic data visualisation in Matplotlib; using additional libraries, including pandas & numpy.
This project contains:
* A python file: plot.py. This file demonstrates the use of libraries in visualising the needed graph. This graph is about the correlation between nutritions in food & drinks at Starbucks.
* 2 CSV files: starbucks-menu-nutrition-drinks.csv, starbucks-menu-nutrition-food.csv. This file is the data file, which I found and download from Kaggle (a sharing data site). [Link](https://www.kaggle.com/datasets/starbucks/starbucks-menu?select=starbucks_drinkMenu_expanded.csv) to the dataset.
* A png file: Starbucks_Nutrition.png. This file is the resulting graph from the python code.
This project aims to get used to the additional libraries, which are useful in data manipulating & data visualisation: matplotlib, pandas, numpy & seaborn.

<!-- GETTING STARTED -->
## Getting Started

You should have installed a Python IDE, in which you could edit & writing codes. There are multiple Python IDEs, or even text editor.
**If you are using a TextEditor, you would have to run by terminal**

### Prerequisites

Because of that, I would recommend using a IDE, in order for additional support; some of the IDEs I would recommend:
1. Pycharm
2. Visual Studio Code
3. Spyder (via Anaconda Navigator)
The information of download I will let it down here:
[Pycharm](https://www.jetbrains.com/pycharm/download)
[Visual Studio Code](https://code.visualstudio.com/download)
[Anaconda Navigator](https://www.anaconda.com/products/distribution)

### Installation

You should install the recommended libraries, including matplotlib, pandas & numpy.
* maplotlib
  ```sh
    python -m pip install -U pip
    python -m pip install -U matplotlib
  ```
  or
  ```sh
    python -m pip install -U pip
    pip install matplotlib
  ```
  
* numpy
  ```sh
    python -m pip install -U numpy
  ```
  or
  ```sh
    pip install numpy
  ```

* seaborn
  ```sh
    python -m pip install -U pip
    python -m pip install -U seaborn
  ```
  or
  ```sh
    python -m pip install -U pip
    pip install seaborn
  ```

* pandas
  ```sh
    python -m pip install -U pip
    python -m pip install -U pandas
  ```
  or
  ```sh
    python -m pip install -U pip
    pip install pandas
  ```

After that, you will have to import into your python file by:
  ```sh
    import maplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
  ```

<!-- USAGE EXAMPLES -->
## Usage

You can see and have an overview how those libaries are used in Data Science.
* Matplotlib is a library in drawing graphs.
* Numpy is a library in manipulating numeric in Python.
* Pandas is a library in dealing with dataframe in Python.
* Seaborn is a library assisting drawing graphs like Matplotlib with some extra features.Furthermore, seaborn is able to provide example datasets.

Through the codes in the project, you can have a view how I'm dealing with the data from an open-source dataset.
Here are the steps that I used to approach a dataset so far:
1. Have an overview on what information in this dataset can be used.
2. Evaluate the value of the information
3. Extract the information needed to visualisation.
4. Start graphing and adding details to the graph.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Duy Chinh Dinh - [@Linkedin](https://www.linkedin.com/in/duychinhdinh/) - chinh.dinhduy03@gmail.com