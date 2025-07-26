# 📚 Moral Stories Blog

A beautiful, responsive Django blog platform dedicated to sharing inspiring moral stories that teach valuable life lessons and promote good values. This project combines modern web design with timeless wisdom to create an engaging storytelling experience.

## ✨ Features

### 🎨 **Modern Design**
- Beautiful responsive design with gradient backgrounds
- Professional card-based layout
- Mobile-first approach with Bootstrap integration
- Smooth animations and hover effects

### 📱 **Responsive Experience**
- Mobile-friendly navigation with hamburger menu
- Touch-optimized interface
- Responsive images with proper centering
- Adaptive layouts for all screen sizes

### 📝 **Content Management**
- Rich blog post management
- Image upload and optimization
- Category and tag system
- SEO-friendly URLs
- Admin dashboard integration

### 📞 **Contact System**
- Professional contact form with validation
- Multiple contact methods
- Social media integration
- Newsletter subscription
- FAQ section

## 🚀 Live Demo

[View Live Demo](your-demo-link-here) 

## 🛠️ Technology Stack

- **Backend:** Django 4.2+
- **Frontend:** HTML5, CSS3, JavaScript 
- **Styling:** Bootstrap 5 + Custom CSS
- **Database:** SQLite (development) 
- **Icons:** Font Awesome 6
- **Fonts:** Google Fonts (Playfair Display, Inter)

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Virtual environment (recommended)

## ⚡ Quick Start

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
``

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 7. Run Development Server
```bash
python manage.py runserver
```

## 📁 Project Structure

```
moral-stories-blog/
├── blog/                   # Main Django app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── about.html      # About page
│   │   ├── contact.html    # Contact page
│   │   ├── index.html      # Homepage
│   │   └── search_results.html # Search results
│   ├── static/            # Static files
│   │   ├── css/           # Stylesheets
│   │   ├── js/            # JavaScript files
│   │   └── images/        # Image assets
│   ├── admin.py           # Admin configuration
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL patterns
│   └── forms.py           # Django forms
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file
```

**Made with ❤️ for sharing moral wisdom and inspiring stories**
