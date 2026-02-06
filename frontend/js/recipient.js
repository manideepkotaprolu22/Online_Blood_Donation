const filterCity = document.getElementById("filterCity");
const filterBlood = document.getElementById("filterBlood");
const donorTable = document.getElementById("donorTable");

function loadDonors() {
    const city = filterCity.value;
    const blood = filterBlood.value;

    let url = "http://127.0.0.1:8000/donors?";
    if (city) url += `city=${city}&`;
    if (blood) url += `blood_group=${blood}`;

    fetch(url)
        .then(res => res.json())
        .then(data => {
            donorTable.innerHTML = "";

            const cities = new Set();
            const bloodGroups = new Set();

            data.forEach(d => {
                donorTable.innerHTML += `
                <tr>
                    <td>${d.name}</td>
                    <td>${d.blood_group}</td>
                    <td>${d.city}</td>
                    <td>${d.phone_number}</td>
                </tr>`;

                cities.add(d.city);
                bloodGroups.add(d.blood_group);
            });

            populateFilters(cities, bloodGroups);
        });
}

function populateFilters(cities, bloodGroups) {
    filterCity.innerHTML = `<option value="">All Cities</option>`;
    filterBlood.innerHTML = `<option value="">All Blood Groups</option>`;

    cities.forEach(city => {
        filterCity.innerHTML += `<option value="${city}">${city}</option>`;
    });

    bloodGroups.forEach(bg => {
        filterBlood.innerHTML += `<option value="${bg}">${bg}</option>`;
    });
}

/* ✅ Load immediately */
window.onload = loadDonors;
