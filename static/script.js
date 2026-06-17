async function sendMessage() {

    let input = document.getElementById("user-input");
    let message = input.value;

    if(message === "") return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += "<p><b>You:</b> " + message + "</p>";

    input.value = "";

    const response = await fetch("/chat", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message
        })
    });

    const data = await response.json();

    chatBox.innerHTML += "<p><b>AI:</b> " + data.reply + "</p>";

    chatBox.scrollTop = chatBox.scrollHeight;
}
