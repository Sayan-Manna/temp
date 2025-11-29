/Downloads/githubstockprediction  ➤➤➤  python app.py                                                                
Traceback (most recent call last):
  File "/Users/sayanmanna/Downloads/githubstockprediction/app.py", line 1, in <module>
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'
 ~/Downloads/githubstockprediction  ➤➤➤  pip install flask flask-cors yfinance pandas statsmodels
Collecting flask
  Downloading flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting flask-cors
  Downloading flask_cors-6.0.1-py3-none-any.whl.metadata (5.3 kB)
Collecting yfinance
  Downloading yfinance-0.2.66-py2.py3-none-any.whl.metadata (6.0 kB)
Collecting pandas
  Downloading pandas-2.3.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (91 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.2/91.2 kB 1.1 MB/s eta 0:00:00
Collecting statsmodels
  Downloading statsmodels-0.14.5-cp311-cp311-macosx_11_0_arm64.whl.metadata (9.5 kB)
Collecting blinker>=1.9.0 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Downloading markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from flask)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting numpy>=1.16.5 (from yfinance)
  Downloading numpy-2.3.5-cp311-cp311-macosx_14_0_arm64.whl.metadata (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 3.6 MB/s eta 0:00:00
Collecting requests>=2.31 (from yfinance)
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting multitasking>=0.0.7 (from yfinance)
  Downloading multitasking-0.0.12.tar.gz (19 kB)
  Preparing metadata (setup.py) ... done
Collecting platformdirs>=2.0.0 (from yfinance)
  Downloading platformdirs-4.5.0-py3-none-any.whl.metadata (12 kB)
Collecting pytz>=2022.5 (from yfinance)
  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting frozendict>=2.3.4 (from yfinance)
  Downloading frozendict-2.4.7-py3-none-any.whl.metadata (23 kB)
Collecting peewee>=3.16.2 (from yfinance)
  Downloading peewee-3.18.3.tar.gz (3.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 6.8 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting beautifulsoup4>=4.11.1 (from yfinance)
  Downloading beautifulsoup4-4.14.2-py3-none-any.whl.metadata (3.8 kB)
Collecting curl_cffi>=0.7 (from yfinance)
  Downloading curl_cffi-0.13.0-cp39-abi3-macosx_11_0_arm64.whl.metadata (13 kB)
Collecting protobuf>=3.19.0 (from yfinance)
  Downloading protobuf-6.33.1-cp39-abi3-macosx_10_9_universal2.whl.metadata (593 bytes)
Collecting websockets>=13.0 (from yfinance)
  Downloading websockets-15.0.1-cp311-cp311-macosx_11_0_arm64.whl.metadata (6.8 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzdata>=2022.7 (from pandas)
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting scipy!=1.9.2,>=1.8 (from statsmodels)
  Downloading scipy-1.16.3-cp311-cp311-macosx_14_0_arm64.whl.metadata (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.0/62.0 kB 4.0 MB/s eta 0:00:00
Collecting patsy>=0.5.6 (from statsmodels)
  Downloading patsy-1.0.2-py2.py3-none-any.whl.metadata (3.6 kB)
Collecting packaging>=21.3 (from statsmodels)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting soupsieve>1.2 (from beautifulsoup4>=4.11.1->yfinance)
  Using cached soupsieve-2.8-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4>=4.11.1->yfinance)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting cffi>=1.12.0 (from curl_cffi>=0.7->yfinance)
  Downloading cffi-2.0.0-cp311-cp311-macosx_11_0_arm64.whl.metadata (2.6 kB)
Collecting certifi>=2024.2.2 (from curl_cffi>=0.7->yfinance)
  Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.31->yfinance)
  Downloading charset_normalizer-3.4.4-cp311-cp311-macosx_10_9_universal2.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests>=2.31->yfinance)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests>=2.31->yfinance)
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting pycparser (from cffi>=1.12.0->curl_cffi>=0.7->yfinance)
  Using cached pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
