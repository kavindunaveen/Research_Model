// You can add interactivity to the table if necessary
document.addEventListener('DOMContentLoaded', function () {
    // Example: Highlight rows on hover
    const rows = document.querySelectorAll("table tbody tr");

    rows.forEach(row => {
        row.addEventListener('mouseover', function () {
            row.style.backgroundColor = "#f0f0f0"; // Light gray on hover
        });
        row.addEventListener('mouseout', function () {
            row.style.backgroundColor = ""; // Reset background color
        });
    });

    // Example: Show alert on button click
    const alertButton = document.getElementById('showAlertButton');
    if (alertButton) {
        alertButton.addEventListener('click', function () {
            alert('Alert triggered from JS!');
        });
    }
});
