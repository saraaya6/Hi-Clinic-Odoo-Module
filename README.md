# Hi Clinic Management Module (Odoo 18 Community)

An advanced, production-ready Odoo 18 Community custom module that redefines clinical workflows by combining smart appointment scheduling with operational efficiency and waste tracking principles.

## 🌟 Key Features

### 1. Bilingual UI (Arabic / English)
* Every field label, menu item, Kanban stage, and view header is strictly designed to display both Arabic and English simultaneously (e.g., `اسم المريض / Patient Name`) to ensure seamless communication among diverse clinic staff.

### 2. Smart Patient Records (`hi.patient`)
* Manages complete digital profiles for patients (Name, Age, Gender, Phone).
* Includes a computed performance metric: **إجمالي وقت البقاء بالدقائق / Total Stay Time (Minutes)** to track the precise time a patient spends from check-in to discharge, exposing clinic bottlenecks.

### 3. Appointment & Notification System (`hi.appointment`)
* Full scheduling workflow management (Draft, Scheduled, Checked In, Completed, Cancelled).
* Built-in automated communication trackers:
  * **Day Before Reminder / قبل الموعد بيوم**
  * **Two Hours Before / قبل الموعد بساعتين**
* **SMS Simulation:** Features a custom action button (`Simulate Reminder`) that simulates real-time patient notification dispatches directly within Odoo's chatter.

### 4. Operational Efficiency Tracker (`hi.operational.efficiency`)
* A dedicated dashboard to log operational issues, redundant testing, and waiting times.
* Maps process waste directly to a **Financial Loss field (SAR)** to measure the monetary impact of clinic inefficiencies.
* Integrated continuous improvement cycle tracking (`Draft` ➔ `Under Review` ➔ `Implemented`).

---

#🚀 Installation & Setup
Prerequisites
Docker Desktop installed on your machine.
Odoo 18 Community environment.
Deployment Steps
Clone/Copy the Module:
Place the hi_clinic directory directly inside your Odoo project's custom_addons folder.
Restart Odoo Server:
If you are using Docker, run the following command in your terminal to restart the web container:
Bash
   docker-compose restart web
Activate Developer Mode:
Log into Odoo as an Administrator.
Navigate to Settings, scroll to the bottom, and click Activate the developer mode.
Update App List & Install:
Go to the Apps menu.
Click Update Apps List from the top navigation bar.
Clear the default Apps filter in the search box, search for hi_clinic or العيادة الذكية, and click Activate.
🛠️ Technical Specifications
Odoo Version Compatibility: Modern Odoo 18.0 standards.
UI Views: Built entirely using updated modern Odoo 18 syntax (<list> instead of <tree>).
Security: Complete access rights configured inside ir.model.access.csv giving secure read/write privileges to clinic managers and users.
----

## 📂 Module Structure

```text
hi_clinic/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── appointment.py
│   ├── operational_efficiency.py
│   └── patient.py
├── security/
│   └── ir.model.access.csv
└── views/
    ├── appointment_views.xml
    ├── clinic_menus.xml
    ├── operational_efficiency_views.xml
    └── patient_views.xml
