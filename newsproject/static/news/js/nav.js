document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    document.querySelectorAll(".nav a").forEach(link => {
      if (currentPath.includes(link.getAttribute("href"))) {
        link.parentElement.classList.add("active");
      }
    });
    
  });

function toggleUserMenu() {
            const dropdown = document.getElementById('userDropdown');
            dropdown.classList.toggle('show');
        }