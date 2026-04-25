# 🚀 Dev Portfolio

A modern, interactive personal portfolio website built with **Streamlit** showcasing projects, certifications, and technical expertise. This is a professional platform to highlight machine learning engineering, software development, and system design capabilities.

**Portfolio Owner:** Nimfa Mae A. Solasco  
**Focus Areas:** Machine Learning Engineer | Software Engineer | Pipeline Architecture

![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-FF4B4B?style=flat-square&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

### 🌐 **[View Live App](https://personalsiteee.streamlit.app/)** ← Click here to see the portfolio in action!

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Pages Overview](#pages-overview)
- [Deployment](#deployment)
- [Contact](#contact)

---

## ✨ Features

### 🏠 Core Functionality
- **Multi-page Portfolio Website** - 5 distinct pages for different content types
- **Interactive Dashboard** - Visual analytics of projects and impact metrics
- **Project Showcase** - Display of 5+ projects with GitHub integration
- **Certification Gallery** - Professional certifications display
- **Contact Form** - Direct messaging system with social links
- **Responsive Design** - Mobile-friendly dark theme interface
- **Custom Styling** - Modern CSS with glassmorphism effects

### 🎨 Design Highlights
- **Dark Mode Theme** - Easy on the eyes with professional aesthetics
- **Cyan/Blue Accents** - Modern color scheme (#38bdf8)
- **Glassmorphism Effects** - Backdrop blur on cards for visual depth
- **Smooth Transitions** - Hover animations and transformations
- **Wide Layout** - Optimized for desktop viewing

### 📊 Analytics & Visualization
- **Plotly Charts** - Interactive data visualizations
- **Project Impact Metrics** - Visual representation of project complexity and impact
- **Professional Dashboard** - Metrics and statistics view

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | [Streamlit](https://streamlit.io/) 1.28.1 |
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas 2.0.3 |
| **Visualization** | Plotly 5.17.0 |
| **Image Processing** | Pillow 10.0.0 |
| **Styling** | CSS3 with Backdrop Filters |
| **Data Format** | JSON |

---

## 📁 Project Structure

```
Portfolio_App/
│
├── 📄 README.md                      # Project documentation
├── 📄 requirements.txt               # Python dependencies
│
├── 📂 Portfolio_App/                 # Main application directory
│   │
│   ├── 🐍 app.py                     # Main entry point & configuration
│   │
│   ├── 📂 assets/                    # Static files & styling
│   │   ├── 🎨 styles.css            # Global CSS styling
│   │   ├── 🖼️  nymf.png             # Profile image
│   │   ├── 📜 Cert1.png             # Certification: Python Specialization
│   │   ├── 📜 Cert2.png             # Certification: ML Specialization
│   │   └── 📜 Cert3.png             # Certification: JavaScript Specialization
│   │
│   ├── 📂 pages/                     # Streamlit multi-page app pages
│   │   ├── 🏠 1_Home.py              # Home page - Profile & intro
│   │   ├── 💼 2_Projects.py          # Projects showcase
│   │   ├── 📊 3_Dashboard.py         # Analytics dashboard
│   │   ├── 📜 4_Certifications.py    # Certifications gallery
│   │   └── 📬 5_Contact.py           # Contact form & social links
│   │
│   ├── 📂 Components/               # Reusable UI components (expandable)
│   │   ├── 🧭 navbar.py             # Navigation component
│   │   ├── 📍 footer.py             # Footer component
│   │   ├── 🎴 project_card.py       # Project card component
│   │   └── ✨ animations.py         # Animation utilities
│   │
│   ├── 📂 data/                      # Data sources
│   │   └── 📋 projects.json          # Project data (5 projects)
│   │
│   └── 📂 utils/                     # Utility functions
│       ├── 🔄 data_loader.py        # Data loading utilities
│       └── 🛠️  helpers.py            # Helper functions
│
└── 📂 Documentation/
    └── 📄 REQUIREMENTS.md            # Detailed requirements doc

```

### Key Files Description

| File | Purpose |
|------|---------|
| `app.py` | Streamlit configuration, page setup, CSS loading |
| `styles.css` | Global styling with dark theme and animations |
| `projects.json` | Project data: title, description, tech stack, links |
| `1_Home.py` | Profile introduction and tech stack display |
| `2_Projects.py` | Displays all projects from JSON data |
| `3_Dashboard.py` | Analytics with Plotly visualizations |
| `4_Certifications.py` | Certification images gallery |
| `5_Contact.py` | Contact form and social media links |

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or Download the Repository**
   ```bash
   cd Portfolio_App
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Running Locally

```bash
# From the Portfolio_App directory
streamlit run app.py
```

The application will open at `http://localhost:8501`

### Navigation
- Use the **Streamlit sidebar** (hamburger menu) to navigate between pages
- All pages are numbered for easy identification:
  - 1️⃣ Home
  - 2️⃣ Projects
  - 3️⃣ Dashboard
  - 4️⃣ Certifications
  - 5️⃣ Contact

---

## 📄 Pages Overview

### 🏠 **Home Page** (`1_Home.py`)
Profile introduction highlighting expertise in:
- Machine Learning Pipeline Engineering
- System Optimization
- Production Integration
- Tech stack: PyTorch, Scikit-learn, TensorFlow, JavaScript, SQL, Plotly

**Features:**
- Profile image display
- Professional headline
- Comprehensive bio
- Tech stack showcase

---

### 💼 **Projects Page** (`2_Projects.py`)
Showcases 5 featured projects from `projects.json`

**Projects Featured:**
1. 🖥️ **CPU Instruction Cycle Simulator** - Fetch-decode-execute visualization
2. 🔧 **Compiler Design Simulator** - Lexical analysis & parsing
3. 🏦 **ATM Banking System V2** - OOP banking application
4. 📊 **Profiling System** - Youth analytics dashboard
5. 🌐 **Network Packet Flow Simulator** - OSI model visualization

**Features:**
- 2-column card layout
- Technology tags for each project
- Direct GitHub repository links
- Glassmorphic card design

---

### 📊 **Dashboard Page** (`3_Dashboard.py`)
Analytics and metrics visualization

**Features:**
- Project impact metrics
- Complexity analysis charts
- Plotly interactive visualizations
- Project performance overview

---

### 📜 **Certifications Page** (`4_Certifications.py`)
Professional certifications display

**Certifications:**
- 🎓 Python Specialization - 2026
- 🤖 Machine Learning Specialization - 2026
- 💻 JavaScript Specialization - 2026

**Features:**
- Full certification images with captions
- Year of certification
- Professional credential showcase

---

### 📬 **Contact Page** (`5_Contact.py`)
Communication and social media

**Social Links:**
- 🔗 [LinkedIn](https://www.linkedin.com/in/nimfa-solasco-b31a76405/)
- 💻 [GitHub](https://github.com/nimfaSol)
- 📘 [Facebook](https://www.facebook.com/nimfa.mae.solascoe)

**Contact Form:**
- Name input
- Email input
- Message textarea
- Form submission with success feedback

---

## 🎨 Design & Styling

### Color Palette
```css
Primary Background:    #0f172a → #020617 (gradient)
Text Color:           #e2e8f0 (light gray)
Primary Accent:       #38bdf8 (cyan)
Card Background:      rgba(30, 41, 59, 0.7) (semi-transparent)
Border Color:         #1e293b (dark slate)
```

### Key CSS Features
- **Glassmorphism:** Backdrop blur effects on cards
- **Hover Animations:** Cards lift on hover with glow effect
- **Smooth Transitions:** 0.3s transition timing
- **Responsive Layout:** Optimized for different screen sizes

---

## 🌐 Deployment

### Deployment Options

#### 1. **Streamlit Cloud** (Recommended)
- Free hosting platform specifically for Streamlit apps
- [Deploy on Streamlit Cloud](https://streamlit.io/cloud)
- Steps: Connect GitHub repo → Deploy

#### 2. **Heroku**
- Requires Procfile configuration
- Supports custom domains
- Small dynos available for free tier

#### 3. **Docker**
- Create Docker image for containerized deployment
- Deploy to AWS, Azure, or DigitalOcean

#### 4. **Self-Hosted**
- Deploy on personal server/VPS
- Use nginx/Apache as reverse proxy

### Environment Setup
Ensure `requirements.txt` is in root directory for automatic dependency installation during deployment.

---

## 📋 Project Data Format

### `projects.json` Structure
```json
[
  {
    "title": "Project Title",
    "description": "Detailed project description",
    "tech": ["Technology1", "Technology2", "Technology3"],
    "link": "https://github.com/username/repo"
  }
]
```

---

## 🔄 Development Roadmap

### Currently Implemented ✅
- Multi-page portfolio structure
- Responsive dark theme design
- Project showcase with GitHub integration
- Certification gallery
- Contact form UI
- Analytics dashboard

### Planned Enhancements 📋
- Email integration for contact form
- Form validation and error handling
- Reusable component system
- Animation transitions
- Mobile optimization
- Blog section
- Skills visualization
- Experience timeline

---

## 📞 Contact & Social

- **LinkedIn:** [Nimfa Solasco](https://www.linkedin.com/in/nimfa-solasco-b31a76405/)
- **GitHub:** [@nimfaSol](https://github.com/nimfaSol)
- **Facebook:** [Nimfa Mae Solasco](https://www.facebook.com/nimfa.mae.solascoe)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🎯 Quick Start

### 🌐 View Live
Visit the live app: **[https://personalsiteee.streamlit.app/](https://personalsiteee.streamlit.app/)**

### 🖥️ Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
streamlit run Portfolio_App/app.py

# 3. Open in browser
# http://localhost:8501
```

---

**Last Updated:** April 25, 2026  
**Version:** 1.0  
**Status:** Active Development
