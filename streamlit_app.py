""" streamlit_app.py fast geotag map app (c) 2022 Diego Carvalho
MIT License

Copyright (c) 2022 Diego Carvalho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

# COPYRIGHT SECTION
__author__ = "Diego Carvalho"
__copyright__ = "Copyright 2022, The MOBLAB Collaboration (CEFET/RJ)"
__credits__ = ["Diego Carvalho"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Diego Carvalho"
__email__ = "d.carvalho@ieee.org"
__status__ = "Research"


def show_file(uploaded_file, header, zoom):
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        s = string_data.split()

        if s[0].find("lat") == -1:
            colnames = ["lat", "lon"]
            df = pd.read_csv(uploaded_file, names=colnames, header=None)
        else:
            df = pd.read_csv(uploaded_file)
            st.write(df.columns)

        st.subheader(f"{header} ({uploaded_file.name})")
        st.map(df, zoom=zoom)

    return


st.sidebar.header("MOBLAB Cefet/RJ (c) 2022")
zoom = st.sidebar.slider("Initial Zoom", 7, 15, 10, 1)
upf1 = st.sidebar.file_uploader("Choose a File 1")
upf2 = st.sidebar.file_uploader("Choose a File 2")

# col1, col2 = st.columns(1)

# with col1:
show_file(upf1, "File 1", zoom)

# with col2:
show_file(upf2, "File 2", zoom)
