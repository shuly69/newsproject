document.addEventListener("DOMContentLoaded", function () {
    initMobileMenu()
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


function initMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.nav');
    
    if (mobileToggle && nav) {
        mobileToggle.addEventListener('click', function() {
            nav.classList.toggle('mobile-open');
            const icon = this.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });
    }
}
