function displayRandomChoice(fromThisArray, intoThisDomElementId) {
  let randomChoice =
    fromThisArray[Math.floor(Math.random() * fromThisArray.length)];
  document.getElementById(intoThisDomElementId).innerText = randomChoice;
  console.log(randomChoice);
}
