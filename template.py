{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnr2g5txQD9ixLevnKG54M",
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
        "<a href=\"https://colab.research.google.com/github/Kavin-Hanzo/soil_test/blob/main/template.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UntJHboLNCi7",
        "outputId": "e7f634e5-27a8-4809-c878-8f445bae4b6e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: destination path 'soil_test' already exists and is not an empty directory.\n"
          ]
        }
      ],
      "source": [
        "!git clone \"https://github.com/Kavin-Hanzo/soil_test.git\""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from pathlib import Path # for windows path\n",
        "import logging"
      ],
      "metadata": {
        "id": "bgOzm_n-RDfv"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\n",
        "project_name = 'soiltester'\n",
        "list_of_files = [\n",
        "    \".github/workflows/.gitkeep\",\n",
        "    f\"src/{project_name}/__init__.py\",\n",
        "    f\"src/{project_name}/components/__init__.py\",\n",
        "    f\"src/{project_name}/utils/__init__.py\",\n",
        "    f\"src/{project_name}/config/__init__.py\",\n",
        "    f\"src/{project_name}/config/configuration.py\",\n",
        "    f\"src/{project_name}/pipeline/__init__.py\",\n",
        "    f\"src/{project_name}/entity/__init__.py\",\n",
        "    f\"src/{project_name}/constants/__init__.py\",\n",
        "    \"config/config.yaml\",\n",
        "    \"params.yaml\",\n",
        "    \"app.py\",\n",
        "    \"main.py\",\n",
        "    \"Dockerfile\",\n",
        "    \"requirements.txt\",\n",
        "    \"setup.py\",\n",
        "    \"research/trials.ipynb\", #for notebook experiments\n",
        "]"
      ],
      "metadata": {
        "id": "pL1D5MJiRKcT"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for filepath in list_of_files:\n",
        "  filepath = Path(filepath)\n",
        "  filedir,filename = os.path.split(filepath)\n",
        "  if filedir != \"\":\n",
        "    os.makedirs(filedir,exist_ok=True)\n",
        "    logging.info(f\"creating file directory : {filedir} for the file :{filename}\")\n",
        "  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):            # filepath checking,(presence of file)\n",
        "    with open(filepath ,'w') as f:\n",
        "      pass\n",
        "      logging.info(f\"creating empty file: {filepath }\")\n",
        "  else:\n",
        "    logging.info(f\"{filename} already exists\")"
      ],
      "metadata": {
        "id": "0YZxdeyrSCM3"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Pushing to GitHub\n",
        "!git add .\n",
        "!git commit -m \"Folder Structure Created\"\n",
        "!git push origin main"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BfmrEkfiVlG8",
        "outputId": "8465c89c-0da3-4823-8275-f62117b495c6"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n",
            "fatal: not a git repository (or any of the parent directories): .git\n",
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ]
        }
      ]
    }
  ]
}