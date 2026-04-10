

const API = "";

async function fetchTasks() {
  const res = await fetch(`${API}/tasks`);
  const tasks = await res.json();

  const list = document.getElementById("taskList");
  list.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.innerHTML = `
      ${task.title} - ${task.completed ? "✅" : "❌"}
      <button onclick="completeTask('${task.id}')">Complete</button>
    `;
    list.appendChild(li);
  });
}

async function addTask() {
  const input = document.getElementById("taskInput");

  await fetch(`${API}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: input.value })
  });

  input.value = "";
  fetchTasks();
}

async function completeTask(id) {
  await fetch(`${API}/tasks/${id}/complete`, {
    method: "PUT"
  });

  fetchTasks();
}

async function deleteCompletedTasks() {
  await fetch(`${API}/tasks/completed`, {
    method: "DELETE"
  });

  fetchTasks();
}

fetchTasks();