
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const emailText = document.getElementById("mensagem");
  const copyBtn = document.getElementById("copyBtn");
  const copyFeedback = document.getElementById("copyFeedback");
  const suggestedResponse = document.getElementById("suggestedResponse");
  const charCount = document.createElement("small");
  charCount.classList.add("text-muted", "d-block", "mb-2");
  emailText.parentNode.appendChild(charCount);

  // Atualiza contador de caracteres
  emailText.addEventListener("input", () => {
    const length = emailText.value.length;
    charCount.textContent = `Caracteres digitados: ${length}`;
  });

  // Copiar resposta
  if (copyBtn) {
    copyBtn.addEventListener("click", async () => {
      const text = suggestedResponse.innerText;
      try {
        await navigator.clipboard.writeText(text);
        copyFeedback.classList.remove("d-none");
        setTimeout(() => copyFeedback.classList.add("d-none"), 1500);
      } catch (e) {
        alert("Não foi possível copiar. :(");
      }
    });
  }

  // Efeito fade-in no resultado
  const resultCard = document.querySelector(".card.shadow-sm + .card.shadow-sm");
  if (resultCard) {
    resultCard.style.opacity = 0;
    resultCard.style.transition = "opacity 0.8s ease-in-out";
    setTimeout(() => {
      resultCard.style.opacity = 1;
      // Scroll suave até o resultado
      resultCard.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 100);
  }

  // Animação de badge (Produtivo / Improdutivo)
  const badge = document.querySelector(".card .badge");
  if (badge) {
    badge.style.transition = "all 0.5s ease";
    if (badge.textContent.trim() === "Produtivo") {
      badge.classList.remove("text-bg-secondary");
      badge.classList.add("text-bg-success");
    } else {
      badge.classList.remove("text-bg-success");
      badge.classList.add("text-bg-secondary");
    }
  }


});
