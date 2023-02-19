{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Linear Regression.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPYKVn24Z0fCYDg6xLOC9rx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vincejferrante/BMR-Calculator/blob/main/Linear_Regression.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "5PojARGtx4X-"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset = pd.read_csv('50_Startups.csv')\n",
        "X = dataset.iloc[:, :-1].values\n",
        "Y = dataset.iloc[:, -1].values"
      ],
      "metadata": {
        "id": "tK_Ony_7x7Gv"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.compose import ColumnTransformer\n",
        "from sklearn.preprocessing import OneHotEncoder\n",
        "ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')\n",
        "X = np.array(ct.fit_transform(X))"
      ],
      "metadata": {
        "id": "-giUbyBoyWxb"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LVB5g89T0blI",
        "outputId": "012941a6-3c81-409f-dbc4-694e56fab216"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0.0 0.0 1.0 165349.2 136897.8 471784.1]\n",
            " [1.0 0.0 0.0 162597.7 151377.59 443898.53]\n",
            " [0.0 1.0 0.0 153441.51 101145.55 407934.54]\n",
            " [0.0 0.0 1.0 144372.41 118671.85 383199.62]\n",
            " [0.0 1.0 0.0 142107.34 91391.77 366168.42]\n",
            " [0.0 0.0 1.0 131876.9 99814.71 362861.36]\n",
            " [1.0 0.0 0.0 134615.46 147198.87 127716.82]\n",
            " [0.0 1.0 0.0 130298.13 145530.06 323876.68]\n",
            " [0.0 0.0 1.0 120542.52 148718.95 311613.29]\n",
            " [1.0 0.0 0.0 123334.88 108679.17 304981.62]\n",
            " [0.0 1.0 0.0 101913.08 110594.11 229160.95]\n",
            " [1.0 0.0 0.0 100671.96 91790.61 249744.55]\n",
            " [0.0 1.0 0.0 93863.75 127320.38 249839.44]\n",
            " [1.0 0.0 0.0 91992.39 135495.07 252664.93]\n",
            " [0.0 1.0 0.0 119943.24 156547.42 256512.92]\n",
            " [0.0 0.0 1.0 114523.61 122616.84 261776.23]\n",
            " [1.0 0.0 0.0 78013.11 121597.55 264346.06]\n",
            " [0.0 0.0 1.0 94657.16 145077.58 282574.31]\n",
            " [0.0 1.0 0.0 91749.16 114175.79 294919.57]\n",
            " [0.0 0.0 1.0 86419.7 153514.11 0.0]\n",
            " [1.0 0.0 0.0 76253.86 113867.3 298664.47]\n",
            " [0.0 0.0 1.0 78389.47 153773.43 299737.29]\n",
            " [0.0 1.0 0.0 73994.56 122782.75 303319.26]\n",
            " [0.0 1.0 0.0 67532.53 105751.03 304768.73]\n",
            " [0.0 0.0 1.0 77044.01 99281.34 140574.81]\n",
            " [1.0 0.0 0.0 64664.71 139553.16 137962.62]\n",
            " [0.0 1.0 0.0 75328.87 144135.98 134050.07]\n",
            " [0.0 0.0 1.0 72107.6 127864.55 353183.81]\n",
            " [0.0 1.0 0.0 66051.52 182645.56 118148.2]\n",
            " [0.0 0.0 1.0 65605.48 153032.06 107138.38]\n",
            " [0.0 1.0 0.0 61994.48 115641.28 91131.24]\n",
            " [0.0 0.0 1.0 61136.38 152701.92 88218.23]\n",
            " [1.0 0.0 0.0 63408.86 129219.61 46085.25]\n",
            " [0.0 1.0 0.0 55493.95 103057.49 214634.81]\n",
            " [1.0 0.0 0.0 46426.07 157693.92 210797.67]\n",
            " [0.0 0.0 1.0 46014.02 85047.44 205517.64]\n",
            " [0.0 1.0 0.0 28663.76 127056.21 201126.82]\n",
            " [1.0 0.0 0.0 44069.95 51283.14 197029.42]\n",
            " [0.0 0.0 1.0 20229.59 65947.93 185265.1]\n",
            " [1.0 0.0 0.0 38558.51 82982.09 174999.3]\n",
            " [1.0 0.0 0.0 28754.33 118546.05 172795.67]\n",
            " [0.0 1.0 0.0 27892.92 84710.77 164470.71]\n",
            " [1.0 0.0 0.0 23640.93 96189.63 148001.11]\n",
            " [0.0 0.0 1.0 15505.73 127382.3 35534.17]\n",
            " [1.0 0.0 0.0 22177.74 154806.14 28334.72]\n",
            " [0.0 0.0 1.0 1000.23 124153.04 1903.93]\n",
            " [0.0 1.0 0.0 1315.46 115816.21 297114.46]\n",
            " [1.0 0.0 0.0 0.0 135426.92 0.0]\n",
            " [0.0 0.0 1.0 542.05 51743.15 0.0]\n",
            " [1.0 0.0 0.0 0.0 116983.8 45173.06]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)"
      ],
      "metadata": {
        "id": "ElOWhDFv1S4j"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "regressor = LinearRegression()\n",
        "regressor.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x-_2P_EY2pwa",
        "outputId": "379e35de-200d-426b-a93c-a40b11c984ed"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = regressor.predict(X_test)\n",
        "np.set_printoptions(precision=2)\n",
        "print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MDt5Kdgi3Rii",
        "outputId": "bf474c12-ef77-471f-ab64-983f28783ef8"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[103015.2  103282.38]\n",
            " [132582.28 144259.4 ]\n",
            " [132447.74 146121.95]\n",
            " [ 71976.1   77798.83]\n",
            " [178537.48 191050.39]\n",
            " [116161.24 105008.31]\n",
            " [ 67851.69  81229.06]\n",
            " [ 98791.73  97483.56]\n",
            " [113969.44 110352.25]\n",
            " [167921.07 166187.94]]\n"
          ]
        }
      ]
    }
  ]
}
