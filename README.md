# Reproduce ClearML getting stuck in multi-processing:

<b>Reproduced on:</b><br/>
Python 3.8.6 | OS: Ubuntu 16.04.7 LTS (with GPU)<br/>
Python 3.6.9 | OS: Ubuntu 18.04.5 LTS (without GPU)<br/>

<b>Not reproduced on:</b><br/>
Python 3.8.12 | OS: Windows 10 (without GPU)

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Run this ~10 times, atleast once, it will get stuck:
python multiprocess_bug_reproduction.py
```
