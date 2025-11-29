// ✨ Gentle glow animation for Mystic Enchantress pages

document.addEventListener("DOMContentLoaded", () => {
  const glowTargets = document.querySelectorAll("h1, h2, a, .cta-button");

  glowTargets.forEach(el => {
    el.style.transition = "0.8s";
    el.addEventListener("mouseover", () => {
      el.style.textShadow = "0 0 15px #ffb3ff";
    });
    el.addEventListener("mouseout", () => {
      el.style.textShadow = "none";
    });
  });
});