// Simple glowing effect for buttons
document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".nav-button");

  buttons.forEach(btn => {
    btn.addEventListener("mouseover", () => {
      btn.style.boxShadow = "0 0 15px #ffd98e";
    });
    btn.addEventListener("mouseout", () => {
      btn.style.boxShadow = "none";
    });
  });
});
