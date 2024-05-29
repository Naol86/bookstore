const navLinks = document.querySelectorAll(".nav-link");
let currentNav = navLinks[0];
const navbar = document.querySelector(".navbar");

navLinks.forEach((nav) => nav.addEventListener("click", handleActive));

function handleActive(e) {
  e.preventDefault();
  if (currentNav !== e.target) {
    currentNav.classList.remove("active");
    currentNav = e.target;
    currentNav.classList.add("active");
  }
}

window.addEventListener("scroll", handleScroll);

function handleScroll() {
  if (window.scrollY > 150) {
    navbar.classList.add("fixed");
  } else {
    navbar.classList.remove("fixed");
  }
}

const panels = document.querySelectorAll(".panel-n");
let prevActivePanel;
let prevActiveDescription;

panels.forEach((panel) => {
  panel.addEventListener("click", () => {
    const description = panel.querySelector(".school-description");

    if (prevActivePanel && prevActivePanel !== panel) {
      prevActivePanel.classList.remove("active-n");
      if (prevActiveDescription) {
        prevActiveDescription.classList.remove("expanded");
      }
    }

    panel.classList.toggle("active-n");
    description.classList.toggle("expanded");

    prevActivePanel = panel;
    prevActiveDescription = description;
  });
});



document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();
  var query = document.getElementById('searchInput').value;
  if (query) {
    window.location.href = "{% url 'search' %}?q=" + encodeURIComponent(query);
  }
});