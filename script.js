const BASE_URL = "http://127.0.0.1:8000";

const output = document.getElementById("output");
const messageBox = document.getElementById("message");

// ---------------- Chat ----------------

async function chat() {

    const message = messageBox.value.trim();

    if (message === "") return;

    output.innerHTML += `
        <div class="user">${message}</div>
    `;

    messageBox.value = "";

    output.innerHTML += `
        <div class="bot" id="loading">
            🤖 Thinking...
        </div>
    `;

    output.scrollTop = output.scrollHeight;

    try {

        const response = await fetch(BASE_URL + "/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        document.getElementById("loading").remove();

        output.innerHTML += `
            <div class="bot">
                ${data.message}
            </div>
        `;

        output.scrollTop = output.scrollHeight;

    } catch (error) {

        document.getElementById("loading").remove();

        output.innerHTML += `
            <div class="bot">
                ❌ Unable to connect to backend.
            </div>
        `;

    }

}

// ---------------- HR Questions ----------------

async function hrQuestions() {

    const response = await fetch(BASE_URL + "/hr-questions");

    const data = await response.json();

    output.innerHTML += `
        <div class="bot">
            <b>HR Interview Questions</b><br><br>
            ${data.questions.join("<br><br>")}
        </div>
    `;

    output.scrollTop = output.scrollHeight;

}

// ---------------- Technical Questions ----------------

async function technicalQuestions() {

    const response = await fetch(BASE_URL + "/technical-questions");

    const data = await response.json();

    output.innerHTML += `
        <div class="bot">
            <b>Technical Questions</b><br><br>
            ${data.questions.join("<br><br>")}
        </div>
    `;

    output.scrollTop = output.scrollHeight;

}

// ---------------- Evaluate ----------------

async function evaluate() {

    const answer =