Downloading flask-3.1.2-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.3/103.3 kB 4.8 MB/s eta 0:00:00
Downloading flask_cors-6.0.1-py3-none-any.whl (13 kB)
Downloading yfinance-0.2.66-py2.py3-none-any.whl (123 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.4/123.4 kB 6.1 MB/s eta 0:00:00
Downloading pandas-2.3.3-cp311-cp311-macosx_11_0_arm64.whl (10.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.8/10.8 MB 4.8 MB/s eta 0:00:00
Downloading statsmodels-0.14.5-cp311-cp311-macosx_11_0_arm64.whl (9.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.7/9.7 MB 2.2 MB/s eta 0:00:00
Downloading beautifulsoup4-4.14.2-py3-none-any.whl (106 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.4/106.4 kB 2.2 MB/s eta 0:00:00
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.3.1-py3-none-any.whl (108 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.3/108.3 kB 2.3 MB/s eta 0:00:00
Downloading curl_cffi-0.13.0-cp39-abi3-macosx_11_0_arm64.whl (3.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 2.3 MB/s eta 0:00:00
Downloading frozendict-2.4.7-py3-none-any.whl (16 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl (12 kB)
Downloading numpy-2.3.5-cp311-cp311-macosx_14_0_arm64.whl (5.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━ 4.2/5.4 MB 1.8 MB/s eta 0:00:01ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━ 4.2/5.4 MB 1.8 MB/s eta 0:00:01

[notice] A new release of pip is available: 23.3.2 -> 25.3
[notice] To update, run: python3.11 -m pip install --upgrade pip
 ~/Downloads/githubstockprediction  ➤➤➤  python app.py
Traceback (most recent call last):
  File "/Users/sayanmanna/Downloads/githubstockprediction/app.py", line 1, in <module>
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'
 ~/Downloads/githubstockprediction  ➤➤➤  which python                                                             
python: aliased to python3
 ~/Downloads/githubstockprediction  ➤➤➤  python --version
Python 3.13.2
 ~/Downloads/githubstockprediction  ➤➤➤  pip install flask                                       
Collecting flask
  Using cached flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting blinker>=1.9.0 (from flask)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask)
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Using cached markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from flask)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Using cached flask-3.1.2-py3-none-any.whl (103 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl (12 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 4.0 MB/s eta 0:00:00
Installing collected packages: markupsafe, itsdangerous, click, blinker, werkzeug, jinja2, flask
Successfully installed blinker-1.9.0 click-8.3.1 flask-3.1.2 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 werkzeug-3.1.3

[notice] A new release of pip is available: 23.3.2 -> 25.3
[notice] To update, run: python3.11 -m pip install --upgrade pip
 ~/Downloads/githubstockprediction  ➤➤➤  source venv/bin/activate

source: no such file or directory: venv/bin/activate
 ~/Downloads/githubstockprediction  ➤➤➤  source .venv/bin/activate
source: no such file or directory: .venv/bin/activate
 ~/Downloads/githubstockprediction  ➤➤➤  rm -rf .venv       
 ~/Downloads/githubstockprediction  ➤➤➤  python3 -m venv .venv
 ~/Downloads/githubstockprediction  ➤➤➤  source .venv/bin/activate
 ~/Downloads/githubstockprediction  ➤➤➤  source .venv/bin/activate
 ~/Downloads/githubstockprediction  ➤➤➤  pip install flask flask-cors yfinance pandas statsmodels
Collecting flask
  Using cached flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting flask-cors
  Using cached flask_cors-6.0.1-py3-none-any.whl.metadata (5.3 kB)
Collecting yfinance
  Using cached yfinance-0.2.66-py2.py3-none-any.whl.metadata (6.0 kB)
Collecting pandas
  Downloading pandas-2.3.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (91 kB)
Collecting statsmodels
  Downloading statsmodels-0.14.5-cp313-cp313-macosx_11_0_arm64.whl.metadata (9.5 kB)
Collecting blinker>=1.9.0 (from flask)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask)
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Downloading markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from flask)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting numpy>=1.16.5 (from yfinance)
  Downloading numpy-2.3.5-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Collecting requests>=2.31 (from yfinance)
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting multitasking>=0.0.7 (from yfinance)
  Using cached multitasking-0.0.12.tar.gz (19 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting platformdirs>=2.0.0 (from yfinance)
  Using cached platformdirs-4.5.0-py3-none-any.whl.metadata (12 kB)
Collecting pytz>=2022.5 (from yfinance)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting frozendict>=2.3.4 (from yfinance)
  Using cached frozendict-2.4.7-py3-none-any.whl.metadata (23 kB)
Collecting peewee>=3.16.2 (from yfinance)
  Using cached peewee-3.18.3.tar.gz (3.0 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting beautifulsoup4>=4.11.1 (from yfinance)
  Using cached beautifulsoup4-4.14.2-py3-none-any.whl.metadata (3.8 kB)
Collecting curl_cffi>=0.7 (from yfinance)
  Using cached curl_cffi-0.13.0-cp39-abi3-macosx_11_0_arm64.whl.metadata (13 kB)
Collecting protobuf>=3.19.0 (from yfinance)
  Using cached protobuf-6.33.1-cp39-abi3-macosx_10_9_universal2.whl.metadata (593 bytes)
Collecting websockets>=13.0 (from yfinance)
  Downloading websockets-15.0.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (6.8 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzdata>=2022.7 (from pandas)
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting scipy!=1.9.2,>=1.8 (from statsmodels)
  Downloading scipy-1.16.3-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Collecting patsy>=0.5.6 (from statsmodels)
  Using cached patsy-1.0.2-py2.py3-none-any.whl.metadata (3.6 kB)
Collecting packaging>=21.3 (from statsmodels)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting soupsieve>1.2 (from beautifulsoup4>=4.11.1->yfinance)
  Using cached soupsieve-2.8-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4>=4.11.1->yfinance)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting cffi>=1.12.0 (from curl_cffi>=0.7->yfinance)
  Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.6 kB)
Collecting certifi>=2024.2.2 (from curl_cffi>=0.7->yfinance)
  Using cached certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.31->yfinance)
  Downloading charset_normalizer-3.4.4-cp313-cp313-macosx_10_13_universal2.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests>=2.31->yfinance)
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests>=2.31->yfinance)
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting pycparser (from cffi>=1.12.0->curl_cffi>=0.7->yfinance)
  Using cached pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
Using cached flask-3.1.2-py3-none-any.whl (103 kB)
Using cached flask_cors-6.0.1-py3-none-any.whl (13 kB)
Using cached yfinance-0.2.66-py2.py3-none-any.whl (123 kB)
Downloading pandas-2.3.3-cp313-cp313-macosx_11_0_arm64.whl (10.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.7/10.7 MB 21.7 MB/s eta 0:00:00
Downloading statsmodels-0.14.5-cp313-cp313-macosx_11_0_arm64.whl (9.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.7/9.7 MB 3.5 MB/s eta 0:00:00
Using cached beautifulsoup4-4.14.2-py3-none-any.whl (106 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Using cached curl_cffi-0.13.0-cp39-abi3-macosx_11_0_arm64.whl (3.0 MB)
Using cached frozendict-2.4.7-py3-none-any.whl (16 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl (12 kB)
Downloading numpy-2.3.5-cp313-cp313-macosx_14_0_arm64.whl (5.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 2.0 MB/s eta 0:00:00
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Downloading patsy-1.0.2-py2.py3-none-any.whl (233 kB)
Downloading platformdirs-4.5.0-py3-none-any.whl (18 kB)
Downloading protobuf-6.33.1-cp39-abi3-macosx_10_9_universal2.whl (427 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Downloading scipy-1.16.3-cp313-cp313-macosx_14_0_arm64.whl (20.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.9/20.9 MB 2.4 MB/s eta 0:00:00
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Downloading websockets-15.0.1-cp313-cp313-macosx_11_0_arm64.whl (173 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl (181 kB)
Downloading charset_normalizer-3.4.4-cp313-cp313-macosx_10_13_universal2.whl (208 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached soupsieve-2.8-py3-none-any.whl (36 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Using cached pycparser-2.23-py3-none-any.whl (118 kB)
Building wheels for collected packages: multitasking, peewee
  Building wheel for multitasking (pyproject.toml) ... done
  Created wheel for multitasking: filename=multitasking-0.0.12-py3-none-any.whl size=15636 sha256=f699537189bbe4e557a47abc66a5e321e9dab8ceebbfeb3542786f216edb845c
  Stored in directory: /Users/sayanmanna/Library/Caches/pip/wheels/1e/df/0f/e2bbb22d689b30c681feb5410ab64a2523437b34c8ecfc6476
  Building wheel for peewee (pyproject.toml) ... done
  Created wheel for peewee: filename=peewee-3.18.3-cp313-cp313-macosx_15_0_arm64.whl size=283976 sha256=80894c46ea98f50be4c0ae15cdb3ce41a4a27d95a81a9c1313901b7b789c2d00
  Stored in directory: /Users/sayanmanna/Library/Caches/pip/wheels/8c/a9/a4/df972cd49f865ffde174d9c5b26f14f08f8a363ed31e10ff91
Successfully built multitasking peewee
Installing collected packages: pytz, peewee, multitasking, websockets, urllib3, tzdata, typing-extensions, soupsieve, six, pycparser, protobuf, platformdirs, packaging, numpy, markupsafe, itsdangerous, idna, frozendict, click, charset_normalizer, certifi, blinker, werkzeug, scipy, requests, python-dateutil, patsy, jinja2, cffi, beautifulsoup4, pandas, flask, curl_cffi, yfinance, statsmodels, flask-cors
ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device


[notice] A new release of pip is available: 25.0 -> 25.3
[notice] To update, run: pip install --upgrade pip
 ~/Downloads/githubstockprediction  ➤➤➤  pip install flask flask-cors yfinance pandas statsmodels
Collecting flask
  Using cached flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting flask-cors
  Using cached flask_cors-6.0.1-py3-none-any.whl.metadata (5.3 kB)
Collecting yfinance
  Using cached yfinance-0.2.66-py2.py3-none-any.whl.metadata (6.0 kB)
Collecting pandas
  Using cached pandas-2.3.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (91 kB)
Collecting statsmodels
  Using cached statsmodels-0.14.5-cp313-cp313-macosx_11_0_arm64.whl.metadata (9.5 kB)
Requirement already satisfied: blinker>=1.9.0 in ./.venv/lib/python3.13/site-packages (from flask) (1.9.0)
Requirement already satisfied: click>=8.1.3 in ./.venv/lib/python3.13/site-packages (from flask) (8.3.1)
Requirement already satisfied: itsdangerous>=2.2.0 in ./.venv/lib/python3.13/site-packages (from flask) (2.2.0)
Collecting jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Requirement already satisfied: markupsafe>=2.1.1 in ./.venv/lib/python3.13/site-packages (from flask) (3.0.3)
Requirement already satisfied: werkzeug>=3.1.0 in ./.venv/lib/python3.13/site-packages (from flask) (3.1.3)
Requirement already satisfied: numpy>=1.16.5 in ./.venv/lib/python3.13/site-packages (from yfinance) (2.3.5)
Collecting requests>=2.31 (from yfinance)
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Requirement already satisfied: multitasking>=0.0.7 in ./.venv/lib/python3.13/site-packages (from yfinance) (0.0.12)
Requirement already satisfied: platformdirs>=2.0.0 in ./.venv/lib/python3.13/site-packages (from yfinance) (4.5.0)
Requirement already satisfied: pytz>=2022.5 in ./.venv/lib/python3.13/site-packages (from yfinance) (2025.2)
Requirement already satisfied: frozendict>=2.3.4 in ./.venv/lib/python3.13/site-packages (from yfinance) (2.4.7)
Requirement already satisfied: peewee>=3.16.2 in ./.venv/lib/python3.13/site-packages (from yfinance) (3.18.3)
Collecting beautifulsoup4>=4.11.1 (from yfinance)
  Using cached beautifulsoup4-4.14.2-py3-none-any.whl.metadata (3.8 kB)
Collecting curl_cffi>=0.7 (from yfinance)
  Using cached curl_cffi-0.13.0-cp39-abi3-macosx_11_0_arm64.whl.metadata (13 kB)
Requirement already satisfied: protobuf>=3.19.0 in ./.venv/lib/python3.13/site-packages (from yfinance) (6.33.1)
Requirement already satisfied: websockets>=13.0 in ./.venv/lib/python3.13/site-packages (from yfinance) (15.0.1)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.13/site-packages (from pandas) (2025.2)
Requirement already satisfied: scipy!=1.9.2,>=1.8 in ./.venv/lib/python3.13/site-packages (from statsmodels) (1.16.3)
Collecting patsy>=0.5.6 (from statsmodels)
  Using cached patsy-1.0.2-py2.py3-none-any.whl.metadata (3.6 kB)
Requirement already satisfied: packaging>=21.3 in ./.venv/lib/python3.13/site-packages (from statsmodels) (25.0)
Requirement already satisfied: soupsieve>1.2 in ./.venv/lib/python3.13/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.8)
Requirement already satisfied: typing-extensions>=4.0.0 in ./.venv/lib/python3.13/site-packages (from beautifulsoup4>=4.11.1->yfinance) (4.15.0)
Collecting cffi>=1.12.0 (from curl_cffi>=0.7->yfinance)
  Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.6 kB)
Requirement already satisfied: certifi>=2024.2.2 in ./.venv/lib/python3.13/site-packages (from curl_cffi>=0.7->yfinance) (2025.11.12)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.13/site-packages (from requests>=2.31->yfinance) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.13/site-packages (from requests>=2.31->yfinance) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.13/site-packages (from requests>=2.31->yfinance) (2.5.0)
Requirement already satisfied: pycparser in ./.venv/lib/python3.13/site-packages (from cffi>=1.12.0->curl_cffi>=0.7->yfinance) (2.23)
Using cached flask-3.1.2-py3-none-any.whl (103 kB)
Using cached flask_cors-6.0.1-py3-none-any.whl (13 kB)
Using cached yfinance-0.2.66-py2.py3-none-any.whl (123 kB)
Using cached pandas-2.3.3-cp313-cp313-macosx_11_0_arm64.whl (10.7 MB)
Using cached statsmodels-0.14.5-cp313-cp313-macosx_11_0_arm64.whl (9.7 MB)
Using cached beautifulsoup4-4.14.2-py3-none-any.whl (106 kB)
Using cached curl_cffi-0.13.0-cp39-abi3-macosx_11_0_arm64.whl (3.0 MB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached patsy-1.0.2-py2.py3-none-any.whl (233 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl (181 kB)
Installing collected packages: requests, python-dateutil, patsy, jinja2, cffi, beautifulsoup4, pandas, flask, curl_cffi, yfinance, statsmodels, flask-cors
Successfully installed beautifulsoup4-4.14.2 cffi-2.0.0 curl_cffi-0.13.0 flask-3.1.2 flask-cors-6.0.1 jinja2-3.1.6 pandas-2.3.3 patsy-1.0.2 python-dateutil-2.9.0.post0 requests-2.32.5 statsmodels-0.14.5 yfinance-0.2.66

[notice] A new release of pip is available: 25.0 -> 25.3
[notice] To update, run: pip install --upgrade pip
 ~/Downloads/githubstockprediction  ➤➤➤  python app.py
Traceback (most recent call last):
  File "/Users/sayanmanna/Downloads/githubstockprediction/app.py", line 6, in <module>
    from statsmodels.tsa.arima.model import ARIMA
  File "/Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/statsmodels/__init__.py", line 1, in <module>
    from statsmodels.compat.patsy import monkey_patch_cat_dtype
  File "/Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/statsmodels/compat/__init__.py", line 1, in <module>
    from statsmodels.tools._test_runner import PytestTester
  File "/Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/statsmodels/tools/__init__.py", line 1, in <module>
    from .tools import add_constant, categorical
  File "/Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/statsmodels/tools/tools.py", line 6, in <module>
    import scipy.linalg
  File "/Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/scipy/linalg/__init__.py", line 222, in <module>
    from ._sketches import *
  File "/Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/scipy/linalg/_sketches.py", line 10, in <module>
    from scipy.sparse import csc_matrix, issparse
ModuleNotFoundError: No module named 'scipy.sparse'
 ~/Downloads/githubstockprediction  ➤➤➤  pip uninstall scipy statsmodels
Found existing installation: scipy 1.16.3
Uninstalling scipy-1.16.3:
  Would remove:
    /Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/scipy-1.16.3.dist-info/*
    /Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/scipy/*
Proceed (Y/n)? y                                                          
  Successfully uninstalled scipy-1.16.3
Found existing installation: statsmodels 0.14.5
Uninstalling statsmodels-0.14.5:
  Would remove:
    /Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/statsmodels-0.14.5.dist-info/*
    /Users/sayanmanna/Downloads/githubstockprediction/.venv/lib/python3.13/site-packages/statsmodels/*
Proceed (Y/n)? y
  Successfully uninstalled statsmodels-0.14.5
 ~/Downloads/githubstockprediction  ➤➤➤  pip install numpy==1.26.0 scipy==1.11.3 statsmodels==0.14.0
ERROR: Could not find a version that satisfies the requirement numpy==1.26.0 (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0, 1.11.1, 1.11.2, 1.11.3, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 1.13.3, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.21.0, 1.21.1, 1.22.0, 1.22.1, 1.22.2, 1.22.3, 1.22.4, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.23.5, 1.24.0, 1.24.1, 1.24.2, 1.24.3, 1.24.4, 1.25.0, 1.25.1, 1.25.2, 1.26.2, 1.26.3, 1.26.4, 2.0.0, 2.0.1, 2.0.2, 2.1.0, 2.1.1, 2.1.2, 2.1.3, 2.2.0, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 2.3.0, 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5)

[notice] A new release of pip is available: 25.0 -> 25.3
[notice] To update, run: pip install --upgrade pip
ERROR: No matching distribution found for numpy==1.26.0
 ~/Downloads/githubstockprediction  ➤➤➤  pip install flask flask-cors yfinance pandas            
Requirement already satisfied: flask in ./.venv/lib/python3.13/site-packages (3.1.2)
Requirement already satisfied: flask-cors in ./.venv/lib/python3.13/site-packages (6.0.1)
Requirement already satisfied: yfinance in ./.venv/lib/python3.13/site-packages (0.2.66)
Requirement already satisfied: pandas in ./.venv/lib/python3.13/site-packages (2.3.3)
Requirement already satisfied: blinker>=1.9.0 in ./.venv/lib/python3.13/site-packages (from flask) (1.9.0)
Requirement already satisfied: click>=8.1.3 in ./.venv/lib/python3.13/site-packages (from flask) (8.3.1)
Requirement already satisfied: itsdangerous>=2.2.0 in ./.venv/lib/python3.13/site-packages (from flask) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in ./.venv/lib/python3.13/site-packages (from flask) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in ./.venv/lib/python3.13/site-packages (from flask) (3.0.3)
Requirement already satisfied: werkzeug>=3.1.0 in ./.venv/lib/python3.13/site-packages (from flask) (3.1.3)
Requirement already satisfied: numpy>=1.16.5 in ./.venv/lib/python3.13/site-packages (from yfinance) (2.3.5)
Requirement already satisfied: requests>=2.31 in ./.venv/lib/python3.13/site-packages (from yfinance) (2.32.5)
Requirement already satisfied: multitasking>=0.0.7 in ./.venv/lib/python3.13/site-packages (from yfinance) (0.0.12)
Requirement already satisfied: platformdirs>=2.0.0 in ./.venv/lib/python3.13/site-packages (from yfinance) (4.5.0)
Requirement already satisfied: pytz>=2022.5 in ./.venv/lib/python3.13/site-packages (from yfinance) (2025.2)
Requirement already satisfied: frozendict>=2.3.4 in ./.venv/lib/python3.13/site-packages (from yfinance) (2.4.7)
Requirement already satisfied: peewee>=3.16.2 in ./.venv/lib/python3.13/site-packages (from yfinance) (3.18.3)
Requirement already satisfied: beautifulsoup4>=4.11.1 in ./.venv/lib/python3.13/site-packages (from yfinance) (4.14.2)
Requirement already satisfied: curl_cffi>=0.7 in ./.venv/lib/python3.13/site-packages (from yfinance) (0.13.0)
Requirement already satisfied: protobuf>=3.19.0 in ./.venv/lib/python3.13/site-packages (from yfinance) (6.33.1)
Requirement already satisfied: websockets>=13.0 in ./.venv/lib/python3.13/site-packages (from yfinance) (15.0.1)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.venv/lib/python3.13/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.13/site-packages (from pandas) (2025.2)
Requirement already satisfied: soupsieve>1.2 in ./.venv/lib/python3.13/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.8)
Requirement already satisfied: typing-extensions>=4.0.0 in ./.venv/lib/python3.13/site-packages (from beautifulsoup4>=4.11.1->yfinance) (4.15.0)
Requirement already satisfied: cffi>=1.12.0 in ./.venv/lib/python3.13/site-packages (from curl_cffi>=0.7->yfinance) (2.0.0)
Requirement already satisfied: certifi>=2024.2.2 in ./.venv/lib/python3.13/site-packages (from curl_cffi>=0.7->yfinance) (2025.11.12)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.13/site-packages (from requests>=2.31->yfinance) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.13/site-packages (from requests>=2.31->yfinance) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.13/site-packages (from requests>=2.31->yfinance) (2.5.0)
Requirement already satisfied: pycparser in ./.venv/lib/python3.13/site-packages (from cffi>=1.12.0->curl_cffi>=0.7->yfinance) (2.23)

[notice] A new release of pip is available: 25.0 -> 25.3
[notice] To update, run: pip install --upgrade pip
 ~/Downloads/githubstockprediction  ➤➤➤  python app.py
Traceback (most recent call last):
  File "/Users/sayanmanna/Downloads/githubstockprediction/app.py", line 6, in <module>
    from statsmodels.tsa.arima.model import ARIMA
ModuleNotFoundError: No module named 'statsmodels'
 ~/Downloads/githubstockprediction  ➤➤➤  pip install --upgrade pip
pip install numpy scipy
pip install statsmodels==0.14.2
Requirement already satisfied: pip in ./.venv/lib/python3.13/site-packages (25.0)
Collecting pip
  Downloading pip-25.3-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-25.3-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 17.8 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.0
    Uninstalling pip-25.0:
      Successfully uninstalled pip-25.0
Successfully installed pip-25.3
Requirement already satisfied: numpy in ./.venv/lib/python3.13/site-packages (2.3.5)
Collecting scipy
  Using cached scipy-1.16.3-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Using cached scipy-1.16.3-cp313-cp313-macosx_14_0_arm64.whl (20.9 MB)
Installing collected packages: scipy
Successfully installed scipy-1.16.3
Collecting statsmodels==0.14.2
  Downloading statsmodels-0.14.2.tar.gz (20.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.4/20.4 MB 2.7 MB/s  0:00:07
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy>=1.22.3 in ./.venv/lib/python3.13/site-packages (from statsmodels==0.14.2) (2.3.5)
Requirement already satisfied: scipy!=1.9.2,>=1.8 in ./.venv/lib/python3.13/site-packages (from statsmodels==0.14.2) (1.16.3)
Requirement already satisfied: pandas!=2.1.0,>=1.4 in ./.venv/lib/python3.13/site-packages (from statsmodels==0.14.2) (2.3.3)
Requirement already satisfied: patsy>=0.5.6 in ./.venv/lib/python3.13/site-packages (from statsmodels==0.14.2) (1.0.2)
Requirement already satisfied: packaging>=21.3 in ./.venv/lib/python3.13/site-packages (from statsmodels==0.14.2) (25.0)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.venv/lib/python3.13/site-packages (from pandas!=2.1.0,>=1.4->statsmodels==0.14.2) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.13/site-packages (from pandas!=2.1.0,>=1.4->statsmodels==0.14.2) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.13/site-packages (from pandas!=2.1.0,>=1.4->statsmodels==0.14.2) (2025.2)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas!=2.1.0,>=1.4->statsmodels==0.14.2) (1.17.0)
Building wheels for collected packages: statsmodels
  Building wheel for statsmodels (pyproject.toml) ... done
  Created wheel for statsmodels: filename=statsmodels-0.14.2-cp313-cp313-macosx_15_0_arm64.whl size=9974344 sha256=ea87765828c193cf8e8244d0dcd93c79409f76f49ebcd97ba11475c29dc6cbb0
  Stored in directory: /Users/sayanmanna/Library/Caches/pip/wheels/c3/06/7f/a0ab342b9cce684217d27b4c08ca4e966e361af3494bd196f7
Successfully built statsmodels
Installing collected packages: statsmodels
Successfully installed statsmodels-0.14.2
 ~/Downloads/githubstockprediction  ➤➤➤  python app.py                               
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 862-118-538
open index.html
127.0.0.1 - - [25/Nov/2025 21:17:23] "OPTIONS /predict HTTP/1.1" 200 -
--- Processing request for: AAPL ---
Simulating BERT sentiment for: AAPL
Fetching data from Yahoo Finance for: AAPL
[*********************100%***********************]  1 of 1 completed
Training ARIMA model...
Forecasting...
Error during model training/forecasting: 'str' object has no attribute 'strftime'
127.0.0.1 - - [25/Nov/2025 21:17:25] "POST /predict HTTP/1.1" 400 -
127.0.0.1 - - [25/Nov/2025 21:17:35] "OPTIONS /predict HTTP/1.1" 200 -
--- Processing request for: AAPL ---
Simulating BERT sentiment for: AAPL
Fetching data from Yahoo Finance for: AAPL
[*********************100%***********************]  1 of 1 completed
Training ARIMA model...
Forecasting...
Error during model training/forecasting: 'str' object has no attribute 'strftime'
127.0.0.1 - - [25/Nov/2025 21:17:35] "POST /predict HTTP/1.1" 400 -
 * Detected change in '/Users/sayanmanna/Downloads/githubstockprediction/app.py', reloading
 * Restarting with stat
  File "/Users/sayanmanna/Downloads/githubstockprediction/app.py", line 58
    last_30_days = model_data.tail(30)
IndentationError: unexpected indent
 ~/Downloads/githubstockprediction  ➤➤➤  open index.html
 ~/Downloads/githubstockprediction  ➤➤➤  python app.py  
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 862-118-538
127.0.0.1 - - [25/Nov/2025 21:22:08] "OPTIONS /predict HTTP/1.1" 200 -
--- Processing request for: AAPL ---
Simulating BERT sentiment for: AAPL
Fetching data from Yahoo Finance for: AAPL
[*********************100%***********************]  1 of 1 completed
Training ARIMA model...
Forecasting...
127.0.0.1 - - [25/Nov/2025 21:22:09] "POST /predict HTTP/1.1" 200 -
 * Detected change in '/Users/sayanmanna/Downloads/githubstockprediction/app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 862-118-538
127.0.0.1 - - [25/Nov/2025 21:22:56] "OPTIONS /predict HTTP/1.1" 200 -
--- Processing request for: AAPL ---
Simulating BERT sentiment for: AAPL
Fetching data from Yahoo Finance for: AAPL
[*********************100%***********************]  1 of 1 completed
Training ARIMA model...
Forecasting...
127.0.0.1 - - [25/Nov/2025 21:22:56] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [25/Nov/2025 21:24:09] "OPTIONS /predict HTTP/1.1" 200 -
--- Processing request for: AAPL ---
Simulating BERT sentiment for: AAPL
Fetching data from Yahoo Finance for: AAPL
[*********************100%***********************]  1 of 1 completed
Training ARIMA model...
Forecasting...
127.0.0.1 - - [25/Nov/2025 21:24:10] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [25/Nov/2025 21:24:50] "OPTIONS /predict HTTP/1.1" 200 -
--- Processing request for: GOOGL ---
Simulating BERT sentiment for: GOOGL
Fetching data from Yahoo Finance for: GOOGL
[*********************100%***********************]  1 of 1 completed
Training ARIMA model...
Forecasting...
127.0.0.1 - - [25/Nov/2025 21:24:51] "POST /predict HTTP/1.1" 200 -
