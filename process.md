# Flask Concepts Explained Using Your Code

---

# 1. What is `@app.route()` ?

## Answer

`@app.route()` is used to connect a URL with a Python function. In Flask, one @app.route() decorator maps to one view function.

It tells Flask:

> "If this URL is requested, run this function."

---

# Example From Your Code

```python
@app.route("/", methods=["GET"])
def welcome():
    return "Hi Welcome"
```

---

# What Happens Internally

When browser opens:

```text
http://127.0.0.1:5000/
```

Flask checks:

```text
Which function is connected to "/"
```

It finds:

```python
def welcome():
```

Then executes:

```python
return "Hi Welcome"
```

Browser receives:

```text
Hi Welcome
```

---

# Simple Flow

```text
Browser Request
      ↓
URL = "/"
      ↓
Flask Route Matching
      ↓
welcome() function runs
      ↓
Response sent back
```

---

# Parameters of `app.route()`

## Basic Syntax

```python
@app.route(rule, options)
```

---

# Main Parameters

| Parameter | Meaning              |
| --------- | -------------------- |
| `rule`    | URL path             |
| `methods` | Allowed HTTP methods |

---

# Example

```python
@app.route("/form", methods=["GET","POST"])
```

| Part         | Meaning               |
| ------------ | --------------------- |
| `/form`      | URL                   |
| `GET`,`POST` | Allowed request types |

---

# 2. How Does Flask Connect With Frontend ?

## Answer

Frontend sends requests.

Flask receives requests.

Flask processes data and sends responses back.

---

# Complete Story Using Your Code

---

# Step 1 : Browser Opens Form Page

User opens:

```text
http://127.0.0.1:5000/form
```

Browser sends:

```text
GET request
```

---

# Step 2 : Flask Receives GET Request

Flask checks:

```python
@app.route("/form", methods=["GET","POST"])
```

It finds matching function:

```python
def form():
```

---

# Step 3 : GET Condition Runs

```python
if request.method == 'GET':
    return render_template("form.html")
```

Flask sends:

```text
form.html
```

to browser.

---

# Step 4 : Browser Displays HTML Form

Your frontend page appears.

```html
<form action="{{ url_for('form') }}" method="POST">
```

This means:

```text
When form submits,
send POST request to /form
```

---

# Step 5 : User Clicks Calculate

Browser sends:

```text
POST request
```

with form data:

```text
maths
science
history
```

---

# Step 6 : Flask Receives POST Request

This block runs:

```python
else:
```

Then:

```python
maths = float(request.form["maths"])
```

Flask extracts data from form.

---

# Step 7 : Flask Processes Data

```python
avg_marks = (maths+science+history) / 3
```

---

# Step 8 : Flask Decides Result

```python
if avg_marks >= 70:
```

Pass or fail decision happens.

---

# Step 9 : Flask Redirects User

```python
return redirect(url_for(res.__name__, score=avg_marks))
```

Browser gets redirected.

---

# Final Flow

```text
Frontend Form
      ↓
POST Request
      ↓
Flask Backend
      ↓
Data Processing
      ↓
Redirect
      ↓
Result Page
```

---

# 3. What is Variable Rule ?

## Answer

Variable rule allows dynamic values inside URL.

---

# Example From Your Code

```python
@app.route("/success/<int:score>")
```

---

# Meaning

```text
/success/85
```

Here:

```text
85
```

is dynamic value.

Flask stores it inside:

```python
score
```

---

# Example

If browser visits:

```text
/success/90
```

Flask executes:

```python
success(score=90)
```

---

# Why `<int:score>` ?

| Part    | Meaning       |
| ------- | ------------- |
| `int`   | datatype      |
| `score` | variable name |

---

# Supported Types

| Type     | Example   |
| -------- | --------- |
| `int`    | numbers   |
| `float`  | decimal   |
| `string` | text      |
| `path`   | full path |

---

# Example

```python
@app.route("/user/<string:name>")
def user(name):
    return f"Hello {name}"
```

URL:

```text
/user/Krittik
```

Output:

```text
Hello Krittik
```

---

# 4. What is URL Redirecting ?

## Answer

Redirect means:

> Send user automatically to another URL.

---

