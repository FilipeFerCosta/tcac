function togglePasswordVisibility() {
    const passwordField = document.querySelector('input[name="password"]');
    const passwordToggleBtn = document.querySelector('.show-password-btn');

    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        passwordToggleBtn.textContent = 'Ocultar Senha';
    } else {
        passwordField.type = 'password';
        passwordToggleBtn.textContent = 'Mostrar Senha';
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('registerForm');

    form.addEventListener('submit', function(event) {
        const passwordField = document.querySelector('input[name="password"]');
        const password = passwordField.value;
        
        if (password.length < 6) {
            alert("A senha deve ter pelo menos 6 caracteres.");
            event.preventDefault();
        } else {
            alert("Cadastro realizado com sucesso!");
        }
    });
});
