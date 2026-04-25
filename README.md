# 🔐 Multi-Format Encoder/Decoder with Auto Detection

## 📌 Overview

This project is a command-line tool that supports encoding and decoding of multiple formats including **Base64, Base32, Hexadecimal, and URL encoding**. It also features **automatic format detection**, making it useful for security testing, data analysis, and general-purpose encoding tasks.

Encoding is not encryption—it simply transforms data into different representations for safe transmission and storage.

---

## 🚀 Features

* ✅ Base64 encode & decode
* ✅ Base32 support (RFC 4648 compliant)
* ✅ Hexadecimal conversion (multiple formats)
* ✅ URL encoding/decoding (standard + form encoding)
* ✅ Automatic format detection with confidence scoring
* ✅ CLI interface (arguments, stdin, file input)
* ✅ Batch processing & interactive mode

---

## 🧠 Key Concepts

* Data encoding vs encryption
* Pattern recognition for format detection
* Binary and string data handling
* CLI tool design

---

## ⚙️ Supported Formats

### 1. Base64

* Uses 64 printable characters
* Common in tokens, certificates, APIs
* Handles padding using `=`

### 2. Base32

* Uses A–Z and 2–7
* More restrictive environments
* Produces longer output than Base64

### 3. Hexadecimal

* Represents bytes as `00–FF`
* Used in low-level and binary analysis
* Supports multiple output styles:

  * Plain
  * Space-separated
  * Colon-separated (e.g., MAC addresses)

### 4. URL Encoding

* Encodes unsafe characters as `%HH`
* Supports:

  * Standard encoding (`%20` for space)
  * Form encoding (`+` for space)

---

## 🔍 Automatic Detection

The tool detects encoding formats using pattern matching:

| Format | Pattern                               |
| ------ | ------------------------------------- |
| Base64 | `A-Za-z0-9+/=` (length multiple of 4) |
| Base32 | `A-Z2-7=`                             |
| Hex    | `0-9A-Fa-f`                           |
| URL    | `%XX` patterns                        |

Outputs include a **confidence score** and possible alternatives.

---

## 💻 Installation

```bash
git clone https://github.com/your-username/encoder-decoder.git
cd encoder-decoder
pip install -r requirements.txt
```

---

## 🛠️ Usage

### Basic Usage

```bash
python main.py encode base64 "hello"
python main.py decode base64 "aGVsbG8="
```

### Auto Detection

```bash
python main.py detect "aGVsbG8="
```

### From File

```bash
python main.py encode base64 -f input.txt
```

### Interactive Mode

```bash
python main.py interactive
```

---

## 📦 Examples

| Input       | Format | Output         |
| ----------- | ------ | -------------- |
| hello       | Base64 | aGVsbG8=       |
| hello       | Hex    | 68 65 6c 6c 6f |
| hello world | URL    | hello%20world  |

---

## ⚠️ Common Issues

* Missing Base64 padding (`=`)
* Unicode encoding errors
* Case sensitivity in Base32
* Misidentification in auto-detection (low confidence cases)

---

## 🔐 Security Use Cases

* Decode tokens and encoded payloads
* Analyze encoded data in web requests
* Inspect binary data in hex format
* Reverse engineer encoded values

---

## 📁 Project Structure

```
encoder-decoder/
│── main.py
│── encoder/
│   ├── base64.py
│   ├── base32.py
│   ├── hex.py
│   └── url.py
│── detector/
│   └── detect.py
│── utils/
│   └── helpers.py
│── requirements.txt
│── README.md
```

---

## 🎯 Deliverables

* Multi-format encoding/decoding tool
* Automatic format detection system
* CLI with batch & interactive modes
* Documentation with examples

---

## 📌 Future Improvements

* Add Base58 and Base85 support
* Web UI version
* API integration
* Improved detection using ML heuristics

---

## 👨‍💻 Author

Dex

---

## 📜 License

This project is licensed under the MIT License.

### How to add MIT License

1. Create a file named `LICENSE` in your project root
2. Paste the following template and replace `[year]` and `[your name]`

```
MIT License

Copyright (c) [year] [your name]

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

💡 Example:

```
Copyright (c) 2026 Dex
```
