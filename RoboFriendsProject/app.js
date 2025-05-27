const container = document.getElementById("cardContainer");
const searchBox = document.getElementById("searchBox");

function displayRobots(robotArray) {
  container.innerHTML = "";
  robotArray.forEach(robot => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <img src="${robot.image}" />
      <h2>${robot.name}</h2>
      <p>${robot.email}</p>
    `;
    container.appendChild(card);
  });
}

displayRobots(robots); // Initial anzeigen

searchBox.addEventListener("input", () => {
  const searchTerm = searchBox.value.toLowerCase();
  const filtered = robots.filter(robot =>
    robot.name.toLowerCase().includes(searchTerm)
  );
  displayRobots(filtered);
});
