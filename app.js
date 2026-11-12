const form = document.querySelector("#task-form");
const titleInput = document.querySelector("#task-title");
const taskList = document.querySelector("#task-list");
const statusMessage = document.querySelector("#task-status");
const taskCount = document.querySelector("#task-count");

function showMessage(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("is-error", isError);
}

async function apiRequest(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const result = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(result.error || "İşlem tamamlanamadı.");
  }
  return result;
}

function makeTaskItem(task) {
  const item = document.createElement("li");
  item.className = "task-item";
  item.dataset.id = task.id;

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = task.completed;
  checkbox.dataset.action = "toggle";
  checkbox.setAttribute(
    "aria-label",
    task.completed ? "Görevi tamamlanmadı olarak işaretle" : "Görevi tamamlandı olarak işaretle"
  );

  const title = document.createElement("span");
  title.className = task.completed ? "task-title is-complete" : "task-title";
  title.textContent = task.title;

  const removeButton = document.createElement("button");
  removeButton.type = "button";
  removeButton.className = "task-delete";
  removeButton.dataset.action = "delete";
  removeButton.textContent = "Sil";
  removeButton.setAttribute("aria-label", task.title + " görevini sil");

  item.append(checkbox, title, removeButton);
  return item;
}

function renderTasks(tasks) {
  taskList.replaceChildren();
  taskCount.textContent = tasks.length + (tasks.length === 1 ? " görev" : " görev");

  if (tasks.length === 0) {
    const empty = document.createElement("li");
    empty.className = "task-empty";
    empty.textContent = "Henüz görev yok. İlk görevi sen ekle.";
    taskList.append(empty);
    return;
  }

  tasks.forEach((task) => taskList.append(makeTaskItem(task)));
}

async function loadTasks() {
  try {
    const result = await apiRequest("/api/tasks");
    renderTasks(result.tasks);
  } catch (error) {
    showMessage(error.message + " Uygulamayı Flask sunucusundan açtığından emin ol.", true);
    taskList.replaceChildren();
    taskCount.textContent = "Bağlantı yok";
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const title = titleInput.value.trim();
  if (!title) {
    showMessage("Görev başlığını yaz.", true);
    return;
  }

  const submitButton = form.querySelector("button");
  submitButton.disabled = true;
  try {
    await apiRequest("/api/tasks", {
      method: "POST",
      body: JSON.stringify({ title }),
    });
    titleInput.value = "";
    showMessage("Görev SQLite veritabanına kaydedildi.");
    await loadTasks();
    titleInput.focus();
  } catch (error) {
    showMessage(error.message, true);
  } finally {
    submitButton.disabled = false;
  }
});

taskList.addEventListener("change", async (event) => {
  if (event.target.dataset.action !== "toggle") return;
  const item = event.target.closest(".task-item");
  try {
    await apiRequest("/api/tasks/" + item.dataset.id, {
      method: "PATCH",
      body: JSON.stringify({ completed: event.target.checked }),
    });
    showMessage("Görev durumu güncellendi.");
    await loadTasks();
  } catch (error) {
    showMessage(error.message, true);
    await loadTasks();
  }
});

taskList.addEventListener("click", async (event) => {
  if (event.target.dataset.action !== "delete") return;
  const item = event.target.closest(".task-item");
  try {
    await apiRequest("/api/tasks/" + item.dataset.id, { method: "DELETE" });
    showMessage("Görev silindi.");
    await loadTasks();
  } catch (error) {
    showMessage(error.message, true);
  }
});

loadTasks();
