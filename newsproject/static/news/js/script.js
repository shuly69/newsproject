// News Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initViewToggle();
    initSearch();
    initMobileMenu();
    initNewsletter();
    initLoadMore();
    initSmoothScrolling();
});

// View Toggle Functionality (Grid/List)
function initViewToggle() {
    const toggleButtons = document.querySelectorAll('.toggle-btn');
    const newsGrid = document.getElementById('newsGrid');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const view = this.dataset.view;
            
            // Remove active class from all buttons
            toggleButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Toggle grid/list view
            if (view === 'list') {
                newsGrid.classList.add('list-view');
            } else {
                newsGrid.classList.remove('list-view');
            }
        });
    });
}

// Search Functionality
function initSearch() {
    const searchInput = document.querySelector('.search-input');
    const searchBtn = document.querySelector('.search-btn');
    
    function performSearch() {
        const query = searchInput.value.trim();
        if (query) {
            // In a real application, this would make an API call
            console.log('Searching for:', query);
            // For demo purposes, we'll just show an alert
            alert(`Searching for: "${query}"`);
        }
    }
    
    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

// Mobile Menu Toggle
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

// Newsletter Subscription
function initNewsletter() {
    const newsletterForms = document.querySelectorAll('.newsletter-form, .footer-newsletter');
    
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            
            if (email) {
                // In a real application, this would send the email to a server
                console.log('Newsletter subscription:', email);
                alert('Thank you for subscribing to our newsletter!');
                this.reset();
            }
        });
    });
}

// Load More Articles
function initLoadMore() {
    const loadMoreBtn = document.querySelector('.load-more .btn');
    
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            // Simulate loading more articles
            this.textContent = 'Loading...';
            this.disabled = true;
            
            setTimeout(() => {
                // In a real application, this would load more articles from an API
                console.log('Loading more articles...');
                alert('More articles loaded!');
                this.textContent = 'Load More Articles';
                this.disabled = false;
            }, 1000);
        });
    }
}

// Smooth Scrolling for Anchor Links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Category Filtering (for category page)
function filterByCategory(category) {
    const articles = document.querySelectorAll('.news-card');
    
    articles.forEach(article => {
        const articleCategory = article.querySelector('.category-badge').textContent.toLowerCase();
        
        if (category === 'all' || articleCategory === category) {
            article.style.display = 'block';
        } else {
            article.style.display = 'none';
        }
    });
}

// Article Reading Time Calculator
function calculateReadingTime(text) {
    const wordsPerMinute = 200;
    const wordCount = text.split(' ').length;
    const readingTime = Math.ceil(wordCount / wordsPerMinute);
    return readingTime;
}

// Share Article Functionality
function shareArticle(title, url) {
    if (navigator.share) {
        navigator.share({
            title: title,
            url: url
        });
    } else {
        // Fallback for browsers that don't support Web Share API
        const shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}`;
        window.open(shareUrl, '_blank');
    }
}

// Bookmark Article
function bookmarkArticle(articleId) {
    let bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
    
    if (bookmarks.includes(articleId)) {
        bookmarks = bookmarks.filter(id => id !== articleId);
        console.log('Article removed from bookmarks');
    } else {
        bookmarks.push(articleId);
        console.log('Article bookmarked');
    }
    
    localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
}

// Dark Mode Toggle (if needed)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

// Initialize dark mode from localStorage
function initDarkMode() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
    }
}

// Image Lazy Loading
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Form Validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('error');
            isValid = false;
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// Toast Notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 3000);
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initDarkMode();
    initLazyLoading();
});

// Utility Functions
const utils = {
    // Format date
    formatDate: function(date) {
        return new Intl.DateTimeFormat('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        }).format(new Date(date));
    },
    
    // Truncate text
    truncateText: function(text, maxLength) {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    },
    
    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};




// Export functions for use in other files
window.NewsWebsite = {
    filterByCategory,
    shareArticle,
    bookmarkArticle,
    toggleDarkMode,
    validateForm,
    showToast,
    utils,
};
