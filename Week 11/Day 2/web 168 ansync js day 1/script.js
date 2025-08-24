/* fetch ✅ */

const URL = "https://jsonplaceholder.typicode.com/users";
const XML = "https://zvuch.github.io/emails.xml";

// let response = fetch(XML);

// console.log(response);

/*
  response.json() -> return promise
  response.text() -> return promise
*/

/*
response.then(res => {
  return res.text();
}).then(data => {
  console.log(data);
});
*/

function getUser(e) {
  e.preventDefault();
  console.log("submit the form");
  let userId = e.target.id.value;
  console.log("userId =", userId);

  // fetch(`${URL}?id=` + userId)
  fetch(`https://jsonplaceholder.typicode.com/users?id=${userId}`)
    .then(res => {
      return res.json();
    })
    .then(data => {
      console.log(data[0]);
      render(data[0]);
    })
    .catch(e => {
      console.log(e);
    });
}

function render(obj) {
  console.log(obj);
  const h2 = document.createElement("h2");
  const p = document.createElement("p");

  h2.textContent = obj.name;
  p.textContent = obj.username;

  const root = document.getElementById("root");
  root.appendChild(h2);
  root.appendChild(p);
}

function addPost(e) {
  e.preventDefault();

  let title = e.target.title.value;
  let body = e.target.body.value;
  let userId = e.target.userId.value;

  console.log(title, body, userId);

  fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      title,
      body,
      userId,
    }),
  })
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((e) => {
      console.log(e);
    });
}
