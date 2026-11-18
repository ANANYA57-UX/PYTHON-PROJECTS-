document.addEventListener("DOMContentLoaded", function () {
    const search = document.getElementById("search");
    const taskList = document.getElementById("task-list");
    const noResults = document.getElementById("no-results");
    const dueDate = document.getElementById("due_date");

    if (dueDate) {
        dueDate.min = new Date().toISOString().slice(0, 10);
    }

    if (!search || !taskList || !noResults) {
        return;
    }

    search.addEventListener("input", function () {
        const query = search.value.trim().toLocaleLowerCase();
        const tasks = taskList.querySelectorAll(".task-card");
        let visibleTasks = 0;

        tasks.forEach(function (task) {
            const matches = task.textContent.toLocaleLowerCase().includes(query);
            task.hidden = !matches;
            if (matches) {
                visibleTasks += 1;
            }
        });

        noResults.hidden = visibleTasks > 0 || tasks.length === 0;
    });
});
