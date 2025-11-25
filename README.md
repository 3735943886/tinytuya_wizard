# TinyTuya Wizard2

**tinytuya-wizard** is an interactive wizard for discovering registered devices on Tuya Cloud.

---

## 🔧 Features
- QR code login via SmartLife / Tuya app
- Automatic cloud credential handling
- Fetch Tuya device information from the cloud
- Optional local network scan to match IPs

---

## 📦 Installation
```bash
pip install tinytuya-wizard
```

---

## ▶️ Usage

### Standard execution

```bash
python3 -m tinytuya-wizard
```

---

## ⚙️ Command-line Options

| Option                   | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| `-max_time`              | Maximum time to find devices during polling (default: 18)                         |
| `-force` / `-f`          | Force scan device IP addresses                                                    |
| `-nocolor`               | Disable colored terminal output                                                   |
| `-yes` / `-y`            | Automatically answer *yes* to prompts                                             |
| `-no-poll` / `-no`       | Skip local IP polling (overrides `-yes`)                                          |
| `-device-file FILE`      | Path for storing the device list JSON                                             |
| `-credentials-file FILE` | Path for storing cloud credentials JSON                                           |

Example:

```bash
tinytuya-wizard 60 -y -force
```

---

## 💾 Output

Upon completion, the wizard writes the following:

* Cloud credentials JSON
* Device informations JSON

---

## 📌 Example Workflow

1. Run `tinytuya-wizard`
2. Scan the QR code using SmartLife / Tuya app
3. Devices are fetched from the cloud
4. (Optional) Perform local LAN scan to resolve IPs and firmware versions
5. Results are saved to JSON files

---

## ❗ Notes

* This project does not modify `tinytuya` — it is an interactive wrapper focused on simplicity and usability.

---

## 🪪 License

MIT License

---

## 💬 Contributions

Issues and pull requests are welcome.

---
