var form_input = d3.select("");
var button_input = d3.select("");

form_input.on("submit", handleInput());
button_input.on("click", handleInput());

function handleInput() {
    // Call model from python file and feed in user's text input
    var text_input = form_input.property("value");
};