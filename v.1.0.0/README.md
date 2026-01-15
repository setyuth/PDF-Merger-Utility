# PDF Merger Utility

A lightweight, user-friendly Windows desktop application built with Python to combine multiple PDF files into a single document. This tool allows users to import PDFs, reorder them manually to ensure the correct sequence, and export the final result with one click.

## ✨ Features

* **Batch Import:** Add multiple PDF files at once.
* **Manual Reordering:** Use "Move Up" and "Move Down" buttons to organize your files exactly how you want them in the final document.
* **Remove Tool:** Easily remove accidental additions from the list.
* **Clean UI:** Simple, no-nonsense interface for quick tasks.
* **Open Source:** Free to use, modify, and distribute under the MIT License.

## 🚀 Getting Started

### Prerequisites

To run this tool from the source code, you need:

* **Python 3.x** installed on your system.
* The `pypdf` library.

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/PDF-Merger-Utility.git
cd PDF-Merger-Utility

```


2. **Install dependencies:**
```bash
pip install pypdf

```


3. **Run the application:**
```bash
python PDFMerger.py

```



---

## 📖 User Guide

Using the PDF Merger is straightforward:

1. **Add Files:** Click the **Add Files...** button to select the PDFs you want to combine.
2. **Organize:** * Click on a file name in the list to select it.
* Click **Move Up ↑** or **Move Down ↓** to change the order. The final PDF will be merged from top to bottom.


3. **Remove:** If you made a mistake, select the file and click **Remove Selected**.
4. **Merge:** Click the green **MERGE PDFS** button. A window will pop up asking you where to save your new file and what to name it.
5. **Success:** Once the process is complete, a success message will appear.

---

## 🛠️ How to Build an Executable (.exe)

If you want to create a standalone version that runs without Python:

1. Install PyInstaller: `pip install pyinstaller`
2. Run: `pyinstaller --onefile --noconsole PDFMerger.py`
3. Find your `PDFMerger.exe` in the `dist` folder.

---

## 📄 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Yuth Set

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

```

---
## Current Version
**v1.0.0** (Initial Release)