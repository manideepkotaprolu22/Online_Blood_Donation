function registerDonor() {
    const name = document.getElementById("name");
    const age = document.getElementById("age");
    const gender = document.getElementById("gender");
    const blood_group = document.getElementById("blood_group");
    const city = document.getElementById("city");
    const phone = document.getElementById("phone");

    fetch("http://127.0.0.1:8000/donor/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("token")
        },
        body: JSON.stringify({
            name: name.value,
            age: parseInt(age.value),
            gender: gender.value,
            blood_group: blood_group.value,
            city: city.value,
            phone_number: parseInt(phone_number.value)
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        window.location.href = "role.html";
    });
}
