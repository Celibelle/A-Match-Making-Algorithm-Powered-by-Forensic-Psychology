// Floating sparkles
document.addEventListener("DOMContentLoaded", () => {
  for (let i = 0; i < 20; i++) createSparkle();
});

function createSparkle() {
  const sparkle = document.createElement("div");
  sparkle.className = "sparkle";
  sparkle.style.left = Math.random() * 100 + "vw";
  sparkle.style.animationDuration = 4 + Math.random() * 6 + "s";
  document.body.appendChild(sparkle);

  setTimeout(() => sparkle.remove(), 10000);
}
