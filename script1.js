const age = document.getElementById("age").value;

if (!age || parseInt(age) <= 0) {
  alert("Please enter a valid age before continuing.");
  return;
}
document.getElementById("predictForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const age = document.getElementById("age").value;

  if (!age || parseInt(age) <= 0) {
    alert("Please enter a valid age before continuing.");
    return;
  }

  window.location.href = "predict.html";
});
const button = document.querySelector("button[type='submit']");
button.textContent = "Redirecting...";
button.disabled = true;

