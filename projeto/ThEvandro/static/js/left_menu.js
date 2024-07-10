document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    const hamburger = document.querySelector('.hamburger');
    const navbar = document.querySelector('.navbar');

    // Função para fechar a sidebar se o clique for fora dela ou do hamburger
    function closeSidebarIfClickOutside(event) {
        const isClickInsideSidebar = event.target.closest('.sidebar');
        const isClickInsideHamburger = event.target.closest('.hamburger');
        if (!isClickInsideSidebar && !isClickInsideHamburger) {
            sidebar.classList.remove('active');
            content.classList.remove('with-sidebar');
            navbar.classList.remove('with-navbar-sidebar');
            hamburger.classList.remove('active');
        }
    }

    // Adiciona o evento de clique no hamburger
    hamburger.addEventListener('click', function() {
        sidebar.classList.toggle('active');
        content.classList.toggle('with-sidebar');
        navbar.classList.toggle('with-navbar-sidebar');
        hamburger.classList.toggle('active');
    });

    // Inicializa a sidebar como fechada ao carregar a página
    sidebar.classList.remove('active');
    content.classList.remove('with-sidebar');
    navbar.classList.remove('with-navbar-sidebar');
    hamburger.classList.remove('active');

    // Executa a função para fechar a sidebar ao carregar a página
    closeSidebarIfClickOutside();

    // Adiciona o evento de clique no documento para fechar a sidebar
    document.addEventListener('click', closeSidebarIfClickOutside);
});
