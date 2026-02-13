function addMessage(text, sender) {
    let box = document.getElementById("chat-box");
    let div = document.createElement("div");
    div.className = sender;
    div.innerHTML = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

function sendMessage(msg=null) {
    let input = document.getElementById("user-input");
    let message = msg || input.value;

    if (message.trim() === "") return;

    addMessage(message, "user");
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.reply, "bot");
    });
}

function sendSuggestion(text) {
    sendMessage(text);
}
