// your_app/static/your_app/admin_geolocation.js
document.addEventListener("DOMContentLoaded", function () {
  const latInput = document.getElementById("id_latitude");
  const lonInput = document.getElementById("id_longitude");

  if (latInput && lonInput) {
    // Create the button
    const btn = document.createElement("button");
    btn.type = "button";
    btn.innerText = "📍 Use My Current Location";
    btn.style.marginTop = "5px";
    btn.classList.add("button", "default"); // Django admin style

    // Insert button after latitude input
    latInput.parentNode.appendChild(btn);

    btn.addEventListener("click", function () {
      if (!navigator.geolocation) {
        alert("❌ Geolocation is not supported by your browser.");
        return;
      }

      btn.innerText = "Fetching location...";
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const { latitude, longitude } = pos.coords;
          latInput.value = latitude.toFixed(6);
          lonInput.value = longitude.toFixed(6);
          btn.innerText = "📍 Location Updated";
          btn.style.backgroundColor = "#d4edda";
        },
        (err) => {
          alert("❌ Unable to fetch location. Please allow permission.");
          console.error(err);
          btn.innerText = "📍 Use My Current Location";
        }
      );
    });
  }
});
