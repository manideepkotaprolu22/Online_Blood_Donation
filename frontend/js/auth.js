const API = "http://127.0.0.1:8000";

function signup() {
    fetch(`${API}/signup`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    }).then(() => window.location.href = "login.html");
}

function login() {
    fetch(`${API}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
    .then(res => res.json())
    .then(data => {
        localStorage.setItem("token", data.access_token);
        window.location.href = "role.html";
    });
}
