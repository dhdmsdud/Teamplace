from django.shortcuts import render
# import numpy as np
# import pandas as pd
# import os
# import matplotlib.pyplot as plt
# from django.conf import settings

# Create your views here.

def index(request) :
    return render(request, 'index.html')