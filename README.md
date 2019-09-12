---
tags: Website-Filter-Testing-Tool, ChromeDrive
---
website-filter 
===
- A testing tool for websites filter which develope by Taiwan MoE.
- Only support chrome.
- If there are some problem, please contact me by using the <a mailto:hanhan3927@gmail.com>mail</a>

## Build the Program
- Please reference the "<b>Note</b>"

## Convert PY(python file) to EXE(execution)
- please use <b>pyinstaller</b> to create the execution ,and please use the <b>main.spec</b> config file.
- please config the <b>main.spec</b> config file before you create the execution because there is some parameter which could be reconfig.

## How to use the Program
1. Open..(開檔): 目前只支援csv，後續會加入json檔，且目前只能開啟純網頁url列表
2. Run(執行測試): 檔案讀取後，按Run執行。
3. Stop(終止測試): 執行後"Run"按鈕會改變為"Stop"，按下Stop可終止測試，按鈕變回Run，終止後重按Run會重頭開始測試。
4. Save..(存檔):將結果存檔，檔案名稱與附檔名需自行輸入。

## Note

1. The Version only support the "Chrome" browser
2. These files is the main code file, other code files are belong the "selenium" package, and the reason is there has a code file "config.py" must edit when the program is be package into a execution.
	- WF/Main.py
	- WF/ConnectWebsite.py
	- WF/UI.py
	- WF/Var.py

3. If you want to package this project into a execution by using "Pyinstaller", you must edit the "config.py", you should change the code A to code B, because the path of setting file "default.ini" will be change in the execution.

	- Code A 
	``_default_config_path = os.path.join(os.path.dirname(__file__), 'default.ini')``

	- Code B 
	``_default_config_path = os.path.join(os.path.dirname(__file__), 'default.ini/default.ini')``