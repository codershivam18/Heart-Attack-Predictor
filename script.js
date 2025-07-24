document.getElementById("predictForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const age = parseInt(document.getElementById("age").value);
  const cholesterol = parseInt(document.getElementById("cholesterol").value);
  const bp = parseInt(document.getElementById("bp").value);
  const hr = parseInt(document.getElementById("hr").value);
  const resultDiv = document.getElementById("result");

  // Input validation
  if (isNaN(age) || isNaN(cholesterol) || isNaN(bp) || isNaN(hr)) {
    resultDiv.textContent = "❌ Please fill out all fields correctly.";
    resultDiv.style.color = "black";
    return;
  }

  // Reset
  resultDiv.style.color = "";
  resultDiv.style.fontWeight = "bold";

  // Simple rule-based logic
  let risk = 0;
  if (age > 50) risk++;
  if (cholesterol > 240) risk++;
  if (bp > 140) risk++;
  if (hr > 100) risk++;

  let prediction;
  if (risk >= 3) {
    prediction = "⚠️ High Risk of Heart Issue";
    resultDiv.style.color = "red";
  } else if (risk === 2) {
    prediction = "⚠️ Moderate Risk";
    resultDiv.style.color = "orange";
  } else {
    prediction = "✅ Low Risk";
    resultDiv.style.color = "green";
  }

  resultDiv.textContent = prediction;
});
resultDiv.textContent = "⏳ Analyzing...";
setTimeout(() => {
  // logic and result here
}, 800);