# Your Code

```python
return redirect(url_for(res.__name__, score=avg_marks))
```

---

# What Happens

Suppose average is:

```text
82
```

Flask chooses:

```python
res = success
```

Then:

```python
url_for(res.__name__, score=82)
```

creates:

```text
/success/82
```

Then:

```python
redirect()
```

sends browser there.

---

# Flow

```text
POST /form
      ↓
Calculate average
      ↓
Create URL
      ↓
Redirect browser
      ↓
Browser opens new page
```

---

# Why `url_for()` Is Used ?

Instead of writing hardcoded URL:

```python
"/success/82"
```

Flask generates URL automatically.

Safer and cleaner.

---

# Example

```python
url_for("success", score=82)
```

creates:

```text
/success/82
```

---

# 5. What is GET Request ?

## Answer

GET is used to:

```text
Request data or page from server
```

---

# Characteristics

| Feature                  | GET        |
| ------------------------ | ---------- |
| Sends data in URL        | Yes        |
| Used for fetching        | Yes        |
| Used for form submission | Usually No |
| Secure for passwords     | No         |

---

# Your Example

```python
@app.route("/form", methods=["GET"])
```

Browser asks:

```text
Give me form page
```

Server sends HTML page.

---

# Example URL

```text
/search?name=krittik
```

Data visible in URL.

---

# 6. What is POST Request ?

## Answer

POST is used to:

```text
Send data to server
```

Usually:

* forms
* login
* signup
* file upload

---

# Your Example

```html
<form method="POST">
```

When user clicks:

```text
Calculate
```

browser sends form data using POST.

---

# Flask Receives It

```python
request.form["maths"]
```

---

# Characteristics

| Feature              | POST |
| -------------------- | ---- |
| Sends data in body   | Yes  |
| Visible in URL       | No   |
| Used for submitting  | Yes  |
| Better for passwords | Yes  |

---

# 7. What is PUT Request ?

## Answer

PUT is mainly used in APIs.

Purpose:

```text
Update existing data completely
```

---

# Example

Suppose database contains:

```text
User ID = 5
Name = Rahul
```

PUT request:

```text
PUT /user/5
```

updates full user data.

---

# Difference

| Method | Purpose          |
| ------ | ---------------- |
| GET    | Fetch data       |
| POST   | Create/send data |
| PUT    | Update data      |
| DELETE | Remove data      |

---

# Real API Example

```python
@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    return "User Updated"
```

---

# 8. When To Use GET vs POST vs PUT ?

| Situation              | Method |
| ---------------------- | ------ |
| Open webpage           | GET    |
| Search data            | GET    |
| Submit form            | POST   |
| Login                  | POST   |
| Upload image           | POST   |
| Update profile         | PUT    |
| Update database record | PUT    |

---

# 9. What is Jinja Template Engine ?

## Answer

Jinja is the template engine used by Flask.

It allows Python data to be inserted inside HTML.

---

# Why Needed ?

Normal HTML is static.

Jinja makes HTML dynamic.

---

# Example From Your Code

```html
{{score}}
```

This is Jinja syntax.

---

# Meaning

Flask replaces:

```html
{{score}}
```

with actual value.

Example:

```html
82.3
```

---

# Another Example

```html
{{ url_for('form') }}
```

Jinja executes Flask function inside HTML.

It generates:

```text
/form
```

---

# Important Jinja Symbols

| Syntax  | Purpose     |
| ------- | ----------- |
| `{{ }}` | Print value |
| `{% %}` | Logic/loops |
| `{# #}` | Comments    |

---

# Example

```html
{% for i in range(5) %}
    <p>{{i}}</p>
{% endfor %}
```

Output:

```html
0
1
2
3
4
```

---

# Final Understanding of Your Project

Your application flow is:

```text
Browser
   ↓
GET /form
   ↓
Flask sends HTML
   ↓
User fills form
   ↓
POST /form
   ↓
Flask processes marks
   ↓
Redirects user
   ↓
Dynamic URL executes
   ↓
Result shown
```

Your project already demonstrates:

* routing
* GET request
* POST request
* Jinja templates
* form handling
* variable rules
* redirecting
* dynamic URLs

These are the core foundations of Flask.
