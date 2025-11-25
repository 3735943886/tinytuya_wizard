# TinyTuya Wizard

**tinytuya_wizard** is an interactive wizard for discovering registered devices on Tuya Cloud.

---

## 🔧 Features
- QR code login via SmartLife / Tuya app
- Automatic cloud credential handling
- Fetch Tuya device information from the cloud
- Optional local network scan to match IPs

---

## 📦 Installation
```bash
pip install tinytuya_wizard
```

---

## ▶️ Usage

### Standard execution

```bash
python3 -m tinytuya_wizard
```

---

## ⚙️ Command-line Options

| Option                   | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| `max_time`               | Maximum time to find devices during polling (default: 18)                         |
| `-force` / `-f`          | Force scan device IP addresses                                                    |
| `-nocolor`               | Disable colored terminal output                                                   |
| `-yes` / `-y`            | Automatically answer *yes* to prompts                                             |
| `-no-poll` / `-no`       | Skip local IP polling (overrides `-yes`)                                          |
| `-device-file FILE`      | Path for storing the device list JSON                                             |
| `-credentials-file FILE` | Path for storing cloud credentials JSON                                           |

---

## 💾 Output

Upon completion, the wizard writes the following:

* Cloud credentials JSON
* Device informations JSON

---

## ❗ Notes

* This project does not modify `tinytuya` — it is an interactive wrapper focused on simplicity and usability.
* Currently using temporary `Home Assistant` client credentials. Intended to be replaced when 3rd Party credentials become available.
* **Warning** `tinytuya.json` will be replaced with new QR-based credentials information.

---
