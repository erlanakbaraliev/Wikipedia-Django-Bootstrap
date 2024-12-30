# **Wikipedia Application**

A simple web-based wikipedia application built with Django. This project demonstrates various key web development skills and features.

---

## **Skills Demonstrated**
1. **HTTP Request Handling**: Processing `GET` and `POST` requests in Django views.  
2. **Form Handling in Django**: Creating, validating, and pre-populating forms with `forms.Form`.  
3. **Template Rendering**: Rendering dynamic content using Django templates.  
4. **URL Routing**: Implementing dynamic routing with the `path()` function.  
5. **Markdown Conversion**: Converting Markdown to HTML using the `markdown` library.  
6. **Template Inheritance and Context Variables**: Building reusable templates with `{% extends %}` and `{% block %}`.  
7. **CSRF Protection**: Securing forms with `{% csrf_token %}`.

---

## **Features and Screenshots**

### 1. **All Pages**
View a list of all wiki entries.  
![All Pages](https://github.com/user-attachments/assets/7dce2bd0-e365-4a06-85f6-1aa040584c0c)

---

### 2. **Selected Page**
View the details of a selected wiki entry.  
![Selected Page](https://github.com/user-attachments/assets/3b995827-5f06-4f66-bf3b-444309365252)

---

### 3. **Edit Page**
Edit an existing wiki entry.  
![Edit Page](https://github.com/user-attachments/assets/cd2319c9-2fc2-4683-bb8d-4866a3b3c20b)

---

### 4. **Edit Result**
Preview the updated content after editing.  
![Edit Result](https://github.com/user-attachments/assets/9a2acaa1-0704-4cb1-b690-ecb403448e16)

---

### 5. **Search**
Search for wiki entries by name or keyword.  
![Search](https://github.com/user-attachments/assets/72056186-3056-4c9c-82ff-d68080f0dbd8)

---

### 6. **Search with Full Name**
Search by the full name to navigate directly to the page.  
![Search with Full Name](https://github.com/user-attachments/assets/f2a54332-7ec2-4d43-88a6-2841bcf99b49)

---

### 7. **Create a New Page**
Add a new wiki entry with a title and Markdown content.  
![Create a New Page](https://github.com/user-attachments/assets/99bd124f-e3f2-47b3-b64b-a5e6f7c18b31)

---

### 8. **Result of the Created Page**
View the newly created entry.  
![Result of the Created Page](https://github.com/user-attachments/assets/95e23a33-eeb8-41cb-bd0e-3fe17fad0fd3)

---

### 9. **Newly Created Page in All Pages**
See the newly created page listed among all entries.  
![Newly Created Page](https://github.com/user-attachments/assets/000ac96c-4430-438f-8689-7c5a789b743c)

---

## **Getting Started**

### Prerequisites
- Python 3.8 or higher
- Django 5.1 or higher

### Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/wiki-app.git
   cd wiki-app
   ```
2. Run the development server:  
   ```bash
   python manage.py runserver
   ```

### Usage
- Navigate to `http://127.0.0.1:8000` in your web browser.
- Explore, edit, create, and search for wiki entries.
