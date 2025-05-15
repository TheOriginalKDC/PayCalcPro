# PayCalcPro

PayCalcPro is a professional-grade desktop application for calculating weekly pay, including overtime. It features a clean, user-friendly interface and supports common overtime rate types such as time and a half or double time.

## Features

- Simple, modern GUI  
- Calculates regular and overtime pay  
- Built-in overtime options: time and a half, double time, or custom multiplier  
- No installation needed — portable `.exe` for Windows  
- Fully embedded icon  

## How to Use

1. Open the app (`PayCalcPro.exe`)  
2. Enter total hours worked  
3. Enter base pay rate (hourly)  
4. Select an overtime rate (or enter a custom one)  
5. Click **Calculate Pay** to see results  

## Developer Notes

Clone the repo:  
`git clone https://github.com/theoriginalkdc/PayCalcPro.git`  
`cd PayCalcPro`  
`python main.py`  

To rebuild the `.exe` with icon:  
`pyinstaller --noconsole --onefile --icon=PayCalcPro_Icon.ico main.py`  

## Files Included

- `main.py` – Launch point for the app  
- `gui.py` – Handles all UI rendering and interaction  
- `logic.py` – Contains pay calculation logic  
- `PayCalcPro_Icon.ico` – Embedded icon for the app  
- `dist/PayCalcPro.exe` – Final built app (after packaging)  

## License

Internal use only. All rights reserved © theoriginalkdc
