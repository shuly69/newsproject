 // Registration form functionality
        document.addEventListener('DOMContentLoaded', function() {
            initRegistrationForm();
        });

        function initRegistrationForm() {
            const form = document.getElementById('registerForm');
            const passwordInput = document.getElementById('password');
            const confirmPasswordInput = document.getElementById('confirmPassword');

            // Password strength checker
            passwordInput.addEventListener('input', checkPasswordStrength);
            
            // Password confirmation checker
            confirmPasswordInput.addEventListener('input', checkPasswordMatch);

            // Form submission
            
        }

        function checkPasswordStrength() {
            const password = document.getElementById('password').value;
            const strengthFill = document.getElementById('strengthFill');
            const strengthText = document.getElementById('strengthText');

            let strength = 0;
            let feedback = '';

            if (password.length >= 8) strength += 1;
            if (/[a-z]/.test(password)) strength += 1;
            if (/[A-Z]/.test(password)) strength += 1;
            if (/[0-9]/.test(password)) strength += 1;
            if (/[^A-Za-z0-9]/.test(password)) strength += 1;

            const percentage = (strength / 5) * 100;
            strengthFill.style.width = percentage + '%';

            if (strength < 2) {
                strengthFill.className = 'strength-fill weak';
                feedback = 'Weak password';
            } else if (strength < 4) {
                strengthFill.className = 'strength-fill medium';
                feedback = 'Medium strength';
            } else {
                strengthFill.className = 'strength-fill strong';
                feedback = 'Strong password';
            }

            strengthText.textContent = feedback;
        }

        function checkPasswordMatch() {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const matchText = document.getElementById('matchText');

            if (confirmPassword.length === 0) {
                matchText.textContent = '';
                return;
            }

            if (password === confirmPassword) {
                matchText.textContent = '✓ Passwords match';
                matchText.className = 'match-text match';
            } else {
                matchText.textContent = '✗ Passwords do not match';
                matchText.className = 'match-text no-match';
            }
        }

        function togglePassword(fieldId) {
            const field = document.getElementById(fieldId);
            const toggle = field.parentElement.querySelector('.password-toggle i');
            
            if (field.type === 'password') {
                field.type = 'text';
                toggle.className = 'fas fa-eye-slash';
            } else {
                field.type = 'password';
                toggle.className = 'fas fa-eye';
            }
        }

   

        function validateRegistrationForm(data) {
            // Check if passwords match
            if (data.password !== document.getElementById('confirmPassword').value) {
                showNotification('Passwords do not match', 'error');
                return false;
            }

            // Check password strength
            if (data.password.length < 8) {
                showNotification('Password must be at least 8 characters long', 'error');
                return false;
            }

            // Check if email is valid
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(data.email)) {
                showNotification('Please enter a valid email address', 'error');
                return false;
            }

            // Check if terms are agreed
            if (!document.getElementById('agreeTerms').checked) {
                showNotification('Please agree to the terms and conditions', 'error');
                return false;
            }

            return true;
        }

        function showNotification(message, type) {
            // Create notification element
            const notification = document.createElement('div');
            notification.className = `notification notification-${type}`;
            notification.innerHTML = `
                <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
                <span>${message}</span>
            `;

            // Add to page
            document.body.appendChild(notification);

            // Show notification
            setTimeout(() => notification.classList.add('show'), 100);

            // Remove notification
            setTimeout(() => {
                notification.classList.remove('show');
                setTimeout(() => document.body.removeChild(notification), 300);
            }, 5000);
        }