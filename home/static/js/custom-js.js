const navLinks = document.querySelectorAll('.nav-link');
let currentNav = navLinks[0];
const navbar = document.querySelector('.navbar');

navLinks.forEach((nav) => nav.addEventListener('click', handleActive));

function handleActive(e) {
  e.preventDefault();
  if (currentNav !== e.target) {
    currentNav.classList.remove('active');
    currentNav = e.target;
    currentNav.classList.add('active');
  }
}

window.addEventListener('scroll', handleScroll);

function handleScroll() {
  if (window.scrollY > 150) {
    navbar.classList.add('fixed');
  } else {
    navbar.classList.remove('fixed');
  }
}