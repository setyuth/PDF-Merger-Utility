# PDF Merger Utility

A lightweight, user-friendly Windows desktop application built with Python to combine multiple PDF files into a single document. Version 2.0.0 introduces a modern Drag-and-Drop interface and workflow automation.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ New in v2.0.0
* **Drag & Drop Support:** You can now drag files directly from your desktop into the app window.
* **Auto-Open:** The folder containing your merged file opens automatically after processing.
* **UI Improvements:** Added version badge and instructional prompts.

## 🚀 Features
* **Batch Import:** Add multiple PDF files via file browser or Drag & Drop.
* **Manual Reordering:** Use "Move Up" and "Move Down" buttons to ensure the perfect page sequence.
* **Smart Parsing:** Automatically handles file paths even if they contain spaces.
* **Standalone Utility:** Can be built into a single `.exe` file that runs without Python installed.

## 🛠️ Installation & Setup

### Prerequisites
To run the source code, you need **Python 3.x** and the following libraries:

```bash
pip install pypdf tkinterdnd2 pyinstaller
```

### Running the App

```bash
python PDFMerger_v2.py
```

## 📦 How to Build the Executable (.exe)

**Important:** Because this version uses `tkinterdnd2` for drag-and-drop, the build command is different from standard Python scripts. You must use the `--collect-all` flag to include the necessary system hooks.

1. Open your terminal/command prompt.
2. Run the following command:
```bash
pyinstaller --noconsole --onefile --collect-all tkinterdnd2 PDFMerger_v2.py
```

3. Your standalone application will appear in the `dist/` folder.

## 📖 User Guide

1. **Launch:** Open `PDFMerger Utility`.
2. **Add Files:** Drag PDF files into the white box, or click **➕ Add Manually**.
3. **Organize:** Select a file and use the **↑** or **↓** arrows to change the order.
4. **Merge:** Click **MERGE NOW**.
5. **Finish:** Choose a save location. The folder will open automatically once done.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---

### 🚀 Major Update: v2.0.0

This release focuses on User Experience (UX) improvements, making it faster and easier to merge documents.

### 🆕 What's New
- **Drag & Drop Support:** Completely replaced the static list view with a Drop-enabled zone. Users can now drag PDFs directly from Explorer into the app.
- **Workflow Automation:** The application now automatically opens the destination folder after a successful merge, saving you the extra clicks to find your file.
- **UI Polish:** Added clear instructional text and a version badge to the interface.
- **Bug Fixes:** Improved file path parsing for filenames containing spaces.

### 📦 How to Use
Download the `PDFMerger.exe` attached below. No installation is required—just double-click and run!