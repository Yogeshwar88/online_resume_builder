# Resume Builder Website

A web-based Resume Builder that allows users to register, log in, and choose between multiple professional resume templates.  
This project is built using **HTML**, **CSS**, and **JavaScript** with **Local Storage** for user authentication (no backend required).

---

## 🚀 Features

- 🧾 **Three Resume Templates**:
  - Basic Resume
  - Standard Resume
  - Modern Resume

- 🔐 **User Authentication**:
  - Register and Login functionality.
  - Credentials (email and password) stored safely in the browser's Local Storage.
  - Dynamic Login/Logout button shown based on user status.

- 🎨 **Attractive and Responsive UI**:
  - Modern gradient backgrounds.
  - Professional, clean layout with responsive design.
  - Styled buttons, hover effects, and dynamic content loading.

- ⚡ **Session Management**:
  - User session maintained using `loggedIn` and `currentUser` flags in Local Storage.
  - Logout option clears the session and resets the homepage.

---

## 📁 Project Structure

---

## 🛠 How it Works

1. **Registration**:
   - New users can create an account using an email and password.
   - Their details are saved inside the browser’s Local Storage.

2. **Login**:
   - Existing users can log in.
   - If credentials match Local Storage, they are redirected to the homepage.

3. **Session Control**:
   - After login, a Logout button appears.
   - On logout, Local Storage is cleared and the homepage refreshes.

---

## 📋 Technologies Used

- HTML5
- CSS3 (inline styles + media queries)
- JavaScript (LocalStorage APIs)

---

## 📸 Screenshots

| Screen | Preview |
|:------|:---------|
| Login Page | ![Login](img/login-preview.png) |
| Home Page with Templates | ![Homepage](img/home-preview.png) |
| Responsive Design | ![Responsive](img/mobile-preview.png) |

---

## ⚠️ Important Notes

- This project uses **Local Storage** for saving user details — it's suitable for **demo**, **portfolio**, or **personal use only**.
- **Not recommended for production** use where sensitive information is involved.
- For production-level authentication, implement a proper backend system (PHP, Node.js, Firebase, etc).

---

## ✨ Future Improvements

- Add option to edit/save resumes.
- Allow users to download their resume as a **PDF**.
- Secure user data with encrypted storage.
- Add admin panel for managing user profiles.

---

## 🙌 Acknowledgments

Developed and designed by **Likhitha MR** as a part of a learning project on web development and resume building applications.

---

## 📢 License

This project is open source and free to use for educational purposes.



