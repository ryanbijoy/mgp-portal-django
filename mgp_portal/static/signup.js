document.addEventListener("DOMContentLoaded", function() {
    const passwordField = document.getElementById("password");
    const confirmField = document.getElementById("confirm_password");

    const togglePassword = document.querySelector(".password-toggle-icon .eye-icon");
    const toggleConfirmPassword = document.querySelector(".confirm-password-toggle-icon .eye-icon");

    togglePassword.addEventListener("click", function () {
        if (passwordField.type === "password") {
            passwordField.type = "text";
            togglePassword.classList.remove("fa-eye");
            togglePassword.classList.add("fa-eye-slash");
        } else {
            passwordField.type = "password";
            togglePassword.classList.remove("fa-eye-slash");
            togglePassword.classList.add("fa-eye");
        }
    });

    toggleConfirmPassword.addEventListener("click", function () {
        if (confirmField.type === "password") {
            confirmField.type = "text";
            toggleConfirmPassword.classList.remove("fa-eye");
            toggleConfirmPassword.classList.add("fa-eye-slash");
        } else {
            confirmField.type = "password";
            toggleConfirmPassword.classList.remove("fa-eye-slash");
            toggleConfirmPassword.classList.add("fa-eye");
        }
    });
});
