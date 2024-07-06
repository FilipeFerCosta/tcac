document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    const hamburger = document.querySelector('.hamburger');
    const navbar = document.querySelector('.navbar');
  
    hamburger.addEventListener('click', function() {
        sidebar.classList.toggle('active');
        content.classList.toggle('with-sidebar');
        navbar.classList.toggle('with-navbar-sidebar'); // Adiciona a classe ao navbar
        hamburger.classList.toggle('active');
    });
  
    document.addEventListener('click', function(event) {
        const isClickInsideSidebar = event.target.closest('.sidebar');
        const isClickInsideHamburger = event.target.closest('.hamburger');
        if (!isClickInsideSidebar && !isClickInsideHamburger) {
            sidebar.classList.remove('active');
            content.classList.remove('with-sidebar');
            navbar.classList.remove('with-navbar-sidebar'); // Remove a classe do navbar
            hamburger.classList.remove('active');
        }
    });
  });
  